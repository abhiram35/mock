from __future__ import annotations

import subprocess
import tempfile
import time
from pathlib import Path

from app.enums.coding_language import CodingLanguage
from app.models.coding_question import CodingQuestion
from app.schemas.code_execution import (
    CodeExecutionResponse,
    TestCaseResult,
)


class CodeExecutionService:
    """
    Executes candidate code inside an isolated Docker container.
    """

    TIMEOUT_SECONDS = 5

    MEMORY_LIMIT = "128m"

    CPU_LIMIT = "0.5"

    LANGUAGE_CONFIG = {
        CodingLanguage.PYTHON: {
            "image": "python:3.12-slim",
            "filename": "main.py",
            "command": [
                "python",
                "/code/main.py",
            ],
        },
        CodingLanguage.JAVASCRIPT: {
            "image": "node:20-slim",
            "filename": "main.js",
            "command": [
                "node",
                "/code/main.js",
            ],
        },
        CodingLanguage.JAVA: {
            "image": "openjdk:21-slim",
            "filename": "Main.java",
            "command": [
                "sh",
                "-c",
                "javac -d /tmp /code/Main.java && java -cp /tmp Main",
            ],
        },
        CodingLanguage.CPP: {
            "image": "gcc:latest",
            "filename": "main.cpp",
            "command": [
                "sh",
                "-c",
                "g++ -O2 /code/main.cpp -o /tmp/main && /tmp/main",
            ],
        },
    }

    def _resolve_language(
        self,
        question: CodingQuestion,
        language_override: CodingLanguage | str | None = None,
    ) -> CodingLanguage:
        target = language_override or question.language
        if isinstance(target, str):
            try:
                target = CodingLanguage(target.lower())
            except ValueError:
                raise ValueError(f"Unsupported coding language: {target}")
        return target

    def run_visible(
        self,
        question: CodingQuestion,
        code: str,
        language: CodingLanguage | str | None = None,
    ) -> CodeExecutionResponse:
        """
        Execute candidate code against visible test cases only (is_hidden=False).
        Returns full input, expected output, and actual output for candidate debugging.
        """
        resolved_language = self._resolve_language(question, language)

        if not question.test_cases:
            raise ValueError(
                "No test cases are configured for this coding question."
            )

        visible_cases = [tc for tc in question.test_cases if not tc.is_hidden]
        cases_to_run = visible_cases if visible_cases else question.test_cases

        return self._execute_cases(
            question=question,
            cases=cases_to_run,
            code=code,
            language=resolved_language,
            mask_hidden=False,
        )

    def submit(
        self,
        question: CodingQuestion,
        code: str,
        language: CodingLanguage | str | None = None,
    ) -> CodeExecutionResponse:
        """
        Execute candidate code against ALL test cases (visible and hidden).
        For hidden test cases, never reveals input_data, expected_output, or actual_output.
        """
        resolved_language = self._resolve_language(question, language)

        if not question.test_cases:
            raise ValueError(
                "No test cases are configured for this coding question."
            )

        return self._execute_cases(
            question=question,
            cases=question.test_cases,
            code=code,
            language=resolved_language,
            mask_hidden=True,
        )

    def execute(
        self,
        question: CodingQuestion,
        code: str,
        language: CodingLanguage | str | None = None,
    ) -> CodeExecutionResponse:
        """
        Default execution method maintained for backward compatibility.
        Executes against visible test cases.
        """
        return self.run_visible(question, code, language)

    def _execute_cases(
        self,
        question: CodingQuestion,
        cases: list,
        code: str,
        language: CodingLanguage,
        mask_hidden: bool,
    ) -> CodeExecutionResponse:
        if language not in self.LANGUAGE_CONFIG:
            raise ValueError(
                f"Code execution for {language.value} is not available yet."
            )

        config = self.LANGUAGE_CONFIG[language]
        results: list[TestCaseResult] = []
        passed_count = 0

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            source_file = temp_path / config["filename"]
            source_file.write_text(code, encoding="utf-8")

            for index, test_case in enumerate(cases, start=1):
                is_hidden = bool(test_case.is_hidden)
                mask_this_case = mask_hidden and is_hidden

                result = self._run_test_case(
                    source_file=source_file,
                    input_data=test_case.input_data,
                    expected_output=test_case.expected_output,
                    index=index,
                    config=config,
                    is_hidden=is_hidden,
                    mask_details=mask_this_case,
                )

                results.append(result)

                if result.passed:
                    passed_count += 1

        total = len(results)

        return CodeExecutionResponse(
            success=passed_count == total,
            language=language.value,
            total_test_cases=total,
            passed_test_cases=passed_count,
            failed_test_cases=total - passed_count,
            results=results,
        )

    def _run_test_case(
        self,
        source_file: Path,
        input_data: str,
        expected_output: str,
        index: int,
        config: dict,
        is_hidden: bool = False,
        mask_details: bool = False,
    ) -> TestCaseResult:
        """
        Run one test case inside Docker.
        """
        command = [
            "docker",
            "run",
            "--rm",
            "--network",
            "none",
            "--memory",
            self.MEMORY_LIMIT,
            "--cpus",
            self.CPU_LIMIT,
            "--pids-limit",
            "64",
            "--read-only",
            "--tmpfs",
            "/tmp:rw,exec,nosuid,size=64m",
            "-v",
            f"{source_file.parent}:/code:ro",
            config["image"],
        ]

        command.extend(config["command"])

        start_time = time.perf_counter()

        try:
            process = subprocess.run(
                command,
                input=input_data,
                text=True,
                capture_output=True,
                timeout=self.TIMEOUT_SECONDS,
                check=False,
            )

            execution_time_ms = (
                time.perf_counter() - start_time
            ) * 1000

            actual_output = process.stdout.strip()
            expected = expected_output.strip()

            if process.returncode != 0:
                raw_error = (
                    process.stderr.strip()
                    or "Code execution failed."
                )

                error_msg = (
                    "Execution error on hidden test case."
                    if mask_details
                    else raw_error
                )

                return TestCaseResult(
                    test_case_number=index,
                    passed=False,
                    input_data=None if mask_details else input_data,
                    expected_output=None if mask_details else expected,
                    actual_output=None if mask_details else actual_output,
                    is_hidden=is_hidden,
                    error=error_msg,
                    execution_time_ms=execution_time_ms,
                )

            passed = (actual_output == expected)

            error_msg = None
            if not passed:
                error_msg = (
                    "Hidden test case failed."
                    if mask_details
                    else "Output does not match expected output."
                )

            return TestCaseResult(
                test_case_number=index,
                passed=passed,
                input_data=None if mask_details else input_data,
                expected_output=None if mask_details else expected,
                actual_output=None if mask_details else actual_output,
                is_hidden=is_hidden,
                error=error_msg,
                execution_time_ms=execution_time_ms,
            )

        except subprocess.TimeoutExpired:
            return TestCaseResult(
                test_case_number=index,
                passed=False,
                input_data=None if mask_details else input_data,
                expected_output=None if mask_details else expected_output.strip(),
                actual_output=None if mask_details else "",
                is_hidden=is_hidden,
                error="Execution timed out.",
                execution_time_ms=self.TIMEOUT_SECONDS * 1000,
            )

        except FileNotFoundError:
            raise RuntimeError(
                "Docker is not installed or is not available in PATH."
            )
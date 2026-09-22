import subprocess

import pytest

from app.enums.coding_language import CodingLanguage
from app.enums.question_difficulty import QuestionDifficulty
from app.models.coding_question import CodingQuestion
from app.models.coding_test_case import CodingTestCase
from app.services.code_execution_service import CodeExecutionService


def docker_available():
    try:
        result = subprocess.run(
            ["docker", "info"],
            capture_output=True,
            timeout=5,
            check=False,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


pytestmark = pytest.mark.skipif(
    not docker_available(),
    reason="Docker daemon is unavailable",
)


def make_question(input_data="2 3", expected_output="5"):
    question = CodingQuestion(
        topic_id=1,
        language=CodingLanguage.PYTHON,
        difficulty=QuestionDifficulty.EASY,
        title="Add two numbers",
        problem_statement="Add two numbers.",
        input_format="Two integers.",
        output_format="Their sum.",
        constraints="Integers.",
        examples="2 3 -> 5",
        starter_code="",
    )
    question.test_cases = [
        CodingTestCase(
            input_data=input_data,
            expected_output=expected_output,
            execution_order=1,
        ),
    ]
    return question


def test_code_execution_passing_case():
    response = CodeExecutionService().execute(
        make_question(),
        "a, b = map(int, input().split())\nprint(a + b)",
    )

    assert response.success is True
    assert response.passed_test_cases == 1


def test_code_execution_failing_case():
    response = CodeExecutionService().execute(
        make_question(),
        "print('wrong')",
    )

    assert response.success is False
    assert response.failed_test_cases == 1


def test_code_execution_timeout_case():
    response = CodeExecutionService().execute(
        make_question(),
        "while True:\n    pass",
    )

    assert response.success is False
    assert response.results[0].error == "Execution timed out."

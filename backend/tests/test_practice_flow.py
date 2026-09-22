from unittest.mock import patch, MagicMock
import pytest

from app.enums.coding_language import CodingLanguage
from app.enums.question_difficulty import QuestionDifficulty
from app.models.coding_question import CodingQuestion
from app.models.coding_test_case import CodingTestCase
from app.models.coding_submission import CodingSubmission
from app.services.code_execution_service import CodeExecutionService


def create_mock_question():
    q = CodingQuestion(
        id=1,
        topic_id=1,
        language=CodingLanguage.PYTHON,
        difficulty=QuestionDifficulty.EASY,
        title="Sum Problem",
        problem_statement="Calculate sum",
        input_format="Two ints",
        output_format="Sum",
        constraints="None",
        examples="1 2 -> 3",
        starter_code="def solve(): pass",
    )
    tc_visible = CodingTestCase(
        id=1,
        coding_question_id=1,
        input_data="1 2",
        expected_output="3",
        is_hidden=False,
        execution_order=1,
    )
    tc_hidden = CodingTestCase(
        id=2,
        coding_question_id=1,
        input_data="100 200",
        expected_output="300",
        is_hidden=True,
        execution_order=2,
    )
    q.test_cases = [tc_visible, tc_hidden]
    return q


def test_run_visible_only_runs_visible_cases():
    q = create_mock_question()
    service = CodeExecutionService()

    with patch.object(service, "_run_test_case") as mock_run:
        from app.schemas.code_execution import TestCaseResult
        mock_run.return_value = TestCaseResult(
            test_case_number=1,
            passed=True,
            input_data="1 2",
            expected_output="3",
            actual_output="3",
            is_hidden=False,
        )

        resp = service.run_visible(q, "print(3)")
        assert resp.total_test_cases == 1
        assert resp.results[0].input_data == "1 2"
        assert resp.results[0].expected_output == "3"
        assert resp.results[0].is_hidden is False
        assert mock_run.call_count == 1


def test_submit_runs_all_cases_and_masks_hidden():
    q = create_mock_question()
    service = CodeExecutionService()

    with patch("subprocess.run") as mock_sub:
        # First call (visible: 1 2 -> 3)
        # Second call (hidden: 100 200 -> 300)
        res1 = MagicMock(returncode=0, stdout="3\n", stderr="")
        res2 = MagicMock(returncode=0, stdout="300\n", stderr="")
        mock_sub.side_effect = [res1, res2]

        resp = service.submit(q, "code")
        assert resp.total_test_cases == 2
        assert resp.success is True

        # Case 1 is visible -> input and expected output present
        assert resp.results[0].is_hidden is False
        assert resp.results[0].input_data == "1 2"
        assert resp.results[0].expected_output == "3"
        assert resp.results[0].actual_output == "3"

        # Case 2 is hidden -> input, expected, and actual output MUST BE NONE (NO LEAK)
        assert resp.results[1].is_hidden is True
        assert resp.results[1].input_data is None
        assert resp.results[1].expected_output is None
        assert resp.results[1].actual_output is None


def test_multi_language_config_has_all_languages():
    service = CodeExecutionService()
    for lang in [CodingLanguage.PYTHON, CodingLanguage.JAVASCRIPT, CodingLanguage.JAVA, CodingLanguage.CPP]:
        assert lang in service.LANGUAGE_CONFIG
        config = service.LANGUAGE_CONFIG[lang]
        assert "image" in config
        assert "command" in config
        assert "filename" in config

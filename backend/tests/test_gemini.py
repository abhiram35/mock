from types import SimpleNamespace

import pytest

from app.ai.gemini_client import GeminiEvaluationClient
from app.core.exceptions import GeminiResponseException
from app.models.interview_answer import InterviewAnswer
from app.schemas.evaluation import InterviewEvaluation
from app.services import evaluation_service
from app.services.evaluation_service import EvaluationService


class FakeGemini:
    def evaluate_answer(self, **kwargs):
        return InterviewEvaluation(
            overall_score=86,
            technical_score=90,
            communication_score=80,
            relevance_score=88,
            feedback="Clear and correct.",
            strengths="Strong fundamentals.",
            improvements="Add a concrete example.",
        )


def test_evaluation_service_maps_gemini_response(monkeypatch):
    monkeypatch.setattr(
        evaluation_service,
        "GeminiEvaluationClient",
        lambda: FakeGemini(),
    )
    service = EvaluationService(db=None)
    answer = InterviewAnswer(
        session_id=1,
        question_id=1,
        answer_text="candidate answer",
    )
    question = SimpleNamespace(
        question_text="question",
        expected_answer="expected",
    )

    result = service.evaluate_answer(answer, question)

    assert result.overall_score == 86
    assert result.technical_score == 90
    assert result.communication_score == 80
    assert result.relevance_score == 88
    assert result.feedback == "Clear and correct."
    assert result.strengths == "Strong fundamentals."
    assert result.improvements == "Add a concrete example."


def make_client(response):
    client = GeminiEvaluationClient.__new__(GeminiEvaluationClient)
    client.model = "test-model"
    client.client = SimpleNamespace(
        models=SimpleNamespace(
            generate_content=lambda **kwargs: response,
        ),
    )
    return client


def test_gemini_falls_back_to_json_text():
    response = SimpleNamespace(
        parsed=None,
        text=(
            '{"overall_score": 70, "technical_score": 70, '
            '"communication_score": 70, "relevance_score": 70, '
            '"feedback": "Good", "strengths": "Clear", '
            '"improvements": "More detail"}'
        ),
    )

    result = make_client(response).evaluate_answer(
        question="question",
        expected_answer="expected",
        candidate_answer="answer",
    )

    assert result.overall_score == 70
    assert result.feedback == "Good"


def test_malformed_gemini_response_raises_custom_exception():
    response = SimpleNamespace(
        parsed=None,
        text="not valid evaluation JSON",
    )

    with pytest.raises(GeminiResponseException) as error:
        make_client(response).evaluate_answer(
            question="question",
            expected_answer="expected",
            candidate_answer="answer",
        )

    assert error.value.status_code == 503

from __future__ import annotations

from pydantic import BaseModel, Field


class CodeExecutionRequest(BaseModel):
    """
    Schema used when running or submitting candidate code.
    """

    coding_question_id: int = Field(
        ...,
        gt=0,
    )

    code: str = Field(
        ...,
        min_length=1,
    )

    mode: str = Field(
        default="run",
        description="Execution mode: 'run' for visible test cases, 'submit' for full evaluation",
    )


class TestCaseResult(BaseModel):
    """
    Result of one test case.
    """

    test_case_number: int

    passed: bool

    input_data: str | None = None

    expected_output: str | None = None

    actual_output: str | None = None

    is_hidden: bool = False

    error: str | None = None

    execution_time_ms: float | None = None


class CodeExecutionResponse(BaseModel):
    """
    Response returned after executing candidate code.
    """

    success: bool

    language: str

    total_test_cases: int

    passed_test_cases: int

    failed_test_cases: int

    results: list[TestCaseResult]

    submission_id: int | None = None

    status: str | None = None
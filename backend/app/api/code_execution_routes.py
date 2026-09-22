from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.rate_limit import enforce_code_execution_rate_limit
from app.dependencies.auth import get_current_user
from app.enums.coding_submission_status import CodingSubmissionStatus
from app.models.coding_submission import CodingSubmission
from app.models.user import User
from app.schemas.code_execution import (
    CodeExecutionRequest,
    CodeExecutionResponse,
)
from app.services.code_execution_service import (
    CodeExecutionService,
)
from app.services.coding_question_service import (
    CodingQuestionService,
)


router = APIRouter(
    prefix="/code-execution",
    tags=["Code Execution"],
)


@router.post(
    "/run",
    response_model=CodeExecutionResponse,
)
def run_code(
    execution_data: CodeExecutionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    _: None = Depends(enforce_code_execution_rate_limit),
):
    """
    Execute candidate code against visible test cases only.
    Provides complete debugging input, expected, and actual output.
    """
    question_service = CodingQuestionService(db)
    question = question_service.get_question_by_id(
        execution_data.coding_question_id
    )

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coding question not found.",
        )

    execution_service = CodeExecutionService()

    try:
        return execution_service.run_visible(
            question=question,
            code=execution_data.code,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        )


@router.post(
    "/submit",
    response_model=CodeExecutionResponse,
)
def submit_code(
    execution_data: CodeExecutionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    _: None = Depends(enforce_code_execution_rate_limit),
):
    """
    Execute candidate code against all test cases (visible and hidden),
    mask hidden test case details, and record the submission status.
    """
    question_service = CodingQuestionService(db)
    question = question_service.get_question_by_id(
        execution_data.coding_question_id
    )

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coding question not found.",
        )

    execution_service = CodeExecutionService()

    try:
        response = execution_service.submit(
            question=question,
            code=execution_data.code,
        )

        submission_status = (
            CodingSubmissionStatus.SOLVED
            if response.success
            else CodingSubmissionStatus.ATTEMPTED
        )
        submission = CodingSubmission(
            user_id=current_user.id,
            coding_question_id=question.id,
            status=submission_status,
            code=execution_data.code,
            language=question.language,
        )
        db.add(submission)
        db.commit()
        db.refresh(submission)

        response.submission_id = submission.id
        response.status = submission_status.value
        return response

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )
    except RuntimeError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        )
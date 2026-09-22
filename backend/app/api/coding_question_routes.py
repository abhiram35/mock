from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.enums.coding_submission_status import CodingSubmissionStatus
from app.models.coding_submission import CodingSubmission
from app.models.user import User
from app.schemas.coding_question import (
    CodingQuestionBulkCreate,
    CodingQuestionCreate,
    CodingQuestionResponse,
    CodingQuestionUpdate,
)
from app.schemas.coding_submission import CodingSubmissionResponse
from app.services.coding_question_service import (
    CodingQuestionService,
)


router = APIRouter(
    prefix="/coding-questions",
    tags=["Coding Questions"],
)


@router.post(
    "",
    response_model=CodingQuestionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_question(
    question_data: CodingQuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CodingQuestionService(db)

    try:
        return service.create_question(
            question_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


@router.post(
    "/bulk",
    response_model=list[CodingQuestionResponse],
    status_code=status.HTTP_201_CREATED,
)
def create_questions_bulk(
    bulk_data: CodingQuestionBulkCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CodingQuestionService(db)

    try:
        return service.create_questions_bulk(
            bulk_data
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


@router.get(
    "",
    response_model=list[CodingQuestionResponse],
)
def get_questions(
    topic_id: int | None = None,
    language: str | None = None,
    difficulty: str | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CodingQuestionService(db)

    try:
        return service.get_questions(
            topic_id=topic_id,
            language=language,
            difficulty=difficulty,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


@router.get(
    "/user/submissions",
    response_model=list[CodingSubmissionResponse],
)
def get_user_submissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Get all coding submissions submitted by the current user.
    """
    return (
        db.query(CodingSubmission)
        .filter(CodingSubmission.user_id == current_user.id)
        .order_by(CodingSubmission.submitted_at.desc())
        .all()
    )


@router.get(
    "/solved-status",
    response_model=list[int],
)
@router.get(
    "/user/solved-ids",
    response_model=list[int],
)
def get_user_solved_status(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Get set/list of distinct question IDs solved by the current user.
    """
    rows = (
        db.query(CodingSubmission.coding_question_id)
        .filter(
            CodingSubmission.user_id == current_user.id,
            CodingSubmission.status == CodingSubmissionStatus.SOLVED,
        )
        .distinct()
        .all()
    )
    return [row[0] for row in rows]


@router.get(
    "/{question_id}/submissions",
    response_model=list[CodingSubmissionResponse],
)
def get_question_submissions(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Get current user's submissions for a specific question.
    """
    return (
        db.query(CodingSubmission)
        .filter(
            CodingSubmission.user_id == current_user.id,
            CodingSubmission.coding_question_id == question_id,
        )
        .order_by(CodingSubmission.submitted_at.desc())
        .all()
    )


@router.get(
    "/{question_id}",
    response_model=CodingQuestionResponse,
)
def get_question(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CodingQuestionService(db)

    question = service.get_question_by_id(
        question_id
    )

    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coding question not found.",
        )

    return question


@router.put(
    "/{question_id}",
    response_model=CodingQuestionResponse,
)
def update_question(
    question_id: int,
    question_data: CodingQuestionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CodingQuestionService(db)

    try:
        return service.update_question(
            question_id,
            question_data,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


@router.delete(
    "/{question_id}",
    response_model=CodingQuestionResponse,
)
def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CodingQuestionService(db)

    try:
        return service.delete_question(
            question_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )
from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.enums.coding_language import CodingLanguage
from app.enums.coding_submission_status import CodingSubmissionStatus
from app.models.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.coding_question import CodingQuestion
    from app.models.user import User


class CodingSubmission(TimestampMixin, Base):
    """
    Database model representing candidate submissions for coding practice questions.
    """

    __tablename__ = "coding_submissions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    coding_question_id: Mapped[int] = mapped_column(
        ForeignKey("coding_questions.id"),
        nullable=False,
        index=True,
    )

    status: Mapped[CodingSubmissionStatus] = mapped_column(
        Enum(
            CodingSubmissionStatus,
            values_callable=lambda enum_cls: [
                member.value for member in enum_cls
            ],
            native_enum=False,
            length=20,
            name="coding_submission_status_enum",
        ),
        nullable=False,
        index=True,
    )

    code: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    language: Mapped[CodingLanguage] = mapped_column(
        Enum(
            CodingLanguage,
            values_callable=lambda enum_cls: [
                member.value for member in enum_cls
            ],
            native_enum=False,
            length=20,
            name="coding_submission_language_enum",
        ),
        nullable=False,
    )

    submitted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="coding_submissions",
    )

    coding_question: Mapped["CodingQuestion"] = relationship(
        "CodingQuestion",
        back_populates="submissions",
    )

    def __repr__(self) -> str:
        return (
            f"<CodingSubmission("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"coding_question_id={self.coding_question_id}, "
            f"status='{self.status.value}', "
            f"language='{self.language.value}'"
            f")>"
        )

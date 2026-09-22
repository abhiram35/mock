from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CodingSubmissionResponse(BaseModel):
    """
    Schema for a coding submission record.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    user_id: int
    coding_question_id: int
    status: str
    code: str
    language: str
    submitted_at: datetime

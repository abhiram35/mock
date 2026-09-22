"""add coding submissions

Revision ID: e8c21a5b8f01
Revises: 369fcb17d942
Create Date: 2026-09-22 21:40:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e8c21a5b8f01"
down_revision: Union[str, Sequence[str], None] = "369fcb17d942"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create coding_submissions table."""
    op.create_table(
        "coding_submissions",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "user_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "coding_question_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.String(length=20),
            nullable=False,
        ),
        sa.Column(
            "code",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "language",
            sa.String(length=20),
            nullable=False,
        ),
        sa.Column(
            "submitted_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["coding_question_id"],
            ["coding_questions.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_coding_submissions_user_id"),
        "coding_submissions",
        ["user_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_coding_submissions_coding_question_id"),
        "coding_submissions",
        ["coding_question_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_coding_submissions_status"),
        "coding_submissions",
        ["status"],
        unique=False,
    )


def downgrade() -> None:
    """Drop coding_submissions table."""
    op.drop_index(
        op.f("ix_coding_submissions_status"),
        table_name="coding_submissions",
    )
    op.drop_index(
        op.f("ix_coding_submissions_coding_question_id"),
        table_name="coding_submissions",
    )
    op.drop_index(
        op.f("ix_coding_submissions_user_id"),
        table_name="coding_submissions",
    )
    op.drop_table("coding_submissions")

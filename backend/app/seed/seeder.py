"""
Consolidated database seeder for the AI-Powered Mock Interview backend.

Usage (from the backend/ directory):

    python -m app.seed.seeder            # seed everything (practice + coding)
    python -m app.seed.seeder --practice # only create empty practice topics
    python -m app.seed.seeder --coding   # only seed coding questions + test cases
    python -m app.seed.seeder --reset    # delete seeded interview/coding data first

Run the per-topic question-bank scripts afterwards (or instead of --practice):

    python seed_python_interview.py
    python seed_java_interview.py
    python seed_dbms_interview.py
    python seed_os_interview.py
    python seed_cn_interview.py
    python seed_swe_interview.py

Every step is idempotent: re-running this module never duplicates rows.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from sqlalchemy.orm import Session

from app.enums.coding_language import CodingLanguage
from app.enums.question_difficulty import QuestionDifficulty
from app.models.coding_question import CodingQuestion
from app.models.coding_test_case import CodingTestCase
from app.models.question import Question
from app.models.topic import Topic

SEED_DATA_PATH = Path(__file__).resolve().parent / "seed_data.json"


def load_seed_data() -> dict:
    with open(SEED_DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def seed_practice_topics(db: Session) -> None:
    """
    Create one active Topic row per practice topic so the platform
    has topics to attach question banks to.

    The question banks themselves live in the per-topic scripts at the
    repository root (seed_python_interview.py, seed_java_interview.py,
    ...). This seeder creates the topics; those scripts fill them with
    questions. If a topic already has questions, nothing is touched.
    """
    data = load_seed_data()

    for entry in data["practice_topics"]:
        topic = db.query(Topic).filter(Topic.name == entry["name"]).first()

        if topic:
            print(f"Topic exists: {topic.name} (ID: {topic.id}) - skipped")
            continue

        topic = Topic(
            name=entry["name"],
            description=entry["description"],
            is_active=True,
        )
        db.add(topic)
        db.commit()
        db.refresh(topic)
        print(f"Created topic: {topic.name} (ID: {topic.id})")

    print(
        "\nNote: topics were created without questions. Populate each topic's "
        "question bank with the per-topic scripts, e.g.:\n"
        "    python seed_python_interview.py\n"
        "    python seed_java_interview.py\n"
        "    python seed_dbms_interview.py\n"
        "    python seed_os_interview.py\n"
        "    python seed_cn_interview.py\n"
        "    python seed_swe_interview.py"
    )


def seed_coding_questions(db: Session) -> None:
    """
    Seed CodingQuestion + CodingTestCase rows from seed_data.json.

    All seeded questions are Python (the only language the code-execution
    sandbox currently supports). Each question carries visible and hidden
    test cases so the coding-interview feature works out of the box.
    """
    data = load_seed_data()

    coding_topic_data = data["coding_topic"]
    topic = (
        db.query(Topic)
        .filter(Topic.name == coding_topic_data["name"])
        .first()
    )

    if not topic:
        topic = Topic(
            name=coding_topic_data["name"],
            description=coding_topic_data["description"],
            is_active=True,
        )
        db.add(topic)
        db.commit()
        db.refresh(topic)
        print(f"Created coding topic: {topic.name} (ID: {topic.id})")
    else:
        print(f"Using existing coding topic: {topic.name} (ID: {topic.id})")

    created_questions = 0
    created_test_cases = 0

    for entry in data["coding_questions"]:
        existing = (
            db.query(CodingQuestion)
            .filter(
                CodingQuestion.topic_id == topic.id,
                CodingQuestion.title == entry["title"],
            )
            .first()
        )

        if existing:
            print(f"Coding question exists: {entry['title']} - skipped")
            continue

        question = CodingQuestion(
            topic_id=topic.id,
            language=CodingLanguage(entry["language"]),
            difficulty=QuestionDifficulty(entry["difficulty"]),
            title=entry["title"],
            problem_statement=entry["problem_statement"],
            input_format=entry["input_format"],
            output_format=entry["output_format"],
            constraints=entry["constraints"],
            examples=entry["examples"],
            starter_code=entry["starter_code"],
        )

        question.test_cases = [
            CodingTestCase(
                input_data=tc["input_data"],
                expected_output=tc["expected_output"],
                is_hidden=tc.get("is_hidden", False),
                execution_order=tc.get("execution_order", 0),
            )
            for tc in entry["test_cases"]
        ]

        db.add(question)
        db.commit()
        db.refresh(question)

        created_questions += 1
        created_test_cases += len(question.test_cases)

        print(
            f"Created coding question: {question.title} "
            f"({len(question.test_cases)} test cases, "
            f"{sum(1 for tc in question.test_cases if tc.is_hidden)} hidden)"
        )

    print()
    print("=" * 60)
    print("CODING QUESTION SEEDING COMPLETE")
    print("=" * 60)
    print(f"Questions created : {created_questions}")
    print(f"Test cases created: {created_test_cases}")
    print("=" * 60)


def reset_seeded_data(db: Session) -> None:
    """
    Remove all seeded interview/coding data so it can be re-seeded.

    Admin-created questions and topics are also removed. User accounts,
    interview sessions, and submissions are left untouched.
    """
    deleted_test_cases = db.query(CodingTestCase).delete()
    deleted_coding_questions = db.query(CodingQuestion).delete()
    deleted_questions = db.query(Question).delete()
    deleted_topics = db.query(Topic).delete()
    db.commit()

    print("Reset complete:")
    print(f"  Coding test cases deleted: {deleted_test_cases}")
    print(f"  Coding questions deleted : {deleted_coding_questions}")
    print(f"  Practice questions deleted: {deleted_questions}")
    print(f"  Topics deleted           : {deleted_topics}")


def main() -> None:
    # Imported here so importing this module (e.g. in tests) does not
    # require a configured database.
    from app.database import SessionLocal, engine
    from app.models import Base

    # Create any missing tables so the seeder works on a fresh database
    # without running Alembic first (no-op for tables that already exist).
    Base.metadata.create_all(bind=engine)

    parser = argparse.ArgumentParser(
        description="Seed the AI Mock Interview database."
    )
    parser.add_argument(
        "--practice",
        action="store_true",
        help="Only create the practice topics (question banks come from the per-topic scripts).",
    )
    parser.add_argument(
        "--coding",
        action="store_true",
        help="Only seed coding questions and their test cases.",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Delete seeded topics/questions (including coding questions) before seeding.",
    )
    args = parser.parse_args()

    db: Session = SessionLocal()

    try:
        if args.reset:
            reset_seeded_data(db)

        if args.practice:
            seed_practice_topics(db)
        elif args.coding:
            seed_coding_questions(db)
        else:
            seed_practice_topics(db)
            print()
            seed_coding_questions(db)
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()

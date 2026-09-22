import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from app.database import get_db
from app.main import app
from app.models import Base
from app.models.user import User


@pytest.fixture()
def client():
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)

    def override_get_db():
        db = session_factory()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(engine)
    engine.dispose()


def register(client, email="candidate@example.com"):
    return client.post(
        "/auth/register",
        json={
            "full_name": "Test Candidate",
            "email": email,
            "password": "StrongPassword123",
        },
    )


def test_register_persists_hashed_password(client):
    response = register(client)

    assert response.status_code == 201
    assert response.json()["email"] == "candidate@example.com"

    db = next(app.dependency_overrides[get_db]())
    user = db.query(User).filter(User.email == "candidate@example.com").one()
    assert user.password_hash != "StrongPassword123"
    assert user.password_hash.startswith("$2")
    db.close()


def test_duplicate_email_returns_conflict(client):
    register(client)

    response = register(client)

    assert response.status_code == 409
    assert "already exists" in response.json()["detail"]


def test_login_returns_jwt_for_valid_credentials(client):
    register(client)

    response = client.post(
        "/auth/login",
        json={
            "email": "candidate@example.com",
            "password": "StrongPassword123",
        },
    )

    assert response.status_code == 200
    assert response.json()["token_type"] == "bearer"
    assert response.json()["access_token"]


def test_invalid_credentials_return_401(client):
    register(client)

    wrong_password = client.post(
        "/auth/login",
        json={
            "email": "candidate@example.com",
            "password": "WrongPassword123",
        },
    )
    unknown_email = client.post(
        "/auth/login",
        json={
            "email": "unknown@example.com",
            "password": "WrongPassword123",
        },
    )

    assert wrong_password.status_code == 401
    assert unknown_email.status_code == 401


def test_protected_route_requires_token(client):
    response = client.get("/auth/me")

    assert response.status_code == 401


def test_regular_user_cannot_access_admin_route(client):
    register(client)
    token = client.post(
        "/auth/login",
        json={
            "email": "candidate@example.com",
            "password": "StrongPassword123",
        },
    ).json()["access_token"]

    response = client.get(
        "/admin/dashboard",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 403

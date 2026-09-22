from types import SimpleNamespace

import pytest
from starlette.requests import Request

from app.config import settings
from app.core import rate_limit
from app.core.exceptions import RateLimitExceededException
from app.services.coding_question_service import CodingQuestionService
from app.enums.coding_language import CodingLanguage


def make_request(host="127.0.0.1"):
    return Request(
        {
            "type": "http",
            "method": "POST",
            "path": "/test",
            "headers": [],
            "client": (host, 1234),
            "server": ("testserver", 80),
            "scheme": "http",
        }
    )


def test_rate_limit_rejects_requests_after_configured_limit(monkeypatch):
    rate_limit._requests.clear()
    monkeypatch.setattr(settings, "GEMINI_RATE_LIMIT", 1)

    rate_limit.enforce_gemini_rate_limit(make_request())

    with pytest.raises(RateLimitExceededException):
        rate_limit.enforce_gemini_rate_limit(make_request())

    rate_limit._requests.clear()


def test_unsupported_coding_language_is_rejected():
    with pytest.raises(ValueError, match="Only Python"):
        CodingQuestionService._ensure_supported_language(
            CodingLanguage.JAVASCRIPT
        )
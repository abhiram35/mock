from collections import defaultdict, deque
from threading import Lock
from time import monotonic

from fastapi import Request

from app.config import settings
from app.core.exceptions import RateLimitExceededException


_requests = defaultdict(deque)
_lock = Lock()


def _check_limit(request: Request, bucket: str, limit: int):
    now = monotonic()
    client = request.client.host if request.client else "unknown"
    key = f"{bucket}:{client}"
    cutoff = now - settings.RATE_LIMIT_WINDOW_SECONDS

    with _lock:
        timestamps = _requests[key]
        while timestamps and timestamps[0] <= cutoff:
            timestamps.popleft()

        if len(timestamps) >= limit:
            raise RateLimitExceededException()

        timestamps.append(now)


def enforce_gemini_rate_limit(request: Request):
    _check_limit(
        request,
        "gemini",
        settings.GEMINI_RATE_LIMIT,
    )


def enforce_code_execution_rate_limit(request: Request):
    _check_limit(
        request,
        "code-execution",
        settings.CODE_EXECUTION_RATE_LIMIT,
    )
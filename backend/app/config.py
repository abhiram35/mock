import logging

from pydantic_settings import BaseSettings, SettingsConfigDict


logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Gemini
    GEMINI_LIVE_API_KEY: str
    GEMINI_EVALUATION_API_KEY: str

    GEMINI_LIVE_MODEL: str
    GEMINI_EVALUATION_MODEL: str

    ALLOWED_ORIGINS: str = "http://localhost:5173"
    GEMINI_RATE_LIMIT: int = 10
    CODE_EXECUTION_RATE_LIMIT: int = 10
    RATE_LIMIT_WINDOW_SECONDS: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()


# Values that mark an unconfigured Gemini API key. AI features fail (or fail
# silently) with these in place, so warn loudly at startup instead.
_PLACEHOLDER_KEY_MARKERS = ("placeholder", "replace-with", "your-")


def _is_placeholder_key(value: str) -> bool:
    normalized = value.strip().lower()
    if not normalized or normalized in {"none", "null", "changeme"}:
        return True
    return any(marker in normalized for marker in _PLACEHOLDER_KEY_MARKERS)


def warn_on_placeholder_gemini_keys() -> list[str]:
    """
    Log a prominent warning for every Gemini key still set to a placeholder.

    Returns the names of the settings that are placeholders, so callers
    (and tests) can inspect the result. Safe to call multiple times.
    """
    placeholder_keys: list[str] = []

    if _is_placeholder_key(settings.GEMINI_LIVE_API_KEY):
        placeholder_keys.append("GEMINI_LIVE_API_KEY")

    if _is_placeholder_key(settings.GEMINI_EVALUATION_API_KEY):
        placeholder_keys.append("GEMINI_EVALUATION_API_KEY")

    if placeholder_keys:
        names = ", ".join(placeholder_keys)
        logger.warning(
            "=" * 72
        )
        logger.warning(
            "GEMINI API KEYS NOT CONFIGURED: %s still contain placeholder "
            "values in backend/.env.",
            names,
        )
        logger.warning(
            "AI-powered features (live interview and answer evaluation) are "
            "DISABLED and related requests will fail until real keys are set."
        )
        logger.warning(
            "Set the key(s) in backend/.env (see backend/.env.example) and "
            "restart the server."
        )
        logger.warning(
            "=" * 72
        )

    return placeholder_keys


warn_on_placeholder_gemini_keys()
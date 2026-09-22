import os


os.environ.setdefault(
    "DATABASE_URL",
    "sqlite+pysqlite:///:memory:",
)
os.environ.setdefault("SECRET_KEY", "test-secret-key")
os.environ.setdefault("ALGORITHM", "HS256")
os.environ.setdefault("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
os.environ.setdefault("GEMINI_LIVE_API_KEY", "test-live-key")
os.environ.setdefault("GEMINI_EVALUATION_API_KEY", "test-evaluation-key")
os.environ.setdefault("GEMINI_LIVE_MODEL", "test-live-model")
os.environ.setdefault(
    "GEMINI_EVALUATION_MODEL",
    "test-evaluation-model",
)
os.environ.setdefault("ALLOWED_ORIGINS", "http://localhost:5173")
os.environ.setdefault("GEMINI_RATE_LIMIT", "100")
os.environ.setdefault("CODE_EXECUTION_RATE_LIMIT", "100")
os.environ.setdefault("RATE_LIMIT_WINDOW_SECONDS", "60")

# Backend Application Layout

The FastAPI application lives in `backend/app/`. Every HTTP request follows the
**route → service → model** flow: route handlers in `api/` validate input and
call a service function; services in `services/` contain the business logic and
interact with SQLAlchemy models defined in `models/`; Pydantic schemas in
`schemas/` handle request/response serialisation. Enums, shared dependencies
(authentication, database session), AI prompt templates, and utility helpers each
have their own sub-package.

```
app/
├── ai/              # Gemini AI client wrappers
├── api/             # FastAPI route handlers (one file per domain)
├── core/            # Security helpers (hashing, JWT)
├── dependencies/    # FastAPI dependency functions (auth, db session)
├── enums/           # Shared enums (difficulty, status, role, language)
├── models/          # SQLAlchemy ORM models (one file per table)
├── prompts/         # AI prompt templates for evaluation & interviews
├── routes/          # (reserved — currently empty)
├── schemas/         # Pydantic request/response models
├── seed/            # Database seeder (practice topics + coding questions)
├── services/        # Business logic layer (one file per domain)
├── utils/           # Miscellaneous utility functions
├── config.py        # Pydantic settings (reads .env)
├── database.py      # SQLAlchemy engine & session factory
└── main.py          # FastAPI app creation, middleware, router wiring
```

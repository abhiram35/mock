# AI-Powered Mock Interview

AI-Powered Mock Interview is a full-stack practice platform. Users can complete traditional and coding interviews, receive Gemini-powered evaluation, and review their performance. Administrators can monitor platform activity.

## Architecture

```text
React + TypeScript + Vite frontend
              |
        FastAPI backend
          /         \
   MySQL database   Google Gemini
                         |
              Docker code-execution sandbox
```

The frontend calls the FastAPI API. SQLAlchemy and Alembic manage MySQL persistence. Gemini generates interview and evaluation responses. Coding submissions execute inside resource-limited Docker containers.

## Prerequisites

- Python 3.11 or newer
- Node.js 20 or newer and npm
- MySQL 8 or newer
- Docker Desktop or Docker Engine, running for coding interviews

## Setup

1. Clone the repository and enter the project directory.
2. Copy `backend/.env.example` to `backend/.env` and fill in the database and Gemini values.
3. Copy `frontend/.env.example` to `frontend/.env`.
4. Install backend dependencies:

   ```powershell
   cd backend
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

5. Create the configured MySQL database, then run migrations:

   ```powershell
   alembic upgrade head
   ```

6. Seed interview data and create an administrator:

   ```powershell
   python -m app.seed.seeder
   ```

   This creates the practice topics plus the coding questions and their test
   cases. It is safe to re-run; nothing is duplicated.

   Then populate each practice topic's question bank with its per-topic
   script:

   ```powershell
   python seed_python_interview.py
   python seed_java_interview.py
   python seed_dbms_interview.py
   python seed_os_interview.py
   python seed_cn_interview.py
   python seed_swe_interview.py
   ```

   These scripts are also idempotent: re-running them never duplicates rows.

   Finally, create an administrator account:

   ```powershell
   python -m app.seed.admin_seeder
   ```

7. Start the backend:

   ```powershell
   uvicorn app.main:app --reload
   ```

8. In a second terminal, install and start the frontend:

   ```powershell
   cd frontend
   npm install
   npm run dev
   ```

Docker must be installed and running for the coding-interview feature to execute submissions.

Coding execution currently supports Python only. JavaScript, Java, and C++ are
intentionally rejected by the backend until their sandbox images and
compile/run flows are validated, even though Docker configs for them are
already prepared in the code execution service. The API also applies
configurable per-client limits to Gemini evaluation and code execution
requests; configure these in `backend/.env`.

If `GEMINI_LIVE_API_KEY` or `GEMINI_EVALUATION_API_KEY` are left at their
placeholder values, the backend logs a prominent startup warning and AI
features remain disabled; the server still boots for the rest of the app.

## Tests

From `backend`, run:

```powershell
pytest
```

From `frontend`, run the typecheck and production build:

```powershell
npm run build
```

The test suite mocks external Gemini calls. Docker-dependent code execution tests skip when Docker is unavailable.

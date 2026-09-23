#!/usr/bin/env bash
# backend/scripts/lint.sh — run all backend linters
set -euo pipefail

cd "$(dirname "$0")/.."

echo "=== ruff check ==="
ruff check app/ tests/ seed_*.py

echo ""
echo "=== ruff format --check ==="
ruff format --check app/ tests/ seed_*.py

echo ""
echo "All checks passed."

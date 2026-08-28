#!/usr/bin/env bash
set -euo pipefail

echo "== Repository verification =="

if command -v ruff >/dev/null 2>&1; then
  echo "-- ruff check"
  ruff check .
  echo "-- ruff format check"
  ruff format --check .
else
  echo "WARN: ruff not installed; skipping lint/format." >&2
fi

if command -v pytest >/dev/null 2>&1; then
  echo "-- pytest"
  pytest -q
else
  echo "WARN: pytest not installed; skipping tests." >&2
fi

if command -v mypy >/dev/null 2>&1; then
  echo "-- mypy"
  if [ -d src ]; then
    mypy src
  fi
else
  echo "INFO: mypy not installed/configured; skipping type check." >&2
fi

echo "== Verification complete =="

#!/usr/bin/env bash
set -euo pipefail

echo "== Security checks =="

missing=0

if command -v bandit >/dev/null 2>&1; then
  if [ -d src ]; then
    echo "-- bandit"
    bandit -q -r src
  fi
else
  echo "WARN: bandit not installed." >&2
  missing=1
fi

if command -v pip-audit >/dev/null 2>&1; then
  echo "-- pip-audit"
  pip-audit
else
  echo "WARN: pip-audit not installed." >&2
  missing=1
fi

# Optional secret scanners if the developer installed one.
if command -v gitleaks >/dev/null 2>&1; then
  echo "-- gitleaks"
  gitleaks detect --no-banner --redact
else
  echo "INFO: gitleaks not installed; skipping secret-history scan." >&2
fi

if [ "$missing" -ne 0 ]; then
  echo
  echo "Install the project's security dev dependencies before treating this as a passing security gate." >&2
  exit 2
fi

echo "== Security checks passed =="

#!/usr/bin/env python3
"""Fast PostToolUse checks for modified Python files. Never auto-fixes."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

payload = json.load(sys.stdin)
args = payload.get("toolCall", {}).get("args", {})
target_raw = args.get("TargetFile") or ""

# hooks.json lives in <repo>/.agents; this script lives in <repo>/scripts/agent.
REPO_ROOT = Path(__file__).resolve().parents[2]

if not target_raw.endswith(".py"):
    print("{}")
    raise SystemExit(0)

target = Path(target_raw)
if not target.is_absolute():
    target = REPO_ROOT / target
target = target.resolve()

if not target.exists():
    print("{}")
    raise SystemExit(0)

problems = []

proc = subprocess.run(
    [sys.executable, "-m", "py_compile", str(target)],
    cwd=REPO_ROOT,
    capture_output=True,
    text=True,
)
if proc.returncode != 0:
    problems.append("Python syntax check failed:\n" + (proc.stderr or proc.stdout))

ruff = shutil.which("ruff")
if ruff:
    proc = subprocess.run(
        [ruff, "check", str(target)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        problems.append("Ruff check failed:\n" + (proc.stdout or proc.stderr))

if problems:
    print("\n\n".join(problems), file=sys.stderr)

# PostToolUse hooks return an empty object.
print("{}")

#!/usr/bin/env python3
"""
Lightweight Antigravity Stop hook.

Blocks the first completion attempt when changed Python files fail syntax/Ruff.
It does not run the entire test/security suite on every conversational stop.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

payload = json.load(sys.stdin)
execution_num = int(payload.get("executionNum", 0))
fully_idle = bool(payload.get("fullyIdle", True))

if not fully_idle:
    print(json.dumps({"decision": "allow"}))
    raise SystemExit(0)

REPO_ROOT = Path(__file__).resolve().parents[2]
git = shutil.which("git")
if not git:
    print(json.dumps({"decision": "allow"}))
    raise SystemExit(0)

def run(cmd):
    return subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )

# Include both unstaged/staged working-tree changes relative to HEAD.
diff = run([git, "diff", "--name-only", "--diff-filter=ACMR", "HEAD"])
if diff.returncode != 0:
    print(json.dumps({"decision": "allow"}))
    raise SystemExit(0)

py_files = []
for rel in diff.stdout.splitlines():
    if rel.endswith(".py"):
        p = (REPO_ROOT / rel).resolve()
        if p.exists():
            py_files.append(str(p))

if not py_files:
    print(json.dumps({"decision": "allow"}))
    raise SystemExit(0)

failures = []

compile_proc = run([sys.executable, "-m", "compileall", "-q", *py_files])
if compile_proc.returncode != 0:
    failures.append("Python compilation failed.")

ruff = shutil.which("ruff")
if ruff:
    ruff_proc = run([ruff, "check", *py_files])
    if ruff_proc.returncode != 0:
        failures.append(
            "Ruff failed:\n" + (ruff_proc.stdout or ruff_proc.stderr)[-3000:]
        )

if failures and execution_num < 2:
    print(json.dumps({
        "decision": "continue",
        "reason": "Completion gate failed. Fix these checks before finishing:\n"
                  + "\n".join(failures)
    }))
else:
    print(json.dumps({"decision": "allow"}))

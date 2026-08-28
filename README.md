# Antigravity Hook Fix

Replace these files in the repository:

- `.agents/hooks.json`
- `scripts/agent/safety_gate.py`
- `scripts/agent/protected_file_gate.py`
- `scripts/agent/post_edit_check.py`
- `scripts/agent/stop_gate.py`

Changes:
1. Hook commands now use `../scripts/agent/...` because Antigravity executes workspace hooks from `.agents/`.
2. Python file-checking hooks now derive the repository root from `__file__`.
3. File checks execute with the repository root as their working directory.
4. Windows workspace-relative paths are normalized safely.

After copying, test in Antigravity:

1. `Run git status.` — should be allowed and execute normally.
2. `Run git commit --help.` — the hook pattern may require approval because it contains `git commit`; cancel the approval rather than running if desired.
3. Ask Antigravity to edit an ordinary temporary Python file with a syntax error — the PostToolUse check should report a syntax problem.
4. Ask it to modify `AGENTS.md` — it should require explicit confirmation.

Also run manually from repository root:

```bash
python scripts/agent/check-agent-setup.py
```

On Windows, ensure the `python` command Antigravity sees is the intended interpreter.

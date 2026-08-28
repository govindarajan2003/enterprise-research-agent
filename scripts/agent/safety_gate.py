#!/usr/bin/env python3
"""Antigravity PreToolUse hook for shell-command safety."""
import json
import re
import sys

payload = json.load(sys.stdin)
tool_call = payload.get("toolCall", {})
if tool_call.get("name") != "run_command":
    print(json.dumps({"decision": "allow"}))
    raise SystemExit(0)

args = tool_call.get("args", {})
command = (args.get("CommandLine") or "").strip()
lower = command.lower()

hard_deny = [
    r"(^|\s)rm\s+-rf\s+/(?:\s|$)",
    r"(^|\s)rm\s+-rf\s+/\*",
    r"(^|\s)mkfs(?:\.|\s)",
    r"(^|\s)dd\s+if=.*\s+of=/dev/",
    r":\(\)\s*\{\s*:\|:&\s*\};:",
]

force_ask = [
    r"\bgit\s+push\b.*--force(?:-with-lease)?",
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+clean\s+-[^\s]*f",
    r"\bgit\s+rebase\b",
    r"\bgit\s+commit\b",
    r"\bgit\s+push\b",
    r"\bgit\s+merge\b",
    r"\bgit\s+branch\s+-D\b",
    r"\bdrop\s+database\b",
    r"\bdrop\s+schema\b",
    r"\btruncate\s+(?:table\s+)?",
    r"\bdocker\s+system\s+prune\b",
    r"\bdocker\s+volume\s+prune\b",
    r"\bdocker\s+volume\s+rm\b",
    r"\bdocker\s+compose\s+down\b.*-v",
    r"\bkubectl\s+delete\b",
    r"\bterraform\s+destroy\b",
    r"\balembic\s+downgrade\b",
]

for pattern in hard_deny:
    if re.search(pattern, lower):
        print(json.dumps({
            "decision": "deny",
            "reason": "Blocked catastrophic/destructive command by repository safety policy."
        }))
        raise SystemExit(0)

for pattern in force_ask:
    if re.search(pattern, lower):
        print(json.dumps({
            "decision": "force_ask",
            "reason": "This command changes Git history/state, persistent data, or infrastructure and requires explicit user approval."
        }))
        raise SystemExit(0)

print(json.dumps({"decision": "allow"}))

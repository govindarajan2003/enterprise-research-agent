#!/usr/bin/env python3
"""Require confirmation before mutation of governance/ADR/security files."""
import json
import os
import sys

payload = json.load(sys.stdin)
tool_call = payload.get("toolCall", {})
args = tool_call.get("args", {})

target = (args.get("TargetFile") or "").replace("\\", "/")

protected_exact = {
    "AGENTS.md",
    ".agents/hooks.json",
    "SECURITY.md",
}
protected_parts = (
    "docs/adr/",
    ".agents/rules/",
    ".agents/skills/",
    ".agents/agents/",
    "scripts/agent/",
)

is_protected = (
    target in protected_exact
    or os.path.basename(target) in {"AGENTS.md", "SECURITY.md"}
    or any(part in target for part in protected_parts)
)

if is_protected:
    print(json.dumps({
        "decision": "force_ask",
        "reason": "This file defines architecture/governance/security enforcement. Review the proposed change explicitly before modification."
    }))
else:
    print(json.dumps({"decision": "allow"}))

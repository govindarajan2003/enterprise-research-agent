#!/usr/bin/env python3
"""Validate the repository Antigravity governance file layout."""
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[2]

required = [
    root / "AGENTS.md",
    root / ".agents" / "hooks.json",
    root / ".agents" / "rules" / "00-project-contract.md",
    root / ".agents" / "rules" / "architecture.md",
    root / ".agents" / "rules" / "security.md",
]

errors = []
for path in required:
    if not path.exists():
        errors.append(f"Missing: {path.relative_to(root)}")

for skill_dir in (root / ".agents" / "skills").glob("*"):
    if skill_dir.is_dir() and not (skill_dir / "SKILL.md").exists():
        errors.append(f"Skill missing SKILL.md: {skill_dir.relative_to(root)}")

try:
    json.loads((root / ".agents" / "hooks.json").read_text())
except Exception as exc:
    errors.append(f"Invalid .agents/hooks.json: {exc}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("Antigravity governance layout looks valid.")

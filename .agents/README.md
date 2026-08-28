# Antigravity Project Governance

This directory contains repository-scoped Antigravity customizations.

## What Is Committed

```text
.agents/
├── rules/
├── skills/
├── agents/
└── hooks.json
```

These files are engineering policy and should remain in Git.

Local caches, logs, state, and personal overrides are ignored by `.gitignore`.

## Recommended Rule Activation

Antigravity workspace rules are configured through the Customizations panel.

Recommended activation:

| Rule | Activation |
|---|---|
| `00-project-contract.md` | Always On |
| `architecture.md` | Always On |
| `security.md` | Always On |
| `git-workflow.md` | Always On |
| `python-backend.md` | Glob: `src/**/*.py`, `tests/**/*.py`, `scripts/**/*.py` |
| `testing.md` | Model Decision, or Glob for `tests/**` |
| `ai-rag.md` | Model Decision initially; later use graph/retrieval globs |
| `documentation.md` | Glob: `docs/**/*.md`, `README.md`, `AGENTS.md` |

Rules are kept focused because Antigravity discovers and applies them independently.

## Skills

Skills are procedural workflows. They should be invoked automatically when their
description matches the task; they can also be named explicitly.

Recommended usage:

- `implement-feature` — normal implementation
- `architecture-review` — before merging architecture-sensitive work
- `security-audit` — auth, ingestion, AI, retrieval, APIs, dependencies
- `code-review` — PR/diff review
- `test-feature` — test design
- `implementation-review` — learn/trace code after generation
- `rag-evaluation` — retrieval/grounding quality changes
- `database-change-review` — schema/migration/data-isolation changes

## Custom Agents

Review-only personas:

- `architecture-reviewer`
- `security-reviewer`
- `code-reviewer`

Use these for independent review rather than implementation.

## Hooks

`hooks.json` provides deterministic enforcement:

- dangerous shell commands are denied or require explicit confirmation,
- protected governance/ADR files require confirmation before edits,
- changed Python files receive fast syntax/lint checks,
- a stop gate performs lightweight verification before the agent declares completion.

The hooks deliberately do not auto-install dependencies or auto-fix code.

## Manual Verification

Run:

```bash
./scripts/agent/verify.sh
./scripts/agent/security-check.sh
```

The security script expects project dev tooling to be installed.

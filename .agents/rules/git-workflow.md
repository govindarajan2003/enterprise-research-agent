# Git Workflow Rules

- Never work directly on `main`.
- Never commit, push, merge, rebase, reset, clean, or force-push unless the user requested that Git operation.
- Before proposing a commit, show `git status` and summarize the diff.
- Never discard uncommitted user work.
- Never use `git reset --hard`, `git clean`, or force push without explicit per-action approval.
- Never bypass hooks/checks with `--no-verify` unless explicitly approved.

Branch prefixes:
- `feat/`
- `fix/`
- `docs/`
- `test/`
- `refactor/`
- `chore/`
- `security/`

Commit messages follow Conventional Commit style.

Architectural changes should include an ADR update in the same PR when practical.

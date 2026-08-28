# Contributing

## Branch Naming

Use one of:

- `feat/<short-name>`
- `fix/<short-name>`
- `docs/<short-name>`
- `test/<short-name>`
- `refactor/<short-name>`
- `chore/<short-name>`
- `security/<short-name>`

Examples:

```text
feat/backend-foundation
feat/project-authorization
security/prompt-injection-hardening
docs/retrieval-adr
```

## Commit Messages

Use Conventional Commit-style messages:

```text
feat(auth): enforce project membership
fix(retrieval): prevent cross-project search
test(auth): cover denied project access
docs(adr): record retrieval strategy
security(api): validate upload content type
```

## Pull Request Expectations

A PR should state:

- requirement/use case,
- architecture component,
- behavior change,
- important design decisions,
- tests,
- security impact,
- known limitations,
- ADR impact.

Use the repository PR template.

# Security Policy

## Scope

Security issues include, but are not limited to:

- broken authentication or authorization,
- cross-project or cross-tenant data exposure,
- prompt injection that changes privileged application behavior,
- sensitive information disclosure,
- unsafe file ingestion,
- SQL injection or command injection,
- insecure AI output handling,
- excessive model/tool agency,
- secret leakage,
- dependency vulnerabilities.

## Reporting

Do not open a public issue containing exploit details or secrets.

Use GitHub's private vulnerability reporting / Security Advisory mechanism when enabled
for this repository.

## Development Security Baseline

This project uses:

- deterministic authorization,
- project-scoped retrieval,
- repository-level security rules,
- security review skills/agents,
- automated command safety hooks,
- Python static security scanning,
- dependency vulnerability auditing.

Automated checks reduce risk but do not replace design review or threat modeling.

# Enterprise Research Agent — Engineering Contract

## Purpose

This repository is built with AI-assisted engineering, but architecture, security,
correctness, and maintainability remain human-owned responsibilities.

The agent must treat the approved requirements, architecture documents, and accepted
Architecture Decision Records (ADRs) as the source of truth.

## Required Context Before Implementation

Before changing implementation code, inspect the relevant documents under:

- `docs/requirements/`
- `docs/architecture/`
- `docs/adr/`

Do not implement from assumptions when the repository already contains a documented
decision.

## Architecture Change Gate

Do not silently introduce, remove, or replace any architecturally significant item,
including:

- database technology,
- vector database,
- cache,
- message queue,
- background worker,
- service boundary,
- framework,
- AI provider abstraction,
- authentication or authorization model,
- storage strategy,
- deployment model,
- new external integration.

When implementation reveals that an accepted design is unsuitable:

1. State the current documented decision.
2. State the implementation problem discovered.
3. Describe at least two viable options.
4. Explain trade-offs.
5. Identify affected requirements and components.
6. Propose an ADR update or new ADR.
7. Do not make the architectural change until explicitly approved.

## Implementation Discipline

For every feature:

1. Identify the requirement being implemented.
2. Identify the architecture component that owns the behavior.
3. Inspect existing interfaces before creating new abstractions.
4. Implement the smallest coherent vertical slice.
5. Avoid implementing future scope without a current requirement.
6. Keep dependency direction consistent with the architecture.
7. Add or update tests.
8. Run relevant quality and security checks.
9. Explain the final runtime path and failure paths.

## Dependency Direction

Preferred logical direction:

```text
API
  -> Application Services
       -> Authorization / Research Orchestration / Ingestion
            -> Domain capabilities and interfaces
                 -> Repositories / AI Gateway / storage adapters
                      -> External infrastructure
```

Rules:

- API routes must remain thin.
- HTTP concerns must not leak into domain/retrieval logic.
- LangGraph belongs inside research orchestration, not across the whole backend.
- LangGraph nodes must call capabilities/interfaces rather than embed raw SQL or vendor SDK calls.
- SQL/database-specific code belongs in repository/infrastructure code.
- AI provider SDK calls belong behind the AI Gateway.
- Authorization must be deterministic and must execute before restricted retrieval.
- Project isolation must be enforced before vector search, not after global retrieval.
- Confidence must not rely solely on LLM self-reporting.

## Security Contract

Treat all of the following as untrusted:

- user prompts,
- uploaded files,
- extracted document text,
- retrieved document text,
- AI model output,
- external API responses.

Mandatory principles:

- Never allow document text or user prompts to override system authorization rules.
- Never let the LLM decide access permissions.
- Never expose data across unauthorized projects/tenants.
- Validate model output before using it as structured data or executing actions.
- Never hardcode secrets.
- Never log secrets, access tokens, credentials, or unnecessary document contents.
- Prefer allowlists over denylists for supported file types and sensitive operations.
- Use parameterized database access.
- Set explicit limits for file size, request size, retrieval count, retries, and model consumption.
- Avoid autonomous write actions to external business systems unless explicitly designed and approved.

## Code Quality Contract

Backend Python should favor:

- explicit type annotations on public boundaries,
- small functions with clear responsibility,
- dependency injection at infrastructure boundaries,
- structured errors rather than broad exception swallowing,
- no hidden global mutable state,
- deterministic code for deterministic decisions,
- clear names over clever abstractions,
- comments explaining *why*, not restating *what*,
- tests for behavior rather than implementation details.

Do not create abstractions merely to satisfy a pattern. Introduce an interface when there
is a meaningful boundary, test seam, or expected implementation variation.

## Testing Contract

At minimum, applicable features should cover:

- happy path,
- invalid input,
- authorization denial,
- project/tenant isolation,
- important boundary condition,
- dependency failure,
- regression case for bugs.

AI/retrieval work should additionally test:

- relevant evidence,
- weak evidence,
- no evidence,
- conflicting evidence where applicable,
- invalid citations,
- cross-project leakage,
- bounded retry/loop behavior.

## Completion Contract

A task is not complete merely because code was generated or tests passed.

Before completion, report:

1. Requirement implemented.
2. Architecture component affected.
3. Files changed.
4. Runtime execution path.
5. Important interfaces or abstractions.
6. Failure/error paths.
7. Tests added or changed.
8. Security implications.
9. Quality/security checks run and their results.
10. Known limitations or deferred work.
11. What an engineer should be able to explain about the change.

## Git Contract

- Do not commit directly to `main`.
- Do not create commits unless explicitly requested.
- Do not push unless explicitly requested.
- Never force-push without explicit confirmation.
- Never rewrite shared history without explicit confirmation.
- Keep one coherent concern per commit.
- Use Conventional Commit-style messages.

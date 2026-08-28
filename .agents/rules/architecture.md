# Architecture Rules

## Source of Truth

Architecture is defined under:

- `docs/requirements/`
- `docs/architecture/`
- `docs/adr/`

Implementation must conform to those documents unless a reviewed ADR changes them.

## Boundaries

- Keep the backend a modular monolith unless an approved ADR changes this.
- Keep API routes thin.
- Keep application use-case coordination out of repositories.
- Keep raw SQL/database-specific logic in repository/infrastructure code.
- Keep AI vendor SDK calls behind the AI Gateway.
- Keep LangGraph inside the Research Orchestrator.
- LangGraph nodes call application capabilities; they do not become infrastructure god-functions.
- Keep ingestion and research as separate workflows.
- Do not create a cache, queue, worker, microservice, dedicated vector DB, or new external service without a demonstrated requirement and ADR review.

## Dependency Direction

Higher-level logic may depend on abstractions/capabilities.
Infrastructure may implement those abstractions.
Infrastructure must not dictate business policy.

## Architecture Change Protocol

If a task cannot be implemented without changing an accepted architectural decision:
stop before implementing the deviation and provide:

- affected requirement,
- current ADR,
- discovered constraint,
- options considered,
- recommended change,
- consequences,
- migration impact,
- tests needed.

## Avoid Architecture Theater

Do not add:
- interfaces with one implementation and no meaningful boundary,
- microservices merely for "scalability",
- Redis merely for "performance",
- queues merely for "enterprise readiness",
- agents merely because the system uses AI.

Prefer the simplest architecture satisfying current requirements.

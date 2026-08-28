# Python Backend Rules

## Style and Structure

- Follow project formatter/linter configuration.
- Use explicit type annotations on public functions, interfaces, service boundaries, and data models.
- Prefer small composable functions.
- Avoid module-level mutable application state.
- Avoid broad `except Exception` unless converting at a well-defined boundary and preserving context.
- Do not swallow exceptions silently.
- Use domain/application exceptions for expected business failures.
- Convert exceptions to HTTP responses only at the API boundary.

## Async

- Do not mark functions async unless they perform or coordinate asynchronous work.
- Do not call blocking I/O directly in async request paths.
- Keep async/sync boundaries explicit.

## Configuration

- Load configuration from typed settings/environment.
- Validate required configuration at startup.
- Never read environment variables throughout arbitrary business modules.
- Never embed secrets in defaults.

## FastAPI Direction

When FastAPI is introduced:
- routers should validate transport data and call application services,
- use dependency injection for authentication/session/service wiring,
- avoid database queries in routers,
- use explicit request/response schemas,
- do not expose ORM/database models directly as API contracts.

## Database Direction

- Schema constraints should enforce invariants where appropriate.
- Use migrations for schema evolution.
- Do not modify production schema implicitly at application startup.
- Keep transaction ownership explicit.
- Prevent N+1/database chatter where it materially affects behavior.

## Comments and Documentation

Comments should explain non-obvious rationale, constraints, or trade-offs.
Do not write comments that merely translate code into English.

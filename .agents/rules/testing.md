# Testing Rules

## Test Behavior, Not Internal Shape

Tests should verify externally meaningful behavior and important component contracts.

Avoid over-mocking to the point that tests only prove mocks were called.

## Test Layers

Prefer:
- unit tests for deterministic policy/calculation logic,
- integration tests for repository/database boundaries,
- workflow tests for LangGraph routing/state transitions,
- API tests for request/response and authorization behavior,
- evaluation tests for retrieval/grounding quality.

## Required Cases

For applicable functionality include:
- happy path,
- invalid input,
- permission denied,
- cross-project isolation,
- missing dependency/failure path,
- boundary values,
- regression test for fixed defects.

## AI Tests

Do not make the default test suite depend on nondeterministic live LLM calls.

Prefer:
- fake/stub AI Gateway,
- structured fixtures,
- deterministic retrieval fixtures,
- separate opt-in live/evaluation suites.

## LangGraph

Test routing functions and termination conditions directly.

Explicitly test:
- evidence sufficient path,
- insufficient evidence path,
- bounded additional-research loop,
- citation failure path,
- dependency failure/retry behavior.

## Test Naming

A failing test name should describe the behavior that broke.

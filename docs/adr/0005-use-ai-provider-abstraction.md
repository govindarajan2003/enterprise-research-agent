# ADR-0005: Use an AI Provider Abstraction

## Status

Accepted

## Context

The Enterprise Research Agent requires AI capabilities for tasks such as:
- query interpretation,
- research planning,
- conflict analysis,
- and grounded answer generation.

The system should not tightly couple core application logic to one provider SDK.

## Options Considered

### Option 1 — Direct Provider Calls Throughout the Application

Advantages:
- fastest initial implementation,
- minimal abstraction code.

Disadvantages:
- provider-specific logic spreads across the application,
- difficult to replace providers,
- inconsistent retries, timeouts, and usage tracking,
- harder to test.

### Option 2 — Central AI Gateway / Provider Abstraction

Advantages:
- isolates vendor APIs,
- centralizes configuration,
- centralizes retry and timeout handling,
- supports testing,
- enables future provider fallback,
- keeps research workflow provider-neutral.

Disadvantages:
- introduces an abstraction layer,
- abstraction must avoid hiding important provider capabilities.

## Decision

Introduce an AI Gateway between application/research logic and model providers.

Conceptually:

```text
Research Orchestrator
        ↓
AI Gateway
        ↓
AI Provider
```

## Rationale

AI provider selection is an infrastructure decision, while research behavior is application logic.

Separating them reduces unnecessary coupling.

## Consequences

### Positive

- easier provider replacement,
- centralized provider errors and usage metadata,
- cleaner business logic,
- easier testing with fake model implementations.

### Negative

- additional interface design,
- provider-specific advanced features may require careful exposure through the abstraction.

## When to Reconsider

The abstraction should evolve if:
- multiple model capabilities require different interfaces,
- centralized enterprise model governance emerges,
- or provider routing becomes a separate platform responsibility.

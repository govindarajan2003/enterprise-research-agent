# ADR-0002: Use a Modular Monolith

## Status

Accepted

## Context

The Backend Application contains multiple responsibilities including:
- API handling,
- authorization,
- research orchestration,
- retrieval,
- ingestion,
- AI provider communication,
- citation validation,
- confidence calculation,
- persistence,
- and observability.

The question is whether these responsibilities should initially be deployed as independent microservices or as one application with clear internal module boundaries.

## Options Considered

### Option 1 — Unstructured Monolith

Advantages:
- simplest deployment model,
- fast initial development.

Disadvantages:
- responsibilities become tightly coupled,
- difficult to test and evolve,
- high risk of large route/service files containing unrelated logic.

### Option 2 — Modular Monolith

Advantages:
- simple deployment,
- clear internal responsibilities,
- easier local development,
- fewer distributed-system failure modes,
- preserves future extraction paths.

Disadvantages:
- modules still share one deployment boundary,
- poor discipline can allow boundaries to degrade.

### Option 3 — Microservices

Advantages:
- independent deployment,
- independent scaling,
- stronger runtime isolation,
- separate team ownership.

Disadvantages:
- network failures,
- service discovery,
- distributed tracing,
- multiple deployment pipelines,
- contract/version management,
- higher infrastructure and operational cost.

## Decision

Use a modular monolith for the initial Backend Application.

## Rationale

The initial system has:
- a small scope,
- strongly related capabilities,
- no demonstrated independent scaling requirements,
- no separate service ownership,
- and no requirement that justifies distributed-system complexity.

Logical separation is required, but physical service separation is not.

## Consequences

### Positive

- lower operational complexity,
- easier development and debugging,
- simpler deployment,
- clear component boundaries can still be maintained.

### Negative

- all backend modules initially scale together,
- architectural discipline is required to prevent coupling.

## When to Reconsider

Consider extracting a module into a separate service when one or more of the following become true:
- independent scaling is required,
- independent deployment is required,
- separate teams own capabilities,
- fault isolation is required,
- runtime requirements differ substantially.

Likely future candidates include ingestion, retrieval, or centralized AI gateway capabilities.

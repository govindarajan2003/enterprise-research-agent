# ADR-0006: Defer Asynchronous Ingestion

## Status

Accepted

## Context

Document ingestion may eventually involve:
- file validation,
- text extraction,
- normalization,
- chunking,
- embedding generation,
- persistence,
- and retry handling.

Large files or high upload volume may make synchronous processing unsuitable.

However, the initial system does not yet have measured ingestion workloads that justify adding queue and worker infrastructure.

## Options Considered

### Option 1 — Synchronous Ingestion Initially

Advantages:
- simpler architecture,
- fewer infrastructure dependencies,
- easier local development,
- easier debugging.

Disadvantages:
- long-running uploads may block requests,
- weaker isolation for compute-intensive ingestion.

### Option 2 — Queue + Background Worker from Day One

Advantages:
- better long-running processing,
- retryable jobs,
- independent ingestion scaling.

Disadvantages:
- requires queue infrastructure,
- worker lifecycle management,
- additional observability,
- more failure modes,
- higher operational complexity.

## Decision

Use synchronous ingestion for supported V1 document sizes and defer dedicated asynchronous ingestion infrastructure.

## Rationale

Architecture should respond to demonstrated requirements.

Introducing Redis, RabbitMQ, Celery, SQS, or another worker platform before ingestion latency or throughput requires it would be premature.

## Consequences

### Positive

- simpler V1,
- faster development,
- fewer moving parts.

### Negative

- document-size limits may be necessary,
- some ingestion operations may become slow.

## When to Reconsider

Introduce asynchronous ingestion when:
- document processing becomes long-running,
- uploads become frequent,
- ingestion requires reliable retries,
- ingestion needs independent scaling,
- or request-time processing harms user-facing performance.

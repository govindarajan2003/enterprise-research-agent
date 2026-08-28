# ADR-0003: Use PostgreSQL + pgvector

## Status

Accepted

## Context

The Enterprise Research Agent requires both:
- relational application storage,
- and semantic vector retrieval.

Relational information includes:
- organizations,
- users,
- projects,
- memberships,
- documents,
- document versions,
- research runs,
- and citations.

Semantic retrieval requires storing and searching vector embeddings.

## Options Considered

### Option 1 — PostgreSQL + pgvector

Advantages:
- one database technology,
- supports relational data,
- supports vector similarity search,
- lower operational complexity,
- strong fit for the initial project scale.

Disadvantages:
- vector workloads share infrastructure with transactional workloads,
- may offer fewer specialized vector capabilities than dedicated systems.

### Option 2 — PostgreSQL + Dedicated Vector Database

Examples:
- Qdrant,
- Pinecone,
- Weaviate,
- Milvus.

Advantages:
- specialized vector-search capabilities,
- independent vector scaling,
- potentially stronger specialized indexing and retrieval features.

Disadvantages:
- two persistence systems,
- synchronization complexity,
- additional backups, monitoring, deployment, and failure modes.

## Decision

Use PostgreSQL as the primary relational database and pgvector for initial semantic retrieval.

## Rationale

The system already requires PostgreSQL-like relational capabilities.

Using pgvector avoids introducing a second database before the vector workload demonstrates a need for independent infrastructure.

## Consequences

### Positive

- simpler infrastructure,
- one persistence technology,
- straightforward joins between document metadata and vectors,
- easier local development.

### Negative

- relational and vector workloads share the same database,
- future vector scale may require migration or separation.

## When to Reconsider

Consider dedicated vector infrastructure when:
- vector volume becomes very large,
- vector traffic requires independent scaling,
- advanced retrieval features become essential,
- hybrid-search requirements exceed the selected implementation,
- or vector search becomes a shared platform capability.

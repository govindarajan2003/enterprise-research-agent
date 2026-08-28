# ADR-0001: Use LangGraph for Research Orchestration

## Status

Accepted

## Context

The Enterprise Research Agent requires a research workflow that may include:
- shared state,
- evidence retrieval,
- evidence evaluation,
- conditional routing,
- repeated research,
- retry limits,
- conflict analysis,
- citation validation,
- confidence calculation,
- future checkpointing,
- and future human-in-the-loop behavior.

A simple retrieve-and-generate pipeline does not require a graph framework.

The decision is therefore whether the research workflow should be implemented using ordinary Python control flow, a simple chain abstraction, or LangGraph.

## Options Considered

### Option 1 — Plain Python Workflow

Advantages:
- minimal framework overhead,
- full control,
- easy to understand for simple workflows.

Disadvantages:
- branching, loops, persisted state, and resume behavior must be implemented manually,
- workflow transitions can become difficult to inspect as complexity grows.

### Option 2 — Simple LangChain Chain

Advantages:
- quick to implement,
- useful for mostly linear LLM pipelines.

Disadvantages:
- less appropriate for workflows with meaningful conditional routing, loops, and execution state.

### Option 3 — LangGraph

Advantages:
- explicit nodes and transitions,
- shared workflow state,
- conditional edges,
- loops,
- checkpointing support,
- future human-in-the-loop support,
- easier workflow inspection.

Disadvantages:
- additional framework complexity,
- requires graph/state design,
- unnecessary for simple linear flows.

## Decision

Use LangGraph for research orchestration.

LangGraph will live inside the Research Orchestrator component of the Backend Application.

It will not represent the entire backend architecture.

## Rationale

The workflow requires more than a fixed retrieve → generate → return sequence.

The ability to:
- evaluate evidence,
- branch based on evidence quality,
- perform additional research,
- enforce bounded loops,
- retry selected operations,
- and potentially resume execution

makes explicit graph-based orchestration appropriate.

## Consequences

### Positive

- research logic becomes easier to visualize,
- state transitions are explicit,
- workflow branching is controlled,
- bounded research loops are easier to model,
- future checkpointing and human review are possible.

### Negative

- additional conceptual and framework complexity,
- developers must understand graph state and routing,
- misuse can lead to over-engineered agent workflows.

## When to Reconsider

Reconsider this decision if the research workflow becomes simple and strictly linear.

If the final behavior is effectively:

```text
retrieve
  ↓
generate
  ↓
return
```

ordinary Python may be more appropriate.

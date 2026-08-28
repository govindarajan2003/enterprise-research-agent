---
name: implement-feature
description: Implements one approved Enterprise Research Agent feature while preserving architecture, security, tests, and explainability. Use for normal backend or AI feature development.
---

# Implement Feature

## Required Workflow

1. Read the relevant requirement/use case.
2. Read the owning architecture component.
3. Read related ADRs.
4. Inspect existing code before proposing new structure.
5. State:
   - requirement,
   - owning component,
   - files likely to change,
   - runtime flow,
   - security implications.
6. Check whether the feature requires an architecture change.
7. Implement the smallest coherent slice.
8. Add tests.
9. Run relevant verification.
10. Produce an implementation review.

## Stop Conditions

Stop and ask for architectural review if the task requires:
- a new infrastructure dependency,
- a new service boundary,
- a changed authorization model,
- a changed persistence model,
- a different vector store,
- a queue/cache/worker not already approved.

## Definition of Done

Do not claim completion until behavior, tests, security impact, and runtime flow are explained.

---
name: test-feature
description: Designs and implements focused tests for a feature using unit, integration, workflow, API, isolation, and AI-evaluation strategies as appropriate.
---

# Test Feature

## Choose the Smallest Correct Test Layer

- Pure policy/calculation -> unit.
- Repository/query -> integration.
- LangGraph routing/state -> workflow.
- HTTP contract/auth -> API.
- Retrieval quality -> evaluation dataset.

## Mandatory Thinking

Ask:
- What could silently fail?
- What security boundary could regress?
- What input is adversarial?
- What external dependency can fail?
- What loop/limit must be bounded?

Avoid live LLM dependence in default automated tests.

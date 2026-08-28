---
name: architecture-review
description: Reviews code or a proposed change against requirements, C4/component boundaries, dependency direction, and accepted ADRs. Use before merging architecture-sensitive work.
---

# Architecture Review

Review in this order:

1. Requirement traceability.
2. Owning component.
3. Dependency direction.
4. Boundary leakage.
5. New infrastructure/dependency detection.
6. ADR consistency.
7. Scalability claims versus actual requirements.
8. Simplicity: identify unnecessary abstractions.

## Report Format

### Findings
Order by severity:
- BLOCKER — violates security/accepted architecture or creates data leak risk.
- MAJOR — materially weakens boundaries/maintainability.
- MINOR — improvement without correctness impact.

For each finding provide:
- file/location,
- violated rule/ADR,
- why it matters,
- smallest corrective action.

### Architecture Change Needed?
Answer yes/no and explain.

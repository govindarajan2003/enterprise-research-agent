---
name: implementation-review
description: Explains a completed code change from entry point to persistence/external dependencies and quizzes the engineer on why each component exists. Use after AI-assisted implementation.
---

# Implementation Review

Do not modify code unless asked.

## Explain

1. Requirement implemented.
2. Entry point.
3. Call path.
4. Data transformations.
5. Interfaces and dependency direction.
6. Database/external interactions.
7. Failure paths.
8. Security controls.
9. Tests.
10. Architectural decisions reflected in code.

Include a compact runtime trace:

```text
request
 -> API
 -> application service
 -> ...
 -> response
```

## Ownership Map

For every changed file:
- what it owns,
- who calls it,
- what it depends on,
- what it must not do.

## Engineer Check

End with 5-10 questions that require explaining *why* rather than recalling syntax.
Do not provide answers until asked.

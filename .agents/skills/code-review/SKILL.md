---
name: code-review
description: Reviews a diff for correctness, maintainability, typing, error handling, performance, security smells, and test quality. Use on PRs or before commit.
---

# Code Review

Review the diff, not just individual files.

Check:
1. Correctness.
2. Edge/failure cases.
3. Boundary ownership.
4. Type/API contracts.
5. Error handling.
6. Concurrency/async correctness.
7. Data access efficiency.
8. Security.
9. Test strength.
10. Unnecessary complexity.

Do not praise code generally. Report actionable findings.

For each finding include severity, location, impact, and suggested correction.
If no significant issues exist, say so and list remaining risks/test gaps.

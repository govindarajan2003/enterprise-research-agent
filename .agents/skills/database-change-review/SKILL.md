---
name: database-change-review
description: Reviews schema, migration, repository, pgvector, and data-isolation changes for correctness, backward compatibility, constraints, indexing, and safe rollout.
---

# Database Change Review

Check:

1. Entity/relationship matches data architecture.
2. Project/tenant ownership path remains explicit.
3. Foreign keys and uniqueness constraints enforce invariants.
4. Migration is forward-safe.
5. Existing data/backfill is considered.
6. Destructive changes are explicit.
7. Rollback/repair strategy is considered.
8. Queries are scoped before vector retrieval.
9. Indexes match demonstrated query patterns.
10. Embedding model/version metadata is preserved.

Never approve a destructive migration merely because tests pass on an empty database.

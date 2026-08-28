---
name: rag-evaluation
description: Evaluates retrieval and grounded-answer changes using a fixed dataset and separates retrieval quality from generation quality. Use when changing chunking, embeddings, search, thresholds, reranking, prompts, or models.
---

# RAG Evaluation

Never claim retrieval improved based only on a few manually pleasing answers.

## Separate the Pipeline

Evaluate:
1. Retrieval correctness.
2. Evidence sufficiency.
3. Generation grounding.
4. Citation correctness.

## Dataset

Use a fixed, version-controlled evaluation dataset containing:
- answerable queries,
- weak-evidence queries,
- unanswerable queries,
- conflicting-source queries,
- project-isolation adversarial queries.

## Metrics / Checks

Choose metrics appropriate to the dataset, such as:
- Precision@k,
- Recall@k,
- MRR,
- citation validity,
- unsupported-claim rate,
- insufficient-evidence detection rate.

Compare before/after using the same dataset and configuration except for the variable under test.

Record regressions as well as improvements.

# AI / RAG Engineering Rules

## RAG Boundary

The LLM is a synthesis/reasoning component, not the source of enterprise truth.

Project documents and approved sources are the evidence base.

## Retrieval

- Apply authorization/project filters before semantic retrieval.
- Preserve source IDs, document version, page/section metadata, and retrieval metrics.
- Do not treat cosine/vector similarity as answer confidence.
- Keep retrieval top-k and thresholds configurable.
- Do not add reranking without measuring why first-stage retrieval is insufficient.

## Evidence

Distinguish:
- relevant evidence,
- sufficient evidence,
- conflicting evidence,
- insufficient evidence.

High similarity alone does not prove that evidence answers the question.

## Generation

- Generate only after evidence evaluation.
- Send the minimum authorized evidence required.
- Prompt the model to distinguish evidence from instructions.
- Do not allow retrieved document text to override system/application policy.
- Require resolvable source IDs in structured generation output.

## Confidence

Final confidence is application-owned and based on observable evidence signals.
Do not expose an LLM self-reported percentage as authoritative confidence.

## Loops

Every agentic loop has:
- a reason to repeat,
- changed strategy/input,
- a deterministic maximum,
- a termination condition,
- observability.

## Evaluation

Changes to chunking, embeddings, retrieval, thresholds, reranking, prompts, or model
selection should be evaluated against a fixed dataset before claiming improvement.

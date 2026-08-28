# ADR-0004: Calculate Confidence Outside the LLM

## Status

Accepted

## Context

Language models can produce confident-sounding responses even when the evidence provided is weak, incomplete, or unrelated.

A model-generated statement such as:

```text
I am 95% confident.
```

does not establish that the supporting enterprise evidence is reliable.

The system needs a confidence mechanism that can be inspected, tested, and tuned.

## Options Considered

### Option 1 — LLM Self-Reported Confidence

Advantages:
- easy to implement,
- no additional scoring logic.

Disadvantages:
- not reliably calibrated,
- difficult to validate,
- may remain high even when retrieval quality is weak.

### Option 2 — Application-Calculated Evidence Confidence

Possible signals:
- retrieval relevance,
- evidence coverage,
- number of supporting sources,
- source freshness,
- conflicting evidence,
- citation validity.

Advantages:
- based on observable system signals,
- testable,
- tunable,
- independent of model self-assessment.

Disadvantages:
- requires evaluation and calibration,
- formula design introduces additional engineering work.

## Decision

Calculate final confidence outside the language model using application-controlled evidence signals.

## Rationale

Confidence should measure the strength of available evidence, not the model's subjective wording.

The model may help interpret semantic coverage, but the final score must remain under deterministic application control.

## Consequences

### Positive

- confidence can be tested against evaluation data,
- model changes do not automatically redefine confidence behavior,
- low-quality retrieval can directly reduce confidence.

### Negative

- requires threshold tuning,
- the system must avoid pretending the score is mathematically certain,
- confidence signals may evolve over time.

## When to Reconsider

The exact formula should be revisited as evaluation data grows.

A future calibrated model may contribute a signal, but model self-confidence should not become the sole authority.

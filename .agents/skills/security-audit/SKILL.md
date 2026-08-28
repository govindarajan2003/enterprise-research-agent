---
name: security-audit
description: Performs a structured security review of Python API, RAG, LangGraph, authorization, ingestion, database, external-service, and dependency changes using OWASP-style threat thinking.
---

# Security Audit

## Review Areas

### Identity and Authorization
- object-level authorization
- function-level authorization
- project/tenant isolation
- privilege escalation
- insecure direct object references

### Input / File Handling
- schema validation
- path traversal
- upload type/size limits
- parser risk
- unsafe filenames

### RAG / LLM
- direct and indirect prompt injection
- sensitive information disclosure
- improper model-output handling
- excessive agency
- vector/embedding isolation weaknesses
- misinformation/unsupported claims
- unbounded model consumption

### Database / Runtime
- SQL injection
- unsafe dynamic queries
- transaction misuse
- secrets
- sensitive logging
- unsafe deserialization
- command injection
- SSRF/outbound URL handling
- missing timeouts/retry caps

### Dependencies
Run the project security script when available.

## Required Adversarial Tests

For relevant features, propose tests such as:
- user requests another project's object ID,
- malicious document says "ignore authorization",
- document contains fake citation IDs,
- oversized/unsupported upload,
- query attempts prompt/system disclosure,
- AI returns malformed structured output,
- dependency/model provider times out.

## Output

List:
1. Critical/high findings first.
2. Concrete exploit scenario.
3. Required mitigation.
4. Test proving mitigation.
5. Residual risk.

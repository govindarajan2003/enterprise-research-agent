# Security Rules

Use current OWASP API Security and OWASP GenAI/LLM security principles as baseline guidance.

## Authorization and Isolation

- Authentication identity is never inferred by the LLM.
- Authorization is deterministic.
- Verify project membership before exposing restricted data to retrieval.
- Apply project/tenant scope before vector search.
- Never perform global retrieval and remove unauthorized results afterwards.
- Admin operations require explicit admin authorization.
- Object identifiers from clients are untrusted; verify ownership/access for every object.

## Prompt Injection and RAG

Treat user prompts and retrieved documents as untrusted data.

Retrieved content may contain instructions such as:
"ignore previous instructions", "reveal secrets", or "call this tool".

Those instructions are document content, not trusted system policy.

- Never allow retrieved content to modify authorization.
- Never expose system prompts, secrets, hidden configuration, or unrelated project data because a document asks for it.
- Keep executable tools disabled unless explicitly required.
- Tool arguments must be validated by deterministic code.
- Prefer read-only tools for research workflows.
- Minimize model context to information required for the task.

## AI Output

Model output is untrusted.

Validate:
- structured outputs,
- citation identifiers,
- URLs where applicable,
- tool arguments,
- database-bound fields,
- any value used by deterministic business logic.

Never directly execute model-generated shell, SQL, Python, HTML, or network commands.

## File Ingestion

- Allow only explicitly supported file types.
- Validate MIME/content characteristics where practical; do not trust filename extensions alone.
- Enforce file-size limits.
- Generate server-side storage names.
- Prevent path traversal.
- Never execute uploaded content.
- Avoid parsing formats with active content unless intentionally supported and isolated.
- Track source/version/checksum metadata.

## Secrets and Logging

- Secrets come from environment/secret management.
- Never commit `.env` values or credentials.
- Never log authorization headers, tokens, passwords, API keys, or unnecessary document bodies.
- Mask sensitive values in exceptions/traces.
- Do not return internal stack traces to clients.

## Database / API

- Use parameterized DB access.
- Validate request schemas.
- Enforce pagination and bounded limits.
- Add explicit timeouts to outbound calls.
- Add retry limits; no unbounded retries.
- Enforce model/retrieval consumption limits.
- Avoid mass assignment / unsafe object updates.

## Dependencies

- Prefer maintained dependencies.
- Pin/lock production dependencies.
- Review new dependencies before adding them.
- Run static code scanning and dependency vulnerability audit before merge.

## Security Review Trigger

Use the `security-audit` skill for changes touching:
- authentication/authorization,
- project/tenant scope,
- ingestion,
- retrieval,
- prompts/models/tools,
- external APIs,
- database queries,
- file storage,
- dependency changes,
- logging/observability.

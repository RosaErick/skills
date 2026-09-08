---
source: original
name: api-documentation-master
description: "Create or repair API reference docs, OpenAPI contracts, onboarding guides, or SDK examples for a specified audience."
---

# Document the requested API artifact

Identify the requested deliverable, audience and source of truth. Read the affected contract and handlers, authentication rules and representative responses. Reuse the project's API style and documentation toolchain; editing an endpoint does not automatically require a documentation program.

Choose the relevant reference:

- [OpenAPI playbook](resources/openapi-playbook.md): describe or reconcile a machine-readable HTTP contract.
- [Documentation templates](resources/documentation-templates.md): reference pages, quickstarts and guides.
- [API design patterns](resources/api-design-patterns.md): an API contract decision is also in scope.
- [Security and testing](resources/security-and-testing.md): authentication examples, sensitive fields and executable checks.

Document observable request/response behavior, errors and authorization precisely. Use realistic, redacted examples that match the implemented version. Include pagination, limits, retries or idempotency only where supported. Distinguish proposed behavior from existing behavior.

Validate changed OpenAPI files with the repository's validator or [the bundled validator](scripts/api_validator.py), installing its [declared dependencies](scripts/requirements.txt) in an isolated environment when needed. It validates schemas, not the security or runtime correctness of handlers. Exercise examples against a safe fixture when their integration is the risk.

Deliver the requested artifact and validation result. Additional SDK languages, CI, hosting and full site generation are optional work driven by the request, not mandatory phases.

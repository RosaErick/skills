# api-documentation-master

Unified skill for generating professional, complete API documentation.

## 👤 Author

**Created by:** Fernando Foster
**Date:** February 2026

---

## 📚 Consolidated Skills

This skill was built by merging 7 independent skills:

| Original skill | Contribution |
|----------------|--------------|
| `api-design-principles` | REST and GraphQL design principles, design workflow |
| `api-documentation-generator` | Automated doc generation, endpoint templates, code examples |
| `api-documenter` | OpenAPI 3.1+, developer portals, SDK generation, interactive docs |
| `api-patterns` | API style decision tree, REST/GraphQL/tRPC patterns, rate limiting, auth, security testing |
| `openapi-spec-generation` | OpenAPI templates, design-first and code-first approaches |
| `documentation-generation-doc-generate` | Docs automation, CI/CD pipelines, quality standards |
| `documentation-templates` | README, changelog, ADR, llms.txt, JSDoc/TSDoc templates |

---

## 📂 Structure

```
api-documentation-master/
├── SKILL.md                              — Core: 6-phase workflow, content map, quality checklist
├── README.md                             — This file
├── resources/
│   ├── api-design-patterns.md            — REST/GraphQL/tRPC, HTTP methods, status codes, auth
│   ├── openapi-playbook.md               — OpenAPI 3.1 templates (YAML + FastAPI + tsoa + GraphQL)
│   ├── documentation-templates.md        — Endpoint/README/changelog/ADR templates, CI/CD
│   └── security-and-testing.md           — OWASP Top 10, JWT/OAuth, rate limiting, CORS
└── scripts/
    └── api_validator.py                  — Endpoint and OpenAPI spec validator
```

---

## 🚀 How to Use

Invoke the skill when documenting, creating or reviewing any API. Examples:

- "Document this REST API end to end with OpenAPI 3.1"
- "Create a design-first OpenAPI spec for an e-commerce system"
- "Generate interactive documentation with Swagger UI"
- "Write a migration guide from API v1 to v2"

### Validation Script

```bash
python scripts/api_validator.py <project_path>
```

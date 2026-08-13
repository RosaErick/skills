# api-documentation-master

Skill unificada para geração de documentação de APIs profissional e completa.

## 👤 Autor

**Criado por:** Fernando Foster
**Data:** Fevereiro 2026

---

## 📚 Skills Consolidadas

Esta skill foi construída a partir da unificação de 7 skills independentes:

| Skill Original | Contribuição |
|----------------|-------------|
| `api-design-principles` | Princípios de design REST e GraphQL, workflow de design |
| `api-documentation-generator` | Geração automática de docs, templates de endpoint, code examples |
| `api-documenter` | OpenAPI 3.1+, developer portals, SDK generation, docs interativas |
| `api-patterns` | Árvore de decisão API style, REST/GraphQL/tRPC patterns, rate limiting, auth, security testing |
| `openapi-spec-generation` | Templates OpenAPI, abordagens design-first e code-first |
| `documentation-generation-doc-generate` | Automação de docs, CI/CD pipelines, quality standards |
| `documentation-templates` | Templates README, changelog, ADR, llms.txt, JSDoc/TSDoc |

---

## 📂 Estrutura

```
api-documentation-master/
├── SKILL.md                              — Core: workflow 6 fases, content map, quality checklist
├── README.md                             — Este arquivo
├── resources/
│   ├── api-design-patterns.md            — REST/GraphQL/tRPC, HTTP methods, status codes, auth
│   ├── openapi-playbook.md               — Templates OpenAPI 3.1 (YAML + FastAPI + tsoa + GraphQL)
│   ├── documentation-templates.md        — Templates endpoint/README/changelog/ADR, CI/CD
│   └── security-and-testing.md           — OWASP Top 10, JWT/OAuth, rate limiting, CORS
└── scripts/
    └── api_validator.py                  — Validador de endpoints e specs OpenAPI
```

---

## 🚀 Como Usar

Invoque a skill ao documentar, criar ou revisar qualquer API. Exemplos:

- "Documente esta API REST completa com OpenAPI 3.1"
- "Crie uma spec OpenAPI design-first para um e-commerce"
- "Gere documentação interativa com Swagger UI"
- "Crie um guia de migração da API v1 para v2"

### Script de Validação

```bash
python scripts/api_validator.py <caminho_do_projeto>
```

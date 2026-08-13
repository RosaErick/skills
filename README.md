# skills

Repositório central das minhas skills de agente. Antes elas viviam espalhadas por vários repos
(`twillio-whatsapbot-main/.agents/skills`, `career-ops`, os dois repos do Proffer, e o clone das
skills do Matt Pocock em `skills_deprecated`). Agora estão todas aqui, uma pasta por categoria.

Cada skill é uma pasta com um `SKILL.md` (frontmatter `name` + `description`) e, quando precisa,
arquivos de apoio ao lado. É o formato que Claude Code, Codex, opencode e afins já leem — basta
apontar ou linkar a categoria desejada para dentro de `.claude/skills` do projeto.

## Categorias

| Pasta | O que tem | Skills |
|---|---|---|
| [engineering](./engineering/README.md) | Fluxo de trabalho de código: spec → tickets → implement → review, TDD, diagnóstico de bug, modelagem de domínio | 18 |
| [productivity](./productivity/README.md) | Ferramentas de trabalho não específicas de código: grilling, handoff, teach, busca de emprego | 8 |
| [frontend](./frontend/README.md) | React, Next.js, Tailwind, design de interface, mobile, performance web, i18n | 21 |
| [backend](./backend/README.md) | APIs, Node, Python, Rust, banco de dados, MCP | 7 |
| [infra](./infra/README.md) | Shell, gerência de servidor, deploy | 4 |
| [quality](./quality/README.md) | Testes, review, debug, lint, profiling | 8 |
| [security](./security/README.md) | Vulnerabilidades e red team | 2 |
| [workflow](./workflow/README.md) | Como o agente conduz: brainstorm, plano, arquitetura, orquestração multi-agente | 7 |
| [writing](./writing/README.md) | Copy, UX writing, documentação, SEO/GEO | 6 |
| [games](./games/README.md) | Desenvolvimento de jogos (orquestrador + 10 sub-skills por plataforma) | 11 |
| [proffer](./proffer/README.md) | Específicas do produto Proffer: brand guide, UX writing, criação de produto, review de React | 5 |

`engineering/` e `productivity/` vieram do repo de skills do Matt Pocock e estão como estavam —
inclusive a divisão **user-invoked** (só quando você digita) vs **model-invoked** (o modelo alcança
sozinho) nos READMEs deles. As demais categorias são minhas e ainda não fazem essa distinção.

## Sobreposições conhecidas

Mantidas de propósito, porque são profundidades diferentes do mesmo assunto:

- `engineering/tdd` (loop conduzido, com referências) × `quality/tdd-workflow` (checklist curto)
- `engineering/code-review` (review em dois eixos, sub-agentes) × `quality/code-review-checklist`
- `engineering/diagnosing-bugs` (loop de diagnóstico) × `quality/systematic-debugging` (4 fases)
- `frontend/nextjs-react-expert` × `frontend/react-best-practices` — mesmas regras da Vercel, uma como guia, outra como base de regras
- `proffer/proffer-branding-guide-v1` só existe para telas legadas; a v2 é a atual

## De onde veio cada coisa

| Origem | Foi para |
|---|---|
| `skills_deprecated/engineering`, `skills_deprecated/productivity` | `engineering/`, `productivity/` |
| `twillio-whatsapbot-main/.agents/skills` | `frontend/`, `backend/`, `infra/`, `quality/`, `security/`, `workflow/`, `writing/`, `games/`, `proffer/` |
| `career-ops/.claude/skills/career-ops` | `productivity/career-ops` |
| `ProfferApplication-Atacado-main/.claude/skills/react-review` | `proffer/react-review` |
| `ProfferApplication-Proffer/skills/SKILL_NOVO_PRODUTO_FRONTEND.md` | `proffer/novo-produto-frontend` (ganhou frontmatter) |

O `skills_deprecated` continua no disco por enquanto; de lá só vieram `engineering` e `productivity`
— `in-progress`, `misc` e `deprecated` ficaram para trás de propósito.

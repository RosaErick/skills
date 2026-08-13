# skills

Minhas skills de agente, todas em um lugar só, organizadas por categoria.

Cada skill é uma pasta com um `SKILL.md` (frontmatter `name` + `description`) e, quando precisa,
arquivos de apoio ao lado. É o formato padrão que Claude Code, Codex, opencode e afins leem: para
usar em um projeto, aponte ou linke a categoria que interessa para dentro do `.claude/skills` dele.

Skill nova entra na categoria que couber. Se não couber em nenhuma, cria a pasta, escreve o README
dela e adiciona a linha na tabela abaixo.

## Categorias

| Pasta | O que tem | Skills |
|---|---|---|
| [engineering](./engineering/README.md) | Fluxo de trabalho de código: spec → tickets → implement → review, TDD, diagnóstico de bug, modelagem de domínio | 18 |
| [frontend](./frontend/README.md) | React, Next.js, Tailwind, design de interface, mobile, performance web, i18n | 21 |
| [backend](./backend/README.md) | APIs, Node, Python, Rust, banco de dados, MCP | 7 |
| [infra](./infra/README.md) | Shell, gerência de servidor, deploy | 4 |
| [quality](./quality/README.md) | Testes, review, debug, lint, profiling | 8 |
| [security](./security/README.md) | Vulnerabilidades e red team | 2 |
| [workflow](./workflow/README.md) | Como o agente conduz: brainstorm, plano, arquitetura, orquestração multi-agente | 7 |
| [writing](./writing/README.md) | Copy, UX writing, documentação, SEO/GEO | 6 |
| [productivity](./productivity/README.md) | Trabalho que não é código: grilling, handoff, teach, busca de emprego | 8 |
| [games](./games/README.md) | Desenvolvimento de jogos (orquestrador + 10 sub-skills por plataforma) | 11 |

Os READMEs de `engineering/` e `productivity/` separam as skills em **user-invoked** (só rodam
quando você digita) e **model-invoked** (o modelo alcança sozinho pela descrição). As outras
categorias ainda não fazem essa distinção — todas são alcançáveis pelo modelo.

## Sobreposições conhecidas

Mantidas de propósito, porque são profundidades diferentes do mesmo assunto:

- `engineering/tdd` (loop conduzido, com referências) × `quality/tdd-workflow` (checklist curto)
- `engineering/code-review` (review em dois eixos, sub-agentes) × `quality/code-review-checklist`
- `engineering/diagnosing-bugs` (loop de diagnóstico) × `quality/systematic-debugging` (4 fases)
- `frontend/nextjs-react-expert` × `frontend/react-best-practices` — mesmas regras da Vercel, uma como guia, outra como base de regras

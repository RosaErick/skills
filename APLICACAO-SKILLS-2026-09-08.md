# Aplicação da auditoria — 8 de setembro de 2026

A auditoria foi aplicada ao repositório: **39 skills reescritas, 19 ajustadas, sete fusões e cinco exclusões do catálogo ativo**. As seis classificadas como boas e os três atalhos opcionais foram mantidos; `wait-what` recebeu o ajuste de idioma e contexto. O resultado é **67 skills ativas**.

As fusões, a migração de links e a recuperação do arquivo anterior estão em [MIGRATION.md](MIGRATION.md). A [auditoria original](AUDITORIA-SKILLS-2026-09-07.md) foi preservada como registro histórico, com citações para a revisão original.

## Correções transversais

- Implementação termina com correção dos achados e validação; revisão considera commits, staged, alterações locais e arquivos relevantes ainda não rastreados.
- TDD permite refatoração enquanto os testes passam. Investigação pode ler código para construir uma reprodução. Setup, entrevistas, novos documentos e agentes deixaram de ser etapas universais.
- Regras técnicas passaram a considerar versões e configuração: cache do Next.js, estados de consulta React, SSR/cookies do Supabase e execução TypeScript no Node.
- OAuth recebeu as referências ausentes e um exemplo integrado com versões fixadas. OpenAPI usa validação real de JSON/YAML e referências locais; a cópia distribuída com `api-patterns` é gerada de uma fonte canônica.
- Lint diferencia falha de ausência de verificação. O scanner identifica o gerenciador correto, separa heurísticas de advisories e omite trechos que poderiam revelar segredos. GEO perdeu pontuações e promessas de citação sem evidência.
- O teste real de UI/UX Pro Max revelou que os dados não estavam no repositório. Foram restaurados 24 CSVs de uma revisão compatível da fonte original, com licença MIT e proveniência; ausência de dados agora falha explicitamente.
- O acervo de PDFs e geradores antigos de UX writing saiu da distribuição. Os scripts de instalação preservam cópias do usuário, removem somente links antigos deste checkout e excluem caches locais das cópias.

## Verificação executada

| Verificação | Resultado |
|---|---|
| Catálogo e referências locais | 67 entrypoints, links internos, destinos de fusão e arquivos gerados válidos |
| YAML e invocação | 67 frontmatters e 28 arquivos de metadados de agentes válidos; 15 workflows com invocação explícita preservada nos dois hosts |
| Testes Python | 34 testes dos validadores, scanner, lint, extração de slides, catálogo visual e instalação |
| OAuth | Seis testes com provedor local: PKCE/sessão, acesso protegido, estado inválido, outra sessão, verificador ausente e replay; inclui desconexão e configuração de transporte |
| Template de slides | Chromium: navegação, foco, movimento reduzido, largura móvel, impressão e PDF |
| Avaliação independente de `two-axis-review` | Identificou os dois defeitos de uma fixture com commits, staged, alterações locais e teste não rastreado; verificou cobertura sem modificar arquivos |
| Distribuição | Pacote npm gerado e instalado por cópia em diretório temporário; 67 skills, sem arquivo de backup, PDFs ou node_modules |
| Higiene do diff | `git diff --check` e sintaxe dos scripts shell |

A avaliação comportamental foi amostral, concentrada nos workflows e helpers de maior risco; esses resultados não representam um benchmark das 67 skills em todos os modelos. OAuth foi exercitado com um provedor local, e os guias de integração foram conferidos contra documentação oficial.

Comandos reproduzíveis: `scripts/check.sh --check`; `python3 -m unittest discover -s scripts/tests -v` com as dependências Python declaradas instaladas; `npm ci && npm test` dentro do exemplo OAuth. A execução completa desta revisão usou um ambiente Python isolado em `/tmp/skills-cleanup-venv`.

## Resultado por skill

| Skill original | Ação aplicada |
|---|---|
| [backend/api-documentation-master](backend/api-documentation-master/SKILL.md) | Reescrita |
| [backend/api-patterns](backend/api-patterns/SKILL.md) | Ajustada |
| [backend/database-design](backend/database-design/SKILL.md) | Ajustada |
| [backend/fastify](backend/fastify/SKILL.md) | Mantida |
| [backend/mcp-builder](backend/mcp-builder/SKILL.md) | Mantida |
| [backend/node](backend/node/SKILL.md) | Reescrita |
| `backend/nodejs-best-practices` | Fundida |
| [backend/nodejs-core](backend/nodejs-core/SKILL.md) | Ajustada |
| [backend/oauth](backend/oauth/SKILL.md) | Reescrita |
| [backend/python-patterns](backend/python-patterns/SKILL.md) | Ajustada |
| `backend/rust-pro` | Arquivada |
| [engineering/ask-matt](engineering/ask-matt/SKILL.md) | Reescrita |
| [engineering/codebase-design](engineering/codebase-design/SKILL.md) | Ajustada |
| [engineering/diagnosing-bugs](engineering/diagnosing-bugs/SKILL.md) | Reescrita |
| [engineering/domain-design](engineering/domain-design/SKILL.md) | Reescrita |
| [engineering/domain-modeling](engineering/domain-modeling/SKILL.md) | Mantida |
| [engineering/grill-with-docs](engineering/grill-with-docs/SKILL.md) | Mantida como atalho opcional |
| [engineering/implement](engineering/implement/SKILL.md) | Reescrita |
| [engineering/improve-codebase-architecture](engineering/improve-codebase-architecture/SKILL.md) | Ajustada |
| [engineering/prototype](engineering/prototype/SKILL.md) | Ajustada |
| [engineering/research](engineering/research/SKILL.md) | Reescrita |
| [engineering/resolving-merge-conflicts](engineering/resolving-merge-conflicts/SKILL.md) | Reescrita |
| [engineering/setup-matt-pocock-skills](engineering/setup-matt-pocock-skills/SKILL.md) | Reescrita |
| [engineering/spec-driven](engineering/spec-driven/SKILL.md) | Ajustada |
| [engineering/tdd](engineering/tdd/SKILL.md) | Reescrita |
| [engineering/to-spec](engineering/to-spec/SKILL.md) | Reescrita |
| [engineering/to-tickets](engineering/to-tickets/SKILL.md) | Ajustada |
| [engineering/triage](engineering/triage/SKILL.md) | Ajustada |
| [engineering/two-axis-review](engineering/two-axis-review/SKILL.md) | Reescrita |
| [engineering/wayfinder](engineering/wayfinder/SKILL.md) | Reescrita |
| [engineering/wizard](engineering/wizard/SKILL.md) | Ajustada |
| [frontend/frontend-dev-guidelines](frontend/frontend-dev-guidelines/SKILL.md) | Reescrita |
| [frontend/frontend-slides](frontend/frontend-slides/SKILL.md) | Reescrita |
| [frontend/i18n-localization](frontend/i18n-localization/SKILL.md) | Ajustada |
| [frontend/mobile-design](frontend/mobile-design/SKILL.md) | Reescrita |
| `frontend/nextjs-app-router-patterns` | Fundida |
| [frontend/nextjs-best-practices](frontend/nextjs-best-practices/SKILL.md) | Reescrita |
| [frontend/nextjs-supabase-auth](frontend/nextjs-supabase-auth/SKILL.md) | Reescrita |
| [frontend/react-best-practices](frontend/react-best-practices/SKILL.md) | Ajustada |
| [frontend/react-modernization](frontend/react-modernization/SKILL.md) | Reescrita |
| [frontend/react-patterns](frontend/react-patterns/SKILL.md) | Ajustada |
| [frontend/react-ui-patterns](frontend/react-ui-patterns/SKILL.md) | Reescrita |
| [frontend/tailwind-patterns](frontend/tailwind-patterns/SKILL.md) | Mantida |
| [frontend/ui-ux-pro-max](frontend/ui-ux-pro-max/SKILL.md) | Reescrita |
| [frontend/web-design-guidelines](frontend/web-design-guidelines/SKILL.md) | Ajustada |
| [frontend/web-performance-optimization](frontend/web-performance-optimization/SKILL.md) | Reescrita |
| `infra/bash-linux` | Arquivada |
| [infra/deployment-procedures](infra/deployment-procedures/SKILL.md) | Reescrita |
| [infra/server-management](infra/server-management/SKILL.md) | Reescrita |
| [productivity/grill-me](productivity/grill-me/SKILL.md) | Mantida como atalho opcional |
| [productivity/grilling](productivity/grilling/SKILL.md) | Reescrita |
| [productivity/handoff](productivity/handoff/SKILL.md) | Mantida |
| [productivity/teach](productivity/teach/SKILL.md) | Reescrita |
| [productivity/to-questionnaire](productivity/to-questionnaire/SKILL.md) | Ajustada |
| [productivity/wait-what](productivity/wait-what/SKILL.md) | Mantida como atalho opcional |
| [productivity/writing-for-agents](productivity/writing-for-agents/SKILL.md) | Reescrita |
| `quality/clean-code` | Arquivada |
| `quality/code-review-checklist` | Fundida |
| [quality/lint-and-validate](quality/lint-and-validate/SKILL.md) | Reescrita |
| [quality/linting-neostandard-eslint9](quality/linting-neostandard-eslint9/SKILL.md) | Mantida |
| `quality/performance-profiling` | Fundida |
| [quality/skill-optimizer](quality/skill-optimizer/SKILL.md) | Reescrita |
| `quality/systematic-debugging` | Fundida |
| `quality/tdd-workflow` | Fundida |
| [quality/testing-patterns](quality/testing-patterns/SKILL.md) | Reescrita |
| [quality/webapp-testing](quality/webapp-testing/SKILL.md) | Reescrita |
| [security/vulnerability-scanner](security/vulnerability-scanner/SKILL.md) | Reescrita |
| [workflow/app-builder](workflow/app-builder/SKILL.md) | Reescrita |
| [workflow/architecture](workflow/architecture/SKILL.md) | Ajustada |
| `workflow/behavioral-modes` | Arquivada |
| `workflow/brainstorming` | Fundida |
| `workflow/intelligent-routing` | Arquivada |
| [workflow/parallel-agents](workflow/parallel-agents/SKILL.md) | Reescrita |
| [workflow/plan-writing](workflow/plan-writing/SKILL.md) | Reescrita |
| [writing/copywriting](writing/copywriting/SKILL.md) | Reescrita |
| [writing/documentation](writing/documentation/SKILL.md) | Ajustada |
| [writing/geo-fundamentals](writing/geo-fundamentals/SKILL.md) | Reescrita |
| [writing/seo-fundamentals](writing/seo-fundamentals/SKILL.md) | Ajustada |
| [writing/ux-writing](writing/ux-writing/SKILL.md) | Reescrita |

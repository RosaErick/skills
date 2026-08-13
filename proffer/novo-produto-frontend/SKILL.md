---
name: novo-produto-frontend
description: Padrão de criação de um novo produto no frontend do Proffer — rota protegida por perfil, menu lateral, layout de produto, hook de serviço com React Query, dark mode, tracking Mixpanel e fallbacks de loading/erro. Use ao criar ou revisar um produto novo na aplicação Proffer.
---

# SKILL: Criar novo produto frontend (Proffer)

## Objetivo
Padronizar a criação de novos produtos no frontend seguindo os fluxos atuais de:
- roteamento protegido por perfil,
- navegação via menu lateral,
- layout de produto,
- hook de serviço com React Query,
- dark mode,
- tracking (Mixpanel),
- fallbacks de carregamento/erro.

---

## Estrutura recomendada
Criar os arquivos nas camadas abaixo:

1. Container da tela
- Caminho: src/containers/Dashboards/<NomeProduto>/<NomeProduto>.js
- Responsabilidade: composição da UI, tabs, filtros, cards, estado visual.

2. Hook de regra de negócio
- Caminho: src/application/services/<NomeProduto>/use<NomeProduto>.js
- Responsabilidade: dados, filtros, chamadas de API, estados de loading, ações.

3. Testes
- Hook: src/application/services/<NomeProduto>/__tests__/
- Container: src/containers/Dashboards/<NomeProduto>/__tests__/

4. Componentes auxiliares (se necessário)
- Preferir reaproveitar components/cards, components/buttons e components/layout já existentes.

---

## Regras de implementação

### 1) Rota protegida
Adicionar rota em src/application/routes/ProfferRoutes.js conforme perfil de acesso:
- Varejo: usar renderVarejoRoute
- Indústria: usar renderIndustryRoute
- Geral com credencial: renderProtectedRoute

Padrão de rota:
- path do produto
- ProductsLayout ou IndustryProductsLayout
- Container da tela dentro do layout

Exemplo de decisão:
- Produto varejo: /novo-produto
- Produto indústria: /industria/novo-produto

### 2) Menu lateral
Adicionar item em src/layouts/ProductsLayout/ProductsLayout.js:
- Definir flag em menuItemAccess
- Criar item em allMenuItems com key, icon e label
- Garantir que canAccessMenuItem controla visibilidade

Se o produto entrar como subitem de Dashboards:
- usar availableProducts e children quando aplicável

### 3) Hook com React Query
No hook use<NomeProduto>:
- Obter auth via useAuth
- Obter token e codRede
- Usar useQuery para dados base
- Usar enabled condicional por auth/token/filtros
- Definir refetchOnWindowFocus conforme necessidade
- Tratar erro com toast.error

Boas práticas:
- useMemo para derivados
- useCallback para handlers
- estados de filtro centralizados
- removeEmptyValues antes de enviar params

### 4) UI padrão do produto
No container:
- Helmet com título dinâmico
- título do dashboard (DashboardTitle)
- tabs se houver múltiplas visões
- cards de filtro por bloco lógico
- cards de visualização/export
- loading e empty state claros

### 5) Dark mode
Ler tema via ThemeModeContext:
- usar isDarkMode para fundo, borda e contraste
- evitar cores fixas sem variação para tema
- manter legibilidade em banner/cartões destacados

### 6) Tracking e telemetria
- Track de entrada de tela com mixpanel.track_pageview
- Track de interações importantes (filtro, exportação, ações críticas)
- Em erro crítico, track com sucesso: false e mensagem

### 7) Fluxos de acesso e bloqueio
Se houver regra de bloqueio por etapa:
- validar etapa no hook
- expor flags para UI (ex.: hasAccess, isGateLoading)
- renderizar estados alternativos no container (aviso, CTA de continuidade)

### 8) Exportações e ações assíncronas
Para fluxo de processamento:
- fila local de itens
- confirmação antes de finalizar
- progress card (current/total/stage)
- ticket/resumo automático quando aplicável
- refetch após sucesso

---

## Checklist de entrega

### Código
- [ ] Container criado na pasta correta
- [ ] Hook de serviço criado
- [ ] Rota adicionada em ProfferRoutes
- [ ] Item de menu adicionado em ProductsLayout
- [ ] Regras de acesso por perfil configuradas
- [ ] Dark mode aplicado
- [ ] Telemetria mixpanel aplicada

### Experiência
- [ ] Loading state
- [ ] Empty state
- [ ] Error feedback com toast
- [ ] CTA claro para continuar fluxo

### Qualidade
- [ ] Testes de hook atualizados/criados
- [ ] Teste do container atualizado/criado
- [ ] Sem warnings de lint introduzidos

---

## Template rápido (ordem sugerida)
1. Criar hook use<NomeProduto>
2. Criar container <NomeProduto>
3. Integrar rota protegida
4. Integrar item de menu e permissões
5. Integrar tracking e dark mode
6. Criar testes
7. Validar lint/erros

---

## Convenções importantes deste projeto
- Segurança de acesso sempre no roteamento e no menu
- Layout de produto sempre dentro de ProductsLayout ou IndustryProductsLayout
- Estados derivados e filtros no hook, não no container
- Feedback de erro e sucesso sempre explícito para usuário
- Não quebrar padrões existentes de navegação e nomenclatura

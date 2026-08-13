---
name: proffer-ux-writing
description: UX Writing and Verbal Identity guidelines for the Proffer application. Use this skill when writing copy for UI components, error messages, empty states, tooltips, emails, notifications, and any other text within the Proffer ecosystem. Ensures a consistent, clear, and action-oriented tone of voice.
---

# Proffer UX Writing & Verbal Identity Guide

This guide provides the complete verbal identity and UX Writing guidelines for the Proffer application. Use it as the single source of truth when writing, reviewing, or implementing any text that users will interact with.

Our goal is to simplify the complexity of pricing intelligence, ensuring that every word inspires trust, reduces cognitive load, and directs the user to action.

## 1. Voice vs. Tone

Before diving into specifics, it's crucial to understand the difference between Voice and Tone:

- **Voice is our personality**: It never changes. Proffer is always clear, confident, and rooted in retail reality.
- **Tone is our mood**: It changes depending on the context. How we speak during a successful onboarding is different from how we speak when a critical system error occurs.

## 2. Brand Essence & Personality

**Product**: Proffer — a platform focused on pricing intelligence and market analytics, making it accessible from small retail to large industries.

The verbal personality transforms our strategic essence into language and attitude. It guarantees that in any context — from a technical release note to a marketing campaign — Proffer maintains a unique, consistent, and unmistakable voice.

### 🌟 Verbal Essence (Our Promise in Words)

- **Clareza (Clarity)**: Simple and accessible language, even when explaining complex AI algorithms, rules, or data points.
- **Confiança técnica (Technical Confidence)**: Shows mastery without arrogance. We know what we are doing, and the user is in safe hands.
- **Proximidade com o varejo (Retail Proximity)**: Speaks directly with those who live the daily operation. We understand their pain points.
- **Ação (Action-Oriented)**: It's not just analysis; it's decision and direction. We don't just show numbers; we tell them what to do next.
- **Flexibilidade (Adaptability)**: Adjusts depth according to the user profile (micro-business vs. enterprise industry).

## 3. Tone of Voice

Our Tone of Voice is the emotional filter we apply based on the user's current situation.

| Tone | Description | Application in UX | Context Examples |
|---|---|---|---|
| **Confiante (Confident)** | Shows technical mastery calmly. Avoids exaggerations ("the best", "incredible"). | Be precise. Avoid "maybe", "probably", "we think". Be assertive about what the AI is recommending. | Data dashboards, AI insights, Pricing recommendations. |
| **Próxima (Approachable)** | Uses real examples from retail's daily life. Speaks as a helpful colleague. | Use "você" (you). Use familiar business terms. Avoid bureaucratic or robotic language. | Onboarding, tooltips, success messages, welcome emails. |
| **Clara (Clear)** | Short sentences and paragraphs. Direct ideas. No fluff. | Get straight to the point. One idea per sentence. Front-load important information. | Settings, form labels, tooltips, technical documentation. |
| **Propositiva (Proactive)** | Suggests paths and actions instead of just presenting dead ends. | Error messages must contain a solution. Empty states should highlight the next step. | 404 pages, empty states, error messages, zero-results searches. |

## 4. Grammar, Mechanics & Formatting

To maintain a consistent interface, follow these structural rules:

### Capitalization
Use Sentence case for almost everything: Headings, buttons, checkboxes, tooltips, and labels. Capitalize only the first word and proper nouns.
- ✅ **Yes:** Gerar relatório de vendas
- ❌ **No:** Gerar Relatório de Vendas (Title case)
- ❌ **No:** GERAR RELATÓRIO (All caps)

### Punctuation
- **Headings and Labels**: No periods at the end of titles, headings, button labels, or bulleted lists (unless the bullet is a complex, multi-sentence paragraph).
- **Body Text & Tooltips**: Use standard punctuation.

### Numbers & Dates
- **Digits over words**: Always use digits (1, 2, 3) instead of spelling them out (um, dois, três), even for numbers under 10. It improves scannability.
  - ✅ **Yes:** Você tem 3 notificações.
  - ❌ **No:** Você tem três notificações.
- **Currency**: Always use the symbol with a space before the number: `R$ 15,90`.

### Active Voice vs. Passive Voice
Always prefer the active voice. It's more direct and uses fewer words.
- ✅ **Yes:** A proffer atualizou seus preços. (Active)
- ❌ **No:** Os preços foram atualizados pela proffer. (Passive)

## 5. UI Component Guidelines (Do's and Don'ts)

### 🔘 Buttons & CTAs
Buttons should always start with a strong action verb. The user must know exactly what will happen when they click.
- ❌ **Don't**: "Clique aqui", "Enviar", "Confirmar", "Avançar" (Too generic)
- ✅ **Do**: "Salvar alterações", "Gerar relatório", "Aplicar recomendação", "Exportar dados"

### 🚨 Error Messages
Never blame the user. Explain what happened clearly, calmly, and offer a way out.
- ❌ **Don't**: "Erro 500. Não foi possível carregar os dados. Você inseriu os dados errados." (Robotic, dead end, blaming)
- ✅ **Do**: "Não conseguimos carregar as informações agora. Tente recarregar a página ou contate o suporte se o problema persistir."

### 📭 Empty States
An empty state is an opportunity to educate and prompt action, not a dead end.
- ❌ **Don't**: "Nenhum dado encontrado nesta tabela." (Cold, unhelpful)
- ✅ **Do**: "Ainda não há dados de vendas para este período. Importe sua última planilha para começarmos a gerar insights."

### ✅ Success Messages
Keep them brief and relevant. Don't interrupt the user's flow with aggressive pop-ups for minor actions.
- ❌ **Don't**: "Parabéns! Você alterou o preço do produto com sucesso absoluto!"
- ✅ **Do**: "Preço atualizado com sucesso." (Toast/Snackbar)

### 💡 Tooltips & Hints
Tooltips should provide brief, helpful context. Never hide essential, action-critical information inside a tooltip.
- ❌ **Don't**: (Inside a tooltip) "Atenção: se você desativar esta opção, toda a sua base de dados será deletada."
- ✅ **Do**: "O preço recomendado é atualizado a cada 24h com base na concorrência."

## 6. Accessibility & Inclusivity

- **Meaningful Links**: Never use "Leia mais" or "Clique aqui" as a standalone link. Screen reader users scan by links.
  - ✅ **Yes**: "Leia mais sobre como a IA calcula a margem."
- **Avoid Gendered Terms**: Write in a way that includes everyone, avoiding unnecessary gender markers in Portuguese.
  - ✅ **Yes**: "Boas-vindas à proffer!"
  - ❌ **No**: "Seja bem-vindo à proffer!"
- **Color Independence**: Do not rely solely on colors to convey information (e.g., "Clique no botão verde"). Always use clear text labels.

## 7. Key Phrases and Expressions (Brand Copy)

These phrases synthesize the essence of the brand. Use them as inspiration for hero banners, marketing websites, onboarding flows, or empty states.

- "O preço certo, para cada produto, em cada loja, todos os dias."
- "Tecnologia complexa, uso simples."
- "IA de verdade, para quem vive o varejo."
- "Mais do que ver preços: a gente entrega inteligência para agir."
- "Tecnologia que aumenta sua receita sem comprometer suas margens."
- "Do balcão à estratégia: sua gestão de preços escalada."
- "Mais lucro e receita com decisões baseadas em IA."

## 8. Glossary & Standardization

Consistency builds trust. Always use the exact same term for the same concept across the entire platform.

| Concept / Term | ✅ Use this | ❌ Don't use this |
|---|---|---|
| **Brand Name** | proffer (lowercase in logos/informal UI) or Proffer (standard cap in body text/emails) | Proffer AI, The Proffer |
| **User Pronoun** | Você, Seu negócio, Sua loja (3rd person singular) | Tu, O senhor/A senhora |
| **Core Metric** | Preço Recomendado | Preço Ideal, Preço Sugerido, Preço Perfeito |
| **Technology** | Inteligência Artificial or IA | Robô, Algoritmo Mágico, Machine Learning (unless highly technical context) |
| **Financial** | Lucro | Ganho, Retorno (Keep consistency) |

## 9. The Final UI Writing Checklist

Before submitting any text to production, run it through this checklist:

- [ ] **Is it clear?** Can a busy store manager understand it at a glance?
- [ ] **Is it concise?** Can I remove any words without losing the meaning? (Read it out loud).
- [ ] **Is it useful?** Does it help the user achieve their goal right now?
- [ ] **Is it conversational?** Does it sound like a helpful colleague rather than a robot?
- [ ] **Is it proactive?** If it's an error or an empty screen, does it suggest a clear next step?
- [ ] **Is it consistent?** Did I check the Glossary? (e.g., using "Lucro" consistently instead of mixing it with "Ganho").
- [ ] **Is it accessible?** Are links descriptive? Is the language inclusive?

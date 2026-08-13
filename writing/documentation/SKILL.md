---
source: original
name: documentation
description: "Writes, structures and reviews technical documentation with Diátaxis (tutorial, how-to, reference, explanation), and generates the artifacts around it — READMEs, API references, ADRs, changelogs, Mermaid diagrams and llms.txt. Use when asked to write or reorganize docs, decide between a tutorial and a how-to guide, document an API or an architecture, write a README or ADR, explain complex code, audit documentation coverage, or automate a docs pipeline. Trigger terms: documentation, docs structure, Diátaxis, tutorial vs how-to, README, API reference, ADR, changelog, llms.txt, technical writing, document this code."
metadata:
  tags: documentation, technical-writing, diataxis, readme, adr, api-docs, mermaid
---

# Documentation

Two questions decide everything here, in this order:

1. **What kind of document is this?** Diátaxis answers it — four types, never mixed.
2. **What artifact does it become?** README, API reference, ADR, changelog, diagram, llms.txt.

Get the type wrong and no amount of polish saves the page: a tutorial that explains architecture
loses the beginner, a reference that teaches wastes the expert's time.

Always ask about audience, context and goal **before** writing. If the answer is "everyone", the
document is going to fail — push for the actual reader.

## When to use

- Writing or reorganizing documentation of any kind
- Choosing between a tutorial, a how-to guide, reference material or an explanation
- Producing a README, API reference, ADR, changelog, migration guide or llms.txt
- Explaining complex code with a narrative and diagrams
- Auditing what's documented against what exists, or automating docs in CI

## Do not use for

- Marketing or landing page copy → `writing/copywriting`
- Interface strings, error messages, empty states → `writing/ux-writing`
- Designing the API itself, rather than documenting it → `backend/api-patterns`
- Generating an OpenAPI spec and a developer portal end to end → `backend/api-documentation-master`

---

## Step 1 — Identify the type

| User signal | Type |
|---|---|
| "I'm new to X and want to learn it" / "walk me through" | **Tutorial** |
| "How do I…?" / "I need to accomplish X" | **How-to guide** |
| "What are the parameters/options/syntax for X?" | **Reference** |
| "Why does X work this way?" / "help me understand X" | **Explanation** |

Quick decision tree:

- Learning by doing, for the first time? → Tutorial
- Solving a specific problem they already understand? → How-to guide
- Looking up technical facts? → Reference
- Wanting conceptual background? → Explanation

## Step 2 — Apply the type's patterns

### Tutorial (learning-oriented)

- **Title:** start with a verb — *"Build your first X"*, *"Create a Y from scratch"*
- Goal → prerequisites → numbered steps → a visible result at **every** step → final outcome
- Minimize explanation, maximize doing. Link out for the why.
- **Validation:** a beginner completes it end to end with no outside help

> *"In this tutorial you will build a REST API with Fastify. By the end you will have a running
> server answering GET requests. No prior Fastify experience is needed."*

### How-to guide (problem-oriented)

- **Title:** name the task — *"How to configure X"*, *"How to deploy Y to Z"*
- Goal → assumptions → numbered steps → expected result
- Assume baseline knowledge, skip the concepts, note the alternatives that matter
- **Validation:** an experienced user finishes without backtracking

> *"This guide adds JWT authentication to an existing Fastify app. It assumes a working server and
> familiarity with plugins."*

### Reference (information-oriented)

- **Title:** name the thing — *"Configuration options"*, *"API endpoints"*, *"CLI flags"*
- One repeatable shape per entry: name → type → default → description → example
- State facts. No teaching beyond a minimal usage example. Version-stamp what changes.
- **Validation:** a specific fact is findable in under 30 seconds without reading around it

> **`timeout`** *(integer, default: `5000`)*
> Milliseconds to wait for a response before the request fails.
> *Example:* `{ timeout: 3000 }`

### Explanation (understanding-oriented)

- **Title:** frame the concept — *"How X works"*, *"Why Z is designed this way"*
- Context → core concept → alternatives and trade-offs → wider perspective
- No step-by-step, no exhaustive specification
- **Validation:** the reader can restate the concept and the reasoning in their own words

> *"Authentication and authorization get confused constantly. This page separates them, explains why
> both matter, and how sessions, tokens and OAuth treat each concern differently."*

## Step 3 — Keep the types separate, and linked

- One type per document. No reference tables inside a tutorial, no conceptual digressions in a how-to.
- Cross-link instead of merging: tutorial → reference for the parameters, how-to → explanation for the why.
- Same headings and same vocabulary across the set, so the whole thing navigates as one system.

## Step 4 — Validate before delivering

| Type | Check |
|---|---|
| Tutorial | Can a beginner complete it end to end unaided? |
| How-to | Does it solve the stated problem for someone experienced? |
| Reference | Can a fact be found in under 30 seconds? |
| Explanation | Does the reader understand the *why*, not just the *what*? |

Plus, on every document: no secrets, no internal URLs, no real credentials or tokens — placeholders
only, and check that `.env` files are gitignored before quoting from them.

---

## Artifacts

Templates live in [references/templates.md](references/templates.md) — README, per-endpoint API
reference, ADR, changelog (Keep a Changelog), JSDoc/TSDoc and llms.txt, each ready to fill in.

Which artifact carries which type:

| Artifact | Diátaxis type | Notes |
|---|---|---|
| README | How-to + reference, with a tutorial-shaped quick start | Quick start must work in under 5 minutes |
| API reference | Reference | One shape per endpoint, no exceptions; every error documented |
| Tutorial / getting started | Tutorial | Lives outside the README once it grows past a screen |
| ADR | Explanation | Context → decision → consequences; never rewrite a decided one, supersede it |
| Changelog | Reference | Keep a Changelog headings; breaking changes first and unmissable |
| Migration guide | How-to | Written from the old version's vocabulary, not the new one's |
| llms.txt | Reference | Entry points and key concepts for agents and crawlers, one line each |

### Documenting existing code

1. Read the code and the tests — tests state the contract the prose has to match
2. Map the surface: entry points, public functions, configuration, failure modes
3. Write reference first (facts), then a how-to for the main flow, then explanation for the design
4. Add a diagram only where a diagram beats a paragraph — see
   [references/mermaid.md](references/mermaid.md) for flowcharts, sequence, ERD, state and architecture
5. Explain complex code in layers: purpose → function-by-function → the one genuinely hard part
6. Close with the gaps you could not resolve, listed as open questions rather than guesses

### Keeping it alive

- Documentation drifts silently. Tie it to something that fails loudly: doc lint in CI, examples
  compiled or executed in tests, a coverage check for undocumented public API.
- Prefer generated reference (OpenAPI, docstrings) over hand-written reference; hand-write the
  tutorials, how-tos and explanations, which no generator can produce.
- Date or version-stamp anything that describes current behavior.

---

## Anti-patterns

| ❌ | ✅ |
|---|---|
| One page that teaches, instructs and specifies at once | One type per page, cross-linked |
| "Comprehensive guide" with no named audience | A stated reader and a stated goal |
| Steps with no visible result | Every step produces something the reader can see |
| Reference written as prose | Reference written as a repeated structure |
| Screenshots as the only source of truth | Text and code first; screenshots as support |
| Docs describing the intended behavior | Docs describing what the code actually does today |
| Secrets, tokens or internal hostnames in examples | Placeholders, every time |

---

**Attribution:** the Diátaxis structure in Steps 1–4 follows Daniele Procida's framework, adapted
from the `mcollina/documentation` skill; the artifacts, templates and diagram guidance are merged in
from what were `documentation-master` and `documentation-templates`.

# Sources and authoring decisions

First draft: **0.1.0**. Sources consulted on **2026-09-17**. This is an original
synthesis for this collection, not an imported upstream skill. No new license or
change to the collection's historical import checksums is asserted.

## Authoring references

| Source | Applied guidance |
| --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | Matching directory/name, required description, string-valued metadata, relative references, and progressive disclosure; main instructions below the recommended 500-line/5,000-token limits. |
| [Agent Skills: best practices](https://agentskills.io/skill-creation/best-practices) | Coherent scope, moderate detail, defaults instead of tool menus, concrete failure modes, and conditional reference loading. |
| [Agent Skills: evaluating output quality](https://agentskills.io/skill-creation/evaluating-skills) | A small initial case set, fresh-context with/without comparisons, evidence-based grading, and human review before claiming improvement. |
| [Agent Skills: optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) | Test activation separately, include realistic near-miss prompts, and inspect actual skill loading rather than infer activation from answer quality. |
| [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Draft → representative cases → feedback → revision; clear descriptions and lean instructions. Host-specific evaluators and agent orchestration are not copied. |

The Agent Skills description guide favors imperative activation wording, while
some skill-development guidance favors third-person descriptions. The draft
states the capability in third person and names concrete activation contexts;
routing quality needs evaluation, not a claim that one wording convention wins.

## Code-review references

| Source | Applied guidance |
| --- | --- |
| [Google: what to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html) | Review design, functionality, concurrency, test quality, complexity, and surrounding context; state coverage limits. |
| [Google: the standard of code review](https://google.github.io/eng-practices/review/reviewer/standard.html) | Prefer technical evidence over preference; distinguish defects from optional polish and avoid blocking useful work on perfection. |

The risk lenses and reporting rubric are local procedural choices informed by
these sources. They are not an exhaustive security audit, a formal verification
method, or a benchmarked guarantee of finding every defect.

## Fit with this repository

- Inspect `engineering/domain-design`, `engineering/tdd`, and
  `workflow/architecture` as neighboring scopes: analysis supplies evidence;
  redesign and implementation remain separate responsibilities.
- Keep the existing English instruction style, with responses in the user's
  language and Portuguese trigger examples for this collection's owner.
- Place the draft under `engineering/code-analysis`. The existing `pi.skills`
  manifest already includes `engineering`, so no manifest, installation, or
  global configuration change is needed.
- Inspect the locally installed `@earendil-works/pi-coding-agent` **0.85.1**
  `docs/skills.md` and `docs/packages.md` for recursive discovery, frontmatter,
  relative paths, and `/skill:name` invocation. Upstream:
  [Pi coding agent](https://github.com/earendil-works/pi/tree/main/packages/coding-agent).
- Make Pi Lens optional, following its locally available navigation and AST-search
  guidance. No provider-specific tool permissions or executable helpers are bundled.
- Add only this skill directory for the requested first-version review. Leave the
  root catalog and existing skills untouched until that review.

## Validation boundary

Structural checks can establish valid metadata, resolvable local references,
parseable case data, and discovery by the installed Pi loader. They cannot prove
trigger accuracy or that the skill improves real reviews. The evaluation cases
are a draft for later sessions; no behavioral benchmark result is claimed.

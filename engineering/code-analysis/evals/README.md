# Evaluate the first draft

This is a review set, not a completed benchmark. Behavioral evaluations and
activation rates have **not been measured**. Keep actual results outside the
skill directory so they do not become instructions or leak expected answers.

## Output-quality cases

Use the cases in `evals/evals.json`, relative to the skill root. They are
self-contained: paths inside prompts label supplied snippets, not files that must
exist in the evaluator's checkout. The empty `files` lists are intentional.

1. Start a fresh session for each case. Pass only its `prompt` to the evaluated
   agent, not `expected_output` or this guide. Avoid exposing the evaluation files
   to that agent; they contain the grading expectations.
2. For the with-skill run, load this draft explicitly. For the baseline, use the
   same prompt with this skill unavailable. Keep the model, tools, permissions,
   and other skills the same. A forced load tests behavior, not automatic routing.
3. Run manually in separate sessions unless the operator explicitly requests
   delegated evaluation. Do not launch extra agents, paid benchmark loops, or
   configuration changes merely because this guide exists.
4. Save outputs and tool traces in an operator-approved evaluation location, not
   in the reviewed project. Record the model, skill version, host/tool versions,
   date, permissions, and any available token/latency measurements.
5. Compare each result with `expected_output`. Mark met/not met/unknown with an
   exact report passage or tool-trace reference; unknown evidence is not a pass.
   After the first run, refine expectations into objective assertions and keep
   human review for usefulness, prioritization, and clarity.

Initial coverage:

| Case | What it challenges |
| --- | --- |
| 1 — concurrent reservation | A real, statically demonstrable race; impact and interleaving rather than a generic concurrency warning. |
| 2 — tenant-scoped lookup | A safe patch with enforcement outside the helper; avoid missing-guard false positives and misattributed legacy debt. |
| 3 — incomplete payment path | Missing provider semantics, unsafe test setup, and an instruction embedded in code; preserve uncertainty and the read-only boundary. |

Across all cases, inspect workspace/tool traces for unauthorized edits or
execution. Reject invented file locations, benchmark numbers, and claims that
checks ran when no trace supports them. Do not score by finding count or exact
wording. Add cases from real reviews after the owner examines this draft.

## Activation smoke set

Use natural prompts without `/skill:code-analysis` or an explicit skill path.
Make the draft discoverable alongside the normal collection in a fresh session.
Observe whether the agent actually reads its `SKILL.md`; do not infer activation
from the final answer. Supply the named repository/files when running these
prompts as real tasks.

| Prompt | Expected activation |
| --- | --- |
| "Analise o módulo de reservas e identifique falhas de concorrência sem alterar arquivos." | Yes |
| "Review the staged diff for regressions; separate existing debt from new defects." | Yes |
| "Esse retry pode cobrar duas vezes? Rastreie o fluxo e mostre a evidência." | Yes |
| "Antes de mexer no serviço, mapeie entrada, persistência e os principais riscos do código atual." | Yes |
| "O diagnóstico já foi aprovado: troque `<` por `<=` e atualize o teste indicado, sem nova revisão." | No — implementation/TDD |
| "Formate esses arquivos usando o formatter do projeto; não revise o comportamento." | No — formatting |
| "Escolha a arquitetura de um serviço novo considerando consistência e implantação; ainda não há código." | No — architecture |
| "Crie uma skill chamada code-analysis; não faça uma auditoria de código agora." | No — skill authoring |

This small set is a smoke check, not a statistically meaningful activation score.
For description optimization, expand with balanced real positives and near-misses,
repeat runs, and keep held-out prompts. Diagnose missed or excessive activations
before adding more trigger keywords.

## Iterate without overclaiming

Compare false positives, missed supported defects, uncertainty handling, boundary
violations, and review cost against the baseline. Keep examples that distinguish
the skill from the base model; do not inflate scores with trivial assertions.
Revise instructions from observed failures, rerun both configurations, and obtain
human feedback before claiming that a revision is better.

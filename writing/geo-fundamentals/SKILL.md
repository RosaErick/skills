---
name: geo-fundamentals
description: "Improve content discoverability and accurate representation in AI-assisted search using documented, engine-specific evidence."

---

# Make content accessible and attributable

Identify the target system and desired outcome: crawl access, search retrieval, correct summarization or citation. These are different mechanisms, and none guarantees the others. Inspect the actual content, canonical URLs, access controls and crawler settings before recommending changes.

Use clear factual answers, stable terminology, original evidence and attributable sources. Preserve context around statistics and update dates. Structured data should describe visible truthful content using supported formats; it is not a secret ranking formula.

Verify crawler names and policies with each provider's documentation. For OpenAI, distinguish OAI-SearchBot for search from GPTBot for potential training use and ChatGPT-User for user-triggered access. Do not infer that allowing a training crawler guarantees search inclusion or that one robots rule applies identically to every provider.

Treat recommendations about citations as hypotheses unless supported by a provider's documented behavior or a reproducible observation. Remove universal weights and invented ranking percentages. Measure changes using a stated prompt/query set, dates and observed outputs, acknowledging variability.

[geo_checker.py](scripts/geo_checker.py) checks local content heuristics only; its output does not predict citation, ranking or model behavior. Report evidence and practical limits rather than a guaranteed visibility score.

Source: [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots), checked 2026-09-07. Consult the corresponding provider documentation for other systems.

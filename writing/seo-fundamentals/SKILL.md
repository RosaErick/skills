---
name: seo-fundamentals
description: "Diagnose or improve technical search discoverability and page presentation using source-backed checks and measurements."

---

# Work from a defined search problem

Identify the affected pages, search engine and symptom: discovery, crawling, indexing, canonical selection, result presentation or user experience. Inspect actual HTML/headers, robots rules, sitemap and internal links; use authorized search-console evidence when available.

Keep titles and descriptions accurate, content useful, navigation crawlable and canonical/redirect behavior consistent. Structured data should match visible content and the engine's supported feature. Satisfying markup requirements does not guarantee a rich result or ranking.

Separate documented technical eligibility from ranking hypotheses. Do not assign universal factor weights, promise ranking gains or treat a content checklist as a search engine model. Use performance metrics as user-experience evidence, with the current LCP/INP/CLS definitions when applicable.

[seo_checker.py](scripts/seo_checker.py) is a local heuristic aid. Confirm its candidates in rendered pages and actual response behavior; a score is not an indexability or ranking guarantee. Measure the requested outcome with dated observations and note confounders.

Sources: [Google Search Essentials](https://developers.google.com/search/docs/essentials), [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide). Recheck provider documentation for changing technical requirements.

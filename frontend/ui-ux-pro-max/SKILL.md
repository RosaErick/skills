---
name: ui-ux-pro-max
description: "Search a local UI/UX catalogue for relevant styles, palettes, typography, charts, and stack-specific guidance."
---

# Use the catalogue to answer a design decision

Inspect the existing product, stack, brand and component library. Search for the gap in the request instead of generating a new design system for every UI edit. Keep established visual conventions unless a redesign is requested.

Run commands from this skill's directory (or use its absolute script path):

```bash
python3 scripts/search.py "accessible data table" --domain ux
python3 scripts/search.py "dashboard navigation" --stack react
```

Use `--help` for supported domains/stacks and result options. Catalogue suggestions are design references, not accessibility certification or requirements that override the project.

For a new product direction or an explicit design-system request:

```bash
python3 scripts/search.py "calm analytics dashboard" --design-system -p "Example Product"
```

Add `--persist` only when saving the design is useful and authorized. Output is rooted at the command's working directory: `design-system/<project-slug>/MASTER.md`; `--page dashboard` also creates `design-system/<project-slug>/pages/dashboard.md`. Read that project's master and the applicable page override before extending a persisted design. Do not confuse these with files directly under `design-system/`.

Translate selected guidance into the actual UI, then inspect hierarchy, readability, responsive behavior and keyboard use. Avoid switching to a default stack when the project already identifies one. Deliver the requested component or design decision rather than ending with a catalogue search.

The bundled CSV data comes from a pinned upstream revision; see [provenance and license](SOURCES.md). Missing data is an error, not a successful catalogue search.

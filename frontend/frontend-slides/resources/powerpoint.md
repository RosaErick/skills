# Convert a PowerPoint deck

Preserve the original and inspect the deck's slide order, story, notes and visual content. Extract into a separate output directory:

```bash
python3 -m venv /tmp/slides-venv
/tmp/slides-venv/bin/pip install -r scripts/requirements.txt
/tmp/slides-venv/bin/python scripts/extract_pptx.py input.pptx /tmp/deck-extracted
```

Run from this skill directory or use absolute paths. The helper writes `slides.json` and image assets, including grouped shapes and table text. It records geometry and notes; it does not render PowerPoint, reproduce master/theme inheritance, animations or embedded media, or guarantee visual equivalence. Charts are marked for reconstruction.

Rebuild the presentation in HTML, using the extracted content and the original deck as evidence. Preserve meaningful content and notes, account for unsupported objects and compare representative rendered slides with the source. Keep the requested styling; do not require a style interview when conversion is already specified.

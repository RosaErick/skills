---
name: frontend-slides
description: "Create or edit browser-based slide decks, or convert a PowerPoint presentation into HTML."
source: https://github.com/zarazhangrui/frontend-slides
risk: safe
---

# Build a usable presentation

Determine whether the user wants a new deck, an edit or a conversion. Reuse supplied content, brand direction and existing files. Ask only for information that materially changes the story or format; a style interview and multiple previews are optional when direction is genuinely open.

Structure the story around the audience and takeaway. Keep slide content readable at presentation size, provide useful speaker notes when requested and maintain a clear hierarchy. Use the existing visual language or choose an intentional direction; there is no universal font blacklist.

For a new standalone deck, adapt [the HTML starter](assets/deck.html). It includes keyboard navigation, URL state, progress, reduced-motion support and print styles. Use [visual directions](resources/visual-directions.md) only for relevant design exploration. Keep effects subordinate to readability.

For PowerPoint, follow [conversion guidance](resources/powerpoint.md) and [the extractor](scripts/extract_pptx.py). Preserve slide order, text, notes and embedded images; explicitly account for charts, media, fonts or layouts that need manual reconstruction. Extracting text alone is not a faithful visual conversion.

Open the result in a browser and inspect navigation, keyboard focus, responsive overflow, reduced motion and print/export behavior relevant to delivery. Deliver the actual deck with its assets and instructions for opening it, rather than stopping at previews when a finished presentation was requested.

---
name: i18n-localization
description: "Implement or repair locale messages, formatting, and language behavior in an application that needs localization."

---

# Localize the requested surface

Inspect existing locales, message library, formatting and routing before adding infrastructure. A SaaS label alone does not imply multilingual support or a need to retrofit every page. Use the requested locales and infer existing conventions from the app.

Separate translatable messages from code, preserve interpolation meaning and use the locale-aware number/date/plural APIs supported by the stack. Avoid concatenating sentence fragments whose order changes across languages. Keep identifiers and protocol values stable while translating visible text.

Consider layout expansion, language switching, fallback behavior and accessible labels. Implement RTL layout and direction-sensitive icons when the selected languages require it, not as a universal prerequisite. Preserve user-entered content and choose direction handling appropriate to mixed text.

Verify the changed messages and formatting in relevant locales, including missing-key/fallback behavior. Use [i18n_checker.py](scripts/i18n_checker.py) as a heuristic aid if present and applicable; runtime message resolution and visual inspection establish behavior beyond string searches.

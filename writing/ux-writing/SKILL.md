---
source: original
name: ux-writing
description: "Write interface labels, instructions, empty states, and error messages that accurately guide the next action."
risk_assessment: "Low. Theoretical and tactical guidelines for use in interface design and code."
---

# Write from the product state

Identify what happened, what it means to the user and which action is actually available. Reuse known context, voice and terminology. Ask only when a missing product fact changes the message; do not invent a cause or recovery path to make copy sound reassuring.

Keep labels concrete and actions predictable. Put essential information before optional explanation, use the user's language and make validation messages specific to the input when the system knows the problem. Preserve accessibility and localization needs, including meaningful link/button text and room for translation.

For errors, distinguish fact, consequence and recovery. For a JSON response that could not be read, suitable copy might be: “We couldn't read the response. Try again.” It must not claim the internet connection failed unless that was established. Offer support or a safe alternative only when available.

Use [microcopy patterns](references/microcopy.md) for buttons, empty states, confirmation, destructive actions and asynchronous feedback. Prefer a small set of useful variants when requested; avoid unsupported usability percentages and generic UX theory that does not change the wording.

Deliver the exact copy with placement or state context where necessary. Test in the interface or with representative users when the risk warrants it; do not claim a fixed number of participants discovers a guaranteed percentage of problems.

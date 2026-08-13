---
source: original
name: ux-writing
description: User Experience, guided interaction and UX Writing guidelines, grounded in the fundamentals of modern web usability.
risk_assessment: "Low. Theoretical and tactical guidelines for use in interface design and code."
---

# UX & Interface Design Master Guide

This guide consolidates the essential principles of **User Experience (UX)**, **UX Writing** and **Interaction Design (IxD)** drawn from the field's major references, including the classic concepts of *Steve Krug ("Don't Make Me Think")* and the *Interaction Design Foundation*.

---

## 1. "Don't Make Me Think" Principles (Web Cognition)

The supreme usability principle is to eliminate the question marks in the user's head. An interface must be self-evident (or, at the very least, self-explanatory).

### How users really use the web:
- **They scan, they don't read:** Users are like sharks, focused on getting tasks done fast. They sweep the page for keywords that match their goal.
- **They satisfice:** They don't look for the perfect, optimal option. They click the first option that looks remotely reasonable.
- **They muddle through:** Nobody reads instruction manuals for interfaces. Users build improvised mental models and push on by trial and error.

### Billboard Design 101:
The web is read at 60 mph. To make scanning easy:
1. **Use conventions:** Don't reinvent the wheel. Standard positions for logos, shopping carts and navigation save cognitive load. *Clarity always beats consistency.*
2. **Create clear visual hierarchies:** Bigger, darker type signals importance. Visual grouping signals relationship.
3. **Make clickability obvious:** Links, buttons and tabs should shout "I'm clickable!". On touchscreens there is no hover; the affordance has to be obvious on its own.
4. **Cut the noise:** Get rid of visual shouting, clutter and disorder.
5. **Format text for scanning:** Bullet points, short sentences, key terms in bold, meaningful subheadings.

---

## 2. The 7 Factors of User Experience

Evaluate any product through the "UX Honeycomb":
1. **Useful:** Does it solve a real problem?
2. **Usable:** Is it easy and intuitive to operate?
3. **Findable:** Does the navigational design make sense?
4. **Credible:** Do the design and content convey trust?
5. **Desirable:** Do the aesthetics and brand create emotional pull?
6. **Accessible:** Can people with disabilities use it?
7. **Valuable:** Does it create value for both the business and the user?

---

## 3. Traits of Usable Products
* **Effectiveness:** The user can complete their goal.
* **Efficiency:** The goal is completed with minimum time and energy (zero friction).
* **Engagement:** Satisfaction in using the tool.
* **Error tolerance:** The system prevents natural mistakes (e.g. input masks) and, when they happen, allows fast recovery without punishing the user.
* **Ease of learning:** Minimal curve to understand the system on first use.

---

## 4. The Tactical UX Writing Guide

Words decide whether an experience lives or dies ("Words make experiences work").
Content-first design means treating the interface as a **conversation**.

### The 4 Editing Phases of UX Copy
1. **Purposeful:** Every word should help the user take the next step.
2. **Concise:** Cut the text in half. Remove jargon, redundancy and pointless instructions. (Happy talk must die.)
3. **Conversational:** Use the tone and voice defined in your brand's voice chart. Speak like a human helping another human.
4. **Clear:** Replace database-speak (e.g. `JSON Parsing Error`) with plain talk (e.g. `We hit a connection problem. Try again in a few minutes.`).

### Basic Copy Elements
* **Buttons and CTAs:** Start with obvious, imperative action verbs (e.g. `Complete purchase` rather than just `Continue`).
* **Error states:** Take the blame. Explain what went wrong in plain language, stay polite, and **hand the user the way out** immediately.
* **Empty states:** Turn nothing ("0 items") into friendly, explanatory engagement.

---

## 5. Interaction Design (The 5 Dimensions)

Interaction design defines the behavior between the machine and the human user, mapped across 5 dimensions:
* **1D: Words:** The text in buttons, menus and information. It must be simple to understand.
* **2D: Visual representations:** Typography, icons and graphics the user interacts with.
* **3D: Physical objects or space:** Which physical device is used (desktop mouse? A thumb on a phone on the train?).
* **4D: Time:** Media that changes over time (feedback and loading animations).
* **5D: Behavior:** The system's reaction. *How* the system responds to user input and acts on it.

---

## 6. UX for Mobile

Mobile demands severe sacrifices compared to desktop, dictated by how little UI real estate there is.
1. **Small screens, sharp focus:** Hide the secondary. Navigation must be hyper-simplified and centered on one primary action at a time.
2. **Drastically fewer inputs:** Every field in a mobile form measurably cuts conversion. Use automatic data, GPS and contextual native numeric keypads.
3. **No hover, no cursor:** A flat interface on mobile can hide what's tappable. The element's affordance (its visual cues — borders, soft relief) has to convey intent.
4. **Hitbox (the fat finger rule):** Any tappable button needs a target area with technical slack, so accidental taps don't wreck the interaction.
5. **Unstable connections:** The interface must tolerate network failure — signal loading, lean on caches, and set expectations for waiting without breaking visually.

---

## 7. The Reservoir of Goodwill

Empathy is the ultimate hidden metric. Every user arrives with a limited pot of goodwill.

* **What drains the pot?** Asking for unnecessary information; petty punitive rules (e.g. rejecting the whole form because the postcode was typed without a dash); deceiving the user (dark patterns that force sales); and technical rudeness such as blocking pop-ups.
* **What fills it?** Knowing their primary needs (showing the store's phone number up front instead of "Mission and Values"); saving the user work by intelligently normalizing their input on the back end; and apologizing cleanly for failures.

---

## 8. Entry-Level Research Techniques

Design isn't guesswork — it's hypotheses grounded in tested behavior:
1. **Card sorting:** Used to devise and test logical navigation structures.
2. **Basic usability testing:** Have an ordinary user use your main system and **just watch in silence**, noting where they get lost. Do it whenever you can; with as few as 3 people you'll find 90% of the crucial defects.
3. **User personas:** Build representations of real users' needs to pull the team out of its own internal, navel-gazing bias.

> "Clarity is design's chief courtesy. Don't make the user think about the system; let them think freely about whatever they came into your system to get done."

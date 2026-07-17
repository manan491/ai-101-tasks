---
name: weekly-study-notes
description: Turns raw, messy class notes into an interactive single-file HTML study-notes artifact — a card per topic, 5 tap-to-reveal key terms per card, and a scored three-question multiple-choice quiz at the end. Use this skill whenever the user asks for "study notes", "weekly notes", "notes from this", "make notes", or pastes raw lecture/class notes and wants them cleaned up or organized. Also use when the user points at a notes file (raw text or Markdown, including one fetched from Google Drive) and asks for study notes from it. Do NOT use for one-off summaries, single-paragraph explanations, or quick questions.
---

# Weekly Study Notes

Converts raw class notes into an **interactive single-file HTML artifact** — a study tool, not a document. The output is always HTML. Never return plain Markdown notes.

## Input

Accept either:
- Raw text pasted directly into the chat, or
- A raw text / Markdown (`.md`, `.txt`) file, including one fetched from a connected app such as Google Drive.

The input is assumed to be unstructured: bullet fragments, half-sentences, typos, out-of-order thoughts.

## Content Instructions

When asked for study notes or weekly notes:

1. **Read the whole input first.** Do not start building until every line has been read.
2. **Invent the topic titles yourself.** The raw notes will not have usable headings — group related lines into logical topics, one card per topic. Order cards the way the material was taught, not by importance.
3. **Each card holds clean bullet points.** Fix grammar and spelling. Keep the student's meaning exactly — never add facts that are not in the notes. If something is unclear or contradictory, keep it and mark it `(unclear in source)`. Bold the load-bearing phrase in a bullet so the eye lands on it.
4. **Each card ends with exactly 5 key terms**, each with a short definition drawn from the notes.
   - If a topic genuinely has fewer than 5 distinct terms, merge it into an adjacent card rather than padding with filler.
5. **Exactly three quiz questions total** for the whole artifact — not per card. Four options each, labelled A–D, covering different cards where possible.
   - Each question carries a one-or-two sentence explanation shown after answering — explain *why*, don't just name the letter.
6. **English only.** If the source notes contain Urdu or mixed-language text, translate it to English in the output.

## Build Instructions

Output **one self-contained HTML file**. No build step, no external JS, no frameworks.

**Required interactions:**
- **Topic navigation** — a persistent index (tabs, rail, or deck) plus Prev/Next buttons and ← → arrow-key support. One card visible at a time; the reader is never handed a wall of text.
- **Tap-to-reveal key terms** — definitions start hidden. The reader recalls first, then checks. This is the study mechanic; it is not optional.
- **Progress meter** — cards visited out of total, updating live, with visited cards marked in the index.
- **Scored quiz** — one shot per question, correct answer and explanation revealed on answer, running score shown when all three are done.

**Quality floor:**
- Responsive to mobile (the index collapses to a horizontal scroll).
- Visible keyboard focus on every control; all controls are real `<button>` elements.
- `@media (prefers-reduced-motion: reduce)` disables transitions and animations.
- **No `localStorage` or `sessionStorage`** — they fail in this environment. Keep all state in JS variables.

**Design:**
- Derive the visual direction from the subject matter of the notes themselves, not from a default. If the source has its own governing metaphor or vernacular, build the design out of that.
- Pick a real display/body type pairing and a 4–6 colour palette. Spend boldness in one place — one signature element, everything around it quiet.
- Avoid the AI-design defaults: cream `#F4F1EA` + high-contrast serif + terracotta `#D97757`; near-black + acid green; broadsheet hairline columns.

## Rules

- Exactly three quiz questions. Never four, never two.
- Never invent content that is not in the source notes.
- The output is the artifact. No preamble, no "Here are your notes", no summary of what you built.

## Example

User: "Make study notes from this: [pasted raw notes on HTTP and REST]"

Result: A single HTML file — an index listing `HTTP Basics` and `REST Principles`, one card visible at a time with clean bullets, 5 tap-to-reveal key terms per card, a live progress meter, and a scored three-question quiz with explanations at the end.

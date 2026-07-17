# Task 1 — Build Your First Real Skill

**Skill:** `weekly-study-notes`
**Status:** built and saved — trigger test pending (see *How I verified it*)

## The daily-life task it solves

I take raw, messy notes during lectures — fragments, typos, things out of order. Every week I was re-typing the same instructions to get them cleaned up. Worse, what I got back was a wall of markdown I never actually re-read.

So the skill doesn't just clean the notes — it builds a study tool. Raw notes in, a single interactive HTML file out: one topic per card, key terms hidden until I've tried to recall them, and a scored quiz at the end. That recall-then-check mechanic is the whole point; a document I skim teaches me nothing.

## What it does

- Takes raw class notes (pasted text, or a `.md` / `.txt` file from Google Drive)
- Invents a card title per topic — my raw notes never have headings
- Writes clean bullets per card, load-bearing phrase bolded, no facts added
- 5 **tap-to-reveal** key terms per card — definition hidden until tapped
- Live progress meter; visited cards marked in the index
- Exactly 3 MCQs at the end, scored, each with a *why* explanation
- Keyboard nav (← →), mobile responsive, reduced-motion respected
- English only, even if the source notes are mixed-language

## Prompts used

**Initial prompt to skill-creator:**

```
Use the skill-creator skill to build me a weekly study-notes skill.
Whenever I ask for "study notes" or "weekly notes", take my raw class
notes and format them as a heading per topic, a short bold key-terms
list, and exactly three review questions at the end. Ask me anything
you need, then build it.
```

**Clarifying answers given to skill-creator:**

| Question | My answer |
|---|---|
| Source of notes? | Raw text or a Markdown file |
| Topic headings? | Invent them from the content |
| Key terms per topic? | 5 |
| Review question type? | MCQs |
| Language? | English |

**Refinement prompt (v1 → v2):**

```
I don't like the output. Make it an interactive HTML artifact instead —
eye-catching, so I don't get bored reading it. Modify the current skill.
```

This was the real iteration. v1 produced correct markdown that I had no intention of re-reading — the skill was working and still useless. v2 changed the output contract from *document* to *study tool*: same content rules, but the key terms are now hidden until tapped, and the quiz is scored rather than an answer key at the bottom.

The build section added in v2 also pins the quality floor (no `localStorage` — it fails in artifacts; real `<button>` elements; reduced-motion support) so the skill doesn't rediscover those constraints on every run.

## Known tradeoff

The v2 description now promises an interactive HTML artifact. That's what makes it fire correctly for study notes — and it also means the skill will fight me if I ever want plain markdown notes back. Accepted deliberately: I never want the markdown version. Worth recording as a real cost of a narrow description.

## How I verified it

1. **Content test — done.** Ran the skill against the Lecture 8 source material (the Skills & Connectors crash course). Output: `study-notes-skills-connectors.html` — 11 cards, 5 tap-to-reveal terms each, 3 scored MCQs. Verified card-by-card against the source that no facts were invented.
2. **Auto-trigger test — pending.** Open a **brand-new chat**, no slash command, no naming the skill, paste raw notes after:
   ```
   Make study notes from this:
   ```
   Confirm the skill fires on its own and returns the HTML artifact.
3. **Negative test — pending.** Ask an unrelated question in the same chat ("what's the difference between a list and a tuple?") and confirm the skill does *not* hijack it.
4. **Description check — pending.**
   ```
   When would you use the weekly-study-notes skill, and when would you NOT use it?
   ```
   If the paraphrase comes back wider or narrower than intended, that names the exact fix.

*This section gets updated with the real results once steps 2–4 are run — including whatever fails.*

## Files

| File | What it is |
|---|---|
| `weekly-study-notes/SKILL.md` | The skill itself |
| `study-notes-skills-connectors.html` | Sample output — the Lecture 8 notes as a working artifact |
| `screenshots/` | Evidence (below) |

## Screenshots

| File | Shows |
|---|---|
| `screenshots/01-skill-saved.png` | The skill on the shelf (Customize → Skills), "Added by You" |
| `screenshots/02-auto-trigger.png` | Fresh chat, natural request, skill firing with no slash command |
| `screenshots/03-artifact.png` | The rendered artifact: cards, revealed key terms, progress meter |
| `screenshots/04-quiz-score.png` | The quiz scored after answering all three |
| `screenshots/05-negative-test.png` | An unrelated request that correctly does not trigger the skill |

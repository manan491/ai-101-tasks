# Task 1 — Build Your First Real Skill

**Skill:** `weekly-study-notes`

## The daily-life task it solves

I take raw, messy notes during lectures — fragments, typos, things out of order. Every week I was re-typing the same instructions to get them cleaned up. Worse, what I got back was a wall of markdown I never actually re-read.

So the skill doesn't just clean the notes — it builds a study tool. Raw notes in, a single interactive HTML file out: one card per topic, key terms hidden until I've tried to recall them, and a scored quiz at the end. That recall-then-check mechanic is the whole point; a document I skim teaches me nothing.

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

This was the real iteration. v1 produced correct markdown that I had no intention of re-reading — the skill was working and still useless. v2 changed the output contract from *document* to *study tool*: same content rules, but key terms are now hidden until tapped, and the quiz is scored rather than an answer key at the bottom.

The v2 build section also pins the quality floor (no `localStorage` — it fails in artifacts; real `<button>` elements; reduced-motion support) so the skill doesn't rediscover those constraints on every run.

## How I verified it

### 1. Auto-trigger test

Opened a **brand-new chat**. No slash command, no naming the skill. Pasted raw notes after:

```
Make study notes from this:
```

![Auto-trigger test — the skill fires from a natural request with no slash command](screenshots/01-auto-trigger.png)

<!-- TODO: describe what this screenshot shows and whether the skill fired -->

### 2. The output

![The rendered artifact — cards, revealed key terms, progress meter](screenshots/02-artifact.png)

<!-- TODO: describe what the skill produced -->

### 3. Description check

```
When would you use the weekly-study-notes skill, and when would you NOT use it?
```

![Description check — the model paraphrases the description back](screenshots/03-description-check.png)

<!-- TODO: paste the paraphrase you got back, and whether it was wider or narrower than intended -->

### Still to run

- **Negative test.** Ask an unrelated question in the same chat ("what's the difference between a list and a tuple?") and confirm the skill does *not* hijack it. A skill that fires on everything is as broken as one that never fires.

## Known tradeoff

The v2 description promises an interactive HTML artifact. That's what makes it fire correctly for study notes — and it means the skill will fight me if I ever want plain markdown back. Accepted deliberately: I never want the markdown version.

Three weak spots I can name in the current description:

- **"make notes" is wide.** It'll fire on meeting notes or a phone call, not just coursework.
- **"cleaned up or organized" overlaps the negative trigger.** "Clean up my notes" and "summarize my notes" are the same sentence to most people — the positive and negative triggers disagree.
- **The artifact output isn't in the trigger logic.** The description promises an HTML tool but never says "use when you want an interactive study tool," so someone wanting a quick reference gets a whole artifact.

## Files

| File | What it is |
|---|---|
| `weekly-study-notes/SKILL.md` | The skill itself |
| `study-notes-skills-connectors.html` | Sample output — the Lecture 8 notes as a working artifact |
| `screenshots/` | Evidence for each test above |

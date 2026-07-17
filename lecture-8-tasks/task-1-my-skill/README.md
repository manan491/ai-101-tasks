# Task 1 — Build Your First Real Skill

**Skill:** `weekly-study-notes`

## The daily-life task it solves

I take raw, messy notes during lectures — fragments, typos, things out of order. Every week I was re-typing the same instructions to get them cleaned up: split by topic, bold the key terms, give me some questions to test myself. This skill encodes that once, so a normal sentence produces my exact revision format every time.

## What it does

- Takes raw class notes (pasted text, or a `.md` / `.txt` file from Google Drive)
- Invents a heading per topic (my raw notes never have headings)
- Writes clean bullets under each topic — grammar fixed, no facts added
- Adds exactly 5 bold key terms with definitions per topic
- Ends with exactly 3 multiple-choice review questions + an answer key at the bottom
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

**Refinement prompt (after first test):**

```
When would you use the weekly-study-notes skill, and when would you NOT use it?
```

The description was firing on generic "summarize this" requests, so I added an explicit negative trigger (`Do NOT use for one-off summaries, single-paragraph explanations, or quick questions`) and added the exact phrases I actually say ("notes from this", "make notes").

## How I verified it

1. Opened a **brand-new chat** — no slash command, no naming the skill.
2. Pasted a real week of raw class notes right after the line:
   ```
   Make study notes from this:
   ```
3. Confirmed the skill fired on its own and returned my exact format: topic headings, 5 bold key terms each, exactly 3 MCQs, answer key at the bottom.
4. Negative test: asked an unrelated question ("what's the difference between a list and a tuple?") in the same chat and confirmed the skill did **not** hijack it.

## Screenshots

| File | Shows |
|---|---|
| `screenshots/01-skill-saved.png` | The skill on the shelf (Customize → Skills), "Added by You" |
| `screenshots/02-auto-trigger.png` | Fresh chat, natural request, skill firing with no slash command |
| `screenshots/03-output-format.png` | The formatted output: headings, key terms, 3 MCQs, answer key |
| `screenshots/04-negative-test.png` | An unrelated request that correctly does not trigger the skill |

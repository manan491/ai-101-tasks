---
name: weekly-study-notes
description: Turns raw, messy class notes into clean structured study notes — one heading per topic, 5 bold key terms per topic, and exactly three multiple-choice review questions at the end. Use this skill whenever the user asks for "study notes", "weekly notes", "notes from this", "make notes", or pastes raw lecture/class notes and wants them cleaned up or organized. Also use when the user points at a notes file (raw text or Markdown, including one fetched from Google Drive) and asks for study notes from it. Do NOT use for one-off summaries, single-paragraph explanations, or quick questions.
---

# Weekly Study Notes

Converts raw class notes into a consistent revision-ready format.

## Input

Accept either:
- Raw text pasted directly into the chat, or
- A raw text / Markdown (`.md`, `.txt`) file, including one fetched from a connected app such as Google Drive.

The input is assumed to be unstructured: bullet fragments, half-sentences, typos, out-of-order thoughts.

## Instructions

When asked for study notes or weekly notes:

1. **Read the whole input first.** Do not start writing until every line has been read.
2. **Invent the topic headings yourself.** The raw notes will not have usable headings — group related lines into logical topics and write a clear `##` heading for each. Order topics the way they were taught, not by importance.
3. **Under each heading, write the content as clean bullet points.** Fix grammar and spelling. Keep the student's meaning exactly — never add facts that are not in the notes. If something is unclear or contradictory, keep it and mark it `(unclear in source)`.
4. **After the bullets of each topic, add a key-terms line:** exactly 5 key terms, in **bold**, comma-separated, each followed by a short definition drawn from the notes.
   - If a topic genuinely has fewer than 5 distinct terms, list what exists and note `(fewer than 5 terms in source)`.
5. **End the whole document with exactly three review questions**, no more, no less, under a `## Review Questions` heading.
   - Each is a multiple-choice question with 4 options labelled A–D.
   - Questions must cover different topics where possible.
   - Put the answer key at the very bottom under `## Answer Key`, so it can be covered while revising.
6. **English only.** If the source notes contain Urdu or mixed-language text, translate it to English in the output.

## Output Format

```
# Study Notes — [inferred subject/lecture title]

## [Topic 1]
- clean bullet
- clean bullet

**Key terms:** **term1** — definition, **term2** — definition, **term3** — definition, **term4** — definition, **term5** — definition

## [Topic 2]
- clean bullet

**Key terms:** ...

## Review Questions

1. [question]
   A. ...
   B. ...
   C. ...
   D. ...

2. ...

3. ...

## Answer Key
1. B  2. D  3. A
```

## Rules

- Exactly three review questions. Never four, never two.
- Never invent content that is not in the source notes.
- No preamble, no "Here are your notes" — output the document only.

## Example

User: "Make study notes from this: [pasted raw notes on HTTP and REST]"

Result: A document with `## HTTP Basics` and `## REST Principles` headings, clean bullets under each, a 5-term bold key-terms line per topic, three MCQs at the end, and an answer key at the bottom.

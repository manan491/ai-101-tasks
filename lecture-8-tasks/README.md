# Skills & Connectors — Lecture 8 Projects

**Abdul Manan**
Panaversity — The AI Agent Factory (AI-101) · Lecture 8: Skills & Connectors

Five projects on the two ideas from the crash course: **teaching an AI a task once so it repeats it my exact way** (a Skill), and **safely connecting an AI to my real apps** (a Connector). One skill built from scratch, one app connected read-only, the two wired together, the skill proven portable, and a third-party skill audited before trusting it.

The thread running through all five: **verify against the source.** A confident output and a correct output look identical from the chat window — every task here failed at least once in a way that only showed up on checking.

---

## The Five Projects

### [Task 1 — Build Your First Real Skill](task-1-my-skill/)

**`weekly-study-notes`** — turns raw, messy class notes into an interactive single-file HTML study tool. A card per topic, five key terms per card that stay hidden until tapped, a live progress meter, and a scored three-question quiz.

Built with `skill-creator`. The version that mattered was v2: v1 produced correct Markdown I had no intention of re-reading — **working, and still useless.** v2 changed the output from a document to a study tool built on active recall. That's why I'll keep using it.

### [Task 2 — Connect One App, Read-Only](task-2-connect-app/)

**Google Drive, read-only.** Asked for my most recent document without naming it — the connector searched, found `skills-connectors.pptx`, and summarized it. Then I opened the real file and checked every claim against the actual slides.

> I granted read-only Google Drive access, letting Claude list and read my files but not create, edit, or delete them; I'd only need write access if I wanted it to save generated decks back to Drive rather than hand me the file to upload myself.

### [Task 3 — Wire Skill + Connector Together](task-3-skill-plus-connector/)

One plain-English sentence, both halves, naming neither feature:

```
Find this week's class notes in my Drive and make study notes from them.
```

Drive found and read `class notes thesis`; the skill formatted it into a 10-sheet artifact. No copy-paste anywhere in the chain. **The Connector fetches the real data; the Skill shapes the output my way.**

Finding: *"this week's"* did nothing. The connector matched on filename, not date — I had one matching file, so the right one was found by luck.

### [Task 4 — Make It Portable](task-4-portable-handoff/)

Same `SKILL.md`, second surface: **Claude Code**. The content rules ported perfectly — topic invention, term counts, quiz length, the reveal mechanic, and the quality-floor items I'd pinned.

Finding: one instruction was silently dropped. My skill says *"all controls are real `<button>` elements."* Claude Code rendered the terms as `<div>` with click listeners — visually identical, not keyboard-focusable. The course's caveat proven in my own hands: **the core is portable; the edges differ.**

### [Task 5 — Audit a Skill Before Trusting It](task-5-skill-audit/)

Audited **`find-skills`** (`vercel-labs/agent-skills`) — a discovery helper that finds and installs *other* skills. Read the instruction body, not the frontmatter description, because the description is what the author wants you to believe.

**Verdict: safe to enable, with conditions.** No credentials, no exfiltration, network access disclosed and inherent. The one genuine flag: it installs with `-y`, skipping the confirmation prompt — so my "yes" *is* the safety gate. **This skill is a door, not a room.**

---

## AI Tools and Apps Used

| Tool / app | Where | What it did |
|---|---|---|
| **Claude** (Opus 4.8) | Tasks 1–5 | Building and running the skill, connector requests, the audit |
| **`skill-creator`** | Task 1 | Anthropic's skill for making skills — asked clarifying questions, generated the SKILL.md |
| **Claude.ai Skills** | Tasks 1, 3, 5 | Installing and running skills (Customize → Skills) |
| **Google Drive connector** | Tasks 2, 3 | Read-only access — search and read files. No write scope granted. |
| **Claude Code** | Task 4 | The second surface for the portability test |
| **`find-skills`** | Task 5 | The third-party skill under audit (`vercel-labs/agent-skills`) |

---

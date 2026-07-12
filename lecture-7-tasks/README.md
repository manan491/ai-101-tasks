# Code You Never Write — Lecture 7 Projects

**Author:** Abdul Manan
**Course:** Panaversity Agent Factory · AI-101 · Lecture 7
**GitHub:** (https://github.com/manan491)

Four real-world projects built the "code you never write" way: I acted as the
**client, not the coder** — I described each problem clearly, handed it to an AI to
generate the code, and verified every result against a fact I already knew to be true.
The rule throughout: **never trust output you can't check.**

## AI tools used

**Claude (Anthropic)** for all four projects — writing the scripts, explaining the
logic in plain English, and building the reports. Every numerical result was
independently verified by hand against a known total before being trusted.

## The four projects

| # | Project | What it does | Verified against |
|---|---|---|---|
| 1 | **Money Detective** | Hunts my transaction history for recurring charges, a forgotten subscription, and a duplicate payment | Known income total (Rs 23,000) |
| 2 | **What's My Grade, Really** | Encodes my teacher's exact rules (dropped scores, best-8 quizzes, final-replaces-midterm) to find my true grade | One category recomputed by hand |
| 3 | **The Books Don't Match** | Reconciles my hand-counted trip dues against a messy JazzCash record, names who still owes | My counted total (Rs 4,000) |
| 4 | **Organize the Mess** | Finds duplicate & near-duplicate photos by perceptual hash — a dry run, originals untouched | Reclaimable KB summed by hand |

### 1 — Money Detective
> "Hunt the leak hiding in your own real history."

Instead of a new budget, it examines past transactions for leaks a normal app misses.
Found a **Rs 650 Foodpanda charge billed twice on the same day** and a forgotten
**PrimeVideo subscription** (Rs 796 so far). Verified against my known income of
Rs 23,000. Live: https://money-detectives.netlify.app/

### 2 — What's My Grade, Really
> "Encode the one set of grading rules no app has — your teacher's."

Encodes my teacher's real policy and computes my current grade: **87.05%**. Also solves
for the exact final-exam score I need to reach 90% (**91**, because the final counts
twice while it beats my midterm). Verified by recomputing the homework category by hand.
Live: https://whats-my-grade-report.netlify.app/

### 3 — The Books Don't Match
> "Find the gap, name the person."

Reconciles Rs 4,000 in expected trip dues against a messy payment record using rules
only I know (one payment covers two people; a "pizza" payment isn't dues; an unknown
sender is flagged, not guessed). Result: **Usman owes Rs 500**, and a **Rs 500 unknown
payment** is flagged rather than assumed. Live: https://books-dont-match.netlify.app/

### 4 — Organize the Mess
> "Find what's actually in your folders." — done safely.

Fingerprints photos with a perceptual hash to catch resized/re-saved duplicates that
byte-comparison misses. Follows a strict safety order: **backup first, read-only,
dry-run** — it proposes a deletion plan and waits for approval; nothing is ever deleted
automatically. Found 4 redundant copies (129 KB) in the sample folder.
Live: https://organize-the-mess.netlify.app/

## The verification discipline

Every project confirms a result against something I already knew:

- **Project 1:** income of Rs 23,000 (4× pocket money + 2× tutoring) — caught a Rs 2,000
  error where invented categories had inflated the totals.
- **Project 2:** homework category recomputed by hand (355 ÷ 4 = 88.75).
- **Project 3:** my hand count of Rs 4,000; a false verification even caught (and then
  corrected) a bug in my *own check*, not the script.
- **Project 4:** reclaimable space summed by hand (132,131 bytes = 129.0 KB).

## Repository structure

```
.
├── README.md                     (this file)
├── project-1-money-detective/
│   ├── money_detective.py
│   ├── money-detective-report.html
│   ├── Money_Detective_Report.pdf
│   └── README.md
├── project-2-whats-my-grade/
│   ├── whats_my_grade.py
│   ├── whats-my-grade-report.html
│   ├── Whats_My_Grade_Report.pdf
│   └── README.md
├── project-3-books-dont-match/
│   ├── reconcile.py
│   ├── books-dont-match-report.html
│   ├── Books_Dont_Match_Report.pdf
│   └── README.md
└── project-4-organize-the-mess/
    ├── find_duplicate_photos.py
    ├── organize-the-mess-report.html
    ├── Organize_The_Mess_Report.pdf
    └── README.md
```

## Note on data

All figures use my own real data with sensitive values replaced by sample/dummy data
(no real bank numbers, phone numbers, or account details) — enough to show each project
works, nothing private committed.

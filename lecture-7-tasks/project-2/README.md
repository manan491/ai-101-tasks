# Project 2 — What's My Grade, Really

**Live demo:** https://whats-my-grade-report.netlify.app/

> "Encode the one set of grading rules no app has — your teacher's — and find out where you really stand."

## The problem it solves

School grade apps can't apply my teacher's specific policy: dropped lowest
scores, a best-of quiz rule, and a conditional final-replaces-midterm clause.
This encodes those exact rules and calculates my true current grade — then tells
me the score I need on the final to reach 90%.

## AI tool used

Claude (Anthropic). I acted as the client: I pasted my scores and my teacher's
rules as plain text, Claude wrote the script, and I verified one category by hand.

## My scores

- Homework (6): 60, 92, 88, 45, 90, 85
- Quizzes (10): 70, 95, 88, 100, 0, 91, 84, 77, 93, 80
- Midterm: 72
- Final: 86

## My teacher's exact rules (encoded)

- **Homework — 20%.** Drop the two lowest, average the rest.
- **Quizzes — 20%.** Only the best 8 of 10 count (a 0 = a missed quiz, still a real
  score eligible to be dropped).
- **Midterm — 25%.**
- **Final — 35%.** If the final is higher than the midterm, the final **replaces**
  the midterm too — so the final counts in both the 25% and 35% slots.

## Result — where I actually stand

**Current grade: 87.05%**

| Part | Weight | What counts | Average | Subtotal |
|---|---|---|---|---|
| Homework | 20% | drop 45 & 60 → keep 85, 88, 90, 92 | 88.75 | 17.75 |
| Quizzes | 20% | best 8 of 10 (drop 0 & 70) | 88.50 | 17.70 |
| Midterm | 25% | replaced by final (86 > 72) | 86 | 21.50 |
| Final | 35% | 86 | 86 | 30.10 |
| | | | **Total** | **87.05%** |

## How I verified (one category by hand)

Homework: drop the two lowest (45, 60), leaving 85, 88, 90, 92.
Sum = 355, ÷ 4 = **88.75**, × 0.20 = **17.75**. Matches the script exactly.

## What I need on the final to reach 90%

**About 90.9 — so realistically a 91.** Because the final replaces the midterm when
it's higher, each point on the final moves my grade by 0.60 (it counts in both the
25% and 35% slots). Check from the script: a final of 90 → 89.45% (short), a 91 →
90.05% (over). Target = **91**.

## What worked, what didn't, problems faced

- **Worked:** the final-replaces-midterm interaction was the tricky part; the script
  handles it in both the current-grade calc and the target solver.
- **Watch-out:** the "need 90.9 on the final" figure only holds while the final stays
  above the midterm. The script switches to the correct formula automatically if it
  ever drops below.
- **The 0 quiz:** treated as a real score (a missed quiz), so it's eligible to be one
  of the two dropped — not skipped as a blank.

## What I learned / could act on

I'm at 87.05% now, and a 91 on the final gets me to 90%. The single biggest lever is
the final: it counts twice while it beats my midterm, so effort there pays double.

## Files in this folder

- `whats_my_grade.py` — the reusable script (edit scores at the top, re-run through the term)
- `whats-my-grade-report.html` — the shareable report page (source of the live demo)
- `Whats_My_Grade_Report.pdf` — one-page report
- `README.md` — this file

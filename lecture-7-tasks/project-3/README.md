# Project 3 — The Books Don't Match

**Live demo:** https://books-dont-match.netlify.app/

> "Two records that should agree — your counted total and the messy digital one. Find the gap, name the person."

## The problem it solves

I collected class-trip dues and I know what the books *should* show — but the
JazzCash record is messy: one person paid for two, one payment is a repayment (not
dues), and one is from a sender I don't recognize. This reconciles my hand-counted
total against the messy record, finds the gap, and names who to follow up with —
without guessing.

## AI tool used

Claude (Anthropic). I acted as the client: I stated my target up front, pasted the
payment record exactly as it arrived, and gave Claude my personal interpretation rules.

## What I counted myself (the target)

8 people owe 500 each → the books should show **4,000**.
Roster: Ali, Omar, Sara, Bilal, Hina, Zoya, Ayesha, Usman.

## The digital record (JazzCash, exactly as received)

```
Date,From,Amount,Memo
2025-09-02,Ali,1000,trip me + my brother Omar
2025-09-02,Sara,500,trip dues
2025-09-03,Bilal,500,
2025-09-03,Hina,500,class trip
2025-09-05,0300-unknown,500,
2025-09-05,Usman,300,pizza
2025-09-06,Zoya,500,dues
2025-09-08,Ayesha,500,trip
```

## The rules only I know (encoded)

1. **Ali's 1,000 covers Ali AND his brother Omar** — count it for both.
2. **Usman's 300 "pizza" is a repayment**, not dues — ignore it.
3. **The 500 from "0300-unknown" has no name I recognize** — do not assume, flag it.

## Result — the reconciled books

**Paid (7 of 8):** Ali, Omar, Sara, Bilal, Hina, Zoya, Ayesha.
**Still owes (1): Usman — 500.** His only payment was the 300 pizza repayment, which
isn't dues, so he hasn't paid the trip.
**Flagged, not matched:** the 500 from "0300-unknown" — credited to nobody.
**Ignored per rules:** Usman's 300 "pizza."

| | Amount |
|---|---|
| Counted total (target) | 4,000 |
| Dues accounted for | 3,500 |
| **Gap** | **500 short** |
| Unmatched money in limbo | 500 |

## How I verified against my counted total

My hand count was 4,000. The script accounts for 3,500 in real dues, leaving a **500
gap** — which is exactly Usman's unpaid dues. Separately there's a **500 unmatched**
payment. The gap and the unmatched amount are equal, but that's a coincidence I did
**not** treat as "they cancel out": if the unknown 500 is Usman, I'm square; if it's
someone else, I'm still short *and* holding a stranger's money. Two separate open items.

## What worked, what didn't, problems faced

- **Worked:** the "cover two people with one payment" rule and the "ignore repayment"
  rule both applied cleanly.
- **The trap avoided:** assuming the unknown 500 was Usman's dues. The rules said don't
  guess, so the script flags it instead of silently balancing the books.
- **Limitation:** the unknown sender can only be resolved by me (checking the phone
  number), which is exactly why the script surfaces it rather than deciding.

## Who to follow up with

1. **Usman** — still owes 500 trip dues (the 300 was pizza money).
2. **"0300-unknown"** — confirm whose payment this is before spending it.

## Files in this folder

- `reconcile.py` — the reusable script (edit target, records, and rules at the top)
- `books-dont-match-report.html` — the shareable report page (source of the live demo)
- `Books_Dont_Match_Report.pdf` — one-page report
- `README.md` — this file

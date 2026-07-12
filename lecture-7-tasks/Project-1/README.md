# Project 1 — Money Detective

**Live demo:** https://money-detective-report.netlify.app/

> "Don't track your money going forward. Hunt the leak hiding in your own real history."

## The problem it solves

Instead of starting a new budget, this project examines my past transactions
(June–September 2025) to find the leaks a normal budgeting app would miss:
recurring charges, a forgotten subscription, and a duplicate payment. The rules
for what counts as a "leak" are personal, so no ready-made app can do this — the
code has to encode *my* logic.

## AI tool used

Claude (Anthropic) — used as the coder while I acted as the client: I described
the problem, handed over my real transaction export, and verified every number
against totals I already knew.

## The data

A CSV export of my own transactions with three columns: `Date`, `What`, `Amount`
(income is positive, spending is negative). 28 rows across 4 months.

## How the code works (in plain English)

- **Reads the file** one row at a time; income is the `+` numbers, spending the `-`.
- **Recurring charge** = the same description appears in **2 or more months**
  (this catches forgotten subscriptions — the tell is repetition, not the amount).
- **Duplicate charge** = the **same date + same description + same amount** appears
  more than once (this catches a genuine double-billing, not two separate meals
  that happen to cost the same on different days).
- **Totals** are plain addition, grouped by month using the `YYYY-MM` date prefix.

## What the detective found

| Finding | Detail | Action |
|---|---|---|
| **Double charge** | Foodpanda, Rs 650, billed twice on 2025-07-08 | Dispute — Rs 650 recoverable |
| **Forgotten subscription** | PrimeVideo, Rs 199/mo → Rs 796 so far | Cancel if unused |
| **Biggest leak** | Food delivery, Rs 4,050 over 4 months | Bigger than all subscriptions combined |

## How I verified the result (against facts I already knew)

I never trusted output I couldn't check. Two independent checks:

1. **Income = Rs 23,000.** I know this by hand: 4 months of Rs 5,000 pocket money
   (20,000) plus two Rs 1,500 tutoring payments (3,000). The script agreed.
2. **Category totals reconcile to money-out.** Food 4,050 + Subscriptions 1,992 +
   Transport 1,250 + Bank 200 = **7,492**, which equals the total spending the
   script computed. Wallet now = 23,000 − 7,492 = **Rs 15,508**.

## What worked, what didn't, problems faced

- **Worked:** the duplicate detection cleanly isolated the one real double charge
  without false-flagging normal repeat spending.
- **Didn't at first:** an early version of the report page invented two categories
  ("Books" and "Cinema") that were **not in my data**, inflating money-out by
  Rs 2,000. Verifying against my known income total is exactly what caught it —
  the fix was to derive categories *only* from real transaction rows.
- **Limitation:** duplicate detection requires the date to match exactly. Charges
  double-billed a day or two apart wouldn't be caught by this rule as written.

## What I learned / could act on

The concrete wins: dispute the Rs 650 Foodpanda double charge, and decide whether
PrimeVideo is worth Rs 199/month. The bigger insight: I'm net positive every month
— I only *felt* broke because food delivery nibbles in small amounts. And the
verification step isn't a formality: it's what caught a real Rs 2,000 error.

## Files in this folder

- `money_detective.py` — the final, re-runnable script
- `money-detective-report.html` — the shareable report page (source of the live demo)
- `Money_Detective_Report.pdf` — one-page printable report
- `transactions.csv` — sample data (dummy values, structure intact)
- `README.md` — this file

#!/usr/bin/env python3
"""
Money Detective — hunt the leak in your transaction history.

Finds:
  1. Recurring charges (same description in 2+ months) — catches forgotten subscriptions
  2. Exact duplicate payments (same date + description + amount)
  3. Monthly spend totals + overall totals — so you can verify against numbers you know

Usage:
    python3 money_detective.py transactions.csv

CSV format expected (header row required):
    Date,What,Amount
    2025-06-01,Pocket money,+5000     <- income is positive
    2025-06-04,PrimeVideo subscription,-199   <- spending is negative
"""

import csv
import sys
from collections import defaultdict


def load(path):
    """Read rows; skip any row we can't parse and report it at the end."""
    good, bad = [], []
    with open(path, newline="") as f:
        for i, r in enumerate(csv.DictReader(f), start=2):  # line 2 = first data row
            try:
                good.append((r["Date"].strip(), r["What"].strip(), int(r["Amount"])))
            except (KeyError, ValueError, TypeError):
                bad.append((i, r))
    return good, bad


def analyze(rows):
    income = sum(a for _, _, a in rows if a > 0)
    spend = sum(a for _, _, a in rows if a < 0)

    # Monthly spend (spending only)
    monthly = defaultdict(int)
    for d, _, a in rows:
        if a < 0:
            monthly[d[:7]] += a

    # Recurring: same description appearing in 2+ distinct months
    months_by_desc = defaultdict(set)
    amounts_by_desc = defaultdict(list)
    for d, w, a in rows:
        if a < 0:
            months_by_desc[w].add(d[:7])
            amounts_by_desc[w].append(a)
    recurring = {
        w: sorted(set(amounts_by_desc[w]))
        for w in months_by_desc
        if len(months_by_desc[w]) >= 2
    }

    # Exact duplicates: same date + description + amount, seen more than once
    seen = defaultdict(int)
    for row in rows:
        seen[row] += 1
    duplicates = {k: c for k, c in seen.items() if c > 1}

    return income, spend, monthly, recurring, duplicates


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 money_detective.py <transactions.csv>")
        sys.exit(1)

    rows, bad = load(sys.argv[1])
    income, spend, monthly, recurring, duplicates = analyze(rows)

    print("=" * 50)
    print("MONEY DETECTIVE REPORT")
    print("=" * 50)

    print(f"\nTotal income:  {income:+,}")
    print(f"Total spend:   {spend:+,}")
    print(f"Net balance:   {income + spend:+,}")

    print("\nMonthly spend:")
    for m in sorted(monthly):
        print(f"  {m}: {monthly[m]:+,}")

    print("\nRecurring charges (appear in 2+ months):")
    for w, amts in recurring.items():
        flag = "  <-- amount varies" if len(amts) > 1 else ""
        print(f"  {w}: {amts}{flag}")

    print("\nDuplicate charges (same date + description + amount):")
    if duplicates:
        for (d, w, a), c in duplicates.items():
            print(f"  {d}  {w}  {a}  (x{c})  <-- possible double charge")
    else:
        print("  none found")

    if bad:
        print("\nUnreadable rows (skipped):")
        for line_no, r in bad:
            print(f"  line {line_no}: {r}")


if __name__ == "__main__":
    main()

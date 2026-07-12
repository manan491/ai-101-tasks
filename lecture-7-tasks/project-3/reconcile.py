#!/usr/bin/env python3
"""
The Books Don't Match — reconcile a hand-counted total against a messy digital record.

Two records that should agree: your counted total, and a messy payment export with
ambiguous memos. This script encodes YOUR interpretation rules, finds the gap, and
names who to follow up with — without guessing.

Edit the three sections marked EDIT as your situation changes, then re-run:
    python3 reconcile.py
"""

# ------------------------------------------------------------------
# EDIT 1 — The target you counted yourself
# ------------------------------------------------------------------
DUE_PER_PERSON = 500
ROSTER = ["Ali", "Omar", "Sara", "Bilal", "Hina", "Zoya", "Ayesha", "Usman"]
EXPECTED_TOTAL = DUE_PER_PERSON * len(ROSTER)     # 4,000

# ------------------------------------------------------------------
# EDIT 2 — The digital record, exactly as it came in (don't clean it)
#          (date, sender, amount, memo)
# ------------------------------------------------------------------
RECORDS = [
    ("2025-09-02", "Ali",          1000, "trip me + my brother Omar"),
    ("2025-09-02", "Sara",          500, "trip dues"),
    ("2025-09-03", "Bilal",         500, ""),
    ("2025-09-03", "Hina",          500, "class trip"),
    ("2025-09-05", "0300-unknown",  500, ""),
    ("2025-09-05", "Usman",         300, "pizza"),
    ("2025-09-06", "Zoya",          500, "dues"),
    ("2025-09-08", "Ayesha",        500, "trip"),
]

# ------------------------------------------------------------------
# EDIT 3 — The rules only you know, as small functions.
#          Each returns one of:
#            ("cover", [people])  -> credit these people their full dues
#            ("ignore", reason)   -> this payment is not dues
#            None                 -> rule doesn't apply, fall through
# ------------------------------------------------------------------
def apply_rules(date, sender, amount, memo):
    m = memo.lower()

    # Rule: Ali's payment covers Ali AND his brother Omar
    if sender == "Ali" and "omar" in m:
        return ("cover", ["Ali", "Omar"])

    # Rule: Usman's "pizza" payment is a repayment to me, not dues
    if sender == "Usman" and "pizza" in m:
        return ("ignore", "repayment, not dues")

    # (Unrecognised senders are handled below as unmatched — never guessed)
    return None
# ------------------------------------------------------------------


def reconcile():
    paid_for = {}      # person -> amount credited toward dues
    counted = 0        # money that counts toward the target
    ignored = []       # deliberately excluded payments
    unmatched = []     # payments we can't tie to a roster name

    for date, sender, amount, memo in RECORDS:
        rule = apply_rules(date, sender, amount, memo)

        if rule and rule[0] == "ignore":
            ignored.append((date, sender, amount, memo, rule[1]))
            continue

        if rule and rule[0] == "cover":
            for person in rule[1]:
                paid_for[person] = DUE_PER_PERSON
            counted += amount
            continue

        # No rule fired. Must be a recognised roster member, or it's unmatched.
        if sender in ROSTER:
            paid_for[sender] = paid_for.get(sender, 0) + amount
            counted += amount
        else:
            unmatched.append((date, sender, amount, memo))

    return paid_for, counted, ignored, unmatched


def report():
    paid_for, counted, ignored, unmatched = reconcile()
    paid   = [p for p in ROSTER if paid_for.get(p, 0) >= DUE_PER_PERSON]
    owing  = [p for p in ROSTER if paid_for.get(p, 0) <  DUE_PER_PERSON]

    print("=" * 48)
    print("THE BOOKS DON'T MATCH — reconciliation")
    print("=" * 48)
    print(f"\nCounted total (target): {EXPECTED_TOTAL}")

    print(f"\nPAID ({len(paid)}/{len(ROSTER)}):")
    for p in paid:
        print(f"  {p}: {paid_for[p]}")

    print(f"\nSTILL OWES:")
    if owing:
        for p in owing:
            print(f"  {p}: paid {paid_for.get(p,0)}, owes {DUE_PER_PERSON - paid_for.get(p,0)}")
    else:
        print("  nobody")

    print(f"\nIGNORED (per your rules):")
    for d, s, a, mm, why in ignored:
        print(f'  {d} {s} {a} "{mm}" -> {why}')

    print(f"\nUNMATCHED (flagged, NOT guessed):")
    for d, s, a, mm in unmatched:
        print(f'  {d} {s} {a} "{mm}"')

    gap = EXPECTED_TOTAL - counted
    limbo = sum(a for _, _, a, _ in unmatched)
    print("\n" + "-" * 48)
    print(f"Dues accounted for : {counted}")
    print(f"Gap (target - accounted): {gap}")
    print(f"Unmatched money in limbo: {limbo}")
    print("-" * 48)
    print("\nNOTE: even if the gap equals the unmatched amount, do NOT assume")
    print("they cancel out. Confirm whose the unmatched payment is first.")


if __name__ == "__main__":
    report()

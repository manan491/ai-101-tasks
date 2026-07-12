#!/usr/bin/env python3
"""
What's My Grade, Really — encode your teacher's exact rules and find your true grade.

Encodes one specific teacher's policy:
  - Homework 20%: drop the two lowest, average the rest
  - Quizzes  20%: best 8 of 10 count
  - Midterm  25%
  - Final    35%: if the final is higher than the midterm, the final
                  REPLACES the midterm too (final then counts in both slots)

Update the scores below throughout the term and re-run:
    python3 whats_my_grade.py
"""

# ------------------------------------------------------------------
# EDIT THESE as new scores come in
# ------------------------------------------------------------------
HOMEWORK = [60, 92, 88, 45, 90, 85]
QUIZZES  = [70, 95, 88, 100, 0, 91, 84, 77, 93, 80]
MIDTERM  = 72
FINAL    = 86          # set to your real/expected final; None if not taken yet
TARGET   = 90          # the overall grade you're aiming for

# Rule knobs (change if your policy differs)
HW_DROP_LOWEST   = 2
QUIZ_BEST_N      = 8
W_HOMEWORK       = 0.20
W_QUIZZES        = 0.20
W_MIDTERM        = 0.25
W_FINAL          = 0.35
# ------------------------------------------------------------------


def homework_average(scores):
    kept = sorted(scores)[HW_DROP_LOWEST:]          # drop the two lowest
    return sum(kept) / len(kept), sorted(scores)[:HW_DROP_LOWEST], kept


def quiz_average(scores):
    best = sorted(scores, reverse=True)[:QUIZ_BEST_N]   # best 8 of 10
    dropped = sorted(scores, reverse=True)[QUIZ_BEST_N:]
    return sum(best) / len(best), sorted(best), sorted(dropped)


def midterm_used(midterm, final):
    """The final replaces the midterm when it is strictly higher."""
    if final is not None and final > midterm:
        return final, True
    return midterm, False


def compute():
    hw_avg, hw_dropped, hw_kept = homework_average(HOMEWORK)
    qz_avg, qz_best, qz_dropped = quiz_average(QUIZZES)
    mid_val, replaced = midterm_used(MIDTERM, FINAL)

    hw_sub  = hw_avg * W_HOMEWORK
    qz_sub  = qz_avg * W_QUIZZES
    mid_sub = mid_val * W_MIDTERM
    fin_sub = (FINAL if FINAL is not None else 0) * W_FINAL
    total   = hw_sub + qz_sub + mid_sub + fin_sub

    print("=" * 46)
    print("WHAT'S MY GRADE, REALLY")
    print("=" * 46)

    print(f"\nHOMEWORK (20%)")
    print(f"  dropped two lowest : {hw_dropped}")
    print(f"  kept               : {hw_kept}")
    print(f"  average            : {hw_avg:.2f}   subtotal: {hw_sub:.2f}")

    print(f"\nQUIZZES (20%)  best {QUIZ_BEST_N} of {len(QUIZZES)}")
    print(f"  dropped            : {qz_dropped}")
    print(f"  best {QUIZ_BEST_N}            : {qz_best}")
    print(f"  average            : {qz_avg:.2f}   subtotal: {qz_sub:.2f}")

    print(f"\nMIDTERM (25%) / FINAL (35%)")
    print(f"  midterm={MIDTERM}  final={FINAL}"
          + ("  -> final replaces midterm" if replaced else "  -> midterm stays"))
    print(f"  midterm used       : {mid_val}    subtotal: {mid_sub:.2f}")
    print(f"  final              : {FINAL}    subtotal: {fin_sub:.2f}")

    print("\n" + "-" * 46)
    print(f"CURRENT GRADE: {total:.2f}%")
    print("-" * 46)

    return total, hw_sub, qz_sub


def final_needed_for_target(hw_sub, qz_sub):
    """
    Solve for the final score F that reaches TARGET.
    When F > MIDTERM the final counts in BOTH slots, so its weight is
    (W_MIDTERM + W_FINAL). Otherwise only W_FINAL, with midterm fixed.
    """
    fixed = hw_sub + qz_sub

    # Case A: final replaces midterm (F > MIDTERM)
    weight_a = W_MIDTERM + W_FINAL
    f_a = (TARGET - fixed) / weight_a
    if f_a > MIDTERM:
        return f_a, "final replaces midterm (counts in both slots)"

    # Case B: midterm stays fixed
    f_b = (TARGET - fixed - MIDTERM * W_MIDTERM) / W_FINAL
    return f_b, "midterm stays; final counts in the 35% slot only"


if __name__ == "__main__":
    total, hw_sub, qz_sub = compute()
    need, why = final_needed_for_target(hw_sub, qz_sub)
    print(f"\nTo reach {TARGET}%: you need about {need:.2f} on the final")
    print(f"  ({why})")
    if need > 100:
        print("  NOTE: that's above 100 — the target isn't reachable on the final alone.")

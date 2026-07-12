# Project 4 — Organize the Mess (The Files You Forgot)

**Live demo:** https://organize-the-mess.netlify.app/

> "Find what's actually in your folders." — done safely, with your originals untouched.

## The problem it solves

Photo folders accumulate duplicates you can't see: the same shot resized, re-saved by
WhatsApp, screenshotted, or thumbnailed. Ordinary "find duplicates" tools only catch
byte-identical files, so these near-copies slip through. This fingerprints every image
with a **perceptual hash**, groups the ones that look the same, and reports how many
duplicates there are and how much space they waste — **without deleting anything.**

## AI tool used

Claude (Anthropic). I acted as the client: I described what "clean" means for me
(near-duplicate photos), and demanded a **dry run** — a full plan first, approval before
anything is touched.

## The safety discipline (the point of this task)

This project touches real files, so it follows the assignment's safety order exactly:

1. **Copy first.** The script backs up the entire folder to a timestamped copy before
   doing anything (`folder__backup-YYYYMMDD-HHMMSS`).
2. **Read-only.** It never deletes, moves, or renames an original — it only *reads* and
   *proposes*.
3. **Dry run.** It prints a plan: which file to keep and which copies you *could* delete.
   Deletion is a separate step that only happens after you approve.

## What "clean" means here (the rules)

- Match on **perceptual hash**, not file bytes — a resized or re-compressed copy still
  counts as a duplicate.
- **Near-duplicate** = within a small hash distance (default 5 bits), not just an exact
  match.
- In each group, **keep the largest** (by resolution, then bytes); list the rest as
  deletable — so the full-res version is never the one proposed for deletion.
- **Skip** unreadable/corrupt files and non-images; list them at the end.
- **Flag** any copy that's much smaller than the keeper (a likely thumbnail) so it isn't
  deleted by mistake.

## Result — the dry-run report (on a sample messy folder)

Ran on a 9-image test folder (plus a stray `.txt` and a corrupt `.jpg`):

```
GROUP 1  (2 matching images)
  KEEP    DSC00891.png            [1400x1400, 11.1 KB]
  delete  IMG-20250903-WA0007.jpg [1050x1050, 42.8 KB]   (WhatsApp recompress)

GROUP 2  (4 matching images)
  KEEP    IMG_2043.jpg            [1600x1200, 92.3 KB]
  delete  beach_sunset_edited.jpg [1600x1200, 54.4 KB]
  delete  IMG_2043-copy.jpg       [800x600,   28.0 KB]
  delete  thumb_2043.jpg          [160x120,    3.8 KB]  <-- flagged: thumbnail

Duplicate groups found  : 2
Extra copies (deletable): 4
Space reclaimable       : 129.0 KB
Skipped: broken.jpg (unreadable), notes.txt (not an image)
```

## How I verified the result

I checked the reported reclaimable space by hand: the four deletable files sum to
132,131 bytes = **129.0 KB**, matching the script exactly. I also confirmed all 11
files were still present after the run (nothing deleted) and that, with backup enabled,
the script copied all 11 files to a timestamped folder first. On a real folder the same
check applies — pick one group and confirm the "keep" file really is the best copy
before approving any deletion.

## What worked, what didn't, problems faced

- **Worked:** perceptual hashing caught the resized copy, the re-saved lower-quality
  copy, the WhatsApp recompress, and the thumbnail — none of which are byte-identical.
- **The safety trap avoided:** the script never deletes. It proposes; I approve. On real
  files that distinction is everything.
- **Watch-out:** the "keeper" is chosen by resolution first, so a higher-res but
  smaller-byte file (e.g. a PNG) can be kept over a larger JPG. That's usually right, but
  it's why the report shows dimensions and sizes — so you can override before approving.
- **Threshold tuning:** the near-duplicate distance (5 bits) can be raised to catch
  looser matches or lowered to be stricter, depending on your folder.

## What I learned / could act on

On the sample, 4 redundant copies across 2 groups. On a real Downloads or Photos folder
this typically surfaces hundreds of MB of resized/re-saved duplicates you didn't know
were there — reclaimable safely, because the plan is reviewed before anything is removed.

## Files in this folder

- `find_duplicate_photos.py` — the dry-run script (backup-first, read-only, perceptual-hash)
- `organize-the-mess-report.html` — the shareable report page
- `Organize_The_Mess_Report.pdf` — one-page report
- `README.md` — this file

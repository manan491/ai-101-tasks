# Brief: Find duplicate and near-duplicate photos in a folder

## Goal
Find the duplicate and near-duplicate photos cluttering my folder — so I
can see how much space they're wasting and decide what to delete — without
anything being deleted yet.

## Input
A folder of image files (JPG, PNG, and similar). I don't know the exact
count — could be a few dozen to a few thousand. Some are true copies, some
are near-duplicates (same shot resized, re-saved, lightly edited, or
screenshotted).

## Output
A report I can read, showing:
- how many duplicate/near-duplicate images were found,
- how much disk space they take up (and how much I'd reclaim by keeping
  one per group),
- the images grouped into match-clusters, with each file's path and size.

## Rules
The constraints a stranger wouldn't know:
- Match on **perceptual hash**, not exact file bytes — so a resized or
  re-compressed copy still counts as a duplicate, not just byte-identical files.
- "Near-duplicate" means within a small hash distance, not only an exact
  hash match. Same picture, different file = a match.
- This is a **dry run only**: fingerprint, group, and report. Do NOT delete,
  move, or rename anything. Work read-only on the originals.

## Edge cases
What to do when the data isn't clean:
- A file that isn't a real image, or is corrupt/unreadable: skip it and list
  it at the end rather than crashing.
- A non-image file that slipped into the folder (e.g. a stray .txt or .pdf):
  ignore it.
- Within a match-group, keep the largest/highest-resolution file as the
  "keeper" when estimating reclaimable space, since that's the one I'd likely
  keep.
- If two images are visually identical but one is much smaller (a thumbnail),
  still group them, but flag the size gap so I don't delete the full-res one
  by mistake.
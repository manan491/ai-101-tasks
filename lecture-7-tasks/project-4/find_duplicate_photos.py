#!/usr/bin/env python3
"""
Organize the Mess — find duplicate & near-duplicate photos (DRY RUN ONLY).

Safety discipline (follows the assignment's safety order):
  1. COPY FIRST  — backs up the whole folder to a new location before doing anything.
  2. READ ONLY   — never deletes, moves, or renames a single original file.
  3. DRY RUN     — only PROPOSES what you could delete, and waits for your approval.
  Nothing is removed. You get a plan; you decide.

How it matches:
  Each image is fingerprinted with a PERCEPTUAL hash (not file bytes), so a resized,
  re-compressed, or lightly re-saved copy still counts as a duplicate. Images whose
  hashes are within THRESHOLD bits of each other are grouped together.

Within each group it keeps the LARGEST file (by resolution, then bytes) as the keeper
and lists the rest as "could delete" — so you never lose the full-res version.

Usage:
    python3 find_duplicate_photos.py /path/to/messy/folder
    python3 find_duplicate_photos.py /path/to/folder --no-backup
"""

import sys
import os
import shutil
import argparse
from datetime import datetime

from PIL import Image
import imagehash

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".tif"}
THRESHOLD = 5          # max Hamming distance between hashes to count as "near-duplicate"
HASH_SIZE = 16         # bigger = more precise fingerprint


def human(n):
    for unit in ["B", "KB", "MB", "GB"]:
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def backup_folder(src):
    """Step 1: copy the entire folder before touching anything."""
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    dest = f"{src.rstrip('/')}__backup-{stamp}"
    shutil.copytree(src, dest)
    return dest


def fingerprint_images(folder):
    """Hash every readable image. Skip and record anything unreadable / non-image."""
    fingerprints = []   # (path, hash, width, height, bytes)
    skipped = []        # (path, reason)
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            ext = os.path.splitext(name)[1].lower()
            if ext not in IMAGE_EXTS:
                skipped.append((path, "not an image file"))
                continue
            try:
                with Image.open(path) as im:
                    im.load()
                    h = imagehash.phash(im, hash_size=HASH_SIZE)
                    w, ht = im.size
                fingerprints.append((path, h, w, ht, os.path.getsize(path)))
            except Exception as e:
                skipped.append((path, f"unreadable: {type(e).__name__}"))
    return fingerprints, skipped


def group_duplicates(fingerprints):
    """Cluster images whose perceptual hashes are within THRESHOLD of each other."""
    groups = []
    used = [False] * len(fingerprints)
    for i in range(len(fingerprints)):
        if used[i]:
            continue
        cluster = [fingerprints[i]]
        used[i] = True
        for j in range(i + 1, len(fingerprints)):
            if used[j]:
                continue
            if fingerprints[i][1] - fingerprints[j][1] <= THRESHOLD:
                cluster.append(fingerprints[j])
                used[j] = True
        if len(cluster) > 1:                 # only keep real duplicate groups
            groups.append(cluster)
    return groups


def report(folder, groups, skipped):
    print("=" * 58)
    print("ORGANIZE THE MESS — duplicate photo report (DRY RUN)")
    print("=" * 58)
    print(f"\nFolder scanned: {folder}")

    total_dupe_files = 0
    reclaimable = 0

    for n, cluster in enumerate(groups, 1):
        cluster_sorted = sorted(cluster, key=lambda x: (x[2] * x[3], x[4]), reverse=True)
        keeper = cluster_sorted[0]
        deletable = cluster_sorted[1:]

        print(f"\nGROUP {n}  ({len(cluster)} matching images)")
        print(f"  KEEP    {os.path.basename(keeper[0])}"
              f"  [{keeper[2]}x{keeper[3]}, {human(keeper[4])}]")
        for d in deletable:
            flag = "  <-- much smaller (thumbnail?)" if d[4] * 4 < keeper[4] else ""
            print(f"  delete  {os.path.basename(d[0])}"
                  f"  [{d[2]}x{d[3]}, {human(d[4])}]{flag}")
            total_dupe_files += 1
            reclaimable += d[4]

    print("\n" + "-" * 58)
    print(f"Duplicate groups found : {len(groups)}")
    print(f"Extra copies (deletable): {total_dupe_files}")
    print(f"Space reclaimable       : {human(reclaimable)}")
    print("-" * 58)

    if skipped:
        print(f"\nSkipped {len(skipped)} file(s):")
        for path, reason in skipped:
            print(f"  {os.path.basename(path)} — {reason}")

    print("\nDRY RUN COMPLETE. Nothing was deleted, moved, or renamed.")
    print("Review the plan above. Deletion is a separate, approved step.")
    return len(groups), total_dupe_files, reclaimable


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--no-backup", action="store_true", help="skip the backup copy step")
    args = ap.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Not a folder: {args.folder}")
        sys.exit(1)

    if not args.no_backup:
        dest = backup_folder(args.folder)
        print(f"[safety] Backed up entire folder to: {dest}\n")
    else:
        print("[safety] Backup skipped (--no-backup). Working read-only on originals.\n")

    fingerprints, skipped = fingerprint_images(args.folder)
    groups = group_duplicates(fingerprints)
    report(args.folder, groups, skipped)


if __name__ == "__main__":
    main()

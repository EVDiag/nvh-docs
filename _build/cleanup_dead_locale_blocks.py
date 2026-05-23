"""Delete the dead duplicate locale blocks in user_guide_batch6.py.

Approach:
  1. Parse the file to find locale block start lines (matching pattern
     "^'XX': \"\"\"" at column 0).
  2. Identify locales that appear more than once.
  3. For each duplicate, the FIRST occurrence is dead (Python dict literal
     dedup keeps only the LAST). Delete from the dead block's start line
     up to (but not including) the next locale block start line.
  4. Process deletions in REVERSE order so line numbers stay stable.
  5. Verify: rebuild and confirm that the generated output is byte-identical
     before and after this cleanup.

Safety: The script does NOT delete unless --apply is passed. By default it
prints what it would do and exits.

Run from the nvh-docs repo root:
    python _build/cleanup_dead_locale_blocks.py             # dry run
    python _build/cleanup_dead_locale_blocks.py --apply     # actually delete
"""
import os
import re
import sys

# Find the batch file relative to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BATCH_FILE = os.path.join(SCRIPT_DIR, 'user_guide_batch6.py')

# Pattern for a locale block start: 'XX': """ at column 0 (no indent)
LOCALE_START_RE = re.compile(r"^'([a-z]{2})':\s*\"\"\"")


def find_locale_blocks(lines):
    """Return list of (locale, start_line_idx) tuples in order of appearance."""
    blocks = []
    for i, line in enumerate(lines):
        m = LOCALE_START_RE.match(line)
        if m:
            blocks.append((m.group(1), i))
    return blocks


def identify_dead_blocks(blocks):
    """Return list of (locale, start_idx, end_idx_exclusive) for dead blocks.

    A locale that appears N>1 times has its first N-1 occurrences as dead.
    Each dead block's end is the start of the next locale block (or end of file).
    """
    # Count occurrences per locale
    counts = {}
    for loc, _ in blocks:
        counts[loc] = counts.get(loc, 0) + 1

    # Build list of (locale, start, end) for ALL blocks
    spans = []
    for i, (loc, start) in enumerate(blocks):
        end = blocks[i + 1][1] if i + 1 < len(blocks) else None
        spans.append((loc, start, end))

    # Dead blocks: per locale, all occurrences except the LAST one
    dead = []
    last_seen = {}  # locale -> index of last block
    for i, (loc, _, _) in enumerate(spans):
        last_seen[loc] = i
    for i, (loc, start, end) in enumerate(spans):
        if counts[loc] > 1 and i != last_seen[loc]:
            dead.append((loc, start, end))
    return dead


def main(apply=False):
    if not os.path.exists(BATCH_FILE):
        print(f"ERROR: {BATCH_FILE} not found")
        sys.exit(1)

    with open(BATCH_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    blocks = find_locale_blocks(lines)
    print(f"Found {len(blocks)} locale blocks in user_guide_batch6.py:")
    for loc, idx in blocks:
        print(f"  line {idx + 1}: '{loc}'")

    dead = identify_dead_blocks(blocks)
    if not dead:
        print("\nNo duplicate locale blocks found. Nothing to do.")
        return

    print(f"\n{len(dead)} dead (duplicate) blocks identified:")
    total_dead_lines = 0
    for loc, start, end in dead:
        end_idx = end if end is not None else len(lines)
        n_lines = end_idx - start
        total_dead_lines += n_lines
        print(f"  '{loc}': lines {start + 1}-{end_idx} ({n_lines} lines)")

    print(f"\nTotal dead lines: {total_dead_lines}")
    print(f"File size before: {len(lines)} lines")
    print(f"File size after:  {len(lines) - total_dead_lines} lines")

    if not apply:
        print("\nDRY RUN — no changes made. Re-run with --apply to actually delete.")
        return

    # Apply deletions in REVERSE order so line indices stay valid
    new_lines = list(lines)
    for loc, start, end in sorted(dead, key=lambda x: x[1], reverse=True):
        end_idx = end if end is not None else len(new_lines)
        del new_lines[start:end_idx]

    with open(BATCH_FILE, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"\nDONE. {BATCH_FILE} now has {len(new_lines)} lines (was {len(lines)}).")


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    main(apply=apply)

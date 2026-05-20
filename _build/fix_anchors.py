"""Fix broken TOC anchors in translated user-guide.html files.

Problem: python-markdown auto-generates heading IDs from heading text.
When headings are translated (e.g., "How it works" -> "Jak to funguje"),
the IDs change to match the new text, but the TOC links still use the
original English slugs (#how-it-works). Result: clicking a TOC entry
does nothing.

Fix: extract heading IDs from en/user-guide.html in document order,
then overwrite each translated file's heading IDs with the English ones
(matched positionally). This works because the document structure
(number and order of h1/h2/h3 headings) is identical across all locales.
"""

import os
import re
import sys

DOCS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HEADING_RE = re.compile(r'(<h([1-6]))\s+id="([^"]*)"', re.IGNORECASE)


def extract_ids(html: str):
    """Return list of (level, id) tuples in document order."""
    return [(m.group(2), m.group(3)) for m in HEADING_RE.finditer(html)]


def rewrite_ids(html: str, english_ids):
    """Replace each heading's id attribute with the positionally-matched English id."""
    it = iter(english_ids)

    def sub(m):
        try:
            level, eng_id = next(it)
        except StopIteration:
            return m.group(0)
        # Sanity check: heading level should match
        if level != m.group(2):
            print(f"  WARN: level mismatch — expected h{level}, found h{m.group(2)}")
        return f'{m.group(1)} id="{eng_id}"'

    new_html, n = HEADING_RE.subn(sub, html)
    return new_html, n


def main():
    en_path = os.path.join(DOCS_ROOT, "en", "user-guide.html")
    with open(en_path, encoding="utf-8") as f:
        en_html = f.read()
    english_ids = extract_ids(en_html)
    print(f"Extracted {len(english_ids)} heading IDs from en/user-guide.html")

    locales = sorted(
        d for d in os.listdir(DOCS_ROOT)
        if os.path.isdir(os.path.join(DOCS_ROOT, d))
        and d != "en"
        and os.path.exists(os.path.join(DOCS_ROOT, d, "user-guide.html"))
    )

    total_changed = 0
    for loc in locales:
        path = os.path.join(DOCS_ROOT, loc, "user-guide.html")
        with open(path, encoding="utf-8") as f:
            html = f.read()
        loc_ids = extract_ids(html)
        if len(loc_ids) != len(english_ids):
            print(f"  SKIP {loc}: heading count mismatch ({len(loc_ids)} vs {len(english_ids)})")
            continue
        new_html, n = rewrite_ids(html, english_ids)
        if new_html != html:
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(new_html)
            total_changed += 1
            print(f"  {loc}: rewrote {n} heading IDs")
        else:
            print(f"  {loc}: no changes needed")

    print(f"\nDone. Updated {total_changed} of {len(locales)} translated user guides.")


if __name__ == "__main__":
    main()

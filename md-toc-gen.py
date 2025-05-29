#!/usr/bin/env python3

"""
Generate or refresh a Markdown Table of Contents (TOC).

Examples
--------
  md-toc README.md
  md-toc README.md --depth 2
  md-toc README.md --no-overwrite
"""
import argparse
import re
import sys
import string
from pathlib import Path


def slugify(text: str) -> str:
    """Return a GitHub-style anchor slug for a heading.

    Rules (mirrors current GitHub behaviour):
      1. Lower-case the text.
      2. Remove every character except ASCII letters, numbers, spaces and dashes.
      3. Convert spaces → dashes **without collapsing repeats**.  
         This means two adjacent spaces (created when we delete e.g. an “&”) turn
         into two dashes — so "Four & four" → "four--four".
      4. Trim leading/trailing dashes.
    """
    anchor = text.strip().lower()
    allowed = set(string.ascii_lowercase + string.digits + " -")
    anchor = ''.join(ch for ch in anchor if ch in allowed)
    anchor = anchor.replace(' ', '-')
    return anchor.strip('-')


def generate_toc(md: str, max_level: int) -> str:
    """Create the Table of Contents as a Markdown string."""
    lines = ["## Table of Contents", ""]
    for hashes, title in re.findall(r'^(#{2,6})\s+(.+)$', md, re.MULTILINE):
        level = len(hashes) - 1
        if level <= max_level:
            indent = " " * ((level - 1) * 2)
            lines.append(f"{indent}- [{title}](#{slugify(title)})")
    return "\n".join(lines)  # no trailing blank line so we can control spacing


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate (or refresh) a Markdown Table of Contents.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Examples:\n  md-toc README.md\n  md-toc README.md --depth 2"
    )
    parser.add_argument("filename", help="Markdown file to update")
    parser.add_argument("-d", "--depth", type=int, choices=range(1, 6),
                        default=1, metavar="N",
                        help="Include headings down to level N (default: 1)")
    parser.add_argument("--no-overwrite", action="store_true",
                        help="Leave the file unchanged if a TOC already exists")
    args = parser.parse_args()

    path = Path(args.filename)
    try:
        md = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        parser.error(f"File not found: {path}")

    # Remove any existing TOC (keep at most one leading newline)
    toc_block = re.compile(
        r"\n?##\s*Table of Contents\n(?:[ \t]*\n|[ \t]*- .+\n)+", re.MULTILINE)
    md = toc_block.sub("\n", md, count=1)

    # Find first H1
    h1_match = re.search(r'^# .+$', md, re.MULTILINE)
    insert_at = h1_match.end() if h1_match else 0

    # Exactly one blank line after H1 and after TOC
    before = md[:insert_at].rstrip('\n') + '\n\n'
    after = md[insert_at:].lstrip('\n')

    toc = generate_toc(md, args.depth).rstrip('\n')
    new_md = before + toc + '\n\n' + after

    path.write_text(new_md, encoding="utf-8")


if __name__ == "__main__":
    main()

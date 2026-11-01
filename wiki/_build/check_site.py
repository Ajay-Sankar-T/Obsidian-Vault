#!/usr/bin/env python3
"""Sanity-check the built site: broken internal links and anchors, leftover placeholders, personal strings, size."""
import re, sys
from pathlib import Path
from urllib.parse import unquote

WIKI = Path(__file__).resolve().parent.parent
PERSONAL = ["ME25B012", "EP25B001", "CH25B002", "ME25B146", "CS25B028", "Group 14", "Batch B", "Ajay Sankar", "Gudditi", "Aadit Pankaj"]
pages = [p for p in WIKI.rglob("*.html") if "_build" not in p.parts and "node_modules" not in p.parts]
ids = {p: set(re.findall(r'\bid="([^"]+)"', p.read_text(encoding="utf-8"))) for p in pages}
bad, anchors, leftovers, personal = [], [], [], []
for p in pages:
    t = p.read_text(encoding="utf-8")
    if re.search(r"[-]", t):
        leftovers.append(p.name)
    for s in PERSONAL:
        if s in t:
            personal.append((p.name, s))
    for m in re.finditer(r'(?:href|src)="([^"#]*)(#[^"]*)?"', t):
        href, frag = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|javascript:|data:)", href):
            continue
        if href == "":
            target = p
        else:
            target = (p.parent / unquote(href)).resolve()
            if "../.." in href or not str(target).startswith(str(WIKI)):
                continue  # links out to vault PDFs
            if not target.exists():
                bad.append((p.name, href)); continue
        if frag and target.suffix == ".html" and target in ids and frag[1:] not in ids[target]:
            anchors.append((p.name, href + frag))
print(f"pages: {len(pages)}  broken links: {len(bad)}  broken anchors: {len(anchors)}  leftover math/stash tokens: {len(leftovers)}  personal strings: {len(personal)}")
for b in bad[:15]: print("  broken:", b)
for a in anchors[:15]: print("  anchor:", a)
for l in leftovers[:10]: print("  placeholder in:", l)
for q in personal[:10]: print("  personal:", q)
size = sum(f.stat().st_size for f in WIKI.rglob("*") if f.is_file() and "_build" not in f.parts)
print(f"size (excluding _build): {size/1e6:.1f} MB")
sys.exit(1 if (bad or leftovers or personal) else 0)

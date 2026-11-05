"""Check that every [[wikilink]] and ![[image]] in the Physics notes resolves somewhere in the vault."""
import os
import re
import sys

PHYS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
VAULT = os.path.normpath(os.path.join(PHYS, "..", ".."))
names = set()
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "wiki", "graphify-out", ".obsidian")]
    for f in files:
        names.add(os.path.splitext(f)[0].lower()); names.add(f.lower())
bad = 0
count = 0
for root, _, files in os.walk(PHYS):
    for f in files:
        if not f.endswith(".md"):
            continue
        text = open(os.path.join(root, f), encoding="utf-8").read()
        for m in re.finditer(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", text):
            t = m.group(1).strip(); count += 1
            key = os.path.basename(t).lower()
            if key not in names and os.path.splitext(key)[0] not in names:
                bad += 1; print("BROKEN in", f, "->", t)
print(count, "links checked,", bad, "broken")
sys.exit(1 if bad else 0)

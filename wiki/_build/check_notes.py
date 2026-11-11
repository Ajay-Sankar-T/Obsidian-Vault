"""Check every [[wikilink]] / ![[image]] in the given vault folders resolves to a real file somewhere in the vault.
usage: python check_notes.py "Mechanical Engineering/Physics Lab" "Mechanical Engineering/Applied Mechanics Lab" ..."""
import os
import re
import sys

VAULT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
names = set()
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "wiki", "graphify-out", ".obsidian")]
    for f in files:
        names.add(f.lower()); names.add(os.path.splitext(f)[0].lower())
bad = count = 0
for folder in sys.argv[1:]:
    for root, _, files in os.walk(os.path.join(VAULT, folder)):
        for f in files:
            if not f.endswith(".md"):
                continue
            text = open(os.path.join(root, f), encoding="utf-8").read()
            for m in re.finditer(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]", text):
                t = m.group(1).strip(); count += 1; key = os.path.basename(t).lower()
                if key not in names and os.path.splitext(key)[0] not in names:
                    bad += 1; print("BROKEN in", f, "->", t)
print(count, "links checked,", bad, "broken")
sys.exit(1 if bad else 0)

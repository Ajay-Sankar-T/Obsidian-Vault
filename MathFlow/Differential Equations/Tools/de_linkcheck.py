"""Check that every [[wikilink]] and ![[embed]] in the Differential Equations notes resolves to a file or a heading."""
import os, re, io
VAULT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
DE = os.path.join(VAULT, "MathFlow", "Differential Equations")
names = {}
for dp, dn, fn in os.walk(VAULT):
    if ".git" in dp or ".obsidian" in dp: continue
    for f in fn:
        names.setdefault(f.lower(), os.path.join(dp, f)); names.setdefault(os.path.splitext(f)[0].lower(), os.path.join(dp, f))
def headings(path):
    hs = set()
    for line in io.open(path, encoding="utf-8", errors="ignore"):
        m = re.match(r"^#{1,6}\s+(.*)", line)
        if m: hs.add(re.sub(r"[\s]+", " ", m.group(1).strip()).lower())
    return hs
bad = []; n = 0
for dp, dn, fn in os.walk(DE):
    if "Tools" in dp or "assets" in dp: continue
    for f in fn:
        if not f.endswith(".md"): continue
        p = os.path.join(dp, f); text = io.open(p, encoding="utf-8").read()
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for m in re.finditer(r"!?\[\[([^\]]+)\]\]", text):
            t = m.group(1).split("|")[0].replace("\\", ""); target, _, head = t.partition("#"); n += 1
            if target == "" and head: continue
            key = target.strip().lower(); key = key.split("/")[-1]
            if key not in names: bad.append((f, m.group(0))); continue
            if head and names[key].endswith(".md"):
                hs = headings(names[key]); hh = re.sub(r"\s+", " ", head.strip()).lower()
                if hh not in hs and not any(hh == re.sub(r"[$\\]", "", h) for h in hs): bad.append((f, m.group(0) + "  (heading)"))
print("links checked:", n, " unresolved:", len(bad))
for b in bad: print(b)

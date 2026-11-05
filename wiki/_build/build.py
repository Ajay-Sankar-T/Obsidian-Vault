#!/usr/bin/env python3
"""Build the static learning site in wiki/ from the Obsidian vault.

    python wiki/_build/build.py          (run from anywhere; needs `pip install markdown` and `npm install` in wiki/_build)

Reads the notes, renders them to HTML (wikilinks, callouts, KaTeX math, mermaid, task lists), turns lesson and problem notes
into interactive pages, and writes wiki/index.html, wiki/course/*.html, wiki/n/*.html, wiki/practice.html, wiki/solve.html,
wiki/graph.html and wiki/assets/*.  Personal folders (Applications, Clubs & Projects, team assignments, logs) are excluded.
"""
import html as H
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys
import urllib.parse
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify as md_slugify

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
WIKI = HERE.parent
VAULT = WIKI.parent
ASSETS = WIKI / "assets"

# --------------------------------------------------------------------------------------------- scope
EXCL_DIRS = {"wiki", ".git", ".obsidian", ".claude", "graphify-out", "Templates", "Excalidraw", "Applications", "Clubs & Projects",
             "Chemistry", "Life sciences", "node_modules", "__pycache__"}
EXCL_PREFIX = ("Entrepreneurship/Solution",)
EXCL_FILES = {"CLAUDE.md", "LLM Wiki Guide.md", "Wiki Maintenance Log.md", "Home.md"}
STRIP_SECTIONS = re.compile(r"^(MOC Maintenance Rules|Study Log|Course Completion Checklist|Maintenance)\b", re.I)

COURSES = [
    # id, title, code, colour, dark shade, root prefix, blurb
    ("de", "Differential Equations", "MA2020", "#7a5a9a", "#4f3a6b", "MathFlow/Differential Equations", "ODEs, series solutions, Bessel and Legendre, Sturm–Liouville"),
    ("som", "Strength of Materials", "AM2200", "#4f7a52", "#335636", "mech stuff/Strength of materials", "Stress, torsion, bending, deflection, buckling, energy methods"),
    ("ph", "Physics I", "PH1010", "#7c8a3a", "#566225", "mech stuff/Physics", "Newton's laws, oscillations, phase space, Lagrangian mechanics, orbits, vector calculus"),
    ("fm", "Fluid Mechanics", "AM2530", "#3f6d99", "#284a6e", "mech stuff/Fluid Mechanics", "Statics, kinematics, control volumes, dimensional analysis, Bernoulli"),
    ("kdoms", "Kinematics & Dynamics of Machinery", "ME2201", "#b8692f", "#84451a", "mech stuff/KDoMs", "Velocity and acceleration, mechanism synthesis, gears"),
    ("ee", "Basic Electrical Engineering", "EE1100", "#b8962f", "#86691a", "Basic Electrical Engineering", "Circuits, phasors, transients, resonance, transformers, machines"),
    ("xd", "Cross-Domain Connections", "", "#a54540", "#752c28", "Cross-Domain Synthesis", "Where the same mathematics appears in different subjects"),
    ("ml", "Computing", "", "#38558a", "#243a63", "CS stuff", "Machine-learning formula sheet, web basics"),
    ("ent", "Entrepreneurship", "", "#a8607e", "#794159", "Entrepreneurship", "Innovation course: slides, auctions and pricing"),
    ("fte", "Foundations of Thermal Engineering", "ME2102 / ME3105", "#3a8579", "#255a52", "mech stuff/Foundations of Thermal Engineering", "Exergy, cycles, refrigeration, combustion, turbomachines"),
    ("ht", "Heat Transfer", "ME3101", "#bd5a35", "#8a3a1d", "mech stuff/Heat transfer", "Conduction, convection, radiation, heat exchangers"),
    ("mat", "Materials and Design", "ME2200", "#6a68a3", "#4a487a", "mech stuff/Materials and design", "Crystal structure, failure theories, fatigue, phase diagrams"),
    ("mfg", "Manufacturing Technology", "ME2302 / ME3305", "#7a7d80", "#55575a", "mech stuff/Manufacturing Technology", "Casting, forming, machining, additive, metrology"),
    ("mic", "Measurements, Instrumentation and Control", "ME2400", "#3f8794", "#2a606a", "mech stuff/Measurements and instrumentation", "Sensors, signal conditioning, feedback control"),
    ("mdes", "Introduction to Machine Design", "ME3203", "#a8814c", "#785a30", "mech stuff/Introduction to Machine Design", "Shafts, bearings, gears, springs, bolts"),
    ("camd", "Computer Aided Machine Drawing", "ME3283", "#6f8294", "#4b5c6b", "mech stuff/Computer Aided Machine Drawing", "Sections, fasteners, assemblies, tolerances"),
    ("cur", "Mechanical Engineering Curriculum", "", "#77716a", "#55504a", "mech stuff/Mechanical Engineering Curriculum - MOC.md", "Semester map"),
]
ACTIVE = ["de", "ph", "som", "fm", "kdoms", "ee", "xd", "ml", "ent"]
UPCOMING = ["fte", "ht", "mat", "mfg", "mic", "mdes", "camd"]
UNIT_NAMES = {"de": {"Intro": "First-order ODEs", "2nd Order DE": "Second-order ODEs", "Series Solutions of DE": "Series solutions",
                     "Special Functions": "Special functions", "PDEs": "Partial differential equations", "Problems": "Assignments"},
              "kdoms": {"Velocity-Acceleration-Bank": "Velocity and acceleration", "Synthesis-Formula-Bank": "Mechanism synthesis", "Formula-Bank": "Gears"},
              "ml": {"ML": "Machine learning", "WebOps": "Web basics"}}
UNIT_ORDER = {"de": ["Intro", "2nd Order DE", "Series Solutions of DE", "Special Functions", "PDEs", "Problems"],
              "kdoms": ["Velocity-Acceleration-Bank", "Synthesis-Formula-Bank", "Formula-Bank"],
              "ee": ["", "AC Transients", "RLC Circuits - Responses", "Transformers and Induction Machines"]}
DEFAULT_UNIT = {"ee": "Weekly lessons", "xd": "Connections", "ent": "Class notes"}

# interactive widgets attached to notes (by note file name without .md)
WIDGETS = {
    "oscillator": ["The Universal Second-Order Linear System", "Series RLC Natural Response - Damping Cases", "Parallel RLC Natural Response - Damping Cases",
                   "Second-Order AC Transients (Series and Parallel RLC)", "DC Step Response of RLC Circuits", "Measurements, Instrumentation and Control - MOC"],
    "decay": ["Exponential Decay - Time Constants, Damping and Spatial Relaxation", "Applications of First Order ODEs", "First-Order AC Transients (RC and RL)",
              "04 Capacitors, Inductors and First Order Circuits"],
    "lumped": ["Heat Transfer - MOC"],
    "mohr": ["Mohr's Circle for Stress", "Plane Stress Transformation", "Eigenvalues, Rotation and Diagonalization Everywhere"],
    "beam": ["Double Integration and Macaulay's Method", "Tutorial 8 - Deflection of Beams", "Moment-Area Method"],
    "euler": ["Euler Buckling of Columns"],
    "series": ["Sturm-Liouville Problems", "Legendre Series and Fourier-Legendre Expansions", "Fourier-Bessel Series", "Inner Product Spaces and Orthogonal Functions"],
    "special": ["Bessel's Equation and Bessel Functions of the First Kind", "Bessel Function Properties and Recurrence Relations", "Bessel Generating Function",
                "Legendre Polynomials and Rodrigues' Formula", "Generating Function of Legendre Polynomials"],
    "resonance": ["Frequency Response and Resonance Curves", "Series vs Parallel RLC - Key Distinctions", "Resonance and Buckling - Instability as an Eigenvalue Problem"],
    "auction": ["Primitives, Markets with Power and Auctions"],
    "freeosc": ["Damped Oscillations"],
    "driven": ["Driven Oscillations and Resonance"],
    "phase": ["The Nonlinear Pendulum"],
    "orbit": ["Kepler's Laws and Orbits"],
    "vfield": ["Divergence Theorem and Flux"],
}
WIDGET_OF = {name: w for w, names in WIDGETS.items() for name in names}
WIDGET_TITLE = {"oscillator": "Damping explorer", "decay": "Time-constant explorer", "lumped": "Lumped-capacitance cooling", "mohr": "Mohr's circle explorer",
                "beam": "Beam deflection explorer", "euler": "Column buckling calculator", "series": "Series approximation explorer",
                "special": "Special-function explorer", "resonance": "Resonance explorer", "auction": "GSP vs VCG auction explorer",
                "freeosc": "Free-oscillation explorer", "driven": "Driven-oscillator explorer", "phase": "Pendulum phase-portrait explorer",
                "orbit": "Orbit explorer", "vfield": "Divergence and curl explorer"}

# --------------------------------------------------------------------------------------------- helpers
def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower().replace("&", " and "))
    return re.sub(r"[\s_-]+", "-", s).strip("-") or "note"


def heading_slug(value, separator="-"):
    """slug for heading ids and #anchors; math/code placeholders are dropped so both sides agree"""
    value = re.sub("[][0-9]+[]", "", value).replace("$", "")
    return md_slugify(value, separator)


def esc(s):
    return H.escape(s, quote=True)


def parse_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    fm = {}
    if not m:
        return fm, text
    key = None
    for line in m.group(1).splitlines():
        if re.match(r"^\s+-\s+", line) and key:
            fm.setdefault(key, []).append(re.sub(r"^\s+-\s+", "", line).strip().strip("\"'"))
            continue
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                fm[key] = [v.strip().strip("\"'") for v in val[1:-1].split(",") if v.strip()]
            elif val == "":
                fm[key] = []
            else:
                fm[key] = val.strip("\"'")
    return fm, text[m.end():]


def course_of(rel):
    for cid, _, _, _, _, root, _ in COURSES:
        if rel == root or rel.startswith(root + "/"):
            return cid
    return "ml" if rel.startswith("CS stuff") else None


def excluded(rel):
    return any(rel == p or rel.startswith(p + "/") for p in EXCL_PREFIX)


# --------------------------------------------------------------------------------------------- scan the vault
class Note:
    pass


def scan():
    notes, files = [], {}
    for root, dirs, fs in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in EXCL_DIRS]
        rel_root = Path(root).relative_to(VAULT).as_posix()
        rel_root = "" if rel_root == "." else rel_root
        for f in fs:
            rel = f"{rel_root}/{f}" if rel_root else f
            if excluded(rel):
                continue
            ext = Path(f).suffix.lower()
            if ext in (".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".html"):
                files.setdefault(f, []).append(rel)
            if ext != ".md" or f in EXCL_FILES or f.startswith("Untitled"):
                continue
            cid = course_of(rel)
            if cid is None:
                continue
            n = Note()
            n.rel, n.cid, n.base = rel, cid, f[:-3]
            raw = (VAULT / rel).read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
            n.fm, n.body = parse_frontmatter(raw)
            h1 = re.search(r"^#\s+(.+)$", n.body, re.M)
            n.h1 = re.sub(r"[*`_]", "", h1.group(1)).strip() if h1 else n.fm.get("title", n.base)
            n.h1 = n.h1.replace(" --- ", " — ")
            n.title = n.h1 if "_" in n.base else n.base   # file names written with underscores are not display titles
            if n.base == "Course Details":
                n.title = next(c[1] for c in COURSES if c[0] == cid) + " — syllabus"
            tags = n.fm.get("tags", [])
            n.tags = [t for t in (tags if isinstance(tags, list) else [tags]) if t and t.lower() not in ("moc", "course")]
            n.slug = slugify(n.base)
            notes.append(n)
    # unique slugs
    seen = {}
    for n in notes:
        if n.slug in seen:
            parent = slugify(Path(n.rel).parent.name)
            n.slug = f"{parent}-{n.slug}"
            seen[n.slug] = n
        else:
            seen[n.slug] = n
    return notes, files


def classify(n):
    title, parts = n.base, Path(n.rel).parts
    if n.base == "Course Details" or n.base == "Mechanical Engineering Curriculum - MOC":
        return "ref"
    if title.endswith("- MOC") or title.endswith(" MOC"):
        return "moc"
    if any(p.startswith("Tutorial") for p in parts[:-1]) or re.search(r"\bQ\d|^A-Q|^B-Q|Tutorial|Assignment|Solved Problems|solution|Problem-", title):
        return "problem"
    return "concept"


# --------------------------------------------------------------------------------------------- rendering
MATH, STASH = [], []
MATH_INDEX = {}


def stash(htmlfrag):
    STASH.append(htmlfrag)
    return f"\ue002{len(STASH) - 1}\ue003"


def katex_safe(tex):
    """Rewrite constructs KaTeX does not implement into ones it does."""
    tex = re.sub(r"\\begin\{psmallmatrix\}(.*?)\\end\{psmallmatrix\}", lambda m: r"\left(\begin{smallmatrix}" + m.group(1) + r"\end{smallmatrix}\right)", tex, flags=re.S)
    return tex


def math_token(tex, display):
    key = (katex_safe(tex.strip()), display)
    if key not in MATH_INDEX:
        MATH_INDEX[key] = len(MATH)
        MATH.append({"tex": key[0], "display": display})
    return f"\ue000{MATH_INDEX[key]}\ue001"


class Resolver:
    def __init__(self, notes, files):
        self.by_base = {}
        for n in notes:
            self.by_base.setdefault(n.base.lower(), []).append(n)
        self.files = files
        self.used_imgs = set()
        self.used_sims = set()

    def note(self, target):
        t = target.strip()
        t = re.sub(r"\.md$", "", t)
        base = t.split("/")[-1].lower()
        hits = self.by_base.get(base, [])
        if len(hits) > 1 and "/" in t:
            hits = [h for h in hits if h.rel.lower().endswith(t.lower() + ".md")] or hits
        return hits[0] if hits else None

    def file(self, target):
        name = target.strip().split("/")[-1]
        hits = self.files.get(name)
        return hits[0] if hits else None


def render_note(n, R, depth):
    """Markdown -> HTML (with stash/math placeholders).  depth = path prefix from the page to the wiki root."""
    text = n.body
    text = re.sub(r"^#\s+.+\n", "", text, count=1, flags=re.M)
    text = strip_sections(text)
    # 1. code
    text = re.sub(r"```mermaid\n(.*?)```", lambda m: "\n\n" + stash(f'<pre class="mermaid">{esc(m.group(1).strip())}</pre>') + "\n\n", text, flags=re.S)
    text = re.sub(r"```[^\n]*\n(.*?)```", lambda m: "\n\n" + stash(f"<pre><code>{esc(m.group(1).rstrip())}</code></pre>") + "\n\n", text, flags=re.S)
    text = re.sub(r"`([^`\n]+)`", lambda m: stash(f"<code>{esc(m.group(1))}</code>"), text)
    # 2. math
    def disp(m):
        tex = re.sub(r"^\s*>\s?", "", m.group(1), flags=re.M)
        return "\n\n" + math_token(tex, True) + "\n\n"
    text = re.sub(r"\$\$(.+?)\$\$", disp, text, flags=re.S)
    out = []
    for line in text.split("\n"):
        is_row = line.lstrip().lstrip(">").lstrip().startswith("|")
        def inl(m):
            tex = m.group(1)
            if is_row:
                tex = tex.replace("\\|", "|")
            return math_token(tex, False)
        out.append(re.sub(r"(?<![\\$\w])\$(?!\s|\$)([^$\n]+?)(?<![\s\\])\$(?!\d)", inl, line))
    text = "\n".join(out)
    # 3. embeds and links
    def embed(m):
        target = m.group(1).strip()
        ext = Path(target).suffix.lower()
        if ext in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"):
            rel = R.file(target)
            if not rel:
                return ""
            R.used_imgs.add(rel)
            return f'<img src="{depth}assets/img/{urllib.parse.quote(Path(rel).name)}" alt="{esc(Path(target).stem)}" loading="lazy">'
        nt = R.note(target)
        return f'<a href="{depth}n/{nt.slug}.html">{esc(nt.title)}</a>' if nt else ""
    text = re.sub(r"!\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]", embed, text)

    def link(m):
        target, anchor, alias = m.group(1).strip(), (m.group(2) or "").lstrip("#"), m.group(3)
        label = (alias if alias is not None else None)
        if not target:
            return f'<a href="#{heading_slug(anchor, "-")}">{esc(label or anchor)}</a>'
        if target == "Home":
            return f'<a href="{depth}index.html">{esc(label or "Home")}</a>'
        ext = Path(target).suffix.lower()
        if ext in (".pdf", ".png", ".jpg"):
            rel = R.file(target)
            text_label = label or Path(target).stem
            return f'<span class="ghost" title="kept in the vault, not published on the site">{esc(text_label)}</span>'
        nt = R.note(target)
        if not nt:
            return f'<span class="ghost">{esc(label or Path(target).name)}</span>'
        href = f"{depth}n/{nt.slug}.html" + (f"#{heading_slug(anchor, '-')}" if anchor else "")
        n.links.add(nt.slug)
        return f'<a href="{href}">{esc(label if label else nt.title)}</a>'
    text = re.sub(r"\[\[([^\]|#]*?)(#[^\]|]*)?(?:\\?\|([^\]]*))?\]\]", link, text)

    # standard markdown images and links to vault files: ![alt](img.png), [text](gear-explorer.html), [text](Note.md)
    def md_image(m):
        alt, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|data:)", url):
            return f'<img src="{esc(url)}" alt="{esc(alt)}" loading="lazy">'
        rel = R.file(urllib.parse.unquote(url))
        if not rel:
            return ""
        R.used_imgs.add(rel)
        return f'<img src="{depth}assets/img/{urllib.parse.quote(Path(rel).name)}" alt="{esc(alt)}" loading="lazy">'
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", md_image, text)

    def md_link(m):
        label, url = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#)", url):
            return m.group(0)
        u = urllib.parse.unquote(url.split("#")[0])
        if u.endswith(".md"):
            nt = R.note(u)
            if nt:
                n.links.add(nt.slug)
                return f'<a href="{depth}n/{nt.slug}.html">{label}</a>'
            return label
        rel = R.file(u)
        if not rel:
            return label
        if rel.endswith(".html"):
            R.used_sims.add(rel)
            return f'<a class="file" href="{depth}assets/sims/{urllib.parse.quote(Path(rel).name)}" target="_blank" rel="noopener">{label}</a>'
        return f'<span class="ghost" title="kept in the vault, not published on the site">{label}</span>'
    text = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", md_link, text)
    # 4. interactive problem structures, then callouts
    kind = n.kind
    if kind == "problem":
        text = wrap_problems(text)
    text = convert_callouts(text)
    text = fix_lists(text)
    # 5. markdown
    md = markdown.Markdown(extensions=["tables", "md_in_html", "toc", "sane_lists", "footnotes"], extension_configs={"toc": {"anchorlink": False, "slugify": heading_slug}})
    body = md.convert(text)
    n.toc = [(t["level"], t["id"], H.unescape(re.sub(r"<[^>]+>", "", re.sub(r"(\d+)", lambda x: STASH[int(x.group(1))], t["name"])))) for t in md.toc_tokens]
    n.ids = set(re.findall(r'<h[1-6] id="([^"]+)"', body))
    # 6. restore stash
    for _ in range(2):
        body = re.sub(r"\ue002(\d+)\ue003", lambda m: STASH[int(m.group(1))], body)
    body = re.sub(r"<p>(<pre.*?</pre>)</p>", r"\1", body, flags=re.S)
    # 7. task lists
    cnt = [0]
    def task(m):
        cnt[0] += 1
        checked = m.group(1).lower() == "x"
        return f'<li class="task"><label><input type="checkbox" data-task="{n.slug}:{cnt[0]}"{" checked" if checked else ""}> <span>'
    body = re.sub(r"<li>\[( |x|X)\]\s*", task, body)
    body = re.sub(r"(<li class=\"task\">.*?)</li>", lambda m: m.group(1) + "</span></label></li>", body, flags=re.S)
    return body


def fix_lists(text):
    """Obsidian lets a list start straight after a paragraph line; python-markdown needs a blank line first."""
    out, in_list = [], False
    for ln in text.split("\n"):
        if not ln.strip():
            in_list = False
        else:
            m = re.match(r"^(\s{0,3})([-*+]|(\d+)[.)])\s+\S", ln)
            if m and not in_list:
                interrupts = not m.group(3) or m.group(3) == "1"
                prev = out[-1] if out else ""
                if interrupts and prev.strip() and not prev.lstrip().startswith(("<", "|", "#", ">")) and not re.match(r"^\s*([-*_]\s*){3,}$", prev):
                    out.append("")
            if m:
                in_list = True
        out.append(ln)
    return "\n".join(out)


def strip_sections(text):
    lines, out, skip = text.split("\n"), [], False
    for ln in lines:
        m = re.match(r"^##\s+(.*)$", ln)
        if m:
            skip = bool(STRIP_SECTIONS.match(m.group(1).strip()))
        if not skip:
            out.append(ln)
    return "\n".join(out)


def convert_callouts(text):
    """Obsidian callouts. `> [!kind]- Title` folds closed, `> [!kind]+ Title` folds open; both become <details> on the site."""
    lines, out, i = text.split("\n"), [], 0
    while i < len(lines):
        m = re.match(r"^>\s*\[!(\w+)\]([+-]?)\s*(.*)$", lines[i])
        if not m:
            out.append(lines[i]); i += 1; continue
        kind, fold, title = m.group(1).lower(), m.group(2), m.group(3).strip()
        body = []
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            body.append(re.sub(r"^>\s?", "", lines[i])); i += 1
        title_html = re.sub(r"\*(.+?)\*", r"<i>\1</i>", re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", title)) or kind.capitalize()
        if fold:
            out += ["", f'<details class="callout callout-{kind} fold"{" open" if fold == "+" else ""} markdown="1">', f'<summary markdown="0">{title_html}</summary>', ""] + body + ["", "</details>", ""]
        else:
            out += ["", f'<div class="callout callout-{kind}" markdown="1">', f'<div class="callout-title" markdown="0">{title_html}</div>', ""] + body + ["", "</div>", ""]
    return "\n".join(out)


REVEAL = {"principle and why it applies": ("hint", "Hint: which principle?"), "solution": ("sol", "Show solution"), "result": ("res", "Show result"),
          "check": ("chk", "Check your answer"), "trap": ("trap", "Common trap")}


def wrap_problems(text):
    """Hide principle/solution/result behind reveal buttons (tutorial sheets) or solutions behind a button (assignment sheets)."""
    lines = text.split("\n")
    if any(re.match(r"^###\s+Problem\s*$", l) for l in lines):
        out, i = [], 0
        while i < len(lines):
            m = re.match(r"^###\s+(.+?)\s*$", lines[i])
            if m and m.group(1).lower() in REVEAL:
                k, label = REVEAL[m.group(1).lower()]
                out += ["", f'<details class="rv rv-{k}" markdown="1">', f"<summary>{label}</summary>", ""]
                i += 1
                while i < len(lines) and not re.match(r"^#{1,3}\s", lines[i]):
                    out.append(lines[i]); i += 1
                out += ["", "</details>", ""]
                continue
            out.append(lines[i]); i += 1
        return "\n".join(out)
    # assignment style: "## Q1 ..." sections with a [!question] callout first
    out, i = [], 0
    while i < len(lines):
        out.append(lines[i])
        if re.match(r"^##\s+(Q\d+|Problem\s+\d+|Question\s+\d+)\b", lines[i]):
            i += 1
            while i < len(lines) and lines[i].strip() == "":
                out.append(lines[i]); i += 1
            if i < len(lines) and lines[i].startswith("> [!question]"):
                while i < len(lines) and lines[i].startswith(">"):
                    out.append(lines[i]); i += 1
                out += ["", '<details class="rv rv-sol" markdown="1">', "<summary>Show solution</summary>", ""]
                while i < len(lines) and not re.match(r"^##\s", lines[i]):
                    out.append(lines[i]); i += 1
                out += ["", "</details>", ""]
            continue
        i += 1
    return "\n".join(out)


def wrap_steps(body, n):
    parts = re.split(r'(?=<h2 id=")', body)
    secs = []
    for idx, p in enumerate(parts):
        if not p.strip():
            continue
        m = re.match(r'<h2 id="([^"]+)">(.*?)</h2>', p, re.S)
        if idx == 0 or not m:
            secs.append(f'<section class="step intro">{p}</section>')
        else:
            title = re.sub(r"<[^>]+>", "", m.group(2))
            prob = n.kind == "problem" and re.search(r"(Q\d|Problem \d)", title)
            cls = "step prob" if prob else "step"
            extra = f' data-q="{n.slug}#{m.group(1)}"' if prob else ""
            secs.append(f'<section class="{cls}" data-title="{esc(title)}"{extra}>{p}</section>')
    return "".join(secs)


def plain_text(body):
    t = re.sub(r"\ue000\d+\ue001", " ", body)
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", H.unescape(t)).strip()


# --------------------------------------------------------------------------------------------- math via node
def render_math(start=0):
    if len(MATH) <= start:
        return []
    tmp_in, tmp_out = HERE / "_math_in.json", HERE / "_math_out.json"
    tmp_in.write_text(json.dumps(MATH[start:]), encoding="utf-8")
    subprocess.run(["node", str(HERE / "render_math.js"), str(tmp_in), str(tmp_out)], check=True, cwd=HERE, stderr=subprocess.DEVNULL)
    out = json.loads(tmp_out.read_text(encoding="utf-8"))
    tmp_in.unlink(); tmp_out.unlink()
    return out


def finalize(html_text, math_html):
    return re.sub(r"\ue000(\d+)\ue001", lambda m: math_html[int(m.group(1))], html_text)


# --------------------------------------------------------------------------------------------- page shell
ICON = {
    "learn": '<svg viewBox="0 0 24 24"><path d="M12 3 2 8l10 5 8-4v6h2V8L12 3Zm-6 9.6V16c0 1.7 2.7 3 6 3s6-1.3 6-3v-3.4l-6 3-6-3Z"/></svg>',
    "practice": '<svg viewBox="0 0 24 24"><path d="M7 4h2v16H7V4Zm8 0h2v16h-2V4ZM3 9h2v6H3V9Zm16 0h2v6h-2V9ZM9 11h6v2H9v-2Z"/></svg>',
    "solve": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm3.8 6.2-2.1 5.5-5.5 2.1 2.1-5.5 5.5-2.1ZM12 11a1 1 0 1 0 0 2 1 1 0 0 0 0-2Z"/></svg>',
    "graph": '<svg viewBox="0 0 24 24"><path d="M6 3a3 3 0 0 0-1 5.8v6.4a3 3 0 1 0 2 0V13l6-2.2A3 3 0 1 0 12.4 9 3 3 0 0 0 9 11.3L7 12V8.8A3 3 0 0 0 6 3Zm0 2a1 1 0 1 1 0 2 1 1 0 0 1 0-2Zm12 2a1 1 0 1 1 0 2 1 1 0 0 1 0-2ZM6 17a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z"/></svg>',
    "search": '<svg viewBox="0 0 24 24"><path d="M10 3a7 7 0 1 0 4.4 12.4l4.6 4.6 1.4-1.4-4.6-4.6A7 7 0 0 0 10 3Zm0 2a5 5 0 1 1 0 10 5 5 0 0 1 0-10Z"/></svg>',
}
ICON["menu"] = '<svg class="i" viewBox="0 0 24 24"><path d="M4 6h16v2H4V6Zm0 5h16v2H4v-2Zm0 5h16v2H4v-2Z"/></svg>'
ICON["sun"] = '<svg class="i" viewBox="0 0 24 24"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm0-5h-1v3h2V2h-1Zm0 17h-1v3h2v-3h-1ZM2 11v2h3v-2H2Zm17 0v2h3v-2h-3ZM5.6 4.2 4.2 5.6l2.1 2.1 1.4-1.4-2.1-2.1Zm12.1 12.1-1.4 1.4 2.1 2.1 1.4-1.4-2.1-2.1ZM4.2 18.4l1.4 1.4 2.1-2.1-1.4-1.4-2.1 2.1ZM16.3 6.3l1.4 1.4 2.1-2.1-1.4-1.4-2.1 2.1Z"/></svg>'
NAV = [("learn", "Library", "index.html"), ("practice", "Practice", "practice.html"), ("solve", "How to solve", "solve.html"), ("graph", "Link map", "graph.html")]


def shell(title, body, root, page, slug="", course="", scripts=(), katex=False, mermaid=False, crumbs=(), wide=False):
    tabs = "".join(f'<a class="tab{" on" if page == k else ""}" href="{root}{href}">{label}</a>' for k, label, href in NAV)
    dock = "".join(f'<a class="{"on" if page == k else ""}" href="{root}{href}">{ICON[k]}<span>{label if k != "solve" else "Solve"}</span></a>' for k, label, href in NAV)
    dock += f'<button id="openSearchDock" type="button" aria-label="Search">{ICON["search"]}<span>Search</span></button>'
    kcss = f'<link rel="stylesheet" href="{root}assets/vendor/katex.min.css">' if katex else ""
    extra = "".join(f'<script src="{root}assets/{s}"></script>' for s in scripts)
    mer = f'<script src="{root}assets/vendor/mermaid.min.js"></script>' if mermaid else ""
    cb = ""
    if crumbs:
        parts = [f'<a href="{root}{h}">{esc(t)}</a>' if h else f"<span>{esc(t)}</span>" for t, h in crumbs]
        cb = '<nav class="crumbbar" aria-label="Breadcrumb">' + "<i>›</i>".join(parts) + "</nav>"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#4a2f20"><meta name="description" content="Course notes, worked problems and interactive explorers, bound as a notebook"><link rel="icon" href="{root}assets/Favicons/Alya.png" type="image/png"><link rel="apple-touch-icon" href="{root}assets/Favicons/Alya.png"><link rel="manifest" href="{root}manifest.webmanifest">
<title>{esc(title)} · Engineering Notebook</title>
<script>try{{var t=localStorage.getItem('wiki.theme');if(!t&&matchMedia('(prefers-color-scheme: dark)').matches)t='dark';if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<link rel="stylesheet" href="{root}assets/style.css">{kcss}
</head><body data-root="{root}" data-page="{page}" data-slug="{slug}" data-course="{course}">
<header class="top"><button class="key key-menu" id="menuBtn" type="button" aria-label="Open contents" aria-expanded="false">{ICON["menu"]}</button>
<a class="plate" href="{root}index.html"><span class="plate-mark">EN</span><span class="plate-t">Engineering Notebook</span></a>
<nav class="tabs" aria-label="Sections">{tabs}</nav>
<div class="top-r"><button class="search-key" id="openSearch" type="button" aria-label="Search the notebook">{ICON["search"]}<span>Search the notebook</span><kbd>/</kbd></button><button class="key" id="themeBtn" type="button" aria-label="Switch between day and night desk"></button></div></header>
<div class="thread" id="thread"></div>
<div class="frame"><aside class="tree" id="tree" aria-label="Contents"></aside>
<main class="content">{cb}<div class="paper{" wide" if wide else ""}">{body}</div></main></div>
<div class="scrim" id="scrim"></div>
<nav class="dock" aria-label="Sections">{dock}</nav>
<button class="key totop" id="toTop" type="button" aria-label="Back to top">↑</button>
<div class="search" id="search" hidden><div class="search-box"><div class="search-h"><span>Find in the notebook</span><button id="closeSearch" type="button" aria-label="Close search">×</button></div><input id="q" type="search" placeholder="Title, heading or any word…" autocomplete="off"><div id="results"></div></div></div>
<script src="{root}assets/data.js"></script>{mer}
<script src="{root}assets/app.js"></script>{extra}
</body></html>"""


# --------------------------------------------------------------------------------------------- main build
def main():
    (HERE / "math_errors.txt").unlink(missing_ok=True)
    notes, files = scan()
    for n in notes:
        n.kind = classify(n)
        n.links = set()
    R = Resolver(notes, files)
    by_slug = {n.slug: n for n in notes}
    cmap = {c[0]: c for c in COURSES}

    # course structure: units and lesson order from the course MOC
    order, local_order = {}, {}
    for n in notes:
        if n.kind == "moc" and n.base != "Mechanical Engineering Curriculum - MOC":
            for i, m in enumerate(re.finditer(r"\[\[([^\]|#]+)", n.body)):
                name = m.group(1).strip().split("/")[-1].lower()
                order.setdefault((n.cid, name), i)
                local_order.setdefault((posixpath.dirname(n.rel), name), i)   # a unit's own sub-map beats the course map
    for n in notes:
        root = cmap[n.cid][5]
        sub = Path(n.rel).relative_to(root).parts[:-1] if n.rel.startswith(root + "/") else ()
        raw = sub[0] if sub else ""
        raw = re.sub(r"^\d+\s*[-–.]\s*|^\d+\s+", "", raw)
        n.unit = UNIT_NAMES.get(n.cid, {}).get(raw, raw) or ("Overview" if n.kind == "moc" else DEFAULT_UNIT.get(n.cid, "Lessons"))
        n.unit_key = sub[0] if sub else ""
        n.ord = order.get((n.cid, n.base.lower()), 9999)
        n.lord = local_order.get((posixpath.dirname(n.rel), n.base.lower()), 9999)
    # a course with no concept lesson uses its map as the single lesson
    for cid in {n.cid for n in notes}:
        cn = [n for n in notes if n.cid == cid]
        if not any(n.kind == "concept" for n in cn):
            for n in cn:
                if n.kind == "moc":
                    n.kind = "concept"; n.unit = "Overview"

    # render every note
    for n in notes:
        n.html = render_note(n, R, "../")
    math_html = render_math()
    ids_of = {n.slug: n.ids for n in notes}

    def fix_anchor(slug, anchor):
        ids = ids_of.get(slug, set())
        if anchor in ids:
            return anchor
        near = sorted((i for i in ids if i.startswith(anchor) or anchor.startswith(i) or anchor in i), key=len)
        return near[0] if near else None
    for n in notes:
        def other(m):
            a = fix_anchor(m.group(1), m.group(2))
            return f'href="../n/{m.group(1)}.html' + (f"#{a}" if a else "") + '"'
        n.html = re.sub(r'href="\.\./n/([a-z0-9-]+)\.html#([^"]+)"', other, n.html)
        def same(m):
            a = fix_anchor(n.slug, m.group(1))
            return f'href="#{a}"' if a else 'href="#"'
        n.html = re.sub(r'href="#([^"]+)"', same, n.html)
        n.html = re.sub(r'<a href="#">(.*?)</a>', r'<span class="ghost"></span>', n.html, flags=re.S)

    # backlinks
    back = {n.slug: set() for n in notes}
    for n in notes:
        for t in n.links:
            if t in back and t != n.slug:
                back[t].add(n.slug)

    # ---------------------------------------------------------------- course paths
    courses_out = []
    for cid, title, code, color, dark, root, blurb in COURSES:
        cn = [n for n in notes if n.cid == cid]
        if not cn:
            continue
        units = {}
        for n in sorted(cn, key=lambda x: (x.unit_key, x.lord, x.ord, x.title)):
            if n.kind == "concept":
                units.setdefault((n.unit_key, n.unit), []).append(n)
        ulist = sorted(units.items(), key=lambda kv: (min(x.ord for x in kv[1]) if any(x.ord < 9999 for x in kv[1]) else 9999, kv[0][0]))
        # numbered folders keep their natural order
        if any(re.match(r"^\d", k[0][0]) for k in ulist):
            ulist = sorted(ulist, key=lambda kv: kv[0][0])
        if cid in UNIT_ORDER:
            fixed = UNIT_ORDER[cid]
            ulist = sorted(ulist, key=lambda kv: fixed.index(kv[0][0]) if kv[0][0] in fixed else len(fixed))
        syllabus = []
        if cid in UPCOMING:
            m0 = next((n for n in cn if n.kind in ("moc", "concept")), None)
            sm = re.search(r"##\s*Syllabus Map\s*\n(.*?)(?=\n##\s|\Z)", m0.body, re.S) if m0 else None
            if sm:
                syllabus = [re.sub(r"[:.]$", "", t).strip() for t in re.findall(r"^\s*\d+\.\s+\*\*(.+?)\*\*", sm.group(1), re.M)]
        moc = next((n for n in cn if n.kind == "moc"), None)
        courses_out.append(dict(id=cid, title=title, code=code, color=color, dark=dark, blurb=blurb, moc=moc.slug if moc else None,
                                units=[dict(name=u[1], lessons=[x.slug for x in ls]) for u, ls in ulist],
                                problems=[n.slug for n in sorted(cn, key=lambda x: x.title) if n.kind == "problem"],
                                upcoming=cid in UPCOMING, syllabus=syllabus))
    cobj = {c["id"]: c for c in courses_out}
    path_of = {}
    for c in courses_out:
        seq = [s for u in c["units"] for s in u["lessons"]]
        for i, s in enumerate(seq):
            path_of[s] = (c["id"], i, seq)

    # ---------------------------------------------------------------- note pages
    NOTEDIR = WIKI / "n"
    for d in (NOTEDIR, WIKI / "course", ASSETS / "img"):
        if d.exists() and d.name != "img":
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)
    search = []
    for n in notes:
        c = cobj.get(n.cid)
        color = cmap[n.cid][3]
        body = n.html
        wk = WIDGET_OF.get(n.base)
        if wk:
            marker = f'<div class="widget-wrap"><h3 class="widget-h">{WIDGET_TITLE[wk]}</h3><div class="widget" data-widget="{wk}"></div></div>'
            m = re.search(r'<h2 id="', body)
            body = (body[:m.start()] + marker + body[m.start():]) if m else body + marker
        steps = wrap_steps(body, n)
        nsteps = steps.count('class="step')
        lesson = n.kind == "concept" and n.base not in ("Course Details",) and nsteps >= 2
        has_math = "\ue000" in n.html
        mer = 'class="mermaid"' in n.html
        # header chips
        chips = "".join(f'<span class="chip">{esc(t)}</span>' for t in n.tags[:5])
        crumb_list = [("Library", "index.html"), (cmap[n.cid][1], f"course/{n.cid}.html")] + ([(n.unit, None)] if n.unit and n.unit not in ("Lessons", "Overview") else [])
        actions = ""
        if lesson:
            actions += '<button class="btn" id="startLesson" type="button">Study mode</button>'
        actions += '<button class="btn btn-ghost" id="markDone" type="button">Mark as read</button>' if n.kind in ("concept", "moc") else ""
        # pager
        pager = ""
        if n.slug in path_of:
            cid, i, seq = path_of[n.slug]
            prv = f'<a class="pg" href="{seq[i-1]}.html"><small>Previous page</small>{esc(by_slug[seq[i-1]].title)}</a>' if i > 0 else "<span></span>"
            nxt = f'<a class="pg pg-next" href="{seq[i+1]}.html"><small>Next page</small>{esc(by_slug[seq[i+1]].title)}</a>' if i + 1 < len(seq) else "<span></span>"
            pager = f'<nav class="pager">{prv}{nxt}</nav>'
        # related
        outs = sorted((s for s in n.links if s in by_slug and s != n.slug), key=lambda s: by_slug[s].title)
        ins = sorted((s for s in back[n.slug] if s not in n.links), key=lambda s: by_slug[s].title)
        def card(s):
            t = by_slug[s]
            return f'<a class="rel" href="{s}.html" style="--c:{cmap[t.cid][3]}"><span class="dot"></span><span>{esc(t.title)}<small>{esc(cmap[t.cid][1])}</small></span></a>'
        related = ""
        if outs:
            related += f'<h3>Links to</h3><div class="rels">{"".join(card(s) for s in outs[:18])}</div>'
        if ins:
            related += f'<h3>Linked from</h3><div class="rels">{"".join(card(s) for s in ins[:18])}</div>'
        related = f'<section class="related"><h2>Related notes</h2>{related}<canvas id="miniGraph" width="640" height="320" aria-label="Connections"></canvas></section>' if (outs or ins) else ""
        toc = [(lv, i, t) for lv, i, t in n.toc if lv == 2]
        tochtml = ""
        if len(toc) >= 3:
            tochtml = '<aside class="toc"><b>On this page</b>' + "".join(f'<a href="#{i}">{esc(t)}</a>' for lv, i, t in toc[:14]) + "</aside>"
        problem_hint = ""
        if n.kind == "problem" and 'class="step prob"' in steps:
            problem_hint = ('<div class="howto"><b>How to attack a problem</b><ol><li>Say what is asked and what is given.</li><li>Pick the principle <em>before</em> calculating (open the hint).</li>'
                            '<li>Solve symbolically, then plug in numbers.</li><li>Check units and a limiting case.</li><li>Be honest: mark it solved only if you could redo it.</li></ol></div>')
        done_bar = ""
        page = f"""<article class="note" data-kind="{n.kind}" style="--c:{color};--cd:{cmap[n.cid][4]}">
<h1>{esc(n.h1 if n.h1 else n.title)}</h1><div class="chips">{chips}</div>
<div class="actions">{actions}</div>{problem_hint}
<div class="body" id="body">{steps}</div>{done_bar}{pager}{related}</article>{tochtml}"""
        page = finalize(page, math_html)
        text = plain_text(n.html)
        search.append(dict(s=n.slug, t=n.title, c=n.cid, h=[t for lv, i, t in n.toc][:20], x=text[:6000]))
        out = shell(n.title, page, "../", "note", slug=n.slug, course=n.cid, scripts=(["widgets.js"] if wk else []), katex=has_math, mermaid=mer, crumbs=crumb_list)
        (NOTEDIR / f"{n.slug}.html").write_text(out, encoding="utf-8")
        n.nsteps, n.nprob = nsteps, steps.count('class="step prob"')
        n.qs = re.findall(r'<section class="step prob" data-title="([^"]*)" data-q="[^#"]+#([^"]+)"', steps)

    def qcount(p):
        return f"{p.nprob} question{'s' if p.nprob != 1 else ''}" if p.nprob else "worked solution"

    # ---------------------------------------------------------------- course pages
    for c in courses_out:
        cm = cmap[c["id"]]
        unit_html = []
        k = 0
        for ui, u in enumerate(c["units"]):
            rows = []
            for li, sl in enumerate(u["lessons"]):
                k += 1
                ttl = "Course overview" if u["name"] == "Overview" else by_slug[sl].title
                rows.append(f'<li><a class="node" data-slug="{sl}" href="../n/{sl}.html"><span class="no">{k:02d}</span><span class="lbl">{esc(ttl)}</span><i class="lead"></i><span class="mark"></span></a></li>')
            guide = f'<a class="unit-guide" href="../n/{c["moc"]}.html">Course map</a>' if c["moc"] and c["moc"] not in u["lessons"] else ""
            unit_html.append(f'<section class="unit"><div class="unit-h"><span class="tape">Chapter {ui + 1}</span><h2>{esc(u["name"])}</h2>{guide}</div><ol class="toc-list">{"".join(rows)}</ol></section>')
        if c["syllabus"]:
            soon = "".join(f'<li><span class="node locked"><span class="no">{i + 1:02d}</span><span class="lbl">{esc(t)}</span><i class="lead"></i><span class="mark"></span></span></li>' for i, t in enumerate(c["syllabus"]))
            unit_html.append(f'<section class="unit"><div class="unit-h"><span class="tape">Planned</span><h2>Syllabus topics</h2></div><ol class="toc-list">{soon}</ol></section>')
        probs = ""
        if c["problems"]:
            probs = '<section class="unit-more"><div class="unit-h"><span class="tape">Problems</span><h2>Practice sets</h2></div><div class="pgrid">' + "".join(
                f'<a class="pcard" data-slug="{sl}" href="../n/{sl}.html" style="--c:{c["color"]}"><span class="dot"></span><span>{esc(by_slug[sl].title)}<small>{qcount(by_slug[sl])}</small></span></a>'
                for sl in c["problems"]) + "</div></section>"
        head = (f'<div class="cover" style="--c:{c["color"]};--cd:{c["dark"]}"><div><small>{esc(c["code"]) or "COURSE"}</small><h1>{esc(c["title"])}</h1><p>{esc(c["blurb"])}</p></div>'
                f'<div class="stat" data-course="{c["id"]}"><b>0%</b>read</div></div>')
        body = head + ('<p class="upnote">Upcoming course: this is a syllabus-based map; chapters will appear as notes are written.</p>' if c["upcoming"] else "") + "".join(unit_html) + probs
        (WIKI / "course" / f'{c["id"]}.html').write_text(shell(c["title"], body, "../", "course", course=c["id"], crumbs=[("Library", "index.html"), (c["title"], None)]), encoding="utf-8")

    # ---------------------------------------------------------------- home
    def book(cid):
        c = cobj.get(cid)
        if not c:
            return ""
        nl = sum(len(u["lessons"]) for u in c["units"])
        sub = "syllabus map only" if c["upcoming"] else f"{nl} page" + ("s" if nl != 1 else "")
        bar = "" if c["upcoming"] else '<span class="bar"><i></i></span>'
        return (f'<a class="book{" soon" if c["upcoming"] else ""}" data-course="{cid}" href="course/{cid}.html" style="--c:{c["color"]};--cd:{c["dark"]}">'
                f'<span class="book-code">{esc(c["code"]) or "Notes"}</span><span class="book-t">{esc(c["title"])}</span><span class="book-n">{sub}</span>{bar}</a>')
    sims = []
    for rels in files.values():
        for rel in rels:
            if rel.endswith(".html"):
                t = (VAULT / rel).read_text(encoding="utf-8", errors="replace")
                tm = re.search(r"<title>(.*?)</title>", t, re.S)
                title = (tm.group(1).strip() if tm else Path(rel).stem.replace("-", " ").replace("_", " ")).strip()
                sims.append((title, Path(rel).name))
    sims.sort()
    sims_html = ('<h2 class="sec"><span class="tape">Workshop</span>Stand-alone simulations</h2><p class="lead">Interactive explorers from the notes; each opens in a new tab.</p><div class="plates">'
                 + "".join(f'<a class="plate-card" href="assets/sims/{urllib.parse.quote(f)}" target="_blank" rel="noopener"><span>{esc(t)}</span><small>interactive</small></a>' for t, f in sims) + "</div>") if sims else ""
    home = f"""<section class="hero"><div><h1>Engineering Notebook</h1><p>Course notes, worked problems and interactive explorers, bound in one place. Take a book from the shelf, or search for any topic.</p>
<div class="recent-h" id="recentH" hidden>Recently opened</div><div class="recent" id="recent"></div></div>
<div class="ribbon" id="continue"></div></section>
<h2 class="sec"><span class="tape">Shelf</span>Your courses</h2><div class="bookcase"><div class="shelf">{"".join(book(c) for c in ACTIVE)}</div></div>
<h2 class="sec"><span class="tape">Coming up</span>Planned courses</h2><div class="bookcase"><div class="shelf">{"".join(book(c) for c in UPCOMING)}</div></div>
{sims_html}
<p class="foot"><a href="n/{next((n.slug for n in notes if n.base == 'Mechanical Engineering Curriculum - MOC'), '')}.html">Curriculum map</a> · {len(notes)} notes · progress is saved in this browser only</p>"""
    (WIKI / "index.html").write_text(shell("Library", home, "", "learn"), encoding="utf-8")

    # ---------------------------------------------------------------- practice page
    plist = []
    for c in courses_out:
        for s in c["problems"]:
            plist.append((c, by_slug[s]))
    def pcard(c, p):
        def qlabel(t, k):
            m = re.search(r"([A-Z]-)?Q\d+[*′']?(?:\s*[–-]\s*Q?\d+)?|Problem \d+", H.unescape(t))
            return m.group(0) if m else f"Part {k}"
        qs = "".join(f'<a href="n/{p.slug}.html#{i}" data-q="{p.slug}#{i}">{esc(qlabel(t, k))}</a>' for k, (t, i) in enumerate(p.qs, 1))
        return (f'<div class="pcard pcard-q" data-slug="{p.slug}" data-course="{c["id"]}" style="--c:{c["color"]}"><span class="dot"></span>'
                f'<div class="pbody"><a class="pt" href="n/{p.slug}.html">{esc(p.title)}</a><small>{qcount(p)}</small>{f"<div class=qs>{qs}</div>" if len(p.qs) > 1 else ""}</div></div>')
    groups = []
    for c in courses_out:
        if not c["problems"]:
            continue
        by_folder = {}
        for s in c["problems"]:
            p = by_slug[s]
            folder = posixpath.basename(posixpath.dirname(p.rel))
            by_folder.setdefault(re.sub(r"^\d+\s*[-–.]\s*|^\d+\s+", "", folder), []).append(p)
        inner = "".join(f'<h3>{esc(f)}</h3><div class="pgrid">{"".join(pcard(c, p) for p in sorted(ps, key=lambda x: x.title))}</div>' if len(by_folder) > 1 else
                        f'<div class="pgrid">{"".join(pcard(c, p) for p in sorted(ps, key=lambda x: x.title))}</div>' for f, ps in sorted(by_folder.items()))
        groups.append(f'<section class="pgroup" data-course="{c["id"]}" style="--c:{c["color"]}"><h2 class="sec">{esc(c["title"])}</h2>{inner}</section>')
    cards = "".join(groups)
    chips = '<button class="fchip on" data-f="all">All</button>' + "".join(f'<button class="fchip" data-f="{c["id"]}" style="--c:{c["color"]}">{esc(c["title"])}</button>' for c in courses_out if c["problems"])
    practice = f"""<h1 class="pg-title">Practice</h1><p class="lead">Read the problem, open only the hint, try it on paper, then lift the flap for the solution and mark yourself honestly. Problems you solve get a stamp.</p>
<div class="howto"><b>How to attack a problem</b><ol><li>Say what is asked and what is given.</li><li>Choose the principle before calculating.</li><li>Solve symbolically, then plug in numbers.</li><li>Check units and a limiting case.</li></ol></div>
<div class="filters"><input id="sf" type="search" placeholder="Filter, e.g. beam, bessel, rectifier…" autocomplete="off"></div><div class="filters">{chips}</div>{cards}"""
    (WIKI / "practice.html").write_text(shell("Practice", practice, "", "practice", crumbs=[("Library", "index.html"), ("Practice", None)]), encoding="utf-8")

    # ---------------------------------------------------------------- how to solve (problem-type tables)
    entries = []
    def inline(txt, n):
        txt = txt.replace("\\|", "|")
        t = re.sub(r"`([^`]+)`", lambda m: stash(f"<code>{esc(m.group(1))}</code>"), txt)
        t = re.sub(r"(?<![\\$\w])\$(?!\s|\$)([^$\n]+?)(?<![\s\\])\$(?!\d)", lambda m: math_token(m.group(1), False), t)
        def lk(m):
            nt = R.note(m.group(1))
            lab = m.group(3) if m.group(3) is not None else (nt.title if nt else m.group(1))
            return f'<a href="n/{nt.slug}.html">{esc(lab)}</a>' if nt else esc(lab)
        t = re.sub(r"\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]*))?\]\]", lk, t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
        t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
        return re.sub(r"\ue002(\d+)\ue003", lambda m: STASH[int(m.group(1))], t)
    for n in notes:
        lines = n.body.split("\n")
        i = 0
        while i < len(lines):
            if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
                head = [h.strip() for h in re.split(r"(?<!\\)\|", lines[i].strip().strip("|"))]
                j = i + 2
                rows = []
                while j < len(lines) and lines[j].lstrip().startswith("|"):
                    rows.append([c.strip() for c in re.split(r"(?<!\\)\|", lines[j].strip().strip("|"))]); j += 1
                hl = [h.lower() for h in head]
                if re.match(r"(problem|task|situation)", hl[0]) and any(re.search(r"method|approach|tool", h) for h in hl[1:]):
                    mi = next(k for k, h in enumerate(hl) if re.search(r"method|approach|tool", h))
                    for r in rows:
                        if len(r) > mi and r[0] and r[mi]:
                            entries.append(dict(c=n.cid, s=n.slug, p=inline(r[0], n), m=inline(r[mi], n)))
                i = j
            else:
                i += 1
    from solve_extra import SOLVE_EXTRA
    missing = []
    for cid, prob, meth in SOLVE_EXTRA:
        first = re.search(r"\[\[([^\]|#]+)", meth)
        nt = R.note(first.group(1)) if first else None
        for t in re.findall(r"\[\[([^\]|#]+)", meth):
            if not R.note(t):
                missing.append(t)
        entries.append(dict(c=cid, s=nt.slug if nt else "", p=inline(prob, None), m=inline(meth, None)))
    if missing:
        print("solve_extra: unresolved note names:", sorted(set(missing)))
    order_c = [c[0] for c in COURSES]
    entries.sort(key=lambda e: order_c.index(e["c"]))
    solve_cards = "".join(
        f'<details class="scard" data-course="{e["c"]}" style="--c:{cmap[e["c"]][3]}"><summary><span class="dot"></span><span class="sp">{e["p"]}</span><small>{esc(cmap[e["c"]][1])}</small></summary><div class="sm"><b>Use</b> {e["m"]}{f'<a class="src" href="n/{e["s"]}.html">Open note →</a>' if e["s"] else ""}</div></details>' for e in entries)
    schips = '<button class="fchip on" data-f="all">All</button>' + "".join(f'<button class="fchip" data-f="{cid}" style="--c:{cmap[cid][3]}">{esc(cmap[cid][1])}</button>' for cid in dict.fromkeys(e["c"] for e in entries))
    solve = f"""<h1 class="pg-title">How to solve</h1><p class="lead">“I see this kind of problem — what do I use?” Type a keyword or filter by course; open a card for the method.</p>
<div class="filters"><input id="sf" type="search" placeholder="Filter, e.g. beam, resonance, eigenvalue…" autocomplete="off"></div><div class="filters">{schips}</div>
<div class="scards">{solve_cards}</div>"""
    math_html = math_html + render_math(len(math_html))   # math added by the how-to-solve entries
    solve_html = finalize(solve, math_html)
    (WIKI / "solve.html").write_text(shell("How to solve", solve_html, "", "solve", katex=True, crumbs=[("Library", "index.html"), ("How to solve", None)]), encoding="utf-8")

    # ---------------------------------------------------------------- graph page
    idx = {n.slug: i for i, n in enumerate(notes)}
    edges = set()
    for n in notes:
        for t in n.links:
            if t in idx and t != n.slug:
                edges.add(tuple(sorted((idx[n.slug], idx[t]))))
    deg = [0] * len(notes)
    for a, b in edges:
        deg[a] += 1; deg[b] += 1
    graph = dict(n=[[n.slug, n.title, n.cid, deg[i]] for i, n in enumerate(notes)], l=[list(e) for e in sorted(edges)])
    legend = "".join(f'<span class="lg" style="--c:{c[3]}"><i></i>{esc(c[1])}</span>' for c in COURSES if any(n.cid == c[0] for n in notes))
    gbody = f'<h1 class="pg-title">Link map</h1><p class="lead">Every note is a pin and every link between notes a thread. Drag to pan, scroll or pinch to zoom; tap a pin to see its name, tap again to open it.</p><div class="legend">{legend}</div><div class="gwrap"><canvas id="graph"></canvas><div id="gtip"></div></div>'
    (WIKI / "graph.html").write_text(shell("Link map", gbody, "", "graph", wide=True, crumbs=[("Library", "index.html"), ("Link map", None)]), encoding="utf-8")

    # ---------------------------------------------------------------- data files
    meta = {n.slug: [n.title, n.cid, n.kind, getattr(n, "nsteps", 0), getattr(n, "nprob", 0)] for n in notes}
    data = dict(courses=courses_out, notes=meta, colors={c[0]: [c[3], c[4]] for c in COURSES}, titles={c[0]: c[1] for c in COURSES},
                graph=graph, back={k: sorted(v) for k, v in back.items()}, links={n.slug: sorted(n.links) for n in notes})
    (ASSETS / "data.js").write_text("window.WIKI=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")
    (ASSETS / "search.js").write_text("window.WIKI_SEARCH=" + json.dumps(search, ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")

    # ---------------------------------------------------------------- vendor assets
    for rel in sorted(R.used_imgs):
        shutil.copy2(VAULT / rel, ASSETS / "img" / Path(rel).name)
    sims_dir = ASSETS / "sims"
    if sims_dir.exists():
        shutil.rmtree(sims_dir)
    sims_dir.mkdir(parents=True, exist_ok=True)
    for name, rels in files.items():
        for rel in rels:
            if rel.endswith(".html"):
                shutil.copy2(VAULT / rel, sims_dir / Path(rel).name)
    nm = HERE / "node_modules"
    vend = ASSETS / "vendor"
    (vend / "fonts").mkdir(parents=True, exist_ok=True)
    css = (nm / "katex/dist/katex.min.css").read_text(encoding="utf-8")
    css = re.sub(r',url\(fonts/[^)]+\.woff\) format\("woff"\),url\(fonts/[^)]+\.ttf\) format\("truetype"\)', "", css)
    (vend / "katex.min.css").write_text(css, encoding="utf-8")
    for f in (nm / "katex/dist/fonts").glob("*.woff2"):
        shutil.copy2(f, vend / "fonts" / f.name)
    shutil.copy2(nm / "mermaid/dist/mermaid.min.js", vend / "mermaid.min.js")
    nun = nm / "@fontsource-variable/nunito/files"
    for f in ("nunito-latin-wght-normal.woff2", "nunito-latin-ext-wght-normal.woff2"):
        if (nun / f).exists():
            shutil.copy2(nun / f, vend / "fonts" / f)
    print(f"notes: {len(notes)}  math snippets: {len(MATH)}  images: {len(R.used_imgs)}  how-to-solve entries: {len(entries)}  graph edges: {len(edges)}")
    by_kind = {}
    for n in notes:
        by_kind[n.kind] = by_kind.get(n.kind, 0) + 1
    print("kinds:", by_kind, "| pages with steps:", sum(1 for n in notes if getattr(n, 'nsteps', 0) >= 2))


if __name__ == "__main__":
    main()

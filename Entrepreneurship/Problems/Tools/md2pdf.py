"""Convert an Obsidian note to a plain submission PDF: `python md2pdf.py "<note>.md" "<output>.pdf" [figure width %]`.
   Handles frontmatter, ![[image]] embeds, [[wikilinks]], > [!callout] blocks and a title block
   (a "**Batch ... Group ...**" paragraph followed by a "Name (ROLL) · Name (ROLL)" paragraph); prints through headless Edge."""
import re, sys, os, subprocess, markdown

src, dst = sys.argv[1], sys.argv[2]
imgw = sys.argv[3] if len(sys.argv) > 3 else "92"
base = os.path.dirname(os.path.abspath(src))
t = open(src, encoding="utf-8").read()
t = re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)
t = re.sub(r"^Related:.*\n", "", t, flags=re.M)
t = re.sub(r"!\[\[([^\]|]+)\]\]", lambda m: f'<img src="assets/{m.group(1)}">', t)
t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", t)
t = re.sub(r"\[\[([^\]]+)\]\]", lambda m: re.sub(r"\.pdf$", "", m.group(1)), t)

def callout(m):
    body = re.sub(r"^> ?", "", m.group(2), flags=re.M)
    return f'<div class="callout" markdown="1">\n\n{body}\n\n</div>\n'
t = re.sub(r"^> \[!(\w+)\][^\n]*\n((?:>.*\n?)*)", callout, t, flags=re.M)

ROLL = r"[A-Z]{2}\d{2}[A-Z]\d{3}"
def title_block(m):
    title, meta, names = m.group(1), m.group(2).strip("* "), m.group(3)
    people = "; ".join(f"{n.strip()} ({r})" for n, r in re.findall(r"([^()·]+?)\s*\((" + ROLL + r")\)", names))
    return f'<div class="head"><h1>{title}</h1><p class="meta">{meta}</p><p class="names">{people}</p></div>\n'
t = re.sub(r"^# (.+)\n+(\*\*Batch[^\n]*)\n+([^\n]*\(" + ROLL + r"\)[^\n]*)\n", title_block, t, count=1, flags=re.M)

html = markdown.markdown(t, extensions=["tables", "md_in_html"])
# keep an image and its caption together
html = re.sub(r"(?:<p>)?(<img [^>]*>)(?:</p>)?\s*<p><em>((?:Figure|Fig\.)[^<]*(?:<[^>]+>[^<]*)*?)</em></p>",
              lambda m: f"<figure>{m.group(1)}<figcaption>{m.group(2)}</figcaption></figure>", html)
# long tables may break across pages (rows stay whole, header repeats); short ones stay in one piece
html = re.sub(r"<table>(.*?)</table>", lambda m: ('<table class="long">' if m.group(1).count("<tr>") > 4 else "<table>") + m.group(1) + "</table>", html, flags=re.S)

css = """
@page{size:A4;margin:20mm 20mm 18mm}
*{box-sizing:border-box}
body{font-family:Cambria,'Times New Roman',Georgia,serif;font-size:10.5pt;line-height:1.38;color:#000;margin:0}
.head{margin-bottom:10pt;padding-bottom:6pt;border-bottom:.75pt solid #000}
h1{font-size:15pt;line-height:1.2;margin:0 0 4pt;font-weight:700}
.meta{margin:0;font-weight:700}
.names{margin:1pt 0 0;font-size:9.5pt}
h2{font-size:11.5pt;font-weight:700;margin:13pt 0 4pt;break-after:avoid}
h3{font-size:10.5pt;font-weight:700;font-style:italic;margin:9pt 0 3pt;break-after:avoid}
p{margin:4pt 0}
table{border-collapse:collapse;width:100%;margin:6pt 0 8pt;font-size:9pt;line-height:1.3;border-top:1pt solid #000;border-bottom:1pt solid #000;break-inside:avoid}
table.long{break-inside:auto}tr{break-inside:avoid}thead{display:table-header-group}
th{text-align:left;font-weight:700;padding:3pt 6pt 3pt 0;border-bottom:.6pt solid #000;vertical-align:bottom}
td{padding:2.5pt 6pt 2.5pt 0;vertical-align:top;border:0}
img{display:block;margin:6pt auto 2pt;max-width:__IMGW__%;max-height:105mm}
figure{margin:6pt 0;break-inside:avoid}figcaption{font-size:9pt;text-align:center;margin-top:2pt}
ul,ol{margin:4pt 0 4pt 16pt;padding:0}li{margin:1.5pt 0}
a{color:#000;text-decoration:underline}
code{font-family:Consolas,monospace;font-size:9pt}
.callout{border-left:1.5pt solid #777;padding:1pt 0 1pt 9pt;margin:7pt 0}
""".replace("__IMGW__", imgw)
full = f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{html}</body></html>"
tmp = os.path.join(base, "_tmp_render.html"); open(tmp, "w", encoding="utf-8").write(full)
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
subprocess.run([edge, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={os.path.abspath(dst)}", "file:///" + tmp.replace("\\", "/")], check=True, timeout=120)
os.remove(tmp); print("wrote", dst)

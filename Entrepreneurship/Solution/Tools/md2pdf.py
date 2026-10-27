"""Convert an Obsidian note to a submission PDF: `python md2pdf.py "<note>.md" "<output>.pdf"`.
   Handles frontmatter, ![[image]] embeds, [[wikilinks]] and > [!callout] blocks; prints through headless Edge."""
import re, sys, os, subprocess, tempfile, markdown

src, dst = sys.argv[1], sys.argv[2]
base = os.path.dirname(os.path.abspath(src))
t = open(src, encoding="utf-8").read()
t = re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)
t = re.sub(r"^Related:.*\n", "", t, flags=re.M)
t = re.sub(r"!\[\[([^\]|]+)\]\]", lambda m: f'<img src="assets/{m.group(1)}">', t)
t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", t)
t = re.sub(r"\[\[([^\]]+)\]\]", lambda m: re.sub(r"\.pdf$", "", m.group(1)), t)
def callout(m):
    kind, body = m.group(1), re.sub(r"^> ?", "", m.group(2), flags=re.M)
    return f'<div class="callout {kind}" markdown="1">\n\n{body}\n\n</div>\n'
t = re.sub(r"^> \[!(\w+)\][^\n]*\n((?:>.*\n?)*)", callout, t, flags=re.M)
html = markdown.markdown(t, extensions=["tables", "md_in_html"])
css = """@page{size:A4;margin:16mm 14mm}body{font-family:'Segoe UI',Arial,sans-serif;font-size:10pt;line-height:1.4;color:#222}
h1{font-size:18pt;margin:0 0 4pt;color:#12355b}h2{font-size:13pt;margin:16pt 0 5pt;color:#12355b;border-bottom:1px solid #bbb;padding-bottom:2pt}
table{border-collapse:collapse;width:100%;margin:6pt 0;font-size:8.6pt}th,td{border:1px solid #bbb;padding:3pt 5pt;vertical-align:top}th{background:#e9eef5}
img{max-width:94%;max-height:118mm;display:block;margin:6pt auto}h2{page-break-after:avoid}em{color:#444}a{color:#12355b}tr,img{page-break-inside:avoid}
.callout{border-left:4px solid #12355b;background:#f2f6fb;padding:4pt 10pt;margin:8pt 0}.callout.warning{border-color:#c0392b;background:#fdf1ef}p{margin:4pt 0}"""
full = f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{html}</body></html>"
tmp = os.path.join(base, "_tmp_render.html"); open(tmp, "w", encoding="utf-8").write(full)
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
subprocess.run([edge, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={os.path.abspath(dst)}", "file:///" + tmp.replace("\\", "/")], check=True, timeout=120)
os.remove(tmp); print("wrote", dst)

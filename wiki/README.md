# Wiki site

A static, offline learning site generated from the vault's notes. Open `index.html` in a browser; nothing needs a server.

## What you get
- **Learn**: each course is a path of lessons (Duolingo-style). *Start lesson* turns a note into step-by-step cards; *Mark as learned* gives XP and fills the progress ring.
- **Play with it**: interactive explorers on the relevant notes (damping, time constants, Mohr's circle, beam deflection, column buckling, series approximations, Bessel/Legendre, resonance, lumped cooling, GSP vs VCG auctions).
- **Practice**: tutorial and assignment notes with the hint, solution, result and trap hidden behind buttons, plus self-grading (+15 XP).
- **How to solve**: "I see this kind of problem, what do I use?" cards for every course (108 entries).
- **Graph**, **Search** (`/` or Ctrl+K), **backlinks and related notes**, **dark mode**, and the stand-alone simulations from the vault.
- Progress (XP, streak, finished lessons, ticked checklists) is stored in the browser's local storage on this device.

## Rebuild after editing notes
```
pip install markdown          # once
cd wiki/_build && npm install # once (KaTeX, mermaid, Nunito font)
python wiki/_build/build.py   # from the vault root, regenerates everything in wiki/
python wiki/_build/check_site.py   # broken links, leftover placeholders, personal strings
```
`build.py` reads the notes directly, so the generated folders (`n/`, `course/`, `assets/img`, `assets/sims`, `assets/data.js`, `assets/search.js`, `assets/vendor`) can be deleted and rebuilt at any time.

## Scope
Published: Differential Equations, Strength of Materials, Fluid Mechanics, KDoMs, EE1100, Cross-Domain notes, Computing, the Entrepreneurship map and the course maps for the upcoming courses.
Left out: `Applications`, `Clubs & Projects`, `Entrepreneurship/Solution` (team assignments with names and roll numbers), `Chemistry`, `Life sciences`, `Templates`, `CLAUDE.md`, the guide and the maintenance log. PDFs (lecture slides, problem sheets) are **not** copied or linked: a reference to one shows as plain text, so nothing from the course packs is published.
To add a note, just write it in the vault. To attach an explorer to a note, add its file name to `WIDGETS` in `build.py`. To add a how-to-solve entry for a course, edit `solve_extra.py`, or add a table with a "Problem type | Method" header to any note.

## Deploy on Vercel
The site is plain static files, so there is no build step on Vercel.
1. Push the repository (the generated `wiki/` folder is committed).
2. In Vercel: **Add New Project**, import the repository, set **Root Directory** to `wiki`, **Framework Preset** to *Other*, leave *Build Command* empty and *Output Directory* at its default (`.`).
3. `vercel.json` adds cache and security headers; `.vercelignore` keeps `_build/` (scripts, `node_modules`) out of an upload made with the CLI (`vercel --prod` from `wiki/`).
4. After editing notes: run `python wiki/_build/build.py`, commit the regenerated `wiki/` and push; Vercel redeploys.

Progress is kept in each visitor's own browser (local storage), so a public deployment shares nothing between people.

## Phones
Layout switches to a bottom tab bar under 820 px; every page was checked for horizontal overflow at 360 px and 390 px widths. Sliders and buttons have 44 px touch targets, the graph supports one-finger pan, two-finger pinch and tap-to-preview/tap-to-open, wide equations and tables scroll sideways inside their own box, and `manifest.webmanifest` lets the site be added to the home screen.

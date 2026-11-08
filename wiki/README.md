# Wiki site

A static, offline learning site generated from the vault's notes. Open `index.html` in a browser; nothing needs a server.

## What you get
- **A notebook on a desk.** Leather top bar with brass keys, wood-grain desk, ruled paper pages with binder holes, a bookshelf of cloth-bound course books on the home page, taped sticky-note callouts, and brushed-metal panels for the explorers. Day desk and night desk (the sun/moon key).
- **Easy navigation.** A contents tree (chapters fold open, your place is highlighted, read pages are ticked) sits beside every course and note; on a phone it slides in from the menu key. Breadcrumbs on every page, a bottom tab bar on phones (Library, Practice, Solve, Link map, Search), "On this page" outline, previous/next page, a reading thread under the top bar, a back-to-top key, and Search (`/` or Ctrl+K) that lists your recently opened pages before you type.
- **Library and courses.** Each course is a book on the shelf with a progress bar; opening it shows a table of contents. *Study mode* turns a note into one page at a time; *Mark as read* ticks it off.
- **Foldable callouts.** Obsidian callouts written as `> [!question]- Title` fold closed (`+` opens them) and become tappable flaps on the site: predict-first prompts, traps, analogies, worked examples and quiz answers hide until you open them.
- **Play with it**: interactive explorers on the relevant notes (damping, free and driven oscillations, pendulum phase portraits, orbits, divergence and curl, time constants, Mohr's circle, beam deflection, column buckling, series approximations, Bessel/Legendre, resonance, lumped cooling, GSP vs VCG auctions).
- **Practice**: tutorial and assignment notes with the hint, solution, result and trap hidden behind flaps; mark a problem solved and it gets a stamp.
- **How to solve**: "I see this kind of problem, what do I use?" cards for every course (108 entries).
- **Link map**: every note is a pin on a cork board, every link a red thread; backlinks and related notes on each page; plus the stand-alone simulations from the vault.
- Progress (read pages, solved problems, ticked checklists, recent pages) is stored in the browser's local storage on this device. There are no points or streaks.

## Rebuild after editing notes
```
pip install markdown          # once
cd wiki/_build && npm install # once (KaTeX, mermaid)
python wiki/_build/build.py   # from the vault root, regenerates everything in wiki/
python wiki/_build/check_site.py   # broken links, leftover placeholders, personal strings
```
`build.py` reads the notes directly, so the generated folders (`n/`, `course/`, `assets/img`, `assets/sims`, `assets/data.js`, `assets/search.js`, `assets/vendor`) can be deleted and rebuilt at any time.

## Scope
Published: Differential Equations, Physics I, Engineering Mechanics, Engineering Drawing, Physics Laboratory I, Applied Mechanics Lab, Strength of Materials, Fluid Mechanics, KDoMs, Heat Transfer, Introduction to Machine Design, Materials and Design, Manufacturing Technology, Measurements, Instrumentation and Control, Foundations of Thermal Engineering, Computer Aided Machine Drawing, EE1100, Cross-Domain notes, Computing and the Entrepreneurship map.
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
The contents tree becomes a slide-in drawer under 1000 px and a bottom tab bar appears;  every page was checked for horizontal overflow at 360 px and 390 px widths. Sliders and buttons have 44 px touch targets, the graph supports one-finger pan, two-finger pinch and tap-to-preview/tap-to-open, wide equations and tables scroll sideways inside their own box, and `manifest.webmanifest` lets the site be added to the home screen.

### Phone layout (700 px and under)
A separate "pocket notebook" layout: the paper runs edge to edge (no desk border, margin line or binder holes), the header is 48 px, the breadcrumb is a single scrolling line, and the five-tab dock stays at the bottom. The home page opens with a slim *continue* card and a two-column bookshelf; reading text is 16.5 px at 1.62 line height; figures, tables and code blocks run full width and scroll sideways inside themselves; callout tape is hidden; chip and filter rows scroll horizontally; the heavy paper-noise textures are dropped for smoother scrolling. Checked for horizontal overflow at 360 px on every course's pages.

### Scrollbars
Every scroll area uses a slim, theme-coloured bar (never the white OS bar). On phones (700 px and under) bars are hidden entirely; tables and display equations that scroll sideways show a soft edge shadow instead, and tags and breadcrumbs wrap rather than scrolling.

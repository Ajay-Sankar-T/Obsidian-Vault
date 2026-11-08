---
tags: [wiki, maintenance, log]
---

# Wiki Maintenance Log

Use this note to record structural changes that affect navigation, naming, templates, or MOCs.

## 2026-09-20

- Added [[Home]] as the vault entry point.
- Added [[LLM Wiki Guide]] so future LLM-assisted edits follow the same conventions.
- Added note templates in [[Templates/Atomic Concept Note]] and [[Templates/Course MOC]].
- Added a top-level [[Differential Equations - MOC|Differential Equations MOC]] to connect the existing Differential Equations sub-MOCs.

## 2026-10-07

- Added three formula-bank + solved-problem pairs to [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] (folders 06, 07, 08): dimensional analysis and similitude, differential mass conservation and fluid kinematics, incompressible inviscid flow and Bernoulli (source: White, Fluid Mechanics 4th ed., Chs. 3–6).
- Added `Fluid Mechanics/Tools/` (`fm_core.py` verification, `fm_viz.py`, `fm_pitot.py`) and `Fluid Mechanics/assets/` (figures `FM-*.png`).
- The existing [[Fluid Mechanics/01 Dimensionless Numbers/Buckingham Pi Theorem|Buckingham π Theorem]] note was kept; the new formula bank links to it instead of duplicating it.

## 2026-10-08

- Added `CLAUDE.md` and `.claude/skills/` (`wiki-concept-note`, `wiki-course-moc`, `wiki-tutorial-problem`, `wiki-visuals`), built from [[Templates/Atomic Concept Note]], [[Templates/Course MOC]] and [[LLM Wiki Guide]].
- Fixed missing `---` frontmatter fences in [[LLM Wiki Guide]] and both templates.
- Added [[KDoMs/KDoMs - MOC|KDoMs MOC]]; linked KDoMs, WebOps, Excalidraw and the AM2540 lab manuals from [[Home]] / [[Strength of materials/Strength of Materials - MOC|Strength of Materials MOC]].
- Repointed six Tutorial 5 (Strength of Materials) links from the empty stub `02 Axial Loading` to the real MOC section.
- Added five cross-domain syntheses (now eleven) to [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]: gears/transformers, rotating vectors, conservation laws and flow networks, second moments, fluids vs solids. Added "Cross-domain links" backlinks in 16 concept notes.
- Corrected the continuity note's tank analogy: stored mass ↔ capacitor charge/voltage continuity, not inductor current.
- `.gitignore` now ignores `__pycache__/` and `*.pyc`.
- Pending (needs user approval to delete): empty `2026-09-08.md`, `02 Axial Loading.md`, `MathFlow/Untitled 1.md`, `MathFlow/Differential Equations/Untitled 1 1.md`; five 0-byte PDFs in `Fluid Mechanics/GPS/`; tracked `__pycache__` files.

## 2026-10-15

- Added [[Strength of materials/Tutorial 6 - Torsional Members/Tutorial 6 - Torsional Members|AM2200 Tutorial 6 — Torsional Members]] (theory + Q1–Q6 in one note, as requested), linked from [[Strength of materials/Strength of Materials - MOC|Strength of Materials MOC]] and [[Strength of materials/03 Torsion/Torsion of Circular Shafts|Torsion of Circular Shafts]].
- Added `Strength of materials/Tools/sm_t6.py` (verification numbers and figure generator) and `Strength of materials/assets/SM-T6-*.png` (six figures).
- Results agree with the handwritten `AM2200 Tutorial-6 Solutions.pdf` (tau_max = 4.653 ksi, phi_D = 0.978 deg, d_B/d_A = 1.446, Q3/Q5/Q6 closed forms).

## 2026-10-22

- Added [[Strength of materials/Tutorial 7 - Bending and Shear Stresses/Tutorial 7 - Bending and Shear Stresses|AM2200 Tutorial 7 — Bending and Shear Stresses]] (theory + Q1–Q8 in one note, same layout as Tutorial 6), linked from [[Strength of materials/Strength of Materials - MOC|Strength of Materials MOC]] and [[Strength of materials/05 Bending Stresses/Flexure Formula|Flexure Formula]].
- Added `Strength of materials/Tools/sm_t7.py` (verification numbers and figure generator) and `Strength of materials/assets/SM-T7-*.png` (nine figures).
- No reference solution exists for this sheet; results were checked by numerical integration of section properties and limiting cases. Interpretation choices flagged in the note: Q2 compression side at the bottom, Q3 plate 350x20 on three 10x30 legs, Q8 moment sense read from the figure (tension on top).

## 2026-10-26

- Added [[MathFlow/Differential Equations/Problems/Assignment 6 - Bessel Functions - Solutions|Assignment 6 — Bessel Functions]] and [[MathFlow/Differential Equations/Problems/Assignment 7 - Sturm-Liouville Problems - Solutions|Assignment 7 — Sturm–Liouville Problems]] (every question solved, same layout as Assignments 1–5), linked from [[MathFlow/Differential Equations/Problems/Problems - MOC|Problems MOC]] and [[MathFlow/Differential Equations/Special Functions/Special Functions - MOC|Special Functions MOC]].
- Added three concept notes drawn from Lectures 26–28: [[MathFlow/Differential Equations/Special Functions/Reducing Equations to Bessel Form|Reducing Equations to Bessel Form]], [[MathFlow/Differential Equations/Special Functions/Fourier-Bessel Series|Fourier-Bessel Series]], [[MathFlow/Differential Equations/Special Functions/Sturm-Liouville Problems|Sturm-Liouville Problems]]. Replaced the "no solution note yet" remarks in the two Bessel notes; the Special Functions MOC and DE MOC now cover Lectures 18–28.
- Added `MathFlow/Differential Equations/Tools/de_a6a7.py` (asserts every identity, eigenpair and coefficient quoted; generates the figures) and `Problems/assets/A6-fig1…8`, `A7-fig1…5`.
- Sheet errors found and flagged in the notes: A6 Q3(c) has the wrong sign ($-2x^{-3}J_3$, not $+2x^{-3}J_3$); A6 Q11(a) needs the non-elementary $\int J_0$; A7 Q3(j), (k) put a condition at the singular point $x=0$ (continuous spectrum / no eigenvalues as printed; regular variants with left end 1 are given); A7 Q5 and Q6 label two parts "(c)".
- Interpretation choices: Fourier–Bessel series use the Dirichlet zeros of $J_\nu$ (Lecture 27 convention); Q6 coefficients are given both for the orthonormal and the plain cosine basis.

## 2026-10-27

- Added `Entrepreneurship/Solution/` for the Session 8 (Exponential & Systems Thinking) assignments: [[Entrepreneurship/Solution/Assignment 8.1 - Six Ds Analysis of Ather Energy|Assignment 8.1]] (complete: Ather Energy on the 6 Ds, EXPAND checklist and Exponential Project Canvas, three figures, sourced), plus fill-in templates [[Entrepreneurship/Solution/Assignment 8.2 - Exponential Thinking for Our Project|Assignment 8.2]] and [[Entrepreneurship/Solution/Team Contribution|Team Contribution]] (the team's project and member details are not in the vault).
- Added `Solution/Tools/ather_figs.py` (figures), `Solution/Tools/md2pdf.py` (note → submission PDF via headless Edge) and `Solution/assignment_8_1_batch_XX_group_YY.pdf` (rename with the real batch and group).
- Numbers in 8.1 come from the Session 8 deck, the Ather case study and press coverage of Ather's results (outlets differ; each is attributed). The running-cost comparison and the 10× delivery target are labelled as the author's own illustrative estimates.

## 2026-10-27 (b)

- Added [[Strength of materials/Tutorial 8 - Deflection of Beams/Tutorial 8 - Deflection of Beams|AM2200 Tutorial 8 — Deflection of Beams]] (theory + Q1–Q8 in one note, same layout as Tutorial 7) in its own folder, linked from [[Strength of materials/Strength of Materials - MOC|Strength of Materials MOC]], [[Strength of materials/08 Deflection of Beams/Double Integration and Macaulay's Method|Double Integration and Macaulay's Method]] and [[Strength of materials/10 Energy Methods/Strain Energy and Castigliano's Theorem|Strain Energy and Castigliano's Theorem]].
- Added `Strength of materials/Tools/sm_t8.py` (symbolic and numerical verification, figure generator) and `Strength of materials/assets/SM-T8-*.png` (eight figures).
- No reference solution exists for this sheet; all results were checked against numerical double integration. Figure readings flagged in the note: Q1 ($L$ measured to the load, $AB=L-l$), Q3 (triangle's 15 kN/m end next to the point load, "mm⁶" read as mm⁴), Q4 (couple clockwise), Q6 (post 1 m high, load on the whole beam), Q7 (UDL on $B$–$C$ only).

## 2026-10-27 (c)

- Added course maps for the Semester 4–5 mechanical-engineering courses whose syllabi were placed in `mech stuff/`: [[Foundations of Thermal Engineering - MOC]] (ME2102 + ME3105), [[Heat Transfer - MOC]] (ME3101), [[Materials and Design - MOC]] (ME2200), [[Manufacturing Technology - MOC]] (ME2302 + ME3305), [[Measurements, Instrumentation and Control - MOC]] (ME2400), [[Introduction to Machine Design - MOC]] (ME3203), [[Computer Aided Machine Drawing - MOC]] (ME3283).
- Added [[Mechanical Engineering Curriculum - MOC]] (semester map from `ME25B_curriculum.pdf`, credits, status of each course in the vault) and linked all of them from [[Home]].
- These are **syllabus-based maps**, not lecture notes: topics are listed from each `Course Details.md`; problem-type tables and cross-domain links are written from standard course content and the existing vault notes. Atomic concept notes will be added when the courses start. Empty folders (Thermodynamics, Computing for Mechanical Engineers, Mechanical engineering lab) have no syllabus yet, so they are listed in the curriculum map but have no MOC.
- The syllabus file for Foundations of Thermal Engineering (`Desc.md` → `Course Details.md`) contains both FTE-1 and FTE-2 text; the split was inferred from content (the second block refers back to "Foundations of Thermal Engg-1").

## 2026-10-28

- Added `Entrepreneurship/Solution/Assignment_9_Batch_B_group_14.pdf` and its source note [[Entrepreneurship/Solution/Assignment 9 - Sponsored Search Market (VCG and GSP)|Assignment 9 — Sponsored Search Market (VCG and GSP)]]: social optimum, VCG prices, GSP truthful bidding, equilibria and revenue for the slide-57 market of `Pricing-1.pdf` (slide 57 shows only the market, so the task was read from slides 54–56 and cross-checked against slides 58–59).
- Added `Solution/Tools/assignment9_check.py` (brute-force VCG, GSP and equilibrium checks; figure `A9-fig2`). All slide numbers (VCG 44, GSP equilibria 48 and 34, payoffs 10 and 24) are reproduced.

## 2026-10-29

- Updated the knowledge graph incrementally with `/graphify` (94 changed files; 6,545 nodes, 10,899 edges, 396 communities).
- Linked related notes that were not connected: 65 notes gained a "Cross-domain links", "See also" or "Continues in" section. Main bridges: exponential decay ↔ heat transfer, instrumentation and ODEs; Fourier's law as a third constitutive law; thermal and electrical analogy; eigenvalues ↔ Sturm–Liouville, transfer-function poles and covariance; the ML formula sheet (previously isolated) ↔ inner-product spaces, gradient flow, second-order systems; course MOCs ↔ the courses that continue them; missing links inside DE, EE1100, KDoMs, Strength of Materials and Fluid Mechanics.
- Added [[Entrepreneurship - MOC]] (the Entrepreneurship folder had no map) and linked it, and the ML sheet, from [[Home]].
- Every wikilink added in this pass resolves; every note now has an incoming link except `CLAUDE.md`.
- Restructuring the vault layout was considered and declined by the owner: folder layout and PDF locations are unchanged.

## 2026-10-31

- Added `wiki/`: a static, offline learning site generated from the vault (`wiki/index.html`). Duolingo-style course paths, lesson mode, practice problems with hint/solution/result reveal and self-grading, how-to-solve cards, interactive explorers on 25 notes, search, backlinks, graph, dark mode and XP/streak stored in the browser. Rebuild with `python wiki/_build/build.py`; see `wiki/README.md`.
- Scope: course notes only. Applications, Clubs & Projects, Entrepreneurship/Solution (team assignments), Chemistry, Life sciences, Templates, CLAUDE.md, the guide and this log are not published.
- `wiki/_build/node_modules/` is gitignored; the generated site itself is not committed yet.
- Site audit pass: fixed unit order and names (Differential Equations now starts at first-order ODEs; machinery, computing and electrical units renamed), lesson order follows each unit's own map, upcoming courses list their syllabus topics as locked nodes, Practice groups by course and tutorial with a link per question, and every math snippet now renders (the build prints any KaTeX failure to `wiki/_build/math_errors.txt`).
- Source fixes found by the audit: unclosed `\boxed{` in `AC Transient and Steady-State Response of RLC Circuits`; escaped callouts (`> \[!abstract\]`) in `ML_Formula_Theory_Obsidian`.
- Site second pass: lists that follow a paragraph line (common inside callouts) now render as lists; the Mohr's circle explorer no longer clips the circle (equal axis scales); all explorer axes use round tick values; upcoming-course cards on the home page say "syllabus map, notes coming" instead of "1 lesson".

## 2026-11-02

- **Partial differential equations (Lectures 29–37, Assignments 8–10).** New folder `MathFlow/Differential Equations/PDEs/` with [[PDEs - MOC]] and 13 concept notes (definitions and direct integration, formation, Lagrange's method, Cauchy problem, complete/general/singular integrals, classification, canonical forms, d'Alembert, separation of variables, wave, heat, Laplace in rectangles/strips and in polar coordinates); Lecture 29 examples added to [[Sturm-Liouville Problems]]. Solutions: [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]], [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]], [[Assignment 10 - Laplace Equations - Solutions]]. Verification and figures in `Tools/de_a8_*.py`, `de_a9_a10.py`, `de_pde_figs.py`. The checks found three mistakes in the sheets' printed answers (A9 Q3(c), A10 Q8(a) and Q8(b)); they are flagged in the notes.
- **Fluid Mechanics 09 Pipe Flow and Losses** (GPS 7 and 8): formula bank and six solved problems with Moody-chart figures; `Tools/fm_pipe.py`.
- **EE1100 Tutorials 6 (op-amps) and 7 (transformers):** one note per question, theory note for op-amps, circuits redrawn; `Basic Electrical Engineering/Tools/ee_t6_t7.py`. New concept notes in `Transformers and Induction Machines/` from Lectures 39–41 (voltage regulation and efficiency, revolving field, slip and power flow, types and construction); the two animations are linked from them.
- KDoMs tutorial PDFs now live in `KDoMs/Tutorials/`; the MOC text was updated (Tutorials 1–4 and 8 still unsolved).
- Site: mobile polish and Vercel configuration (see the wiki README).

## 2026-11-05

- **AM2200 Tutorial 9 (Columns):** [[Tutorial 9 - Columns/Tutorial 9 - Columns|solution note]] for Q1–Q5 with figures and `Strength of materials/Tools/sm_t9.py` (the spring-ended and rigid-plus-elastic conditions were cross-checked by integrating the buckling ODE); [[Euler Buckling of Columns]] got a short section on restrained and stepped columns.
- **Site redesign:** dropped the gamified look (XP, streaks, rings) for a skeuomorphic notebook (leather bar, wood desk, paper pages, bookshelf, cork-board link map) with a contents tree, breadcrumbs, phone drawer and bottom tabs; `wiki/README.md` describes it. Checked at 360 and 390 px.
- **Physics I (PH1010) concept notes.** New [[Physics/Physics I - MOC|Physics I - MOC]] and 22 atomic notes in `mech stuff/Physics/` (numbered folders `01`–`08`, one per syllabus module), written from the 2026 syllabus and the weekly slide decks. Each note has a core idea, figures, foldable callouts (predict-first, traps, analogies, worked examples, quiz questions), cross-domain links and a self-check list. 35 figures are generated by `Physics/Tools/ph_all.py` into `Physics/assets/PH-*.png`; `Tools/ph_check.py` recomputes every number quoted in the notes and `Tools/ph_links.py` checks the wikilinks. Linked from Home, the curriculum MOC, [[The Universal Second-Order Linear System]] and [[Conservation of Mass (Continuity Equation)]].
- **Site support for the new notes:** Obsidian foldable callouts (`> [!kind]-` / `+`) now become tappable flaps on the site; Physics added as a course (olive book); five new explorers (free oscillation, driven oscillator, pendulum phase portrait, orbit, divergence and curl); widget slider labels no longer forced to upper case (it turned ω into Ω).
- **Course-file folders turned into notes (from the PDFs):** [[Engineering Mechanics - MOC|Engineering Mechanics]] (16 notes in `Statics/` and `Dynamics/`, built on the Meriam & Kraige books; 15 figures; a small truss solver in `Tools/em_figs.py`), [[Engineering Drawing - MOC|Engineering Drawing]] (6 notes from the General Guidelines deck, 6 figures), [[Physics Laboratory I - MOC|Physics Laboratory I]] (9 experiment notes plus [[Error Analysis - Uncertainty and Propagation]], 11 figures, from the PH1030 manual and error-analysis handout and the grating deck) and [[Applied Mechanics Lab - MOC|Applied Mechanics Lab]] (5 experiment notes from the `Fluid Mechanics Lab/` manuals, which are really the AM2540 solid-mechanics experiments; 4 figures). Each folder has `Tools/` scripts that regenerate the figures and recompute the numbers. Experiment figures use **illustrative** specimen data and say so. A filled-in torsion report in `Fluid Mechanics Lab/` was not summarised (personal data). Still empty, so nothing to read: `Thermodynamics/`, `Computing for Mechanical Engineers/`, `Mechanical engineering lab/`.
- Site: four new books (AM1100, ME1480, PH1030, AM2540); shorter titles on book spines. Link check helper: `wiki/_build/check_notes.py`.
- **Site: phone redesign.** New last block in `wiki/assets/style.css` (≤700 px): full-bleed paper, 48 px header, slimmer dock, compact home (continue card first, 2-column shelf), 16.5 px reading text, full-width figures and tables, horizontal-scroll chip/filter rows, no noise textures. Verified at 360 px on 111 pages with no sideways overflow, in light and dark.

## 2026-11-06

- **KDoMs Tutorials 9 and 10 solved.** [[KDoMs/Tutorial-solutions/Tutorial-9-solution|Tutorial 9]] (flat-face cam, cycloidal: profile, graphical construction, $v_{\max}$, $a_{\max}$, $\rho$, driving-effort eccentricity) and [[KDoMs/Tutorial-solutions/Tutorial-10-solution|Tutorial 10]] (Q1 flywheel mass, Q2 two-plane balancing, checked against the answer key of Mallik & Ghosh 7.14). Script `KDoMs/Tutorial-solutions/tut9_10.py` produces every number and the figures in `Tutorial-solutions/assets/T9-*`, `T10-*` and `T9-anim.gif`.
- New concept folder `KDoMs/Cams-Flywheels-Balancing/` with [[Cam Motion Laws and the Flat-Face Follower]], [[Flywheel Sizing from the Turning-Moment Diagram]] and [[Balancing of Rotors - Static and Dynamic]]; linked from [[KDoMs - MOC]] (new spine item 4, method-selector rows, exam patterns, problem coverage). Site: new unit "Cams, flywheels and balancing" in `build.py`.
- **Fluid Mechanics GPS 9 & 10 solved.** New folder `Fluid Mechanics/10 Viscous Flow and Exact Solutions/` with a [[Viscous Flow and Exact Solutions - Formula Bank|formula bank]] (unidirectional-flow recipe, Couette/Poiseuille/film/pipe/annulus table) and [[Viscous Flow and Exact Solutions - Solved Problems|solved problems]] for all eight questions (flow chamber, lava, stagnation-point flow, wire coating, dashpot, syringe, siphon, pump); `Tools/fm_gps9_10.py` recomputes every number and draws the nine `FM-V*` figures. Linked from [[Fluid Mechanics - MOC]].

## 2026-11-08

- **KDoMs lecture slides turned into notes (lectures 1–5).** New folder `KDoMs/Foundations/`: [[Kinematic Pairs, Links and Chains]], [[Mobility - Kutzbach Equation and Exceptions]], [[Grashof Criterion and Four-Bar Inversions]] and [[Kinematic Inversion - Slider-Crank and Double-Slider Families]], with seven figures `FND-*` and `found_core.py` (mobility counts, brute-force Grashof check, quick-return ratios). New interactive explorer on the Grashof note (`fourbar` in `widgets.js`/`build.py`). Linked from [[KDoMs - MOC]] (new spine item 0, method-selector rows); site unit "Mechanism basics".
- **Site: scrollbars and phone clean-up.** One slim, theme-coloured scrollbar style for every scroll area (tree, contents, tables, equations, code); on phones no bars at all, edge shadows on sideways-scrolling tables and equations, tags and breadcrumbs wrap instead of being clipped (`style.css`, last blocks).

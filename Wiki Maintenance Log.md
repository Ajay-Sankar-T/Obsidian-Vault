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

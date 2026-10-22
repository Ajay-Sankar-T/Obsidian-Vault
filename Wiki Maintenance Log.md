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

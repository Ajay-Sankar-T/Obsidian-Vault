---
tags: [strength-of-materials, MOC, course]
---

# Strength of Materials — Map of Content

Part of [[Home|Ajay's Engineering Wiki]]. For future LLM-assisted edits, follow [[LLM Wiki Guide]].

Map of content for a standard Strength of Materials / Mechanics of Solids course (AM2200-style). Each numbered folder builds on the previous.

## 01 Stress and Strain
- [[Concept of Stress]]
- [[Stress-Strain Diagram and Hooke's Law]]
- [[Generalized Hooke's Law and Poisson's Ratio]]

## 02 Axial Loading
- [[Axial Deformation]]
- [[Statically Indeterminate Axial Members]]
- [[Thermal Stresses]]

## 03 Torsion
- [[Torsion of Circular Shafts]]
- [[Power Transmission by Shafts]]

## 04 Shear Force and Bending Moment
- [[Shear Force and Bending Moment Diagrams]]
- [[Relations Between Load, Shear, and Moment]]

## 05 Bending Stresses
- [[Flexure Formula]]
- [[Unsymmetric and Combined Bending]]

## 06 Shear Stresses in Beams
- [[Shear Stress Formula for Beams]]

## 07 Transformation of Stress and Strain
- [[Plane Stress Transformation]]
- [[Mohr's Circle for Stress]]
- [[Strain Transformation and Rosettes]]
- [[Stress-Strain Transformation Analogy]] — fast-recall mnemonic layer tying the whole section together

## 08 Deflection of Beams
- [[Double Integration and Macaulay's Method]]
- [[Moment-Area Method]]

## 09 Columns and Buckling
- [[Euler Buckling of Columns]]

## 10 Energy Methods
- [[Strain Energy and Castigliano's Theorem]]

## 11 Thin-Walled Pressure Vessels
- [[Thin Cylindrical and Spherical Pressure Vessels]]

## Tutorials

- [[Tutorial 4 - Stress-Strain Relationship/Tutorial 4 - Stress-Strain Relationship|Tutorial 4 — Stress-Strain Relationship]] (Q1–Q7 + extra problem, all applications of Generalized Hooke's Law):
  - [[Tutorial 4 - Stress-Strain Relationship/Restrained and Confined Deformation|Restrained and Confined Deformation]]
  - [[Tutorial 4 - Stress-Strain Relationship/Composite Members under Axial Load|Composite Members under Axial Load]]
  - [[Tutorial 4 - Stress-Strain Relationship/Principal Stresses to Principal Strains|Principal Stresses to Principal Strains]]
  - [[Tutorial 4 - Stress-Strain Relationship/Thermal Strain in Restrained Plates|Thermal Strain in Restrained Plates]]
  - [[Tutorial 4 - Stress-Strain Relationship/Elongation Under Self-Weight and End Load|Elongation Under Self-Weight and End Load]]
  - [[Tutorial 4 - Stress-Strain Relationship/Two Dissimilar Plates in a Rigid Opening|Two Dissimilar Plates in a Rigid Opening]]

- [[Tutorial 5 - Axial Loading/Q1 - Axially Loaded Member|Tutorial 5 — Axial Loading]] (Statically indeterminate members and complex axial systems):
  - [[Tutorial 5 - Axial Loading/Q1 - Axially Loaded Member|Q1 - Axially Loaded Member]]
  - [[Tutorial 5 - Axial Loading/Q3 - Four-Wire Support System|Q3 - Four-Wire Support System]]
  - [[Tutorial 5 - Axial Loading/Q5 - Self-Weight Pyramid|Q5 - Self-Weight Pyramid]]
  - [[Tutorial 5 - Axial Loading/Q6 - Bolt and Tube Assembly|Q6 - Bolt and Tube Assembly]]
  - [[Tutorial 5 - Axial Loading/Q7 - Massive Bar with Thermal Expansion|Q7 - Massive Bar with Thermal Expansion]]
  - [[Tutorial 5 - Axial Loading/Q8 - Elastically Supported Bar|Q8 - Elastically Supported Bar]]

- [[Tutorial 6 - Torsional Members/Tutorial 6 - Torsional Members|Tutorial 6 — Torsional Members]] (theory + Q1–Q6 in one note: stepped shaft and energy method, tapered bar, misfit between shafts, distributed torque, shrink-fit composite shaft, gear train; figures `assets/SM-T6-*.png`, check script `Tools/sm_t6.py`). Tests [[Torsion of Circular Shafts]], [[Power Transmission by Shafts]], [[Strain Energy and Castigliano's Theorem]].

- [[Tutorial 7 - Bending and Shear Stresses/Tutorial 7 - Bending and Shear Stresses|Tutorial 7 — Bending and Shear Stresses]] (theory + Q1–Q8 in one note: self-weight rod, bimodular beam, diving board, box beam, plywood/pine composite, glued cantilever shear, concrete–steel composite, notched section with unequal allowables; figures `assets/SM-T7-*.png`, check script `Tools/sm_t7.py`). Tests [[Flexure Formula]], [[Shear Stress Formula for Beams]], [[Shear Force and Bending Moment Diagrams]], [[Unsymmetric and Combined Bending]].


## Lab manuals (AM2540)

PDFs in `AM2540 Manuals/` — not yet turned into notes: [[AM2540 Manuals/TENSILE TEST LAB MANUAL.pdf.pdf|Tensile test]] · [[AM2540 Manuals/Tensile Test DIC.pdf|Tensile test with DIC]] · [[AM2540 Manuals/Torsion_manual.pdf|Torsion]] · [[AM2540 Manuals/3 Point Bending.pdf|Three-point bending]] · [[AM2540 Manuals/Buckling of Struts.pdf|Buckling of struts]]. They pair with [[Stress-Strain Diagram and Hooke's Law]], [[Torsion of Circular Shafts]], [[Flexure Formula]] and [[Euler Buckling of Columns]].

## Cross-domain synthesis

Buckling, resonance, energy methods, and stress/strain transformation all turn out to be the same handful of mathematical structures shared with [[EE1100 MOC|EE1100]] (RLC circuits) and [[2nd Order ODEs - MOC|Differential Equations]]. See [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis]] for the eleven explicit connections. Those most relevant here:

- [[Cross-Domain Synthesis/Second Moments of Area - One Integral, Many Jobs|Second Moments of Area — One Integral, Many Jobs]] — $I$, $J$, $EI$, $GJ$, buckling, centre of pressure
- [[Cross-Domain Synthesis/Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids — Pressure, Stress and Constitutive Laws]] — pressure vessels, $G$ vs $\mu$
- [[Cross-Domain Synthesis/Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — equilibrium and compatibility as KCL and KVL
- [[Cross-Domain Synthesis/Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]] — shaft power $P=T\omega$ through a gear train

---
*Note:* the source link (a ChatGPT project page) was private/authenticated and couldn't be scraped, so this structure follows a standard AM2200-style Strength of Materials syllabus instead. If you can paste the actual topic list or lecture PDFs, I can re-align the folders to match exactly.


|     |     |
| --- | --- |
|     |     |

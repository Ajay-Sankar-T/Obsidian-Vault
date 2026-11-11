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
- [[Failure Planes - Ductile and Brittle Fracture]] — where tension, torsion, compression and bending break ductile and brittle specimens, and why

## 08 Deflection of Beams
- [[Double Integration and Macaulay's Method]]
- [[Moment-Area Method]]

## 09 Columns and Buckling
- [[Euler Buckling of Columns]]
- [[Tutorial 9 - Columns|Tutorial 9 — Columns]]: effective length, axis choice, elastic end restraint and stepped columns

## 10 Energy Methods
- [[Strain Energy and Castigliano's Theorem]]

## 11 Thin-Walled Pressure Vessels
- [[Thin Cylindrical and Spherical Pressure Vessels]]

## 12 Formula and Question Bank
- [[Strength of Materials - Formula Bank]] — the whole course on one page: eleven chapters, section properties, standard beam table, column curve, failure criteria, the lab formulas and a "which method?" table
- [[Strength of Materials - Question Bank]] — 48 conceptual questions, 36 solved numerical problems and 24 multiple-choice questions, in four parts:
  - [[Question Bank 1 - Stress, Axial Loading and Torsion]]
  - [[Question Bank 2 - Beams, Bending and Shear]]
  - [[Question Bank 3 - Stress Transformation and Pressure Vessels]]
  - [[Question Bank 4 - Deflection, Energy and Columns]]
- Lab-style mock exams: [[Applied Mechanics Lab - Mock Papers]]

## Tutorials

- [[Tutorial 4 - Stress-Strain Relationship|Tutorial 4 — Stress-Strain Relationship]] (Q1–Q7 + extra problem, all applications of Generalized Hooke's Law):
  - [[Restrained and Confined Deformation|Restrained and Confined Deformation]]
  - [[Composite Members under Axial Load|Composite Members under Axial Load]]
  - [[Principal Stresses to Principal Strains|Principal Stresses to Principal Strains]]
  - [[Thermal Strain in Restrained Plates|Thermal Strain in Restrained Plates]]
  - [[Elongation Under Self-Weight and End Load|Elongation Under Self-Weight and End Load]]
  - [[Two Dissimilar Plates in a Rigid Opening|Two Dissimilar Plates in a Rigid Opening]]

- [[Q1 - Axially Loaded Member|Tutorial 5 — Axial Loading]] (Statically indeterminate members and complex axial systems):
  - [[Q1 - Axially Loaded Member|Q1 - Axially Loaded Member]]
  - [[Q3 - Four-Wire Support System|Q3 - Four-Wire Support System]]
  - [[Q5 - Self-Weight Pyramid|Q5 - Self-Weight Pyramid]]
  - [[Q6 - Bolt and Tube Assembly|Q6 - Bolt and Tube Assembly]]
  - [[Q7 - Massive Bar with Thermal Expansion|Q7 - Massive Bar with Thermal Expansion]]
  - [[Q8 - Elastically Supported Bar|Q8 - Elastically Supported Bar]]

- [[Tutorial 6 - Torsional Members|Tutorial 6 — Torsional Members]] (theory + Q1–Q6 in one note: stepped shaft and energy method, tapered bar, misfit between shafts, distributed torque, shrink-fit composite shaft, gear train; figures `assets/SM-T6-*.png`, check script `Tools/sm_t6.py`). Tests [[Torsion of Circular Shafts]], [[Power Transmission by Shafts]], [[Strain Energy and Castigliano's Theorem]].

- [[Tutorial 7 - Bending and Shear Stresses|Tutorial 7 — Bending and Shear Stresses]] (theory + Q1–Q8 in one note: self-weight rod, bimodular beam, diving board, box beam, plywood/pine composite, glued cantilever shear, concrete–steel composite, notched section with unequal allowables; figures `assets/SM-T7-*.png`, check script `Tools/sm_t7.py`). Tests [[Flexure Formula]], [[Shear Stress Formula for Beams]], [[Shear Force and Bending Moment Diagrams]], [[Unsymmetric and Combined Bending]].

- [[Tutorial 8 - Deflection of Beams|Tutorial 8 — Deflection of Beams]] (theory + Q1–Q8 in one note: two-rod cantilever, couple on a simple beam, singularity-function beams, triangular load by Castigliano, beam on a post with a gap, continuous beam by Castigliano, frame by modified Castigliano; figures `assets/SM-T8-*.png`, check script `Tools/sm_t8.py`). Tests [[Double Integration and Macaulay's Method]], [[Moment-Area Method]], [[Strain Energy and Castigliano's Theorem]].

- [[Tutorial 9 - Columns|Tutorial 9 — Columns]] (theory + Q1–Q5 in one note: control rod BC from lever statics, column AB about two axes with different ends and a factor of safety, fixed–fixed column free to sway, torsional-spring ends $\tan u=-2u$, rigid + elastic halves $\tan ka=-ka$)


## Lab manuals (AM2540)

All seven experiments now have notes in [[Applied Mechanics Lab - MOC]]: [[Lab - Tensile Test on the ES6 Tester|ES6 tensile test]] · [[Lab - Tensile Test of Mild Steel with DIC|tensile test with DIC]] · [[Lab - Torsion of Circular Shafts|torsion]] · [[Lab - Deflection of Beams (Three-Point Bending)|three-point bending]] · [[Lab - Buckling of Struts|buckling of struts]] · [[Lab - Strain Gauge Measurement on a Cantilever Beam|strain gauge on a cantilever]] · [[Lab - Photoelasticity - Fringes and Stress|photoelasticity]]. They pair with [[Stress-Strain Diagram and Hooke's Law]], [[Torsion of Circular Shafts]], [[Flexure Formula]], [[Euler Buckling of Columns]] and [[Mohr's Circle for Stress]]. Exam practice: [[Applied Mechanics Lab - Mock Papers]].

## Cross-domain synthesis

Buckling, resonance, energy methods, and stress/strain transformation all turn out to be the same handful of mathematical structures shared with [[EE1100 MOC|EE1100]] (RLC circuits) and [[2nd Order ODEs - MOC|Differential Equations]]. See [[Cross-Domain Synthesis - MOC|Cross-Domain Synthesis]] for the eleven explicit connections. Those most relevant here:

- [[Second Moments of Area - One Integral, Many Jobs|Second Moments of Area — One Integral, Many Jobs]] — $I$, $J$, $EI$, $GJ$, buckling, centre of pressure
- [[Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids — Pressure, Stress and Constitutive Laws]] — pressure vessels, $G$ vs $\mu$
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — equilibrium and compatibility as KCL and KVL
- [[Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]] — shaft power $P=T\omega$ through a gear train

---
*Note:* the source link (a ChatGPT project page) was private/authenticated and couldn't be scraped, so this structure follows a standard AM2200-style Strength of Materials syllabus instead. If you can paste the actual topic list or lecture PDFs, I can re-align the folders to match exactly.


|     |     |
| --- | --- |
|     |     |

## Continues in
- [[Materials and Design - MOC]] — failure theories, fatigue and fracture build on stress transformation.
- [[Introduction to Machine Design - MOC]] — shafts, springs, bolts and gears sized with these formulas.

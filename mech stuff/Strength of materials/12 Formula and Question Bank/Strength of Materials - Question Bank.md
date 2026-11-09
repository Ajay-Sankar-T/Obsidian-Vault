---
title: Strength of Materials – Question Bank
tags: [strength-of-materials, question-bank, MOC]
up: "[[Strength of Materials - MOC]]"
aliases: [SoM question bank, AM2200 practice questions, strength of materials practice problems]
---

# Strength of Materials — Question Bank

Part of [[Strength of Materials - MOC]] · formulas: [[Strength of Materials - Formula Bank]] · lab-style papers: [[Applied Mechanics Lab - Mock Papers]]

> [!abstract] What it is
> About 100 questions over the whole course: **48 conceptual questions** and **36 numerical problems** with worked solutions in four parts, and **24 multiple-choice questions** on this page. Every numerical answer is computed in `Tools/sm_bank_core.py` (and most were checked a second way: numerical integration, a brute-force sweep or an independent identity). Solutions sit in folds: write your answer first.

## The four parts

| Part | Chapters | Conceptual | Numerical (Q) | Highlights |
|---|---|---|---|---|
| [[Question Bank 1 - Stress, Axial Loading and Torsion]] | 1, 2, 3 | A1–A12 | Q1–Q9 | stepped bar, rigid bar on wires, load plus heating, gap, plane-strain, shaft design, fixed–fixed shaft, composite shaft |
| [[Question Bank 2 - Beams, Bending and Shear]] | 4, 5, 6 | A1–A12 | Q1–Q9 | shear and moment diagrams, contraflexion, T-section in cast iron, I-section shear, transformed section, nails, inclined load, eccentric load, sizing |
| [[Question Bank 3 - Stress Transformation and Pressure Vessels]] | 7, 11 | A1–A12 | Q1–Q8 | Mohr's circle, combined loads with Tresca and von Mises, rosette, gauge on a vessel, joint efficiency, absolute shear |
| [[Question Bank 4 - Deflection, Energy and Columns]] | 8, 9, 10 | A1–A12 | Q1–Q10 | standard deflections, moment-area, overhang, propped cantilever, Macaulay, Castigliano, impact, Euler/Johnson, secant |

![[SM-QB-4-curves.png]]

**Figure** (from Part 4): the three kinds of curve you are asked to draw or read most: an overhang, a Macaulay deflection curve and the stress–load curve of an eccentric column.

## How to use it

1. **Week of the lecture:** do the conceptual questions for the chapter without notes; open a fold only after writing the answer.
2. **Before a tutorial:** do two numericals from the same chapter cold, then check the setup (hint) and the answer.
3. **Revision:** mixed sets from the table below; time each at 15 minutes. If the setup takes more than 3 minutes, re-read the chapter's formula-bank section.
4. **Final week:** the 24 questions below (3 minutes each), then the lab-style papers.

## Which question tests which skill

| Skill | Where |
|---|---|
| Internal force, then $\sum PL/AE$ | QB1 Q1, Q5 |
| Compatibility with a rigid body or a gap | QB1 Q2, Q4 |
| Two materials, load and temperature | QB1 Q3, Q9, QB2 Q5 |
| Shaft sizing by strength **and** twist | QB1 Q7 |
| Indeterminate torsion | QB1 Q8 |
| Diagrams from $dV/dx=-w$, $dM/dx=V$ | QB2 Q1, Q2 |
| Which way up is the section? | QB2 Q3 |
| $VQ/It$ and shear flow | QB2 Q4, Q6 |
| Biaxial or eccentric bending | QB2 Q7, Q8 |
| Transformation and Mohr's circle | QB3 Q1, Q7, Q8 |
| Failure theories on a shaft | QB3 Q2 |
| Strain gauge $\to$ stress | QB3 Q3, Q4 |
| Pressure-vessel design | QB3 Q4, Q5, Q6 |
| Slope and deflection of beams | QB4 Q1–Q5 |
| Energy: Castigliano, impact | QB4 Q6, Q7 |
| Column: which formula? | QB4 Q8, Q9, Q10 |

## Errors that cost marks (all chapters)

| Error | Fix |
|---|---|
| Using the external load as the force in every segment | cut and balance: the internal force changes at every load |
| Thermal stress without checking whether expansion is restrained | free expansion gives zero stress; compare with the gap |
| Strength design only for a shaft | also check twist, take the larger diameter |
| Maximum moment placed under the point load | it is where $V=0$ |
| One $I$ for both axes | the neutral axis moves for a composite or unsymmetric section |
| Wrong $Q$ in $VQ/It$ | the first moment of the area **beyond** the level, about the neutral axis of the whole section |
| Dropping $\sigma_3=0$ when finding the maximum shear | order all three principal stresses |
| Mixing the signs of $\tau_{xy}$ and the Mohr's-circle plotting direction | check one plane by direct substitution |
| $\sigma=pr/2t$ for the hoop stress | hoop is $pr/t$, longitudinal $pr/2t$ |
| Adding strain energies of two loads | add the deflections instead |
| Euler without checking $\lambda$ | compute $\lambda$ and $\lambda_c$ first |
| Using $E_{\rm steel}=200$ for one half and $210$ for the other | state one value and keep it |

## 24 quick-fire multiple choice questions

> [!question]- 1. The diameter of a bar under a fixed axial load is doubled. The elongation becomes: (a) $\tfrac12$ (b) $\tfrac14$ (c) $\tfrac1{16}$ (d) unchanged
> **(b).** $\delta=PL/AE$ and $A\propto d^2$.

> [!question]- 2. Poisson's ratio of a perfectly incompressible material: (a) 0 (b) 0.25 (c) 0.5 (d) 1
> **(c).** $K=E/3(1-2\nu)\to\infty$ as $\nu\to0.5$.

> [!question]- 3. A steel bar fixed rigidly at both ends is heated by $\Delta T$. The stress is: (a) $E\alpha\Delta T$ tension (b) $E\alpha\Delta T$ compression (c) zero (d) $\alpha\Delta T/E$
> **(b).** The bar wants to expand and is held: compression, $\sigma=E\alpha\Delta T$.

> [!question]- 4. A solid shaft's diameter is halved at the same torque. The maximum shear stress becomes: (a) $2\times$ (b) $4\times$ (c) $8\times$ (d) $16\times$
> **(c).** $\tau\propto1/d^3$. (The twist grows $16\times$.)

> [!question]- 5. For the same material, length and mass, a hollow shaft compared with a solid one has: (a) lower $J$ (b) the same $J$ (c) higher $J$ (d) lower strength
> **(c).** The material is farther from the axis, so $J$ is higher (and strength is higher).

> [!question]- 6. The slope of the shear-force diagram at a point equals: (a) $M$ (b) $-w$ (c) $+w$ (d) $dM/dx$
> **(b).** $dV/dx=-w$.

> [!question]- 7. Maximum bending moment of a simply supported beam of span $L$ with a central point load $P$: (a) $PL/2$ (b) $PL/4$ (c) $PL/8$ (d) $PL$
> **(b).**

> [!question]- 8. The ratio of maximum to average shear stress for a rectangular section: (a) 1.0 (b) 1.33 (c) 1.5 (d) 2.0
> **(c).** (Circle 1.33, thin tube 2.)

> [!question]- 9. Section modulus of a solid circular section of diameter $d$: (a) $\pi d^3/16$ (b) $\pi d^3/32$ (c) $\pi d^4/64$ (d) $\pi d^2/4$
> **(b).** $I/c=(\pi d^4/64)/(d/2)$. ($\pi d^3/16$ is the *polar* modulus.)

> [!question]- 10. The shear stress on a rectangular beam section is zero at: (a) the neutral axis (b) the top and bottom fibres (c) the centroid (d) nowhere
> **(b).** It is maximum at the neutral axis, zero at the free surfaces.

> [!question]- 11. For pure shear $\tau$, the principal stresses are: (a) $\tau,\tau$ (b) $\tau,-\tau$ (c) $2\tau,0$ (d) $0,0$
> **(b).** On planes at $45^\circ$; the Mohr's circle is centred at the origin with radius $\tau$.

> [!question]- 12. In a thin cylindrical vessel the ratio $\sigma_{hoop}/\sigma_{long}$ is: (a) 0.5 (b) 1 (c) 2 (d) 4
> **(c).** $pr/t$ against $pr/2t$.

> [!question]- 13. For equal $r$, $p$ and allowable stress, a spherical vessel needs a wall of ___ the cylinder's: (a) $1/4$ (b) $1/2$ (c) equal (d) twice
> **(b).**

> [!question]- 14. Tip deflection of a cantilever with a UDL $w$ over its length $L$: (a) $wL^4/3EI$ (b) $wL^4/8EI$ (c) $5wL^4/384EI$ (d) $wL^3/6EI$
> **(b).** ((d) is the slope.)

> [!question]- 15. Changing a pin-ended column to fixed–fixed ends multiplies the Euler load by: (a) 2 (b) 3 (c) 4 (d) 0.5
> **(c).** $K=1\to0.5$, $P\propto1/K^2$.

> [!question]- 16. The slenderness ratio of a column is: (a) $L/A$ (b) $KL/r$ (c) $KL/I$ (d) $r/L$
> **(b).**

> [!question]- 17. By Castigliano's second theorem, the deflection of the load point in the load direction is: (a) $\partial U/\partial P$ (b) $U/P$ (c) $\partial P/\partial U$ (d) $2U/P$
> **(a).** (For a linear structure $U=\tfrac12P\delta$ gives $2U/P$ for a single load, which is also correct, but (a) is the general statement.)

> [!question]- 18. A load applied suddenly (not impacting) produces a stress of ___ the static value: (a) 1 (b) 1.5 (c) 2 (d) 4
> **(c).**

> [!question]- 19. A free steel bar is uniformly heated. The thermal stress is: (a) $E\alpha\Delta T$ (b) $E\alpha\Delta T/2$ (c) zero (d) $\alpha\Delta T$
> **(c).** No restraint, no stress.

> [!question]- 20. Gauge factor is defined as: (a) $\varepsilon/(\Delta R/R)$ (b) $(\Delta R/R)/\varepsilon$ (c) $\Delta R/\varepsilon$ (d) $R\varepsilon$
> **(b).** About 2 for foil gauges.

> [!question]- 21. A brittle shaft in torsion cracks along: (a) the cross-section (b) a $45^\circ$ helix (c) the axis (d) a $90^\circ$ helix
> **(b).** Perpendicular to the maximum tensile stress, see [[Failure Planes - Ductile and Brittle Fracture]].

> [!question]- 22. In the diametral compression of a polymer disk, if the material fringe value $f_\sigma$ is halved at the same load, the number of fringes: (a) halves (b) is unchanged (c) doubles (d) cannot be predicted
> **(c).** $N=8P/(\pi Df_\sigma)$.

> [!question]- 23. A circle and a square of the **same area** are columns of equal length, material and ends. Which has the higher Euler load? (a) circle (b) square (c) equal (d) depends on $E$
> **(b).** For equal area, $I_{circle}=A^2/4\pi=0.0796A^2$ and $I_{square}=A^2/12=0.0833A^2$: the square is higher by $\pi/3=1.05$. **Trap:** for equal **perimeter** the circle wins, because it encloses more area ($I_{circle}=P^4/64\pi^3$ against $P^4/3072$ for the square: ratio 1.55). Read which quantity is held equal.

> [!question]- 24. A simply supported beam's central deflection when the depth of a rectangular section is doubled (same width, load, span): (a) $/2$ (b) $/4$ (c) $/8$ (d) $/16$
> **(c).** $I\propto h^3$.

## Related
[[Strength of Materials - MOC]] · [[Strength of Materials - Formula Bank]] · [[Applied Mechanics Lab - Mock Papers]] · the same layout for fluids: [[Fluid Mechanics - MOC]]

---
tags: [strength-of-materials, tutorial, stress-strain]
up: "[[Strength of materials/Strength Of Materials - MOC]]"
---

# Tutorial 4 — Stress-Strain Relationship

← up: [[Strength of Materials - MOC|Strength of Materials MOC]] · builds on: [[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]]

Seven questions (Q1–Q7), plus an extra two-material plate problem, that together are almost entirely **applications** of the [[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law]] matrix — the theory itself doesn't change from problem to problem; only *which stresses/strains are known, zero, or coupled by a constraint* changes. This tutorial is best read as a catalogue of the ways that matrix equation gets specialized.

## The three principles behind every problem here

$$\boxed{\text{Equilibrium}}\qquad\boxed{\text{Compatibility}}\qquad\boxed{\text{Constitutive law (Hooke)}}$$

Every question below is a different combination of these three — exactly the same triad used throughout [[Statically Indeterminate Axial Members|Statically Indeterminate Axial Members]] and [[Strain Energy and Castigliano's Theorem|Castigliano's Theorem]].

## Question map

| Q | Topic | Note |
|---|---|---|
| Q1 | Basic stress/strain/Hooke's law definitions | [[Generalized Hooke's Law and Poisson's Ratio\|Generalized Hooke's Law and Poisson's Ratio]] |
| Q2 | Block under pressure, varying restraint | [[Restrained and Confined Deformation\|Restrained and Confined Deformation]] |
| Q3 | Fully confined rubber block, effective modulus | [[Restrained and Confined Deformation\|Restrained and Confined Deformation]] |
| Q4 | Composite brass/aluminium member | [[Composite Members under Axial Load\|Composite Members under Axial Load]] |
| Q5 | Principal stresses → principal strains | [[Principal Stresses to Principal Strains\|Principal Stresses to Principal Strains]] |
| Q6 | Heated plate in a rigid oversized opening | [[Thermal Strain in Restrained Plates\|Thermal Strain in Restrained Plates]] |
| Q7 | Elongation under end load + self-weight | [[Elongation Under Self-Weight and End Load\|Elongation Under Self-Weight and End Load]] |
| extra | Two dissimilar plates in a rigid opening | [[Two Dissimilar Plates in a Rigid Opening\|Two Dissimilar Plates in a Rigid Opening]] |

## The golden rule that resolves half the ambiguity in this tutorial

$$\boxed{\text{Restricted deformation}\Rightarrow\varepsilon=0}\qquad\qquad\boxed{\text{Free direction}\Rightarrow\sigma=0}$$

These are **not** interchangeable, and confusing them is the single most common error in this tutorial: a restrained direction generally still develops nonzero stress (the restraint is exactly what *causes* the stress, via Poisson coupling to the other directions), while a free direction genuinely carries zero stress but may still deform (via Poisson effect from stress in the other directions).

## Master problem-solving algorithm

1. **Identify axes** $x,y,z$ and draw the loading.
2. **Identify what is known** — e.g. an applied pressure $\sigma_z=-p$, or an applied load $P$.
3. **Classify each remaining direction:** free ($\sigma=0$) or restrained ($\varepsilon=0$) — per the golden rule above.
4. **Write Hooke's law** for each direction: $\varepsilon_i=\dfrac1E[\sigma_i-\nu(\sigma_j+\sigma_k)]$.
5. **Apply equilibrium** ($\sum F=0$) where multiple members/parts share a load.
6. **Apply compatibility** ($\delta_1=\delta_2$ or $\varepsilon_1=\varepsilon_2$) where parts are rigidly connected.
7. **Solve** the resulting system for the unknown stresses/strains.
8. **Check signs**: positive stress = tension, negative = compression; positive strain = expansion, negative = contraction.

## Related
- [[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]]
- [[Statically Indeterminate Axial Members|Statically Indeterminate Axial Members]] (the same equilibrium+compatibility+Hooke procedure, one level simpler)
- [[Thermal Stresses|Thermal Stresses]]

## See also
- [[Q1 - Axially Loaded Member]] — equilibrium + compatibility + constitutive law in the axial sheet.

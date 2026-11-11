---
tags: [strength-of-materials, stress-strain, composite-members]
up: "[[Tutorial 4 - Stress-Strain Relationship]]"
---

# Two Dissimilar Plates in a Rigid Opening

← up: [[Tutorial 4 - Stress-Strain Relationship|Tutorial 4]] · builds on: [[Composite Members under Axial Load|Composite Members under Axial Load]]

## Setup

Two square plates of side $a$, materials $(E_1,\nu_1)$ and $(E_2,\nu_2)$, placed side by side (frictionless contact) inside a rigid opening of width $l<2a$ — the plates are oversized and must be compressed to fit.

```text
   ┌───────── l (opening) ─────────┐
   │←────a────→│←────a────→│
   ├────────────┼────────────┤
   │  Plate 1   │  Plate 2   │      2a > l  → both plates compressed
   │  E1, ν1    │  E2, ν2    │      frictionless interface (normal force only)
   └────────────┴────────────┘
```

## Why this is the equal-*stress* counterpart of the composite member

In [[Composite Members under Axial Load|Composite Members under Axial Load]], a rigid end plate forced **equal strain** on both materials. Here, the frictionless interface transmits **normal force but no shear**, and since both plates have the same cross-sectional area in contact, equilibrium (force balance across the interface) forces:

$$\boxed{\sigma_1=\sigma_2=\sigma}\qquad\text{but}\qquad\boxed{\varepsilon_1\ne\varepsilon_2}\quad\left(\varepsilon_i=\frac{\sigma}{E_i}\right)$$

— the mirror image of the composite-member case: there, stress differed while strain was shared; here, strain differs while stress is shared. This equal-stress/equal-strain duality is the same distinction as **series vs parallel** in circuit elements (see the cross-domain note below).

## Compatibility

The total forced contraction must equal the total oversize $2a-l$:

$$\boxed{\Delta a_1+\Delta a_2=l-2a}\ (\text{a negative quantity, since }2a>l)$$

with $\Delta a_1=a\sigma/E_1$, $\Delta a_2=a\sigma/E_2$ (both compressive, i.e. negative $\sigma$). Substituting and solving:

$$\boxed{\sigma=-\frac{E_1E_2}{E_1+E_2}\cdot\frac{2a-l}{a}}$$

— note the **harmonic-mean-like** combination $\dfrac{E_1E_2}{E_1+E_2}$ (an equal-stress/series-style combination), in contrast to the **arithmetic** combination $E_1A_1+E_2A_2$ that appeared for the equal-strain/parallel-style composite member.

## Individual plate contractions

$$\boxed{\Delta a_1=-\frac{E_2}{E_1+E_2}(2a-l)},\qquad\boxed{\Delta a_2=-\frac{E_1}{E_1+E_2}(2a-l)}$$

The plate with the **smaller** $E$ undergoes the **larger** deformation — the softer material yields more to accommodate the same shared stress, exactly as the more compliant (larger reactance) element in a series circuit carries a larger share of the total voltage drop for the same current.

## Poisson expansion in the unconstrained (vertical) direction

Each plate's compressive strain in the loaded direction produces a lateral (vertical) expansion via Poisson's ratio:

$$\boxed{\Delta b_1=\nu_1\frac{E_2}{E_1+E_2}(2a-l)},\qquad\boxed{\Delta b_2=\nu_2\frac{E_1}{E_1+E_2}(2a-l)}$$

directly from $\varepsilon_{\rm lateral}=-\nu\varepsilon_{\rm longitudinal}$ ([[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]]) applied to each plate's own $\Delta a_i/a$.

## Cross-domain: series vs parallel, mechanically

This equal-stress ("series") vs the composite member's equal-strain ("parallel") duality is *exactly* the electrical series/parallel distinction under [[The Mechanical-Electrical Analogy (Impedance Analogy)|The Mechanical-Electrical Analogy]]: two mechanical "compliances" (elements sharing the same force, i.e. the same stress here) combine like impedances in **series** ($Z_{\rm eq}=Z_1+Z_2$, mirrored here by the $E_1E_2/(E_1+E_2)$ combination, which is precisely the "reciprocal of sum of reciprocal-stiffnesses" rule — springs in series), while two elements sharing the same displacement (equal strain, the composite-member case) combine like impedances in **parallel** ($Y_{\rm eq}=Y_1+Y_2$, mirrored by $E_1A_1+E_2A_2$ — springs in parallel). Recognizing "do these share force or displacement?" is the mechanical-mechanics version of recognizing "do these share current or voltage?" before combining circuit elements.

## Related
- [[Composite Members under Axial Load|Composite Members under Axial Load]]
- [[The Mechanical-Electrical Analogy (Impedance Analogy)|Cross-Domain: The Mechanical-Electrical Analogy]]

## See also
- [[Tutorial 6 - Torsional Members]] — series and parallel statically indeterminate torsion.

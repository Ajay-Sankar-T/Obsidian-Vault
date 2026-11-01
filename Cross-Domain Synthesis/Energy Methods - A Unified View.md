---
tags: [synthesis, cross-domain, energy-methods, castigliano]
up: "[[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC]]"
---

# Energy Methods — A Unified View

← up: [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]

## Same integral, three notations

[[Strength of materials/10 Energy Methods/Strain Energy and Castigliano's Theorem|Strain Energy and Castigliano's Theorem]]'s table of $U$ for axial/torsion/bending loading all share the structure

$$U = \frac{(\text{stress resultant})^2 \times \text{length}}{2\times\text{stiffness}}$$

Compare directly with the electrical energy-storage terms implicit in [[Cross-Domain Synthesis/The Mechanical-Electrical Analogy (Impedance Analogy)|The Mechanical-Electrical Analogy]]:

$$U_L=\frac{1}{2}Li^2,\qquad U_C=\frac{1}{2}Cv^2=\frac{q^2}{2C}$$

$U_C=q^2/(2C)$ is *literally* the same shape as $U=N^2L/(2AE)$ — a "flow-like" quantity squared, over twice a stiffness-like constant. This isn't coincidence: both come from integrating a linear constitutive law ($\sigma=E\varepsilon$ or $v=q/C$) against its own conjugate variable, i.e. both are $\int(\text{effort})\,d(\text{displacement})$ for a linear spring-like element — see [[Strength of materials/01 Stress and Strain/Stress-Strain Diagram and Hooke's Law|Stress-Strain Diagram and Hooke's Law]]'s modulus-of-resilience definition $u=\sigma^2/2E$, which is exactly $U_C=q^2/2C$ with $\sigma\leftrightarrow q$ and $E\leftrightarrow1/C$ (i.e. $E$ plays the role of an *elastance*, not a capacitance — matching the stiffness/elastance pairing already found in the impedance-analogy note).

## Castigliano's theorem *is* a small-signal AC sensitivity, generalized

[[Strength of materials/10 Energy Methods/Strain Energy and Castigliano's Theorem|Strain Energy and Castigliano's Theorem]]'s $\delta_i=\partial U/\partial P_i$ finds a displacement by differentiating stored energy with respect to a load. There's no electrical note in your vault that states the direct circuit analogue, but it exists and is worth having explicitly: for a linear reciprocal network, the same partial-derivative trick recovers a **Thevenin-equivalent relationship** — differentiating total stored energy $U=\tfrac12LI^2+\tfrac12CV^2$ with respect to a source parameter gives the sensitivity of that source's own terminal variable to itself, which is exactly how self- and mutual-inductance/capacitance are *defined* in energy terms in more advanced treatments (energy method for computing $L$ and $M$ in magnetically coupled circuits — directly relevant to [[08 Resonance and Magnetically Coupled Circuits|Week 8]]'s magnetic coupling, which currently states $M$ and $k$ without deriving them from energy).

## The genuinely new theorem you can now state

**Castigliano's theorem for maximum power transfer.** [[Thevenin, Norton and Maximum Power Transfer (AC)|Thevenin, Norton and Maximum Power Transfer (AC)]] derives $Z_L=Z_{\rm Th}^{*}$ by an impedance argument. It can equally be derived as a **Castigliano-style stationarity condition**: treat average power delivered to the load as a function $P(R_L,X_L)$ of the two load parameters, and set $\partial P/\partial R_L=0$, $\partial P/\partial X_L=0$ simultaneously. This is *exactly* the same "set the partial derivative of the energy-like functional to zero" move as Castigliano's first theorem, $\partial U/\partial R=0$, used in [[Strength of materials/10 Energy Methods/Strain Energy and Castigliano's Theorem|Strain Energy and Castigliano's Theorem]] to solve statically indeterminate structures. In both cases: a physical extremum (max power delivered; zero displacement at a redundant support) is found by differentiating a scalar energy/power functional with respect to a free parameter and setting the result to zero — the calculus-of-variations principle underlying *both* fields, usually taught as two unrelated "tricks" but actually one idea (a discrete instance of the principle of stationary/least action / Castigliano's theorems being a special case of the more general variational principles that also produce Maxwell's reciprocity and Rayleigh-Ritz).

## Related
- [[Strength of materials/10 Energy Methods/Strain Energy and Castigliano's Theorem|Strain Energy and Castigliano's Theorem]]
- [[Cross-Domain Synthesis/The Mechanical-Electrical Analogy (Impedance Analogy)|The Mechanical-Electrical Analogy]]
- [[Thevenin, Norton and Maximum Power Transfer (AC)|Thevenin, Norton and Maximum Power Transfer (AC)]]

## Cross-domain links
- [[Foundations of Thermal Engineering - MOC]] — exergy is the available-work form of the second law: the most useful work obtainable relative to the dead state.
- [[Tutorial 8 - Deflection of Beams]] — Castigliano's theorem worked on beams, a frame and a continuous beam.

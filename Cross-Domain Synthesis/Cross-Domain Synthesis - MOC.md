---
tags: [synthesis, cross-domain, MOC]
---

# Cross-Domain Synthesis — Map of Content

Part of [[Home|Ajay's Engineering Wiki]]. For future LLM-assisted edits, follow [[LLM Wiki Guide]].

Your vault has three technical domains that were built separately — [[Differential Equations - MOC|Differential Equations]], [[Strength of Materials - MOC|Strength of Materials]], and [[EE1100 MOC|EE1100 Basic Electrical Engineering]] (with [[Fluid Mechanics - MOC|Fluid Mechanics]] joining at the edges) — but they are, underneath, the **same handful of mathematical structures wearing different units**. This folder makes those structures explicit: not just "these look similar" but the actual shared theorem, the actual shared matrix, the actual shared physical mechanism, and — in a few places — a genuine new-to-you observation that falls out once you line the three domains up side by side.

## The six syntheses

1. [[The Universal Second-Order Linear System|The Universal Second-Order Linear System]] — RLC circuits, column buckling, and every damped oscillator are literally the same ODE.
2. [[The Mechanical-Electrical Analogy (Impedance Analogy)|The Mechanical-Electrical Analogy]] — a dictionary that turns any circuit theorem into a structural-mechanics theorem and vice versa.
3. [[Eigenvalues, Rotation and Diagonalization Everywhere|Eigenvalues, Rotation and Diagonalization Everywhere]] — principal stresses, phasor rotation by $j$, and Mohr's circle are one linear-algebra fact in three costumes.
4. [[Exponential Decay - Time Constants, Damping and Spatial Relaxation|Exponential Decay — Time Constants, Damping and Spatial Relaxation]] — $\tau=RC$, damping ratio $\zeta$, and Saint-Venant's principle are all "how fast does the homogeneous solution die."
5. [[Energy Methods - A Unified View|Energy Methods — A Unified View]] — Castigliano's theorem and circuit energy storage are the same calculus-of-variations move.
6. [[Resonance and Buckling - Instability as an Eigenvalue Problem|Resonance and Buckling — Instability as an Eigenvalue Problem]] — $P_{cr}$ and $\omega_0$ are both the point where a boundary-value problem's homogeneous solution stops being negligible.

## Added 2026-10-08: KDoMs, Fluid Mechanics and the recurring structures

7. [[Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]] — gear trains, ideal transformers and DC motors as lossless two-ports; reflected inertia = reflected impedance; the matching condition.
8. [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics|Rotating Vectors — Phasors, Velocity Polygons and Complex Kinematics]] — $d/dt\to j\omega$; loop closure = KVL; the acceleration image has an impedance angle.
9. [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — KCL, continuity and equilibrium; KVL, Bernoulli and compatibility; hydraulic and structural analogies.
10. [[Second Moments of Area - One Integral, Many Jobs|Second Moments of Area — One Integral, Many Jobs]] — bending, torsion, buckling, centre of pressure, metacentre, rotational inertia; Mohr's circle for inertia.
11. [[Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids — Pressure, Stress and Constitutive Laws]] — pressure as isotropic stress, hoop stress from projected area, $G$ vs $\mu$, Deborah number as a Maxwell time constant.

### Recurring structures → where each lives

| Structure | Synthesis |
|---|---|
| linear ODEs, resonance, stability | 1, 6 |
| impedance | 2, 7 |
| eigenvalue problems, rank-1 vs rank-2 | 3, 8, 10 |
| time constants | 4, 11 |
| energy methods | 5, 7, 9 |
| conservation laws | 9 |
| second moments | 10 |
| transformations / reflected quantities | 7 |

## How to read these

Each note names the *exact* existing notes it's connecting (with links), states the shared mathematical object precisely (not just "similar vibes"), and then draws out at least one consequence that isn't obvious from either domain alone — the kind of thing you'd only notice by holding both subjects in your head at once.

## Related
- [[2nd Order ODEs - MOC|2nd Order ODEs — MOC]]
- [[Differential Equations - MOC|Differential Equations — MOC]]
- [[Strength of Materials - MOC|Strength of Materials — MOC]]
- [[EE1100 MOC|EE1100 — MOC]]
- [[Fluid Mechanics - MOC|Fluid Mechanics — MOC]]
- [[KDoMs - MOC|KDoMs — MOC]]

---
tags: [fluid-mechanics, dimensionless-numbers]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Knudsen Number

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · governs: [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Continuum Concept|Continuum Concept]]

## Definition

$$\boxed{Kn=\frac{\lambda}{L}}$$

- $\lambda$ — mean free path: the average distance a molecule travels between successive collisions
- $L$ — characteristic length of the flow/problem

**Memory:** $Kn=\dfrac{\text{molecular scale}}{\text{flow scale}}$ — it directly measures how "grainy" the fluid looks relative to the size of the thing you're studying.

## Flow regimes

| $Kn$ | Regime | Meaning |
|---|---|---|
| $<0.01$ | Continuum | molecular graininess totally negligible — [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Continuum Concept\|continuum hypothesis]] fully valid |
| $0.01$–$0.1$ | Slip flow | continuum equations mostly valid, but need modified (slip) boundary conditions at walls |
| $0.1$–$10$ | Transitional | neither continuum PDEs nor free-molecular kinetic theory alone is accurate |
| $>10$ | Free molecular | molecules travel so far between collisions that they interact with boundaries more than with each other — must use kinetic theory, not continuum PDEs |

## Why $L$, not just $\lambda$, controls the regime

The mean free path $\lambda$ for a given gas at fixed temperature and pressure is essentially fixed (roughly 68 nm for air at sea level). What changes $Kn$ in practice is $L$ — a full-scale aircraft has $Kn\ll0.01$ (continuum, ordinary aerodynamics applies), while a MEMS micro-channel or a spacecraft in the upper atmosphere can have $L$ small/large enough to push $Kn$ into the slip or free-molecular regime **for the same air**. This is the same reclassification logic as [[Fluid Mechanics/01 Dimensionless Numbers/Deborah Number|Deborah Number]]'s regime table: the *substance's* own microscopic property ($\lambda$, or $\lambda$ the relaxation time) stays fixed, and it is the *problem's own scale* ($L$, or $t_{\rm flow}$) that determines which physical model applies.

## Related
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Continuum Concept|Continuum Concept]]
- [[Fluid Mechanics/01 Dimensionless Numbers/Deborah Number|Deborah Number]]
- [[Fluid Mechanics/01 Dimensionless Numbers/Buckingham Pi Theorem|Buckingham π Theorem]] — $Kn$ is one instance of the general $n-r$ dimensionless-group construction

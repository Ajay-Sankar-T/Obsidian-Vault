---
tags: [synthesis, cross-domain, ODE, RLC, buckling]
up: "[[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC]]"
---

# The Universal Second-Order Linear System

← up: [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]

## The shared equation

Three notes in three different vaults independently write down the same ODE:

$$a\ddot x + b\dot x + cx = f(t)\qquad\Longleftrightarrow\qquad s^2+2\alpha s+\omega_n^2=0$$

| Domain | Note | Physical variable $x$ | $a$ | $b$ | $c$ |
|---|---|---|---|---|---|
| Circuits | [[Second-Order AC Transients (Series and Parallel RLC)\|Second-Order AC Transients]] | current $i$ (series RLC) | $L$ | $R$ | $1/C$ |
| Structures | [[Strength of materials/09 Columns and Buckling/Euler Buckling of Columns\|Euler Buckling of Columns]] | lateral deflection $v$ | $EI$ | $0$ | $P$ |
| Pure math | [[2nd Order Linear ODE with Constant Coefficients\|2nd Order Linear ODE with Constant Coefficients]] | abstract $y$ | any | any | any |

## Where this is genuinely surprising

The buckling equation $EI\,v''+Pv=0$ has **zero damping term** ($b=0$) — it looks like a pure oscillator in *space* rather than time, and indeed its solution $v(x)=A\sin(kx)+B\cos(kx)$, $k=\sqrt{P/EI}$, is undamped. But the *RLC* equation is a decaying oscillator in time. These look unrelated until you notice: **buckling's independent variable is a spatial coordinate with fixed boundary conditions at both ends** ($v(0)=v(L)=0$), exactly like a vibrating string or an undamped LC circuit with boundary conditions instead of initial conditions. The "damping" term $R$ in the electrical case has no structural analogue in buckling because buckling has no dissipation mechanism built into the idealized model — the analogous term would be a distributed lateral elastic foundation or internal material damping, which real column-on-elastic-foundation problems do include (Winkler foundation: $EIv''''+kv=q$, a fourth-order cousin).

The deep point: **both problems are eigenvalue problems**, not initial-value problems, even though the RLC "characteristic equation" language usually gets taught as an IVP technique. Requiring $v(0)=v(L)=0$ with a nontrivial solution forces $\sin(kL)=0$, i.e. $kL=n\pi$ — this is *identical in structure* to requiring a homogeneous linear system to have a nontrivial solution, i.e. $\det(A-\lambda I)=0$. $P_{cr}$ is literally an eigenvalue of the differential operator $EI\,d^2/dx^2$ subject to Dirichlet boundary conditions. See [[Cross-Domain Synthesis/Resonance and Buckling - Instability as an Eigenvalue Problem|Resonance and Buckling — Instability as an Eigenvalue Problem]] for the parallel with electrical resonance.

## The damping ratio $\zeta$ as a universal classifier

$$\zeta = \frac{\alpha}{\omega_n}$$

reappears with the *same three qualitative regimes* everywhere this equation shows up:

| $\zeta$ | RLC ([[Second-Order AC Transients (Series and Parallel RLC)\|link]]) | Would-be mechanical analogue |
|---|---|---|
| $\zeta>1$ | overdamped — current creeps back with no oscillation | overdamped spring-mass-damper (heavy damper) |
| $\zeta=1$ | critically damped — fastest non-oscillatory return | critical damping (shock absorbers are tuned here) |
| $\zeta<1$ | underdamped — decaying sinusoid at $\omega_d=\sqrt{\omega_n^2-\alpha^2}$ | underdamped vibration |

Nothing in the Strength of Materials vault currently models a *damped* vibrating structure (only static buckling), but the vault's [[Strength of materials/10 Energy Methods/Strain Energy and Castigliano's Theorem|Strain Energy and Castigliano's Theorem]] note already sets up exactly the energy machinery ($U=\int M^2/2EI\,dx$) that a Rayleigh-Ritz vibration analysis would need to estimate a structure's own $\omega_n$ — the natural next topic if you ever add beam vibration to that vault, and it would import this damping-ratio table unchanged.

## Consequence you probably didn't have before

Because $P_{cr}=\pi^2EI/L^2$ and $\omega_0=1/\sqrt{LC}$ are computed by the *same* "smallest eigenvalue of a linear operator" logic, the design lever is structurally identical in both fields: **you cannot fix an instability problem by making the material stronger — you can only fix it by changing the operator's coefficients ($EI$, or $L,C$).** [[Strength of materials/09 Columns and Buckling/Euler Buckling of Columns|Euler Buckling of Columns]] already states this for columns ("buckling load depends on $EI$, not material strength"); the electrical mirror is that a circuit's resonant frequency depends only on $L,C$, never on $R$ or on how "strong" (high-power-rated) the resistor is — $R$ only controls the *damping*, exactly as a column's damping (if it had any) wouldn't move $P_{cr}$ either.

## Related
- [[Cross-Domain Synthesis/Resonance and Buckling - Instability as an Eigenvalue Problem|Resonance and Buckling — Instability as an Eigenvalue Problem]]
- [[Cross-Domain Synthesis/Exponential Decay - Time Constants, Damping and Spatial Relaxation|Exponential Decay — Time Constants, Damping and Spatial Relaxation]]
- [[2nd Order Linear ODE with Constant Coefficients|2nd Order Linear ODE with Constant Coefficients]]

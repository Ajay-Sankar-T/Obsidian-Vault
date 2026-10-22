---
tags: [synthesis, cross-domain, exponential-decay, time-constant, saint-venant]
up: "[[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC]]"
---

# Exponential Decay — Time Constants, Damping and Spatial Relaxation

← up: [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]

## The pattern

Three completely different-looking statements in your vault are the same mathematical fact — a linear first-order homogeneous ODE has solution $e^{-t/\tau}$, and the coefficient always has the form (dissipative quantity)/(storage quantity):

| Domain | Note | Decay constant | "Storage" term | "Dissipative" term |
|---|---|---|---|---|
| Circuits | [[First-Order AC Transients (RC and RL)\|First-Order AC Transients]] | $\tau=RC$ or $\tau=L/R$ | $C$ or $L$ | $R$ |
| Structures | [[Strength of materials/02 Axial Loading/Axial Deformation\|Axial Deformation]]'s Saint-Venant's principle | (spatial, not temporal — see below) | geometric stiffness | localized stress concentration |
| Pure math | [[2nd Order Linear ODE with Constant Coefficients\|2nd Order Linear ODE]] | root of characteristic equation | — | — |

## Saint-Venant's principle *is* an exponential decay law — just in space

[[Strength of materials/02 Axial Loading/Axial Deformation|Axial Deformation]] mentions Saint-Venant's principle only qualitatively (stress concentrations near a load smooth out "away from" the load). What's not stated there, but is true and is the useful cross-domain fact: for many elasticity problems, the *rate* at which a self-equilibrated local stress disturbance decays with distance $x$ from its source is genuinely exponential, $\sigma(x)\sim\sigma_0e^{-x/\ell}$, where $\ell$ is a **decay length set by the cross-section's own geometry** (roughly the member's depth/width) — this is the direct spatial analogue of the *temporal* decay in [[First-Order AC Transients (RC and RL)|First-Order AC Transients]], with distance playing the role of time and cross-sectional geometry playing the role of $RC$ or $L/R$. In both cases, **the decay constant depends only on the system's own "storage geometry," never on the size of the initial disturbance** — a 10× larger point load decays over the *same* distance $\ell$, just from a larger $\sigma_0$, exactly as a 10× larger initial capacitor voltage decays over the same $\tau=RC$.

## Damping ratio $\zeta$ as decay-rate-relative-to-oscillation-rate

[[Second-Order AC Transients (Series and Parallel RLC)|Second-Order AC Transients]]'s $\zeta=\alpha/\omega_n$ is a *dimensionless ratio of two rates*: how fast the envelope decays ($\alpha$) versus how fast the system would oscillate if undamped ($\omega_n$). This exact ratio-of-rates idea is implicit but never named in [[Strength of materials/09 Columns and Buckling/Euler Buckling of Columns|Euler Buckling of Columns]]'s slenderness ratio $KL/r$: slenderness is a ratio of *how far the load has to act* ($KL$) to *how resistant the cross-section is to bending* ($r$, radius of gyration) — a geometric damping ratio for stability rather than a temporal one, and it plays the identical classifying role ($\zeta<1$ underdamped ↔ high slenderness = Euler-buckling regime; $\zeta>1$ overdamped ↔ low slenderness = crushing/yield regime dominates instead, per [[Strength of materials/09 Columns and Buckling/Euler Buckling of Columns|Euler Buckling of Columns]]'s "short/stubby vs long/slender" split).

## Consequence you probably didn't have before

Both your circuits vault and your structures vault teach "find $\tau$ (or $\ell$, or slenderness) then classify the regime" as a *procedure*, but never state the reason the procedure works: **any linear system's transient behavior is fully characterized by the ratio of its own internal rate constants — never by the size of the disturbance.** This is why superposition ([[07 AC Circuit Analysis and Network Theorems|Week 7]]) and the elastic superposition used throughout Strength of Materials (e.g. [[Strength of materials/05 Bending Stresses/Unsymmetric and Combined Bending|Unsymmetric and Combined Bending]]) both work: linearity guarantees the decay/oscillation *shape* is disturbance-independent, so responses to different loads can be added and only the amplitudes combine.

## Related
- [[Cross-Domain Synthesis/The Universal Second-Order Linear System|The Universal Second-Order Linear System]]
- [[AC Transients|AC Transients]]
- [[Strength of materials/09 Columns and Buckling/Euler Buckling of Columns|Euler Buckling of Columns]]

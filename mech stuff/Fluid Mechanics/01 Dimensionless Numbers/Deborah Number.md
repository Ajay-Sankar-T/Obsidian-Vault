---
tags: [fluid-mechanics, dimensionless-numbers, viscoelasticity]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Deborah Number

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · classifies: [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Newtonian and Non-Newtonian Fluids|Newtonian and Non-Newtonian Fluids]]

## Definition

$$\boxed{De=\frac{\lambda}{t_{\rm flow}}}$$

- $\lambda$ — the material's own **relaxation time** (how long internal microstructure — polymer chains, suspended particles — takes to relax back toward equilibrium after being disturbed)
- $t_{\rm flow}$ — characteristic timescale of the flow/observation (e.g. $1/\dot\gamma$ for a shear rate $\dot\gamma$, or the duration of the experiment)

**Memory:** $De=\dfrac{\text{relaxation time}}{\text{flow time}}$ — the direct temporal analogue of [[Fluid Mechanics/01 Dimensionless Numbers/Knudsen Number|Knudsen Number]]'s spatial ratio $\lambda/L$.

## Regimes

| $De$ | Behaviour |
|---|---|
| $De\ll1$ | liquid-like — the material fully relaxes long before the flow changes; ordinary viscous ([[Fluid Mechanics/00 Introduction and Fundamental Concepts/Viscosity and Newton's Law of Viscosity\|Newtonian]]) behavior |
| $De\sim1$ | viscoelastic effects important — the material "remembers" its recent deformation history; neither purely viscous nor purely elastic models are accurate |
| $De\gg1$ | elastic/solid-like — the flow changes faster than the material can relax, so it responds like an elastic solid rather than a fluid |

## The physical punchline: "everything flows, given enough time"

Deborah number is named for the Biblical verse "the mountains flowed before the Lord" — the point being that *any* material can be made to look either fluid or solid depending purely on the ratio of observation time to its own relaxation time. Silly putty behaves elastically (bounces) under a fast impact ($De\gg1$) but flows like a viscous liquid if left to sit under its own weight for hours ($De\ll1$) — same substance, same $\lambda$, different $t_{\rm flow}$.

## Cross-domain: relaxation time as a universal $\tau$

$\lambda$ here plays exactly the role of a circuit or structural time constant: compare directly with [[First-Order AC Transients (RC and RL)|First-Order AC Transients]]'s $\tau=RC$ (how fast a capacitor's voltage relaxes toward its new equilibrium) and [[Cross-Domain Synthesis/Exponential Decay - Time Constants, Damping and Spatial Relaxation|Exponential Decay — Time Constants, Damping and Spatial Relaxation]]'s general principle that **any linear relaxation process is governed by a ratio of its own internal rate constant to the observer's timescale, never by the size of the disturbance**. The Deborah number is the fluid-mechanics member of that same family: $De\ll1$ (fluid-like) is the mechanical-relaxation analogue of "steady state reached" ($t\gg\tau$) in an RC circuit, and $De\gg1$ (solid-like) is the analogue of "still mid-transient" ($t\ll\tau$).

## Related
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Newtonian and Non-Newtonian Fluids|Newtonian and Non-Newtonian Fluids]]
- [[Fluid Mechanics/01 Dimensionless Numbers/Knudsen Number|Knudsen Number]]
- [[Fluid Mechanics/01 Dimensionless Numbers/Buckingham Pi Theorem|Buckingham π Theorem]] — $De$ is one instance of the general $n-r$ dimensionless-group construction
- [[Cross-Domain Synthesis/Exponential Decay - Time Constants, Damping and Spatial Relaxation|Cross-Domain: Exponential Decay — Time Constants, Damping and Spatial Relaxation]]


## Cross-domain links

- [[Cross-Domain Synthesis/Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]] — for a Maxwell material λ = μ/G, the RC time constant of a spring in series with a dashpot.

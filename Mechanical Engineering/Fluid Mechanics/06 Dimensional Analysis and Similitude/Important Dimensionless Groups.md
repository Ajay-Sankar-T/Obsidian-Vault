---
tags: [concept, fluid-mechanics, dimensional-analysis, dimensionless-numbers]
status: draft
aliases: [Reynolds number, Froude number, Weber number, Mach number, Euler number, Strouhal number, cavitation number, force ratios]
up: "[[Fluid Mechanics - MOC]]"
---

# Important Dimensionless Groups

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Buckingham Pi Theorem|Buckingham π Theorem]] · full table: [[Dimensional Analysis and Similitude - Formula Bank|Formula Bank §5]] · next: [[Flow Similarity and Model Studies|Flow Similarity and Model Studies]]

## Core Idea

> **One-sentence definition:** a dimensionless group is a ratio of two effects (usually two forces or two time scales) that is the same number in any system of units, so flows with the same groups behave alike.

**Intuition:** a flow is the outcome of a competition. Inertia wants to keep fluid moving, viscosity resists shearing, gravity pulls it down, surface tension holds interfaces together, pressure pushes, compressibility stores energy. Each named group says who is winning.

## Governing Relation

Estimate each force as a *scale*, using a typical speed $U$, length $L$ and the fluid properties:

| Effect | Force scale |
|---|---|
| inertia | $\rho U^2L^2$ |
| viscous | $\mu UL$ |
| gravity | $\rho gL^3$ |
| surface tension | $\sigma L$ |
| pressure | $\Delta p\,L^2$ |
| compressibility (elastic) | $KL^2=\rho a^2L^2$ |

Dividing pairs gives the groups:

$$\boxed{\begin{aligned}
Re&=\frac{\rho UL}{\mu}=\frac{UL}{\nu}&&\text{inertia / viscous}\\
Fr&=\frac{U^2}{gL}\ \Big(\text{or }\frac U{\sqrt{gL}}\Big)&&\text{inertia / gravity}\\
We&=\frac{\rho U^2L}{\sigma}&&\text{inertia / surface tension}\\
Eu&=\frac{\Delta p}{\rho U^2}&&\text{pressure / inertia}\\
Ma&=\frac Ua&&\sqrt{\text{inertia / compressibility}}\\
Ca&=\frac{p-p_v}{\tfrac12\rho U^2}&&\text{pressure margin / inertia (cavitation)}\\
St&=\frac{\omega L}{U}&&\text{unsteady time scale / convective time scale}
\end{aligned}}$$

Heat transfer adds $Pr=\mu c_p/k$ (momentum diffusion / heat diffusion), $Ec=U^2/(c_pT_0)$, $Gr$ and the Nusselt number: see [[Forced Convection Correlations|Forced Convection Correlations]] and [[Natural Convection|Natural Convection]]. Rarefied and viscoelastic flows add [[Knudsen Number|$Kn$]] and [[Deborah Number|$De$]].

**Where:** $U,L$ = characteristic speed and length; $\rho,\mu,\nu,\sigma,a,p_v$ = fluid properties; $\omega$ = oscillation frequency.

**Assumptions:** the choice of $U$ and $L$ is a convention (pipe diameter, chord, depth); always state it. The *ratio* is only a guide to the dominant effect, accurate to a factor of a few.

## Visual

![[FM-D1-scaling.png]]

**Figure:** the reason groups matter in practice: matching $Re$ and $Fr$ together at reduced size needs $\nu_m/\nu_p=\alpha^{3/2}$, which no ordinary fluid provides (see [[Flow Similarity and Model Studies|Flow Similarity]]).

## When To Use

- Deciding **which physics is important** before solving anything (is it viscous? gravity-driven? compressible?).
- Choosing the groups for a **model test** or to correlate measurements ($C_D=g(Re)$, $f=g(Re,e/D)$).
- Reading a correlation in a handbook: all arguments are groups.

**Recognition pattern:** "how fast is the flow compared with sound / waves / viscous diffusion?" → **$Ma$, $Fr$, $Re$**.

## Method

1. **Identify** the relevant physical effects in the problem (free surface? very small scale? gas at high speed? vapour?).
2. **Choose** the group that compares each with inertia.
3. **Apply** with consistent units and the stated $U$, $L$.
4. **Check** the size of each group: $\gg1$ means inertia dominates, $\ll1$ means the other effect dominates, near 1 means both matter.

| If you see | Use | Typical threshold |
|---|---|---|
| internal flow in a pipe | $Re$ | laminar $<2300$, turbulent $>4000$ |
| free surface, waves, ships | $Fr$ | $Fr<1$ sub-critical, $>1$ super-critical |
| gas in motion | $Ma$ | incompressible $<0.3$, supersonic $>1$ |
| drops, bubbles, mm scale | $We$, $Bo$ | surface tension matters for $We\lesssim1$ |
| vapour formation | $Ca$ | cavitation when $Ca\to Ca_i$ |
| vortex shedding, pulsation | $St$ | $St\approx0.2$ for a cylinder |

## Derivation / Why It Works

Nondimensionalising the Navier–Stokes equations with $L$, $U$ and $\rho U^2$ leaves exactly $St$, $1/Fr$ and $1/Re$ as the coefficients (see [[Nondimensionalisation and the Reynolds Number|Nondimensionalisation and the Reynolds Number]]); the interface condition brings in $We$ and the equation of state brings in $Ma$. Hence these are the *only* parameters the solution can depend on, besides geometry.

## Common Traps

- **Trap:** mixing the two definitions of $Fr$ ($U^2/gL$ and $U/\sqrt{gL}$).
  - **Avoid it by:** stating which one you use; the Formula Bank uses White's squared form.
- **Trap:** a different characteristic length (diameter against radius against hydraulic diameter) between model and prototype.
- **Trap:** using gauge pressure in $Ca$ or $Eu$ where absolute pressure is required.
- **Trap:** reading the group as exact: $Re=2300$ is a typical onset, not a sharp line.

## Example

### Given
(a) Water ($\nu=1.0\times10^{-6}$ m²/s) at 2 m/s in a 25 mm pipe. (b) Air ($\nu=1.5\times10^{-5}$) at 30 m/s over a 1 m body. (c) A 100 m ship at 10 m/s. (d) A 1 mm water drop moving at 5 m/s ($\sigma=0.0728$ N/m).

### Solution
$$Re_{(a)}=\frac{2(0.025)}{10^{-6}}=5.0\times10^{4},\quad Re_{(b)}=\frac{30(1)}{1.5\times10^{-5}}=2\times10^{6},$$
$$Fr_{(c)}=\frac{10}{\sqrt{9.81\times100}}=0.319,\quad We_{(d)}=\frac{998(25)(0.001)}{0.0728}=343.$$

**Answer:** (a) turbulent pipe flow; (b) high-$Re$ external flow; (c) sub-critical ship, wave resistance matters; (d) inertia dominates surface tension 343 to 1, so the drop deforms.
**Key takeaway:** one number per effect tells you what to keep in the model without solving the flow.

## Connections

### Prerequisites
- [[Buckingham Pi Theorem|Buckingham π Theorem]]
- [[Viscosity and Newton's Law of Viscosity|Viscosity]], [[Surface Tension and Capillarity|Surface Tension]], [[Vapour Pressure and Cavitation|Cavitation]], [[Density, Specific Weight and Compressibility|Compressibility]]

### Related Concepts
- [[Nondimensionalisation and the Reynolds Number|Nondimensionalisation and the Reynolds Number]]
- [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]] — the critical $Re$ values.

### Next
- [[Flow Similarity and Model Studies|Flow Similarity and Model Studies]]

### Cross-domain links
- [[The Universal Second-Order Linear System|The Universal Second-Order Linear System]] — damping ratio $\zeta$ is a ratio of dissipation to storage, exactly the role $Re^{-1}$ plays (viscous against inertial).
- [[Convection Fundamentals - Boundary Layers and Scale Analysis|Convection Fundamentals]] — the same scale-ratio argument gives $Pr$, $Nu$ and the boundary-layer thickness.

## Quick Recall

> **In one line:** each named group is "inertia over X"; the one that is far from 1 tells you what dominates.

**Formula / trigger:** $$Re=\frac{\rho UL}{\mu},\ Fr=\frac{U^2}{gL},\ We=\frac{\rho U^2L}{\sigma},\ Ma=\frac Ua,\ Eu=\frac{\Delta p}{\rho U^2}$$

**Remember:** pipe laminar below 2300, $Ma<0.3$ incompressible, $Fr=1$ is the wave-speed limit.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** beginner
- **Subjects:** [[Fluid Mechanics - MOC]]

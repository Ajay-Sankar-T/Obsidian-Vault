---
tags: [concept, fluid-mechanics, pipe-flow, turbulence, laminar-flow]
status: draft
aliases: [laminar flow, turbulent flow, transition, Reynolds experiment, critical Reynolds number, entry length, Reynolds stress, friction velocity]
up: "[[Fluid Mechanics - MOC]]"
---

# Laminar and Turbulent Flow

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Nondimensionalisation and the Reynolds Number|Nondimensionalisation and the Reynolds Number]], [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]] · formulas: [[Pipe Flow and Losses - Formula Bank|Pipe Bank §3, §6]]

## Core Idea

> **One-sentence definition:** in **laminar** flow the fluid moves in smooth, ordered layers and momentum is carried only by molecular viscosity; in **turbulent** flow the velocity fluctuates chaotically and eddies carry momentum across the pipe, giving a flatter profile and a much larger wall shear.

**Intuition:** at low $Re$ viscosity damps any disturbance. At high $Re$ inertia wins, small disturbances grow into eddies, and mixing makes the flow behave as if it were far more viscous near the core and sharply sheared at the wall.

## Governing Relations

Pipe Reynolds number $Re=\dfrac{\rho\bar uD}{\mu}=\dfrac{\bar uD}{\nu}$:

| $Re$ | Regime |
|---|---|
| $<2300$ | laminar (disturbances decay) |
| $2300$–$4000$ | transitional, intermittent bursts of turbulence ("puffs") |
| $>4000$ | turbulent |

(The critical value depends on inlet disturbances: very clean, vibration-free pipes can stay laminar to $Re\sim10^5$; $2300$ is the practical lower bound.)

**Mean-velocity profiles at the same flow rate**

$$\text{laminar: }\ \frac u{\bar u}=2\Big(1-\frac{r^2}{R^2}\Big),\ \ u_{\max}=2\bar u,\ \ \alpha=2$$
$$\text{turbulent (1/7 power law): }\ \frac u{u_{\max}}=\Big(1-\frac rR\Big)^{1/7},\ \ \bar u=\frac{49}{60}u_{\max},\ \ \alpha\approx1.05$$

**Turbulence decomposition:** $u=\bar u+u'$; the mean momentum equation gains the **Reynolds stress** $-\rho\overline{u'v'}$, which acts like an extra (turbulent) shear stress much larger than $\mu\,d\bar u/dy$ away from the wall.

**Wall quantities:** $\tau_w=\dfrac f8\rho\bar u^2$ (Darcy $f$), friction velocity $u_\tau=\sqrt{\tau_w/\rho}=\bar u\sqrt{f/8}$; viscous sublayer thickness $\delta_v\approx5\nu/u_\tau$.

**Entry (development) length** (standard approximations): laminar $L_e\approx0.06\,Re\,D$; turbulent $L_e\approx4.4\,Re^{1/6}D$ (about 20–30 $D$).

**Where:** $\bar u$ = mean velocity; $D$ = diameter; $\alpha$ = kinetic-energy coefficient.

**Assumptions:** steady pipe flow, circular straight pipe; the 1/7 law is valid for $Re\sim10^4$–$10^5$ and fails at the wall.

## Visual

![[FM-N2-laminar-vs-turbulent.png]]

**Figure:** left, at the same mean velocity the turbulent profile is flat in the core and steep at the wall (hence greater wall shear), while the laminar profile is a full parabola. Right, the friction factor drops as $64/Re$ in laminar flow and jumps up across the transition band to the turbulent (Blasius) branch.

## When To Use

- Deciding **which friction law** applies: $f=64/Re$ (laminar) against the Moody/Colebrook branch (turbulent).
- Choosing the **kinetic-energy coefficient** $\alpha$ in the energy equation (2 or about 1).
- Judging **mixing and heat transfer** (turbulent flow mixes and transfers heat far faster).

**Recognition pattern:** "check whether the flow is laminar", "$Re$ based on diameter", "transition" → **compute $Re$ first**.

## Method

1. **Identify** $\bar u$, $D$ and $\nu$ (at the right temperature).
2. **Compute** $Re=\bar uD/\nu$.
3. **Choose** the regime: $<2300$ laminar, $>4000$ turbulent, between: avoid (unpredictable, use the conservative value).
4. **Apply** the corresponding law: Hagen–Poiseuille for laminar, Moody/Colebrook for turbulent.
5. **Check:** the entry length compared with the pipe length, and $\alpha$ in the energy equation.

## Derivation / Why It Works

*Transition.* A disturbance of size $\ell$ and velocity $u'$ is stretched by inertia at a rate $u'/\ell$ and damped by viscosity at a rate $\nu/\ell^2$; the ratio is a Reynolds number. Above a critical value the disturbance grows instead of decaying. *Profile.* Eddies transfer momentum from the fast core toward the wall, flattening the core and steepening the gradient at the wall, so for the same flow rate $\tau_w$ is larger and the pressure drop is larger than a laminar extrapolation would suggest.

*Wall shear from $f$.* Force balance on a pipe length $L$: $\Delta p\,\pi D^2/4=\tau_w\pi DL\Rightarrow\tau_w=\Delta p\,D/4L=f\rho\bar u^2/8$ (using $\Delta p=f(L/D)\rho\bar u^2/2$).

## Common Traps

- **Trap:** using $64/Re$ for turbulent flow, or the Moody turbulent branch for $Re<2300$.
- **Trap:** $Re$ with the wrong length (use the diameter for pipes; hydraulic diameter for ducts).
- **Trap:** assuming exactly 2300 is the transition: the band 2300–4000 is intermittent.
- **Trap:** using the kinetic-energy coefficient $\alpha=1$ for laminar flow (it is 2).
- **Trap:** forgetting that $\nu$ depends on temperature.

## Example

### Given
Water at 20 °C ($\nu=1.0\times10^{-6}$ m²/s) in a pipe of diameter 25 mm. Find (a) the largest laminar mean velocity, (b) the Reynolds number and entry length at 2 m/s, (c) the wall shear stress of a commercial-steel pipe example.

### Solution
(a) $\bar u_{\max,\rm lam}=\dfrac{2300\nu}{D}=\dfrac{2300(10^{-6})}{0.025}=0.092$ m/s.
(b) $Re=\dfrac{2(0.025)}{10^{-6}}=5\times10^4$: turbulent; $L_e\approx4.4Re^{1/6}D=4.4(6.07)(0.025)\approx0.67$ m (27 diameters).
(c) For the 100 mm pipe example in [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach]] ($\bar u=1.27$ m/s, $f=0.0196$): $\tau_w=f\rho\bar u^2/8=3.96$ Pa, $u_\tau=0.063$ m/s.

**Answer:** 9.2 cm/s; $Re=50\,000$ and about 0.67 m of development; wall shear 3.96 Pa.
**Key takeaway:** water in an ordinary pipe is turbulent above about 9 cm/s, so almost every practical pipe flow is turbulent.

## Connections

### Prerequisites
- [[Nondimensionalisation and the Reynolds Number|Nondimensionalisation and the Reynolds Number]]
- [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]]

### Related Concepts
- [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]]
- [[Moody Chart|Moody Chart]]
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]] — the coefficient $\alpha$.
- [[Important Dimensionless Groups|Important Dimensionless Groups]]

### Next
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]]

### Cross-domain links
- [[Convection Fundamentals - Boundary Layers and Scale Analysis|Convection Fundamentals]] and [[Forced Convection Correlations|Forced Convection Correlations]] — laminar and turbulent regimes have different Nusselt correlations for the same reason: eddies carry heat as well as momentum (Reynolds analogy).
- [[Euler Buckling of Columns|Euler Buckling of Columns]] and [[Resonance and Buckling - Instability as an Eigenvalue Problem|Resonance and Buckling]] — transition is an instability: below a critical value disturbances decay, above it they grow, exactly as a column buckles above the critical load.

## Quick Recall

> **In one line:** laminar $Re<2300$ (parabola, $f=64/Re$), turbulent $Re>4000$ (flat profile, larger $\tau_w$, Moody chart).

**Formula / trigger:** $$Re=\frac{\bar uD}{\nu},\qquad\tau_w=\frac f8\rho\bar u^2,\qquad L_e\approx0.06ReD\ (\text{lam}),\ 4.4Re^{1/6}D\ (\text{turb})$$

**Remember:** compute $Re$ first, with diameter and the right $\nu$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]

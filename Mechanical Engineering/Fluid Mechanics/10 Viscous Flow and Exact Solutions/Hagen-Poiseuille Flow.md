---
tags: [concept, fluid-mechanics, viscous-flow, exact-solution, poiseuille, pipe-flow]
status: draft
aliases: [Hagen-Poiseuille, Poiseuille flow, laminar pipe flow, Poiseuille law, fully developed laminar flow in a tube]
up: "[[Fluid Mechanics - MOC]]"
---

# Hagen-Poiseuille Flow

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Navier-Stokes Equations|Navier-Stokes Equations]], [[Plane Poiseuille Flow|Plane Poiseuille Flow]] · formulas: [[Viscous Flow and Exact Solutions - Formula Bank|Formula Bank §2]], [[Pipe Flow and Losses - Formula Bank|Pipe Bank §6]]

## Core Idea

> **One-sentence definition:** Hagen–Poiseuille flow is the steady, fully developed laminar flow in a circular pipe driven by a constant pressure gradient; the velocity profile is a paraboloid and the flow rate scales as $R^4$.

**Intuition:** same story as flow between plates: pressure pushes, the wall holds the outer fluid still, shear stress grows linearly from zero on the axis to its maximum at the wall, and integrating gives a parabola. Because the area also grows with $R^2$ and the typical speed with $R^2$, the flow rate grows with $R^4$.

## Governing Relations

Pipe of radius $R$, axial coordinate $z$, $G=-dp/dz>0$ constant.

**Navier–Stokes reduction** ($v_r=v_\theta=0$, $v_z=u(r)$, steady, fully developed):

$$\mu\,\frac1r\frac{d}{dr}\Big(r\frac{du}{dr}\Big)=\frac{dp}{dz}=-G$$

$$\boxed{u(r)=\frac{G}{4\mu}\,(R^2-r^2)},\qquad u_{\max}=\frac{GR^2}{4\mu}=2\bar u$$

$$\boxed{Q=\frac{\pi R^4G}{8\mu}=\frac{\pi D^4\,\Delta p}{128\,\mu L}},\qquad\bar u=\frac QA=\frac{GR^2}{8\mu},\qquad\tau(r)=\frac{Gr}2,\quad\tau_w=\frac{GR}2=\frac{8\mu\bar u}{D}=\frac{D\Delta p}{4L}$$

**Friction factor:** $f=\dfrac{64}{Re}$; kinetic-energy coefficient $\alpha=2$; hydraulic resistance $\Delta p=R_hQ$, $R_h=\dfrac{128\mu L}{\pi D^4}$.

**Validity:** $Re=\rho\bar uD/\mu\lesssim2300$; fully developed beyond an entry length $L_e\approx0.06\,Re\,D$.

**Where:** $G$ = pressure gradient; $\Delta p=GL$ over length $L$; $\bar u$ = mean velocity.

**Assumptions:** laminar, steady, incompressible, Newtonian, straight circular pipe, fully developed.

## Visual

![[FM-N1-laminar-profiles.png]]

**Figure:** right panel: the parabolic profile with mean velocity $\tfrac12u_{\max}$ (compare plane Poiseuille $\tfrac23$ and Couette $\tfrac12$ of the wall speed).

![[FM-N2-laminar-vs-turbulent.png]]

**Figure:** left panel contrasts the laminar parabola with the flatter turbulent profile at the same mean velocity; right panel shows $f=64/Re$ for the laminar branch.

## When To Use

- **Capillaries, syringes, needles, IV lines, microtubes**, laminar flow in small pipes ([[Viscous Flow and Exact Solutions - Solved Problems|GPS 10 syringe problem]]).
- **Viscometers** (capillary type): measure $\Delta p$ and $Q$ to get $\mu$.
- Establishing the laminar friction factor $64/Re$ used in the [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach equation]].

**Recognition pattern:** "laminar flow in a tube", "$Re<2300$", "pressure drop in a capillary", "fully developed" → **Hagen–Poiseuille**.

## Method

1. **Identify** $R$ (or $D$), $L$ and the driver ($\Delta p$ or $Q$); check $Re<2300$.
2. **Choose** the radial ODE with $u(R)=0$ and $u$ finite at $r=0$ (equivalently $du/dr=0$).
3. **Apply:** $u=\frac{G}{4\mu}(R^2-r^2)$, then $Q=\pi R^4G/8\mu$.
4. **Compute** $\bar u$, $\tau_w=8\mu\bar u/D$, and the entry length.
5. **Check:** $Re$, entry length against $L$, and the $D^4$ sensitivity.

## Derivation / Why It Works

**Shell balance.** On a cylindrical fluid shell of radius $r$ and length $dz$, the pressure force $\Delta p\,\pi r^2$ is balanced by the wall shear on the shell surface $\tau\,2\pi r\,dz$, giving $\tau=\dfrac{Gr}2$ (zero on the axis). With $\tau=-\mu\,du/dr$ (velocity decreases outward):
$$\frac{du}{dr}=-\frac{Gr}{2\mu}\ \Rightarrow\ u=\frac{G}{4\mu}(R^2-r^2)\ \ (u(R)=0).$$
**Flow rate.** $Q=\int_0^R u\,2\pi r\,dr=\dfrac{\pi G}{2\mu}\Big(\dfrac{R^4}2-\dfrac{R^4}4\Big)=\dfrac{\pi GR^4}{8\mu}$.

**Link to the friction factor.** With $Q=\bar u\,\pi D^2/4$: $\Delta p=\dfrac{32\mu L\bar u}{D^2}$. Compare with the Darcy form $\Delta p=f\dfrac LD\dfrac{\rho\bar u^2}2$: $\ f=\dfrac{64\mu}{\rho\bar uD}=\dfrac{64}{Re}$.

**Dimensional check.** The four variables $Q,R,\mu,G$ span three dimensions, so there is one group: $Q\mu/(R^4G)=\pi/8$ (the constant that dimensional analysis cannot produce, see [[Buckingham Pi Theorem|the Π theorem]]).

## Common Traps

- **Trap:** using $D$ where $R$ belongs: $Q=\pi R^4G/8\mu$ but $Q=\pi D^4\Delta p/128\mu L$.
  - **Avoid it by:** writing which radius or diameter each formula uses.
- **Trap:** applying it to turbulent flow (the friction law is then different, see [[Moody Chart|Moody Chart]]).
- **Trap:** halving the diameter and expecting a quarter of the flow: $Q\propto D^4$ gives 1/16.
- **Trap:** ignoring the entry region in a short tube.

## Example

### Given
Water at 20 °C ($\mu=10^{-3}$ Pa·s, $\rho=998$ kg/m³) flows at $Q=1$ mL/s through a tube of diameter 2 mm and length 1 m.

### Solution
$$\Delta p=\frac{128\mu LQ}{\pi D^4}=\frac{128(10^{-3})(1)(10^{-6})}{\pi(0.002)^4}=2546\ \text{Pa}.$$
$$\bar u=\frac{Q}{\pi D^2/4}=0.318\ \text{m/s},\quad Re=\frac{998(0.318)(0.002)}{10^{-3}}=635\ (\text{laminar}),$$
$$\tau_w=\frac{8\mu\bar u}{D}=1.27\ \text{Pa}\ \Big(=\frac{D\Delta p}{4L}\ \checkmark\Big),\quad u_{\max}=2\bar u=0.64\ \text{m/s},\quad L_e\approx0.06\,Re\,D=76\ \text{mm}.$$

**Answer:** 2.55 kPa, $\bar u=0.32$ m/s, $Re=635$, wall shear 1.27 Pa, entry length 76 mm ($\ll1$ m).
**Key takeaway:** the same flow in a 1 mm tube would need $16\times$ the pressure drop.

## Connections

### Prerequisites
- [[Navier-Stokes Equations|Navier-Stokes Equations]]
- [[Boundary Conditions in Fluid Flow|Boundary Conditions in Fluid Flow]]
- [[Nondimensionalisation and the Reynolds Number|Nondimensionalisation and the Reynolds Number]]

### Related Concepts
- [[Plane Poiseuille Flow|Plane Poiseuille Flow]], [[Plane Couette Flow|Plane Couette Flow]]
- [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]]
- [[Darcy-Weisbach Equation and Friction Factor|Darcy–Weisbach Equation and Friction Factor]]
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]]

### Next
- [[Laminar and Turbulent Flow|Laminar and Turbulent Flow]]

### Cross-domain links
- [[Power Transmission by Shafts|Power Transmission by Shafts]] — the laminar profile satisfies a Poisson equation $\nabla^2u=$ const, the same as torsion of a bar; the circular case gives $Q\propto R^4$ in flow and $J=\pi R^4/2$ in torsion.
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — $\Delta p=R_hQ$, $R_h=128\mu L/\pi D^4$: a pipe is a resistor, with the notorious $D^{-4}$ dependence.

## Quick Recall

> **In one line:** laminar pipe flow: $u=\frac{G}{4\mu}(R^2-r^2)$, $Q=\pi R^4G/8\mu$, $u_{\max}=2\bar u$, $f=64/Re$.

**Formula / trigger:** $$\Delta p=\frac{128\mu LQ}{\pi D^4}=\frac{32\mu L\bar u}{D^2},\qquad\tau_w=\frac{8\mu\bar u}{D}$$

**Remember:** $D^4$ sensitivity; valid for $Re<2300$ and beyond the entry length $0.06\,Re\,D$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]

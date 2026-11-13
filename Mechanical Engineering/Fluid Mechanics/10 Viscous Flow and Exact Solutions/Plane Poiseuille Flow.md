---
tags: [concept, fluid-mechanics, viscous-flow, exact-solution, poiseuille]
status: draft
aliases: [plane Poiseuille flow, channel flow, flow between parallel plates, cubic law, lubrication flow]
up: "[[Fluid Mechanics - MOC]]"
---

# Plane Poiseuille Flow

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Navier-Stokes Equations|Navier-Stokes Equations]], [[Plane Couette Flow|Plane Couette Flow]] · formulas: [[Viscous Flow and Exact Solutions - Formula Bank|Formula Bank §2]]

## Core Idea

> **One-sentence definition:** plane Poiseuille flow is the steady laminar flow between two fixed parallel plates driven by a constant pressure gradient; the velocity profile is a parabola and the flow rate grows as the cube of the gap.

**Intuition:** pressure pushes the fluid, the walls hold the edge layers still, and viscosity transmits the resulting shear. The fastest fluid sits mid-gap where the shear stress is zero; the shear grows linearly towards each wall, which forces a parabolic profile.

## Governing Relations

Geometry: plates at $y=0$ and $y=h$, both fixed; flow in $x$; $G=-dp/dx>0$ constant.

**Navier–Stokes reduction** (steady, fully developed, $v=w=0$; gravity absorbed in $p$): $\ \mu\dfrac{d^2u}{dy^2}=\dfrac{dp}{dx}$.

$$\boxed{u(y)=\frac{G}{2\mu}\,y\,(h-y)},\qquad u_{\max}=\frac{Gh^2}{8\mu}\ (\text{at }y=h/2)$$

$$\bar u=\frac{Gh^2}{12\mu}=\frac23u_{\max},\qquad q=\bar u\,h=\frac{Gh^3}{12\mu}\ \ (\text{per unit width})$$

$$\tau(y)=\mu\frac{du}{dy}=G\Big(\frac h2-y\Big),\qquad\tau_w=\frac{Gh}2=\frac{6\mu\bar u}{h}$$

**Hydraulic resistance:** $\Delta p=R_hQ$ with $R_h=\dfrac{12\mu L}{wh^3}$ (width $w$): linear, like Ohm's law.

**Where:** $G$ = driving pressure gradient (Pa/m); $q$ = flow per unit width (m²/s); $\tau_w$ = wall shear stress.

**Assumptions:** laminar ($Re=\rho\bar uh/\mu<1400$), steady, fully developed, plates wide compared with $h$ (no side effects), Newtonian, constant $dp/dx$.

## Visual

![[FM-N1-laminar-profiles.png]]

**Figure:** middle panel: the parabola with mean velocity $\tfrac23u_{\max}$. Compare the linear Couette profile (left) and the axisymmetric version (right).

## When To Use

- **Microchannels, lab-on-chip, narrow gaps**, lubrication films.
- **Flow in fractures and porous layers** (the "cubic law" $q\propto h^3$).
- Estimating pressure drop in slot-like passages, and as the 2-D model of duct flow.

**Recognition pattern:** "fluid between two stationary parallel plates", "pressure gradient drives", "thin slot" → **plane Poiseuille flow**.

## Method

1. **Identify** the plate gap $h$ and the pressure gradient $G=-dp/dx$.
2. **Choose** the ODE $\mu u''=-G$ with $u(0)=u(h)=0$.
3. **Apply:** integrate twice to get $u=\frac{G}{2\mu}y(h-y)$.
4. **Compute** $q=Gh^3/12\mu$, $\bar u$, $\tau_w=Gh/2$.
5. **Check:** laminar $Re$, and that the mean speed times area gives the same $q$.

## Derivation / Why It Works

**Force balance on a slab.** Take a slab between $y$ and $y+dy$ of length $dx$. Net pressure force $-dp\,dy$ must equal net shear force $d\tau\,dx$: $d\tau/dy=dp/dx=-G$, so $\tau=G(h/2-y)$ using symmetry ($\tau=0$ at the centre). Newton's law $\tau=\mu\,du/dy$ then gives, with $u(0)=0$:
$$u=\frac G\mu\Big(\frac{hy}2-\frac{y^2}2\Big)=\frac{G}{2\mu}y(h-y).$$
**Flow rate.** $q=\int_0^hu\,dy=\dfrac{G}{2\mu}\Big(\dfrac{h^3}{2}-\dfrac{h^3}3\Big)=\dfrac{Gh^3}{12\mu}$.

**Dimensional check.** The $\Pi$ theorem predicts $q\mu/(h^3G)=$ const (one group), and the solution fixes the constant at $1/12$.

## Common Traps

- **Trap:** using $u_{\max}$ instead of $\bar u$ in the flow rate.
  - **Avoid it by:** $q=\tfrac23u_{\max}h$.
- **Trap:** halving the gap and expecting half the flow: $q\propto h^3$ gives an 8-fold drop.
- **Trap:** using the pipe formula ($\pi R^4/8\mu$) for slot flow.
- **Trap:** forgetting gravity for inclined or vertical channels (use the piezometric gradient $d(p+\rho gz)/dx$).

## Example

### Given
Water ($\mu=10^{-3}$ Pa·s, $\rho=998$ kg/m³) in a gap of $h=1$ mm driven by $dp/dx=-100$ Pa/m.

### Solution
$$u_{\max}=\frac{Gh^2}{8\mu}=\frac{100(10^{-6})}{8\times10^{-3}}=0.0125\ \text{m/s},\qquad\bar u=\frac{Gh^2}{12\mu}=8.33\times10^{-3}\ \text{m/s},$$
$$q=\bar uh=8.33\times10^{-6}\ \text{m}^2/\text{s},\qquad\tau_w=\frac{Gh}{2}=0.050\ \text{Pa},\qquad Re=\frac{\rho\bar uh}{\mu}=8.3.$$

**Answer:** peak 1.25 cm/s, mean 0.83 cm/s, $q=8.3$ mm²/s, wall shear 0.05 Pa, $Re=8.3$ (laminar).
**Key takeaway:** doubling the gap multiplies the flow by 8 for the same pressure gradient.

## Connections

### Prerequisites
- [[Navier-Stokes Equations|Navier-Stokes Equations]]
- [[Boundary Conditions in Fluid Flow|Boundary Conditions in Fluid Flow]]

### Related Concepts
- [[Plane Couette Flow|Plane Couette Flow]] — superpose to get Couette–Poiseuille.
- [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]] — same recipe in a round pipe.
- [[Buckingham Pi Theorem|Buckingham π Theorem]] — the one-group analysis predicting $q\propto h^3G/\mu$.

### Next
- [[Hagen-Poiseuille Flow|Hagen–Poiseuille Flow]]

### Cross-domain links
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — $\Delta p=R_hQ$ with $R_h\propto h^{-3}$ is Ohm's law; channels in series or parallel add like resistors.
- [[Flexure Formula|Flexure Formula]] and [[Shear Stress Formula for Beams|Shear Stress Formula for Beams]] — a parabolic shear profile and the cubic dependence on depth resemble the beam: bending stress linear in $y$, shear parabolic, and stiffness $\propto h^3$ (since $I\propto h^3$); here flow rate $\propto h^3$.

## Quick Recall

> **In one line:** pressure-driven flow between fixed plates: parabola $u=\frac{G}{2\mu}y(h-y)$, $q=Gh^3/12\mu$, $u_{\max}=\tfrac32\bar u$.

**Formula / trigger:** $$u=\frac{G}{2\mu}y(h-y),\quad q=\frac{Gh^3}{12\mu},\quad\tau_w=\frac{Gh}{2}$$

**Remember:** $q\propto h^3$; mean is two-thirds of the peak.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]

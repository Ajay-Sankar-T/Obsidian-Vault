---
tags: [concept, fluid-mechanics, inviscid-flow, bernoulli]
status: draft
aliases: [Bernoulli equation, Bernoulli principle, energy equation along a streamline, Torricelli, venturi, EGL, HGL]
up: "[[Fluid Mechanics - MOC]]"
---

# Bernoulli Equation

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Euler's Equations of Fluid Motion|Euler's Equations]], [[Conservation of Mass (Continuity Equation)|Continuity]] · formulas: [[Incompressible Inviscid Flow and Bernoulli - Formula Bank|Formula Bank §2–§3]] · problems: [[Incompressible Inviscid Flow and Bernoulli - Solved Problems|Solved Problems]]

## Core Idea

> **One-sentence definition:** along a streamline in steady, incompressible, frictionless flow, the sum $p+\tfrac12\rho V^2+\rho gz$ is constant.

**Intuition:** it is a mechanical energy bookkeeping for a parcel: pressure energy, kinetic energy and potential energy can be traded, but the total is fixed when nothing dissipates it or adds work. Where the fluid speeds up, the pressure must fall; where it climbs, it loses pressure or speed.

## Governing Relation

$$\boxed{\frac{p_1}{\rho}+\frac{V_1^2}{2}+gz_1=\frac{p_2}{\rho}+\frac{V_2^2}{2}+gz_2=\text{const along the streamline}}$$

| Form | Equation | Units |
|---|---|---|
| pressure | $p+\tfrac12\rho V^2+\gamma z=$ const | Pa |
| energy per unit mass | $\dfrac p\rho+\dfrac{V^2}{2}+gz=$ const | J/kg |
| head | $\dfrac p\gamma+\dfrac{V^2}{2g}+z=$ const | m |

**Unsteady, along a streamline:** $\displaystyle\int_1^2\frac{\partial V}{\partial t}ds+\int_1^2\frac{dp}\rho+\frac{V_2^2-V_1^2}{2}+g(z_2-z_1)=0$.

**With pump, turbine, losses:** see [[Energy Equation with Head Loss|Energy Equation with Head Loss]].

**The six conditions** (all must hold):

1. steady flow
2. incompressible ($Ma<0.3$)
3. frictionless (no boundary layers, wakes, separation between the points)
4. along a **single streamline** (or throughout, if the flow is irrotational)
5. no shaft work between the points
6. no heat transfer

**Where:** $p$ = static pressure, $V$ = local speed, $z$ = height above a datum.

## Visual

![[FM-B2-venturi-EGL-HGL.png]]

**Figure:** the energy grade line stays constant (frictionless) while the hydraulic grade line dips by $V^2/2g$ in the throat, where the pressure is lowest. The same picture with a pump and losses is in [[Energy Equation with Head Loss|Energy Equation with Head Loss]].

## When To Use

- **Nozzles, jets, tanks draining, venturis, Pitot tubes, siphons**: short, smooth, accelerating flows.
- Relating **pressure and speed** between two points in the core flow.
- First estimate of **cavitation** (lowest pressure) and **forces on a bend** (pressure, then momentum).

**Recognition pattern:** "frictionless", "speed increases so pressure ...", "find the pressure at the throat / the exit speed" → **Bernoulli plus continuity**.

## Method

1. **Identify** the streamline and choose point 1 (upstream, where most is known) and point 2.
2. **Check** the six conditions; if a pump, turbine or loss intervenes, use the energy equation with head terms.
3. **Apply** Bernoulli in one form and **add continuity** $A_1V_1=A_2V_2$ (two unknowns need two equations).
4. **Solve** for the unknown pressure or speed; use **gauge** pressure unless a cavitation or compressibility check needs absolute.
5. **Check:** pressure falls where speed rises, units, and no friction was assumed.

## Derivation / Why It Works

Apply Newton's second law to a parcel of cross-section $dA$ and length $ds$ along a streamline ([[Euler's Equations of Fluid Motion|Euler's equations in streamline coordinates]]):

$$\rho V\frac{dV}{ds}=-\frac{dp}{ds}-\rho g\frac{dz}{ds}\ \Longrightarrow\ \frac{dp}{\rho}+d\Big(\frac{V^2}{2}\Big)+g\,dz=0$$

(steady, so $V\,dV/ds$ is the full acceleration). Integrating with constant $\rho$ gives the boxed result. The same equation follows from the steady-flow energy equation of thermodynamics with no work, heat or friction.

**Rotational flow:** the identity $(\mathbf V\cdot\nabla)\mathbf V=\nabla(V^2/2)-\mathbf V\times\boldsymbol\zeta$ shows the constant differs between streamlines by the term $\mathbf V\times\boldsymbol\zeta$; for **irrotational** flow ($\boldsymbol\zeta=0$) the constant is the same everywhere.

## Common Traps

- **Trap:** applying Bernoulli across a pump, turbine, or through a boundary layer or wake.
  - **Avoid it by:** using the energy equation with $h_p$, $h_t$, $h_l$.
- **Trap:** forgetting continuity (two unknown velocities).
- **Trap:** applying it between different streamlines in a **rotational** flow.
- **Trap:** using gauge pressure when checking for cavitation (use absolute).
- **Trap:** expecting friction losses from Bernoulli: it contains none.
- **Trap:** taking $V_1=0$ for a draining tank when $A_2/A_1$ is not small.

## Example

### Given
(a) Water ($\rho=998$ kg/m³) drains from a large open tank through a small hole 2 m below the free surface. (b) Water flows through a horizontal venturi: pipe 100 mm, throat 50 mm, pipe speed $V_1=2$ m/s.

### Solution
(a) Free surface (point 1, $V_1\approx0$, $p_1=p_{\rm atm}$) to the jet (point 2, $p_2=p_{\rm atm}$):
$$V_2=\sqrt{2gh}=\sqrt{2(9.81)(2)}=6.26\ \text{m/s}.$$

(b) Continuity: $V_2=V_1(A_1/A_2)=4V_1=8$ m/s. Bernoulli at the same height:
$$p_1-p_2=\tfrac12\rho(V_2^2-V_1^2)=\tfrac12(998)(64-4)=29\,940\ \text{Pa}=29.9\ \text{kPa},$$
$$Q=A_1V_1=7.854\times10^{-3}\times2=15.7\ \text{L/s}.$$

**Answer:** 6.26 m/s; pressure drop 29.9 kPa and 15.7 L/s.
**Key takeaway:** reading the pressure drop gives the flow rate: $Q=\dfrac{A_2}{\sqrt{1-(A_2/A_1)^2}}\sqrt{2\Delta p/\rho}$ for a venturi meter (×$c_d$ in practice).

## Connections

### Prerequisites
- [[Euler's Equations of Fluid Motion|Euler's Equations of Fluid Motion]]
- [[Conservation of Mass (Continuity Equation)|Conservation of Mass (Continuity Equation)]]
- [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]

### Related Concepts
- [[Static, Stagnation and Dynamic Pressure|Static, Stagnation and Dynamic Pressure]]
- [[Pitot Tube and Pressure Measurement|Pitot Tube and Pressure Measurement]]
- [[Vapour Pressure and Cavitation|Vapour Pressure and Cavitation]]
- [[Rotational and Irrotational Flow|Rotational and Irrotational Flow]]
- [[Fluid Flow, Continuity and Bernoulli|Fluid Flow, Continuity and Bernoulli (Physics)]]

### Next
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]] — add friction, pumps and turbines.

### Cross-domain links
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — Bernoulli is KVL for a lossless pipe: $\tfrac12\rho V^2$ is the inductor's kinetic energy with inertance $\rho\ell/A$.
- [[Energy Methods - A Unified View|Energy Methods — A Unified View]] — the three terms are the fluid's pressure, kinetic and potential energy per unit volume, the same conservation principle as strain energy plus work in solids.

## Quick Recall

> **In one line:** along a streamline, $p+\tfrac12\rho V^2+\rho gz$ is constant (steady, incompressible, frictionless, no work).

**Formula / trigger:** $$\frac{p_1}{\rho}+\frac{V_1^2}{2}+gz_1=\frac{p_2}{\rho}+\frac{V_2^2}{2}+gz_2,\quad A_1V_1=A_2V_2$$

**Remember:** speed up, pressure down; always pair it with continuity.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]

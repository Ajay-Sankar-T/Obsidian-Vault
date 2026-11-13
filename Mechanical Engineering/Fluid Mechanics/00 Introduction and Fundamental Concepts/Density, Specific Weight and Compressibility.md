---
tags: [concept, fluid-mechanics, fluid-properties, compressibility]
status: draft
aliases: [density, specific weight, specific gravity, bulk modulus, compressibility, speed of sound]
up: "[[Fluid Mechanics - MOC]]"
---

# Density, Specific Weight and Compressibility

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Continuum Concept|Continuum Concept]] · next: [[Viscosity and Newton's Law of Viscosity|Viscosity]], [[Surface Tension and Capillarity|Surface Tension]]

## Core Idea

> **One-sentence definition:** density $\rho$ is mass per unit volume at a point, specific weight $\gamma=\rho g$ is weight per unit volume, and compressibility (bulk modulus $K$) measures how much the density changes when the pressure changes.

**Intuition:** pressing on a fluid squeezes it a little. A liquid barely gives, a gas gives a lot. Whether you may ignore that squeezing decides which set of equations you use for the whole problem (incompressible or compressible flow).

## Governing Relations

$$\rho=\lim_{\delta V\to\delta V^*}\frac{\delta m}{\delta V},\qquad \gamma=\rho g,\qquad SG=\frac{\rho}{\rho_{\rm water,\,4^\circ C}}\quad(\rho_{\rm water,4^\circ C}=1000\ {\rm kg/m^3})$$

The limit stops at a volume $\delta V^*$ that is still large compared with molecular spacing: that is the [[Continuum Concept|continuum hypothesis]].

**Bulk modulus and compressibility**

$$\boxed{K=-V\frac{dp}{dV}=\rho\frac{dp}{d\rho}},\qquad \beta=\frac1K,\qquad \frac{\Delta V}{V}=-\frac{\Delta p}{K}=-\beta\,\Delta p$$

**Speed of sound** (small pressure disturbances travel at)

$$a=\sqrt{\frac{K_s}{\rho}}=\sqrt{\Big(\frac{\partial p}{\partial\rho}\Big)_s}\ \ \Longrightarrow\ \ a_{\rm gas}=\sqrt{kRT}$$

**Ideal gas:** $p=\rho RT$ with absolute $p$ and absolute $T$ (K); $R_{\rm air}=287$ J/(kg·K), $k=c_p/c_v=1.4$. For a gas, $K=p$ (isothermal) or $K=kp$ (isentropic).

| Fluid (20 °C, 1 atm) | $\rho$ (kg/m³) | $K$ | $a$ (m/s) |
|---|---|---|---|
| water | 998 | about 2.2 GPa | about 1480 |
| mercury | 13 550 (SG 13.6) | about 26 GPa | about 1450 |
| air | 1.204 | $kp=142$ kPa | 343 |

**Where:**
- $\rho$ = density (kg/m³); $\gamma$ = specific weight (N/m³); $SG$ = specific gravity (dimensionless)
- $K$ = bulk modulus (Pa), the fluid analogue of Young's modulus for pure compression
- $a$ = speed of sound (m/s)

**Assumptions:** continuum; for $K$ and $a$ the process (isothermal or isentropic) must be stated.

## Visual

No figure here: the content is a handful of numbers. The useful picture is the one in [[Differential Continuity Equation|the differential continuity note]]: $D\rho/Dt=-\rho\nabla\cdot\mathbf V$, which is where density change enters the flow equations.

## When To Use

- Converting between mass-based and weight-based formulas: pressure from depth is $p=\gamma h=\rho g h$.
- Deciding **incompressible or compressible**: compute $Ma=V/a$. If $Ma\lesssim0.3$ the density change is below about 5 % and the flow is treated as incompressible. Almost all liquid flows qualify.
- Water hammer, sound and shock problems, where $K$ sets the wave speed.

**Recognition pattern:** if the problem gives a pressure rise in a liquid and asks for volume change, think of **$K$**. If it gives a gas at a state, think of **$p=\rho RT$**.

## Method

1. **Identify** whether the fluid is a gas (use the ideal gas law with absolute $p$, $T$) or a liquid (use a tabulated $\rho$, correct for temperature if the range is large).
2. **Choose** the compressibility test: $Ma<0.3$ for flow; $\Delta p/K\ll1$ for a liquid under a pressure change.
3. **Apply:** $\Delta V/V=-\Delta p/K$, or $\Delta\rho/\rho\approx Ma^2/2$ at a stagnation point.
4. **Check:** units (kg/m³ against N/m³), absolute temperature, and that $SG$ is a pure number.

## Derivation / Why It Works

The density change at a stagnation point follows from Bernoulli. A flow decelerated to rest raises its pressure by about $\tfrac12\rho V^2$, and $\Delta\rho\approx\Delta p/a^2$ for a small change. Hence

$$\frac{\Delta\rho}{\rho}\approx\frac{\tfrac12\rho V^2}{\rho a^2}=\frac{Ma^2}{2}.$$

At $Ma=0.3$ this is $4.5\%$, which is the origin of the "incompressible below 0.3" rule (the same limit appears in [[Differential Mass Conservation and Fluid Kinematics - Formula Bank|the differential kinematics bank]]).

## Common Traps

- **Trap:** calling a liquid "incompressible" and then using $K=\infty$ for a **sound-speed** or **water-hammer** question.
  - **Why:** the *flow* is incompressible, but the *fluid* is not; $K$ is large, not infinite, and $a=\sqrt{K/\rho}$ is finite.
  - **Avoid it by:** separating "incompressible flow" (a statement about $\nabla\cdot\mathbf V$) from "incompressible fluid" (a statement about $K$).
- **Trap:** using gauge pressure or °C in $p=\rho RT$.
  - **Avoid it by:** converting to absolute pressure and kelvin first.
- **Trap:** confusing $\rho$ (kg/m³) with $\gamma$ (N/m³) when a formula quotes one of them.

## Example

### Given
Air at 20 °C and 101.325 kPa. Also: water compressed from the surface to a depth of 1 km ($\Delta p\approx100$ atm $=10.13$ MPa).

### Solution
$$\rho_{\rm air}=\frac{101\,325}{287\times293.15}=1.204\ \text{kg/m}^3,\qquad a=\sqrt{1.4\times287\times293.15}=343\ \text{m/s}.$$
$$\frac{\Delta V}{V}=-\frac{10.13\times10^{6}}{2.2\times10^{9}}=-0.46\,\%.$$

**Answer:** air 1.204 kg/m³ and 343 m/s; water shrinks by only 0.46 % at 1 km depth.
**Key takeaway:** even 100 atm hardly compresses water, so treating water as incompressible costs almost nothing, while air changes by about 5 % already at $Ma=0.3$.

## Connections

### Prerequisites
- [[Continuum Concept|Continuum Concept]]
- [[Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]]

### Related Concepts
- [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]] — $\rho g$ is the pressure gradient; in a gas $\rho$ varies with height.
- [[Ideal Fluid|Ideal Fluid]] — "ideal" often includes "incompressible".
- [[Important Dimensionless Groups|Important Dimensionless Groups]] — Mach number is the compressibility ratio.

### Next
- [[Differential Continuity Equation|Differential Continuity Equation]] — where $D\rho/Dt$ enters.
- [[Isentropic Nozzle Flow and Choking|Isentropic Nozzle Flow and Choking]] — compressible flow, where $a$ matters.

### Cross-domain links
- [[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]] — $K$ is the same bulk modulus a solid has, $K=E/[3(1-2\nu)]$; a liquid has $G=0$, so $K$ is its only elastic constant. See [[Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]].
- [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]] — compressibility acts as capacitance (a spring that stores flow volume under pressure), the analogue of $C$ in a circuit.

## Quick Recall

> **In one line:** $\rho$ = mass/volume, $\gamma=\rho g$, $K=\rho\,dp/d\rho$ measures stiffness, $a=\sqrt{K/\rho}$, and flow is incompressible when $Ma<0.3$.

**Formula / trigger:** $$\frac{\Delta V}{V}=-\frac{\Delta p}{K},\qquad a_{\rm gas}=\sqrt{kRT}$$

**Remember:** water $K\approx2.2$ GPa, air at 1 atm $K_s=142$ kPa; a gas is about $10^{4}$ times softer.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** beginner
- **Subjects:** [[Fluid Mechanics - MOC]]

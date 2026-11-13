---
tags: [concept, fluid-mechanics, fluid-properties, cavitation]
status: draft
aliases: [vapour pressure, vapor pressure, cavitation, cavitation number, NPSH, boiling by pressure drop]
up: "[[Fluid Mechanics - MOC]]"
---

# Vapour Pressure and Cavitation

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]], [[Surface Tension and Capillarity|Surface Tension]] · next: [[Bernoulli Equation|Bernoulli Equation]]

## Core Idea

> **One-sentence definition:** the vapour pressure $p_v(T)$ is the absolute pressure at which a liquid and its vapour coexist in equilibrium, and **cavitation** is the formation of vapour bubbles where the flow lowers the local pressure to $p_v$.

**Intuition:** boiling is not only a matter of heating. Water at 20 °C "boils" if you reduce the absolute pressure to 2.34 kPa. A fast flow can do that locally, because by Bernoulli high speed means low pressure. The bubbles then ride into higher-pressure regions and collapse violently.

## Governing Relations

**Cavitation condition** (absolute pressures)

$$p_{\min}\le p_v(T)$$

**Cavitation number** (also called Euler or Thoma-type number)

$$\boxed{Ca=\frac{p-p_v}{\tfrac12\rho V^2}}$$

Cavitation sets in when $Ca$ falls to a critical (incipient) value $Ca_i$ that depends on the geometry; a smaller $Ca$ means heavier cavitation.

**Lowest pressure from Bernoulli** (steady, frictionless, between a reference point 1 and the point of maximum speed):

$$p_{\min}=p_1-\tfrac12\rho\,(V_{\max}^2-V_1^2)-\rho g\,\Delta z$$

**Net positive suction head** (pumps, standard result)

$$NPSH_A=\frac{p_{\rm inlet,abs}-p_v}{\rho g}+\frac{V_{\rm inlet}^2}{2g}\ \ >\ \ NPSH_R$$

| $T$ (°C) | 0 | 20 | 40 | 60 | 80 | 100 |
|---|---|---|---|---|---|---|
| $p_v$ of water (kPa abs) | 0.61 | 2.34 | 7.38 | 19.9 | 47.4 | 101.3 |

**Where:** $p$ = absolute static pressure, $V$ = reference velocity, $NPSH_R$ = value the manufacturer gives for the pump.

**Assumptions:** pure liquid, absolute pressure used throughout, steady flow for the Bernoulli estimate of $p_{\min}$.

## Visual

![[FM-N3-vapour-pressure-cavitation.png]]

**Figure:** left, $p_v$ for water climbs about 40-fold from 10 °C to 80 °C, so hot liquids cavitate far more easily. Right, the throat pressure of a venturi falls as $V_1^2$ and meets $p_v$ at $V_1=5.41$ m/s; beyond that the equation no longer holds because the throat is filled with vapour.

## When To Use

- Checking a **venturi, nozzle, valve or orifice** for cavitation.
- Sizing a **pump inlet** (NPSH) or a **siphon** (the suction limit is $(p_a-p_v)/\rho g\approx10$ m for cold water).
- Understanding noise, pitting and loss of performance in pumps, propellers, hydrofoils and control valves.

**Recognition pattern:** a liquid, a pressure that falls (throat, high speed, high elevation), and a question on the lowest allowed pressure or the largest allowed speed → **cavitation**.

## Method

1. **Identify** the point of lowest pressure (throat, highest point of a siphon, blade suction side).
2. **Choose** Bernoulli from a known upstream state to that point.
3. **Apply** with **absolute** pressures: $p_{\min}=p_1-\tfrac12\rho(V_2^2-V_1^2)\ (-\rho g\Delta z)$.
4. **Check** $p_{\min}>p_v$ at the operating temperature; if not, lower the speed, raise the inlet pressure, cool the liquid, or enlarge the throat.

## Derivation / Why It Works

For a venturi at the same height with continuity $V_2=V_1A_1/A_2$:

$$p_2=p_1-\tfrac12\rho V_1^2\Big[\Big(\frac{A_1}{A_2}\Big)^2-1\Big].$$

Setting $p_2=p_v$ gives the onset condition in terms of $Ca$ (the same result is quoted in the Bernoulli formula bank):

$$Ca_1=\frac{p_1-p_v}{\tfrac12\rho V_1^2}=\Big(\frac{A_1}{A_2}\Big)^2-1.$$

**Why collapse is damaging.** A bubble swept into a high-pressure region collapses inward faster than the liquid can follow; the walls strike the centre and, near a solid surface, an asymmetric micro-jet hits the metal. Repeated impacts pit the surface. Dissolved gas comes out of solution earlier and at a higher pressure than $p_v$ (gaseous cavitation), but it is milder because the bubbles cushion their own collapse.

## Common Traps

- **Trap:** using gauge pressure in the cavitation check.
  - **Why:** $p_v$ is an absolute pressure; gauge pressure at the throat can be negative and still be above $p_v$.
  - **Avoid it by:** converting to absolute: $p_{\rm abs}=p_{\rm atm}+p_{\rm gauge}$.
- **Trap:** continuing to use Bernoulli *through* the cavitating region.
  - **Why:** the pressure stays at $p_v$ in the vapour cavity; the equation only holds up to the onset.
- **Trap:** ignoring temperature.
  - **Avoid it by:** reading $p_v$ at the operating temperature (hot water is the worst case).
- **Trap:** thinking cavitation needs high temperature; it is pressure-triggered at any temperature.

## Example

### Given
Water at 20 °C ($\rho=998$ kg/m³, $p_v=2.339$ kPa abs) flows through a horizontal venturi with $A_1/A_2=1/0.3=3.33$ and inlet pressure $p_1=150$ kPa abs. A pump suction tank is 2 m above the pump inlet, open to the atmosphere (101.3 kPa), with 0.8 m of line loss.

### Approach
Cavitation onset: $p_2=p_v$ in the venturi equation. Pump: compute $NPSH_A$.

### Solution
$$V_1=\sqrt{\frac{2(p_1-p_v)}{\rho\,[(A_1/A_2)^2-1]}}=\sqrt{\frac{2(150\,000-2339)}{998\times10.11}}=5.41\ \text{m/s}.$$
$$NPSH_A=\frac{101\,325-2339}{998\times9.81}+2-0.8=10.11+1.2=11.3\ \text{m}.$$

**Answer:** cavitation begins at $V_1=5.41$ m/s; the pump has 11.3 m of available suction head.
**Key takeaway:** the safe speed grows only as the square root of the pressure margin $p_1-p_v$; and the same suction at 80 °C would lose $(47.4-2.34)/9.79=4.6$ m of NPSH.

## Connections

### Prerequisites
- [[Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]]
- [[Bernoulli Equation|Bernoulli Equation]]

### Related Concepts
- [[Static, Stagnation and Dynamic Pressure|Static, Stagnation and Dynamic Pressure]] — the dynamic pressure in the denominator of $Ca$.
- [[Surface Tension and Capillarity|Surface Tension and Capillarity]] — small bubbles need extra pressure $2\sigma/R$ to stay open.
- [[Important Dimensionless Groups|Important Dimensionless Groups]] — $Ca$ is one of the standard groups.
- [[Pipe Systems and the Three Problems|Pipe Systems and the Three Problems]] — the siphon limit.

### Next
- [[Incompressible Inviscid Flow and Bernoulli - Solved Problems|Bernoulli Solved Problems]] and [[Viscous Flow and Exact Solutions - Solved Problems|Viscous Flow Solved Problems]] (siphon with cavitation limit).

### Cross-domain links
- [[Boiling and Condensation|Boiling and Condensation]] — same liquid–vapour boundary, approached by lowering $p$ instead of raising $T$.
- [[Fracture Mechanics - Stress Intensity and Griffith|Fracture Mechanics — Stress Intensity and Griffith]] — failure starts at the weakest or most stressed point, here the point of lowest pressure; cavitation damage is also a fatigue-like surface failure.

## Quick Recall

> **In one line:** a liquid cavitates where the local **absolute** pressure drops to $p_v(T)$, so find the minimum pressure with Bernoulli and compare.

**Formula / trigger:** $$Ca=\frac{p-p_v}{\tfrac12\rho V^2},\qquad p_{\min}>p_v$$

**Remember:** cold water $p_v=2.3$ kPa, suction limit $\approx10$ m, hot liquids cavitate sooner.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]

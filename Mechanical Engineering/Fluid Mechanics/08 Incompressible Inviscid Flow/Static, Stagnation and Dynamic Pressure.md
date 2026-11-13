---
tags: [concept, fluid-mechanics, inviscid-flow, pressure]
status: draft
aliases: [static pressure, stagnation pressure, dynamic pressure, total pressure, pressure coefficient, stagnation point]
up: "[[Fluid Mechanics - MOC]]"
---

# Static, Stagnation and Dynamic Pressure

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Bernoulli Equation|Bernoulli Equation]], [[Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]] · formulas: [[Incompressible Inviscid Flow and Bernoulli - Formula Bank|Formula Bank §4]]

## Core Idea

> **One-sentence definition:** the **static** pressure $p$ is the pressure of the fluid itself, the **dynamic** pressure $\tfrac12\rho V^2$ is the pressure equivalent of its kinetic energy, and the **stagnation** pressure $p_0=p+\tfrac12\rho V^2$ is what the pressure would be if the flow were slowed to rest without loss.

**Intuition:** a probe pointing into a stream stops the fluid at its nose. The kinetic energy turns into extra pressure there. The probe therefore reads the static pressure plus the dynamic pressure; the difference between the two readings tells you the speed.

## Governing Relations

$$\boxed{p_0=p+\tfrac12\rho V^2}\qquad(\text{incompressible, same elevation})$$

| Pressure | Meaning | Measured by |
|---|---|---|
| static $p$ | thermodynamic pressure in the fluid, felt by an observer moving with it | wall tap, static port, piezometer |
| dynamic $q=\tfrac12\rho V^2$ | kinetic energy per unit volume | $p_0-p$ |
| stagnation $p_0$ | pressure reached when the flow is brought to rest isentropically | Pitot (total-head) tube |
| total (hydraulic) $p_T=p+\tfrac12\rho V^2+\rho gz$ | stagnation plus elevation term | with elevation included |

**Pressure coefficient:**
$$C_p=\frac{p-p_\infty}{\tfrac12\rho U^2}=1-\frac{V^2}{U^2},\qquad C_p=1\ \text{at a stagnation point}$$

**Compressible correction** (ideal gas, isentropic):
$$\frac{p_0}{p}=\Big(1+\frac{k-1}{2}Ma^2\Big)^{k/(k-1)},\qquad p_0-p=\tfrac12\rho V^2\Big(1+\frac{Ma^2}{4}+\dots\Big)$$

**Where:** $U$ = free-stream speed; $p_\infty$ = free-stream static pressure.

**Assumptions:** steady, frictionless, along the stagnation streamline; correction needed above $Ma\approx0.3$ (+2.3 % at $Ma=0.3$).

## Visual

![[FM-B4-pitot-compressibility.png]]

**Figure:** the incompressible formula over-reads dynamic pressure as the Mach number rises; the factor is $1+Ma^2/4+\dots$.

## When To Use

- **Airspeed and flow-speed measurement** with Pitot or Pitot-static probes.
- **Pressure distributions** on bodies (wind loads, aerodynamics): $C_p$ from $+1$ at the nose to negative on a suction side.
- Separating **what pressure a gauge reads** (static) from the **pressure that stopping the flow would produce** (stagnation).

**Recognition pattern:** "total-head tube", "stagnation point", "dynamic pressure", "pressure coefficient" → **$p_0=p+\tfrac12\rho V^2$**.

## Method

1. **Identify** which pressure the problem gives and which it asks for.
2. **Choose** the relation $p_0=p+\tfrac12\rho V^2$ (add $\rho gz$ if heights differ).
3. **Apply** to obtain $V=\sqrt{2(p_0-p)/\rho}$, or $p_0$ from $p$ and $V$.
4. **Check:** compressibility ($Ma$) and that $p_0$ is the same along any streamline of a frictionless flow while $p$ varies.

## Derivation / Why It Works

Bernoulli along the stagnation streamline from far upstream (speed $V$, static pressure $p$) to the stagnation point (speed 0, pressure $p_0$): $p+\tfrac12\rho V^2=p_0+0$. For a gas the energy equation $c_pT+\tfrac12V^2=c_pT_0$ and isentropic relations give the exact series in $Ma$.

## Common Traps

- **Trap:** thinking the fluid *is at* the stagnation pressure.
  - **Why:** it is the pressure the fluid *would reach at rest*; the actual static pressure is lower.
  - **Avoid it by:** naming each pressure by the instrument that reads it.
- **Trap:** using the incompressible formula at $Ma>0.3$.
- **Trap:** using gauge and absolute pressures inconsistently when computing $p_0-p$ (the difference is the same, but the absolute $p_0$ matters in compressible calculations).
- **Trap:** forgetting that in a viscous boundary layer the total pressure is *not* constant.

## Example

### Given
An aircraft at sea level flies at $V=60$ m/s ($\rho=1.225$ kg/m³, $a=340.3$ m/s).

### Solution
$$q=\tfrac12\rho V^2=\tfrac12(1.225)(60)^2=2205\ \text{Pa}.$$
$$Ma=\frac{60}{340.3}=0.176,\qquad\text{correction }\frac{Ma^2}{4}=0.78\ \%.$$
So $p_0-p=2205\times1.0078=2222$ Pa; the incompressible formula under-reads by under 1 %.

**Answer:** dynamic pressure 2205 Pa; stagnation excess 2222 Pa with compressibility.
**Key takeaway:** at 60 m/s the incompressible Pitot formula is good to better than 1 %; at 100 m/s ($Ma\approx0.3$) it is off by 2.3 %.

## Connections

### Prerequisites
- [[Bernoulli Equation|Bernoulli Equation]]
- [[Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]]

### Related Concepts
- [[Pitot Tube and Pressure Measurement|Pitot Tube and Pressure Measurement]]
- [[Vapour Pressure and Cavitation|Vapour Pressure and Cavitation]] — dynamic pressure appears in $Ca$.
- [[Density, Specific Weight and Compressibility|Density and Compressibility]] — $\Delta\rho/\rho\approx Ma^2/2$ at stagnation.

### Next
- [[Pitot Tube and Pressure Measurement|Pitot Tube and Pressure Measurement]]

### Cross-domain links
- [[Isentropic Nozzle Flow and Choking|Isentropic Nozzle Flow and Choking]] — stagnation (total) properties are the reference state for compressible nozzle flow.
- [[Exergy and Reversible Work|Exergy and Reversible Work]] — $p_0$ is the reversible-work level of a moving stream: slowing the flow to rest recovers the kinetic energy as pressure.

## Quick Recall

> **In one line:** $p_0=p+\tfrac12\rho V^2$: stagnation = static + dynamic.

**Formula / trigger:** $$V=\sqrt{\frac{2(p_0-p)}{\rho}},\qquad C_p=1-\frac{V^2}{U^2}$$

**Remember:** a Pitot tube measures $p_0$, a wall tap measures $p$; compressibility adds $Ma^2/4$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** beginner
- **Subjects:** [[Fluid Mechanics - MOC]]

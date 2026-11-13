---
tags: [concept, fluid-mechanics, inviscid-flow, measurement, pitot]
status: draft
aliases: [Pitot tube, Pitot-static tube, Prandtl tube, static tap, wall tap, piezometer, airspeed indicator]
up: "[[Fluid Mechanics - MOC]]"
---

# Pitot Tube and Pressure Measurement

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Static, Stagnation and Dynamic Pressure|Static, Stagnation and Dynamic Pressure]], [[Manometers|Manometers]] · formulas: [[Incompressible Inviscid Flow and Bernoulli - Formula Bank|Formula Bank §5]]

## Core Idea

> **One-sentence definition:** a Pitot-static probe measures the stagnation pressure at its nose and the static pressure at its side ports; the difference is the dynamic pressure, from which the flow speed follows: $V=\sqrt{2(p_0-p_s)/\rho}$.

**Intuition:** one tube faces the flow and brings the fluid to rest, so it senses the static plus dynamic pressure; another reads the static pressure alone. A differential gauge or manometer between them reads exactly the kinetic part.

## Governing Relations

$$\boxed{V=\sqrt{\frac{2\,(p_0-p_s)}{\rho}}}\qquad(Re_D>1000,\ \text{frictionless, negligible elevation difference})$$

**With a differential manometer** (manometer fluid $\rho_m$, reading $h$, flowing fluid $\rho$):

$$p_0-p_s=(\rho_m-\rho)\,g\,h\ \Rightarrow\ V=\sqrt{2gh\Big(\frac{\rho_m}{\rho}-1\Big)}$$

Gas with a liquid manometer ($\rho_m\gg\rho$): $V\approx\sqrt{2gh\rho_m/\rho}$.

| Device | Reads | Notes |
|---|---|---|
| piezometer tube | $p_s+\gamma z$ (HGL) | liquids only, $p_s>p_{\rm atm}$ |
| **wall (static) tap** | static pressure $p_w$ | small, flush, burr-free hole normal to a straight wall |
| **Pitot tube** (total-head tube) | stagnation pressure $p_0$ | points into the flow |
| **Pitot-static (Prandtl) tube** | $p_0-p_s$ | static ports about 8 diameters behind the nose |

**Where:** $p_0$ = stagnation pressure at the nose, $p_s$ = static pressure at the side ports, $h$ = manometer difference.

**Assumptions:** steady, nearly frictionless flow around the nose; probe aligned with the flow; small probe compared with flow scale.

## Visual

![[FM-B1-pitot-static.png]]

**Figure:** the stagnation streamline ends at the nose of the probe, the side ports see the local static pressure, and a differential manometer between the two reads the velocity head.

## When To Use

- **Airspeed** of aircraft, **flow speed** in ducts, wind tunnels and pipes (traversing the probe across the section and integrating $Q=\int u\,dA$).
- **Static-pressure** measurement on walls (tap, piezometer ring).
- Any problem that gives a manometer reading and asks for speed.

**Recognition pattern:** "Pitot tube", "manometer reading across total and static ports", "stagnation pressure reading" → **$V=\sqrt{2\Delta p/\rho}$**.

## Method

1. **Identify** the two pressures (total and static) and the flowing fluid.
2. **Choose** the formula; if a manometer is used, convert its reading to $p_0-p_s=(\rho_m-\rho)gh$.
3. **Apply** $V=\sqrt{2(p_0-p_s)/\rho}$ with the flowing fluid's density.
4. **Check:** misalignment (below about 5°), compressibility ($Ma>0.3$ needs the correction in [[Static, Stagnation and Dynamic Pressure|Static, Stagnation and Dynamic Pressure]]), and unsteady flow (the tube responds too slowly).

## Derivation / Why It Works

The streamline hitting the nose has speed $V$ upstream and zero at the nose; Bernoulli gives $p_0=p+\tfrac12\rho V^2$. Because the streamlines past the probe body are nearly straight and parallel at the side ports, the pressure there equals the free-stream static pressure (no pressure variation normal to straight streamlines, [[Euler's Equations of Fluid Motion|Euler's equations]]). The manometer balances $p_0-p_s$ against a column of height $h$: $(\rho_m-\rho)gh$ (the flowing fluid in the legs partly cancels).

## Common Traps

- **Trap:** forgetting to subtract $\rho$ of the flowing fluid in a liquid-in-liquid manometer.
  - **Avoid it by:** always using $(\rho_m-\rho)$.
- **Trap:** a **static tap** read in curved or turbulent regions (burrs, large holes, bends give errors).
  - **Avoid it by:** straight wall, flush hole, several taps around the circumference.
- **Trap:** using the formula at high Mach number or low Reynolds number ($Re_D<1000$).
- **Trap:** a probe not aligned with the flow: both pressure readings go wrong beyond about 5° yaw.

## Example

### Given
(a) A Pitot-static tube in air ($\rho=1.225$ kg/m³) reads $p_0-p_s=550$ Pa. (b) In a water pipe, a mercury differential manometer ($\rho_m/\rho=13.6$) connected to a Pitot-static tube reads $h=50$ mm.

### Solution
(a) $V=\sqrt{2(550)/1.225}=30.0$ m/s ($Ma=0.088$, compressibility error $Ma^2/4=0.19\%$).

(b) $V=\sqrt{2(9.81)(0.05)(13.6-1)}=3.52$ m/s.

**Answer:** 30.0 m/s in air; 3.52 m/s in water.
**Key takeaway:** the mercury column magnifies a small dynamic pressure into a readable height, but only after the $(\rho_m/\rho-1)$ correction.

## Connections

### Prerequisites
- [[Static, Stagnation and Dynamic Pressure|Static, Stagnation and Dynamic Pressure]]
- [[Manometers|Manometers]]

### Related Concepts
- [[Bernoulli Equation|Bernoulli Equation]]
- [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]
- [[Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]]

### Next
- [[Energy Equation with Head Loss|Energy Equation with Head Loss]] — pipe flow with measured pressure drops.

### Cross-domain links
- [[First-Order Systems - Time Constant and Response|First-Order Systems — Time Constant and Response]] — the tube and gauge form a first-order system with a lag; that is why Pitot tubes are poor for fast-changing flow.
- [[Lab - Strain Gauge Measurement on a Cantilever Beam|Lab — Strain Gauge Measurement on a Cantilever Beam]] — the same idea of converting a mechanical quantity into a measurable one with a calibration.

## Quick Recall

> **In one line:** Pitot reads $p_0$, the side ports read $p_s$, and $V=\sqrt{2(p_0-p_s)/\rho}$.

**Formula / trigger:** $$V=\sqrt{\frac{2(p_0-p_s)}{\rho}},\qquad p_0-p_s=(\rho_m-\rho)gh$$

**Remember:** align within 5°, use the flowing fluid's density, add the compressibility correction above $Ma=0.3$.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** beginner
- **Subjects:** [[Fluid Mechanics - MOC]]

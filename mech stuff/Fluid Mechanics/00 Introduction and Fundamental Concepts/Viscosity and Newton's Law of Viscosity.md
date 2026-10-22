---
tags: [fluid-mechanics, fundamentals, viscosity]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Viscosity and Newton's Law of Viscosity

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Fluids and Solids|Fluids and Solids]]

## Definition

Viscosity is a fluid property observed **only when the fluid is in motion** — it quantifies a fluid's internal resistance to the *rate* of shearing, exactly filling the role that a fluid cannot fill statically (see [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Fluids and Solids|Fluids and Solids]]: no static shear resistance, but plenty of dynamic resistance).

## Newton's law of viscosity

For simple parallel (shear) flow, with velocity $u$ varying only in the direction $y$ perpendicular to the flow:

$$\boxed{\tau = \mu\frac{du}{dy}}$$

- $\tau$ — shear stress (force per unit area) between adjacent fluid layers
- $du/dy$ — velocity gradient (rate of shear strain) across the flow
- $\mu$ — **coefficient of (dynamic) viscosity**, a fluid property with units Pa·s

This is the fluid-mechanics analogue of Hooke's law $\sigma=E\varepsilon$ ([[Strength of materials/01 Stress and Strain/Stress-Strain Diagram and Hooke's Law|Stress-Strain Diagram and Hooke's Law]]): both are linear constitutive laws relating a stress to a *rate or amount* of deformation, but Newton's law relates stress to a strain **rate** ($du/dy$, a rate of angular deformation $\dot\gamma$) rather than to strain itself — a solid's shear stress depends on *how much* it has been sheared, while a fluid's shear stress depends on *how fast* it is being sheared.

## Newtonian fluids

Fluids that obey the linear relation $\tau\propto du/dy$, with $\mu$ constant for a given fluid at fixed temperature and pressure, regardless of the flow condition. Examples: water, air, oil, mercury. $\mu$ is a **true material property**, exactly like Young's modulus $E$ is for a linear-elastic solid.

## Kinematic viscosity

$$\nu = \frac{\mu}{\rho}$$

units m²/s — appears naturally in the [[Fluid Mechanics/01 Dimensionless Numbers/Knudsen Number|Reynolds number]] and diffusion-like terms in the full Navier-Stokes equations (not derived in this vault yet, but the natural next topic after [[Fluid Mechanics/04 Control Volume Analysis/Linear Momentum Equation|Linear Momentum Equation]]).

## Related
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Newtonian and Non-Newtonian Fluids|Newtonian and Non-Newtonian Fluids]]
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Ideal Fluid|Ideal Fluid]]
- [[Strength of materials/01 Stress and Strain/Stress-Strain Diagram and Hooke's Law|Stress-Strain Diagram and Hooke's Law (the solid-mechanics analogue)]]


## Cross-domain links

- [[Cross-Domain Synthesis/Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]] — G vs μ side by side; Maxwell time constant μ/G behind the Deborah number.

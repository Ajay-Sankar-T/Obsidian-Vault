---
tags: [fluid-mechanics, fundamentals, viscosity]
up: "[[Fluid Mechanics - MOC]]"
---

# Viscosity and Newton's Law of Viscosity

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluids and Solids|Fluids and Solids]]

## Definition

Viscosity is a fluid property observed **only when the fluid is in motion** — it quantifies a fluid's internal resistance to the *rate* of shearing, exactly filling the role that a fluid cannot fill statically (see [[Fluids and Solids|Fluids and Solids]]: no static shear resistance, but plenty of dynamic resistance).

## Newton's law of viscosity

For simple parallel (shear) flow, with velocity $u$ varying only in the direction $y$ perpendicular to the flow:

$$\boxed{\tau = \mu\frac{du}{dy}}$$

- $\tau$ — shear stress (force per unit area) between adjacent fluid layers
- $du/dy$ — velocity gradient (rate of shear strain) across the flow
- $\mu$ — **coefficient of (dynamic) viscosity**, a fluid property with units Pa·s

This is the fluid-mechanics analogue of Hooke's law $\sigma=E\varepsilon$ ([[Stress-Strain Diagram and Hooke's Law|Stress-Strain Diagram and Hooke's Law]]): both are linear constitutive laws relating a stress to a *rate or amount* of deformation, but Newton's law relates stress to a strain **rate** ($du/dy$, a rate of angular deformation $\dot\gamma$) rather than to strain itself — a solid's shear stress depends on *how much* it has been sheared, while a fluid's shear stress depends on *how fast* it is being sheared.

## Newtonian fluids

Fluids that obey the linear relation $\tau\propto du/dy$, with $\mu$ constant for a given fluid at fixed temperature and pressure, regardless of the flow condition. Examples: water, air, oil, mercury. $\mu$ is a **true material property**, exactly like Young's modulus $E$ is for a linear-elastic solid.

## Kinematic viscosity

$$\nu = \frac{\mu}{\rho}$$

units m²/s — appears naturally in the [[Nondimensionalisation and the Reynolds Number|Reynolds number]] and in the diffusion-like term of the [[Navier-Stokes Equations|Navier-Stokes equations]]; the full 3-D form of Newton's law is the [[Newtonian Constitutive Relation|Newtonian constitutive relation]], and the stress it feeds is described in [[Stress in a Moving Fluid|Stress in a Moving Fluid]].

## Related
- [[Newtonian and Non-Newtonian Fluids|Newtonian and Non-Newtonian Fluids]]
- [[Ideal Fluid|Ideal Fluid]]
- [[Stress-Strain Diagram and Hooke's Law|Stress-Strain Diagram and Hooke's Law (the solid-mechanics analogue)]]


## Cross-domain links

- [[Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]] — G vs μ side by side; Maxwell time constant μ/G behind the Deborah number.

## See also
- [[Heat Transfer - MOC]] — momentum diffusivity $\nu$ is to viscous shear what thermal diffusivity $\alpha$ is to conduction; their ratio is the Prandtl number.

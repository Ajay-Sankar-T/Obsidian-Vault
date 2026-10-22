---
tags: [synthesis, cross-domain, stress, pressure, viscosity, constitutive-laws]
up: "[[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC]]"
---

# Fluids and Solids — Pressure, Stress and Constitutive Laws

← up: [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]

Fluids and solids are described by the **same stress tensor**. What distinguishes them is only the **constitutive law** — what stress the material develops for a given deformation.

## Pressure is the isotropic stress state

In a static fluid, shear stress is zero, so $\sigma_x=\sigma_y=\sigma_z=-p$ on every plane ([[Fluid Mechanics/00 Introduction and Fundamental Concepts/Fluids and Solids|Fluids and Solids]]). Every plane is principal and the equal principal stresses make **Mohr's circle a single point** ([[Strength of materials/07 Transformation of Stress and Strain/Mohr's Circle for Stress|Mohr's Circle for Stress]]). A solid under hydrostatic compression is in the same state; a fluid just can never leave it while at rest.

## The same cut gives pressure force and hoop stress

[[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Curved Surfaces|Hydrostatic Force on Curved Surfaces]] uses: the net force of a uniform pressure on a curved surface, in any direction, equals pressure times the **projected area** in that direction. [[Strength of materials/11 Thin-Walled Pressure Vessels/Thin Cylindrical and Spherical Pressure Vessels|Thin-walled pressure vessels]] is the same trick turned around: cut a cylinder of radius $r$, length $L$, wall $t$ along its axis. The pressure pushes with $p\,(2rL)$ on the projected area; the wall resists with $2\sigma_h tL$, so

$$\sigma_h=\frac{pr}{t},\qquad \sigma_l=\frac{pr}{2t}\ (\text{end cap: }p\pi r^2=\sigma_l\,2\pi rt).$$

The fluid supplies the load, the solid answers with stress; the force balance is identical.

## Two constitutive laws, one stress–deformation slot

| | Elastic solid | Newtonian fluid |
|---|---|---|
| shear law | $\tau=G\gamma$ | $\tau=\mu\,\dot\gamma=\mu\,\dfrac{du}{dy}$ |
| depends on | **how much** it is sheared | **how fast** it is sheared |
| constant | shear modulus $G=\dfrac{E}{2(1+\nu)}$ | viscosity $\mu$ |
| static shear stress | yes | none |

Sources: [[Strength of materials/01 Stress and Strain/Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law]], [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Viscosity and Newton's Law of Viscosity|Viscosity]]. The two laws have the same form with $G\to\mu$ and $\gamma\to\dot\gamma$: the dashpot response is the time derivative of the spring response, which is why a spring and a dashpot differ by one factor of $j\omega$ in the frequency domain.

## A new bridge: the Deborah number is the Maxwell time constant

Put an elastic spring (stiffness $G$) in **series** with a viscous dashpot ($\mu$): the Maxwell model, the simplest viscoelastic material. This model is **not in the vault yet**, but it is the missing piece between the two notes above. In the force-voltage dictionary of [[Cross-Domain Synthesis/The Mechanical-Electrical Analogy (Impedance Analogy)|the impedance analogy]] a dashpot is $R$ and a spring is $1/C$, so the Maxwell element is a series $RC$ circuit and its time constant is

$$\lambda=\frac{\mu}{G}\quad\leftrightarrow\quad\tau=RC.$$

[[Fluid Mechanics/01 Dimensionless Numbers/Deborah Number|Deborah number]] $De=\lambda/t_{\rm flow}$ then reads as $t_{\rm obs}/\tau$ from [[Cross-Domain Synthesis/Exponential Decay - Time Constants, Damping and Spatial Relaxation|Exponential Decay]], inverted: $De\ll1$ is steady state (fluid), $De\gg1$ is mid-transient (solid). The same material is solid or fluid depending on which side of its own time constant you look.

## Common traps

- Quoting a gauge pressure where a stress is needed: sign (compression negative) and reference differ.
- Applying $\sigma_h=pr/t$ to a thick wall ($r/t\ge10$ rule breaks).
- Using $\mu$ where only a static solid shear exists, or $G$ for flow.

## Related
- [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]]
- [[Strength of materials/Strength of Materials - MOC|Strength of Materials MOC]]
- [[Strength of materials/07 Transformation of Stress and Strain/Stress-Strain Transformation Analogy|Stress-Strain Transformation Analogy]]

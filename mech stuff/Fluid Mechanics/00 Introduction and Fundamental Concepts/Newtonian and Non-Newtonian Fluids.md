---
tags: [fluid-mechanics, fundamentals, viscosity, non-newtonian]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Newtonian and Non-Newtonian Fluids

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]

## Non-Newtonian fluids

Fluids that do **not** obey the linear law $\tau\propto du/dy$ of [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Viscosity and Newton's Law of Viscosity|Newton's Law of Viscosity]]. Examples: blood, milk, polymer solutions, gelatin, starch suspensions, ink, and some high-molecular-weight oils. Because the stress-strain-rate relation isn't a fixed constant slope, $\mu$ is no longer a single material constant — instead an **apparent viscosity** is defined at each shear rate as the local slope/ratio $\tau/(du/dy)$, which itself varies with flow condition.

## The power-law (Ostwald–de Waele) model

A common empirical model for the non-Newtonian relation:

$$\boxed{\tau = m\left(\frac{du}{dy}\right)^n}$$

- $m$ — flow consistency index
- $n$ — flow behaviour index (dimensionless)

| $n$ | Behaviour | Apparent viscosity as shear rate increases |
|---|---|---|
| $n<1$ | **Pseudoplastic** (shear-thinning) | decreases — e.g. paint, blood, ketchup |
| $n=1$ | Newtonian ($m=\mu$) | constant |
| $n>1$ | **Dilatant** (shear-thickening) | increases — e.g. cornstarch-water suspension |

## Connecting to the Deborah number

Time-dependent (viscoelastic) non-Newtonian behavior — where the fluid's response depends not just on the instantaneous shear rate but on its own relaxation history — is classified by the [[Fluid Mechanics/01 Dimensionless Numbers/Deborah Number|Deborah Number]] $De=\lambda/t_{\rm flow}$: a fluid can behave essentially Newtonian/liquid-like on slow timescales ($De\ll1$) yet elastic/solid-like on fast timescales ($De\gg1$) — the same physical substance, different regime, exactly as [[Fluid Mechanics/01 Dimensionless Numbers/Knudsen Number|Knudsen Number]] reclassifies the *same* gas as continuum or free-molecular depending on the length scale of the problem rather than the substance itself.

## Cross-domain: power-law fluids vs strain-hardening solids

The power-law exponent $n$ here is the direct fluid-mechanics cousin of the nonlinear stress-strain exponent used in solid-mechanics plasticity models (e.g. the Ramberg-Osgood relation $\varepsilon=\sigma/E+K(\sigma)^n$, not currently in the Strength of Materials vault but a natural extension of [[Strength of materials/01 Stress and Strain/Stress-Strain Diagram and Hooke's Law|Stress-Strain Diagram and Hooke's Law]]'s discussion of the post-yield, nonlinear portion of the stress-strain curve): both use a single dimensionless exponent to interpolate between "stiffens/thickens as loading increases" and "softens/thins as loading increases," and both reduce to the linear (Newtonian / Hookean) case at the exponent's neutral value.

## Related
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]
- [[Fluid Mechanics/01 Dimensionless Numbers/Deborah Number|Deborah Number]]

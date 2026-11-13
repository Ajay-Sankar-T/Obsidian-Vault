---
tags: [concept, fluid-mechanics, fluid-properties, surface-tension]
status: draft
aliases: [surface tension, capillarity, capillary rise, Young-Laplace, contact angle, Weber number]
up: "[[Fluid Mechanics - MOC]]"
---

# Surface Tension and Capillarity

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Density, Specific Weight and Compressibility|Density and Compressibility]], [[Continuum Concept|Continuum Concept]] · next: [[Vapour Pressure and Cavitation|Vapour Pressure and Cavitation]]

## Core Idea

> **One-sentence definition:** surface tension $\sigma$ is the tensile force per unit length acting along a liquid interface (equivalently, the energy per unit area of new surface), and it makes a curved interface carry a pressure jump.

**Intuition:** a molecule inside the liquid is pulled equally in all directions; one at the surface has neighbours only on one side, so the surface behaves like a stretched elastic skin that tries to shrink its area. Small drops are round and some insects walk on water for the same reason.

## Governing Relations

**Pressure jump across a curved interface (Young–Laplace)**

$$\boxed{\Delta p=p_{\rm inside}-p_{\rm outside}=\sigma\Big(\frac1{R_1}+\frac1{R_2}\Big)}$$

| Shape | $\Delta p$ |
|---|---|
| spherical drop or bubble in a liquid (one surface) | $2\sigma/R$ |
| soap bubble (two surfaces, inside and outside) | $4\sigma/R$ |
| cylindrical jet | $\sigma/R$ |
| plane surface | 0 |

**Capillary rise in a tube of diameter $d$, contact angle $\theta$**

$$\boxed{h=\frac{4\sigma\cos\theta}{\rho g d}}\qquad(\theta<90^\circ:\ \text{rise},\ \ \theta>90^\circ:\ \text{depression})$$

**Capillary length**

$$\ell_c=\sqrt{\frac{\sigma}{\rho g}}\qquad(\text{water: }2.7\ \text{mm})$$

Surface tension matters when the length scale of the problem is of order $\ell_c$ or less (Bond number $Bo=\rho gL^2/\sigma\lesssim1$).

| Interface at 20 °C | $\sigma$ (N/m) | contact angle |
|---|---|---|
| water–air | 0.0728 | about 0° on clean glass |
| mercury–air | 0.48 | about 130°–140° on glass |
| ethanol–air | 0.0223 | about 0° |
| soap solution–air | about 0.025 | |

$\sigma$ falls with temperature (water: 0.0757 N/m at 0 °C, 0.0589 N/m at 100 °C) and drops sharply with surfactants or contamination.

**Where:**
- $\sigma$ = surface tension (N/m = J/m²); $R_1,R_2$ = principal radii of curvature
- $\theta$ = contact angle measured **through the liquid**
- $\rho$ = density of the liquid; $d$ = tube diameter

**Assumptions:** clean surfaces, static meniscus, tube narrow enough that the meniscus is a spherical cap, liquid column weight balanced entirely by the wall pull.

## Visual

![[FM-N5-capillary-rise.png]]

**Figure:** left, rise is inversely proportional to the tube diameter (note the steep growth below 2 mm), and mercury is *depressed* because $\cos140^\circ<0$. Right, the meniscus bends up for a wetting liquid and down for a non-wetting one.

## When To Use

- Droplets, bubbles, sprays, foams, inkjet, microfluidics.
- Small-bore manometers and level tubes (meniscus error).
- Wicking in porous media, paper, soil, plant xylem.
- Any model-scale test where $We$ or $Bo$ could stop the model from being a faithful copy.

**Recognition pattern:** a very small length (millimetre or less), a free interface, or "drop", "bubble", "meniscus", "rises in the tube" → **surface tension**.

## Method

1. **Identify** the interface and whether it has one surface or two (a soap film has two).
2. **Choose** the tool: curved interface → Young–Laplace; liquid in a narrow tube → force balance giving $h=4\sigma\cos\theta/\rho gd$.
3. **Apply** with SI units; use the contact angle through the liquid.
4. **Check** that $d$ is small enough for the formula (compare with $\ell_c$) and that the sign of $\cos\theta$ gives rise or depression correctly.

## Derivation / Why It Works

**Drop.** Cut a spherical drop in half. The pressure excess pushes the halves apart over the area $\pi R^2$; surface tension pulls them together along the circumference $2\pi R$:
$$\Delta p\,\pi R^2=\sigma\,2\pi R\ \Rightarrow\ \Delta p=\frac{2\sigma}{R}.$$

**Capillary rise.** The wall pulls the meniscus up with vertical force $\sigma\cos\theta\,\pi d$. It balances the weight of the lifted column $\rho g\,h\,\pi d^2/4$:
$$\sigma\cos\theta\,\pi d=\rho g h\frac{\pi d^2}{4}\ \Rightarrow\ h=\frac{4\sigma\cos\theta}{\rho gd}.$$

The same dimensional argument appears as the capillary-rise example of the [[Buckingham Pi Theorem|Π theorem]]: $h/d=F(\rho g d^2/\sigma,\theta)$.

## Common Traps

- **Trap:** using $2\sigma/R$ for a soap bubble.
  - **Why:** a bubble has an inner and an outer surface.
  - **Avoid it by:** counting surfaces; use $4\sigma/R$.
- **Trap:** reading the contact angle through the gas instead of through the liquid.
  - **Avoid it by:** sketching the meniscus and measuring inside the liquid.
- **Trap:** applying the capillary formula to wide tubes (several $\ell_c$) or ignoring the meniscus entirely in a thin manometer tube.
- **Trap:** quoting $\sigma$ for "water" without noting temperature or contamination.

## Example

### Given
(a) A water drop of radius 0.5 mm in air. (b) A soap bubble of radius 25 mm, $\sigma=0.025$ N/m. (c) Clean water in a glass tube of diameter 1 mm.

### Solution
(a) $\Delta p=2(0.0728)/0.0005=291$ Pa.
(b) $\Delta p=4(0.025)/0.025=4.0$ Pa.
(c) $h=\dfrac{4(0.0728)(1)}{998\times9.81\times0.001}=0.0297$ m.

**Answer:** 291 Pa, 4.0 Pa, 29.7 mm.
**Key takeaway:** the pressure jump grows as the radius shrinks (a 0.5 mm drop is already 3 mbar), and $h\propto1/d$, so a tube three times wider (3 mm) lifts the water only 9.9 mm.

## Connections

### Prerequisites
- [[Density, Specific Weight and Compressibility|Density and Compressibility]]
- [[Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]

### Related Concepts
- [[Manometers|Manometers]] — meniscus error in small-bore tubes.
- [[Important Dimensionless Groups|Important Dimensionless Groups]] — Weber and Bond numbers.
- [[Boundary Conditions in Fluid Flow|Boundary Conditions in Fluid Flow]] — the pressure jump becomes the free-interface boundary condition.
- [[Vapour Pressure and Cavitation|Vapour Pressure and Cavitation]] — bubble stability depends on $2\sigma/R$.

### Next
- [[Flow Similarity and Model Studies|Flow Similarity and Model Studies]] — when $We$ must be matched.

### Cross-domain links
- [[Thin Cylindrical and Spherical Pressure Vessels|Thin Cylindrical and Spherical Pressure Vessels]] — $\Delta p=2\sigma/R$ is the thin-sphere formula $p=2t\sigma_{\rm hoop}/R$ with the membrane force per length $t\sigma_{\rm hoop}$ replaced by $\sigma$: a liquid skin is a pressure vessel of zero thickness whose "wall" has a fixed tension.
- [[Fracture Mechanics - Stress Intensity and Griffith|Fracture Mechanics — Stress Intensity and Griffith]] — surface energy per unit area is the same quantity: creating new area costs energy $\sigma$ per unit area.
- [[Boiling and Condensation|Boiling and Condensation]] — bubble nucleation sizes are set by the Laplace pressure.

## Quick Recall

> **In one line:** $\sigma$ is the pull of an interface; curvature turns it into a pressure jump $\sigma(1/R_1+1/R_2)$, and in a narrow tube it lifts a column $h=4\sigma\cos\theta/\rho gd$.

**Formula / trigger:** $$\Delta p=\frac{2\sigma}{R}\ (\text{drop}),\quad\frac{4\sigma}{R}\ (\text{bubble}),\quad h=\frac{4\sigma\cos\theta}{\rho gd}$$

**Remember:** water: $\sigma=0.0728$ N/m, $\ell_c=2.7$ mm, rise in 1 mm tube = 30 mm.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** beginner
- **Subjects:** [[Fluid Mechanics - MOC]]

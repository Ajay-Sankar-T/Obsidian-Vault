---
tags: [fluid-mechanics, fundamentals, continuum]
up: "[[Fluid Mechanics - MOC]]"
---

# Continuum Concept

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · governs validity of: [[Lagrangian and Eulerian Descriptions|Lagrangian and Eulerian Descriptions]]

## The assumption

Fluid mechanics treats properties like pressure, velocity, temperature, and density as **continuous functions of space and time** — $p(x,y,z,t)$, $\mathbf V(x,y,z,t)$ — rather than acknowledging that, at the molecular scale, a fluid is actually a swarm of discrete, colliding particles with enormous gaps between them. This is the **continuum hypothesis**: at each mathematical "point," properties are really local averages over a volume large enough to contain many molecules but small enough to be effectively a point on the macroscopic scale of the problem.

## When it's valid

Valid whenever the mean free path of molecules is much smaller than the smallest length scale of the flow — this is exactly what [[Knudsen Number|Knudsen Number]] $Kn=\lambda/L$ quantifies. For ordinary liquids and gases at everyday scales ($Kn<0.01$), the continuum assumption holds essentially perfectly; it breaks down for rarefied gases (very low pressure, e.g. high-altitude or vacuum-chamber flows) or for flows at extremely small length scales (micro/nanofluidics), where $L$ shrinks toward $\lambda$.

## Why every governing equation in this vault depends on it

The differential forms of the conservation laws — the [[Conservation of Mass (Continuity Equation)|differential continuity equation]] $\partial\rho/\partial t+\nabla\cdot(\rho\mathbf V)=0$ and the momentum equations used in [[Linear Momentum Equation|Linear Momentum Equation]] — are only meaningful if $\rho(x,y,z,t)$ and $\mathbf V(x,y,z,t)$ are differentiable fields. A discrete swarm of molecules has no well-defined derivative at a point; the continuum hypothesis is what licenses treating fluid mechanics as a subject of partial differential equations at all, in the same way the [[Concept of Stress|Concept of Stress]] note's stress field $\sigma(x,y,z)$ implicitly assumes a solid continuum (no individual atoms/crystal grains resolved).

## Related
- [[Knudsen Number|Knudsen Number]]
- [[Lagrangian and Eulerian Descriptions|Lagrangian and Eulerian Descriptions]]

## See also (concept notes)

- [[Density, Specific Weight and Compressibility]] — density as the continuum limit.

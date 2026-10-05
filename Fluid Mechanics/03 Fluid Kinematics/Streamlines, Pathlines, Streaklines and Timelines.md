---
tags: [fluid-mechanics, kinematics, streamlines]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Streamlines, Pathlines, Streaklines and Timelines

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/03 Fluid Kinematics/Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]

## Streamline

A curve everywhere tangent to the **instantaneous** velocity field:

$$\boxed{\frac{dx}{u}=\frac{dy}{v}=\frac{dz}{w}}\qquad\text{2D: }\boxed{\frac{dy}{dx}=\frac vu}$$

**Worked example** ($\mathbf V=(x,-y)$, from [[Fluid Mechanics/03 Fluid Kinematics/Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]): $\dfrac{dy}{dx}=-\dfrac yx\Rightarrow\dfrac{dy}{y}=-\dfrac{dx}{x}\Rightarrow\ln y=-\ln x+C$, so

$$\boxed{xy=C}$$

— a family of hyperbolas, the classic stagnation-point flow pattern. This is a **separable first-order ODE**, solved with exactly the technique in [[First Order ODEs|First Order ODEs]] — streamline equations are, quite literally, an application of separable/exact ODE methods to a velocity field.

## The four curves compared

| Concept | Meaning |
|---|---|
| **Streamline** | instantaneous curve tangent to velocity (a snapshot; changes if the field is unsteady) |
| **Pathline** | the actual trajectory traced by *one* fluid particle over time (Lagrangian, [[Fluid Mechanics/03 Fluid Kinematics/Lagrangian and Eulerian Descriptions\|Lagrangian and Eulerian Descriptions]]) |
| **Streakline** | the locus of *all* particles that have, at some point, passed through one fixed point |
| **Timeline** | the shape formed by a set of particles all marked simultaneously, observed at a later time |

## The steady-flow simplification

$$\boxed{\text{Steady flow: Streamline}=\text{Pathline}=\text{Streakline}}$$

Because in steady flow the velocity field itself doesn't change with time, a particle's future path always follows the *same* instantaneous tangent curve it started on, and every particle threading through a fixed point traces the identical curve thereafter — the three otherwise-distinct concepts collapse into one. In **unsteady** flow they generically differ, and distinguishing them is essential (e.g. in flow visualization: dye injection shows a streakline, not a streamline, unless the flow happens to be steady).

## Related
- [[Fluid Mechanics/03 Fluid Kinematics/Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]
- [[First Order ODEs|First Order ODEs (the ODE technique that solves streamline equations)]]

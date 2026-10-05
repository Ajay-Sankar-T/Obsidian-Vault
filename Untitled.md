# Fluid Mechanics — Introduction and Fundamental Concepts I

## Lecture metadata
- **Course:** Fluid Mechanics
- **Lecture:** Mod-01 Lec-01
- **Instructor:** Prof. S. K. Som, IIT Kharagpur
- **Source:** NPTEL
- **Duration:** 51:58

## Main idea
Fluid mechanics studies the behavior of **liquids and gases**, focusing on how they move, what forces act on them, and how properties like pressure, velocity, density, and viscosity describe that motion. [page:1]

## Why fluid mechanics matters
- Fluid flow is present in many natural and engineering situations.
- Examples include breathing, blood circulation, atmospheric pressure, pipe flow, aircraft, submarines, and space systems.
- The subject is important both for daily life and for engineering design. [page:1]

## Course outline
The lecture briefly lists the major topics in the course:
- Introduction and fundamental concepts.
- Fluid statics.
- Kinematics of fluids.
- Conservation equations for fluid flow.
- Fluid flow applications.
- Viscous incompressible flow.
- Pipe flow.
- Principles of similarity.
- Ideal fluid flow.
- Free-surface flow.
- Unsteady flow phenomena.
- Laminar boundary layers.
- Turbulent flow. 

## Fluid vs solid
### Solid
- A solid can resist a tangential force or shear stress in static equilibrium.
- It undergoes a finite deformation.
- When the load is removed, it may recover its original shape, fully or partly. 

### Fluid
- A fluid keeps deforming continuously when shear stress is applied.
- It cannot sustain tangential stress in static equilibrium.
- When the load is removed, it does not return to its original shape in the usual case.
- This is why fluids are described as having “zero memory” behavior, except in special viscoelastic cases. 

## Continuum concept
- In fluid mechanics, properties such as pressure, velocity, and temperature are treated as continuous functions of space and time.
- This assumes the fluid behaves like a continuous medium rather than as separate molecules.
- The assumption is valid for ordinary conditions in most solids, liquids, and many gases. 
## Knudsen number and validity of continuum
- The mean free path \( \lambda \) is the average distance a molecule travels between two collisions.
- The characteristic dimension of the problem is \( L \).
- The ratio \( \lambda/L \) is the **Knudsen number**.
- Flow regimes mentioned in the lecture:
$$
  ( \lambda/L < 0.01 ): continuum valid. 
  ( 0.01 < \lambda/L < 0.1 ): slip flow.
  ( 0.1 < \lambda/L < 10 ): transition regime.
  ( lambda/L > 10 ): free molecular flow. $$
## Viscosity
- Viscosity is a property of a fluid, but it is observed only when the fluid is in motion.
- In simple parallel flow, shear stress \( \tau \) is proportional to velocity gradient \( du/dy \).
- This is written as:
  \[
  \tau = \mu \frac{du}{dy}
  \]
- Here \( \mu \) is the coefficient of viscosity. [page:1]

## Newtonian fluids
- Fluids that obey the linear relation between shear stress and velocity gradient are **Newtonian fluids**.
- For these fluids, viscosity is a true fluid property and remains constant for a given fluid under the same conditions.
- Common examples mentioned: water, air, oil, mercury. [page:1]

## Non-Newtonian fluids
- Fluids that do not obey the linear law \( \tau \propto du/dy \) are **non-Newtonian fluids**.
- Examples mentioned: blood, milk, polymer solutions, gelatin, starch suspensions, ink, and some high molecular weight oils.
- For non-Newtonian fluids, viscosity may depend on flow conditions, so it is called **apparent viscosity**. [page:1]

## Power-law model
A simple model for some non-Newtonian fluids is the Ostwald–de Waele power-law relation:
\[
\tau = m \left(\frac{du}{dy}\right)^n
\]
- \( m \): flow consistency index.
- \( n \): flow behavior index.
- If \( n < 1 \), the fluid is **pseudoplastic**.
- If \( n > 1 \), the fluid is **dilatant**. [page:1]

## Ideal fluid
- An ideal fluid is defined as a fluid with zero viscosity.
- This is a hypothetical model, since real fluids always have viscosity greater than zero.
- The concept is still useful for simplifying analysis in some fluid mechanics topics. [page:1]
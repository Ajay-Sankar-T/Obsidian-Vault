---
tags:
  - fluid-mechanics
  - MOC
  - course
course: AM2530 Fluid Mechanics
instructor: Dr. Anubhab Roy
---

# Fluid Mechanics — Map of Content

Part of [[00 Home|Ajay's Engineering Wiki]]. For future LLM-assisted edits, follow [[LLM Wiki Guide]].

This is the index note for the course, reorganized into topic folders (previously a single flat, partly-empty "Lecture 1" folder). Every note links back here and to its neighbors, and cross-links into [[Strength of materials/Strength of Materials - MOC|Strength of Materials]], [[EE1100 Basic Electrical Engineering/EE1100 MOC|EE1100]], and [[ODE (Ordinary Differential Equations)|Differential Equations]] wherever the same underlying mathematics reappears — see [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis]] for the fully worked-out connections.

## 00 Introduction and Fundamental Concepts
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Introduction|Introduction]]
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Fluids and Solids|Fluids and Solids]]
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Static Equilibrium|Static Equilibrium]]
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Continuum Concept|Continuum Concept]]
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Viscosity and Newton's Law of Viscosity|Viscosity and Newton's Law of Viscosity]]
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Newtonian and Non-Newtonian Fluids|Newtonian and Non-Newtonian Fluids]]
- [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Ideal Fluid|Ideal Fluid]]

## 01 Dimensionless Numbers
- [[Fluid Mechanics/01 Dimensionless Numbers/Buckingham Pi Theorem|Buckingham π Theorem]] — the general method that produces every dimensionless number below (Re, Fr, We, Eu, Ma, Kn, De)
- [[Fluid Mechanics/01 Dimensionless Numbers/Knudsen Number|Knudsen Number]]
- [[Fluid Mechanics/01 Dimensionless Numbers/Deborah Number|Deborah Number]]

## 02 Fluid Statics
- [[Fluid Mechanics/02 Fluid Statics/Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]
- [[Fluid Mechanics/02 Fluid Statics/Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]]
- [[Fluid Mechanics/02 Fluid Statics/Manometers|Manometers]]
- [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces and Centre of Pressure]]
- [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Curved Surfaces|Hydrostatic Force on Curved Surfaces]]
- [[Fluid Mechanics/02 Fluid Statics/Buoyancy and Archimedes' Principle|Buoyancy and Archimedes' Principle]]
- [[Fluid Mechanics/02 Fluid Statics/Stability of Floating Bodies - Metacentre|Stability of Floating Bodies — Metacentre]]

## 03 Fluid Kinematics
- [[Fluid Mechanics/03 Fluid Kinematics/Lagrangian and Eulerian Descriptions|Lagrangian and Eulerian Descriptions]]
- [[Fluid Mechanics/03 Fluid Kinematics/Material Derivative and Fluid Acceleration|Material Derivative and Fluid Acceleration]]
- [[Fluid Mechanics/03 Fluid Kinematics/Streamlines, Pathlines, Streaklines and Timelines|Streamlines, Pathlines, Streaklines and Timelines]]

## 04 Control Volume Analysis
- [[Fluid Mechanics/04 Control Volume Analysis/System and Control Volume|System and Control Volume]]
- [[Fluid Mechanics/04 Control Volume Analysis/Reynolds Transport Theorem|Reynolds Transport Theorem]]
- [[Fluid Mechanics/04 Control Volume Analysis/Conservation of Mass (Continuity Equation)|Conservation of Mass (Continuity Equation)]]
- [[Fluid Mechanics/04 Control Volume Analysis/Linear Momentum Equation|Linear Momentum Equation]]
- [[Fluid Mechanics/04 Control Volume Analysis/Momentum Equation Applications - Jets, Vanes, Bends|Momentum Equation Applications — Jets, Vanes, Bends]]

## 05 Centroids and Centre of Mass
- [[Fluid Mechanics/05 Centroids and Centre of Mass/Centre of Mass and Centroids|Centre of Mass and Centroids]]
- [[Fluid Mechanics/05 Centroids and Centre of Mass/Composite Bodies and Cutouts|Composite Bodies and Cutouts]]
- [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area]]

## The four biggest problem-solving ideas

$$\boxed{\text{Hydrostatics: }P=\rho gh}\qquad\boxed{\text{Curved surface: }H\to\text{projection},\ V\to\text{imaginary-fluid weight}}$$
$$\boxed{\text{Mass: Inflow}-\text{Outflow}=\text{Accumulation}}\qquad\boxed{\text{Momentum: Force}=\text{Momentum out}-\text{Momentum in}}$$

And for floating-body stability: $I_O\to BM=\dfrac{I_O}{V_{\rm sub}}\to GM=BM-BG\to\boxed{GM>0\Rightarrow\text{stable}}$.

## Cross-domain synthesis

Continuity ↔ KCL, momentum/RTT ↔ Reynolds Transport bookkeeping shared with circuit nodal analysis, metacentric stability ↔ column buckling, centroids/second moments of area shared directly with beam bending — see [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis]] for the six fully worked connections across all four vaults.

## Study log
- [ ] Introduction and Fundamental Concepts
- [ ] Dimensionless Numbers
- [ ] Fluid Statics
- [ ] Fluid Kinematics
- [ ] Control Volume Analysis
- [ ] Centroids and Centre of Mass

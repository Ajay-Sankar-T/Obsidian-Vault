---
tags: [synthesis, cross-domain, conservation-laws, kcl, continuity, bernoulli]
up: "[[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC]]"
---

# Conservation Laws and Flow Networks

← up: [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]

Every network in the vault has the same two-law skeleton: a **node law** (what flows in flows out) and a **loop law** (potential differences around a closed path sum to zero), glued together by an element law. This note lines them up for circuits, pipes and structures.

## The three networks

| | Circuit | Pipe flow | Structure (bars and rigid links) |
|---|---|---|---|
| through quantity (conserved at a node) | current $I$ | volume/mass flow $Q$, $\dot m$ | force $F$ |
| across quantity (sums to zero in a loop) | voltage $V$ | pressure/head $p$ | displacement $\delta$ |
| node law | KCL | continuity $\sum\dot m_{\rm in}=\sum\dot m_{\rm out}$ | equilibrium $\sum F=0$ |
| loop law | KVL | Bernoulli between two points | compatibility (deformations fit) |
| dissipative element | $R$ | friction head loss $h_f$ | — |
| stores "potential" | capacitor $\tfrac12CV^2$ | tank, pressure/elevation $p+\rho gz$ | spring/bar $\tfrac12k\delta^2$ |
| stores "kinetic" | inductor $\tfrac12LI^2$ | moving fluid $\tfrac12\rho V^2$ | mass $\tfrac12mv^2$ |

Sources: [[01 Basic Concepts and Basic Laws|Basic Laws]], [[Fluid Mechanics/04 Control Volume Analysis/Conservation of Mass (Continuity Equation)|Conservation of Mass]], [[Fluid Mechanics/08 Incompressible Inviscid Flow/Incompressible Inviscid Flow and Bernoulli - Formula Bank|Bernoulli Formula Bank]], [[Strength of materials/02 Axial Loading/Statically Indeterminate Axial Members|Statically Indeterminate Axial Members]].

**A warning about the dictionary.** [[Cross-Domain Synthesis/The Mechanical-Electrical Analogy (Impedance Analogy)|The Mechanical-Electrical Analogy]] uses force ↔ voltage, which is right for one oscillator equation. For **networks** of joints and members, equilibrium is a node law, so force must be the **through** variable (force ↔ current, displacement ↔ voltage, stiffness ↔ conductance). Pick the analogy by the job, and say which one you are using.

## What the table buys you

- **Force sharing is a current divider.** Bars in parallel share one displacement and their forces add, so each carries a share proportional to its stiffness $AE/L$, exactly as parallel conductances split a current ([[Voltage Divider Rule|Voltage Divider Rule]] and its dual). Springs in parallel add stiffness like conductances.
- **Statically indeterminate = a circuit KCL alone cannot solve.** Equilibrium gives the node law, compatibility the loop law; you need both, as in Tutorial 5 ([[Strength of materials/Tutorial 5 - Axial Loading/Q6 - Bolt and Tube Assembly|bolt and tube]]).
- **Bernoulli is KVL for an ideal pipe.** Between two points, $\tfrac12\rho V^2+p+\rho gz$ is a conserved sum like a loop of ideal elements; adding $h_f$ turns the loop law into KVL with resistors. $\tfrac12\rho V^2$ is the inductor energy: for a pipe segment of length $\ell$ and area $A$, inertance $L_h=\rho\ell/A$ and $Q=AV$ give $\tfrac12L_hQ^2=\tfrac12\rho V^2(A\ell)$, energy density $\tfrac12\rho V^2$.
- **A tank is a capacitor.** For an open tank of area $A$ with $p=\rho gh$, $Q=A\,dh/dt=(A/\rho g)\,dp/dt$, so $C_h=A/\rho g$. Stored mass (like charge) cannot jump; only the rate of change is set by the net flow.

## Correction to carry forward

The continuity note's cross-domain paragraph pairs a filling tank with **inductor current continuity**. The stored conserved quantity there is mass, whose electrical twin is charge on a capacitor, so the matching rule is $v_C(0^+)=v_C(0^-)$ ([[AC Transients|AC Transients]]). Inertia of moving fluid is what matches the inductor. That note has been adjusted accordingly.

## Where energy enters

KVL, Bernoulli and compatibility all hide an energy balance, which is why [[Cross-Domain Synthesis/Energy Methods - A Unified View|Energy Methods — A Unified View]] and [[Cross-Domain Synthesis/The Universal Second-Order Linear System|the second-order system]] reappear whenever a network has both a "potential" store and a "kinetic" store.

## Related
- [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]]
- [[EE1100 MOC|EE1100 MOC]]
- [[Strength of materials/Strength of Materials - MOC|Strength of Materials MOC]]

## Cross-domain links
- [[Foundations of Thermal Engineering - MOC]] — a power cycle or refrigeration plant is a network of components, each obeying mass and energy balance.
- [[Heat Transfer - MOC]] — thermal resistance networks are solved like KCL/KVL networks, with temperature in place of voltage.

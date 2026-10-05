---
tags: [fluid-mechanics, fluid-statics, manometers]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Manometers

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/02 Fluid Statics/Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]

## The one rule that solves every manometer problem

Starting from a known-pressure point, walk through the connected fluid column toward the unknown point:

$$\boxed{\text{Moving DOWN}\rightarrow+\rho gh}\qquad\qquad\boxed{\text{Moving UP}\rightarrow-\rho gh}$$

$$\boxed{\text{Same level, same continuous fluid}\rightarrow P_1=P_2}$$

This is nothing more than repeated application of $P_2=P_1+\rho gh$ from [[Fluid Mechanics/02 Fluid Statics/Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]], plus the "pressure depends only on depth" fact from [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Static Equilibrium|Static Equilibrium]] that licenses equating pressures at the same horizontal level within one connected fluid.

## Piezometer

The simplest manometer — a vertical open tube connected directly to the pressure point:

$$\boxed{P=\rho gh}$$

(gauge pressure, $h$ = height the fluid rises in the tube). Only works for moderate positive gauge pressures in liquids (a large $P$ would need an impractically tall tube; a negative gauge pressure can't be read at all since the tube would need to "suck" fluid up from nothing).

## General procedure

1. Identify the known-pressure reference point (often atmospheric, $P=0$ gauge).
2. Trace a path through the connected fluid(s) to the unknown point, applying $+\rho gh$ for every downward step and $-\rho gh$ for every upward step, using the density of *whichever fluid occupies that segment* (multi-fluid manometers require tracking density changes at each interface).
3. Set the total equal to the unknown pressure.

## Related
- [[Fluid Mechanics/02 Fluid Statics/Pressure and the Hydrostatic Equation|Pressure and the Hydrostatic Equation]]
- [[Fluid Mechanics/02 Fluid Statics/Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]]

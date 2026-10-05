---
tags: [fluid-mechanics, fluid-statics, pressure]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Pressure and the Hydrostatic Equation

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Static Equilibrium|Static Equilibrium]]

## Pressure

$$\boxed{P=\frac FA},\qquad \boxed{1\ \text{Pa}=1\ \text{N/m}^2}$$

## The hydrostatic equation

Balancing the pressure-gradient force against gravity on a static fluid element (derived from [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Static Equilibrium|Static Equilibrium]]'s force balance), with $z$ measured positive upward:

$$\boxed{\frac{dP}{dz}=-\rho g}$$

For constant density (incompressible fluid):

$$\boxed{P+\rho gz=C}\qquad\Longrightarrow\qquad \boxed{P_2-P_1=\rho g(z_1-z_2)}$$

If point 2 is a depth $h$ **below** point 1:

$$\boxed{P_2=P_1+\rho gh}$$

**Key idea:** pressure increases with depth, and — critically — depends **only** on vertical depth, never on horizontal position or on the shape of the container (a direct consequence of $\partial p/\partial x=\partial p/\partial y=0$ noted in [[Fluid Mechanics/00 Introduction and Fundamental Concepts/Static Equilibrium|Static Equilibrium]]). This is the "hydrostatic paradox": a thin tall tube and a wide tank of the same fluid at the same depth exert the same *pressure* on their base, regardless of total weight.

## Pressure head

$$\boxed{h_p=\frac{P}{\rho g}}$$

The equivalent height of a column of the fluid whose weight-per-area produces the given pressure — used to report pressures as "mm Hg," "m of water," etc., and directly usable in [[Fluid Mechanics/02 Fluid Statics/Manometers|Manometers]].

## Related
- [[Fluid Mechanics/02 Fluid Statics/Absolute, Gauge and Vacuum Pressure|Absolute, Gauge and Vacuum Pressure]]
- [[Fluid Mechanics/02 Fluid Statics/Manometers|Manometers]]
- [[Fluid Mechanics/02 Fluid Statics/Hydrostatic Force on Plane Surfaces and Centre of Pressure|Hydrostatic Force on Plane Surfaces and Centre of Pressure]]

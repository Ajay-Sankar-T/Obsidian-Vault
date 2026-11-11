---
title: Viscous Flow and Exact Solutions – Formula Bank
tags: [fluid-mechanics, formula-bank, navier-stokes, laminar-flow, poiseuille, couette]
up: "[[Fluid Mechanics - MOC]]"
source: "GPS 9 & 10 data sheet (Fox, McDonald and Pritchard, 8th ed., ch. 5 and 8)"
aliases: [Navier-Stokes exact solutions, Poiseuille flow, Couette flow, Hagen-Poiseuille, laminar film flow]
---

# Viscous Flow and Exact Solutions – Formula Bank

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Viscosity and Newton's Law of Viscosity]], [[Pipe Flow and Losses - Formula Bank]] · worked problems: [[Viscous Flow and Exact Solutions - Solved Problems]]

Numbers in the solved problems are recomputed in `Tools/fm_gps9_10.py`.

## 1. The recipe for a unidirectional flow

A flow with one velocity component that depends on one coordinate, $u=u(y)$ (or $u(r)$), is an **exact solution** of Navier–Stokes. Steps:

1. **Continuity** is satisfied ($\partial u/\partial x=0$), so $v=w=0$.
2. **Cross-stream momentum** gives $\partial p/\partial y=\rho g_y$: pressure is hydrostatic across the flow.
3. **Streamwise momentum** collapses to one ODE (the data sheet's $0=-\dfrac{dp}{dx}+\mu\dfrac{1}{r}\dfrac{d}{dr}\!\Big(r\dfrac{du}{dr}\Big)$ for pipes and annuli, $0=\rho g_x-\dfrac{dp}{dx}+\mu\dfrac{d^2u}{dy^2}$ for plates).
4. **Integrate twice**, apply two boundary conditions: no-slip on a wall, zero shear $\mu\,du/dy=0$ on a free surface, or a moving wall speed.
5. Read off $Q=\int u\,dA$, $V=Q/A$, $\tau_w=\mu\,du/dn$ at the wall.

The only things that change from case to case are the geometry and the boundary conditions. $\mu$ cancels from the *shape* of the profile when the driver is a pressure gradient or gravity; it sets the *amount*.

## 2. The solutions to know

| Case | Boundary conditions | $u$ | $Q$ (per width or total) | Wall shear |
|---|---|---|---|---|
| **Plane Couette** (plate gap $h$, top plate at $U$, no $dp/dx$) | $u(0)=0,\ u(h)=U$ | $U\,y/h$ | $Uh/2$ per unit width | $\mu U/h$ |
| **Plane Poiseuille** (fixed plates, gap $h$) | $u(0)=u(h)=0$ | $\dfrac{-dp/dx}{2\mu}\,y(h-y)$ | $\dfrac{-dp/dx\;h^3}{12\mu}$ per unit width | $\tau_w=\dfrac{h}{2}\Big(-\dfrac{dp}{dx}\Big)=\dfrac{6\mu Q}{wh^2}$ |
| **Couette + Poiseuille** | $u(0)=0,\ u(h)=U_p$ | $\dfrac{-dp/dx}{2\mu}y(h-y)+U_p\dfrac yh$ | $\dfrac{-dp/dx\;h^3}{12\mu}+\dfrac{U_ph}{2}$ | at each wall from $\mu\,du/dy$ |
| **Film down an incline** (depth $h$, angle $\theta$, free surface) | $u(0)=0,\ du/dy(h)=0$ | $\dfrac{\rho g\sin\theta}{2\mu}(2hy-y^2)$ | $\dfrac{\rho g\sin\theta\,h^3}{3\mu}$ per unit width | $\tau_{\text{bed}}=\rho gh\sin\theta$ |
| **Circular pipe** (radius $R$) | $u(R)=0$, finite at $r=0$ | $\dfrac{-dp/dx}{4\mu}(R^2-r^2)$ | $\dfrac{\pi R^4}{8\mu}\Big(-\dfrac{dp}{dx}\Big)=\dfrac{\pi d^4\Delta p}{128\mu L}$ | $\tau_w=\dfrac{8\mu V}{d}=\dfrac{d\,\Delta p}{4L}$ |
| **Annulus, $dp/dx=0$** (wire radius $a$ moving at $U$ in a die of radius $R$) | $u(a)=U,\ u(R)=0$ | $U\dfrac{\ln(R/r)}{\ln(R/a)}$ | $\pi U\Big[\dfrac{R^2-a^2}{2\ln(R/a)}-a^2\Big]$ | on wire $\dfrac{\mu U}{a\ln(R/a)}$ |

Useful ratios: plane Poiseuille $u_{\max}=\tfrac32V$, pipe $u_{\max}=2V$, film surface $u_s=\tfrac32V$. Kinetic-energy factor $\alpha=2$ for the pipe parabola.

> [!tip] Resistance picture
> Laminar flow is linear: $\Delta p=R_h\,Q$ with $R_h=\dfrac{12\mu L}{wh^3}$ (plates) or $\dfrac{128\mu L}{\pi d^4}$ (pipe). Series and parallel connections add like resistors (see the GPS 10 syringe and dashpot problems). The $h^3$ and $d^4$ are what make small channels so sensitive to size.

## 3. Regimes and limits

- Pipe: laminar for $Re=\rho Vd/\mu<2300$. Plates: laminar for $Re=\rho\bar Vh/\mu<1400$.
- The solutions need **fully developed** flow. The entry length is roughly $0.06\,Re\,d$ for a pipe, negligible at low $Re$ (not on the data sheet; use as a check).
- **Thin gap:** a curved gap of width $h\ll$ radius behaves as a plane gap of perimeter $\pi D$ (dashpot, wire die).

## 4. Stresses and creeping flow

Newtonian stress tensor (data sheet): $\sigma_{xx}=-p+2\mu\,\partial u/\partial x$, $\sigma_{yy}=-p+2\mu\,\partial v/\partial y$, $\tau_{xy}=\mu(\partial u/\partial y+\partial v/\partial x)$.

At a no-slip wall $\partial u/\partial x=0$, so the viscous normal stress vanishes there and only the shear $\mu\,\partial u/\partial y$ acts on the wall.

Scaling the Navier–Stokes equations with length $\ell$, speed $U$ gives inertia/viscous $=\rho U\ell/\mu=Re$. For $Re\ll1$ inertia drops and the equations are linear (Stokes flow): $\nabla p=\mu\nabla^2\mathbf u$. A velocity field can satisfy continuity and the boundary conditions yet fail momentum; whether it is an *exact* solution is decided by whether a pressure exists, i.e. $\partial^2p/\partial x\partial y$ must be the same from both components.

## 5. Cross-domain

- The laminar profile satisfies a Poisson equation $\nabla^2u=\text{const}$, the same equation as torsion of a bar (Prandtl's membrane analogy). The circular case gives $d^4$ in both the flow $Q\propto d^4$ and the torsional constant $J\propto d^4$: [[Power Transmission by Shafts|Power Transmission by Shafts]].
- Resistance, series and parallel: [[Conservation Laws and Flow Networks|Conservation Laws and Flow Networks]].
- Viscosity versus shear modulus: [[Fluids and Solids - Pressure, Stress and Constitutive Laws|Fluids and Solids]].

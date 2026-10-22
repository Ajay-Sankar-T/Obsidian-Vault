---
title: Differential Mass Conservation and Fluid Kinematics – Solved Problems
tags: [fluid-mechanics, tutorial, kinematics, continuity, vorticity, stream-function]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
source: "White, Fluid Mechanics 4th ed., Ch. 4 examples and problems P4.x"
---

# Differential Mass Conservation and Fluid Kinematics – Solved Problems

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · formulas: [[Fluid Mechanics/07 Differential Kinematics and Mass Conservation/Differential Mass Conservation and Fluid Kinematics - Formula Bank|Formula Bank]] · all symbolic results are verified with sympy in `Tools/fm_core.py`

| # | Problem | Concept | Result |
|---|---|---|---|
| 1 | [[#1. P4.1 Acceleration of an unsteady 3-D field]] | material derivative | $\mathbf a=(-4-16t^2,\ 4t+4t^4,\ 0)$ |
| 2 | [[#2. P4.2 / P4.6 Converging nozzle]] | convective acceleration in steady flow | 12.4 g and 37 g |
| 3 | [[#3. P4.9 Constant for incompressible and irrotational flow]] | continuity + curl | $C=6$ for both |
| 4 | [[#4. Ex. 4.2 and 4.3 Using continuity]] | constraints and integration | $a_1+b_2+c_3=0$ |
| 5 | [[#5. P4.13 A flow with a $1/r$ velocity]] | cartesian ⇄ polar, source | line source $K$ |
| 6 | [[#6. P4.22 Density change in a nozzle]] | steady compressible continuity | 1.82 kg/m³ |
| 7 | [[#7. P4.47 and P4.49 Stream functions]] | $\psi$, vorticity, stagnation point | rotational / irrotational |
| 8 | [[#8. P4.54 Flow through a surface from ψ]] | $Q=b\,\Delta\psi$ | $Q=ULb$ |
| 9 | [[#9. P4.56 and Ex. 4.9 Velocity potentials]] | $\phi$, orthogonality | $\phi=Kxy$ |
| 10 | [[#10. P4.59 Deforming fluid element]] | integrate the pathlines | stays rectangular, area 1 |
| 11 | [[#11. Circulation: a numerical loop integral]] | $\Gamma$ vs vorticity | $2\pi K$ or 0 |
| 12 | [[#12. P4.60 Draining vortex]] | irrotational vortex + Bernoulli | $z_C=H-\Omega^2R^2/2g$ |

---

## 1. P4.1 Acceleration of an unsteady 3-D field

**Given.** $\mathbf V=4tx\,\mathbf i+2t^2y\,\mathbf j+4xz\,\mathbf k$. Steady? Dimension? $\mathbf a$ at $(-1,1,0)$.

**Principle.** $\mathbf a=\partial\mathbf V/\partial t+(\mathbf V\!\cdot\!\nabla)\mathbf V$.

**Steps.**
$$a_x=4x+(4tx)(4t)=4x+16t^2x,\qquad a_y=4ty+(2t^2y)(2t^2)=4ty+4t^4y,$$
$$a_z=(4tx)(4z)+(4xz)(4x)=16txz+16x^2z$$

At $(-1,1,0)$: $\ \boxed{\mathbf a=(-4-16t^2)\,\mathbf i+(4t+4t^4)\,\mathbf j}$ (and $a_z=0$). The flow is **unsteady** (explicit $t$) and **three-dimensional** ($u,v,w$ all depend on $x,y,z$, and $w$ is nonzero away from $z=0$). A unit vector normal to $\mathbf a$ is $\mathbf k$ (or $(4+16t^2,\ 4t+4t^4)/\text{norm}$ rotated in the plane).

---

## 2. P4.2 / P4.6 Converging nozzle

**Given.** $u=V_0(1+2x/L)$, $v=w=0$, $V_0=10$ ft/s, $L=0.5$ ft ($=6$ in).

**Steps.** Steady, so only convection:
$$a_x=u\frac{du}{dx}=V_0^2\Big(1+\frac{2x}{L}\Big)\frac2L$$
- $x=0$: $a=\dfrac{2V_0^2}{L}=400$ ft/s² $=\boxed{12.4\,g}$
- $x=L$: $a=\dfrac{6V_0^2}{L}=1200$ ft/s² $=\boxed{37.3\,g}$

**Transit time (P4.6).** $\dfrac{dx}{dt}=V_0(1+2x/L)\Rightarrow t=\dfrac{L}{2V_0}\ln\Big(1+\frac{2x}{L}\Big)$, so for $x=L$: $\ \boxed{t=\dfrac{L}{2V_0}\ln3=0.55\,\dfrac L{V_0}}$ (=0.027 s here).

**Trap.** "Steady" does not mean zero acceleration; the particle accelerates because it moves into a faster region.

---

## 3. P4.9 Constant for incompressible and irrotational flow

**Given.** $\mathbf V=(3y^2-3x^2)\mathbf i+Cxy\,\mathbf j$.

- Incompressible: $\dfrac{\partial u}{\partial x}+\dfrac{\partial v}{\partial y}=-6x+Cx=0\Rightarrow C=6$.
- Irrotational: $\zeta_z=\dfrac{\partial v}{\partial x}-\dfrac{\partial u}{\partial y}=Cy-6y=0\Rightarrow C=6$.

$$\boxed{C=6\ \text{for both}}$$
(Coincidence of the two conditions: $\mathbf V=\nabla\phi$ with $\phi=3xy^2-x^3$, which is harmonic.)

---

## 4. Ex. 4.2 and 4.3 Using continuity

**Ex. 4.2.** $\mathbf V$ linear in $x,y,z$ with constants $a_i,b_i,c_i$: $\nabla\!\cdot\mathbf V=a_1+b_2+c_3=0$. Only the diagonal constants matter; $b_1,c_1,a_2,c_2,a_3,b_3$ are free (they shear and rotate but do not change volume).

**Ex. 4.3.** $u=a(x^2-y^2)$, $w=b$, $v$ unknown: $\partial v/\partial y=-2ax\Rightarrow v=-2axy+f(x,z,t)$.

---

## 5. P4.13 A flow with a $1/r$ velocity

**Given.** $u=\dfrac{Kx}{x^2+y^2},\ v=\dfrac{Ky}{x^2+y^2}$.

**Steps.**
1. $\nabla\!\cdot\mathbf V=0$ for $r\neq0$ (sympy ✓): incompressible continuity satisfied.
2. Polar components: $v_r=u\cos\theta+v\sin\theta=\dfrac Kr,\ \ v_\theta=-u\sin\theta+v\cos\theta=0$.

**Interpretation.** Purely radial with $v_r=K/r$: a **line source** of strength $m=2\pi K$ (sink if $K<0$); singular at the origin, where continuity fails because mass is created.

---

## 6. P4.22 Density change in a nozzle

**Given.** Steady, 1-D compressible flow, $A=A_0[1-x/(2L)]$, $V:76\to167$ m/s from $x=0$ to $L$, $\rho(0)=2.0$ kg/m³.

**Principle.** Steady continuity $\rho AV=\text{const}$.

$$\rho_L=\rho_0\frac{A_0V_0}{A_LV_L}=2.0\times\frac{76}{0.5\times167}=\boxed{1.82\ \text{kg/m}^3}$$
(The density falls 9 % while the speed more than doubles, which is why $Ma>0.3$ flows need the compressible form.)

---

## 7. P4.47 and P4.49 Stream functions

**P4.47.** $\mathbf V=3y\,\mathbf i+2x\,\mathbf j$.
- Continuity: $u_x+v_y=0+0=0$ ✓.
- $u=\psi_y=3y\Rightarrow\psi=\tfrac32y^2+f(x)$; $v=-\psi_x=2x\Rightarrow f=-x^2$:
$$\boxed{\psi=\tfrac32y^2-x^2}\quad(\text{hyperbolas, centre at the origin})$$
- Vorticity $\zeta_z=v_x-u_y=2-3=-1\neq0$: **rotational**, so **no velocity potential** exists.

**P4.49.** $\psi=K(x^2-y^2)$: $u=\psi_y=-2Ky,\ v=-\psi_x=-2Kx$.
- Stagnation point where $u=v=0$: the origin only.
- $\zeta_z=v_x-u_y=-2K+2K=0$: **irrotational** ($\nabla^2\psi=0$).
- Streamlines $y=\pm x$ are the separating lines; this is **stagnation-point (corner) flow** rotated by 45° (compare $\psi=Kxy$).

---

## 8. P4.54 Flow through a surface from $\psi$

**Given.** $\psi=\dfrac{U}{L^2}(3x^2y-y^3)$; surface joining $(2L,0)$ to $(0,L)$ with width $b$.

$$\psi(0,L)=\frac{U}{L^2}(-L^3)=-UL,\quad\psi(2L,0)=0$$
$$\boxed{Q=b\,|\Delta\psi|=ULb}$$
Direction: $\psi_B-\psi_A<0$, so the flow crosses to the **left** of the path $A\to B$, i.e. toward the origin side. The field is the same cubic pattern as Ex. 4.7/4.9 (there $\psi=a(x^2y-y^3/3)$, here $a=3U/L^2$).

---

## 9. P4.56 and Ex. 4.9 Velocity potentials

**P4.56.** $\phi=Kxy$: $u=\phi_x=Ky,\ v=\phi_y=Kx$; $\nabla^2\phi=0$ ✓; stagnation point at the origin.
Stream function: $u=\psi_y=Ky\Rightarrow\psi=\tfrac K2y^2+f(x)$; $v=-\psi_x=Kx\Rightarrow f=-\tfrac K2x^2$:
$$\psi=\tfrac K2(y^2-x^2)$$
Potential lines $xy=c$ (hyperbolas in the quadrants) are **orthogonal** to $\psi$ lines $y^2-x^2=c'$ (rotated by 45°): corner/stagnation flow. 

**Ex. 4.9.** $u=a(x^2-y^2),\ v=-2axy$: $\zeta_z=-2ay+2ay=0$ ✓; $\phi=a\big(\tfrac{x^3}{3}-xy^2\big)$ (verified: $\phi_x=u$, $\phi_y=v$). Streamlines and potential lines have the same shape rotated by 30° (the angle at the origin where both $u,v\to0$).

---

## 10. P4.59 Deforming fluid element

**Given.** $\mathbf V=x\,\mathbf i-y\,\mathbf j$; element with corners $(2,2),(3,2),(3,3),(2,3)$ at $t=0$. Find its shape at $t=0.5$.

**Steps.** $\dot x=x\Rightarrow x=x_0e^t$; $\dot y=-y\Rightarrow y=y_0e^{-t}$. At $t=0.5$: $e^{0.5}=1.6487,\ e^{-0.5}=0.6065$.

| corner | $t=0$ | $t=0.5$ |
|---|---|---|
| 1 | (2, 2) | (3.30, 1.21) |
| 2 | (3, 2) | (4.95, 1.21) |
| 3 | (3, 3) | (4.95, 1.82) |
| 4 | (2, 3) | (3.30, 1.82) |

Rectangle $1.65\times0.61$; **area** $=1.6487\times0.6065=1.000$ (unchanged).

**Interpretation.** Right angles stay right angles ⇒ no angular deformation net and no rotation: **irrotational** ($\zeta_z=0$). Area conserved ⇒ **incompressible** ($\nabla\!\cdot\mathbf V=1-1=0$). Linear deformation $\dot\varepsilon_{xx}=+1,\ \dot\varepsilon_{yy}=-1$ only. See the figure in the [[Fluid Mechanics/07 Differential Kinematics and Mass Conservation/Differential Mass Conservation and Fluid Kinematics - Formula Bank#7. Standard plane flows|Formula Bank]].

---

## 11. Circulation: a numerical loop integral

**Check done in `fm_core.check()`.** Numerically integrate $\oint\mathbf V\!\cdot d\mathbf l$ around squares (side 2):

| Flow | Loop | $\Gamma$ (numeric) | Expected |
|---|---|---|---|
| free vortex $v_\theta=K/r,\ K=1.7$ | centred on the axis | $10.68$ | $2\pi K=10.68$ |
| free vortex | square centred at $(3,0)$ (axis outside) | $0.00$ | $0$ (irrotational region) |
| solid body $\Omega=0.9$ | any square, area 4 | $7.20$ | $\zeta A=2\Omega A=7.20$ |

So circulation can be nonzero in an irrotational flow only if the loop encloses a singularity carrying vorticity.

---

## 12. P4.60 Draining vortex

**Given.** $v_r=v_z=0,\ v_\theta=\Omega R^2/r$ (the problem's constant; symbol lost in the PDF text layer – I take it as $\Omega$ with units 1/s), water depth $z=H$ far from the hole, free surface at atmospheric pressure.

**Rotational?** $\zeta_z=\dfrac1r\dfrac{d(rv_\theta)}{dr}=\dfrac1r\dfrac{d(\Omega R^2)}{dr}=0$ ⇒ **irrotational** (free vortex).

**Depth at $r=R$.** Irrotational ⇒ one Bernoulli constant for the whole flow. At the free surface $p=p_a$: $\dfrac12V^2+gz=\text{const}=gH$ (far away $V\to0$). At $r=R$: $V=\Omega R$:
$$\boxed{z_C=H-\frac{\Omega^2R^2}{2g}}$$
Near the axis $z_s=H-\Omega^2R^4/(2gr^2)\to-\infty$: the surface plunges and the model fails at small $r$ (a real vortex has a viscous core).

## Related
- [[Fluid Mechanics/07 Differential Kinematics and Mass Conservation/Differential Mass Conservation and Fluid Kinematics - Formula Bank|Formula Bank]], [[Fluid Mechanics/08 Incompressible Inviscid Flow/Incompressible Inviscid Flow and Bernoulli - Formula Bank|Bernoulli Formula Bank]]

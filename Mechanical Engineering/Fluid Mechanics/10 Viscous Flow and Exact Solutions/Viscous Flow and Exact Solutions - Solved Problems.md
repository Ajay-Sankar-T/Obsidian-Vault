---
title: Viscous Flow and Exact Solutions – Solved Problems (GPS 9 & 10)
tags: [fluid-mechanics, tutorial, navier-stokes, laminar-flow, pipe-flow, siphon, pump]
up: "[[Fluid Mechanics - MOC]]"
source: "[[GPS_9_10.pdf]]"
---

# Viscous Flow and Exact Solutions – Solved Problems (GPS 9 & 10)

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · formulas: [[Viscous Flow and Exact Solutions - Formula Bank]], [[Pipe Flow and Losses - Formula Bank]] · source: [[GPS_9_10.pdf]] · all numbers recomputed in `Tools/fm_gps9_10.py`

Data from the sheet: $g=9.81$ m/s²; water at 20 °C $\rho=998$ kg/m³, $\nu=1.01\times10^{-6}$ m²/s, $p_v=2.34$ kPa, $p_{atm}=101.3$ kPa; commercial steel $\varepsilon=0.046$ mm. Friction factors from Colebrook.

| # | Problem | Concept | Result |
|---|---|---|---|
| 1 | [[#1. Parallel-plate flow chamber]] | plane Poiseuille | 9.38 mL/min; $\Delta p=384$ Pa; $\tau_w$ 1.03–1.42 Pa |
| 2 | [[#2. Lava flow down a slope]] | film flow, free surface | $\mu=3.08\times10^3$ Pa·s; $q=2.0$ m²/s; $h'=4.31$ m |
| 3 | [[#3. Stagnation-point flow near a wall]] | stress tensor, exact solution? | $\tau_w=0.243$ Pa; no pressure exists; $\ell<15.9$ mm |
| 4 | [[#4. Wire coating]] | annular Couette flow | $F=0.689$ N; $t=49.2\ \mu$m, independent of $U,\mu$ |
| 5 | [[#5. Dashpot]] | Couette + Poiseuille | $c=2.55\times10^4$ N·s/m; $\times0.58$ after wear |
| 6 | [[#6. Syringe and needle]] | Hagen–Poiseuille | 19.7 s; choose 25 G; cold drug 16.8 s |
| 7 | [[#7. Siphon over an embankment]] | energy equation, cavitation | 6.14 L/s; 23.2 kPa; limit 11.5 m, 7.83 L/s |
| 8 | [[#8. Pumping to an elevated tank]] | system head, parallel pipes | 19.1 m → 13.9 m (parallel), 14.0 m (65 mm) |

> [!abstract] Pattern
> Problems 1–6 are one idea: **reduce Navier–Stokes to a single ODE, apply two boundary conditions, integrate** ([[Viscous Flow and Exact Solutions - Formula Bank#1. The recipe for a unidirectional flow|recipe]]). Problems 7–8 are the pipe energy equation of GPS 7 & 8. Before computing, check the Reynolds number: every flow here is laminar except 7 and 8.

---

## 1. Parallel-plate flow chamber

**Tests:** [[Viscous Flow and Exact Solutions - Formula Bank#2. The solutions to know|plane Poiseuille flow]], wall shear stress.

**Given.** $h=0.25$ mm, $w=10$ mm, $L=40$ mm, $\rho=1000$, $\mu=0.80\times10^{-3}$ Pa·s, $\tau_w=1.2$ Pa. Cells on the floor $y=0$.

**(a) Profile.** $w\gg h$, so $\partial/\partial z=0$, $w=0$. Continuity with $\partial u/\partial x=0$ (fully developed) gives $v=0$. Cross-stream momentum: $\partial p/\partial y=0$, so $p=p(x)$. Streamwise: $0=-\dfrac{dp}{dx}+\mu\dfrac{d^2u}{dy^2}$. Boundary conditions $u(0)=u(h)=0$:

$$
u(y)=\frac{1}{2\mu}\frac{dp}{dx}\,(y^2-hy)=\frac{-dp/dx}{2\mu}\,y(h-y)
$$

$$
Q=w\int_0^h u\,dy=\frac{w(-dp/dx)}{2\mu}\Big(\frac{h^3}{2}-\frac{h^3}{3}\Big)=\boxed{-\frac{dp}{dx}\frac{wh^3}{12\mu}}
$$

$$
\tau_w=\mu\frac{du}{dy}\Big|_{0}=\frac h2\Big(-\frac{dp}{dx}\Big)=\frac{h}{2}\cdot\frac{12\mu Q}{wh^3}=\boxed{\frac{6\mu Q}{wh^2}}
$$

**(b) Numbers.**

$$
Q=\frac{\tau_w wh^2}{6\mu}=\frac{(1.2)(0.010)(0.25\times10^{-3})^2}{6(0.80\times10^{-3})}=1.5625\times10^{-7}\ \text{m}^3/\text{s}=\boxed{9.38\ \text{mL/min}}
$$

$$
\bar V=\frac{Q}{wh}=\boxed{62.5\ \text{mm/s}},\quad u_{\max}=\tfrac32\bar V=\boxed{93.8\ \text{mm/s}},\quad
-\frac{dp}{dx}=\frac{2\tau_w}{h}=9600\ \text{Pa/m},\quad \Delta p=9600(0.040)=\boxed{384\ \text{Pa}}
$$

$Re=\rho\bar Vh/\mu=(1000)(0.0625)(0.25\times10^{-3})/(0.80\times10^{-3})=19.5<1400$: **laminar**.

**(c) Gasket tolerance.** At fixed $Q$, $\tau_w=6\mu Q/(wh^2)\propto h^{-2}$:

| $h$ (mm) | 0.23 | 0.25 | 0.27 |
|---|---|---|---|
| $\tau_w$ (Pa) | **1.42** | 1.20 | **1.03** |

So $\tau_w$ lies between **1.03 and 1.42 Pa**, i.e. $-14\%$ to $+18\%$ for a $\pm8\%$ gap error. The sign is asymmetric because of the inverse square.

![[FM-V1-chamber.png]]

> [!question]- Predict first: which is the bigger risk, a gasket that is too thick or too thin?
> Too thin. $\tau_w\propto h^{-2}$ so a $-8\%$ gap raises the stress by $18\%$, more than the $14\%$ drop from a $+8\%$ gap.

**Trap.** Forgetting that $Q=\tau_w wh^2/6\mu$ is for *total* $w$; per unit width the formula has no $w$. Also: $Re$ for plates uses the gap $h$, not the hydraulic diameter, with the limit 1400.

---

## 2. Lava flow down a slope

**Tests:** [[Viscous Flow and Exact Solutions - Formula Bank#2. The solutions to know|film flow down an incline]], free-surface boundary condition.

**Given.** $h=2.0$ m, $\theta=5^\circ$, $u_s=1.5$ m/s, $\rho=2700$ kg/m³, very wide, steady, laminar, fully developed; no shear from the air.

**(a) Setup.** $x$ down the slope, $y$ normal to the bed; gravity components $g_x=g\sin\theta$, $g_y=-g\cos\theta$. Wide and fully developed: $v=0$, $u=u(y)$, no $z$ dependence.

*Pressure.* $y$-momentum: $0=-\rho g\cos\theta-\partial p/\partial y$, so $p=p_{atm}+\rho g\cos\theta\,(h-y)$ (atmospheric at the surface). It is **hydrostatic** across the depth and has no $x$ dependence: $dp/dx=0$.

*Boundary conditions.* Bed: $u(0)=0$ (no slip). Free surface: $\mu\,du/dy=0$ at $y=h$ (air exerts no shear).

*Streamwise momentum:* $0=\rho g\sin\theta+\mu\,u''$. Integrating:

$$
u=\frac{\rho g\sin\theta}{2\mu}\,(2hy-y^2),\qquad u_s=u(h)=\frac{\rho g\sin\theta\,h^2}{2\mu}
$$

$$
\bar V=\frac1h\int_0^hu\,dy=\frac{\rho g\sin\theta}{2\mu h}\Big(h^3-\frac{h^3}{3}\Big)=\frac{\rho g\sin\theta\,h^2}{3\mu}=\boxed{\tfrac23u_s}
$$

**(b) Viscosity and flow rate.**

$$
\mu=\frac{\rho g\sin\theta\,h^2}{2u_s}=\frac{(2700)(9.81)(0.08716)(2.0)^2}{2(1.5)}=\boxed{3.08\times10^{3}\ \text{Pa·s}}
$$

$$
\bar V=\tfrac23(1.5)=1.0\ \text{m/s},\qquad q=\bar Vh=\boxed{2.0\ \text{m}^2/\text{s}}
$$

$Re=\rho\bar Vh/\mu=(2700)(1.0)(2.0)/3078=1.75$: **laminar** by a wide margin (creeping flow; $\mu$ is about $3\times10^6$ times water).

**(c) Bed shear stress.** From the profile:

$$
\tau_{\text{bed}}=\mu\frac{du}{dy}\Big|_0=\mu\cdot\frac{\rho g\sin\theta}{\mu}\,h=\rho gh\sin\theta
$$

From a force balance on a slab of length $\Delta x$ and unit width: weight component along the slope $\rho g h\,\Delta x\sin\theta$; pressure forces on the two ends are equal (hydrostatic, same depth), nothing acts on the free surface. Steady, so the bed shear force equals the weight component: $\tau_{\text{bed}}\Delta x=\rho gh\Delta x\sin\theta$ ✓.

$$
\tau_{\text{bed}}=(2700)(9.81)(2.0)\sin5^\circ=\boxed{4.62\ \text{kPa}}
$$

**(d) Cooled lava.** $\mu'=10\mu$, same $q$. Since $q=\dfrac{\rho g\sin\theta\,h^3}{3\mu}$, $h^3\propto\mu q$ and

$$
h'=h\,10^{1/3}=\boxed{4.31\ \text{m}},\qquad u_s'=\frac{3q}{2h'}=\boxed{0.696\ \text{m/s}}
$$

Check: $u_s'=\rho g\sin\theta h'^2/(2\mu')=0.696$ ✓. The flow is more than twice as deep and less than half as fast; the bed shear rises to $\rho gh'\sin\theta=9.95$ kPa. $Re'=0.18$.

![[FM-V2-lava.png]]

**Trap.** Using $g$ instead of $g\sin\theta$ in the driving term, or putting the zero-shear condition at the bed. The free surface is the zero-shear boundary; the bed is no-slip.

---

## 3. Stagnation-point flow near a wall

**Tests:** [[Viscous Flow and Exact Solutions - Formula Bank#4. Stresses and creeping flow|Newtonian stress, exact-solution test, creeping flow]], [[Differential Mass Conservation and Fluid Kinematics - Formula Bank|continuity and vorticity]].

**Given.** $u=Bxy$, $v=-\tfrac12By^2$, $B=25$ m⁻¹s⁻¹, silicone oil $\rho=970$, $\nu=1.0\times10^{-3}$ m²/s so $\mu=\rho\nu=0.97$ Pa·s. Wall at $y=0$.

**(a) Kinematics.** $\dfrac{\partial u}{\partial x}+\dfrac{\partial v}{\partial y}=By-By=0$ ✓. On the wall $y=0$: $u=0$ (no-slip) and $v=0$ (no-penetration) ✓. Vorticity $\omega_z=\dfrac{\partial v}{\partial x}-\dfrac{\partial u}{\partial y}=-Bx$: **rotational** everywhere except on $x=0$. Streamlines: $\psi=\tfrac12Bxy^2$, so $xy^2=$ const.

**(b) Stresses.**

$$
\sigma_{xx}=-p+2\mu By,\qquad \sigma_{yy}=-p-2\mu By,\qquad \tau_{xy}=\mu(Bx+0)=\mu Bx
$$

At $P=(10\ \text{mm},4\ \text{mm})$: viscous parts $2\mu By=2(0.97)(25)(0.004)=\boxed{0.194\ \text{Pa}}$ in $\sigma_{xx}$, $-0.194$ Pa in $\sigma_{yy}$, and $\tau_{xy}=(0.97)(25)(0.010)=\boxed{0.2425\ \text{Pa}}$.

Wall shear stress at $x=10$ mm: $\tau_{xy}$ does not depend on $y$, so $\tau_w=\mu Bx=\boxed{0.243\ \text{Pa}}$, directed along $+x$ (the oil above moves in $+x$ and drags the wall that way). At $y=0$ the viscous normal stress $2\mu By=0$: the wall feels only the pressure and the shear.

**(c) Navier–Stokes (steady, no gravity).**

$x$: $\rho(u u_x+v u_y)=\rho\big(B^2xy^2-\tfrac12B^2xy^2\big)=\tfrac12\rho B^2xy^2$, and $\nabla^2u=0$, so
$$\frac{\partial p}{\partial x}=-\tfrac12\rho B^2xy^2$$
$y$: $\rho(uv_x+vv_y)=\tfrac12\rho B^2y^3$ and $\nabla^2v=-B$, so
$$\frac{\partial p}{\partial y}=-\mu B-\tfrac12\rho B^2y^3$$
A pressure exists only if $\partial^2p/\partial y\partial x=\partial^2p/\partial x\partial y$. Here $\partial_y(\partial_xp)=-\rho B^2xy$ but $\partial_x(\partial_yp)=0$. They agree only where $xy=0$: **no $p(x,y)$ satisfies both components**. The field is **not an exact solution**: it is the leading term of the expansion of the true flow near the stagnation point and the inertia terms need corrections of higher order in $x,y$.

**(d) Scaling.** With $x,y\sim\ell$, $u\sim B\ell^2$, $\Delta p\sim\mu B\ell$: inertia $\rho u\,\partial u/\partial x\sim\rho B^2\ell^3$, viscous $\mu\nabla^2u\sim\mu B$, so

$$
\frac{\text{inertia}}{\text{viscous}}=\frac{\rho B^2\ell^3}{\mu B}=\frac{B\ell^3}{\nu}=Re
$$

Dropping inertia: $\partial p/\partial x=\mu\nabla^2u=0$ and $\partial p/\partial y=\mu\nabla^2v=-\mu B$, which are compatible: $p=p_0-\mu By$. Both components are then satisfied exactly. $Re<0.1$ needs

$$
\ell<\Big(\frac{0.1\nu}{B}\Big)^{1/3}=\Big(\frac{0.1(10^{-3})}{25}\Big)^{1/3}=\boxed{15.9\ \text{mm}}
$$

At $P$, $\ell=10.8$ mm and $Re=0.031$: well inside the creeping zone. The pressure variation across the zone is only of order $\mu B\ell=0.24$ Pa.

![[FM-V3-stagnation.png]]

> [!question]- What does "satisfies continuity and the wall conditions" prove?
> Only that the field is *kinematically admissible*. Momentum is a separate requirement; here it fails at $O(Re)$, which is why the field becomes exact only as $Re\to0$.

**Trap.** Writing the viscous part of $\sigma_{yy}$ at the wall as nonzero: $\partial v/\partial y=-By\to0$ there. Also the sign of $\sigma_{yy}$'s viscous part is negative.

---

## 4. Wire coating

**Tests:** [[Viscous Flow and Exact Solutions - Formula Bank#2. The solutions to know|annular Couette flow]], thin-gap approximation.

**Given.** $a=0.50$ mm, $R=0.60$ mm, $L=20$ mm, $U=2.0$ m/s, $\rho=1100$, $\mu=0.50$ Pa·s; $dp/dx=0$.

**(a) Profile.** The data-sheet equation with $dp/dx=0$: $\dfrac1r\dfrac{d}{dr}\Big(r\dfrac{du}{dr}\Big)=0$, so $r\,u'=C_1$ and $u=C_1\ln r+C_2$. Conditions: $u(a)=U$ (the liquid sticks to the wire), $u(R)=0$ (die wall):

$$
u(r)=U\frac{\ln(R/r)}{\ln(R/a)}
$$

**(b) Shear and force.** $\ln(R/a)=\ln1.2=0.18232$.

$$
\tau=\mu\Big|\frac{du}{dr}\Big|_{r=a}=\frac{\mu U}{a\ln(R/a)}=\frac{(0.5)(2.0)}{(0.5\times10^{-3})(0.18232)}=\boxed{10.97\ \text{kPa}}
$$

$$
F=\tau\,(2\pi aL)=\frac{2\pi\mu UL}{\ln(R/a)}=\frac{2\pi(0.5)(2.0)(0.020)}{0.18232}=\boxed{0.689\ \text{N}}
$$

The liquid drags back on the wire, so the pull must supply this force (no pressure force acts along the wire).

**(c) Flow rate and coating thickness.**

$$
Q=\int_a^R u\,2\pi r\,dr=\frac{2\pi U}{\ln(R/a)}\Big[\frac{R^2-a^2}{4}-\frac{a^2}{2}\ln\frac Ra\Big]=\pi U\Big[\frac{R^2-a^2}{2\ln(R/a)}-a^2\Big]
$$
$$
=\pi(2.0)\big[3.017\times10^{-7}-2.5\times10^{-7}\big]=\boxed{3.25\times10^{-7}\ \text{m}^3/\text{s}\ (0.325\ \text{mL/s})}
$$

The coating then travels at $U$: $Q=U\pi\big[(a+t)^2-a^2\big]$. Equating:

$$
(a+t)^2=a^2+\frac{Q}{\pi U}=\frac{R^2-a^2}{2\ln(R/a)}\ \Longrightarrow\ \boxed{t=\sqrt{\frac{R^2-a^2}{2\ln(R/a)}}-a=49.2\ \mu\text{m}}
$$

$U$ and $\mu$ cancelled: the coating is set by the die geometry alone. $Q\propto U$ for a given geometry, and the layer is carried off at the same $U$, so $U$ drops out. $\mu$ never enters because there is no pressure gradient: the profile is fixed by the two wall velocities.

**(d) Thin gap.** With $h=R-a$ and $y=r-a$, $\ln(R/r)\approx(h-y)/a$ and $\ln(R/a)\approx h/a$ for $h\ll a$, so $u\approx U(1-y/h)$: **plane Couette flow**.

| | exact | Couette ($h=0.10$ mm) | difference |
|---|---|---|---|
| shear on wire | 10.97 kPa | $\mu U/h=10.00$ kPa | −8.8 % |
| force | 0.689 N | $\mu U/h\cdot2\pi aL=0.628$ N | −8.8 % |
| flow rate | $3.25\times10^{-7}$ | $\pi aUh=3.14\times10^{-7}$ | −3.2 % |
| thickness | 49.2 μm | $h/2=50.0$ μm | +1.5 % |

$h/a=0.2$ is not very small, and curvature raises the shear on the *inner* wall, hence the 9 % error in force; the thickness estimate is much better. Laminar: gap Reynolds number with mean speed $U/2$: $Re=\rho(U/2)h/\mu=0.22\ll1400$.

![[FM-V4-wire.png]]

**Trap.** Applying the pipe parabola. With no pressure gradient the driver is the moving wire: the profile is logarithmic (annulus) or linear (thin gap), not parabolic.

---

## 5. Dashpot

**Tests:** [[Viscous Flow and Exact Solutions - Formula Bank#2. The solutions to know|Couette + Poiseuille flow]], continuity, damping coefficient.

**Given.** $D=40$ mm, $L=30$ mm, $h=0.30$ mm, $\rho=880$, $\mu=0.15$ Pa·s, $F=250$ N.

**(a) Why plates.** $h/D=0.0075\ll1$: the gap is so thin that the curvature of the wall is invisible across it, so the annulus unrolls into a channel of width $\pi D$ and height $h$. $x$ up the gap, $y$ from the cylinder wall. Boundary conditions: $u(0)=0$ (cylinder), $u(h)=-U$ (the piston face moves **down** at $U$). Pressure below the piston exceeds that above by $\Delta p$, so $dp/dx=-\Delta p/L$. The plate equation $0=-dp/dx+\mu u''$ gives

$$
u(y)=\frac{\Delta p}{2\mu L}\,y(h-y)-U\frac{y}{h}
$$

**(b) Flow rate and $U$.**

$$
Q_{\text{gap}}=\pi D\int_0^hu\,dy=\pi D\Big[\frac{\Delta p\,h^3}{12\mu L}-\frac{Uh}{2}\Big]
$$

Continuity: the piston displaces volume per second $\dfrac{\pi D^2}{4}U$, which flows up through the gap: $\dfrac{\pi D^2}{4}U=Q_{\text{gap}}$. Dividing by $\pi D$:

$$
\frac{DU}{4}+\frac{Uh}{2}=\frac{\Delta p\,h^3}{12\mu L}\ \Longrightarrow\ \boxed{U=\frac{\Delta p\,h^3}{3\mu L\,(D+2h)}}
$$

**(c) Numbers.**

$$
\Delta p=\frac{F}{\pi D^2/4}=\frac{250}{1.2566\times10^{-3}}=\boxed{199\ \text{kPa}}
$$

$$
U=\frac{(1.989\times10^5)(0.30\times10^{-3})^3}{3(0.15)(0.030)(0.0406)}=\boxed{9.80\ \text{mm/s}},\qquad c=\frac FU=\boxed{2.55\times10^{4}\ \text{N·s/m}}
$$

Check: $Q_{\text{gap}}=\pi D[\dots]=1.2315\times10^{-5}$ m³/s $=A\,U$ ✓.

**(d) Laminar and inertia.** Mean gap velocity $\bar V=\dfrac{(\pi D^2/4)U}{\pi Dh}=\dfrac{DU}{4h}=0.327$ m/s. $Re=\rho\bar Vh/\mu=0.575<1400$: laminar. Inertia relative to viscous terms is $\rho\bar V^2/L$ over $\mu\bar V/h^2$, i.e. $Re\,h/L=0.575(0.01)=0.006\ll1$: **negligible**.

**(e) Wear.** $c=F/U\propto(D+2h)/h^3$:

$$
\frac{c'}{c}=\frac{D+2(1.2h)}{D+2h}\,\frac{1}{1.2^3}=\frac{40.72}{40.60}\times0.5787=\boxed{0.58}
$$

A 20 % wider gap cuts the damping by **42 %**: the $h^{-3}$ dominates, the $(D+2h)$ factor barely matters.

![[FM-V5-dashpot.png]]

> [!question]- Does the oil near the piston flow up or down?
> Almost all of it flows **up** (peak $\approx0.49$ m/s at mid-gap, driven by $\Delta p$). Only a very thin layer next to the piston face moves down with it at $9.8$ mm/s: $u(h)=-U$. The pressure term is $\sim50$ times bigger than the wall-motion term.

**Trap.** Taking the flow rate as $\pi D h\,\bar V_{\text{Poiseuille}}$ only and forgetting the $-Uh/2$ term, or equating to $\pi D^2U/4$ with the wrong sign (the oil goes up while the piston goes down).

---

## 6. Syringe and needle

**Tests:** [[Viscous Flow and Exact Solutions - Formula Bank#2. The solutions to know|Hagen–Poiseuille flow]], $Q\propto d^4$.

**Given.** $\rho=1000$, $\mu=0.015$ Pa·s, barrel 8.66 mm, needle $L=16$ mm, thumb force $F=15$ N. No plunger friction or barrel losses, so the whole barrel pressure acts across the needle.

$$
p=\frac{F}{\pi D_b^2/4}=\frac{15}{5.890\times10^{-5}}=254.7\ \text{kPa}\qquad(\Delta p=p)
$$

**(a) 27 G, $d=0.21$ mm.** Hagen–Poiseuille (pipe equation integrated, $Q=\pi d^4\Delta p/128\mu L$):

$$
Q=\frac{\pi(0.21\times10^{-3})^4(254\,663)}{128(0.015)(0.016)}=5.06\times10^{-8}\ \text{m}^3/\text{s}=\boxed{0.0506\ \text{mL/s}}
$$

| quantity | value |
|---|---|
| time for 1.0 mL | **19.7 s** |
| mean velocity $V=Q/A$ | **1.46 m/s** |
| maximum velocity $2V$ | **2.92 m/s** |
| wall shear $\tau_w=\dfrac{d\,\Delta p}{4L}=\dfrac{8\mu V}{d}$ | **836 Pa** |

**(b) Checks.** $Re=\rho Vd/\mu=20.5<2300$: **laminar**. The jet kinetic energy $\tfrac12\rho V^2=1.07$ kPa (or $\alpha\rho V^2/2=2.14$ kPa with $\alpha=2$) is **0.4–0.8 %** of the 255 kPa pressure drop, so ignoring it was fine. The developing length $\approx0.06\,Re\,d=0.26$ mm is a tiny fraction of the 16 mm needle.

**(c) Needle choice.** $Q\propto d^4$:

| $d$ (mm) | gauge | $Q$ (mL/s) | time for 1 mL (s) | $Re$ |
|---|---|---|---|---|
| 0.16 | 30 | 0.0171 | 58.6 | 9.1 |
| 0.21 | 27 | 0.0506 | 19.7 | 20.5 |
| **0.26** | **25** | **0.119** | **8.40** | 38.9 |
| 0.34 | 23 | 0.348 | 2.87 | 86.9 |

Under 10 s needs $d>0.249$ mm. The thinnest available that makes it: **0.26 mm (25 G)**, 8.4 s.

**(d) Cold drug.** $\mu\to2\mu$, $Q$ halves, time doubles: **16.8 s** with the 25 G. The threshold diameter rises by $2^{1/4}=1.19$ to 0.296 mm; only the 0.34 mm (23 G) then meets 10 s (5.7 s). So at fridge temperature the user must either warm the drug, push harder, or accept a thicker needle.

![[FM-V6-syringe.png]]

**Trap.** Using $d^2$ instead of $d^4$ when comparing needles: a 24 % larger bore ($0.21\to0.26$) multiplies the flow by $2.35$, not $1.53$.

---

## 7. Siphon over an embankment

**Tests:** [[Pipe Flow and Losses - Formula Bank|energy equation with losses]], absolute pressure and cavitation.

**Given.** $D=50$ mm commercial steel ($\varepsilon/D=9.2\times10^{-4}$), re-entrant inlet ($K=0.8$), two elbows ($0.9$ each), crest 4.5 m above the surface, inlet-to-crest length 8.0 m, total 20 m, outlet 6.0 m below the surface, free jet. Water at 20 °C.

**(a) Flow rate.** Reservoir surface to the free jet. The exit loss $K=1$ and the jet's $V^2/2g$ are the same energy, **counted once**:

$$
6.0=\frac{V^2}{2g}\Big(1+0.8+2(0.9)+f\frac{20}{0.05}\Big)=\frac{V^2}{2g}\big(3.6+400f\big)
$$

Iterating with Colebrook: $f=0.0211$ at $Re=1.55\times10^5$, giving $V^2/2g=0.499$ m and

$$
V=3.13\ \text{m/s},\qquad Q=VA=\boxed{6.14\ \text{L/s}}
$$

**(b) Pressure at the end of the crest.** Energy from the surface to the crest end (after both elbows, 8.0 m of pipe), with $V^2/2g=0.499$ m:

$$
\frac{p_{atm}-p}{\rho g}=z_c+\frac{V^2}{2g}+\Big(0.8+2(0.9)+f\frac{8.0}{0.05}\Big)\frac{V^2}{2g}=4.5+0.499+2.978=7.98\ \text{m}
$$

$p=101.3-\rho g(7.98)/1000=\boxed{23.2\ \text{kPa absolute}}$, about ten times the vapour pressure 2.34 kPa. **No cavitation** at present.

**(c) Where the 7.98 m comes from.**

| part | head (m) | share |
|---|---|---|
| height of the crest | 4.50 | **56 %** |
| velocity head | 0.50 | 6 % |
| losses inlet → crest | 2.98 | **37 %** |

The crest height is set by the embankment. The part a designer can attack is the **loss** (37 %): a larger-diameter pipe on the up-leg (losses scale with $V^2$), fewer or gentler bends, a smooth entrance. A well-rounded inlet ($K=0.8\to0.04$) helps little: the total falls only from 7.98 to 7.81 m, because friction in the 8 m run and the elbows dominate. Lowering the crest is the one change that directly removes the largest term.

**(d) Deepest outlet.** Cavitation starts when the crest-end pressure reaches $p_v$:

$$
\frac{p_{atm}-p_v}{\rho g}=10.11\ \text{m}=4.5+\frac{V^2}{2g}\big(3.6+160f\big)\ \ \Rightarrow\ \ \frac{V^2}{2g}\big(3.6+160f\big)=5.61\ \text{m}
$$

(velocity head $1$, inlet $0.8$, two elbows $1.8$, friction in the 8 m run $160f$). With the outlet at depth $H$ the total pipe length is $20+(H-6)$ and the energy equation to the jet gives $H=\dfrac{V^2}{2g}\big(3.6+f\,\tfrac{14+H}{0.05}\big)$. Solving the two together:

$$
\boxed{H=11.5\ \text{m}},\qquad V=3.99\ \text{m/s},\qquad Q=\boxed{7.83\ \text{L/s}}\ (+27\%)
$$

with $f=0.0207$, total pipe length 25.5 m. Beyond that depth the crest-end pressure would fall below the vapour pressure and the water column would break. A deeper outlet drives a faster flow, and a faster flow raises both the velocity head and the friction loss ahead of the crest, so the crest pressure keeps falling until it reaches $p_v$. The cavitation limit, not the drive, caps the flow.

**(e) Grade lines.** The energy line starts at the reservoir surface, drops $0.8\,V^2/2g$ at the inlet, falls linearly with friction ($f V^2/2gD=0.21$ m per metre), and steps down $0.9\,V^2/2g=0.45$ m at each elbow. It ends at the exit at $z_{out}+V^2/2g=-6+0.50=-5.50$ m (the free jet keeps its velocity head). Constant diameter means the hydraulic grade line is parallel, **$V^2/2g=0.50$ m below**. At the crest end it is at $-3.48$ m, i.e. 7.98 m below the pipe: that is the suction, and the boiling line (HGL level at which $p=p_v$) is at $-5.61$ m.

![[FM-V7a-siphon-grade-lines.png]]

![[FM-V7b-siphon-depth.png]]

**Trap.** Counting both $K_{exit}=1$ and the jet kinetic energy (the sheet warns about this), or leaving out the second elbow when finding the crest-end pressure (the pressure is taken just downstream of it). Absolute, not gauge, pressure is what is compared with $p_v$.

---

## 8. Pumping to an elevated tank

**Tests:** [[Pipe Flow and Losses - Formula Bank|system head]], scaling of losses with $Q$ and $D$.

**Given.** $\Delta z=12$ m, $L=60$ m, $D=50$ mm commercial steel, $Q=4.0$ L/s. $\sum K=0.5\ (\text{entrance})+2.0\ (\text{check})+4(0.9)+0.2\ (\text{gate})+1.0\ (\text{exit})=7.3$. Free surfaces at rest and at atmosphere, so $h_p=\Delta z+h_{lT}$.

**(a) Baseline.** $V=Q/A=2.04$ m/s, $V^2/2g=0.2115$ m, $Re=1.01\times10^5$, $f=0.0219$:

$$
h_p=12+\Big(0.0219\frac{60}{0.05}+7.3\Big)(0.2115)=12+5.55+1.54=\boxed{19.1\ \text{m}}
$$

**(b) Two identical pipes in parallel**, each with the same fittings, $Q/2$ in each: $V=1.02$ m/s, $Re=5.0\times10^4$, $f=0.0238$, $V^2/2g=0.0529$ m:

$$
h_p=12+(0.0238(1200)+7.3)(0.0529)=12+1.51+0.39=\boxed{13.9\ \text{m}}
$$

**(c) One 65 mm pipe**, same fittings: $V=1.21$ m/s, $Re=7.8\times10^4$, $\varepsilon/D=7.1\times10^{-4}$, $f=0.0218$, $L/D=923$, $V^2/2g=0.0741$ m:

$$
h_p=12+(0.0218(923)+7.3)(0.0741)=12+1.49+0.54=\boxed{14.0\ \text{m}}
$$

| | friction | minor | static | $h_p$ | saving |
|---|---|---|---|---|---|
| one 50 mm | 5.55 | 1.54 | 12 | **19.1** | |
| two 50 mm in parallel | 1.51 | 0.39 | 12 | **13.9** | 27 % |
| one 65 mm | 1.49 | 0.54 | 12 | **14.0** | 27 % |

**Why they match.** At fixed $Q$: friction head $\propto fLQ^2/D^5$, minor head $\propto KQ^2/D^4$.
- **Parallel:** each pipe carries $Q/2$ at the same $D$, so both losses fall by $\left(\tfrac12\right)^2=0.25$ (friction slightly less because $f$ rises at the lower $Re$).
- **65 mm:** friction falls by $(50/65)^5=0.27$ and minor losses by $(50/65)^4=0.35$.

Both cut the losses to roughly a quarter to a third, from 7.1 m to about 1.9–2.0 m. **Neither can cut $h_p$ by more than about a quarter** because 12 m of the 19.1 m is the static lift, which no pipe changes: even zero losses would give 12 m, a 37 % saving at best. Cutting the losses by about 72 % gives the 27 %.

![[FM-V8-pump-head.png]]

> [!question]- Predict first: would a 100 mm pipe do much better than the 65 mm?
> No. Losses would drop to about 0.3 m, so $h_p\approx12.3$ m, a further 1.7 m. Beyond 65 mm each extra millimetre buys almost nothing: the pump is lifting water, not fighting the pipe.

**Trap.** Halving $Q$ but keeping $K$ for only one set of fittings in the parallel case. The problem says *the same fittings* in each pipe: each branch has its own entrance, check valve, elbows, gate valve and exit, so $\sum K=7.3$ applies to each branch.

---

## Summary of answers

> [!success] Final answers
> 1. $Q=9.38$ mL/min, $\bar V=62.5$ mm/s, $u_{\max}=93.8$ mm/s, $\Delta p=384$ Pa, laminar ($Re=19.5$); $\tau_w=1.03$–$1.42$ Pa.
> 2. $\mu=3.08\times10^3$ Pa·s, $q=2.0$ m²/s, $Re=1.75$, $\tau_{\text{bed}}=4.62$ kPa; cooled: $h=4.31$ m, $u_s=0.696$ m/s.
> 3. $\tau_w=0.243$ Pa; no pressure field exists; $Re<0.1$ for $\ell<15.9$ mm; $p=p_0-\mu By$ in creeping flow.
> 4. $\tau=10.97$ kPa, $F=0.689$ N, $Q=0.325$ mL/s, $t=49.2\ \mu$m (independent of $U,\mu$); Couette gives 0.628 N and 50 μm.
> 5. $\Delta p=199$ kPa, $U=9.80$ mm/s, $c=2.55\times10^4$ N·s/m; wear: $c\times0.58$.
> 6. 27 G: 0.0506 mL/s, 19.7 s, 1.46 and 2.92 m/s, 836 Pa; use **25 G** (8.4 s); cold: 16.8 s.
> 7. $Q=6.14$ L/s, 23.2 kPa abs; 56 % / 6 % / 37 %; limit $H=11.5$ m, $Q=7.83$ L/s.
> 8. $h_p=19.1$ m; parallel 13.9 m; 65 mm pipe 14.0 m.

### Quick revision
- [ ] Unidirectional flow: continuity → hydrostatic cross-stream → one ODE → two boundary conditions.
- [ ] Plates $h^3$, pipe $d^4$, wall shear $\tau_w=6\mu Q/(wh^2)$ or $8\mu V/d$.
- [ ] Free surface: zero shear; bed shear $=\rho gh\sin\theta$.
- [ ] Exact-solution test: a pressure must exist (mixed derivatives equal).
- [ ] Count the exit loss and the jet kinetic energy once.
- [ ] A fixed static lift limits how much any pipe change can save.

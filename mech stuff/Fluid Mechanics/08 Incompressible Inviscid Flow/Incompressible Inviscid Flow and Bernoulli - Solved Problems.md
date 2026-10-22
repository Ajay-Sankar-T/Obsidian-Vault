---
title: Incompressible Inviscid Flow and Bernoulli – Solved Problems
tags: [fluid-mechanics, tutorial, bernoulli, pitot, euler]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
source: "White, Fluid Mechanics 4th ed., Ch. 3 Examples 3.21–3.24, Problems P3.156–3.180, FE3.9–3.10; P4.60"
---

# Incompressible Inviscid Flow and Bernoulli – Solved Problems

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · formulas: [[Fluid Mechanics/08 Incompressible Inviscid Flow/Incompressible Inviscid Flow and Bernoulli - Formula Bank|Formula Bank]] · all numbers are recomputed in `Tools/fm_core.py`

Standard data (White): water $\rho=998$ kg/m³; sea-level air $\rho=1.225$ kg/m³, $p_{atm}=101\,350$ Pa; 1 gal/min $=6.309\times10^{-5}$ m³/s.

| # | Problem | Concept | Result |
|---|---|---|---|
| 1 | [[#1. Ex. 3.24 Fire hose nozzle: Bernoulli + momentum]] | Bernoulli → pressure, then force | $F_B=4067$ N |
| 2 | [[#2. FE3.9 Cavitation test in a venturi]] | venturi pressure drop | $p_2=30.5$ kPa |
| 3 | [[#3. FE3.10 Venturi flow rate]] | $Q$ from $\Delta p$ | 263 gal/min |
| 4 | [[#4. P3.156 Blimp: stagnation and static pressure]] | stagnation pressure, frame of reference | 102.04 kPa, 5.9 m/s |
| 5 | [[#5. P3.166 Wind-tunnel test section]] | Pitot / static difference | 26.8 m/s |
| 6 | [[#6. Pitot-static tube readings]] | Pitot formula, manometer, compressibility | 30.0 m/s, 3.52 m/s |
| 7 | [[#7. P3.159 Garden hose pressure]] | Bernoulli + projectile | 23.6 psig |
| 8 | [[#8. P3.179 Draining tank]] | quasi-steady Bernoulli | $t_0=255$ s |
| 9 | [[#9. P3.180 Unsteady Bernoulli: a pipe suddenly opened]] | unsteady term | $\tanh$ law |
| 10 | [[#10. Channel flow dropping a step (P3.177 style)]] | two roots | 0.43 m or 5.93 m |
| 11 | [[#11. P4.60 / P4.26 Vortex flows and pressure]] | Euler normal to streamlines | $z_C=H-\Omega^2R^2/2g$ |

---

## 1. Ex. 3.24 Fire hose nozzle: Bernoulli + momentum

**Concept.** Bernoulli finds the pressure; the control-volume momentum equation turns it into a force.

**Given.** $D_1=10$ cm hose, $D_2=3$ cm nozzle, $Q=1.5$ m³/min $=0.025$ m³/s, water to atmosphere ($p_2=0$ gage), frictionless.

**Steps.**
1. $V_2=\dfrac{Q}{\pi D_2^2/4}=35.4$ m/s, $V_1=\dfrac{Q}{\pi D_1^2/4}=3.18$ m/s.
2. Bernoulli: $p_1=\tfrac12\rho(V_2^2-V_1^2)=\tfrac12(1000)(35.4^2-3.2^2)=6.2\times10^5$ Pa gage.
3. Momentum (flange bolts $F_B$ pull the nozzle back, $p_2=0$): $F_B=p_1A_1-\dot m(V_2-V_1)$, $\dot m=25$ kg/s, $A_1=7.85\times10^{-3}$ m².
$$F_B=4872-805=\boxed{4067\ \text{N}\ (\approx915\ \text{lbf})}$$

**Trap.** $p_1$ is gauge; atmospheric pressure acts on both sides and cancels. This is why a charged hose is hard to hold.

---

## 2. FE3.9 Cavitation test in a venturi

**Given.** 6 cm pipe → 3 cm throat, water, $p_1=120$ kPa, $Q=155$ gal/min $=9.78\times10^{-3}$ m³/s; cavitation begins at the throat. Find $p_v$.

**Steps.** $V_1=3.46$ m/s, $V_2=13.83$ m/s.
$$p_2=p_1-\tfrac12\rho(V_2^2-V_1^2)=120\,000-\tfrac12(998)(191.4-11.96)=30\,500\ \text{Pa}$$
Cavitation begins when $p_2=p_v$: $\boxed{p_v\approx31\ \text{kPa}}$ (option (d)). The throat EGL/HGL picture is in the formula bank.

---

## 3. FE3.10 Venturi flow rate

**Given.** 6 cm → 4 cm, $p_1=120$ kPa, $p_2=50$ kPa, water, frictionless.

$$Q=\frac{A_2}{\sqrt{1-\beta^4}}\sqrt{\frac{2\Delta p}{\rho}},\ \ \beta=\tfrac46,\ \ \beta^4=0.1975$$
$$V_2=\sqrt{\frac{2(70\,000)}{998(1-0.1975)}}=13.22\ \text{m/s},\ \ Q=(1.257\times10^{-3})(13.22)=0.01661\ \text{m}^3/\text{s}=\boxed{263\ \text{gal/min}}$$

(option (c)).

---

## 4. P3.156 Blimp: stagnation and static pressure

**Concept.** Stagnation pressure at the nose; velocities are relative to the blimp.

**Given.** Cruise 75 mi/h $=33.5$ m/s through sea-level air; a transducer between the nose and the side reads $p_{nose}-p_{side}=950$ Pa.

**Steps.**
1. Nose is a stagnation point: $p_{nose}=p_\infty+\tfrac12\rho V^2=101\,350+\tfrac12(1.225)(33.5)^2=\boxed{102\,040\ \text{Pa}}$ (a).
2. Side: $p_{nose}-p_{side}=\tfrac12\rho V_{side}^2\Rightarrow V_{side}=\sqrt{\dfrac{2(950)}{1.225}}=39.4$ m/s **relative to the blimp**, directed backward.
3. In the ground frame the air near the side moves at $39.4-33.5=\boxed{5.9\ \text{m/s}}$ backward (b).

**Trap.** The Bernoulli velocity is relative to the body (steady frame); "absolute" velocity requires subtracting the blimp speed.

---

## 5. P3.166 Wind-tunnel test section

**Given.** Open-circuit tunnel draws sea-level air through a contraction; a wall transducer reads 45 mm of water difference between the inside and outside.

**Steps.**
1. $\Delta p=\rho_wgh=998(9.81)(0.045)=440.6$ Pa $=p_{atm}-p_{test}$ (air at rest outside has $p_0=p_{atm}$).
2. $V=\sqrt{\dfrac{2\Delta p}{\rho_a}}=\sqrt{\dfrac{2(440.6)}{1.225}}=26.8$ m/s $=\boxed{60\ \text{mi/h}}$ (a).
3. A model's nose is a stagnation point: $p_{nose}=p_0=p_{atm}=\boxed{101\,350\ \text{Pa}}$ (b).

---

## 6. Pitot-static tube readings

**Air** (aircraft probe): $p_0-p_s=550$ Pa, $\rho=1.225$:
$$V=\sqrt{2(550)/1.225}=30.0\ \text{m/s}\quad(Ma=0.088;\ \text{compressibility error }Ma^2/4=0.19\%)$$

**Water pipe with mercury U-tube** ($h=5$ cm):
$$V=\sqrt{2gh\Big(\tfrac{\rho_m}{\rho}-1\Big)}=\sqrt{2(9.81)(0.05)(13.63-1)}=3.52\ \text{m/s}$$
(using $\rho_m=13\,600$, $\rho=998$). Forgetting the "$-1$" gives 3.66 m/s, an 4 % error.

**Compressibility at $Ma=0.3$:** $(p_0-p)/(\tfrac12\rho V^2)=1.023$ ✓: reading 2.3 % high in dynamic pressure, 1.1 % in speed.

---

## 7. P3.159 Garden hose pressure

**Given.** 0.625-in hose, 0.375-in nozzle, the garden is 125 ft from the nozzle exit; losses neglected. Minimum gauge pressure in the hose?

**Steps.**
1. Minimum speed to reach 125 ft is for a 45° launch: $R=V_2^2/g\Rightarrow V_2=\sqrt{32.2(125)}=63.4$ ft/s.
2. $V_1/V_2=(0.375/0.625)^2=0.36$.
3. $p_1=\tfrac12\rho(V_2^2-V_1^2)=\tfrac12(1.94)(63.4)^2(1-0.36^2)=3398\ \text{lbf/ft}^2=\boxed{23.6\ \text{psig}}$

---

## 8. P3.179 Draining tank

**Given.** Cylinder diameter $D$, depth $h_0$, plug of diameter $d$ removed. Quasi-steady Bernoulli between the surface (speed $V_1=-dh/dt$) and the jet:
$$V_2^2-V_1^2=2gh,\quad A_1V_1=A_2V_2\ \Rightarrow\ \boxed{\frac{dh}{dt}=-\Big(\frac dD\Big)^2\sqrt{\frac{2gh}{1-(d/D)^4}}}$$
Separate and integrate ($d\ll D$):
$$\boxed{t_0=\Big(\frac Dd\Big)^2\sqrt{\frac{2h_0}{g}}}$$
Example: $D=1$ m, $d=5$ cm, $h_0=2$ m ⇒ $t_0=400(0.639)=255$ s $\approx4.3$ min. The exact factor $\sqrt{1-(d/D)^4}$ differs from 1 by $2\times10^{-5}$.

---

## 9. P3.180 Unsteady Bernoulli: a pipe suddenly opened

**Given.** Large tank (depth $h$ constant), pipe of length $L$ and area $A$ opened at $t=0$ to the atmosphere.

**Steps.** Bernoulli (3.76) from the tank surface (V≈0) to the exit: the unsteady integral is $\int_1^2\partial V/\partial t\,ds=L\,dV/dt$ (all the acceleration is in the pipe):
$$L\frac{dV}{dt}+\frac{V^2}{2}=gh$$
Solution with $V(0)=0$ and $V_\infty=\sqrt{2gh}$:
$$\boxed{V(t)=V_\infty\tanh\!\Big(\frac{V_\infty}{2L}\,t\Big)}$$
Check: $\tanh$ satisfies the ODE exactly (sympy ✓). Example $h=3$ m, $L=12$ m: $V_\infty=7.67$ m/s, time constant $2L/V_\infty=3.13$ s; at $t=3.13$ s $V=0.76V_\infty$.

**Interpretation.** Steady Bernoulli would give $V_\infty$ instantly – the unsteady term explains the inertia of the water column. A closed tank at gage pressure $p_0$ (P3.181): replace $gh$ by $gh+p_0/\rho$.

---

## 10. Channel flow dropping a step (P3.177 style)

> [!note] Geometry assumed
> The figures for P3.177–3.178 are not available as text; I assumed a rectangular channel whose floor **drops by $H$**, with uniform flow and hydrostatic pressure at sections 1 and 2, using the data $h_1=1.5$ m, $H=4$ m, $V_1=3$ m/s. For a rise (bump) change the sign of $H$.

**Steps.**
1. Unit flow $q=V_1h_1=4.5$ m²/s.
2. Surface Bernoulli (pressure atmospheric): $h_1+\dfrac{V_1^2}{2g}+H=h_2+\dfrac{q^2}{2gh_2^2}$, so $E=1.5+0.459+4.0=5.959$ m.
3. $h_2^3-E\,h_2^2+\dfrac{q^2}{2g}=0$ (cubic) has two positive roots:

| root | $h_2$ (m) | $V_2$ (m/s) | $Fr=V/\sqrt{gh}$ | regime |
|---|---|---|---|---|
| shallow | 0.432 | 10.4 | 5.06 | supercritical (fast) |
| deep | 5.93 | 0.76 | 0.10 | subcritical (slow) |

critical depth $h_c=(q^2/g)^{1/3}=1.27$ m. **Both satisfy Bernoulli and continuity**; which one occurs is set by the downstream conditions (the two are connected by a hydraulic jump, which dissipates energy, so Bernoulli cannot cross it). See the figure in the formula bank (§6).

---

## 11. P4.60 / P4.26 Vortex flows and pressure

**Free vortex (drain), $v_\theta=\Omega R^2/r$:** irrotational ⇒ same Bernoulli constant everywhere: pressure falls toward the axis as $p=p_\infty-\tfrac12\rho v_\theta^2$ at fixed $z$. Free-surface depth at $r=R$: $z_C=H-\Omega^2R^2/2g$ (see [[Fluid Mechanics/07 Differential Kinematics and Mass Conservation/Differential Mass Conservation and Fluid Kinematics - Solved Problems#12. P4.60 Draining vortex|kinematics problem 12]]).

**Forced vortex, $v_\theta=\Omega r$:** rotational, Bernoulli does **not** connect different radii. Use Euler normal to the streamlines: $\dfrac{V^2}{R}=\Omega^2r=\dfrac1\rho\dfrac{\partial p}{\partial r}$ ⇒ $p=p_0+\tfrac12\rho\Omega^2r^2$; free surface $z=\Omega^2r^2/2g$ (paraboloid).

**Comparison.** Same speed at $r=R$ but opposite behaviour inside: free vortex surface plunges toward the axis, forced vortex surface rises away from it. Real vortices (Rankine) have a forced core and a free-vortex outer region.

## Related
- [[Fluid Mechanics/08 Incompressible Inviscid Flow/Incompressible Inviscid Flow and Bernoulli - Formula Bank|Formula Bank]], [[Fluid Mechanics/04 Control Volume Analysis/Momentum Equation Applications - Jets, Vanes, Bends|Momentum applications]]

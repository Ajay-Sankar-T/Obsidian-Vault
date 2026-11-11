---
title: Dimensional Analysis and Similitude – Solved Problems
tags: [fluid-mechanics, tutorial, dimensional-analysis, similitude]
up: "[[Fluid Mechanics - MOC]]"
source: "White, Fluid Mechanics 4th ed., Ch. 5 examples and problems P5.x"
---

# Dimensional Analysis and Similitude – Solved Problems

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · formulas: [[Dimensional Analysis and Similitude - Formula Bank|Formula Bank]] · every number is recomputed in `Tools/fm_core.py` (`python fm_core.py`)

| # | Problem | Concept | Result |
|---|---|---|---|
| 1 | [[#1. Ex. 5.6 Capillary rise and its scaling]] | Π groups with a given function, scaling to a similar case | $h_2=1.5$ cm |
| 2 | [[#2. P5.20 Centrifugal pump]] | repeating variables $\{\Omega,\rho,D\}$ | pump laws |
| 3 | [[#3. P5.19 Surface-wave period]] | repeating variables $\{\lambda,\rho,g\}$, neglect of $\sigma$ | $T\sqrt{g/\lambda}=f(h/\lambda)$ |
| 4 | [[#4. P5.37 Blast wave and P5.12, P5.13, P5.32 short derivations]] | $j<3$, special exponents | four laws |
| 5 | [[#5. P5.34 Thermal conductivity of hydrogen]] | $j=4$ with temperature, scale a known value | $k=0.182$ W/m·K |
| 6 | [[#6. P5.4 Water-tested sphere to a weather balloon]] | Reynolds similarity | $V=1.55$ m/s, $F=1.29$ N |
| 7 | [[#7. P5.3 Aircraft altitude from Re and Ma]] | combine $Re$ and $Ma$ with the atmosphere | $z\approx10.2$ km |
| 8 | [[#8. P5.5 Car drag in Colorado]] | interpolate $C_D(Re)$ from data | $F\approx210$ lbf, 36 hp |
| 9 | [[#9. P5.15 Can a 1:20 airplane model be tested?]] | feasibility of matching $Re$ | $V_m=6000$ mi/h: no |
| 10 | [[#10. P5.26 Pendulum on the moon]] | which groups change | $T=2.75$ s |
| 11 | [[#11. Froude-scaled hydraulic model]] | model laws | $V,Q,F$ ratios |

---

## 1. Ex. 5.6 Capillary rise and its scaling

**Concept.** Pi theorem with one angle; scaling a similar experiment.

**Given.** $h=f(d,g,\rho,\sigma,\theta)$, $n=6$. (b) $h_1=3$ cm; case 2 has $d_2=d_1/2,\ \sigma_2=\sigma_1/2,\ \rho_2=2\rho_1,\ \theta_2=\theta_1$.

**Principle.** $\{F L T\}$: $h,d\to L$; $g\to LT^{-2}$; $\rho\to FT^2L^{-4}$; $\sigma\to FL^{-1}$; $\theta$ dimensionless. $j=3$ ⇒ $n-j=3$ groups.

**Steps.**
1. $\Pi_3=\theta$ already dimensionless.
2. Repeating $\{\rho,g,d\}$: $\Pi_1=h/d$; $\Pi_2=\sigma\rho^{-1}g^{-1}d^{-2}=\dfrac{\sigma}{\rho g d^2}$.
3. $\dfrac hd=F\!\left(\dfrac{\sigma}{\rho gd^2},\theta\right)$.
4. For case 2: $\dfrac{\sigma_2}{\rho_2gd_2^2}=\dfrac{\sigma_1/2}{2\rho_1g\,d_1^2/4}=\dfrac{\sigma_1}{\rho_1gd_1^2}$ – the same Π, same $\theta$ ⇒ the same $h/d$.

$$h_2=h_1\frac{d_2}{d_1}=3\times\tfrac12=\boxed{1.5\ \text{cm}}$$

**Trap / alternative.** Only valid because *every* Π matches; if $\sigma$ had changed differently you would need the function $F$ (theory gives $h=4\sigma\cos\theta/(\rho gd)$, Ex. 1.9).

---

## 2. P5.20 Centrifugal pump

**Given.** $P=f(Q,D,\Omega,\rho,\mu)$; $n=6$, $j=3$ ⇒ 3 groups. Repeating $\{\Omega,\rho,D\}$.

**Solution** (the exponents come from `pi_groups`, which also verifies them symbolically):

| group | form | name |
|---|---|---|
| $\Pi_1=P\,\Omega^{-3}\rho^{-1}D^{-5}$ | $\dfrac{P}{\rho\Omega^3D^5}$ | power coefficient $C_P$ |
| $\Pi_2=Q\,\Omega^{-1}D^{-3}$ | $\dfrac{Q}{\Omega D^3}$ | flow coefficient $C_Q$ |
| $\Pi_3=\mu\,\rho^{-1}\Omega^{-1}D^{-2}$ | $\dfrac{\mu}{\rho\Omega D^2}=1/Re$ | Reynolds number |

$$\boxed{\frac{P}{\rho\Omega^3D^5}=g\!\left(\frac{Q}{\Omega D^3},\ \frac{\rho\Omega D^2}{\mu}\right)}$$

**Use.** Same-family pumps ($Re$ nearly irrelevant): $P\propto\rho\Omega^3D^5$, $Q\propto\Omega D^3$. Doubling speed ⇒ power ×8, flow ×2.

---

## 3. P5.19 Surface-wave period

**Given.** $T=f(\rho,\lambda,h,g,\sigma)$, $n=6$, $j=3$. Repeating $\{\lambda,\rho,g\}$.

**Solution.**
$$\Pi_1=T\sqrt{g/\lambda},\qquad\Pi_2=h/\lambda,\qquad\Pi_3=\frac{\sigma}{\rho g\lambda^2}\ (\text{inverse Bond number})$$
$$\boxed{T\sqrt{\frac g\lambda}=F\!\left(\frac h\lambda,\ \frac{\sigma}{\rho g\lambda^2}\right)}$$
If $\sigma$ is negligible (long gravity waves): $T\sqrt{g/\lambda}=F(h/\lambda)$; deep water ($h\gg\lambda$) it becomes a constant ($T=\sqrt{2\pi\lambda/g}$ from theory).

---

## 4. P5.37 Blast wave and P5.12, P5.13, P5.32 short derivations

**P5.37** $\Delta p=f(r,t,a,E)$; $n=5$, $j=3$ ⇒ 2 groups; repeating $\{r,a,E\}$ (independent: determinant of their exponents is 1) – result
$$\frac{\Delta p\,r^3}{E}=g\!\left(\frac{at}{r}\right)\ \Rightarrow\ \Delta p\propto E\ \Rightarrow\ \boxed{\text{doubling }E\text{ doubles }\Delta p}$$

**P5.12** $a=f(p,\rho)$: $[a]=LT^{-1}$, $[p/\rho]=L^2T^{-2}$ ⇒ $a=C\sqrt{p/\rho}$ (one group, constant; theory $C=\sqrt k$).

**P5.13** $C=f(\rho,\lambda,\sigma)$: $n=4$, $j=3$ ⇒ one group; $\sigma/(\rho\lambda)$ has dimensions $L^2T^{-2}$, so $C=\text{const}\sqrt{\sigma/(\rho\lambda)}$. Doubling $\sigma$ at fixed $\rho,\lambda$: $C\to\sqrt2\,C$ (×1.41).

**P5.32** weir $Q=f(g,b,H)$, $Q\propto b$: with $b$ taken out, $Q/b=f(g,H)$, $[Q/b]=L^2T^{-1}$ ⇒ $Q=C\,b\,g^{1/2}H^{3/2}$.

---

## 5. P5.34 Thermal conductivity of hydrogen

**Concept.** Temperature adds a fourth dimension ($j=4$).

**Given.** $k=f(\rho,\lambda,R,T)$ with $k$ in W/m·K, mean free path $\lambda$, gas constant $R$, absolute temperature $T$. Air at 20 °C, 1 atm: $k=0.026$ W/m·K, $\lambda=6.5\times10^{-8}$ m. Hydrogen: $\lambda=1.2\times10^{-7}$ m.

**Principle.** $n=5$ variables, 4 primary dimensions ⇒ $k_\Pi=1$. $\{\rho,\lambda,R,T\}$ repeat; the group
$$\frac{k}{\rho\,\lambda\,R^{3/2}\,T^{1/2}}=\text{const}\qquad\text{(checked symbolically in }\texttt{fm\_core})$$

**Steps** (same $T$ and $p$ ⇒ $\rho\propto1/R\propto M$, molar masses $M_{air}=28.97$, $M_{H_2}=2.016$):
$$\frac{k_{H}}{k_{air}}=\frac{\rho_H}{\rho_{air}}\frac{\lambda_H}{\lambda_{air}}\left(\frac{R_H}{R_{air}}\right)^{3/2}=\frac{1}{14.37}\times1.846\times14.37^{1.5}=1.846\sqrt{14.37}=7.0$$
$$\boxed{k_{H_2}\approx0.182\ \text{W/m·K}}\quad(\text{tabulated }\approx0.18)$$

---

## 6. P5.4 Water-tested sphere to a weather balloon

**Concept.** Dynamic similarity = equal $Re$ (no free surface, low speed).

**Given.** Sphere 8 cm, water 20 °C, $V_w=2$ m/s, drag $F_w=5$ N. Balloon $D=1.5$ m in sea-level standard air.
$\rho_w=998,\ \mu_w=0.001$; $\rho_a=1.225,\ \mu_a=1.78\times10^{-5}$ SI.

**Steps.**
1. $\nu_w=1.002\times10^{-6}$, $\nu_a=1.453\times10^{-5}$ m²/s.
2. $Re$ equal: $V_a=V_w\dfrac{D_w}{D_a}\dfrac{\nu_a}{\nu_w}=2\times\dfrac{0.08}{1.5}\times14.5=\boxed{1.55\ \text{m/s}}$
3. Same $C_D$ ⇒ $\dfrac{F}{\rho V^2D^2}$ equal:
$$F_a=F_w\frac{\rho_a}{\rho_w}\Big(\frac{V_a}{V_w}\Big)^2\Big(\frac{D_a}{D_w}\Big)^2=5\times\frac{1.225}{998}\times0.598\times351.6=\boxed{1.29\ \text{N}}$$

**Trap.** The speed is low because air is 14.5× more viscous *kinematically*. The force follows from the full ratio $F_a/F_w=\frac{\rho_a}{\rho_w}(V_a/V_w)^2(D_a/D_w)^2=0.258$, not from the speed ratio alone.

---

## 7. P5.3 Aircraft altitude from Re and Ma

**Given.** Chord $L=1.2$ m, $Ma=0.7$, $Re_L=7\times10^6$ in the standard atmosphere.

**Principle.** $V=0.7\,a(z)$, $Re=\rho(z)V L/\mu(z)$ – solve for $z$.

**Steps** (ISA troposphere $T=288.15-0.0065z$, $p=101325(T/288.15)^{5.2559}$, $\rho=p/RT$, $a=\sqrt{1.4RT}$, Sutherland $\mu$):

| z (m) | T (K) | ρ (kg/m³) | a (m/s) | μ (Pa·s) | Re |
|---|---|---|---|---|---|
| 10 154 | 222.1 | 0.405 | 298.8 | $1.45\times10^{-5}$ | $7.00\times10^6$ |

$$\boxed{z\approx10\,200\ \text{m}\ (\approx33\,000\ \text{ft}),\quad V=209\ \text{m/s}}$$
(bisection in `fm_core.check()`).

---

## 8. P5.5 Car drag in Colorado

**Concept.** Use dimensionless data: convert measured drag to $C_D$ and compare at equal $Re$.

**Given.** $L=8$ ft, $A=60$ ft². Sea-level data: 31, 115, 249 lbf at 20, 40, 60 mi/h. Colorado: 65 mi/h at 3500 m.

**Steps.**
1. Sea level: $\rho=0.002377$ slug/ft³, $\mu=3.74\times10^{-7}$ slug/ft·s.

| V (mi/h) | $Re_L$ | $C_D=\dfrac{F}{\frac12\rho V^2A}$ |
|---|---|---|
| 20 | $1.49\times10^6$ | 0.505 |
| 40 | $2.99\times10^6$ | 0.469 |
| 60 | $4.48\times10^6$ | 0.451 |

2. At 3500 m (ISA): $\rho=0.863$ kg/m³ $=0.001675$ slug/ft³, $\mu=3.50\times10^{-7}$ slug/ft·s; $V=95.3$ ft/s ⇒ $Re=3.65\times10^6$, inside the data range.
3. Interpolate $C_D$ against $\ln Re$: $C_D\approx0.460$.
4. $$F=C_D\tfrac12\rho V^2A=0.460\times\tfrac12(0.001675)(95.3)^2(60)=\boxed{\approx210\ \text{lbf}},\qquad P=FV=\frac{210\times95.3}{550}=\boxed{\approx36\ \text{hp}}$$

**Trap.** Don't scale by $V^2$ with the sea-level $C_D$ at one speed: $C_D$ depends on $Re$, which changes with altitude *and* speed.

---

## 9. P5.15 Can a 1:20 airplane model be tested?

Same pressure and temperature ⇒ same $\nu$. Equal $Re$: $V_mL_m=V_pL_p\Rightarrow V_m=20\times300=6000$ mi/h $\approx2680$ m/s, i.e. $Ma\approx8$ – compressibility would then dominate and destroy similarity. **Not feasible**; use a pressurised (smaller $\nu$) or cryogenic tunnel, or test at lower $Re$ and extrapolate.

---

## 10. P5.26 Pendulum on the moon

$T=f(L,m,\theta,g)$: $n=5$, $j=2$ ($m$ cannot form a group with $L,g$; $m$ drops out) ⇒ $T\sqrt{g/L}=F(\theta)$.

- (a) 45° vs 20° on earth: **cannot be found by dimensional analysis** (the group changes with $\theta$); you need the function $F$ (for small angles $F=2\pi$).
- (b) Moon, $L=0.3$ m, 20°: same $\theta$ ⇒ same $F$:
$$T_2=T_1\sqrt{\frac{L_2}{L_1}\frac{g_1}{g_2}}=2.04\sqrt{0.3\times\frac{9.81}{1.62}}=\boxed{2.75\ \text{s}}$$
(mass is irrelevant).

---

## 11. Froude-scaled hydraulic model

A spillway at scale $\alpha=1/25$, same fluid:

| Quantity | Law | Value |
|---|---|---|
| velocity | $\alpha^{1/2}$ | 1/5 |
| time | $\alpha^{1/2}$ | 1/5 |
| volume flow | $\alpha^{5/2}$ | $3.2\times10^{-4}$ |
| force | $\alpha^{3}$ | 1/15 625 |
| required $\nu_m/\nu_p$ for $Re$ too | $\alpha^{3/2}$ | 0.008 (impossible) |

So the model is run with water at equal $Fr$ and the model $C_D$–$Re$ data extrapolated to prototype $Re$.

## Related
- [[Dimensional Analysis and Similitude - Formula Bank|Formula Bank]], [[Buckingham Pi Theorem|Buckingham π Theorem]]

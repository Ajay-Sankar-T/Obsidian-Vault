---
title: Tutorial 10 – Flywheel Sizing and Two-Plane Rotor Balancing
course: ME 2201 Kinematics & Dynamics of Machinery
tutorial: 10
due: 2026-11-09
tags:
  - KDoM
  - tutorial-solution
  - flywheel
  - balancing
source: "[[Tutorial 10.pdf]]"
aliases:
  - Flywheel and balancing tutorial
  - Tutorial 10 solution
---

# Tutorial 10 – Flywheel Sizing and Rotor Balancing

Source: [[Tutorial 10.pdf]] · Previous: [[Tutorial-9-solution]] · Theory: [[Flywheel Sizing from the Turning-Moment Diagram]], [[Balancing of Rotors - Static and Dynamic]] · Numbers and figures: `tut9_10.py` (same folder)

> [!summary] Answers at a glance
> | Q | Answer |
> |---|---|
> | 1 | $\Delta E=17.51$ kJ, $I=1996$ kg·m², **flywheel mass $m=1386$ kg** |
> | 2 | **Remove 4.35 kg from plane C at 238.4° and 2.90 kg from plane D at 49.6°**, both clockwise from $A_1$, at $r=10$ cm |

---

## Q1 — Flywheel for a four-stroke gas engine

> [!question] Problem
> Turning-moment diagram = four triangles (areas from the zero-pressure line): suction $0.45\times10^{-3}$, compression $1.7\times10^{-3}$, expansion $6.8\times10^{-3}$, exhaust $0.65\times10^{-3}$ m². $1\ \text{m}^2\leftrightarrow3$ MN·m. Resisting torque uniform. Find the flywheel mass to hold the speed between $202$ and $198$ rpm; $k=1.2$ m.

**Tests:** [[Flywheel Sizing from the Turning-Moment Diagram]], [[Mass Moments of Inertia]]

### Given
$a_1..a_4$ as above; scale $3\times10^{6}$ J/m²; $N_{\max}=202$, $N_{\min}=198$ rpm; $k=1.2$ m; one cycle $=4\pi$ (four strokes of $\pi$ each).

### Principle and why it applies
The flywheel's kinetic energy rises while engine torque exceeds the load and falls while it is below. Largest rise-to-fall swing $\Delta E$ fixes $I$ through $\Delta E=I\omega_{\text{mean}}^2C_s$. A uniform resisting torque must equal the mean engine torque, so it is the cycle work divided by $4\pi$.

![[T10-fig1-turning-moment.png]]

### Solution
**Energies** (area × 3 MN·m):

| Stroke | Area (m²) | Energy | Sign |
|---|---|---|---|
| Suction | $0.45\times10^{-3}$ | 1350 J | − |
| Compression | $1.70\times10^{-3}$ | 5100 J | − |
| Expansion | $6.80\times10^{-3}$ | 20 400 J | + |
| Exhaust | $0.65\times10^{-3}$ | 1950 J | − |

$$
W_{\text{cycle}}=20\,400-(1350+5100+1950)=12\,000\ \text{J},\qquad
T_{\text{mean}}=\frac{12\,000}{4\pi}=954.9\ \text{N·m}
$$

**Peak torque** of the expansion triangle (base $\pi$): $a_3=\tfrac12\pi T_{\max}$

$$
T_{\max}=\frac{2(20\,400)}{\pi}=12\,987\ \text{N·m}
$$

**Excess area** = the part of the expansion triangle above $T_{\text{mean}}$ (triangle $ADE$, similar to the whole):

$$
DE=\pi\frac{T_{\max}-T_{\text{mean}}}{T_{\max}}=2.911\ \text{rad},\qquad
\Delta E=\tfrac12(DE)(T_{\max}-T_{\text{mean}})=\tfrac12(2.911)(12\,032)=\mathbf{17\,510\ J}
$$

**Speeds:**

$$
\omega_{\text{mean}}=\frac{202+198}{2}\cdot\frac{2\pi}{60}=20.944\ \text{rad/s},\qquad
C_s=\frac{202-198}{200}=0.02
$$

**Inertia and mass:**

$$
I=\frac{\Delta E}{\omega_{\text{mean}}^2C_s}=\frac{17\,510}{(20.944)^2(0.02)}=1996\ \text{kg·m}^2,\qquad
m=\frac{I}{k^2}=\frac{1996}{1.2^2}=\mathbf{1386\ kg}
$$

### Result

> [!success] Flywheel mass
> $m\approx\mathbf{1390\ kg}$ ($1386$ kg), with $I=1996$ kg·m² and $\Delta E=17.5$ kJ.

### Check
- **Closure:** integrating $T-T_{\text{mean}}$ numerically over $0$–$4\pi$ returns $0$, and the energy curve's max–min is $17\,510.3$ J, matching the triangle result.
- **Exact speeds:** $\tfrac12I(\omega_{202}^2-\omega_{198}^2)$ gives the same $I=1996$ kg·m²; the arithmetic-mean definition of $\omega_{\text{mean}}$ makes the two forms identical.
- **Where the swing is:** minimum energy at $D$ ($2.04\pi$), maximum at $E$ ($2.96\pi$): the crossings of the mean line on the expansion stroke.
- **Magnitude:** 1.4 t is heavy, but the diagram is large: peak torque $13$ kN·m, a $17.5$ kJ swing and a tight ±1 % band. Relaxing to $C_s=5\%$ would cut it to about 550 kg (fig. below).

![[T10-fig2-sizing.png]]

### Trap / alternative
> [!warning] Traps
> - $T_{\text{mean}}=W/2\pi$ for this four-stroke engine: wrong, it is $W/4\pi$. That doubles $T_{\text{mean}}$ and shrinks $\Delta E$.
> - Using the whole $20\,400$ J as $\Delta E$.
> - Reading the speed range as $\pm$ instead of total: here $C_s=(202-198)/200=2\%$ total.

> [!question]- Shortcut: closed form without finding $DE$
> $\Delta E=\dfrac{\pi\,(T_{\max}-T_{\text{mean}})^2}{2\,T_{\max}}=\dfrac{\pi(12\,032)^2}{2(12\,987)}=17\,510$ J.

---

## Q2 — Two-plane balancing: move the correction to planes C and D

> [!question] Problem
> A rotor is balanced by two 2-kg trial masses in each of planes A and B, at $r=15$ cm, at the angles of Fig. 1. Remove the trial masses, and balance the rotor by taking material from planes C and D at $r=10$ cm. Planes along the shaft: A–C 15 cm, C–D 50 cm, D–B 15 cm. (Mallik & Ghosh problem 7.14.)

**Tests:** [[Balancing of Rotors - Static and Dynamic]], [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]]

### Given and reading of the figure
Angles from the end view, anticlockwise from the $+x$ axis ($A_1$ at the top, $90^\circ$):

| Mass | Plane | Angle read | Clockwise from $A_1$ |
|---|---|---|---|
| $A_1$ | A | $90^\circ$ | 0° |
| $A_2$ | A | $-30^\circ$ (120° clockwise of $A_1$) | 120° |
| $B_2$ | B | $150^\circ$ (60° anticlockwise of $A_1$) | 300° |
| $B_1$ | B | $-60^\circ$ (150° anticlockwise of $B_2$) | 150° |

Each is $2\ \text{kg}\times15\ \text{cm}=30$ kg·cm. Axial positions with $z=0$ at C: $z_A=-15$, $z_C=0$, $z_D=50$, $z_B=65$ cm.

![[T10-fig3-geometry.png]]

### Principle and why it applies
With the trial masses on, the rotor is **completely balanced**: rotor unbalance $+$ trial unbalance $=0$, in force and in couple. So without them the rotor carries unbalance **equal and opposite to the trial system**. Fitting masses in C and D that are **equivalent in force and couple** to the trial masses restores balance, and taking the same amount **off the opposite side** does the same by subtraction. The two-plane replacement fixes both vectors ([[Balancing of Rotors - Static and Dynamic]], §2).

### Solution
**Trial unbalance per plane** (vectors in kg·cm, $\mathbf U=m r e^{j\theta}$):

- Plane A: $30e^{j90^\circ}+30e^{-j30^\circ}=(25.98,\ 15.00)$, magnitude $30.0$ at $30^\circ$.
- Plane B: $30e^{j150^\circ}+30e^{-j60^\circ}=(-10.98,\ -10.98)$, magnitude $15.53$ at $225^\circ$.

**Couple about plane C** fixes plane D:

$$
\mathbf U_D\,(50)=\mathbf U_A(-15)+\mathbf U_B(65)
\;\Rightarrow\;
\mathbf U_D=\frac{(-389.7,-225.0)+(-713.7,-713.7)}{50}=(-22.07,\ -18.77)
$$

$|\mathbf U_D|=28.97$ kg·cm at $220.4^\circ$, so $m_D=28.97/10=2.90$ kg.

**Force balance** fixes plane C:

$$
\mathbf U_C=\mathbf U_A+\mathbf U_B-\mathbf U_D=(37.07,\ 22.79)
$$

$|\mathbf U_C|=43.52$ kg·cm at $31.6^\circ$, so $m_C=4.35$ kg.

These are the masses that would be **added**. Material is **removed** at the diametrically opposite angle ($+180^\circ$):

| Plane | Mass | Equivalent added at | **Remove at** (anticlockwise from $x$) | **Remove at (clockwise from $A_1$)** |
|---|---|---|---|---|
| C | 4.35 kg | $31.6^\circ$ | $211.6^\circ$ | **238.4°** |
| D | 2.90 kg | $220.4^\circ$ | $40.4^\circ$ | **49.6°** |

![[T10-fig4-balance.png]]

### Result

> [!success] Material to remove at $r=10$ cm
> **Plane C:** $4.35$ kg at $238.4^\circ$ clockwise from $A_1$ (pointing lower-left).
> **Plane D:** $2.90$ kg at $49.6^\circ$ clockwise from $A_1$ (pointing upper-right).

### Check
- **Closure:** with these removals, the net force and the net couple of rotor plus correction sum to zero to $10^{-13}$ kg·cm (script).
- **Against the book:** the answer key of Mallik & Ghosh lists $m_C=4.35$ kg at $240^\circ$ and $m_D=2.84$ kg at $50^\circ$, clockwise from $A_1$. My $m_C$ matches, both angles are within $2^\circ$, and $m_D$ is $2\%$ above the key. The polygons close exactly with my values; I could not find the source of the key's $2.84$ kg (it looks like limited-precision arithmetic).
- **Physical sense:** C is next to A and D next to B, so each takes up mostly its neighbour's direction: $\mathbf U_C$ points at $31.6^\circ$ (A's resultant is at $30^\circ$) and $\mathbf U_D$ at $220.4^\circ$ (B's is at $225^\circ$).

### Trap / alternative
> [!warning] Traps
> - Giving the **added** position when material is **removed** — differs by 180°.
> - Dividing by $15$ cm instead of $10$ cm: the plane radii differ, so convert $\mathbf U$ to mass with the new radius.
> - Sign of $z_A$: A lies on the opposite side of C from D, so $z_A=-15$.
> - Taking moments about plane A but forgetting the sign of the couple.

> [!question]- Alternative: moments about plane D instead of C
> $\mathbf U_C(-50)=\mathbf U_A(-65)+\mathbf U_B(15)$, giving the same $\mathbf U_C=(37.07,\ 22.79)$. It must, since the answer cannot depend on the reference plane.

---

## Summary of answers

> [!success] Final answers
> 1. $\Delta E=17.5$ kJ, $I=1996$ kg·m², **$m=1386$ kg**.
> 2. Remove **4.35 kg in plane C at 238.4°** and **2.90 kg in plane D at 49.6°** (clockwise from $A_1$, $r=10$ cm).

### Quick revision
- [ ] Four-stroke: $T_{\text{mean}}=W/4\pi$ · $\Delta E=I\omega_{\text{mean}}^2C_s$ · $m=I/k^2$
- [ ] $\Delta E$ = area of the diagram **above the mean line** on the power stroke
- [ ] Balance: force polygon of $mr$ closes, couple polygon of $mrz$ closes
- [ ] Remove at $\theta+180^\circ$ = add at $\theta$

---

## Appendix

```python
import numpy as np
# Q1
E = {'suc': 1350, 'comp': 5100, 'exp': 20400, 'exh': 1950}
Tm = (E['exp'] - E['suc'] - E['comp'] - E['exh']) / (4*np.pi)          # 954.9
Tmax = 2*E['exp']/np.pi                                                # 12987
dE = np.pi*(Tmax - Tm)**2/(2*Tmax)                                     # 17510 J
w = 200*2*np.pi/60
I = dE/(w**2*0.02); print(dE, I, I/1.2**2)                             # 17510  1996  1386

# Q2
c = lambda a: np.exp(1j*np.radians(a))
UA = 30*(c(90) + c(-30)); UB = 30*(c(150) + c(-60))
UD = (UA*(-15) + UB*65)/50; UC = UA + UB - UD
for U in (UC, UD):
    print(abs(U)/10, np.degrees(np.angle(U)) % 360, (90 - (np.degrees(np.angle(U)) + 180)) % 360)
# 4.352 31.59 238.4   |   2.898 220.4 49.6
```

### Figure index
`T10-fig1` turning-moment and energy curve · `fig2` mass against $C_s$ and $k$ · `fig3` rotor and trial masses · `fig4` polygons and the answer. In the `assets` folder; produced by `tut9_10.py`.

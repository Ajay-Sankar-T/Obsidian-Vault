---
title: Gear Formula Bank – Ghosh & Mallik Ch. 9
course: ME 2201 Kinematics & Dynamics of Machinery
tags:
  - KDoM
  - formula-bank
  - gears
  - involute
  - epicyclic
source: "[[Ghosh and Mallik.pdf]]"
pages: "PDF p. 411–441 (book pp. 402–432), Sections 9.1–9.8"
aliases:
  - Gear formulae
  - Gear formula sheet
---

# Gear Formula Bank

Source: [[Ghosh and Mallik.pdf]] (Theory of Mechanisms and Machines), Chapter 9 from PDF p. 411 · Applied in [[Tutorial-7-solution]]
Equation numbers in brackets, e.g. **(9.17)**, are the book's own.

> [!abstract] Contents
> [[#0. Symbols]] · [[#1. Terminology and tooth proportions]] · [[#2. Fundamental law of gearing]] · [[#3. Involute geometry]] · [[#4. Contact ratio]] · [[#5. Interference and undercutting]] · [[#6. Conjugate profile synthesis]] · [[#7. Helical gears]] · [[#8. Spiral gears]] · [[#9. Bevel and worm gears]] · [[#10. Gear trains]] · [[#11. Epicyclic trains]] · [[#12. Torques in epicyclic trains]] · [[#13. Benchmark values]] · [[#14. Notes on the book's equations]] · [[#15. Visualisation tools]]

> [!tip] Quick pick
> | I need… | Go to |
> |---|---|
> | $p,\ P,\ m$, addendum, dedendum | [[#1. Terminology and tooth proportions]] |
> | $r_b,\ \text{inv}\,\alpha$, involute coordinates | [[#3. Involute geometry]] |
> | length of action, $m_c$ | [[#4. Contact ratio]] |
> | minimum teeth, interference check | [[#5. Interference and undercutting]] |
> | helical / spiral / worm / bevel | [[#7. Helical gears]] – [[#9. Bevel and worm gears]] |
> | train value, planetary speeds | [[#10. Gear trains]], [[#11. Epicyclic trains]] |

---

## 0. Symbols

| Symbol | Meaning | Symbol | Meaning |
|---|---|---|---|
| $N$ | number of teeth | $\alpha$ | pressure angle |
| $d_p,\ r_p$ | pitch diameter, radius | $r_b$ | base-circle radius |
| $r_o$ | outer (addendum-circle) radius | $C$ | centre distance |
| $p$ | circular pitch | $p_b$ | base pitch |
| $P$ | diametral pitch | $m$ | module |
| $a,\ b,\ c$ | addendum, dedendum, clearance | $f$ | addendum as fraction of module, $a=fm$ |
| $\lambda=\omega_2/\omega_1$ | speed ratio (pinion = 1) | $m_c$ | contact ratio |
| $\psi$ | helix angle | $\theta$ | shaft angle |
| $n$ | speed (rpm) | $M$ | torque |

---

## 1. Terminology and tooth proportions

![[GFB-fig1-terminology.png]]

| Quantity                    | Formula                                                       | Eq.    |
| --------------------------- | ------------------------------------------------------------- | ------ |
| Circular pitch              | $p=\dfrac{\pi d_p}{N}$                                        | (9.1)  |
| Diametral pitch             | $P=\dfrac{N}{d_p}$                                            | (9.2)  |
| Pitch relation              | $pP=\pi$                                                      |        |
| Module                      | $m=\dfrac{d_p}{N}=\dfrac1P$                                   | (9.3)  |
| Standard addendum           | $a=m$                                                         |        |
| Standard dedendum           | $b=1.25\,m$                                                   |        |
| Clearance                   | $c=b-a=0.25\,m$                                               |        |
| Addendum as module fraction | $a=fm=\dfrac{f\,2r_{p}}{N}$                                   | (9.16) |
| Centre distance             | $C=r_{p1}+r_{p2}$                                             |        |
| Pinion / wheel / rack       | smaller gear / larger gear / $r_p\to\infty$ (translates only) |        |

**Pressure angles:** 14½° (old, $\sin14\tfrac12^\circ\approx\tfrac14$), **20°** (current), 22½° or 25° (aerospace).

---

## 2. Fundamental law of gearing

![[GFB-fig3-fundamental-law.png]]

> [!important] Law
> The common normal at the point of contact must cut the line of centres at a **fixed point $P$** (the pitch point). Then the angular-velocity ratio is constant.

$$
\frac{\omega_2}{\omega_3}=\frac{O_3P}{O_2P}=\text{const}\qquad(\text{Fig. 9.3, instantaneous centre }23=P)
$$

| Relation | Formula | Eq. |
|---|---|---|
| Average speeds | $(\omega_1)_{av}=2\pi n/N_1,\ (\omega_2)_{av}=2\pi n/N_2$ | |
| Proper action | $\dfrac{\omega_1}{\omega_2}=-\dfrac{N_2}{N_1}=\text{const}$ | |
| Rolling pitch circles | $\dfrac{\omega_1}{\omega_2}=\dfrac{r_{p2}}{r_{p1}}$ | (9.4) |
| Belt (base circle) analogue | $\dfrac{\omega_1}{\omega_2}=\dfrac{r_{b2}}{r_{b1}}=\dfrac{r_{p2}}{r_{p1}}$ | (9.5) |
| Involute advantage | ratio unchanged if $C$ changes; pitch radii change, $r_{p1}/r_{p2}=r_{b1}/r_{b2}$, $r_{p1}+r_{p2}=C$ | |

---

## 3. Involute geometry

![[GFB-fig2-involute.png]]

String unwrapped length $\rho$ from base circle $r_b$:

$$
\rho=r_b(\psi+\delta)=r_b\tan\alpha\quad(9.6),\qquad \psi+\delta=\tan\alpha\quad(9.7)
$$

$$
x=r_b\big[\cos\psi+(\psi+\delta)\sin\psi\big]\ (9.8),\qquad
y=r_b\big[\sin\psi-(\psi+\delta)\cos\psi\big]\ (9.9)
$$

$$
\psi=\tan\alpha-\alpha-\delta=\text{inv}(\alpha)-\delta,\qquad \boxed{\text{inv}\,\alpha=\tan\alpha-\alpha}\quad(9.10)
$$

(Here $\delta$ is the angular offset of the involute's start. With $\delta=0$ the point $Q$ lies at polar angle $\theta=\text{inv}\,\alpha$ from the start of the curve, as drawn in the figure; the tangent point $T$ is at $\tan\alpha$.)

| Quantity | Formula |
|---|---|
| Base radius | $r_b=r_p\cos\alpha$ |
| Radius at pressure angle $\alpha_r$ | $r=\dfrac{r_b}{\cos\alpha_r}$ |
| Base pitch | $p_b=\dfrac{2\pi r_b}{N}=p\cos\alpha$ |
| Involute exists only for | $x^2+y^2\ge r_b^2$ (none inside the base circle; radial below it) |
| Common normal | tangent to both base circles = line of action |

| $\alpha$ | $\text{inv}\,\alpha$ |
|---|---|
| 14.5° | 0.00554 |
| 20° | 0.01490 |
| 25° | 0.02998 |

---

## 4. Contact ratio

![[GFB-fig4-contact-ratio.png]]

**Two gears** (length of action $EF=AF+BE-AB$):

$$
EF=\sqrt{r_{o1}^2-r_{b1}^2}+\sqrt{r_{o2}^2-r_{b2}^2}-C\sin\alpha\qquad(9.11)
$$

$$
m_c=\frac{EF}{p_b}=\frac{\sqrt{r_{o1}^2-r_{b1}^2}+\sqrt{r_{o2}^2-r_{b2}^2}-C\sin\alpha}{2\pi r_{b2}/N_2}\qquad(9.12)
$$

**Pinion and rack** (rack addendum $a_r$):

$$
EF=\frac{a_r}{\sin\alpha}+\sqrt{r_{o1}^2-r_{b1}^2}-r_{b1}\tan\alpha\qquad(9.13)
$$

$$
m_c=\frac{N_1}{2\pi r_{b1}}\Big[\frac{a_r}{\sin\alpha}+\sqrt{r_{o1}^2-r_{b1}^2}-r_{b1}\tan\alpha\Big]\qquad(9.14)
$$

> [!note] Rule of thumb
> $m_c=1.3$ means alternately one and two tooth pairs in contact (time average 1.3). Aim for $m_c\gtrsim1.4$. Raising the addendum raises $m_c$ but can cause interference.

---

## 5. Interference and undercutting

![[GFB-fig6-interference.png]]

**Condition to avoid interference:** both addendum circles must cut the common tangent $AB$ **between** the tangent points $A$ and $B$. With equal addenda, the pinion interferes first.

$$
a=O_2P\Big[\sqrt{1+\lambda(\lambda+2)\sin^2\alpha}-1\Big],\quad\lambda=\frac{\omega_2}{\omega_1}=\frac{N_1}{N_2}\qquad(9.15)
$$

| Case | Minimum pinion teeth | Eq. |
|---|---|---|
| Pinion with wheel, $a=fm$ | $N_{1,\min}=\dfrac{2f\lambda}{\sqrt{1+\lambda(\lambda+2)\sin^2\alpha}-1}$ | (9.17) |
| Pinion with rack | $N_{1,\min}=\dfrac{2f}{\sin^2\alpha}$ | (9.18) |
| Equal gears ($\lambda=1$) | $3N^2\sin^2\alpha-4fN-4f^2=0$ | Prob. 9.13 |

Rack, $f=1$: 14.5° → 31.9, 20° → 17.1, 25° → 11.2.

![[GFB-fig5-min-teeth.png]]

> [!tip] Remedies for small $N$
> Undercut (weakens tooth), larger $\alpha$, shorter addendum, or involute-cycloidal profiles. Round $N_{1,\min}$ **up**, then take $N_2=N_1/\lambda$ and check the speed ratio (Prob. 9.3).

---

## 6. Conjugate profile synthesis

**Analytic method** — gears with pitch radii $r_{p1},r_{p2}$, $C=r_{p1}+r_{p2}$, tooth $y_1=f_1(x_1)$; $\theta_1,\theta_2$ are the inclinations of the line of centres in each frame.

| Step | Formula | Eq. |
|---|---|---|
| Given tooth, gear 1 | $y_1=f_1(x_1)$ | (9.19) |
| Wanted tooth, gear 2 | $y_2=f_2(x_2)$ | (9.20) |
| Rolling | $r_{p1}\theta_1=r_{p2}\theta_2$ | |
| Angle between frames | $\theta_1+\theta_2=\gamma\theta_1,\quad\gamma=1+\dfrac{r_{p1}}{r_{p2}}$ | (9.21) |
| Transformation | $x_2=(x_1-C\cos\theta_1)\cos\gamma\theta_1+(y_1-C\sin\theta_1)\sin\gamma\theta_1$ | (9.22) |
| | $y_2=-(x_1-C\cos\theta_1)\sin\gamma\theta_1+(y_1-C\sin\theta_1)\cos\gamma\theta_1$ | (9.23) |
| Normal $PN$ through $P=(r_{p1}\cos\theta_1,\ r_{p1}\sin\theta_1)$ | $y_1-r_{p1}\sin\theta_1=-\dfrac{1}{f_1'(x_1)}\,(x_1-r_{p1}\cos\theta_1)$ | (9.24) |
| Parametric form | $x_1=x_1(\theta_1),\ y_1=y_1(\theta_1)$ → $x_2=x_2(\theta_1),\ y_2=y_2(\theta_1)$ | (9.25, 9.26) |

Solve (9.19)+(9.24) for the contact point $N$, then map with (9.22), (9.23). The locus of $N$ in a fixed frame is the line of action.

**Constant pressure angle** (constant bearing reaction): $F_c\cos\alpha$ and $F_c\sin\alpha$ components, torque $T_1=F_c\cos\alpha\,r_{p1}$, profile slope

$$
y_1'=\tan(\theta_1+\alpha)\quad(9.27),\qquad y_1=r_{p1}\sin\theta_1-\frac{x_1-r_{p1}\cos\theta_1}{\tan(\theta_1+\alpha)}\quad(9.28)
$$

Linear ODE for the contact point, and its solution (constant of integration $(\tan\alpha-\alpha)\,r_{p1}\cos\alpha$):

$$
\frac{dx_1}{d\theta_1}-x_1\cot(\theta_1+\alpha)=-\frac{r_{p1}\cos\alpha\cos^2(\theta_1+\alpha)}{\sin(\theta_1+\alpha)}\quad(9.29)
$$

$$
x_1=r_{p1}\cos\alpha\big[(\theta_1+\tan\alpha)\sin(\theta_1+\alpha)+\cos(\theta_1+\alpha)\big]\quad(9.30)
$$

$$
y_1=r_{p1}\cos\alpha\big[\sin(\theta_1+\alpha)-(\theta_1+\tan\alpha)\cos(\theta_1+\alpha)\big]\quad(9.31)
$$

This is an **involute** with $r_{b1}=r_{p1}\cos\alpha$ (9.32), $\psi=\theta_1+\alpha$ (9.33), $\delta=\tan\alpha-\alpha=\text{inv}\,\alpha$; it cuts the pitch circle on the $x_1$-axis ($\theta_1=0\Rightarrow x_1=r_{p1},\ y_1=0$). With $\theta_2=r_{p1}\theta_1/r_{p2}$, the mating tooth is

$$
x_2=-r_{p2}\cos\alpha\big[(-\theta_2+\tan\alpha)\sin(-\theta_2+\alpha)+\cos(-\theta_2+\alpha)\big]\quad(9.34)
$$

$$
y_2=r_{p2}\cos\alpha\big[(-\theta_2+\tan\alpha)\cos(-\theta_2+\alpha)-\sin(-\theta_2+\alpha)\big]\quad(9.35)^{\dagger}
$$

> [!warning] $\dagger$ Sign in (9.35)
> The book prints **$+\sin(-\theta_2+\alpha)$**. Pushing (9.30)–(9.31) through the book's own transformation (9.22)–(9.23) gives **$-\sin$** (checked numerically, 7 values of $\theta_1$; (9.34) matches exactly). Use the minus sign above. See [[#14. Notes on the book's equations]].

![[GFB-fig11-analytic-involute.png]]

> [!example] Worked pattern (Prob. 9.5: trapezoidal tooth, 12→24 teeth, $r_{p1}=12.5$ cm)
> Flank $y_1=4.96-0.268x_1$, line of action $y_1-12.5\sin\theta_1=3.73(x_1-12.5\cos\theta_1)$, intersection $x_1=1.24+11.65\cos\theta_1-3.125\sin\theta_1$, $y_1=4.628-3.13\cos\theta_1+0.837\sin\theta_1$, then (9.22), (9.23) with $\gamma=1.5$. Plotted in ![[GFB-fig12-problem-9-5.png]]

**Graphical method:** tangent at $Q_1$ → normal through $Q_1$ meets the arc of radius $O_1P$ about $O_1$ → rotate back to bring that point to $P$ → carry $PQ$ round gear 2 using $r_{p1}\theta_1=r_{p2}\theta_2$ (arc $PQ_1'$ = arc $PQ_{12}$).

---

## 7. Helical gears

![[GFB-fig7-helical.png]]

| Quantity | Formula | Eq. |
|---|---|---|
| Normal circular pitch | $p_n=p\cos\psi$ | (9.36) |
| Normal diametral pitch | $P_n=\dfrac{P}{\cos\psi}$ | (9.37) |
| Lead angle | $90^\circ-\psi$ | |
| Minimum face width | $b_{\min}=\dfrac{p}{\tan\psi}$ | (9.38) |
| AGMA recommendation | $b_{\min}=\dfrac{1.15\,p}{\tan\psi}$ | (9.39) |

Mating helices have **opposite hands**; helical gears give axial thrust (cancelled by double-helical / herringbone).

---

## 8. Spiral (crossed-helical) gears

![[GFB-fig8-spiral.png]]

| Hands | Shaft angle $\theta$ | Eq. |
|---|---|---|
| same | $\theta=\alpha+\beta$ | (9.40) |
| opposite | $\theta=\alpha-\beta$ | (9.41) |

$\alpha,\beta$ = helix angles. Point contact only → light loads. Centre distance = shortest distance between the shaft axes.
*Prob. 9.6:* $\theta=15^\circ$, one gear right-hand $25^\circ$ → the other is **left-hand, 10°**.

---

## 9. Bevel and worm gears

**Bevel** (intersecting shafts): pitch surfaces are cones; pitch diameter specified at the large end.

$$
\theta=\gamma_1+\gamma_2\qquad(\gamma_i=\text{pitch angles},\ \theta=\text{shaft angle})
$$

$\gamma=90^\circ$ → crown (face) gear (analogue of a rack). Spiral-bevel = helical teeth; hypoid = offset shafts (hyperboloids).

**Worm and wheel**

![[GFB-fig9-worm.png]]

| Quantity | Formula | Eq. |
|---|---|---|
| Lead | $l=p_xN_1$ | (9.42) |
| Speed ratio | $\dfrac{\omega_1}{\omega_2}=\dfrac{N_2}{N_1}$ | (9.43) |
| Shafts at 90° | $p_x=p$ (wheel circular pitch); lead angle of worm = helix angle of wheel | |
| Shafts at 90° | $\dfrac{\omega_1}{\omega_2}=\dfrac{\pi D_{p2}}{l}$ | (9.44) |

$p_x$ = axial pitch of worm, $N_1$ = threads on worm, $N_2$ = teeth on wheel. Line contact → higher loads than spiral gears; large reduction.

---

## 10. Gear trains

**Simple train** (one gear per shaft) – idlers drop out of the ratio:

$$
\frac{n_A}{n_B}=\frac{N_B}{N_A},\ \ \frac{n_B}{n_C}=\frac{N_C}{N_B},\ \ \frac{n_C}{n_D}=\frac{N_D}{N_C}\ \Rightarrow\ \frac{n_A}{n_D}=\frac{N_D}{N_A}\qquad(9.45,\ 9.46)
$$

Parallel axes: external mesh reverses sense, so include signs, $\dfrac{n_A}{n_B}=-\dfrac{N_B}{N_A}$, …, $\dfrac{n_A}{n_D}=-\dfrac{N_D}{N_A}$ **(9.45a, 9.46a)**; bevel trains use axis vectors (right-hand screw).

**Compound train** ($n_B=n_C$ on one shaft):

$$
\frac{n_A}{n_D}=\frac{N_B}{N_A}\cdot\frac{N_D}{N_C}\ \ (\text{with signs: }(-1)^{k})=\text{train value}\qquad(9.47)
$$

Internal gearing: both gears turn the **same** way. Sign rule: $(-1)^{\#\text{external meshes}}$.

---

## 11. Epicyclic trains

**Degrees of freedom** (simple planetary: 4 links, $j=3$ hinges, $h=1$ higher pair)

$$
F=3(n-1)-2j-h=9-6-1=2
$$

→ two inputs needed (or one input → two outputs). If one gear is fixed: sun (fixed gear), planet, arm = planet carrier.

![[GFB-fig10-epicyclic-table.png]]

### 11.1 Algebraic (Willis) method

$$
\boxed{\frac{n_B-n_{arm}}{n_A-n_{arm}}=\text{train value from A to B}}\qquad(9.48)
$$

For one external mesh the train value is $-N_A/N_B$; for a chain use the product of ratios with $(-1)^k$. (The book prints (9.48) in magnitude form and says to judge the sign from the sense of rotation.)

### 11.2 Tabular method

| Step | Arm | Gear 1 | Gear 2 … |
|---|---|---|---|
| (i) all gears locked to arm, give arm $x$ turns | $x$ | $x$ | $x$ |
| (ii) arm fixed, give gear 1 $y$ turns | $0$ | $y$ | $y\times$ (train ratio, with sign) |
| (iii) resultant | $x$ | $x+y$ | $x+y\times(\dots)$ |

Two inputs → two equations → $x,\ y$ → all speeds. CCW positive. If tooth counts are missing assume equal pitch: $r_C=r_H+r_K+r_L\Rightarrow N_C=N_H+N_K+N_L$ (Prob. 9.9).

### 11.3 Differential (automobile rear axle)

$$
n_B=\frac{n_D+n_E}{2}\qquad(\text{ring gear speed = arithmetic mean of the two wheel speeds})
$$

Straight running: planets act as keys, $n_B=n_D=n_E$.

---

## 12. Torques in epicyclic trains

Constant speeds (no acceleration):

$$
M_1+M_2+M_3=0\quad(9.49),\qquad M_1\omega_1+M_2\omega_2+M_3\omega_3=0\quad(9.50)\ \ (\text{no friction})
$$

Sun gear held: $\omega_3=0$ (9.51) → $M_3$ = **holding torque**; $M_2=-M_1\dfrac{\omega_1}{\omega_2}$, $M_3=-(M_1+M_2)$. Input torque from power: $M_1=\dfrac{\text{Power}\times60}{2\pi n_1}$.

---

## 13. Benchmark values (reproduced numerically)

Every row is recomputed by `gear_core.check()` each time the figures are regenerated.

| Prob. | Data | Result from the formulas |
|---|---|---|
| 9.1 | $r_p=51.5,\ 64.2$; $r_o=57.5,\ 71.2$; $\alpha=20^\circ$; $N_2=20$ | $r_b=48.39,\ 60.33$; $EF=29.3$ mm; $m_c=1.55$ |
| 9.2 | pinion $r_p=62$, $m=4$, rack $a_r=4$, $\alpha=20^\circ$ | $N_1=31$, $r_b=58.26$; $m_c=1.82$ |
| 9.3 | $N=16,18$, $f=1$, $\alpha=14.5^\circ$ | $N_{1,\min}=22.94\to23$; wheel 26 (ratio 0.885) or exactly 24/27 |
| 9.4 | rack, $f=1$, $\alpha=20^\circ$ | $N_{1,\min}=17.1\to18$ |
| 9.6 | $\theta=15^\circ$, RH $25^\circ$ | LH, $10^\circ$ |
| 9.7 | arm 1 turn CCW, B fixed (Ferguson's paradox) | $n_D=-1/49,\ n_E=+1/51$ |
| 9.8 | $n_C=0,\ n_B=1000$ | $n_{arm}=200,\ n_F=-50$ rpm; $x=200,\ y=800$ |
| 9.9 | $n_A=270$ CCW, casing fixed | $x=216,\ y=144$; output 90 rpm, opposite to input |
| 9.10 | 7.5 kW at 1000 rpm | $M_1=71.66$, $M_2=1433$, $M_3=-1504.66$ N·m |

![[GFB-fig13-mesh.png]]

---

## 14. Notes on the book's equations

> [!warning] Things to keep in mind
> 1. **(9.35)** — printed with $+\sin$; the transformation (9.22)–(9.23) gives $-\sin$ (see [[#6. Conjugate profile synthesis]]). (9.34) is fine.
> 2. **(9.48)** — the sign of the train value is not printed; use $(-1)^k$ for $k$ external meshes, as the worked problems do.
> 3. **(9.45)–(9.47)** — unsigned forms hold for magnitudes only; parallel axes need (9.45a)/(9.46a).
> 4. **Prob. 9.10** — $7.5\times10^3\times60/(2\pi\times1000)=71.62$ N·m; the book rounds to 71.66, so $M_2$, $M_3$ differ by ≲ 0.1 %.
> 5. **Problem 9.3** rounds $N_{1,\min}$ up (22.94 → 23). Always round up; a smaller $N$ interferes.
> 6. The text layer of the PDF is duplicated and garbles some fractions; equations here were reconstructed and then re-derived or checked numerically where possible.

---

## 15. Visualisation tools

### Figures (all in `Formula-Bank/assets`)

| Figure | Shows | Section |
|---|---|---|
| `GFB-fig1-terminology` | rack + mating tooth: $a,\ b,\ c,\ p,\ \alpha$ | [[#1. Terminology and tooth proportions]] |
| `GFB-fig3-fundamental-law` | common normal, belt analogue, two involutes | [[#2. Fundamental law of gearing]] |
| `GFB-fig2-involute` | string construction, $\text{inv}\,\alpha$ curves | [[#3. Involute geometry]] |
| `GFB-fig4-contact-ratio` | $A,B,E,F,P$, length of action, zoom | [[#4. Contact ratio]] |
| `GFB-fig6-interference` | $N=7,\ 12.32,\ 20$ with tangent points | [[#5. Interference and undercutting]] |
| `GFB-fig5-min-teeth` | $N_{1,\min}$ vs $\lambda$ and $\alpha$ | [[#5. Interference and undercutting]] |
| `GFB-fig11-analytic-involute` | (9.30)–(9.35) verified by transformation | [[#6. Conjugate profile synthesis]] |
| `GFB-fig12-problem-9-5` | conjugate of a trapezoidal tooth | [[#6. Conjugate profile synthesis]] |
| `GFB-fig7-helical` | $p,\ p_n,\ b_{\min}$ on the unrolled cylinder | [[#7. Helical gears]] |
| `GFB-fig8-spiral` | $\theta=\alpha\pm\beta$ | [[#8. Spiral (crossed-helical) gears]] |
| `GFB-fig9-worm` | lead $l=p_xN_1$ | [[#9. Bevel and worm gears]] |
| `GFB-fig10-epicyclic-table` | tabular method as bars (Probs. 9.7, 9.8) | [[#11. Epicyclic trains]] |
| `GFB-fig13-mesh` | real 20/30 involute mesh | [[#13. Benchmark values]] |

### Animation – involute mesh, contact points moving along $E\to F$

![[GFB-anim-mesh.gif]]

The counter shows one or two tooth pairs in contact; its average is $m_c=1.61$ for this 20/30, $m=10$ mm, 20° pair.

### Interactive explorer

**[Open gear-explorer.html](gear-explorer.html)** — in Obsidian: right-click the file in the sidebar → *Open in default app* (it is a single self-contained page, no internet needed).
Sliders for $N_1,N_2,m,\alpha,f$ and live values of $r_p,r_b,r_o,C,p,p_b,EF,m_c,N_{\min}$ with an interference verdict, a running mesh drawing with the line of action, and calculators for helical, spiral, worm and planetary trains.

### Regenerating

```
cd KDoMs/Formula-Bank
python gear_viz.py            # all figures (runs the benchmark checks first)
python gear_viz.py fig4 anim  # selected ones
```

[[gear_core.py]] holds the formulae and self-checks; [[gear_viz.py]] draws everything.


## Cross-domain links

- [[Cross-Domain Synthesis/Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]] — a gear pair is a lossless two-port like an ideal transformer; load inertia reflects by (ratio)². Map: [[KDoMs/KDoMs - MOC|KDoMs MOC]].

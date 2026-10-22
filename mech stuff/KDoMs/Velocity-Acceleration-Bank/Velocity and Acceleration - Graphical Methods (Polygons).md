---
title: Velocity and Acceleration – Graphical Methods (Polygons)
course: ME 2201 Kinematics & Dynamics of Machinery
tags:
  - KDoM
  - formula-bank
  - kinematics
  - velocity-polygon
  - acceleration-polygon
  - graphical
source: "[[Ghosh and Mallik.pdf]]"
pages: "PDF p. 75–114 (Secs. 2.3–2.8), book pp. 66–105"
aliases:
  - Velocity polygon
  - Acceleration polygon
  - Velocity and acceleration diagrams
---

# Velocity and Acceleration – Graphical Methods (Polygons)

Source: [[Ghosh and Mallik.pdf]], Ch. 2 · Companion: [[Velocity and Acceleration - Analytical Method]] · Mechanisms: [[Motion and Path Generation - Graphical Methods]]
Equation numbers in brackets are the book's.

> [!abstract] Contents
> [[#1. Principle of the diagrams]] · [[#2. Vector equations to use]] · [[#3. Velocity and acceleration images]] · [[#4. Worked constructions]] · [[#5. Instantaneous centres]] · [[#6. Complex mechanisms]] · [[#7. Rules, scales and signs]] · [[#8. Checks and tools]] · [[#9. Notes on the book]]

> [!tip] Which method?
> | Mechanism | Method |
> |---|---|
> | simple (the radius of curvature of every motion-transfer point is known) | direct polygons, [[#4. Worked constructions]] |
> | velocity only, many links | instantaneous centres, [[#5. Instantaneous centres]] |
> | floating ternary link, **low** complexity (another input link makes it simple) | normal accelerations or Goodman, [[#6. Complex mechanisms]] |
> | floating ternary link, **high** complexity | auxiliary points (+ normal components), [[#6. Complex mechanisms]] |

---

## 1. Principle of the diagrams

- The fixed link is represented by a **point**, the **pole** $o$ (for several fixed points $O_2,O_4,\dots$ the same pole $o_2\equiv o_4$).
- Each vector in the diagram is an **absolute** velocity (or acceleration) drawn from the pole; the line joining two image points is the **relative** velocity (or acceleration) between those two points.
- Build the diagram **starting from the input link** and move link by link, writing for every new point one vector equation of the form $\mathbf V_B=\mathbf V_A+\mathbf V_{BA}$.
- **A vector equation gives two scalar unknowns** – two magnitudes, two directions, or one of each. Draw each known vector to scale; for the unknown ones draw only their **direction lines**; the polygon closes where the lines meet.

---

## 2. Vector equations to use

(Sec. 2.3.)

| Situation | Velocity | Acceleration |
|---|---|---|
| two points $A,B$ of one rigid link | $\mathbf V_B=\mathbf V_A+\mathbf V_{BA},\ \ V_{BA}=\omega\,AB,\ \perp AB$ in the sense of $\omega$ (2.16) | $\mathbf a_B=\mathbf a_A+\mathbf a^n_{BA}+\mathbf a^t_{BA}$ (2.17); $a^n_{BA}=\omega^2AB$ **along $BA$** (towards $A$); $a^t_{BA}=\alpha\,AB$, $\perp AB$ in the sense of $\alpha$ |
| a link guided on another: coincident points $P_i,P_j$ (path of $P_j$ on link $i$ known) | $\mathbf V_{P_j}=\mathbf V_{P_i}+\mathbf V_{P_j/i}$ (2.22) | $\mathbf a_{P_j}=\mathbf a_{P_i}+\mathbf a^n_{P_j/i}+\mathbf a^t_{P_j/i}+\mathbf a_c$ (2.23) |
| Coriolis term | – | $\mathbf a_c=2\,\boldsymbol\omega_i\times\mathbf V_{P_j/i}$ (2.24): direction = $\mathbf V_{P_j/i}$ turned $90^\circ$ in the sense of $\omega_i$; magnitude $2\omega_iV_{P_j/i}$ |
| relative normal acceleration on a curved path | – | $a^n_{P_j/i}=\big(V_{P_j/i}\big)^2/\rho$ towards the centre of curvature; $=0$ for a straight slot |

Particle on a path: $V=\rho\omega$ (2.13), $a_n=V^2/\rho=\rho\omega^2$ (2.14), $a_t=\rho\alpha+\dot\rho\omega$ (2.15). Rotating link: tangential component $\alpha r$ (⊥ to the radius), normal component $\omega^2r$ (towards the centre).

> [!warning] The common mistake
> $\mathbf a_{P_3/P_2}$ (difference of absolute accelerations of the coincident points) is **not** $\mathbf a_{P_3/2}$ (acceleration seen from link 2): $\mathbf a_{P_3}-\mathbf a_{P_2}=\mathbf a_{P_3/2}+\mathbf a_c$ (book, after Prob. 2.10). Always include the Coriolis vector when a point slides on a rotating link.

---

## 3. Velocity and acceleration images

(Sec. 2.6.) For a rigid link with points $B,C,D,E$ and angular velocity $\omega$, acceleration $\alpha$:

$$
\frac{eb}{EB}=\frac{bc}{BC}=\frac{ec}{EC}=\frac{bd}{BD}=\omega\qquad(\text{velocity image }bcde\ \text{similar to }BCDE,\ \text{turned }90^\circ\text{ in the sense of }\omega)
$$

$$
\frac{eb}{EB}=\frac{bc}{BC}=\dots=\sqrt{\omega^4+\alpha^2}\qquad(\text{acceleration image similar to the link, turned by }180^\circ-\varphi,\ \varphi=\tan^{-1}\tfrac{\alpha}{\omega^2})
$$

- The letters of an image run in the **same sequence** as on the link.
- The scale differs for every link (set by that link's $\omega$ resp. $\sqrt{\omega^4+\alpha^2}$).
- The absolute velocity (acceleration) of any point $X$ is the line from the pole $o$ to its image $x$.
- **Once two points of a link are known, every other point follows by the image** – this is what makes complex mechanisms workable.

![[VG-g2-fourbar-polygons-images.png]]

*Zero-acceleration point of a link (Prob. 2.12).* The pole $o$ **is** the image of the point of the link with zero acceleration; locate it by making the triangle $\;(\text{point})AB\;$ similar to $o\,a\,b$ (same letter order). It is **not** the instantaneous centre (zero velocity), which for the connecting rod of a slider-crank lies on $O_2A$ extended, at the intersection with the vertical through $B$.

---

## 4. Worked constructions

### 4.1 Slider-crank (Prob. 2.9)

![[VG-g1-slider-crank-polygons.png]]

Steps (crank 1000 rpm CW → $\omega_2=105$ rad/s, $\theta_2=45^\circ$, $O_2A=6$, $AB=16$ cm):

| Step | Equation | Draw |
|---|---|---|
| velocity of $A$ | $\mathbf V_A=\omega_2\times\overrightarrow{O_2A}$, $V_A=\omega_2O_2A$ | $o_2a$ ⊥ $O_2A$ in the sense of $\omega_2$ |
| velocity of $B$ | $\mathbf V_B=\mathbf V_A+\mathbf V_{BA}$ | from $a$ a line ⊥ $AB$; from $o_2$ a horizontal line; they meet at $b$ |
| rod rotation | $\omega_3=ab/AB$ | sense from $\mathbf V_{BA}$ |
| acceleration of $A$ | $a_A=\omega_2^2O_2A$ (⊥ part $=0$, $\alpha_2=0$) | $o_2a'$ towards $O_2$ |
| acceleration of $B$ | $\mathbf a_B=\mathbf a_A+\mathbf a^n_{BA}+\mathbf a^t_{BA}$, $a^n_{BA}=\omega_3^2AB$ | from $a'$ draw $\mathbf a^n_{BA}$ (towards $A$), then a line ⊥ $AB$; horizontal from $o_2$; they meet at $b'$ |
| rod angular acceleration | $\alpha_3=a^t_{BA}/AB$ | |

| Quantity | Book (graphical) | Exact (same construction, computed) |
|---|---|---|
| $V_A$ | 630 cm/s | 628.3 |
| $V_B$ | 574 → | **566.5** → |
| $\omega_3$ | 27.5 rad/s CCW | **28.8** CCW |
| $a_B$ | 46 000 cm/s² ← | **47 490** ← |
| $\alpha_3$ | 2845 rad/s² CCW | **2788** CCW |

(The book rounds $\omega_2$ to 105 and reads lengths off the drawing, hence the 1–5 % scatter.)

### 4.2 Four-bar with a coupler point

Same pattern with $\mathbf V_B\perp O_4B$: from $a$ draw ⊥ $AB$, from $o$ draw ⊥ $O_4B$, intersect → $b$; for the acceleration use **two** normal components ($\mathbf a^n_B$ from the pole, $\mathbf a^n_{BA}$ from $a'$) and two perpendicular lines. Any other point $C$ of the coupler then comes from the **image** $abc\sim ABC$ (previous section) – this was checked to machine precision against the analytic solution.

### 4.3 Slotted-lever with coincident points (Prob. 2.10)

![[VG-g3-slotted-lever-polygons.png]]

Coincident points $A_2$ (on crank 2), $A_3$ (the slider block, $\mathbf V_{A_3}=\mathbf V_{A_2}$ since they always coincide) and $A_4$ (on the lever):

| Level | Equation | What is known |
|---|---|---|
| velocity | $\mathbf V_{A_3}=\mathbf V_{A_4}+\mathbf V_{A_3/4}$ | $\mathbf V_{A_3}$ full; $\mathbf V_{A_4}\perp O_4A$; $\mathbf V_{A_3/4}\parallel$ slot → triangle $o_2a_4a_3$ gives $\omega_4=V_{A_4}/O_4A$ |
| acceleration | $\mathbf a_{A_3}=\mathbf a^n_{A_4}+\mathbf a^t_{A_4}+\mathbf a_{A_3/4}+\mathbf a_c$ | $\mathbf a_{A_3}$ full; $\mathbf a^n_{A_4}=\omega_4^2O_4A$; $\mathbf a_c=2\omega_4\times\mathbf V_{A_3/4}$; directions of $\mathbf a^t_{A_4}$ (⊥ lever) and $\mathbf a_{A_3/4}$ (∥ slot) → closes the polygon, gives $\alpha_4=a^t_{A_4}/O_4A$ |

Then $\mathbf V_B=\omega_4\times\overrightarrow{O_4B}$ and $\mathbf a_B=\mathbf a^n_{B}+\mathbf a^t_B$ from $\omega_4,\alpha_4$; for the ram $C$: $\mathbf V_C=\mathbf V_B+\mathbf V_{CB}$ ($\mathbf V_C$ horizontal) and $\mathbf a_C=\mathbf a_B+\mathbf a^n_{CB}+\mathbf a^t_{CB}$.

**Book results (Prob. 2.10):** $\omega_2=3.14$ rad/s; $\omega_4=0.603$ rad/s CCW, $V_{A_2/4}=27$ cm/s, $V_C=40$ cm/s ←, $\omega_5=0.667$ rad/s; $\alpha_4=0.897$ rad/s² CCW, $a_C=43.8$ cm/s² ←.
Remember: $\mathbf a_{A_3}-\mathbf a_{A_4}=\mathbf a_{A_3/4}+\mathbf a_c$, **not** $\mathbf a_{A_3/4}$ alone.

### 4.4 RPRP linkage (Prob. 2.11)

![[VG-g4-rprp.png]]

$\omega_2=2$ rad/s CCW, $\alpha_2=4$ rad/s² CW, $O_2P_2=5$ cm; $P_3\equiv P_4$ moves along a straight path (vertical) in link 2 and slider 4 is horizontal.

- Velocity: $\mathbf V_{P_4}=\mathbf V_{P_2}+\mathbf V_{P_4/2}$, with $V_{P_2}=\omega_2O_2P_2=10$ ↑, both right-hand vectors **vertical** and $\mathbf V_{P_4}$ **horizontal** ⇒ $V_{P_4}=0$, $V_{P_4/2}=10$ ↓ (slider momentarily at rest).
- Acceleration: $\mathbf a_{P_4}=\mathbf a^n_{P_2}+\mathbf a^t_{P_2}+\mathbf a_c+\mathbf a_{P_4/2}$ with $a^n_{P_2}=\omega_2^2\,O_2P_2=20$ (towards $O_2$), $a^t_{P_2}=\alpha_2O_2P_2=20$ ↓, $a_c=2\omega_2V_{P_4/2}=40$ →, $a^n_{P_4/2}=0$ (straight path) ⇒ $a_{P_4}=20$ cm/s² → (horizontal balance), $a_{P_4/2}=20$ ↑ (vertical balance).

### 4.5 Curved slot (Prob. 2.13, Geneva mechanism)

Pin $P_2$ on the driver, curved slot in the output member 3 with radius of curvature $\rho$ centred at $C$:

$$
\mathbf V_{P_3}=\mathbf V_{P_2}+\mathbf V_{P_3/2}\ (\text{or, with roles swapped, }\mathbf V_{P_2}=\mathbf V_{P_3}+\mathbf V_{P_2/3})
$$

$$
\mathbf a_{P_2}=\mathbf a^n_{P_3}+\mathbf a^t_{P_3}+\mathbf a^n_{P_2/3}+\mathbf a^t_{P_2/3}+2\boldsymbol\omega_3\times\mathbf V_{P_2/3},\qquad a^n_{P_2/3}=\frac{V_{P_2/3}^2}{\rho}\ \text{(towards the centre of curvature }C\text{)}
$$

Book numbers: $O_2P_2=1.6$, $O_3P_3=1.8$, $\rho=2.8$ cm, $\omega_2=30$ rad/s (CW, constant): $V_{P_2}=48$ cm/s, $V_{P_3}=8$ cm/s ⇒ $\omega_3=4.44$ rad/s CCW, $V_{P_2/3}=47.8$; $a^n_{P_2}=1440$, $a^n_{P_3}=35.55$, Coriolis $426.24$, $a^n_{P_2/3}=822.86$ cm/s² ⇒ $a^t_{P_3}=1020$ cm/s², $\alpha_3=566.7$ rad/s² CCW. Only **two** unknown magnitudes remain at the acceleration stage, so the polygon closes.

---

## 5. Instantaneous centres

(Secs. 2.4–2.7; for velocity only.)

| Fact | Statement |
|---|---|
| number of centres | $N(N-1)/2$ for $N$ links |
| definition | $P_{ij}$: point with the same absolute velocity on links $i$ and $j$; $V_A/PA=V_B/PB=\omega$ |
| by inspection | hinge → the hinge; pure sliding → at infinity ⊥ to the sliding direction; rolling → point of contact; sliding on a curved element → its centre of curvature; rolling + sliding → on the common normal |
| Aronhold–Kennedy | for any three links $i,j,k$ the centres $P_{ij},P_{jk},P_{ik}$ are **collinear** |
| velocity of a point | $V_C=PC\cdot V_B/PB$, ⊥ $PC$; for a 4R, $V_{P_{24}}=\omega_2\,O_2P_{24}=\omega_4\,O_4P_{24}$ |

**Finding $P_{24}$, $P_{13}$ for a four-bar (Prob. 2.7):** $P_{13}=P_{14}P_{34}\cap P_{12}P_{23}$; $P_{24}=P_{12}P_{14}\cap P_{23}P_{34}$. For points of link 4 use an **auxiliary point** $F'$ on the line from $P_{14}$ through $P_{24}$ with $O_4F'=O_4F$ ($V_F=V_{F'}$), and the similar triangles $V_F/V_{P_{24}}=O_4F/O_4P_{24}$.

**Circle diagram (Prob. 2.8, Whitworth, 6 links, 15 centres).** Put the links on a circle, draw a chord for every centre found by inspection; a missing chord that is the **common side of two triangles whose other sides are known** is found by Aronhold–Kennedy.

![[VG-g5-circle-diagram.png]]

Order used in Prob. 2.8: $P_{24}$ (triangles 234, 124), $P_{15}$ (145, 165), $P_{25}$ (125, 245), then $P_{26}$ (126, 256). Velocity of the slider $D$ on link 6: $V_{P_{26}}=\omega_2\,O_2P_{26}$ (horizontal) and, since link 6 translates, $V_D=V_{P_{26}}$.

> [!note] Limits
> Not every mechanism's centres can be found geometrically: constrained linkages like Fig. 2.20a, or any mechanism with more than one input (Fig. 2.20b). Instantaneous centres of **acceleration** are of little use and are not used.

---

## 6. Complex mechanisms

Motion-transfer points = the points through which a link transmits motion to its neighbours.

| Kind | Meaning | Method |
|---|---|---|
| simple | radius of path curvature known for the transfer points of every link | direct polygons (§4) |
| complex, **low** degree | simple if another link is chosen as input (Fig. 2.26a); ≥ 2 transfer points of the floating link have known curvature | normal accelerations, auxiliary points, Goodman |
| complex, **high** degree | no input choice makes it simple (Fig. 2.26b) | auxiliary points (+ normal components), Goodman with an inversion |

(The Euler–Savary equation, an alternative, is not covered in the book.)

### 6.1 Method of normal accelerations (low complexity)

Key fact: the component of acceleration of a point $P$ **perpendicular to its velocity** is independent of the link's $\alpha$: $\;a^n_P=V_P^2/\rho_P$.

1. Change the input link to make the mechanism simple.
2. Draw the velocity polygon (any scale), fix the scale from the true input velocity ⇒ true velocities.
3. Draw an **auxiliary acceleration diagram**: alternative input link with $\alpha=0$, true velocities ⇒ normal components of the floating point.
4. Draw the true acceleration diagram with the real input, using those normal components.

*Prob. 2.14:* $\omega_2=10$ rad/s CW constant. With link 6 as input: $V_D=140$ cm/s, $\omega_6=28$, $\omega_3=25.8$, $\omega_4=18.66$ (CW), $\omega_5=14.9$ rad/s; $\alpha_6=320$ rad/s² CW.

### 6.2 Auxiliary-point method (works for most high-complexity mechanisms)

On the ternary floating link (e.g. $BCD$) draw **auxiliary lines I, II, III through $B,C,D$ along the connecting links**; their intersections $X,Y,Z$ are auxiliary points. Along an auxiliary line the velocity (acceleration) component of a point of the link is known, because the connecting link there rotates about a known point (or is a slider). Two auxiliary points are enough.

- Velocity: the component of $\mathbf V_X$ along each auxiliary line is known (a point of the floating link on line I has only the component of $\mathbf V_{A}$ plus relative terms ⊥ to that line, which vanish along it). So $x$ lies on the line through $a$ ⊥ line I **and** on the line through $o$ ⊥ line II; the second auxiliary point is found the same way (in Prob. 2.15 it falls at the pole). Then $b,c,d$ come from the **image** of the link.
- Acceleration: for each auxiliary line the component of $\mathbf a_X$ along it is the known normal part of the connecting link, so $x$ lies on the line through $x'$ ⊥ the line; two auxiliary points ⇒ $x$ and $y$; the images give $b,c,d$ and $\alpha_6$.
- Floating link with a **prismatic** pair: pick the auxiliary directions through the sliding block, and use $\mathbf a_{E/D}=-\mathbf a_c=-2\boldsymbol\omega_f\times\mathbf V_{D/f}$ (Fig. 2.29).
- Two **connected ternary links** (Fig. 2.30): two steps with six auxiliary directions.
- For high complexity with link 2 as input, the same procedure with auxiliary points on link 5 (Fig. 2.31); with link 6 as input, draw $\mathbf V_A,\mathbf V_B$ in proportion to $O_2A:O_2B$ and use normal components.

*Prob. 2.15* (same data as 2.14): $\mathbf V_Y=0$ (so $y$ is at the pole) and $x$ from two perpendiculars; $\omega_3=25.8$ rad/s CCW; $\alpha_6=320$ rad/s² CW.

### 6.3 Goodman's indirect method

Two properties: (i) $\omega_l$ and $\alpha_l$ are **linear** in the input quantities; (ii) relative angular velocities/accelerations between links are unchanged by kinematic inversion.

$$
\omega_l=C_l\,\omega_i,\ \ C_l=\frac{d\theta_l}{d\theta_i}\qquad(2.25)
$$

$$
\alpha_l=C_l\alpha_i+\omega_i^2\frac{dC_l}{d\theta_i}\ \Rightarrow\ \alpha_l=\alpha_l'+\frac{\omega_l}{\omega_i}\,\alpha_i\qquad(2.26,\ 2.27)
$$

$\alpha_l'$ = acceleration of link $l$ from the **auxiliary diagram** (true velocities, zero input acceleration). For a sliding input link (input velocity $V_i$, acceleration $a_i$): $\alpha_l=\alpha_l'+\dfrac{\omega_l}{V_i}\,a_i$ (2.28). For the tangential acceleration of a point $S$ of a link: $\;a_S^t=a_S'^{\,t}+\dfrac{V_S}{\omega_i}\,\alpha_i$ (rotating input) or $a_S'^{\,t}+\dfrac{V_S}{V_i}\,a_i$ (sliding input) (2.29–2.32; the normal component is the same in both diagrams).

In a kinematic inversion with frame $f$ (not necessarily the actual frame), with $i$ the alternative input link whose acceleration is zero in the auxiliary diagram:

$$
\alpha_{lf}=\alpha_{lf}'+\frac{\omega_{lf}}{\omega_{if}}\,\alpha_{if}\qquad(2.27a)
$$

(and the analogue (2.28a) for a sliding input). Relative rotations between two links are unchanged by the inversion, e.g. $\omega_{21}=\omega_{24}-\omega_{14}$.

Sign: rotations CCW positive; tangential acceleration components positive when in the sense of the corresponding velocity.

**Low complexity:** choose an alternative input, do the auxiliary analysis with its $\alpha=0$, then correct with (2.27)–(2.32).
**High complexity:** make a **kinematic inversion** so the mechanism becomes simple; relative rotations $\omega_{lf}=\omega_{l4}-\omega_{f4}$ etc.

> [!example] Prob. 2.16 (= 2.14 by Goodman)
> Alternative input = link 6, auxiliary diagram with $\alpha_6=0$. The tangential acceleration of $A$ in it is $a_A'^{\,t}=850$ cm/s² (positive, in the direction of $V_A$). The real input has $\alpha_2=0$ (so $a_A^t=0$), and by the point relation (2.29): $0=a_A'^{\,t}+\dfrac{V_A}{\omega_6}\,\alpha_6$ ⇒ $\alpha_6=-850\,\dfrac{\omega_6}{V_A}=-318$ rad/s², i.e. $318$ rad/s² CW (book).

> [!example] Probs. 2.17–2.18 (inversion with link 4 fixed, input 2 or 6)
> Velocity diagram with an arbitrary scale $K_v$: $\omega_{24}=0.846K_v,\ \omega_{14}=0.231K_v,\ \omega_{64}=0.482K_v,\ \omega_{34}=0.805K_v,\ \omega_{54}=0.533K_v$. Prob. 2.17 ($\omega_{21}=\omega_{24}-\omega_{14}=1$): $K_v=1.627$, $\omega_{24}=1.378,\ \omega_{14}=0.376,\ \omega_{64}=0.783$ rad/s; $\omega_6=\omega_{61}=\omega_{64}-\omega_{14}=0.407$ rad/s. Auxiliary accelerations $\alpha_{14}'=1.176,\ \alpha_{64}'=3.38$; with $\alpha_{21}=\alpha_{24}-\alpha_{14}=0$: $\alpha_{24}=1.176/(1-\omega_{14}/\omega_{24})=1.619$ rad/s², $\alpha_{14}=\alpha_{14}'+\tfrac{\omega_{14}}{\omega_{24}}\alpha_{24}=1.618$, $\alpha_{64}=4.30$, $\alpha_6=\alpha_{64}-\alpha_{14}=2.682$ rad/s² CCW.
> Prob. 2.18 (given $\omega_6=0.5$ CW, $\alpha_6=1.5$): $K_v=1.99$, $\omega_2=1.224$ rad/s CCW; $\alpha_{24}=-5$, $\alpha_2=\alpha_{21}=-5.72$ rad/s², i.e. $5.72$ rad/s² CW. (All arithmetic reproduced in the checks.)

---

## 7. Rules, scales and signs

| Item | Rule |
|---|---|
| scale | choose a velocity scale $K_v$ (cm/s per cm) and acceleration scale $K_a$ independently; with a different input speed the velocity polygon is **similar** (property of Goodman's method) |
| image scale | velocity image: $\omega$; acceleration image: $\sqrt{\omega^4+\alpha^2}$ |
| acceleration polygon closure | the number of unknown scalars per vector equation must be 2 |
| two polygons | build the **velocity polygon first**: the acceleration normal components need $\omega$ from it |
| signs | CCW positive; $\mathbf V_{BA}$ direction = $\overrightarrow{AB}$ turned $90^\circ$ in the sense of $\omega$; $\mathbf a^t$ likewise with $\alpha$; $\mathbf a^n$ towards the centre |
| input choice | any link may be the input in a simple inversion, but only the **true** input motion gives true values (rescale otherwise) |

---

## 8. Checks and tools

Constructions are done in `va_poly.py` as **direction-line intersections** (the graphical way, not by formulas), then compared:

| Check | Result |
|---|---|
| slider-crank polygons vs analytic $\dot s,\ddot s$ | identical (to $10^{-6}$) |
| four-bar polygon $\omega_3,\omega_4,\alpha_3,\alpha_4$ vs analytic, both assembly modes | identical |
| velocity and acceleration images $abc\sim ABC$ (ratio, rotation difference $=$ constant) | ✓ |
| slotted lever polygon with Coriolis vs analytic $\omega_4,\alpha_4$ | ✓ (three poses) |
| Prob. 2.11 numbers ($a_c=40$, $a_{P_4}=20$, $a_{P_4/2}=20$) | exact |
| Probs. 2.17–2.18 Goodman arithmetic | reproduced |
| Prob. 2.9 vs the book's graphical values | 1–5 % apart (§4.1) |

**Interactive:** [va-polygons.html](va-polygons.html) – mechanism, velocity polygon and acceleration polygon side by side for the four-bar, the slider-crank and the slotted lever; sliders for dimensions, $\theta_2,\omega_2,\alpha_2$; animate. Right-click → *Open in default app*.
**Regenerate figures:** `python va_polyviz.py` (checks first). Figures: `assets/VG-g1…g5`.

---

## 9. Notes on the book

> [!warning]
> 1. **Prob. 2.9** — the book's graphical readings differ from the exact values by 1–5 % (table in §4.1); the construction itself is exact.
> 2. **Auxiliary-point velocity step:** the text layer garbles the bookkeeping of the "$V_{X/D}$ components vanish" argument; the version in §6.2 restates it as the principle (a point on a connecting link has a **known component** along the link, because that link's other end is fixed or slides).
> 3. **(2.27a)/(2.28a):** the printed layout is damaged; the forms written in §6.3 follow the logic of the derivation (acceleration of link $l$ = auxiliary value + $(\omega_l/\omega_i)\times$ the true input acceleration), and the Prob. 2.17–2.18 arithmetic confirms them.
> 4. **Prob. 2.10/2.13 angle data** come from figures not recoverable from the text; the constructions are illustrated with equivalent data, and only the book's *printed* results are quoted.


## Cross-domain links

- [[Cross-Domain Synthesis/Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics|Rotating Vectors]] — a velocity polygon is a phasor diagram with a different ω on every side. Map: [[KDoMs/KDoMs - MOC|KDoMs MOC]].

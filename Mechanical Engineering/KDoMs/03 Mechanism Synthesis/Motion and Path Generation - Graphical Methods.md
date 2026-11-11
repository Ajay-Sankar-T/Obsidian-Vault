---
title: Motion and Path Generation – Graphical Methods
course: ME 2201 Kinematics & Dynamics of Machinery
tags:
  - KDoM
  - formula-bank
  - synthesis
  - motion-generation
  - path-generation
  - graphical
source: "[[Ghosh and Mallik.pdf]]"
pages: "PDF p. 128–170 (book pp. 119–161), Chapter 3, Sections 3.1–3.4, 3.6–3.7"
aliases:
  - Graphical synthesis formula bank
  - Motion generation graphical
---

# Motion and Path Generation – Graphical Methods

Source: [[Ghosh and Mallik.pdf]], Ch. 3 *Dimensional Synthesis of Linkages* · Companion: [[Motion and Path Generation - Analytical Methods]] · Gears: [[Gear Formula Bank]]
Equation numbers in brackets are the book's. Constructions have no equation numbers in the book, so the relations used are written out here.

> [!abstract] Contents
> [[#1. Problem types and vocabulary]] · [[#2. Kinematic inversion]] · [[#3. Motion generation (three positions)]] · [[#4. Path generation (three positions)]] · [[#5. Function generation by inversion (context)]] · [[#6. Poles and relative poles]] · [[#7. Synthesis with relative poles]] · [[#8. Four positions: point-position reduction]] · [[#9. Straight-line mechanisms]] · [[#10. Branch and order defects]] · [[#11. Worked problems]] · [[#12. Checks and tools]]

> [!tip] Which construction?
> | Given | Unknown | Use |
> |---|---|---|
> | 3 coupler **positions** (body guidance) | both ground pivots | circle centres, [[#3. Motion generation (three positions)]] |
> | 3 coupler positions + both ground pivots | the two moving hinges $A,B$ on the coupler | inversion, [[#3. Motion generation (three positions)]] |
> | 3 **points** $C_1,C_2,C_3$ of a coupler point | the whole 4R | choose $O_2,O_4,B_1$, invert, [[#4. Path generation (three positions)]] |
> | 4 points of a coupler point | the 4R | put $O_2$ at pole $P_{13}$, [[#8. Four positions: point-position reduction]] |
> | a straight line | exact / approximate linkage | [[#9. Straight-line mechanisms]] |

---

## 1. Problem types and vocabulary

| Type | What is prescribed | Coordinated with input? |
|---|---|---|
| **Motion generation** | positions of a rigid body (the coupler) | may or may not |
| **Path generation** | a path for a point $C$ on the floating link | may or may not |
| Function generation | input–output relation (displacement, velocity, acceleration) | by definition |
| Dead-centre problems | prescribed dead-centre configuration | – |

- **Approximate synthesis:** generated motion/path agrees with the prescribed one only at a finite number of **precision (accuracy) points**. **Exact synthesis:** agreement everywhere, possible only for a few "nice" functions.
- Number of precision points = number of free design parameters. For the 4R function generator the coupler length ratios give 3 ($l_1/l_2,\ l_1/l_3,\ l_1/l_4$-type) plus $\theta_2^i,\theta_4^i,r_x,r_y$; the book notes at most five coordinated pairs can be handled by the linkage parameters alone.
- With $N$ precision points there are $N-1$ prescribed displacements.
- **Structural error** $E=f-F$: inherent in approximate synthesis. **Mechanical error:** clearances and length inaccuracy.

---

## 2. Kinematic inversion

Hold the coupler fixed in position $I$ and let the frame move. Because $O_2A$ and $O_4B$ have constant length, the inverted ground pivots lie on circles about $A$ and $B$.

| Symbol | Meaning |
|---|---|
| $O_{2,k}^{1}$ | position of $O_2$ seen from the coupler held in position **1**, taken from position $k$ (superscript = inversion position, second subscript = inverted position) |
| $O_{2,1}^{1}=O_2$ | by definition |

**Procedure (tracing paper or compass).** Mark the coupler body axes $\xi\eta$ and $O_2,O_4$ in position $k$ on tracing paper; lay the paper on position 1 with axes coinciding; the marked points are $O_{2,k}^1,O_{4,k}^1$.

$$
\boxed{A_1=\text{centre of the circle through }O_{2,1}^1,\ O_{2,2}^1,\ O_{2,3}^1,\qquad B_1=\text{centre through }O_{4,1}^1,\ O_{4,2}^1,\ O_{4,3}^1}
$$

In coordinates: body position of the pivot $=R(-\varphi_k)(O-t_k)$, inverted point $=R(\varphi_1)\,[\ldots]+t_1$ for coupler pose $(t_k,\varphi_k)$ (used in `synth_core.inverted_positions`).

---

## 3. Motion generation (three positions)

![[SFB-g1-motion-free.png]]

**Pivots free.** Pick two points $A,B$ on the body. Their three positions $A_1A_2A_3$ and $B_1B_2B_3$ (non-collinear) are on circles:

$$
O_2=\text{centre of circle}(A_1,A_2,A_3),\qquad O_4=\text{centre of circle}(B_1,B_2,B_3)
$$

The 4R is $O_2A_1B_1O_4$ (coupler $A_1B_1$). The choice of $A,B$ is free (infinitely many solutions).

**Pivots prescribed** (position $O_2,O_4$ fixed in space): use [[#2. Kinematic inversion]].

![[SFB-g2-motion-pivots.png]]

> [!warning] Check the result
> If the linkage is Grashof, one assembly mode may not reach all three positions → see [[#10. Branch and order defects]].

---

## 4. Path generation (three positions)

![[SFB-g3-path-inversion.png]]

Three points $C_1,C_2,C_3$ of the coupler point are prescribed. The path problem has more freedom than the motion problem, so some parameters are **chosen**:

1. Choose $O_2,\ O_4$ and $B_1$ (so link lengths $O_4B=r_B$ and $BC=\overline{B_1C_1}$ are fixed).
2. $B_2,B_3$: intersect the circle $(O_4,r_B)$ with the circles $(C_2,BC)$ and $(C_3,BC)$.
3. Coupler poses follow from $B_kC_k$. Invert with the coupler fixed at position 1 to get $O_{2,2}^1,O_{2,3}^1$.
4. $A_1$ = centre of the circle through $O_2,\ O_{2,2}^1,\ O_{2,3}^1$.

Result: 4R $O_2A_1B_1O_4$ with coupler point $C_1$ passing through $C_1,C_2,C_3$. Repeating with $A_1$ chosen and $B_1$ unknown gives a second family.

Constraint checks used by the code: $|O_2A_k|$ and $|O_4B_k|$ constant for $k=1,2,3$.

---

## 5. Function generation by inversion (context)

For $(\theta_2^{12},\theta_4^{12})$ and $(\theta_2^{13},\theta_4^{13})$ with $\theta_j^{1k}=\theta_j^k-\theta_j^1$ ($j=2$ input, $j=4$ output): assume $O_2,O_4,A_1$; locate $A_2,A_3$ by rotating about $O_2$; hold the **follower** fixed; inverted $A_2$ is $A_2$ rotated about $O_4$ by $-\theta_4^{12}$, inverted $A_3$ by $-\theta_4^{13}$; $B_1$ = centre of the circle through $A_1,A_2^{1},A_3^{1}$.

*Prob. 3.2 (slotted cutter):* a $B$ at infinity gives the slot axis through $A_1$ and $A_2^1$; offset $e=60$ mm for $\theta_2=40^\circ,\ \theta_4=20^\circ$.

---

## 6. Poles and relative poles

![[SFB-g4-poles.png]]

**Pole $P_{12}$ of a coupler displacement** $A_1B_1\to A_2B_2$: intersection of the perpendicular bisectors of $A_1A_2$ and $B_1B_2$; it is the centre of the equivalent finite rotation, and depends only on the two positions.

$$
\angle A_1P_{12}A_2=\angle B_1P_{12}B_2=\theta_3^{12},\qquad \angle A_1P_{12}N_1=\angle B_1P_{12}N_2=\tfrac12\theta_3^{12}
$$

($N_1,N_2$ = midpoints.) For small rotation $P_{12}$ is the instantaneous centre. The frame $O_2O_4$ and the coupler $A_1B_1$ (in both positions) subtend **equal angles, or angles differing by $180^\circ$** at the pole; so do crank and follower. Measure from $A$ to $O_2$ and from $B$ to $O_4$ (not reversed) and take $O_2O_4$ in the same sense as $AB$.

**Relative pole $R_{12}$** (centre of the equivalent rotation when the crank is the frame): intersection of the lines

$$
N_1:\ \text{through }O_2\text{ at }-\tfrac12\theta_2^{12}\text{ to }O_2O_4,\qquad
N_2:\ \text{through }O_4\text{ at }-\tfrac12\theta_4^{12}\text{ to }O_4O_2
$$

> [!check] Verified numerically
> For a 4R with $\theta_2^{12}=40.1^\circ,\ \theta_4^{12}=14.7^\circ$: $N_1,N_2$ at $-20.1^\circ,-7.4^\circ$; **$O_2A_1$ and $O_4B_1$ subtend the same angle at $R_{12}$ (24.7°) and $O_2O_4$ and $A_1B_1$ subtend the same angle (12.7°)** – both equalities hold to machine precision.

**Slider-crank** ($O_4$ at infinity ⟂ to the slider line, slider displacement $s_{12}$):
$N_1$ through $O_2$ at $-\tfrac12\theta_2^{12}$ to $O_2O_4$; $N_2$ at distance $-\tfrac12 s_{12}$ from $O_2$, ⟂ to the slider line; $R_{12}=N_1\cap N_2$. The frame and the connecting rod subtend equal angles at $R_{12}$.

Mirror property: $R_{21}$ is the mirror image of $R_{12}$ in $O_2O_4$.

---

## 7. Synthesis with relative poles

**One coordinated pair $(\theta_2^{12},\theta_4^{12})$.** Choose $O_2O_4$; construct $R_{12}$; choose $A$ anywhere; then $B$ lies on the line $R_{12}Z$ with $\angle O_2R_{12}O_4=\angle A R_{12}Z$.

**Two pairs** $(\theta_2^{12},\theta_4^{12}),\ (\theta_2^{13},\theta_4^{13})$: construct $R_{12},R_{13}$. Choose $O_2A_1$. $B_1$ is the intersection of the lines $R_{12}Y,\ R_{13}Z$ with

$$
\angle O_2R_{12}A_1=\angle O_4R_{12}Y,\qquad \angle O_2R_{13}A_1=\angle O_4R_{13}Z
$$

For the second configuration use $R_{21},R_{23}$ instead.

**Slider-crank, two pairs** $(\theta_2^{12},s_{12}),(\theta_2^{13},s_{13})$: draw $O_2X$ along the slider line, $O_2Y\perp O_2X$; locate $R_{12},R_{13}$; choose $O_2A_1$; draw $R_{12}P$, $R_{13}Q$ with $\angle O_2R_{12}O_4=\angle A_1R_{12}P$ and $\angle O_2R_{13}O_4=\angle A_1R_{13}Q$; $B_1=R_{12}P\cap R_{13}Q$ gives rod length and **offset**.

---

## 8. Four positions: point-position reduction

![[SFB-g5-point-position-reduction.png]]

Four positions need more than the three-position construction gives; one restricted solution is to **make two inverted positions coincide**:

- *Function generation:* choose $A_1=R_{12}$; then $A_2^{1}\equiv A_1$ and $B_1$ = centre of the circle through $A_1,\ A_3^1,\ A_4^1$. (Link 2 then crosses $O_2O_4$: it cannot be the rocker of a crank-rocker.)
- *Path generation* (coupler point through $C_1,\dots,C_4$): choose $O_4$ and $B_1$, find $B_2,B_3,B_4$ on the circle $(O_4,|O_4B|)$ with $|BC|$ constant; place

$$
O_2=P_{13}\ \ (\text{mid-normals of }B_1B_3\text{ and }C_1C_3)\ \Rightarrow\ O^1_{2,1}\equiv O^1_{2,3}
$$

$A_1$ = centre of the circle through $O_{2,1}^1,\ O_{2,2}^1,\ O_{2,4}^1$. Check: $|O_2A_k|$ constant for all four positions (done to $10^{-15}$ in the code).

Also available: Hrones & Nelson's **atlas of 7300 four-bar coupler curves** (with rate of traverse) for complicated paths.

---

## 9. Straight-line mechanisms

![[SFB-g6-straight-line.png]]

**Inversion principle.** If $P,Q,O$ are always collinear with $OP\cdot OQ=\text{const}$ and $P$ moves on a circle through $O$ (diameter $OR$), then $Q$ moves on a straight line ⟂ $OR$ (similar triangles $OPR,OQX$: $OX=OP\cdot OQ/OR$).

**Peaucellier** (8 links): rhombus $APBQ$, $OA=OB$:

$$
OP\cdot OQ=(OC-PC)(OC+CQ)=OC^2-PC^2=OA^2-AP^2=\text{const}
$$

**Approximate (four-bar coupler point):** the coupler curve is a sixth-order curve.

| Linkage | Dimensions | Coupler point |
|---|---|---|
| Watt | $O_2A=O_4B,\ AC=BC$; $O_2O_4:O_2A:AB=10.77:5:4$ | mid-point of $AB$ |
| Evans | $AB=O_4B=BC$; $O_2A:AB:O_2O_4=2:2.5:5.39$ | $C$ on $AB$ extended, $BC=AB$ |
| Roberts | $O_2O_4=2AB$; $O_2A=AC=BC=O_4B$ | apex $C$ of isosceles $ABC$ |
| Chebyshev | $AB:O_2O_4:O_2A:O_4B=1:2:2.5:2.5$ | mid-point of $AB$ |

(The figure draws all four from these ratios; orange is the other assembly mode.) The fork lift of Prob. 3.4 uses an approximate straight line.

---

## 10. Branch and order defects

| Defect | Meaning | Remedy |
|---|---|---|
| **Branch** | designed 4R is Grashof and the accuracy points need *both* assembly modes | reassembling is impractical → redesign |
| **Order** | accuracy points are met, but not in the prescribed sequence (e.g. 1,2,4,3) or the links move in the wrong sense | check output–input characteristics; with 3 points the order is always achievable with the right input direction |

Always test a cardboard model (drawing-pin hinges). Also keep the transmission angle $\mu_{\min}>30^\circ$ (Prob. 3.4).

---

## 11. Worked problems

| Prob. | Task | Result in the book |
|---|---|---|
| 3.1 | folding classroom desk, 3 positions, pivots $O_2,O_4$ given | $l_3=AB=6$ cm, $l_4=O_4B=25.02$ cm |
| 3.3 | overhead garage door (six-link), $\theta_4^{12}=12^\circ,\ \theta_4^{13}=26^\circ$ CW | $O_4B=72$, $AB=60$, $BD=38$, $CD=84$ cm, $\angle DCE=4^\circ$ |
| 3.4 | fork lift: vertical motion ∝ input rotation, 3 accuracy points | steps: (1) imaginary slider-crank with $\Delta\theta_2=60^\circ$ for $\Delta s=1.5$ m; (2) replace slider by link $O_4C$; (3) add link 5 to keep the fork horizontal |

*Prob. 3.4 step 1 numbers:* Chebyshev points for 1.5 m travel give $s_{12}=0.65$ m, $s_{13}=1.3$ m, and the proportionality $\dfrac{\theta_2^{12}}{\Delta\theta_2}=\dfrac{s_{12}}{\Delta s}$ gives $\theta_2^{12}=26^\circ,\ \theta_2^{13}=52^\circ$.

*Exercises 3.8–3.16 in the book* (tipper dumper, level-luffing crane, bus door, etc.) use these same constructions.

---

## 12. Checks and tools

![[SFB-g2-motion-pivots.png]]

Every construction here is also computed numerically in [[synth_core.py]] (circle through three points, inversion, circle–circle intersection for $B_k$, poles, relative poles, four-bar kinematics) and re-verified when figures are regenerated:

- motion generation: circle-centre pivots reproduce $|O_2A_k|,|O_4B_k|$ constant, and the inversion with those pivots returns the same $A_1,B_1$;
- path generation: $|O_2A_k|$ and $|O_4B_k|$ constant for the 3 and the 4-point cases;
- pole: $\angle A_1P_{12}A_2=\angle B_1P_{12}B_2=\theta_{12}$;
- Peaucellier: $Q$ stays on $x=(OA^2-AP^2)/(2r)$.

An **interactive** version (drag numbers, see the linkage and the coupler curve): [synthesis-explorer.html](synthesis-explorer.html) – right-click → *Open in default app*. Regenerate figures: `python synth_viz.py`.

## See also
- [[Tutorial-6-solution]] — Burmester points and four-position synthesis worked in the tutorial.

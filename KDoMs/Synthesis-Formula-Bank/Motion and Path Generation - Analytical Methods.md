---
title: Motion and Path Generation – Analytical Methods
course: ME 2201 Kinematics & Dynamics of Machinery
tags:
  - KDoM
  - formula-bank
  - synthesis
  - motion-generation
  - path-generation
  - analytical
source: "[[Ghosh and Mallik.pdf]]"
pages: "PDF p. 129–131 (Sec. 3.1) and 156–167 (Sec. 3.5–3.6), book pp. 120–158"
aliases:
  - Analytical synthesis formula bank
  - Dyad method
  - Freudenstein equation
---

# Motion and Path Generation – Analytical Methods

Source: [[Ghosh and Mallik.pdf]], Ch. 3 · Companion: [[Motion and Path Generation - Graphical Methods]]
Equation numbers in brackets are the book's. The **dyad method (3.18–3.21) is the book's analytical route for motion *and* path generation**; Freudenstein's equation and the slider-crank relations are its analytical function generators, included here because the same accuracy-point machinery (spacing, counting of parameters, linear solves) applies.

> [!abstract] Contents
> [[#1. Accuracy points and Chebyshev spacing]] · [[#2. Counting parameters]] · [[#3. Dyad (standard-form) method]] · [[#4. Path generation by dyads]] · [[#5. Motion generation by dyads]] · [[#6. Function generation by dyads]] · [[#7. Freudenstein four-bar function generator]] · [[#8. Slider-crank function generator]] · [[#9. Instantaneous conditions]] · [[#10. Cookbook for the coordinates]] · [[#11. Benchmarks]] · [[#12. Notes on the book's numbers]]

> [!tip] Which tool?
> | Goal | Section |
> |---|---|
> | place accuracy points in an interval | [[#1. Accuracy points and Chebyshev spacing]] |
> | coupler point through $n$ points, motion of a body | [[#3. Dyad (standard-form) method]]–[[#5. Motion generation by dyads]] |
> | $y=f(x)$ with a 4R | [[#7. Freudenstein four-bar function generator]] |
> | slider position ∝ crank rotation | [[#8. Slider-crank function generator]] |
> | velocities/accelerations specified at a pose | [[#9. Instantaneous conditions]] |

---

## 1. Accuracy points and Chebyshev spacing

![[SFB-a1-chebyshev-freudenstein.png]]

Generated function $F(x,R_1,\dots,R_k)$ with $k$ design parameters vs. desired $f(x)$ on $x^i\le x\le x^f$:

$$
E(x)=f(x)-F(x,R_1,\dots,R_k)\qquad(3.3)
$$

$E$ is zero only at the $k$ accuracy (precision) points. For a polynomial $f$ of order $k$ and $F$ of order $k-1$, **Chebyshev spacing** minimises $E$ between adjacent points; for other forms it is the first approximation (Taylor-expand, keep $x^k$ in $f$ and $x^{k-1}$ in $F$):

$$
x_l=a+h\cos\frac{(2l-1)\pi}{2k},\quad l=1,\dots,k,\qquad a=\frac{x^i+x^f}{2},\ \ h=\frac{x^f-x^i}{2}\qquad(3.4)
$$

**Geometric method:** circle of centre $a$ and radius $h$ on the $x$-axis; inscribe a regular polygon of $2k$ sides with two sides ⟂ the axis; project the vertices on the axis.

| $k$ | points on $[1,10]$ |
|---|---|
| 3 | $x=9.40,\ 5.50,\ 1.60$ |
| 4 | $x=9.66,\ 7.22,\ 3.78,\ 1.34$ |

Scale factors (function generation, linear input/output mappings):

$$
\frac{\theta_2-\theta_2^i}{x-x^i}=\frac{\Delta\theta_2}{x^f-x^i}=r_x,\qquad \frac{\theta_4-\theta_4^i}{y-y^i}=\frac{\Delta\theta_4}{y^f-y^i}=r_y\qquad(3.1,\ 3.2)
$$

Only the **ratios** of link lengths matter for the coordination of $\Delta\theta_4$ with $\Delta\theta_2$.

---

## 2. Counting parameters

| Method | Unknown scalars | Equations from $n$ accuracy points |
|---|---|---|
| 4R function generator | $l_1/l_2,\ l_1/l_4,\ K_3$ (three ratios) | 3 at $n=3$ (linear in $K_1,K_2,K_3$) |
| dyad standard form (3.18) | 2 per complex unknown | $2(n-1)$ scalar |

For the dyad (left) side with $n$ positions: $2(n-1)$ scalar equations; unknowns are $L,L^*$ (4 scalars) plus the rotations $\theta_2^j,\theta_3^j$ left unprescribed.
- $n=3$: 4 equations → $L,L^*$ solved **linearly** if $\theta_2^{j},\theta_3^{j}$ ($j=2,3$) are chosen;
- $n=4$: 6 equations, 7 unknowns ($L,L^*$, and $\theta^{j}$ for $j=2,3,4$ when one set is free) → choose **one**; equations are **nonlinear** because some angles are unknown;
- $n=5$: no free choice at all.

---

## 3. Dyad (standard-form) method

![[SFB-a3-dyads.png]]

A 4R is two **dyads**: left $L$ ($O_2\to A$), $L^*$ ($A\to C$); right $R$ ($O_4\to B$), $R^*$ ($B\to C$). Coupler $AB$ and frame $O_2O_4$ follow by vector addition; the coupler point $C_1$ is at vector $P$. Rotations are measured from the starting position, CCW positive; $\theta_3^j$ (coupler) is **common** to both dyads.

Writing the vector loop for the $j$-th configuration against the first (the coupler point moves from $C_1$ to $C_j$):

$$
\boxed{L\big(e^{i\theta_2^j}-1\big)+L^*\big(e^{i\theta_3^j}-1\big)=P_j-P=\delta_j}\qquad(3.18)
$$

$$
\boxed{R\big(e^{i\theta_4^j}-1\big)+R^*\big(e^{i\theta_3^j}-1\big)=\delta_j}\qquad(3.19)
$$

($j=2,\dots,n$.) Each is two scalar equations. With $\delta_j$ and the angles known, both are **linear complex** equations in the dyad vectors.

> [!example] 2×2 complex solve for $n=3$
> $$
> \begin{pmatrix}e^{i\theta_2^2}-1 & e^{i\theta_3^2}-1\\ e^{i\theta_2^3}-1 & e^{i\theta_3^3}-1\end{pmatrix}\begin{pmatrix}L\\L^*\end{pmatrix}=\begin{pmatrix}\delta_2\\\delta_3\end{pmatrix}
> $$
> same matrix with $\theta_4$ in place of $\theta_2$ for $(R,R^*)$. Then $O_2=C_1-L-L^*$, $O_4=C_1-R-R^*$, $A_1=O_2+L$, $B_1=O_4+R$.

---

## 4. Path generation by dyads

Three given points $C_1,C_2,C_3$ ⇒ $\delta_2=C_2-C_1$, $\delta_3=C_3-C_1$ (the right sides are known):

$$
L\big(e^{i\theta_2^2}-1\big)+L^*\big(e^{i\theta_3^2}-1\big)=\delta_2,\qquad
L\big(e^{i\theta_2^3}-1\big)+L^*\big(e^{i\theta_3^3}-1\big)=\delta_3\qquad(3.20a,b)
$$

4 scalar equations ⇒ 4 scalar unknowns ($L$, $L^*$). **Free choices:** $\theta_2^2,\theta_2^3,\theta_3^2,\theta_3^3$. Choosing the two **crank** rotations also coordinates the point motion with the input rotation. The right dyad via (3.19) needs two further choices, $\theta_4^2$ and $\theta_4^3$ (the coupler rotations $\theta_3^j$ are already fixed).


---

## 5. Motion generation by dyads

Prescribe three positions of the coupler $A_1B_1,\ A_2B_2,\ A_3B_3$ (equivalently the coupler rotations $\theta_3^j$ and the displacement of one body point).

- Treat $A$ as the coupler point: **$L^*=0$**, and the right dyad $R^*=\overrightarrow{B_1A_1}$ (known body vector). Then the problem becomes the path problem above.
- Left dyad: $L(e^{i\theta_2^j}-1)=\delta_j$ for $j=2,3$ with $\delta_j=A_j-A_1$: the angles $\theta_2^j$ are **unknowns** here, and $L=O_2A_1$ is exactly the radius vector to the circumcentre of $A_1A_2A_3$ – the same result as the graphical circle construction ([[Motion and Path Generation - Graphical Methods#3. Motion generation (three positions)]]).
- Right dyad: $R(e^{i\theta_4^j}-1)+R^*(e^{i\theta_3^j}-1)=\delta_j$ with $R^*=B_1A_1$ and the prescribed $\theta_3^j$.

**Equivalent circle form** (used in the code): $A_j=O_2+L\,e^{i\theta_2^j}$ lies on a circle about $O_2$; $O_2$ solves $|A_1-O_2|=|A_2-O_2|=|A_3-O_2|$ (circumcentre formula, [[#10. Cookbook for the coordinates]]).

---

## 6. Function generation by dyads

Coordinate only the input and output links; no coupler point is needed. Use a **triad** $L$ (crank), $M$ (coupler), $R$ (rocker), $R$ chosen arbitrarily (it fixes only scale and orientation):

$$
L\big(e^{i\theta_2^j}-1\big)+M\big(e^{i\theta_3^j}-1\big)=R\big(e^{i\theta_4^j}-1\big)\qquad(3.21)
$$

The $\theta_2^j,\theta_4^j$ pairs are assumed. For $>3$ accuracy points the equations become **nonlinear** because one $\theta_3^j$ is left unknown.

---

## 7. Freudenstein four-bar function generator

Coordinates: $A=(l_2\cos\theta_2,\ l_2\sin\theta_2)$, $B=(l_1+l_4\cos\theta_4,\ l_4\sin\theta_4)$.

$$
l_3^2=AB^2=(l_2\cos\theta_2-l_1-l_4\cos\theta_4)^2+(l_2\sin\theta_2-l_4\sin\theta_4)^2
$$

$$
\boxed{\cos(\theta_2-\theta_4)=K_1\cos\theta_4-K_2\cos\theta_2+K_3}\qquad(3.6)
$$

$$
K_1=\frac{l_1}{l_2},\qquad K_2=\frac{l_1}{l_4},\qquad K_3=\frac{l_1^2+l_2^2-l_3^2+l_4^2}{2\,l_2l_4}
$$

**Procedure ($n=3$):** assume $\theta_2^i,\theta_4^i,r_x,r_y$ (three accuracy points ↔ three length ratios) → Chebyshev $x_1,x_2,x_3$ (3.4) → $y_l=f(x_l)$ → $\theta_2^l,\theta_4^l$ from (3.1),(3.2) → three linear equations in $K_1,K_2,K_3$ → ratios; fix one length (smallest link); $l_3=\sqrt{l_1^2+l_2^2+l_4^2-2l_2l_4K_3}$. A **negative** $l_2$ or $l_4$ means the vector sense is reversed ($l_1,l_3>0$ always).

> [!note] Why four parameters are assumed
> If any of $\theta_2^i,\theta_4^i,r_x,r_y$ is left free, the equations in the unknowns stop being linear. The same holds for four accuracy points.

**Solving for the output** (for plotting $F$): rewrite as $(K_1-\cos\theta_2)\cos\theta_4-\sin\theta_2\sin\theta_4=K_2\cos\theta_2-K_3$, i.e. $\rho\cos(\theta_4+\varphi)=K_2\cos\theta_2-K_3$ with $\rho=\sqrt{(K_1-\cos\theta_2)^2+\sin^2\theta_2}$, $\varphi=\operatorname{atan2}(\sin\theta_2,K_1-\cos\theta_2)$.

> [!example] Prob. 3.5: $y=\log_{10}x$, $1\le x\le10$, smallest link 5 cm
> $a=5.5,\ h=4.5$: $x=9.4,5.5,1.6$; $y=0.974,0.741,0.204$. $\theta_2^i=45^\circ,\theta_4^i=135^\circ$, $r_x=60^\circ/9,\ r_y=90^\circ$ → pairs $(101^\circ,222.7^\circ),(75^\circ,201.7^\circ),(49^\circ,153.4^\circ)$ →
> $K_1=2,\ K_2=-0.703,\ K_3=1.078$ → $l_2=5,\ l_1=10,\ l_3=21.85,\ l_4=-14.20$ cm.
> The plot above shows $E(x)$ vanishing at the accuracy points.

---

## 8. Slider-crank function generator

![[SFB-a2-slider-crank.png]]

Slider displacement proportional to a function of crank rotation, e.g.

$$
s-s^i=C(\theta_2-\theta_2^i)\ \text{ or }\ s=s^i+C(\theta_2-\theta_2^i)^2\qquad(3.7)
$$

Design parameters: $\theta_2^i,\ s^i$ (assumed), $l_2,l_3,l_4$ (unknown, $l_4$ = offset). With $A=(l_2\cos\theta_2,\ l_2\sin\theta_2)$, $B=(s,\ l_4)$:

$$
\boxed{K_1 s\cos\theta_2+K_2\sin\theta_2-K_3=s^2}\qquad(3.8)
$$

$$
K_1=2l_2,\quad K_2=2l_2l_4,\quad K_3=l_2^2-l_3^2+l_4^2
$$

Three accuracy points $\to$ three linear equations. Recover: $l_2=K_1/2,\ l_4=K_2/(2l_2),\ l_3=\sqrt{l_2^2+l_4^2-K_3}$ (negative $l_2,l_4$ in the vector sense).

> [!example] Prob. 3.6: $s\propto$ (rotation)$^2$ on $45^\circ\le\theta_2\le135^\circ$
> $s^i=10$, $C=(3-10)/90^2$ per deg², accuracy angles $128.7^\circ,90^\circ,51.3^\circ$ (book) → $s=3.95,\ 8.26,\ 9.97$ cm →
> $K_1=9.61,\ K_2=130.75,\ K_3=62.75$ → $l_2=4.805,\ l_4=13.6,\ l_3=12.05$ cm.

### 8.1 Four accuracy points

$s^i$ also becomes unknown. Write $s_l=s^i+s''_l$ ($s''_l=C(\theta_2^l-\theta_2^i)^2$ known):

$$
R_1\cos\theta_2+R_2s''\cos\theta_2+R_3\sin\theta_2-R_4=R_5s''+(s'')^2,\ \ l=1,\dots,4\qquad(3.9)
$$

$$
R_1=2l_2s^i,\ R_2=2l_2,\ R_3=2l_2l_4,\ R_4=l_2^2-l_3^2+l_4^2+(s^i)^2,\ R_5=2s^i
$$

The five $R$'s are **not independent**: $\boxed{2R_1=R_2R_5}$ (compatibility, 3.10). Put $R_5=\Lambda$; solve the two linear systems

$$
P_1\cos\theta_2+P_2s''\cos\theta_2+P_3\sin\theta_2-P_4=s'',\qquad Q_1\cos\theta_2+Q_2s''\cos\theta_2+Q_3\sin\theta_2-Q_4=(s'')^2\quad(3.13a,b)
$$

and set $R_i=Q_i+\Lambda P_i$ $(i=1..4)$ (3.14). Compatibility (3.11) gives

$$
\Lambda^2P_2+(Q_2-2P_1)\Lambda-2Q_1=0\qquad(3.15)
$$

then $l_2=R_2/2,\ s^i=R_5/2,\ l_4=R_3/R_2,\ l_3=\sqrt{l_2^2+l_4^2+(s^i)^2-R_4}$.

| $(Q_2-2P_1)^2+8P_2Q_1$ | solutions |
|---|---|
| $>0$ | two |
| $=0$ | one |
| $<0$ | none |

(Verified: the code builds a known slider-crank, samples four accuracy points, and this procedure recovers its $l_2,l_3,l_4,s^i$.)

### 8.2 Five accuracy points
$\theta_2^i$ is unknown too: $\theta_2^l=\theta_2^1+\Delta\theta_2^{l1}$ (3.16), $s_l=s^1+\Delta s^{l1}$ (3.17), with spacings specified from the first point; (3.8) gives 5 nonlinear equations in $l_2,l_3,l_4,\theta_2^1,s^1$ – computer needed.

---

## 9. Instantaneous conditions

Prescribe velocities and accelerations of links 2 and 4 at a given pose; differentiate (3.6):

$$
(\omega_2-\omega_4)\sin(\theta_2-\theta_4)=K_1\omega_4\sin\theta_4-K_2\omega_2\sin\theta_2
$$

$$
(\alpha_2-\alpha_4)\sin(\theta_2-\theta_4)+(\omega_2-\omega_4)^2\cos(\theta_2-\theta_4)=K_1(\alpha_4\sin\theta_4+\omega_4^2\cos\theta_4)-K_2(\alpha_2\sin\theta_2+\omega_2^2\cos\theta_2)
$$

Together with (3.6) these are three **linear** equations in $K_1,K_2,K_3$.

> [!example] Prob. 3.7: $\theta_2=60^\circ,\theta_4=90^\circ,\omega_2=3,\omega_4=2$ rad/s, $\alpha_2=-1,\alpha_4=0$
> $0.866=-0.5K_2+K_3,\ -0.5=2K_1-2.598K_2,\ 1.366=-3.634K_2$ → $K_1=-0.738,\ K_2=-0.376,\ K_3=0.678$ → the book prints $-0.738,\ -0.376,\ 0.446$ as the three link-length ratios (the text layer does not make clear which ratio the last one is; $K_3=0.678$ is the third unknown).

---

## 10. Cookbook for the coordinates

Formulas used in [[synth_core.py]] (my own working-out of the book's constructions, checked numerically).

| Task | Formula |
|---|---|
| circumcentre $(a,b,c)$ | $d=2[a_x(b_y-c_y)+b_x(c_y-a_y)+c_x(a_y-b_y)]$, $u_x=\dfrac{|a|^2(b_y-c_y)+|b|^2(c_y-a_y)+|c|^2(a_y-b_y)}{d}$, $u_y=\dfrac{|a|^2(c_x-b_x)+|b|^2(a_x-c_x)+|c|^2(b_x-a_x)}{d}$ |
| point on coupler pose $(t,\varphi)$ | $w=R(\varphi)q+t$; inverse $q=R(-\varphi)(w-t)$ |
| pivot seen from pose 1 | $O^1_{k}=R(\varphi_1)\,R(-\varphi_k)(O-t_k)+t_1$ |
| circle–circle ($B_k$) | $d=|c_1-c_0|$, $a=\dfrac{r_0^2-r_1^2+d^2}{2d}$, $h=\sqrt{r_0^2-a^2}$; take the root nearest the previous $B$ |
| pole $P_{12}$ | solve $(m_1-m_2)+t_1n_1-t_2n_2=0$ for the mid-normals $(m_i,n_i)$ |
| dyad (3.20) | solve the 2×2 complex system above |
| Freudenstein / slider | solve the 3×3 linear systems (3.6), (3.8) |

---

## 11. Benchmarks

| Item | Book | Code |
|---|---|---|
| Chebyshev $k=3$, $[1,10]$ | 9.4, 5.5, 1.6 | 9.40, 5.50, 1.60 |
| Prob. 3.5 $K_1,K_2,K_3$ | 2, −0.703, 1.078 | match ($\pm0.03$) |
| Prob. 3.5 links | 10, 5, 21.85, −14.20 cm | match |
| Prob. 3.6 $K_1,K_2,K_3$ | 9.61, 130.75, 62.75 | match ($\pm1\%$) |
| Prob. 3.6 links | 4.805, 13.6, 12.05 cm | match |
| Prob. 3.7 $K_1,K_2,K_3$ | −0.738, −0.376, 0.678 | match |
| dyad solve (3.20) | – | recovers a known 4R; $L,L^*,R,R^*$ reproduce $O_2A,AC,O_4B,BC$ |
| four-point slider-crank | – | recovers known $l_2,l_3,l_4,s^i$ |

---

## 12. Notes on the book's numbers

> [!warning]
> 1. **Prob. 3.6 accuracy points:** (3.4) with $a=90^\circ,\ h=45^\circ,\ k=3$ gives $129.0^\circ,\ 90^\circ,\ 51.0^\circ$; the book uses $128.7^\circ,\ 90^\circ,\ 51.3^\circ$ (and $s=3.95$ cm; one line prints 3.96). Results differ in the third digit only.
> 2. **(3.6) constants:** the definitions of $K_1,K_2,K_3$ are partly garbled in the text layer. The forms used here ($K_1=l_1/l_2,\ K_2=l_1/l_4,\ K_3=(l_1^2+l_2^2-l_3^2+l_4^2)/2l_2l_4$) reproduce Prob. 3.5 exactly ($l_1/l_2=2$, $l_1/l_4=-0.703$, $l_3=21.85$).
> 3. **Prob. 3.5:** the printed "$\theta_2^f-\theta_2^i=60^\circ$" and "$\theta_4^f-\theta_4^i=90^\circ$" fix $r_x=60/9,\ r_y=90$; the book shows these were obtained "indirectly" from assumed final angles (105°, 225°).
> 4. The PDF text layer is duplicated and garbles some fractions; relations here were re-derived (e.g. (3.8)–(3.15)) or confirmed numerically before use.

---

## Tools

![[SFB-a3-dyads.png]]

- Figures: `Synthesis-Formula-Bank/assets` (`SFB-a1`…`a3` here; `SFB-g1`…`g6` in the graphical note); regenerate with `python synth_viz.py`.
- Interactive: [synthesis-explorer.html](synthesis-explorer.html) – right-click → *Open in default app*. It includes the dyad solver, the Freudenstein solver and the Chebyshev spacing.

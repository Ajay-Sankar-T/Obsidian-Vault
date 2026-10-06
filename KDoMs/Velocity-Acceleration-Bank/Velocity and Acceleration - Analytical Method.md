---
title: Velocity and Acceleration – Analytical Method
course: ME 2201 Kinematics & Dynamics of Machinery
tags:
  - KDoM
  - formula-bank
  - kinematics
  - velocity
  - acceleration
  - loop-closure
source: "[[Ghosh and Mallik.pdf]]"
pages: "PDF p. 60–66 (Sec. 2.2 analytical displacement), 75–80 (Sec. 2.3), 115–116 (Sec. 2.9, Prob. 2.19), book pp. 51–57, 66–71, 106–107"
aliases:
  - Analytical velocity and acceleration
  - Loop closure velocity acceleration
---

# Velocity and Acceleration – Analytical Method

Source: [[Ghosh and Mallik.pdf]], Ch. 2 *Kinematic Analysis of Plane Mechanisms* · Related: [[Motion and Path Generation - Analytical Methods]], [[Gear Formula Bank]]
Equation numbers in brackets are the book's. Relations marked **(derived)** are not printed in the book's Sec. 2.9 but follow by the same method; every formula in this note is checked against finite differences of the displacement solution in `va_core.py`.

> [!abstract] Contents
> [[#0. Conventions]] · [[#1. Principle]] · [[#2. Rigid-body and coincident-point relations]] · [[#3. Four-bar linkage]] · [[#4. Offset slider-crank]] · [[#5. Slotted-lever quick-return (Prob. 2.19)]] · [[#6. General recipe for any loop]] (incl. [[#6.1 Newton–Raphson method]]) · [[#7. Instantaneous centre shortcut]] · [[#8. Checks and tools]] · [[#9. Notes on the book]]

> [!tip] The whole method in four lines
> 1. Write each independent closed loop as a complex vector equation.
> 2. Solve the **displacement** problem (nonlinear): gives all angles and slides.
> 3. Differentiate once: **linear** in the unknown velocities.
> 4. Differentiate again: **linear** in the unknown accelerations (velocities now known).

---

## 0. Conventions

| Symbol | Meaning |
|---|---|
| $l_i$ | length of link $i$ (link 1 = frame), vector $\mathbf l_i=l_ie^{i\theta_i}$ |
| $\theta_i$ | angle of link $i$, **CCW from the frame** ($\theta_1=0$) |
| $\omega_i=\dot\theta_i,\ \alpha_i=\ddot\theta_i$ | angular velocity / acceleration, CCW positive |
| $s$ | slider displacement, $e$ offset |

For a link vector of constant length: $\ \dot{\mathbf l}=i\omega\,\mathbf l,\qquad \ddot{\mathbf l}=(i\alpha-\omega^2)\,\mathbf l$ — i.e. velocity is $\boldsymbol\omega\times\mathbf l$ and acceleration is $\boldsymbol\alpha\times\mathbf l-\omega^2\mathbf l$ (tangential + normal).

---

## 1. Principle

> [!important] Why this works (Sec. 2.9)
> The loop-closure equations hold at every instant, so their time derivatives do too. Once the configuration is known, **velocity and acceleration equations are linear** in the unknown quantities, so they are easy to solve, accurate, and trivial to evaluate for many configurations (a program, or the explorer below).

---

## 2. Rigid-body and coincident-point relations

(Sec. 2.3, needed for coupler points and sliding joints.)

**Particle on a path** (radius of curvature $\rho$, $\omega$ = angular velocity of the radius):

$$
V=\rho\dot\theta=\rho\omega\ (2.13),\qquad a_n=\frac{V^2}{\rho}=\rho\omega^2\ (2.14),\qquad a_t=\rho\dot\omega+\dot\rho\omega=\rho\alpha+\dot\rho\omega\ (2.15)
$$

**Two points on one rigid body** ($A,B$; $\boldsymbol\omega,\boldsymbol\alpha$ of the body):

$$
\mathbf V_B=\mathbf V_A+\boldsymbol\omega\times\overrightarrow{AB}\qquad(2.16)
$$

$$
\mathbf a_B=\mathbf a_A+\underbrace{\boldsymbol\omega\times(\boldsymbol\omega\times\overrightarrow{AB})}_{AB\,\omega^2,\ \text{along }BA}+\underbrace{\boldsymbol\alpha\times\overrightarrow{AB}}_{AB\,\alpha,\ \perp AB}\qquad(2.17)
$$

**Two coincident points $P_i,P_j$ on links $i,j$** (path of $P_j$ known on link $i$; use an inversion with link $i$ fixed to see that path):

$$
\mathbf V_{P_j}=\mathbf V_{P_i}+\mathbf V_{P_j/i}\qquad(2.18,\ 2.22)
$$

$$
\mathbf a_{P_j}=\mathbf a_{P_i}+\mathbf a^{\,n}_{P_j/i}+\mathbf a^{\,t}_{P_j/i}+\mathbf a_c\qquad(2.21,\ 2.23)
$$

$$
\boxed{\mathbf a_c=2\,\boldsymbol\omega_i\times\mathbf V_{P_j/i}}\ (\text{Coriolis}),\qquad a_c=2V_{P_j/i}\,\omega_i\qquad(2.19,\ 2.24)
$$

$a^{\,n}_{P_j/i}=\big(V_{P_j/i}\big)^2/\rho$ (zero for a straight slot, $\rho\to\infty$). The Coriolis direction is $\mathbf V_{P_j/i}$ rotated $90^\circ$ in the sense of $\omega_i$. The coincident points need not be on adjacent links.

![[VA-v5-coriolis.png]]

---

## 3. Four-bar linkage

### 3.1 Displacement (needed first)

Loop $O_2O_4BAO_2$:

$$
\mathbf l_1+\mathbf l_4+\mathbf l_3-\mathbf l_2=0\qquad(2.1)\ \Rightarrow\ l_1+l_4e^{i\theta_4}+l_3e^{i\theta_3}-l_2e^{i\theta_2}=0
$$

$$
l_1+l_4\cos\theta_4+l_3\cos\theta_3-l_2\cos\theta_2=0,\qquad l_4\sin\theta_4+l_3\sin\theta_3-l_2\sin\theta_2=0\qquad(2.2a,b)
$$

Eliminating $\theta_3$:

$$
a\sin\theta_4+b\cos\theta_4=c\qquad(2.3)
$$

$$
a=\sin\theta_2,\quad b=\cos\theta_2-\frac{l_1}{l_2},\quad c=-\frac{l_1}{l_4}\cos\theta_2+\frac{l_1^2+l_2^2+l_4^2-l_3^2}{2l_2l_4}
$$

With $t=\tan(\theta_4/2)$: $(b+c)t^2-2at+(c-b)=0$, so

$$
\boxed{\theta_4=2\tan^{-1}\!\left[\frac{a\pm\sqrt{a^2+b^2-c^2}}{b+c}\right]}\qquad(2.4a,b)
$$

The two roots are the two **assembly modes**. Complex roots ($a^2+b^2<c^2$) mean the linkage cannot be assembled at that $\theta_2$. Then $\theta_3$ from $(2.5a,b)$ or, without quadrant ambiguity,

$$
\theta_3=\operatorname{atan2}\big(l_2\sin\theta_2-l_4\sin\theta_4,\ l_2\cos\theta_2-l_1-l_4\cos\theta_4\big)
$$

Use `atan2` (the book's footnote: ATAN2 in Fortran). Grashof linkages have two **disconnected** branches; non-Grashof ones a single closed loop.

### 3.2 Velocity

Differentiate (2.2a,b):

$$
l_4\sin\theta_4\,\omega_4+l_3\sin\theta_3\,\omega_3-l_2\sin\theta_2\,\omega_2=0,\qquad
l_4\cos\theta_4\,\omega_4+l_3\cos\theta_3\,\omega_3-l_2\cos\theta_2\,\omega_2=0\qquad(2.33a,b)
$$

Two linear equations in $\omega_3,\omega_4$:

$$
\boxed{\omega_3=\omega_2\,\frac{l_2\sin(\theta_2-\theta_4)}{l_3\sin(\theta_3-\theta_4)},\qquad
\omega_4=\omega_2\,\frac{l_2\sin(\theta_2-\theta_3)}{l_4\sin(\theta_4-\theta_3)}}
$$

(Multiply the first equation by $\cos\theta_4$, the second by $\sin\theta_4$, subtract → $\omega_3$; swap roles with $\theta_3$ → $\omega_4$.) Singular when $\sin(\theta_3-\theta_4)=0$, i.e. coupler and follower collinear (toggle position).

### 3.3 Acceleration

Differentiating (2.33a,b) again:

$$
l_4(\cos\theta_4\,\omega_4^2+\sin\theta_4\,\alpha_4)+l_3(\cos\theta_3\,\omega_3^2+\sin\theta_3\,\alpha_3)=l_2(\cos\theta_2\,\omega_2^2+\sin\theta_2\,\alpha_2)
$$

$$
l_4(-\sin\theta_4\,\omega_4^2+\cos\theta_4\,\alpha_4)+l_3(-\sin\theta_3\,\omega_3^2+\cos\theta_3\,\alpha_3)=l_2(-\sin\theta_2\,\omega_2^2+\cos\theta_2\,\alpha_2)\qquad(2.34a,b)
$$

Linear in $\alpha_3,\alpha_4$ (the velocities are known by now):

$$
\boxed{\alpha_3=\frac{l_2\alpha_2\sin(\theta_2-\theta_4)+l_2\omega_2^2\cos(\theta_2-\theta_4)-l_4\omega_4^2-l_3\omega_3^2\cos(\theta_3-\theta_4)}{l_3\sin(\theta_3-\theta_4)}}
$$

$$
\boxed{\alpha_4=\frac{l_2\alpha_2\sin(\theta_2-\theta_3)+l_2\omega_2^2\cos(\theta_2-\theta_3)-l_3\omega_3^2-l_4\omega_4^2\cos(\theta_4-\theta_3)}{l_4\sin(\theta_4-\theta_3)}}
$$

### 3.4 Points on the links

Once $\omega_i,\alpha_i$ are known, any point $C$ of the coupler at $\overrightarrow{AC}$:

$$
\mathbf V_C=\mathbf V_A+\omega_3\,\hat k\times\overrightarrow{AC},\qquad \mathbf a_C=\mathbf a_A+\alpha_3\,\hat k\times\overrightarrow{AC}-\omega_3^2\,\overrightarrow{AC}
$$

with $\mathbf V_A=\omega_2\hat k\times\mathbf l_2$, $\mathbf a_A=\alpha_2\hat k\times\mathbf l_2-\omega_2^2\mathbf l_2$. Check: $B$ computed from the follower ($\mathbf V_B=\omega_4\hat k\times\mathbf l_4$) equals $B$ computed through the coupler.

![[VA-v2-vectors.png]]

![[VA-v1-fourbar-curves.png]]

> [!note] Equal forward/return time and transmission angle (same chapter, useful with the above)
> Equal crank rotation for forward and return strokes of the rocker: $l_1^2+l_2^2=l_3^2+l_4^2$ (2.6), and then $l_2=l_4\sin(\Delta\theta_4/2)$ (2.7). Transmission angle $\mu$ = acute angle between coupler and follower; $\mu_{\min}>30^\circ$ for good transmission. Slider-crank: $\mu_{\min}=\cos^{-1}[(l_2+e)/l_3]$ (2.12).

---

## 4. Offset slider-crank (derived)

Loop: $l_2e^{i\theta_2}+l_3e^{i\theta_3}=s+ie$ (slider at height $e$).

**Displacement**

$$
\sin\theta_3=\frac{e-l_2\sin\theta_2}{l_3},\qquad s=l_2\cos\theta_2+l_3\cos\theta_3\quad(\text{two modes: }\theta_3\text{ or }\pi-\theta_3)
$$

**Velocity** (differentiate: $-l_2\sin\theta_2\omega_2-l_3\sin\theta_3\omega_3=\dot s,\ \ l_2\cos\theta_2\omega_2+l_3\cos\theta_3\omega_3=0$)

$$
\boxed{\omega_3=-\frac{l_2\omega_2\cos\theta_2}{l_3\cos\theta_3},\qquad \dot s=-\frac{l_2\omega_2\sin(\theta_2-\theta_3)}{\cos\theta_3}}
$$

**Acceleration**

$$
\alpha_3=\frac{-l_2\alpha_2\cos\theta_2+l_2\omega_2^2\sin\theta_2+l_3\omega_3^2\sin\theta_3}{l_3\cos\theta_3},\qquad
\ddot s=-l_2\alpha_2\sin\theta_2-l_2\omega_2^2\cos\theta_2-l_3\alpha_3\sin\theta_3-l_3\omega_3^2\cos\theta_3
$$

![[VA-v3-slider-crank.png]]

---

## 5. Slotted-lever quick-return (Prob. 2.19)

Mechanism of Fig. 2.9a: crank $O_2A$ ($l_2$), slotted lever 4 pivoted at $O_4$ with the crank pin sliding in the slot; $l_1=O_2O_4$ (vertical).

**Loop** and displacement:

$$
l_1e^{i\pi/2}+s_4e^{i\theta_4}-l_2e^{i\theta_2}=0\qquad(2.8)
$$

$$
s_4\cos\theta_4=l_2\cos\theta_2,\qquad s_4\sin\theta_4=l_1+l_2\sin\theta_2
$$

$$
\boxed{s_4=\sqrt{l_1^2+l_2^2+2l_1l_2\sin\theta_2}\quad(2.10),\qquad \theta_4=\tan^{-1}\frac{l_1+l_2\sin\theta_2}{l_2\cos\theta_2}\quad(2.11)}
$$

(Quadrant from the signs of numerator and denominator: `atan2`.)

**Velocity** — differentiate the two components:

$$
\dot s_4\cos\theta_4-s_4\sin\theta_4\,\dot\theta_4=-l_2\sin\theta_2\,\dot\theta_2,\qquad
\dot s_4\sin\theta_4+s_4\cos\theta_4\,\dot\theta_4=l_2\cos\theta_2\,\dot\theta_2\quad(c,d)
$$

$$
\boxed{\dot\theta_4=\frac{l_2\dot\theta_2}{s_4}\cos(\theta_4-\theta_2)\quad(e),\qquad \dot s_4=l_2\dot\theta_2\sin(\theta_4-\theta_2)\quad(f)}
$$

**Acceleration** (the book leaves this as an exercise; derived):

$$
\boxed{\ddot\theta_4=\frac{l_2\alpha_2\cos(\theta_4-\theta_2)+l_2\omega_2^2\sin(\theta_4-\theta_2)-2\dot s_4\dot\theta_4}{s_4}}\qquad
\boxed{\ddot s_4=s_4\dot\theta_4^{\,2}+l_2\alpha_2\sin(\theta_4-\theta_2)-l_2\omega_2^2\cos(\theta_4-\theta_2)}
$$

The term $-2\dot s_4\dot\theta_4/s_4$ is the **Coriolis** contribution. Equivalent vector check (verified numerically): the crank-pin acceleration equals

$$
\mathbf a_A=\underbrace{-\omega_4^2s_4\,\hat e}_{a^n_{P_4}}+\underbrace{\alpha_4s_4\,\hat k\times\hat e}_{a^t_{P_4}}+\underbrace{\ddot s_4\,\hat e}_{a_{rel}}+\underbrace{2\omega_4\dot s_4\,\hat k\times\hat e}_{a_c},\qquad \hat e=(\cos\theta_4,\sin\theta_4)
$$

(2.23), with $P_4$ the point of the lever coincident with $A$.

![[VA-v4-slotted-lever.png]]

*Quick-return ratio* for constant $\omega_2$ is the ratio of the crank rotations for the cutting and idle strokes, e.g. Prob. 2.1: $239^\circ/121^\circ=1.975$.

---

## 6. General recipe for any loop (extension, not in the book's section)

Let $\Phi(\mathbf q,\theta_2)=0$ be the stacked real/imaginary loop equations in the unknown coordinates $\mathbf q$ (angles, slide lengths):

$$
\Phi_{\mathbf q}\,\dot{\mathbf q}=-\Phi_{\theta_2}\,\omega_2\qquad\text{(velocity, linear)}
$$

$$
\Phi_{\mathbf q}\,\ddot{\mathbf q}=-\Phi_{\theta_2}\,\alpha_2-\dot\Phi_{\mathbf q}\,\dot{\mathbf q}-\dot\Phi_{\theta_2}\,\omega_2\qquad\text{(acceleration, same matrix)}
$$

The same matrix $\Phi_{\mathbf q}$ appears at both levels; it is singular exactly at the toggle positions. Each loop contributes two scalar equations; use as many loops as there are unknowns (the slotted lever has two loops, (2.8) and (2.9)).

| Mechanism | unknowns | loop equations | singular when |
|---|---|---|---|
| 4R | $\theta_3,\theta_4$ | 2 | $\sin(\theta_3-\theta_4)=0$ |
| slider-crank | $\theta_3,s$ | 2 | $\cos\theta_3=0$ |
| slotted lever | $\theta_4,s_4$ | 2 | $s_4=0$ |

### 6.1 Newton–Raphson method

For a four-bar or slider-crank, (2.4) solves the displacement exactly. For longer chains (several loops) the displacement equations cannot be solved in closed form, so solve $\Phi(\mathbf q,\theta_2)=0$ **numerically** with Newton–Raphson. The velocity and acceleration steps are unchanged, and they reuse the Jacobian $J=\Phi_{\mathbf q}$ that Newton already built.

**Algorithm** (given $\theta_2$, a first guess $\mathbf q_0$):

$$
\mathbf q_{k+1}=\mathbf q_k-J(\mathbf q_k)^{-1}\,\Phi(\mathbf q_k,\theta_2)\quad\Longleftrightarrow\quad J\,\Delta\mathbf q=-\Phi,\ \ \mathbf q\leftarrow\mathbf q+\Delta\mathbf q
$$

Stop when $\lVert\Phi\rVert<\varepsilon$ (e.g. $10^{-12}$). Then, with $\mathbf q$ converged:

$$
J\,\dot{\mathbf q}=-\Phi_{\theta_2}\,\omega_2,\qquad J\,\ddot{\mathbf q}=-\Phi_{\theta_2}\,\alpha_2-\boldsymbol\gamma(\mathbf q,\dot{\mathbf q},\omega_2)
$$

where $\boldsymbol\gamma$ is every term of $\ddot\Phi$ that contains neither $\ddot{\mathbf q}$ nor $\alpha_2$ (the "velocity-squared" terms). These are the normal-acceleration and Coriolis terms.

| Mechanism | $\mathbf q$ | $\Phi$ | $J=\Phi_{\mathbf q}$ | $\Phi_{\theta_2}$ | $\boldsymbol\gamma$ |
|---|---|---|---|---|---|
| 4R | $(\theta_3,\theta_4)$ | $\begin{pmatrix}l_1+l_4c_4+l_3c_3-l_2c_2\\ l_4s_4+l_3s_3-l_2s_2\end{pmatrix}$ | $\begin{pmatrix}-l_3s_3&-l_4s_4\\ l_3c_3&l_4c_4\end{pmatrix}$ | $\begin{pmatrix}l_2s_2\\-l_2c_2\end{pmatrix}$ | $\begin{pmatrix}-l_3c_3\omega_3^2-l_4c_4\omega_4^2+l_2c_2\omega_2^2\\ -l_3s_3\omega_3^2-l_4s_4\omega_4^2+l_2s_2\omega_2^2\end{pmatrix}$ |
| slider-crank | $(\theta_3,s)$ | $\begin{pmatrix}l_2c_2+l_3c_3-s\\ l_2s_2+l_3s_3-e\end{pmatrix}$ | $\begin{pmatrix}-l_3s_3&-1\\ l_3c_3&0\end{pmatrix}$ | $\begin{pmatrix}-l_2s_2\\ l_2c_2\end{pmatrix}$ | $\begin{pmatrix}-l_2c_2\omega_2^2-l_3c_3\omega_3^2\\ -l_2s_2\omega_2^2-l_3s_3\omega_3^2\end{pmatrix}$ |
| slotted lever | $(\theta_4,s_4)$ | $\begin{pmatrix}s_4\cos\theta_4-l_2c_2\\ s_4\sin\theta_4-l_1-l_2s_2\end{pmatrix}$ | $\begin{pmatrix}-s_4\sin\theta_4&\cos\theta_4\\ s_4\cos\theta_4&\sin\theta_4\end{pmatrix}$ | $\begin{pmatrix}l_2s_2\\-l_2c_2\end{pmatrix}$ | $\begin{pmatrix}-2\dot s_4\omega_4\sin\theta_4-s_4\omega_4^2\cos\theta_4+l_2c_2\omega_2^2\\ 2\dot s_4\omega_4\cos\theta_4-s_4\omega_4^2\sin\theta_4+l_2s_2\omega_2^2\end{pmatrix}$ |

($c_i=\cos\theta_i,\ s_i=\sin\theta_i$ for the 4R and slider-crank rows; in the slotted-lever row $s_4$ is the slide length and $c_2,s_2$ are the crank's cosine and sine.)

> [!example] One four-bar step, $l=(5.5,\,1.7,\,5.5,\,4.08)$, $\theta_2=65^\circ$
> First guess: the solution at $\theta_2=60^\circ$, $\mathbf q_0=(2.0353,\,4.1469)$ rad.
>
> | $k$ | $\theta_3$ | $\theta_4$ | $\lVert\Phi\rVert$ |
> |---|---|---|---|
> | 0 | 2.03532 | 4.14695 | $1.5\times10^{-1}$ |
> | 1 | 2.03800 | 4.11259 | $2.4\times10^{-3}$ |
> | 2 | 2.03850 | 4.11293 | $6.0\times10^{-7}$ |
> | 3 | 2.03850 | 4.11293 | $5\times10^{-14}$ |
>
> $\theta_3=116.80^\circ,\ \theta_4=235.65^\circ$. With $\omega_2=2,\ \alpha_2=1.5$: $\omega_3=0.1146,\ \omega_4=-0.7477$ rad/s; $\alpha_3=1.945,\ \alpha_4=0.904$ rad/s², identical to (3.2)/(3.3). The error roughly squares each step (quadratic convergence).

**Practical rules**

1. **Initial guess decides the assembly mode.** Newton lands on whichever root is nearest. For a sweep over $\theta_2$, **continuation**: use the converged $\mathbf q$ at the previous $\theta_2$ as the guess for the next. This follows one branch smoothly and converges in 2–4 iterations. For the first position take a guess from a sketch or (2.4).
2. **A bad guess fails.** From $\mathbf q_0=(0.5,\,1.5)$ at the same $\theta_2$ the iteration wandered for 15 steps before converging, and the angle came out as $\theta_4=-8.45$ rad, which is $4.113-4\pi$: the right configuration with extra full turns. A worse guess can land on the other assembly mode instead. Angles are only defined mod $2\pi$, so wrap them (`atan2`) before using them.
3. **Singular Jacobian = toggle / dead centre.** $\det J=l_3l_4\sin(\theta_4-\theta_3)$ for a 4R (the same quantity that appears in the denominators of (3.2), (3.3)). If it is near zero, $\dot{\mathbf q}$ is infinite or indeterminate; stop and treat the position separately.
4. **Non-assemblable positions** never converge (e.g. $l=(6,1,2,2)$): cap the iterations (30 is plenty) and report failure.
5. **Same $J$ for all three solves.** Factor it once (LU) and reuse it for Newton, velocity and acceleration.
6. **Unwrapped angles in a sweep** may differ from the closed-form values by multiples of $2\pi$; velocities and accelerations are unaffected.

**Code** (`va_newton.py`):

```python
def newton(M, q0, th2, tol=1e-12, itmax=30):
    q = np.array(q0, float)
    for _ in range(itmax):
        F = M.phi(q, th2)
        if np.linalg.norm(F) < tol: return q
        q = q + np.linalg.solve(M.jac(q, th2), -F)        # q_{k+1} = q_k - J^-1 Phi
    raise RuntimeError("no convergence")

def vel_acc(M, q, th2, w2=1.0, a2=0.0):
    J  = M.jac(q, th2)
    qd = np.linalg.solve(J, -M.pth(q, th2)*w2)
    qdd = np.linalg.solve(J, -M.pth(q, th2)*a2 - M.gam(q, qd, th2, w2))
    return qd, qdd
```

`fourbar(l)`, `slidercrank(l2,l3,e)`, `slotted(l1,l2)` build the `M` objects; `sweep(M, q0, th2s, w2, a2)` does the continuation loop.

---

## 7. Instantaneous centre shortcut

For velocities only, the Aronhold–Kennedy theorem (Sec. 2.5) gives, for a 4R, $P_{24}$ (found from $P_{12}P_{14}\cap P_{23}P_{34}$) with $V_{P_{24}}=\omega_2\,O_2P_{24}=\omega_4\,O_4P_{24}$:

$$
\frac{\omega_4}{\omega_2}=\frac{O_2P_{24}}{O_4P_{24}}\quad(\text{positive when }P_{24}\text{ lies outside }O_2O_4\text{, i.e. same sense})
$$

A rigid body at the instant: $V_C=PC\cdot V_B/PB$ about its centre $P$ ($V_A/PA=V_B/PB=\omega$, Sec. 2.4). Instantaneous centres give no acceleration information – use the analytical relations above.

---

## 8. Checks and tools

| Check (in `va_core.check()`) | Result |
|---|---|
| 4R, both assembly modes, $\omega_3,\omega_4,\alpha_3,\alpha_4$ vs finite differences of $\theta_3(t),\theta_4(t)$ with $\theta_2(t)=\theta_0+\omega t+\tfrac12\alpha t^2$ | agree ($\le10^{-5}$ in $\omega$, $10^{-3}$ in $\alpha$) |
| loop closure and (2.33a,b) satisfied | ✓ |
| coupler vs follower route to $\mathbf V_B$ and $\mathbf a_B$ (2.16, 2.17) | ✓ |
| slider-crank, both modes: $\dot s,\ddot s,\omega_3,\alpha_3$ | ✓ |
| slotted lever: $\dot\theta_4,\ddot\theta_4,\dot s_4,\ddot s_4$ | ✓ |
| Coriolis closure $\mathbf a_A=\mathbf a_{P_4}+\mathbf a_{rel}+\mathbf a_c$ | ✓ to $10^{-9}$ |
| Newton–Raphson (`va_newton.check()`): 4R both modes, slider-crank both modes, slotted lever, and a 361-point continuation sweep vs the closed forms; unassemblable linkage reports failure | agree to $10^{-9}$ (angles $10^{-10}$) |

**Interactive:** [va-explorer.html](va-explorer.html) – sliders for link lengths, $\theta_2,\omega_2,\alpha_2$; live $\omega_3,\omega_4,\alpha_3,\alpha_4$ (or $\dot s,\ddot s$ / the Coriolis breakdown), velocity and acceleration arrows, an output-vs-$\theta_2$ plot with a marker, and an animate switch. Right-click → *Open in default app*.
**Regenerate figures:** `python va_viz.py` (runs the checks first).

---

## 9. Notes on the book

> [!warning]
> 1. Sec. 2.9 prints only the first and second differentiation of the four-bar equations and the first-derivative part of Prob. 2.19; the closed-form $\alpha_3,\alpha_4$ (3.3), the slider-crank formulas (§4) and the second derivatives for the slotted lever (§5) were derived here and verified numerically.
> 2. The PDF text layer garbles the sign placements in (2.34); the boxed accelerations above are re-derived, and the book's printed forms for $\omega_3,\omega_4$ agree with (3.2).
> 3. In Prob. 2.19 the book writes the velocity of the slide as "$a_4$" in the text layer; it is $\dot s_4$ (f).
> 4. Choose the correct **assembly mode** (±) before differentiating: velocity and acceleration formulas are the same for both modes, but the angles substituted are different.

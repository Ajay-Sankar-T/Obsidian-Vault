---
tags: [EE1100, diodes, tutorial-solution]
---

# A-Q2 — Poisson's Equation, Electric Field and Voltage

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[A-Q1 - Formation of the p-n Junction]] · Next: [[A-Q3 - V-I Characteristics of a p-n Diode]]

> [!question] Write Poisson's equation of space-charge density. From it write the electric field and voltage as functions of distance $x$ from the centre of the space-charge region. Draw the space-charge density, field and voltage.

## 1. Theory — Poisson's equation

In one dimension, with permittivity $\varepsilon=\varepsilon_r\varepsilon_0$ (Si: $\varepsilon_r=11.7$):

$$\frac{dE}{dx}=\frac{\rho(x)}{\varepsilon},\qquad E=-\frac{dV}{dx}\ \Rightarrow\ \boxed{\frac{d^2V}{dx^2}=-\frac{\rho(x)}{\varepsilon}}$$

**Depletion approximation** (abrupt junction at $x=0$): outside the region $\rho=0$; inside,
$$\rho(x)=\begin{cases}-qN_a,&-x_p<x<0\\ +qN_d,&0<x<x_n\end{cases}\qquad\text{with charge neutrality }N_ax_p=N_dx_n.$$

## 2. Electric field

Integrate once, with $E=0$ at $x=-x_p$ and at $x=x_n$ (no field outside the region):

$$E(x)=\begin{cases}-\dfrac{qN_a}{\varepsilon}(x+x_p),&-x_p\le x\le0\\[2mm]-\dfrac{qN_d}{\varepsilon}(x_n-x),&0\le x\le x_n\end{cases}$$

The field is negative (points from n to p), is **linear** in $x$, and is maximal in magnitude at the junction:
$$|E_{max}|=\frac{qN_ax_p}{\varepsilon}=\frac{qN_dx_n}{\varepsilon}.$$

## 3. Voltage

Integrate $E$, with $V=0$ at $x=-x_p$:

$$V(x)=\begin{cases}\dfrac{qN_a}{2\varepsilon}(x+x_p)^2,&-x_p\le x\le0\\[2mm]V_0-\dfrac{qN_d}{2\varepsilon}(x_n-x)^2,&0\le x\le x_n\end{cases}$$

The potential is **quadratic** (an S-shaped curve), and the total step is
$$V_0=\frac{q}{2\varepsilon}\big(N_ax_p^2+N_dx_n^2\big)=\frac12|E_{max}|\,W.$$

**Symmetric case** ($N_a=N_d=N$, so $x_p=x_n=W/2$, centre of the region at $x=0$):
$$E(x)=-\frac{qN}{\varepsilon}\Big(\frac W2-|x|\Big),\qquad V(x)=\begin{cases}\dfrac{qN}{2\varepsilon}\big(x+\tfrac W2\big)^2,&-\tfrac W2\le x\le0\\[2mm]V_0-\dfrac{qN}{2\varepsilon}\big(\tfrac W2-x\big)^2,&0\le x\le\tfrac W2\end{cases}$$
with $V_0=\dfrac{qNW^2}{4\varepsilon}$ and $|E_{max}|=\dfrac{qNW}{2\varepsilon}$.

## 4. Diagrams

![[A2-poisson-profiles.png]]

Example (Si, $N_a=10^{17}$, $N_d=10^{16}$ cm⁻³): $x_p=0.030$ µm, $x_n=0.298$ µm, $W=0.327$ µm, $|E_{max}|=46$ kV/cm, $V_0=0.753$ V (computed from both $V_T\ln(N_aN_d/n_i^2)$ and $q(N_ax_p^2+N_dx_n^2)/2\varepsilon$, which agree).

> [!note] Shapes to draw
> $\rho$: two rectangles of opposite sign with equal areas ($N_ax_p=N_dx_n$) · $E$: a triangle (negative), apex at the junction · $V$: a smooth rise from 0 to $V_0$, steeper where $|E|$ is larger.

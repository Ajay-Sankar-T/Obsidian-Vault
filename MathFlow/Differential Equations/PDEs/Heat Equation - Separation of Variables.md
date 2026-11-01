---
title: Heat Equation – Separation of Variables
tags: [differential-equations, pdes, concept, heat-equation, diffusion, fourier-series]
source: "[[Lecture-34.pdf]], [[Lecture-35.pdf]], [[A9-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Separation of Variables]] · [[Wave Equation on a Finite Interval]] · [[Laplace Equation on Rectangles and Strips]] · [[Heat Transfer - MOC]] · solved in [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]] Q4(d)–(g), Q10–Q18

## What it is
Temperature $u(x,t)$ in a thin rod (insulated sides) of length $L$ and diffusivity $c^2$:
$$u_t=c^2u_{xx},\quad 0<x<L,\ t>0,\qquad u(x,0)=f(x),\ \text{plus a condition at each end.}$$

## Solution for the standard end conditions
$u=X(x)T(t)$ gives $X''+p^2X=0$ and $T'=-c^2p^2T$, so $T=e^{-c^2p^2t}$: **each mode decays**.

| Ends | $u(x,t)$ | Coefficients |
|---|---|---|
| both at 0°: $u(0,t)=u(L,t)=0$ | $\sum b_n\sin\frac{n\pi x}Le^{-c^2n^2\pi^2t/L^2}$ | $b_n=\frac2L\int_0^Lf\sin\frac{n\pi x}L$ |
| both insulated: $u_x=0$ | $A_0+\sum A_n\cos\frac{n\pi x}Le^{-c^2n^2\pi^2t/L^2}$ | $A_0=\frac1L\int f$ (the mean), $A_n=\frac2L\int f\cos\frac{n\pi x}L$ |
| $u(0,t)=0$, other end loses heat ($u_x+hu=0$ at $L$) | $\sum B_n\sin p_nx\,e^{-c^2p_n^2t}$ | $\tan p_nL=-p_n/h$; $B_n=\frac{\int f\sin p_nx}{\int\sin^2p_nx}$ |

![[DE-PDE-heat.png]]
**Figure:** left, a triangular profile on a rod with ends at 0° smooths and cools, the high modes dying first ($e^{-n^2\pi^2c^2t/L^2}$); right, a rod with ends held at 90° and 60° relaxes to the linear steady state.

## Why it works
Diffusion damps a mode of wavenumber $p$ at rate $c^2p^2$: fine structure disappears fast, the long-wavelength mode lasts longest. As $t\to\infty$ the solution tends to the lowest surviving mode (decaying to 0° for Dirichlet ends, to the **mean** temperature for insulated ends). Only **one** initial condition is needed (first order in $t$), unlike the wave equation.

## Non-homogeneous boundary conditions: subtract the steady state
Separation of variables needs homogeneous conditions. If $u(0,t)=A$, $u(L,t)=B$ (constants), write
$$u(x,t)=w(x)+v(x,t),\qquad w''=0,\ w(0)=A,\ w(L)=B\ \Rightarrow\ w(x)=A+\frac{B-A}{L}x.$$
Then $v$ solves the heat equation with $v(0,t)=v(L,t)=0$ and $v(x,0)=f(x)-w(x)$: expand in sine series.
- **Ends suddenly changed** (rod at steady state $A_1,B_1$, then ends set to $A_2,B_2$): $w$ is the **new** steady state and $v(x,0)=(\text{old steady state})-w$.
- **Ends suddenly insulated** after steady state: the new condition is $u_x=0$; the long-time temperature is the mean of the old linear profile.
- **Flux condition** $u_x(L,t)=1$ and $u_x(0,t)=0$ (heat flux in): $w=\frac{x^2}{2L}+\frac{c^2t}L$, which satisfies $w_t=c^2w_{xx}$, $w_x(0)=0$, $w_x(L)=1$; then $v$ has insulated ends.

**Worked example** ($u_t=u_{xx}$, $u(0,t)=90$, $u(10,t)=60$, $u(x,0)=5x+50$): $w=90-3x$, $v(x,0)=8x-40$, $c_n=\frac{2}{10}\int_0^{10}(8x-40)\sin\frac{n\pi x}{10}dx=\frac{80}{n\pi}\big[(-1)^{n+1}-1\big]$, so
$$u=90-3x+\sum_{n\ge1}\frac{80}{n\pi}\big[(-1)^{n+1}-1\big]\sin\tfrac{n\pi x}{10}\,e^{-n^2\pi^2t/100}.$$

## Method
1. Make the boundary conditions homogeneous (subtract $w$) if they are not.
2. Pick the eigenfunctions from the table; write $T=e^{-c^2p_n^2t}$.
3. Expand $f-w$ in the eigenfunctions (sine, cosine or Robin series).
4. Sanity check: $t\to\infty$ should give $w$ (plus the mean, if insulated), and $t=0$ the data.

> [!warning] Traps
> - Adding the steady state $w$ to the **initial** condition instead of subtracting it ($v(x,0)=f-w$).
> - For insulated ends, forgetting the constant mode $A_0$ (the mean).
> - Using $u_x(L,t)=1$ as if it were homogeneous: it is not, so $w$ must supply it.
> - Initial data not compatible with the boundary values (a jump at the end) is fine mathematically, but the series converges slowly (Gibbs) near that end.

## Cross-domain links
- [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]] — mode $n$ is a first-order lag with time constant $\tau_n=L^2/(c^2n^2\pi^2)$: $\tau_n\propto1/n^2$, so the slowest mode (n = 1) sets the cooling time. Compare the lumped model of [[Heat Transfer - MOC]] (one exponential) with the distributed model here (a series of exponentials).
- [[First-Order AC Transients (RC and RL)]] — an RC line (diffusion along a cable) obeys exactly this equation.

---
title: Laplace Equation on Rectangles and Strips
tags: [differential-equations, pdes, concept, laplace-equation, harmonic-functions, steady-state]
source: "[[Lecture-36.pdf]], [[A10-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Separation of Variables]] · [[Laplace Equation in Polar Coordinates]] · [[Heat Equation - Separation of Variables]] · [[Sturm-Liouville Problems]] · solved in [[Assignment 10 - Laplace Equations - Solutions]] Q2–Q7

## What it is
The **Laplace equation** $\nabla^2u=u_{xx}+u_{yy}=0$ governs steady-state temperature, electrostatic potential, ideal-flow potential and membrane height. Solutions are **harmonic functions**.

- **Dirichlet problem:** $u$ prescribed on the boundary. **Neumann problem:** $\partial u/\partial n$ prescribed (solution unique up to a constant, and the net flux must vanish).
- **Maximum principle:** a harmonic function on a bounded region attains its maximum and minimum on the boundary.
- **Uniqueness:** two Dirichlet solutions differ by a harmonic function that is $0$ on the boundary, hence $0$.

## Solution on a rectangle $0<x<a$, $0<y<b$
$u=X(x)Y(y)$ gives $X''+p^2X=0$, $Y''-p^2Y=0$. With zero on the sides $x=0,a$: $X_n=\sin\frac{n\pi x}a$, $p_n=\frac{n\pi}a$ and
$$Y_n=C\cosh p_ny+D\sinh p_ny\quad(\text{not oscillatory in }y).$$
**Choose the combination that vanishes on the opposite edge.** For data $u(x,0)=f_1(x)$ and $u(x,b)=0$:
$$u=\sum_nD_n\sin\tfrac{n\pi x}a\,\sinh\tfrac{n\pi(b-y)}a,\qquad D_n\sinh\tfrac{n\pi b}a=\frac2a\int_0^af_1\sin\tfrac{n\pi x}a\,dx.$$
Similarly for data on $y=b$: $\sinh\frac{n\pi y}a$; on $x=0$ or $x=a$: swap the roles of $x,y$.

**Several hot edges:** the problem is linear, so solve **four** problems, each with one non-zero edge and the other three at zero, and add them.

![[DE-PDE-laplace.png]]
**Figure:** left, two hot edges (A10 Q2(b)) by superposition; centre, the semi-infinite strip; right, a disk ([[Laplace Equation in Polar Coordinates]]).

**Example (edge profile has a single mode).** $u(x,1)=\sin\pi x$, other three edges 0: $u=\dfrac{\sinh\pi y}{\sinh\pi}\sin\pi x$, one term.

## Other boundary conditions
- **Insulated side** ($u_x=0$): use $\cos\frac{n\pi x}a$ (and $n=0$: $u$ linear in $y$ or constant). E.g. insulated sides and bottom edge $u(x,0)=x$ on $0<x<\pi$, top insulated: $u=\frac{c_0}2+\sum c_n\cos nx\cosh n(y-\pi)$, $c_n=\frac{2[(-1)^n-1]}{n^2\pi\cosh n\pi}$. The $y$-factor is chosen to have **zero slope** at the insulated top.
- **Insulated far edge on $x=1$:** $\cosh n\pi(x-1)$ has zero slope at $x=1$.

## Semi-infinite strip $0<x<L$, $0<y<\infty$
Boundedness as $y\to\infty$ removes the growing exponential: $Y_n=e^{-n\pi y/L}$, so
$$u=\sum D_n\sin\tfrac{n\pi x}Le^{-n\pi y/L},\qquad D_n=\frac2L\int_0^Lu(x,0)\sin\tfrac{n\pi x}L\,dx.$$
Mode $n$ dies like $e^{-n\pi y/L}$: far from the heated edge only the first term survives. With insulated sides the eigenfunctions are $\cos\frac{n\pi x}L$ and the $n=0$ mode is a constant (a term linear in $y$ is unbounded and is dropped), so $u\to$ the **mean** of the edge data as $y\to\infty$. The requirement $u\to0$ then only makes sense when that mean is zero, as in $u(x,0)=2\cos\frac{3\pi x}L+3\cos\frac{4\pi x}L$, which gives $u=2\cos\frac{3\pi x}Le^{-3\pi y/L}+3\cos\frac{4\pi x}Le^{-4\pi y/L}$.

## Why it works
$\sinh$/$\cosh$ appear because the sign of the separation constant is opposite to the wave and heat cases: the equation is elliptic, solutions are determined by the boundary as a whole and **not** by marching in $y$. Large-$n$ modes are strongly damped away from the edge, which is why harmonic functions are smooth in the interior even when the boundary data have corners.

## Method
1. Draw the rectangle, mark which edges are non-zero. Split into one-edge problems.
2. For each, choose $X_n$ from the side conditions, build $Y_n$ to vanish (or have zero slope) on the opposite edge.
3. Fit the edge data by a Fourier series (note symmetries: a tent gives $\frac{8H}{n^2\pi^2}\sin\frac{n\pi}2$).
4. Add the problems.

> [!warning] Traps
> - Using $\sin(ny)$ in $y$ (that is the wave/heat case). In $y$ it is $\sinh$ or $\cosh$.
> - Writing $\sinh\frac{n\pi y}a$ for data on the **bottom** edge: it vanishes there. Use $\sinh\frac{n\pi(b-y)}a$.
> - Compatibility: a Neumann problem needs zero net flux through the boundary.

## Cross-domain links
- [[Conservation Laws and Flow Networks]] — steady heat flow, electrostatics and ideal fluid flow are all the same equation, with potential $\leftrightarrow$ temperature $\leftrightarrow$ voltage and flux $\leftrightarrow$ current.
- [[Heat Equation - Separation of Variables]] — the steady state of the heat equation ($u_t=0$) is Laplace: the transient decays and what is left solves $\nabla^2u=0$.

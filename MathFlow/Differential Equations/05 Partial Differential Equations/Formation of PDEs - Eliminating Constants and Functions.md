---
title: Formation of PDEs – Eliminating Constants and Functions
tags: [differential-equations, pdes, concept, first-order-pde]
source: "[[Lecture-31.pdf]], [[A8-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Partial Differential Equations - Definitions and Direct Integration]] · [[Lagrange's Method for Quasi-linear PDEs]] · [[Complete, General and Singular Integrals]] · solved in [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]] Q1

## What it is
A family of surfaces can be described by a PDE: eliminate the family's **arbitrary constants** or **arbitrary functions** by differentiating. This is the reverse of solving, and it shows what the general solution of a PDE looks like. (Compare ODEs: $y=cx^2$ eliminates $c$ to give $xy'=2y$.)

## Eliminating arbitrary constants
For $f(x,y,u,a,b)=0$ differentiate with respect to $x$ and $y$ (chain rule through $u$):
$$f_x+f_up=0,\qquad f_y+f_uq=0,$$
then eliminate $a,b$ among the three equations. With $k$ constants and $n=2$ independent variables:

| $k$ vs $n$ | Result |
|---|---|
| $k=n$ | one first-order PDE (usually nonlinear) |
| $k>n$ | need second derivatives: a PDE of order 2 or more |
| $k<n$ | several first-order PDEs possible |

| Family | PDE |
|---|---|
| $u=(x^2+a)(y^2+b)$ | $pq=4xyu$ |
| $u=ax+by+ab$ | $u=px+qy+pq$ (Clairaut) |
| $(x-a)^2+(y-b)^2+u^2=1$ | $u^2(p^2+q^2+1)=1$ |
| $u=(x-a)^2+(y-b)^2$ | $p^2+q^2=4u$ |
| spheres with centre on the $u$-axis | $yp-xq=0$ (linear, though the family is not) |

## Eliminating an arbitrary function
Let $\varphi=\varphi(x,y,u)$, $\psi=\psi(x,y,u)$ be given and $G(\varphi,\psi)=0$ with $G$ arbitrary. Differentiating,
$$G_\varphi(\varphi_x+\varphi_up)+G_\psi(\psi_x+\psi_up)=0,\qquad G_\varphi(\varphi_y+\varphi_uq)+G_\psi(\psi_y+\psi_uq)=0.$$
This is a homogeneous linear system in $(G_\varphi,G_\psi)$, so the determinant must vanish. The $pq$ terms cancel, and the result is **quasi-linear**:
$$\frac{\partial(\varphi,\psi)}{\partial(y,u)}\,p+\frac{\partial(\varphi,\psi)}{\partial(u,x)}\,q=\frac{\partial(\varphi,\psi)}{\partial(x,y)}.$$
**Eliminating one arbitrary function always gives a quasi-linear first-order PDE.** Lagrange's method ([[Lagrange's Method for Quasi-linear PDEs]]) reverses exactly this step.

| Relation | PDE |
|---|---|
| $u=f(x^2+y^2)$ | $yp-xq=0$ (surfaces of revolution) |
| $u=x^nf(y/x)$ | $xp+yq=nu$ (Euler's relation, homogeneous of degree $n$) |
| $u=e^{mx}f(x+y)$ | $p-q=mu$ |
| $G(xy+u^2,\,x+y+u)=0$ | $(2u-x)p+(y-2u)q=x-y$ |
| $xyu=f(x+y+u)$ | $x(y-u)p+y(u-x)q=u(x-y)$ |
| $G(x+y+u,\,x^2+y^2-u^2)=0$ | $(y+u)p-(x+u)q=x-y$ |
| $u=f(x-ct)$ | $u_t+cu_x=0$ (transport) |
| $u=f(x+ct)+g(x-ct)$ | $u_{tt}=c^2u_{xx}$ (wave, two functions, second order) |
| $u=f(x+iy)+g(x-iy)$ | $u_{xx}+u_{yy}=0$ (Laplace) |

Rule of thumb: **$k$ arbitrary functions lead to a PDE of order $k$**.

## Method
1. Decide what is arbitrary (constants or a function) and count it against the number of independent variables.
2. Differentiate with respect to each independent variable, using the chain rule for arguments of $f$ (a common slip is $f'(x+y)$ with a missing factor).
3. Eliminate: for functions, divide the two equations to remove $f'$ (or use the determinant).
4. Simplify and check the class of the result.

**Example ($u=x^nf(y/x)$).** $p=nx^{n-1}f-x^{n-2}yf'$, $q=x^{n-1}f'$. Then $xp=nx^nf-x^{n-1}yf'=nu-yq$, so $xp+yq=nu$. ✓

> [!warning] Trap
> $u=f(x+y)\,g(x-y)$ has *two* arbitrary functions: expect a second-order PDE, not first order.

## Cross-domain links
- [[Cauchy-Euler Equations]] — $xp+yq=nu$ is the PDE version of the Euler equation: homogeneous functions are the eigenfunctions of the Euler operator $x\partial_x+y\partial_y$ with eigenvalue $n$.
- [[Exact Differential Equations]] — the first integrals of a characteristic system play the role of the potential $F$ with $F_x=M$, $F_y=N$.

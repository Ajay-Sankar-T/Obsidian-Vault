---
title: Separation of Variables
tags: [differential-equations, pdes, concept, separation-of-variables, eigenvalue-problem]
source: "[[Lecture-34.pdf]], [[A9-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Sturm-Liouville Problems]] · [[Wave Equation on a Finite Interval]] · [[Heat Equation - Separation of Variables]] · [[Laplace Equation on Rectangles and Strips]] · solved in [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]] Q3

## What it is
Look for solutions of a **linear homogeneous** PDE in **product form** $u(x,y)=X(x)Y(y)$. If the PDE can be written with $x$-terms on one side and $y$-terms on the other,
$$\frac{X'}{X}\ \text{(or }\tfrac{X''}{X})=\frac{\text{function of }y}{Y}=\lambda\quad(\text{a constant}),$$
the PDE splits into two ODEs joined by the **separation constant** $\lambda$. The solutions for admissible $\lambda_n$ are added (superposition), and the extra data fix the coefficients.

## Why it works
The operator and the boundary conditions are linear and homogeneous, so products of eigenfunctions of the spatial part are solutions and so is their sum. The spatial ODE with its boundary conditions is a [[Sturm-Liouville Problems|Sturm–Liouville eigenproblem]]: it has solutions only for special $\lambda_n$, its eigenfunctions are orthogonal, and **any** initial or boundary profile can be expanded in them, which determines the coefficients.

## Method
1. Substitute $u=XY$ and separate. A step that does not separate means the method (in this form) fails.
2. Impose the **homogeneous** boundary conditions on the space factor to get the eigenproblem $X''+\lambda X=0$ with $\lambda_n,X_n$. (If the boundary conditions are not homogeneous, first subtract a simple function that satisfies them: [[Heat Equation - Separation of Variables]].)
3. Solve the other ODE for each $\lambda_n$.
4. Superpose: $u=\sum c_nX_nY_n$.
5. Fit the remaining data with an orthogonal expansion: $c_n=\dfrac{\langle f,X_n\rangle}{\langle X_n,X_n\rangle}$.

**Eigenproblems you will meet** ($X''+\lambda X=0$ on $[0,L]$, $\lambda=p^2$):

| Ends | Eigenfunctions $X_n$ | $p_n$ |
|---|---|---|
| fixed–fixed, $X(0)=X(L)=0$ | $\sin\frac{n\pi x}L$ | $\frac{n\pi}L,\ n\ge1$ |
| free–free, $X'(0)=X'(L)=0$ | $\cos\frac{n\pi x}L$ | $\frac{n\pi}L,\ n\ge0$ |
| fixed–free, $X(0)=X'(L)=0$ | $\sin\frac{(2n-1)\pi x}{2L}$ | $\frac{(2n-1)\pi}{2L},\ n\ge1$ |
| fixed–Robin, $X(0)=0$, $X'(L)+hX(L)=0$ | $\sin p_nx$ | roots of $\tan pL=-p/h$ |
| periodic on $[-L,L]$ | $\cos\frac{n\pi x}L,\ \sin\frac{n\pi x}L$ | $\frac{n\pi}L$ |

Only $\lambda>0$ gives oscillatory $X$ for these problems (check $\lambda<0$ and $\lambda=0$ separately: $\lambda=0$ survives only for free–free and periodic).

## First-order examples
- $y^3u_x+x^2u_y=0$: $\frac{X'}{x^2X}=-\frac{Y'}{y^3Y}=k$ gives $X=e^{kx^3/3}$, $Y=e^{-ky^4/4}$. With $u(x,0)=e^{x^3/3}$: $k=1$, $u=e^{x^3/3-y^4/4}$.
- $u_x=2u_t+u$: $\frac{X'}X=\lambda$, $T=e^{(\lambda-1)t/2}$; data $6e^{-3x}$ gives $\lambda=-3$, $u=6e^{-3x-2t}$.
- $u_{xx}=u_y+2u$ with $u(0,y)=0$, $u_x(0,y)=1+e^{-3y}$: $X''=\lambda X$, $Y=e^{(\lambda-2)y}$: the $e^{0\cdot y}$ term needs $\lambda=2$ ($X=\frac1{\sqrt2}\sinh\sqrt2x$) and $e^{-3y}$ needs $\lambda=-1$ ($X=\sin x$): $u=\frac1{\sqrt2}\sinh\sqrt2x+e^{-3y}\sin x$.

> [!warning] Traps
> - Superposing before imposing the boundary conditions, or forgetting that **non-homogeneous** conditions break superposition of the *boundary* data.
> - Dropping $\lambda\le0$ without checking them; with Neumann or periodic ends $\lambda=0$ is a genuine eigenvalue (a constant mode).
> - Taking the product ansatz on a region whose boundary is not a coordinate line (use polar coordinates for a disk).

## Cross-domain links
- [[Eigenvalues, Rotation and Diagonalization Everywhere]] — separation of variables is diagonalisation: each eigenfunction is an independent mode that evolves on its own (wave: oscillates; heat: decays; Laplace: grows or decays in $y$).
- [[Resonance and Buckling - Instability as an Eigenvalue Problem]] — same eigenproblem $X''+\lambda X=0$ as the column buckling loads $P_n=n^2\pi^2EI/L^2$ ([[Euler Buckling of Columns]]).

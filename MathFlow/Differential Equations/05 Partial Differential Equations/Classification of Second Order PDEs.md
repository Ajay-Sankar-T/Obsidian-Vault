---
title: Classification of Second Order PDEs
tags: [differential-equations, pdes, concept, classification, hyperbolic, parabolic, elliptic]
source: "[[Lecture-33.pdf]], [[A8-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Canonical Forms of Second Order PDEs]] · [[D'Alembert's Solution of the Wave Equation]] · [[Separation of Variables]] · solved in [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]] Q4, Q6(e)

## What it is
A second-order linear PDE in two variables,
$$a\,u_{xx}+b\,u_{xy}+c\,u_{yy}+d\,u_x+e\,u_y+f\,u=g\qquad(a,b,c,\dots\text{ functions of }x,y),$$
has a **type** set by the discriminant of its principal part:

| $b^2-4ac$ | Type | Model | Behaviour |
|---|---|---|---|
| $>0$ | **hyperbolic** | $u_{tt}=c^2u_{xx}$ | waves, finite speed, two real characteristic families |
| $=0$ | **parabolic** | $u_t=ku_{xx}$ | diffusion, one characteristic family |
| $<0$ | **elliptic** | $u_{xx}+u_{yy}=0$ | steady state, smoothing, no real characteristics |

The classes need different boundary data: hyperbolic and parabolic equations are **initial-value** (evolution) problems, elliptic equations are **boundary-value** problems.

## Why the discriminant
The type is the character of the quadratic form $a\xi^2+b\xi\eta+c\eta^2$ (indefinite / semi-definite / definite). Under any change of variables $\xi=\xi(x,y)$, $\eta=\eta(x,y)$ with Jacobian $J\ne0$,
$$B^2-4AC=J^2\,(b^2-4ac),$$
so the sign cannot change: **the type is a property of the equation, not of the coordinates.** (Proof: the coefficient matrix transforms as $M'=\mathcal J\,M\,\mathcal J^{T}$ with $\mathcal J=\partial(\xi,\eta)/\partial(x,y)$, hence $\det M'=J^2\det M$ and $\det M=ac-b^2/4$.)

**Variable coefficients:** the type can differ from region to region. The Tricomi equation $y\,u_{xx}+u_{yy}=0$ has $b^2-4ac=-4y$: elliptic for $y>0$, parabolic on $y=0$, hyperbolic for $y<0$ (the equation of transonic flow).

Only the **highest-order terms** decide the type: $y\,u_{xx}+2u_{xy}+u_{yy}=u\,u_x+u_y^2$ has type given by $4-4y$ even though the right side is nonlinear.

## Characteristics
Solving $a\,dy^2-b\,dx\,dy+c\,dx^2=0$ gives the **characteristic curves**
$$\frac{dy}{dx}=\frac{b\pm\sqrt{b^2-4ac}}{2a}.$$
Real and distinct (hyperbolic), real and equal (parabolic), complex conjugate (elliptic). Across a characteristic the second derivatives of a solution are not determined by the data: discontinuities (wave fronts) propagate along characteristics.

## Method
1. Read $a,b,c$ from the **second-order terms** only.
2. Compute $\Delta=b^2-4ac$ as a function of $(x,y)$.
3. Solve $\Delta>0$, $\Delta=0$, $\Delta<0$ to get the regions; sketch them.

![[DE-PDE-classification-regions.png]]
**Figure:** the regions for six equations of Assignment 8, Q4: cones (b), a circle (c), (h), a half-plane (i), the quadrants (l), a parabola (m).

| Equation | $\Delta$ | Regions |
|---|---|---|
| $u_{xx}+(x-1)u_{xy}+u_{yy}$ | $(x-3)(x+1)$ | hyperbolic $x<-1$ or $x>3$; elliptic $-1<x<3$ |
| $y^2u_{xx}-x^2u_{yy}$ ($x,y>0$) | $4x^2y^2$ | hyperbolic everywhere |
| $x^2u_{xx}+2xyu_{xy}+y^2u_{yy}$ | $0$ | parabolic everywhere |
| $u_{xx}+x^2u_{yy}$ | $-4x^2$ | elliptic except on $x=0$ |
| $xu_{xx}+yu_{yy}$ | $-4xy$ | elliptic in quadrants I, III; hyperbolic in II, IV |
| $u_{xx}+yu_{xy}+xu_{yy}$ | $y^2-4x$ | hyperbolic left of $y^2=4x$, elliptic inside |

> [!warning] Traps
> - Using $b$ for the coefficient of $u_{xy}$, not of $u_x$.
> - Treating $u_{xy}$ and $u_{yx}$ as separate terms: the coefficient of $u_{xy}$ already includes both.
> - Quoting one type for the whole plane when the coefficients vary.

## Cross-domain links
- [[Eigenvalues, Rotation and Diagonalization Everywhere]] — the type is the signature of the symmetric matrix $\begin{pmatrix}a&b/2\\b/2&c\end{pmatrix}$: two eigenvalues of opposite sign (hyperbolic), one zero (parabolic), same sign (elliptic). It is the same classification as for conics (hyperbola, parabola, ellipse).
- [[Mohr's Circle for Stress]] — the same symmetric $2\times2$ matrix machinery: stress principal axes are its eigenvectors, and $B^2-4AC=J^2(b^2-4ac)$ says the determinant of such a matrix is multiplied by the positive factor $J^2$ under a change of basis, so its sign (the type) survives.

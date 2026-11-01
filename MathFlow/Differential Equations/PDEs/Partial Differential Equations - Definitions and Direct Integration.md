---
title: Partial Differential Equations – Definitions and Direct Integration
tags: [differential-equations, pdes, concept, classification]
source: "[[Lecture-30.pdf]]"
---

Related: [[PDEs - MOC]] · [[Formation of PDEs - Eliminating Constants and Functions]] · [[Classification of Second Order PDEs]] · [[Lagrange's Method for Quasi-linear PDEs]]

## What it is
A **partial differential equation** relates an unknown $u(x,y,\dots)$ of several variables to its partial derivatives. We write $p=u_x$, $q=u_y$. The **order** is the highest derivative present.

| Order | Example | What it models |
|---|---|---|
| 1 | $u_t+cu_x=0$ | transport at speed $c$ |
| 2 | $u_t=ku_{xx}$ | heat conduction |
| 2 | $u_{tt}=c^2u_{xx}$ | vibrating string |
| 2 | $u_{xx}+u_{yy}=0$ | steady heat, potential |
| 3 | $u_t+uu_x+u_{xxx}=0$ | shallow-water (KdV) waves |

## Classes of first-order PDE $F(x,y,u,p,q)=0$

| Class | Form | Test |
|---|---|---|
| **linear** | $a(x,y)p+b(x,y)q+c(x,y)u=d(x,y)$ | $u,p,q$ appear to the first power, no products |
| **semilinear** | $a(x,y)p+b(x,y)q=c(x,y,u)$ | coefficients of $p,q$ depend on $x,y$ only |
| **quasi-linear** | $a(x,y,u)p+b(x,y,u)q=c(x,y,u)$ | linear in $p,q$ |
| **nonlinear** | anything else, e.g. $p^2+q^2=1$, $pq=u$ | |

linear $\subset$ semilinear $\subset$ quasi-linear. A linear PDE with $d\equiv0$ is **homogeneous**; its solutions can be added. **Identify the class before choosing a method**: quasi-linear equations (all of the next four notes) yield to [[Lagrange's Method for Quasi-linear PDEs]].

**Classify:** $xp+yq=u$ linear homogeneous · $p+(x+y)q=5u+e^x$ linear non-homogeneous · $p+q=u^2$ semilinear · $up+q=0$ quasi-linear · $p^2+q^2=u^2$ nonlinear.

## A PDE has a whole family of solutions
$u=x^2+y^2$ satisfies $yu_x-xu_y=0$, and so do $\sin(x^2+y^2)$, $e^{x^2+y^2}$ and in fact $f(x^2+y^2)$ for any differentiable $f$. Constants of an ODE become **arbitrary functions**, and a general solution of an $n$-th order PDE typically contains $n$ of them. Initial or boundary data pick out one member.

## Solving by direct integration
Integrating with respect to one variable treats the others as constants, so the "constant" of integration is an arbitrary function of the remaining variables.

| PDE | Solution |
|---|---|
| $u_x=x+y$ | $u=\tfrac{x^2}2+xy+f(y)$ |
| $u_{xy}=0$ | $u=h(x)+g(y)$ |
| $u_{xx}=y^2\cos2x$, $u(0,y)=u(\pi/2,y)=0$ | $u=\tfrac{y^2}{4}\big(1-\cos2x-\tfrac{4x}{\pi}\big)$ |
| $u_x=u$ | $u=f(y)e^x$ |
| $u_{xy}=u_x$ (put $v=u_x$: $v_y=v$) | $u=e^{y}F(x)+G(y)$ |

**Worked example** ($u_{xx}=y^2\cos2x$ with the two boundary conditions): integrating twice gives $u=-\tfrac{y^2}{4}\cos2x+xf(y)+g(y)$. $u(0,y)=0\Rightarrow g=\tfrac{y^2}{4}$; $u(\pi/2,y)=0\Rightarrow\tfrac{y^2}{4}+\tfrac\pi2f+\tfrac{y^2}{4}=0\Rightarrow f=-\tfrac{y^2}{\pi}$. Check: $u_{xx}=y^2\cos2x$ ✓, both boundary values vanish ✓.

> [!warning] Trap
> Direct integration only works when the PDE can be integrated in one variable (a pure derivative in $x$ or $y$, or after a substitution like $v=u_x$). For $a p+bq=c$ with both derivatives present use characteristics.

## Cross-domain links
- [[First Order ODEs]] — the ODE method "integrate, add a constant" survives, but the constant becomes a function. Counting arbitrary functions replaces counting constants.
- [[Conservation Laws and Flow Networks]] — $u_t+cu_x=0$ is the simplest conservation law: a profile moves without changing shape.

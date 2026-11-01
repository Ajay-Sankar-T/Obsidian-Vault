---
title: Complete, General and Singular Integrals
tags: [differential-equations, pdes, concept, first-order-pde, clairaut]
source: "[[Lecture-31.pdf]], [[A8-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Formation of PDEs - Eliminating Constants and Functions]] · [[Lagrange's Method for Quasi-linear PDEs]] · solved in [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]] Q6(a)

## What it is
For $F(x,y,u,p,q)=0$ (any first-order PDE, linear or not) there are three kinds of solutions.

| Name | Meaning |
|---|---|
| **complete integral** | a two-parameter family $f(x,y,u,a,b)=0$ that satisfies the PDE for all $a,b$ and whose parameters are independent: $\operatorname{rank}\begin{pmatrix}u_a&p_a&q_a\\u_b&p_b&q_b\end{pmatrix}=2$ |
| **general integral** | put $b=h(a)$ with $h$ arbitrary, take the **envelope** of the one-parameter family: eliminate $a$ from $f(x,y,u,a,h(a))=0$ and $f_a+f_bh'(a)=0$ |
| **singular integral** | envelope of the full two-parameter family: eliminate $a,b$ from $f=0$, $f_a=0$, $f_b=0$ |

An envelope touches every member of the family, so it is again a solution. The number of parameters of the complete integral equals the number of independent variables.

## Why it works
A complete integral is a two-parameter family of surfaces, each a solution. Choosing a one-parameter sub-family and enveloping it produces new solutions, with the arbitrary function $h$. The singular integral touches all members of the family and is generally **not** obtained by any choice of $a,b$.

## Clairaut equation $u=px+qy+g(p,q)$
Complete integral by inspection: $u=ax+by+g(a,b)$ (these are planes). Singular integral: eliminate $a,b$ from $x+g_a=0$, $y+g_b=0$.

**Example.** $u=px+qy+pq$. Complete integral $u=ax+by+ab$. $\partial_a:\ 0=x+b$, $\partial_b:\ 0=y+a$, so $a=-y$, $b=-x$ and
$$\boxed{u=-xy}\ \text{(singular integral)}.$$
Check: $p=-y$, $q=-x$: $px+qy+pq=-xy-xy+xy=-xy$ ✓. It touches every plane of the family ($u=ax+by+ab$ is tangent to the saddle $u=-xy$ at $(-b,-a)$) but is not one of them.

Similarly $u=ax+by+a^2+b^2$ gives $u=px+qy+p^2+q^2$ with singular integral $u=-\frac{x^2+y^2}{4}$.

## Method (finding the singular integral)
1. Write the complete integral $f(x,y,u,a,b)=0$.
2. Differentiate with respect to $a$ and $b$ and set both to zero.
3. Eliminate $a,b$.
4. Check that the result really satisfies the PDE (the envelope may be spurious, e.g. a singular locus of the family).

> [!warning] Trap
> For the **quasi-linear** equations of [[Lagrange's Method for Quasi-linear PDEs]] the general solution $G(\varphi,\psi)=0$ already contains everything, there is no singular integral to find. Singular integrals matter for nonlinear first-order PDEs only.

## Cross-domain links
- [[First Order ODEs]] — Clairaut's ODE $y=xy'+g(y')$ has the same structure: a family of straight lines and an envelope solution (the singular solution).
- [[Energy Methods - A Unified View]] — an envelope of a family of tangent lines or planes is the geometric content of a Legendre transform.

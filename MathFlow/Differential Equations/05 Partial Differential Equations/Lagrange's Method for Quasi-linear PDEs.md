---
title: Lagrange's Method for Quasi-linear PDEs
tags: [differential-equations, pdes, concept, first-order-pde, characteristics]
source: "[[Lecture-31.pdf]], [[Lecture-32.pdf]], [[A8-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Formation of PDEs - Eliminating Constants and Functions]] · [[Cauchy Problem for First Order PDEs]] · [[Complete, General and Singular Integrals]] · solved in [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]] Q2, Q3

## What it is
For the quasi-linear equation
$$a(x,y,u)\,u_x+b(x,y,u)\,u_y=c(x,y,u)\qquad(\text{Lagrange's equation})$$
the PDE is turned into ODEs along curves called **characteristics**.

## Why it works
A solution $u=u(x,y)$ is a surface $S$ in $(x,y,u)$-space with normal $\mathbf n=(p,q,-1)$. The PDE says $(a,b,c)\cdot\mathbf n=ap+bq-c=0$: the vector $(a,b,c)$ is **tangent** to $S$ at every point. So integral surfaces are exactly the surfaces tangent to the direction field $(a,b,c)$, i.e. surfaces made of curves with direction $(a,b,c)$:
$$\boxed{\frac{dx}{a}=\frac{dy}{b}=\frac{du}{c}}\qquad\text{(Lagrange's auxiliary / characteristic equations)}$$
Along any curve on $S$, $du=p\,dx+q\,dy$; compare with $ap+bq=c$.

**Theorem.** If $\varphi(x,y,u)=c_1$ and $\psi(x,y,u)=c_2$ are two independent solutions (first integrals) of the auxiliary equations, the general solution is $G(\varphi,\psi)=0$, $G$ arbitrary (equivalently $\varphi=g(\psi)$). *Proof sketch:* $d\varphi=0$ along characteristics gives $a\varphi_x+b\varphi_y+c\varphi_u=0$ (the same for $\psi$), so $a:b:c$ equals the Jacobians $\frac{\partial(\varphi,\psi)}{\partial(y,u)}:\frac{\partial(\varphi,\psi)}{\partial(u,x)}:\frac{\partial(\varphi,\psi)}{\partial(x,y)}$, which is exactly the PDE obtained by eliminating $G$ ([[Formation of PDEs - Eliminating Constants and Functions]]).

**Check any first integral** by testing $a\varphi_x+b\varphi_y+c\varphi_u\equiv0$.

## Procedure
1. Write the PDE as $ap+bq=c$.
2. Write $\dfrac{dx}a=\dfrac{dy}b=\dfrac{du}c$.
3. Find one first integral $\varphi=c_1$.
4. Find a second, independent $\psi=c_2$.
5. General solution $G(\varphi,\psi)=0$.

**Finding the integrals (steps 3–4):**

| Technique | Idea |
|---|---|
| **grouping** | equate two ratios that involve only two variables, integrate the resulting ODE |
| **grouping with substitution** | use $\varphi=c_1$ to eliminate a variable from a second pair, integrate, then put $c_1=\varphi$ back |
| **multipliers** | each ratio equals $\dfrac{l\,dx+m\,dy+n\,du}{la+mb+nc}$. If $la+mb+nc=0$ then $l\,dx+m\,dy+n\,du=0$, and if that is exact its integral is a first integral. Choose $(l,m,n)=(x,y,u)$, $(1,1,1)$, $(1/x,1/y,1/u)$, $(\varphi_x,\varphi_y,\varphi_u)$ as first tries |
| **eigenvalue (equivalent ratio) method** | for *linear* characteristic systems $\dot{\mathbf v}=M\mathbf v$ (a, b, c linear in $x,y,u$): a left eigenvector $\boldsymbol\ell$ of $M$ gives $d(\boldsymbol\ell\cdot\mathbf v)=\lambda(\boldsymbol\ell\cdot\mathbf v)\,dt$, so ratios such as $(\boldsymbol\ell_2\cdot\mathbf v)/(\boldsymbol\ell_1\cdot\mathbf v)^{\lambda_2/\lambda_1}$ are constant. Complex eigenvalues give $\arctan$ and $\ln$ terms |

## Worked examples
- $ux+uy=1$ is $a=b=c=1$: $x-y=c_1$, $u-y=c_2$, so $u=y+g(x-y)$.
- $xp+yq=u$: $y/x=c_1$, $u/x=c_2$, so $u=x\,g(y/x)$ (homogeneous of degree 1).
- $x^2p+y^2q=(x+y)u$: $\frac1x-\frac1y=c_1$; subtract the first two ratios, $\frac{d(x-y)}{x-y}=\frac{du}u$, so $\frac{x-y}{u}=c_2$.
- $(y-u)p+(u-x)q=x-y$: multipliers $(1,1,1)$ and $(x,y,u)$ both give zero denominators, so $x+y+u=c_1$ and $x^2+y^2+u^2=c_2$ (surfaces of revolution about the line $x=y=u$).
- $(x+y-u)p+(y+u-x)q=u+x-y$: the system is $\dot{\mathbf v}=M\mathbf v$ with $M=I+N$, $N$ skew. The eigenvalues are $1$ and $1\pm i\sqrt3$, so integrals involve $\arctan$ and $\ln(x+y+u)$ (A8 Q2(y)).

![[DE-PDE-characteristics.png]]
**Figure:** left, characteristic base curves for $u_x+2xu_y=y$ (each curve carries its own ODE for $u$); right, a data curve that *is* a characteristic ([[Cauchy Problem for First Order PDEs]]).

> [!warning] Traps
> - The second integral from "substitution" must have $c_1$ replaced by $\varphi$ at the end, or it is not a function of $x,y,u$ only.
> - Two first integrals must be **independent** (Jacobian of rank 2), not e.g. $\varphi$ and $\varphi^2$.
> - Any pair of ratios that is not independent of the third variable cannot be integrated alone: use multipliers or substitution.

## Cross-domain links
- [[Exact Differential Equations]] — a first integral is a potential for the 1-forms $l\,dx+m\,dy+n\,du$.
- [[Eigenvalues, Rotation and Diagonalization Everywhere]] — the eigenvalue method is diagonalising the characteristic flow: a skew part rotates (arctan), the symmetric part grows or decays.
- [[Conservation Laws and Flow Networks]] — $u_t+c(u)u_x=0$ is a conservation law; its characteristics are the particle paths of the flow.

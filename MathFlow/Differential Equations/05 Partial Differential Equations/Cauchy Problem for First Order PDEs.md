---
title: Cauchy Problem for First Order PDEs
tags: [differential-equations, pdes, concept, first-order-pde, characteristics, cauchy-problem]
source: "[[Lecture-32.pdf]], [[A8-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Lagrange's Method for Quasi-linear PDEs]] · [[Formation of PDEs - Eliminating Constants and Functions]] · solved in [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]] Q3, Q6

## What it is
The **Cauchy problem** asks for the integral surface of $a\,p+b\,q=c$ that contains a given space curve
$$\Gamma:\ x=x_0(s),\ y=y_0(s),\ u=u_0(s)$$
(equivalently, $u$ is prescribed on a curve in the $xy$-plane). The general solution $G(\varphi,\psi)=0$ has one arbitrary function; the data fix it.

## Method
1. Find the two first integrals $\varphi=c_1$, $\psi=c_2$ ([[Lagrange's Method for Quasi-linear PDEs]]).
2. Put the curve in: $c_1=\varphi(x_0(s),y_0(s),u_0(s))$, $c_2=\psi(x_0(s),y_0(s),u_0(s))$.
3. Eliminate $s$ to get one relation $H(c_1,c_2)=0$.
4. Replace $c_1=\varphi(x,y,u)$, $c_2=\psi(x,y,u)$: $H(\varphi,\psi)=0$ is the integral surface; solve for $u$ if possible.

(Equivalent view: the surface is the union of the characteristics through the points of $\Gamma$.)

**Example.** $u_x+2xu_y=y$, $u(0,y)=y^2$. Integrals: $y-x^2=c_1$ and $u-c_1x-\tfrac{x^3}3=c_2$. On $x=0$: $c_1=s$, $c_2=s^2$, so $c_2=c_1^2$:
$$u=(y-x^2)^2+x(y-x^2)+\tfrac{x^3}3=(y-x^2)^2+xy-\tfrac23x^3.$$

**Example (quasi-linear, nonlinear solution).** $uu_x+u_y=0$, $u(x,0)=x$: integrals $u=c_1$, $x-uy=c_2$; data give $c_2=c_1$, so $x-uy=u$ and $u=\dfrac{x}{1+y}$ (the inviscid Burgers equation with a linear profile).

## When the Cauchy problem is solvable
The characteristic base curves must cross the projection of $\Gamma$ **transversally**:
$$a\,\dot y_0-b\,\dot x_0\ne0\quad\text{along }\Gamma.$$
- If $\Gamma$ is nowhere characteristic: exactly one solution (locally).
- If $\Gamma$ **is** a characteristic and $u_0$ is compatible with the characteristic ODE: **infinitely many** solutions (any surface through the characteristic).
- If $\Gamma$ is a characteristic and the data are *not* compatible: **no** solution.

**Worked pair.** $u_x+u_y=1$: characteristics have direction $(1,1,1)$. Data $u=x$ on $y=x$ is the curve $(s,s,s)$, itself a characteristic: every $u=x+g(x-y)$ with $g(0)=0$ works. Data $u=0$ on $y=x$ would need $u$ to grow like $x$ along the characteristic: impossible. Geometrically the two data curves lie along the tangent direction, so they cannot determine a transverse surface.

**Example (surfaces of revolution).** $y\,u_x-x\,u_y=0$ has $u=f(x^2+y^2)$, whose characteristics are circles $x^2+y^2=$ const at constant $u$. Data on a circle (e.g. $u=1$ on $x^2+y^2=4$) is a characteristic: not unique ($u=1$, $u=\frac{x^2+y^2}4$, … all work). Data on the line $x=0$, $u=y^2$ crosses every circle (twice, symmetric: needs $u_0$ even): unique, $u=x^2+y^2$.

![[DE-PDE-characteristics.png]]

> [!warning] Traps
> - Forgetting that the data curve may meet one characteristic **twice** (the circle example): the data must agree at both points, otherwise there is no solution.
> - The solution may exist only locally: for $u_x+u_y=u^2$, $u(x,0)=\cos x$ gives $u=\dfrac{\cos(x-y)}{1-y\cos(x-y)}$, which blows up where $y\cos(x-y)=1$.

## Intersection of integral surfaces
If two integral surfaces meet transversally along a curve $C$, then $C$ is a characteristic: both tangent planes contain $(a,b,c)$, and two distinct planes meet in exactly that line. So two different solutions can only branch apart along characteristics.

## Cross-domain links
- [[Conservation Laws and Flow Networks]] — characteristics carry information: data are transported along them, and the $a\dot y-b\dot x\ne0$ condition is "the initial curve is not a streamline".
- [[Classification of Second Order PDEs]] — the same idea reappears: characteristics are the curves along which second derivatives can jump.

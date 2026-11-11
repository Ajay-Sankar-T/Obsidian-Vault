---
title: Canonical Forms of Second Order PDEs
tags: [differential-equations, pdes, concept, canonical-form, characteristics]
source: "[[Lecture-33.pdf]], [[A8-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Classification of Second Order PDEs]] · [[D'Alembert's Solution of the Wave Equation]] · [[Lagrange's Method for Quasi-linear PDEs]] · solved in [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]] Q5, Q6

## What it is
A change of independent variables $\xi=\xi(x,y)$, $\eta=\eta(x,y)$ that reduces $a\,u_{xx}+b\,u_{xy}+c\,u_{yy}+\dots=g$ to its simplest form:

| Type | Canonical form |
|---|---|
| hyperbolic | $u_{\xi\eta}=\Phi(\xi,\eta,u,u_\xi,u_\eta)$ (or equivalently $u_{\xi\xi}-u_{\eta\eta}=\dots$) |
| parabolic | $u_{\eta\eta}=\Phi(\xi,\eta,u,u_\xi,u_\eta)$ |
| elliptic | $u_{\xi\xi}+u_{\eta\eta}=\Phi(\xi,\eta,u,u_\xi,u_\eta)$ |

The goal: integrate the reduced equation, or recognise it as a known one (e.g. $u_{\xi\eta}=0$ gives $u=f(\xi)+g(\eta)$).

## Transformation rules
With $u(x,y)=w(\xi,\eta)$ the chain rule gives $u_{xx}=w_{\xi\xi}\xi_x^2+2w_{\xi\eta}\xi_x\eta_x+w_{\eta\eta}\eta_x^2+w_\xi\xi_{xx}+w_\eta\eta_{xx}$ and similarly for $u_{xy},u_{yy}$. The new coefficients are
$$A=a\xi_x^2+b\xi_x\xi_y+c\xi_y^2,\quad B=2a\xi_x\eta_x+b(\xi_x\eta_y+\xi_y\eta_x)+2c\xi_y\eta_y,\quad C=a\eta_x^2+b\eta_x\eta_y+c\eta_y^2,$$
$$D=a\xi_{xx}+b\xi_{xy}+c\xi_{yy}+d\xi_x+e\xi_y\ (\text{coefficient of }w_\xi),\quad E\ \text{likewise with }\eta.$$
**To kill $w_{\xi\xi}$ take $\xi$ with $A=0$**, i.e. $a\xi_x^2+b\xi_x\xi_y+c\xi_y^2=0$: $\xi=$ const is an integral curve of the characteristic equation $a\,dy^2-b\,dx\,dy+c\,dx^2=0$ (see [[Classification of Second Order PDEs]]).

## The three recipes
Solve $\dfrac{dy}{dx}=\dfrac{b\pm\sqrt{b^2-4ac}}{2a}$ (if $a=0$ swap the roles of $x,y$).

| Type | Characteristics | New variables | Result |
|---|---|---|---|
| **hyperbolic** | two real families $\varphi_1=c_1$, $\varphi_2=c_2$ | $\xi=\varphi_1$, $\eta=\varphi_2$ | $A=C=0$, divide by $B$: $u_{\xi\eta}+\dots$ |
| **parabolic** | one family $\varphi=c$ (double root $dy/dx=b/2a$) | $\xi=\varphi$, $\eta=$ any function independent of $\xi$ (e.g. $x$ or $y$) | $A=B=0$, divide by $C$: $u_{\eta\eta}+\dots$ |
| **elliptic** | complex pair $\varphi=\alpha\pm i\beta=c$ | $\xi=\alpha$, $\eta=\beta$ (real and imaginary parts) | $A=C$, $B=0$: $u_{\xi\xi}+u_{\eta\eta}+\dots$ |

## Method
1. Classify; solve the characteristic ODE; build $\xi,\eta$.
2. Compute $A,B,C,D,E$ (the formulas above) and **express them in $\xi,\eta$** (invert $x=x(\xi,\eta)$, $y=y(\xi,\eta)$).
3. Divide by the leading coefficient; write the canonical form.
4. Integrate it if possible: $u_{\xi\eta}=0\Rightarrow f(\xi)+g(\eta)$; $u_{\eta\eta}=0\Rightarrow\eta f(\xi)+g(\xi)$; $u_{\eta\eta}+\kappa u_\eta=0\Rightarrow f(\xi)+g(\xi)e^{-\kappa\eta}$.
5. Substitute back $\xi(x,y)$, $\eta(x,y)$.

## Examples
- **Constant coefficients, hyperbolic** $3u_{xx}+10u_{xy}+3u_{yy}=0$: $dy/dx=3$ or $\frac13$; $\xi=y-3x$, $\eta=3y-x$: $u_{\xi\eta}=0$, $u=f(y-3x)+g(3y-x)$.
- **Parabolic** $u_{xx}+2u_{xy}+u_{yy}=0$: $\xi=x-y$, $\eta=x$: $u_{\eta\eta}=0$, $u=f(x-y)+x\,g(x-y)$.
- **Elliptic** $u_{xx}+2u_{xy}+17u_{yy}=0$: $dy/dx=1\pm4i$, $\xi=y-x$, $\eta=4x$: $u_{\xi\xi}+u_{\eta\eta}=0$ (harmonic in $(\xi,\eta)$), so $u=F\big(y+(-1+4i)x\big)+G\big(y+(-1-4i)x\big)$.
- **Variable coefficients, hyperbolic** $u_{xx}-y^4u_{yy}=2y^3u_y$ ($y\ne0$): $dy/dx=\pm y^2$, $\xi=x+\frac1y$, $\eta=x-\frac1y$: $u_{\xi\eta}=0$ (the first-order term is exactly what makes this integrable), $u=f(x+\tfrac1y)+g(x-\tfrac1y)$.
- **Euler operator** $x^2u_{xx}+2xyu_{xy}+y^2u_{yy}+xu_x+yu_y=0$ is $(x\partial_x+y\partial_y)^2u=0$: $\xi=y/x$, $\eta=\ln x$, $u_{\eta\eta}=0$, $u=f(y/x)+g(y/x)\ln x$.
- **Hyperbolic with non-integrable first-order terms**: $u_{xx}+y\,u_{yy}=0$, $y<0$ gives $u_{\xi\eta}+\dfrac{u_\xi-u_\eta}{2(\xi-\eta)}=0$ (Euler–Poisson–Darboux form), not solvable by elementary means; $y\,u_{xx}+u_{yy}=0$ (Tricomi) gives $u_{\xi\eta}-\dfrac{u_\xi-u_\eta}{6(\xi-\eta)}=0$ for $y<0$ and $u_{\xi\xi}+u_{\eta\eta}+\dfrac{u_\eta}{3\eta}=0$ for $y>0$.

**Removing first-order terms** (constant coefficients): $u=v\,e^{\lambda\xi+\mu\eta}$ in $u_{\xi\eta}-4u_\xi+u_\eta+3u=0$ gives $v_{\xi\eta}+(\mu-4)v_\xi+(\lambda+1)v_\eta+(\lambda\mu-4\lambda+\mu+3)v=0$; choosing $\mu=4$, $\lambda=-1$ leaves $v_{\xi\eta}+7v=0$.

> [!warning] Traps
> - Dividing by $B$ **before** substituting $x,y$ in terms of $\xi,\eta$: the coefficients must be functions of $(\xi,\eta)$ in the answer.
> - Choosing $\eta$ not independent of $\xi$ in the parabolic case (the Jacobian must be non-zero).
> - Branches: $\sqrt{-y}$, $y^{3/2}$, $x^{3/2}$ need a sign convention. Solve in each region separately.

## Cross-domain links
- [[D'Alembert's Solution of the Wave Equation]] — $\xi=x+ct$, $\eta=x-ct$ turns $u_{tt}-c^2u_{xx}=0$ into $u_{\xi\eta}=0$: this *is* the canonical-form method.
- [[Eigenvalues, Rotation and Diagonalization Everywhere]] — a constant-coefficient canonical form is a diagonalisation of the principal-part matrix by a (generally non-orthogonal) change of coordinates.

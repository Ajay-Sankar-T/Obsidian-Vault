---
title: Assignment 10 – Laplace Equations (Solutions)
course: MA 2102 Differential Equations
assignment: 10
tags:
  - DE
  - assignment-solution
  - pdes
  - laplace-equation
  - separation-of-variables
  - polar-coordinates
source: "[[A10-2026.pdf]]"
concepts:
  - "[[Laplace Equation on Rectangles and Strips]]"
  - "[[Laplace Equation in Polar Coordinates]]"
  - "[[Separation of Variables]]"
aliases:
  - Laplace equation assignment solutions
  - Assignment 10 solutions
---

# Assignment 10 – Laplace Equations

Source: [[A10-2026.pdf]] · Theory: [[PDEs - MOC]] · Previous: [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]] · Index: [[Problems - MOC]]

> [!abstract] Contents
> [[#Q1]] · [[#Q2]] · [[#Q3]] · [[#Q4]] · [[#Q5]] · [[#Q6]] · [[#Q7]] · [[#Q8]] · [[#Q9]] · [[#Q10]] · [[#Summary]]

> [!info] Concept notes for this sheet
> | Questions | Concept note |
> |---|---|
> | Q2(a),(b), Q3–Q7 | [[Laplace Equation on Rectangles and Strips]] |
> | Q1, Q2(c),(d), Q8–Q10 | [[Laplace Equation in Polar Coordinates]] |
> | all | [[Separation of Variables]] · [[Sturm-Liouville Problems]] (the eigenfunctions) |

> [!warning] Points where the sheet needs care
> Coefficient formulas and closed forms were checked numerically or symbolically (`Tools/de_a9_a10.py`).
> - **Q8(a):** the boundary condition is printed $u(1,\theta)=10\cos2\theta$, whose harmonic extension is $10r^2\cos2\theta$. The sheet's answer $5(1+r^2\cos2\theta)$ is the solution for $u(1,\theta)=10\cos^2\theta$. Both are given below.
> - **Q8(b):** the printed series $\sum\frac{r^n}{2\pi n^2}\sin\frac{n\pi}2\sin n\theta$ does **not** reproduce the boundary data (at $r=1$, $\theta=0.5$ it sums to $0.062$ while the data equal $0.5$). The coefficients that do are derived below ($b_1=\frac2\pi$, $b_2=\frac12$, $b_3=-\frac2{9\pi}$, $b_4=-\frac14,\dots$).
> - **Q10** is a "prove that": the proof below ends with exactly the sheet's formula, and the coefficient $\frac2\pi\cdot\frac1{(2n-1)^3}$ was checked.

---

## Q1

> [!question] Write $u_{xx}+u_{yy}=0$ in polar coordinates.

$x=r\cos\theta$, $y=r\sin\theta$, $r^2=x^2+y^2$, $\theta=\arctan\frac yx$. Chain rule:
$u_x=\cos\theta\,u_r-\frac{\sin\theta}r\,u_\theta$, $u_y=\sin\theta\,u_r+\frac{\cos\theta}r\,u_\theta$.
Differentiating again and adding, the mixed terms and the $u_\theta$ terms cancel:
$$\boxed{u_{xx}+u_{yy}=u_{rr}+\frac1ru_r+\frac1{r^2}u_{\theta\theta}=0}$$
Separation $u=R(r)\Theta(\theta)$: $r^2R''+rR'-\lambda R=0$ (Cauchy–Euler) and $\Theta''+\lambda\Theta=0$.

---

## Q2

> [!question] Solve $\nabla^2u=0$.

### (a) $0<x,y<1$; $u(x,1)=\sin\pi x$, other three edges 0
$u=\sum D_n\sin n\pi x\,\sinh n\pi y$ (vanishes at $y=0$). Only $n=1$ matches the data: $D_1\sinh\pi=1$.
$$\boxed{u=\frac{\sinh\pi y}{\sinh\pi}\,\sin\pi x}$$

### (b) $u(x,0)=x(1-x)$, $u(0,y)=y(1-y)$, $u(x,1)=u(1,y)=0$
Two non-zero edges: solve two problems and add.
- Edge $y=0$: $u_1=\sum a_n\sin n\pi x\,\frac{\sinh n\pi(1-y)}{\sinh n\pi}$, $a_n=2\int_0^1x(1-x)\sin n\pi x\,dx=\frac{4(1-(-1)^n)}{(n\pi)^3}$.
- Edge $x=0$: $u_2=\sum b_n\sin n\pi y\,\frac{\sinh n\pi(1-x)}{\sinh n\pi}$ with the same $b_n=a_n$ (same profile).
$$\boxed{u=\sum_{n\ \text{odd}}\frac{8}{n^3\pi^3\sinh n\pi}\Big[\sin n\pi x\,\sinh n\pi(1-y)+\sin n\pi y\,\sinh n\pi(1-x)\Big]}$$
At $y=0$: $\sum\frac8{n^3\pi^3}\sin n\pi x=x(1-x)$ ✓ (the odd-$n$ sine series of $x(1-x)$). Symmetric in $x\leftrightarrow y$, as the data are.

![[DE-PDE-laplace.png]]

### (c) Disk $0\le r\le a$, $u(a,\theta)=f(\theta)$
Bounded at the centre (drop $r^{-n}$, $\ln r$), $2\pi$-periodic:
$$\boxed{u=\frac{a_0}2+\sum_{n\ge1}\Big(\frac ra\Big)^n(a_n\cos n\theta+b_n\sin n\theta)},\qquad a_n=\frac1\pi\int_0^{2\pi}f\cos n\theta\,d\theta,\ \ b_n=\frac1\pi\int_0^{2\pi}f\sin n\theta\,d\theta.$$
Equivalent Poisson form $u=\frac1{2\pi}\int_0^{2\pi}\frac{a^2-r^2}{a^2-2ar\cos(\theta-\phi)+r^2}f(\phi)\,d\phi$. At the centre $u(0)=\frac{a_0}2=\frac1{2\pi}\int f$: the mean value property.

### (d) Annulus sector $1<r<2$, $0<\theta<\pi$; $u(1,\theta)=\sin\theta$, $u(2,\theta)=0$, $u(r,0)=u(r,\pi)=0$
Dirichlet in $\theta$: $\Theta_n=\sin n\theta$, $\lambda=n^2$. $R_n=A_nr^n+B_nr^{-n}$. The inner data $\sin\theta$ contain only $n=1$, so only $R_1$ is needed: $R(1)=1$, $R(2)=0$:
$A+B=1$, $2A+\frac B2=0\Rightarrow B=-4A$, $A=-\frac13$, $B=\frac43$.
$$\boxed{u=\frac{4-r^2}{3r}\,\sin\theta}$$
Check: $R=\frac4{3r}-\frac r3$, $R'=-\frac4{3r^2}-\frac13$, $R''=\frac8{3r^3}$, so $R''+\frac{R'}r-\frac R{r^2}=\frac8{3r^3}-\frac4{3r^3}-\frac1{3r}-\frac4{3r^3}+\frac1{3r}=0$ ✓, $R(1)=1$, $R(2)=0$ ✓.

---

## Q3

> [!question] Square plate $0\le x,y\le\pi$; edges $x=0$, $x=\pi$, $y=\pi$ insulated; $u(x,0)=x$. Steady state.

Insulated sides $x=0,\pi$: $X_n=\cos nx$ ($n\ge0$). In $y$ the top is insulated ($u_y(x,\pi)=0$), so use the combination with zero slope at $y=\pi$: $\cosh n(y-\pi)$ for $n\ge1$ and a constant for $n=0$:
$$u=\frac{c_0}2+\sum_{n\ge1}c_n\cos nx\,\cosh n(y-\pi).$$
At $y=0$: $\cosh n\pi$ appears. Cosine series of $x$ on $(0,\pi)$: $\frac\pi2+\sum\frac{2[(-1)^n-1]}{n^2\pi}\cos nx$.
$$c_0=\pi,\qquad c_n=\frac{2\,[\cos n\pi-1]}{n^2\pi\cosh n\pi}$$
$$\boxed{u=\frac\pi2+\sum_{n\ge1}\frac{2[(-1)^n-1]}{n^2\pi\cosh n\pi}\cos nx\,\cosh n(y-\pi)}$$
(odd $n$ only: $-\frac4{n^2\pi\cosh n\pi}$). The constant $\frac{c_0}2=\frac\pi2$ is the mean of the edge data: the other three sides are insulated, so in steady state the net flux through $y=0$ must vanish, $\int_0^\pi u_y(x,0)\,dx=0$, which only the cosine modes ($n\ge1$) satisfy.

---

## Q4

> [!question] Plate $0\le x,y\le1$: $y=0$, $y=1$ at $0^\circ$; $u(0,y)=y(1-y)$; $x=1$ insulated.

$u=0$ on $y=0,1$: $Y_n=\sin n\pi y$, $p_n=n\pi$. Insulated at $x=1$ (zero slope): $X_n=\cosh n\pi(x-1)$.
$$u=\sum c_n\cosh n\pi(x-1)\sin n\pi y,\qquad c_n\cosh n\pi=2\!\int_0^1y(1-y)\sin n\pi y\,dy=\frac{4[1-(-1)^n]}{(n\pi)^3}.$$
$$\boxed{u=\sum_{n\ \text{odd}}\frac{8}{n^3\pi^3\cosh n\pi}\cosh n\pi(x-1)\,\sin n\pi y}$$
The sheet writes $c_n=\frac4{n^3\pi^3\cosh n\pi}[1-(-1)^n]$, which is the same thing.

---

## Q5

> [!question] $0<x,y<\pi$; $u=0$ on $x=0$, $x=\pi$, $y=\pi$; $u(x,0)=\sin^2x$.

$u=\sum b_n\sin nx\,\frac{\sinh n(\pi-y)}{\sinh n\pi}$ (zero on $y=\pi$), $b_n=\frac2\pi\int_0^\pi\sin^2x\sin nx\,dx$. Use $\sin^2x=\frac{1-\cos2x}2$: $\int_0^\pi\sin nx=\frac{1-(-1)^n}n$, $\int_0^\pi\cos2x\sin nx=\frac{n(1-(-1)^n)}{n^2-4}$, so
$$b_n=\frac2\pi\cdot\frac12\cdot\frac{1-(-1)^n}{n}\Big(1-\frac{n^2}{n^2-4}\Big)=\frac{4[(-1)^n-1]}{n\pi(n^2-4)}.$$
$$\boxed{u=\sum_{n\ \text{odd}}\frac{-8}{n\pi(n^2-4)\sinh n\pi}\,\sinh n(\pi-y)\,\sin nx}$$
For even $n$ the coefficient is $0$ (the $n=2$ case is $\frac00$ in the formula; direct integration gives $\int\sin^2x\sin2x=0$). Matches the sheet.

---

## Q6

> [!question] Plate of width 10 cm, infinitely long: $u(x,0)=20x$ ($x\le5$), $20(10-x)$ ($x\ge5$); the long edges and far end at $0^\circ$.

Bounded as $y\to\infty$: $Y_n=e^{-n\pi y/10}$ (the $e^{+n\pi y/10}$ branch grows and is dropped):
$$u=\sum D_n\sin\frac{n\pi x}{10}e^{-n\pi y/10},\qquad D_n=\frac2{10}\int_0^{10}u(x,0)\sin\frac{n\pi x}{10}dx=\frac{8H}{n^2\pi^2}\sin\frac{n\pi}2$$
with tent height $H=100$:
$$\boxed{u=\sum_{n\ \text{odd}}\frac{800}{n^2\pi^2}\sin\frac{n\pi}2\,\sin\frac{n\pi x}{10}\,e^{-n\pi y/10}}$$
The decay length of mode $n$ is $\frac{10}{n\pi}$ cm: a few cm from the hot edge only $n=1$ remains.

---

## Q7

> [!question] Semi-infinite strip $0\le x\le L$, $y\ge0$; $x=0$, $x=L$ insulated; $u(x,0)=2\cos\frac{3\pi x}L+3\cos\frac{4\pi x}L$; $u\to0$ as $y\to\infty$.

Insulated sides: $X_n=\cos\frac{n\pi x}L$. Boundedness: $e^{-n\pi y/L}$. The data are already the $n=3$ and $n=4$ eigenfunctions (and have zero mean, so the constant mode does not appear and $u\to0$ is consistent):
$$\boxed{u=2\cos\frac{3\pi x}Le^{-3\pi y/L}+3\cos\frac{4\pi x}Le^{-4\pi y/L}}$$

---

## Q8

> [!question] $u_{rr}+\frac1ru_r+\frac1{r^2}u_{\theta\theta}=0$, $r<1$.

Disk, bounded at 0: $u=\frac{a_0}2+\sum r^n(a_n\cos n\theta+b_n\sin n\theta)$ with $a_n,b_n$ the Fourier coefficients of $u(1,\theta)$.

**(a) $u(1,\theta)=10\cos2\theta$ (as printed).** Only $n=2$: $\boxed{u=10r^2\cos2\theta}$.
**With $u(1,\theta)=10\cos^2\theta=5(1+\cos2\theta)$** (the case the sheet's answer corresponds to): $\boxed{u=5\big(1+r^2\cos2\theta\big)}$. Both are harmonic ($\mathrm{Re}\,z^2=r^2\cos2\theta$).

**(b) $u(1,\theta)=\theta$ for $-\frac\pi2\le\theta<\frac\pi2$, $0$ for $\frac\pi2\le\theta<\frac{3\pi}2$.** One period is $(-\pi,\pi)$, on which $f=\theta$ for $|\theta|<\frac\pi2$ and $0$ otherwise: an **odd** function, so $a_n=0$ and
$$b_n=\frac2\pi\int_0^{\pi/2}\theta\sin n\theta\,d\theta=\frac2\pi\Big[-\frac{\theta\cos n\theta}n+\frac{\sin n\theta}{n^2}\Big]_0^{\pi/2}=\frac{2}{\pi n^2}\sin\frac{n\pi}2-\frac1n\cos\frac{n\pi}2.$$
$$\boxed{u(r,\theta)=\sum_{n\ge1}r^n\Big[\frac{2}{\pi n^2}\sin\frac{n\pi}2-\frac1n\cos\frac{n\pi}2\Big]\sin n\theta}$$
i.e. $b_n=\frac{2(-1)^{(n-1)/2}}{\pi n^2}$ for odd $n$ and $b_n=\frac{(-1)^{n/2+1}}n$ for even $n$.

**Check.** The series at $r=1$ reproduces the data (numerical sum of 4000 terms: $-1.000,-0.400,0.500,1.200$ at $\theta=-1,-0.4,0.5,1.2$; $0$ at $\theta=2,3$). The sheet's printed series gives $-0.125,-0.05,0.062,0.15,0.14,0.02$ at the same points, so it is not the solution of this problem.

![[DE-PDE-laplace.png]]
**Figure (right):** the solution of (b): a smooth interior with the jump in the boundary data at $\theta=\pm\frac\pi2$.

---

## Q9

> [!question] $u_{rr}+\frac1ru_r+\frac1{r^2}u_{\theta\theta}=0$, $0\le\theta\le\pi$, $r<1$; $u(r,0)=u(r,\pi)=0$, $u(1,\theta)=10\theta(\pi-\theta)$.

Half disk, Dirichlet on the diameter: $\Theta_n=\sin n\theta$, bounded radial part $r^n$:
$$u=\sum b_nr^n\sin n\theta,\qquad b_n=\frac2\pi\int_0^\pi10\theta(\pi-\theta)\sin n\theta\,d\theta=\frac2\pi\cdot10\cdot\frac{2[1-(-1)^n]}{n^3}.$$
$$\boxed{u=\sum_{n\ge1}\frac{40}{\pi n^3}\big(1-\cos n\pi\big)\,r^n\sin n\theta}$$
(odd $n$: $\frac{80}{\pi n^3}$). Matches the sheet.

---

## Q10

> [!question] Sector $a<r<b$, $0\le\theta\le\frac\pi2$; $u(a,\theta)=\theta\big(\frac\pi2-\theta\big)$, zero on the remaining boundary. Prove the stated series.

**Proof.** Separation gives $\Theta''+\lambda\Theta=0$ with $\Theta(0)=\Theta(\frac\pi2)=0$: $\Theta_k=\sin2k\theta$, $\lambda=4k^2$, $k=1,2,\dots$. The radial equation $r^2R''+rR'-4k^2R=0$ has solutions $r^{\pm2k}$. Requiring $R(b)=0$ and $R(a)=c_k$:
$$R_k(r)=c_k\,\frac{(r/b)^{2k}-(b/r)^{2k}}{(a/b)^{2k}-(b/a)^{2k}}$$
(numerator vanishes at $r=b$; at $r=a$ the quotient is 1). The $c_k$ are the sine coefficients of $\theta(\frac\pi2-\theta)$ on $(0,\frac\pi2)$:
$$c_k=\frac2{\pi/2}\int_0^{\pi/2}\theta\Big(\frac\pi2-\theta\Big)\sin2k\theta\,d\theta=\frac4\pi\cdot\frac{1-(-1)^k}{4k^3}=\frac{1-(-1)^k}{\pi k^3}.$$
This is $0$ for even $k$ and $\frac2{\pi k^3}$ for odd $k$. Put $k=2n-1$ (so $2k=4n-2$):
$$\boxed{u(r,\theta)=\frac2\pi\sum_{n=1}^\infty\frac{(r/b)^{4n-2}-(b/r)^{4n-2}}{(a/b)^{4n-2}-(b/a)^{4n-2}}\cdot\frac{\sin(4n-2)\theta}{(2n-1)^3}}\qquad\blacksquare$$
(The even modes vanish because the boundary profile is symmetric about $\theta=\frac\pi4$, while $\sin2k\theta$ is antisymmetric for even $k$.)

---

## Summary

| Pattern | Recognise by | Do |
|---|---|---|
| rectangle, one hot edge | one non-zero side, three zero | $\sin\frac{n\pi x}a$ in the direction of the zero pair, $\sinh$ in the other, vanishing on the opposite edge |
| rectangle, two hot edges | two non-zero sides | add two one-edge solutions |
| insulated side | $\partial_nu=0$ | $\cos$ (or $\cosh$ with zero slope), include $n=0$ |
| strip $y\to\infty$ | semi-infinite | $e^{-n\pi y/L}$ only |
| disk | $r<a$, $u(a,\theta)=f$ | $r^n$, full Fourier series, $u(0)=$ mean of $f$ |
| half disk, quarter disk, sector | zero on the rays | $\sin\frac{n\pi\theta}\alpha$ with $r^{n\pi/\alpha}$ |
| annulus | $a<r<b$ | $r^n$ and $r^{-n}$, match both circles |

Verification: `Tools/de_a9_a10.py` (every coefficient against numerical integration; Q2(d) and Q8(a) substituted symbolically); figures `de_pde_figs.py`.

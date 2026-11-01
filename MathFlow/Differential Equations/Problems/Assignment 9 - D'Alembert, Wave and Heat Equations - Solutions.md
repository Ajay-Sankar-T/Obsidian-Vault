---
title: Assignment 9 – D'Alembert, Wave and Heat Equations (Solutions)
course: MA 2102 Differential Equations
assignment: 9
tags:
  - DE
  - assignment-solution
  - pdes
  - wave-equation
  - heat-equation
  - separation-of-variables
  - fourier-series
source: "[[A9-2026.pdf]]"
concepts:
  - "[[D'Alembert's Solution of the Wave Equation]]"
  - "[[Separation of Variables]]"
  - "[[Wave Equation on a Finite Interval]]"
  - "[[Heat Equation - Separation of Variables]]"
aliases:
  - Wave and heat assignment solutions
  - Assignment 9 solutions
---

# Assignment 9 – D'Alembert, Wave and Heat Equations

Source: [[A9-2026.pdf]] · Theory: [[PDEs - MOC]] · Previous: [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]] · Next: [[Assignment 10 - Laplace Equations - Solutions]] · Index: [[Problems - MOC]]

> [!abstract] Contents
> [[#Q1]] · [[#Q2]] · [[#Q3]] · [[#Q4]] · [[#Q5 - Q9 (string)]] · [[#Q10 - Q18 (rod)]] · [[#Summary]]

> [!info] Concept notes for this sheet
> | Questions | Concept note |
> |---|---|
> | Q1, Q2 | [[D'Alembert's Solution of the Wave Equation]] (formula, odd and even extension) |
> | Q3 | [[Separation of Variables]] (first-order and mixed examples) |
> | Q4(a)–(c), Q5–Q9 | [[Wave Equation on a Finite Interval]] |
> | Q4(d)–(g), Q10–Q18 | [[Heat Equation - Separation of Variables]] (steady-state shift, insulated ends, Robin end) |

> [!warning] Points where the sheet needs care
> All closed forms and all Fourier coefficients were checked symbolically or by numerical integration (`Tools/de_a9_a10.py`).
> - **Q3(c):** the printed answer $3e^{18x-3y}$ is wrong. It does not satisfy $u_x+3u_y=0$ ($18-9\ne0$) and does not match $u(0,y)=3e^{-6y}$. The correct term is $3e^{18x-6y}$.
> - **Q4(e)** gives the initial data only on $[0,1]$ although the rod is $0<x<2$. It is solved with $u(x,0)=x$ on the whole rod, where it is exactly the solution $u=x$ (see below).
> - **Q2(d):** $f(0)=1\ne0$ is incompatible with $u(0,t)=0$, so the solution has a jump along the characteristic $x=ct$ (explained below).
> - **Q4(g):** $u(x,0)=x(1-x)$ does not match $u(0,t)=2$, $u(1,t)=3$ at $t=0$, so the Fourier series converges slowly near the ends.
> - Heat problems Q10–Q18 use the diffusivity $c^2$ (the sheet writes $c^2$ in its answers); where $u_t=u_{xx}$ is given, $c=1$.

---

## Q1

> [!question] Derive d'Alembert's solution and solve the Cauchy problems.

**Derivation.** $u_{tt}-c^2u_{xx}=0$ has characteristics $x\pm ct=$ const. With $\xi=x+ct$, $\eta=x-ct$, $u_{tt}-c^2u_{xx}=-4c^2u_{\xi\eta}$, so $u=F(x+ct)+G(x-ct)$. $u(x,0)=f$: $F+G=f$. $u_t(x,0)=g$: $c(F'-G')=g$, so $F-G=\frac1c\int_0^xg+k$. Hence $F(s)=\frac12f(s)+\frac1{2c}\int_0^sg+\frac k2$, $G(s)=\frac12f(s)-\frac1{2c}\int_0^sg-\frac k2$ and
$$u(x,t)=\frac{f(x+ct)+f(x-ct)}2+\frac1{2c}\int_{x-ct}^{x+ct}g(s)\,ds.$$

| | $f$, $g$ | Solution |
|---|---|---|
| (a) | $\sin x$, $\cos x$ | $u=\tfrac12[\sin(x+ct)+\sin(x-ct)]+\tfrac1{2c}[\sin(x+ct)-\sin(x-ct)]$, so $\boxed{u=\sin x\cos ct+\frac1c\cos x\sin ct}$ |
| (b) | $e^{-\lvert x\rvert}$, $x^2$ | $\int_{x-ct}^{x+ct}s^2ds=2x^2ct+\frac23c^3t^3$, so $\boxed{u=\tfrac12\big(e^{-\lvert x+ct\rvert}+e^{-\lvert x-ct\rvert}\big)+x^2t+\frac{c^2t^3}3}$ |
| (c) | $x$, $4cx$ | $\tfrac12[(x+ct)+(x-ct)]=x$; $\frac{4c}{2c}\int s\,ds=2\cdot2xct$, so $\boxed{u=x(1+4ct)}$ |
| (d) | $x(1-x)$, $\sin\pi x$ | $\tfrac12[(x+ct)(1-x-ct)+(x-ct)(1-x+ct)]=x(1-x)-c^2t^2$; $\frac1{2c}\int\sin\pi s=\frac{\sin\pi x\sin\pi ct}{\pi c}$, so $\boxed{u=x(1-x)-c^2t^2+\frac{\sin\pi x\,\sin\pi ct}{\pi c}}$ |

Each satisfies $u_{tt}=c^2u_{xx}$ and the data (checked symbolically; (b) numerically at a point).

---

## Q2

> [!question] D'Alembert's solution of the half-line initial-boundary value problems.

Extend the data to $x<0$ so that the boundary condition holds automatically, then use d'Alembert: **odd** extension for $u(0,t)=0$, **even** for $u_x(0,t)=0$ ([[D'Alembert's Solution of the Wave Equation]]). For $x>ct$ the plain formula holds; for $x<ct$ one argument is negative and the extension is used.

**(a)** $c=2$, $f=|\sin x|$, $g=0$, $u(0,t)=0$. Odd extension $f_o(s)=\operatorname{sgn}(s)\,|\sin s|$. $u=\frac12[f_o(x+2t)+f_o(x-2t)]$:
$$u=\begin{cases}\tfrac12\big(|\sin(x+2t)|+|\sin(x-2t)|\big),&x\ge2t\\[2pt]\tfrac12\big(|\sin(x+2t)|-|\sin(2t-x)|\big),&0<x<2t\end{cases}$$
$u(0,t)=0$ ✓.

**(b)** $c=1$, $f=\cos\frac{\pi x}2$, $g=0$, $u_x(0,t)=0$. $f$ is already even, so no extension is needed: $u=\tfrac12\big[\cos\tfrac{\pi(x+t)}2+\cos\tfrac{\pi(x-t)}2\big]$, i.e.
$$\boxed{u=\cos\tfrac{\pi x}2\cos\tfrac{\pi t}2}\quad(x\ge0,\ t\ge0)$$
$u_x(0,t)=0$ ✓.

**(c)** $c=3$, $f=0$, $g=x^3$, $u(0,t)=0$. $g$ is already odd, so $u=\frac16\int_{x-3t}^{x+3t}s^3ds=\frac1{24}[(x+3t)^4-(x-3t)^4]$:
$$\boxed{u=x^3t+9xt^3}$$
valid for all $x\ge0$; $u(0,t)=0$ ✓, $u_t(x,0)=x^3$ ✓.

**(d)** $f=e^{-x}$, $g=e^x$, $u(0,t)=0$. Odd extensions: $f_o=e^{-s}$ ($s>0$), $-e^s$ ($s<0$); $g_o=e^s$, $-e^{-s}$.
- $x\ge ct$: $\ u=\tfrac12[e^{-x-ct}+e^{-x+ct}]+\frac1{2c}[e^{x+ct}-e^{x-ct}]=\boxed{e^{-x}\cosh ct+\tfrac1ce^x\sinh ct}$.
- $0<x<ct$: $\ u=\tfrac12\big[e^{-x-ct}-e^{x-ct}\big]+\frac1{2c}\big[e^{x+ct}-e^{ct-x}\big]$.

$u(0,t)=0$ ✓. **Compatibility:** $f(0)=g(0)=1\ne0$, so the odd extension jumps at $0$; the two expressions differ by exactly $1$ on $x=ct$. The solution has a jump of size 1 travelling along the characteristic $x=ct$ (a weak solution).

![[DE-PDE-dalembert.png]]

---

## Q3

> [!question] Separation of variables.

[[Separation of Variables]]: $u=XY$, equate both sides to $\lambda$.

| | Separation | Fit the data | Solution |
|---|---|---|---|
| (a) $y^3u_x+x^2u_y=0$, $u(x,0)=e^{x^3/3}$ | $\frac{X'}{x^2X}=-\frac{Y'}{y^3Y}=k$: $X=e^{kx^3/3}$, $Y=e^{-ky^4/4}$ | $k=1$ | $\boxed{u=\exp\!\big(\tfrac{x^3}3-\tfrac{y^4}4\big)}$ |
| (b) $u_x=2u_t+u$, $u(x,0)=6e^{-3x}$ | $\frac{X'}X=\lambda$, $T=e^{(\lambda-1)t/2}$ | $\lambda=-3$ | $\boxed{u=6e^{-3x-2t}}$ |
| (c) $u_x+3u_y=0$, $u(0,y)=4e^{-2y}+3e^{-6y}$ | $X=e^{\lambda x}$, $Y=e^{-\lambda y/3}$ | $\lambda=6$ for $e^{-2y}$, $\lambda=18$ for $e^{-6y}$ | $\boxed{u=4e^{6x-2y}+3e^{18x-6y}}$ |
| (d) $4u_x+u_y=3u$, $u(0,y)=3e^{-y}-e^{-5y}$ | $u=e^{\lambda x+\mu y}$, $4\lambda+\mu=3$ | $\mu=-1\Rightarrow\lambda=1$; $\mu=-5\Rightarrow\lambda=2$ | $\boxed{u=3e^{x-y}-e^{2x-5y}}$ |
| (e) $u_{xx}=u_y+2u$, $u(0,y)=0$, $u_x(0,y)=1+e^{-3y}$ | $\frac{X''}X=\lambda$, $Y=e^{(\lambda-2)y}$ | $e^{0\cdot y}$: $\lambda=2$, $X=\frac1{\sqrt2}\sinh\sqrt2x$; $e^{-3y}$: $\lambda=-1$, $X=\sin x$ | $\boxed{u=\tfrac1{\sqrt2}\sinh\sqrt2\,x+e^{-3y}\sin x}$ |

The sheet's (c) has a misprint (see the note above). The answer to (e) matches the sheet's $\frac1{2\sqrt2}(e^{\sqrt2x}-e^{-\sqrt2x})+e^{-3y}\sin x$.

---

## Q4

> [!question] Separation of variables for the initial-boundary value problems.

### (a) $u_{tt}=c^2u_{xx}$, $u(x,0)=\cos\frac{\pi x}L$, $u_t=0$, $u(0,t)=u(L,t)=0$
Fixed ends: $u=\sum A_n\sin\frac{n\pi x}L\cos\frac{n\pi ct}L$ with $A_n=\frac2L\int_0^L\cos\frac{\pi x}L\sin\frac{n\pi x}Ldx$. For $n\ne1$: $\int=\frac L{\pi}\frac n{n^2-1}(1+(-1)^n)$, and $0$ for $n=1$. So
$$\boxed{u=\sum_{n\ \text{even}}\frac{4n}{\pi(n^2-1)}\sin\frac{n\pi x}L\cos\frac{n\pi ct}L}$$
(only even modes: $\cos\frac{\pi x}L$ is antisymmetric about $x=L/2$, as are the even-$n$ sines).

### (b) $u(x,0)=0$, $u_t=5\cos\frac{2\pi x}L\sin\frac{3\pi x}L$
$2\cos A\sin B=\sin(A+B)-\sin(A-B)$ gives $u_t(x,0)=\frac52\big[\sin\frac{5\pi x}L+\sin\frac{\pi x}L\big]$: only $n=1$ and $n=5$ are excited. $u=\sum B_n\sin\frac{n\pi x}L\sin\frac{n\pi ct}L$ with $B_n\frac{n\pi c}L=\frac52$:
$$\boxed{u=\frac{5L}{2\pi c}\sin\frac{\pi x}L\sin\frac{\pi ct}L+\frac L{2\pi c}\sin\frac{5\pi x}L\sin\frac{5\pi ct}L}$$

### (c) $u_{tt}=4u_{xx}$, $0<x<1$, $u=0$, $u_t=x(1-x)$
$c=2$, $L=1$: $u=\sum B_n\sin n\pi x\sin2n\pi t$, $B_n\,2n\pi=2\int_0^1x(1-x)\sin n\pi x\,dx=\frac{4[1-(-1)^n]}{(n\pi)^3}$, so $B_n=\frac{2[1-(-1)^n]}{n^4\pi^4}$:
$$\boxed{u=\sum_{n\ \text{odd}}\frac4{n^4\pi^4}\sin n\pi x\,\sin2n\pi t}$$

### (d) $u_t=4u_{xx}$, $0<x<1$, $u(x,0)=x^2(1-x)$, $u(0,t)=u(1,t)=0$
$u=\sum c_n\sin n\pi x\,e^{-4n^2\pi^2t}$, $c_n=2\int_0^1x^2(1-x)\sin n\pi x\,dx$. By parts, $\int_0^1x^2\sin n\pi x=-\frac{(-1)^n}{n\pi}+\frac{2((-1)^n-1)}{(n\pi)^3}$ and $\int_0^1x^3\sin n\pi x=-\frac{(-1)^n}{n\pi}+\frac{6(-1)^n}{(n\pi)^3}$, so
$$\boxed{u=\sum_{n\ge1}\frac{-4\big(1+2(-1)^n\big)}{n^3\pi^3}\sin n\pi x\;e^{-4n^2\pi^2t}}$$
($c_n=\frac4{n^3\pi^3}$ for odd $n$, $-\frac{12}{n^3\pi^3}$ for even $n$).

### (e) $u_t=u_{xx}$, $0<x<2$, $u(0,t)=0$, $u_x(2,t)=1$
With the initial data $u(x,0)=x$ on the whole rod, **$u=x$ is an exact solution**: $u_t=0=u_{xx}$, $u(0,t)=0$, $u_x(2,t)=1$ ✓. As printed (data only on $[0,1]$) the problem is incomplete. In general write $u=x+v$ with $v_t=v_{xx}$, $v(0,t)=0$, $v_x(2,t)=0$, $v(x,0)=f(x)-x$, and expand in $\sin\frac{(2n-1)\pi x}4$ with factor $e^{-(2n-1)^2\pi^2t/16}$; the data $f=x$ gives $v\equiv0$:
$$\boxed{u(x,t)=x}$$

### (f) $u_t=u_{xx}$, $0<x<100$, $u(x,0)=60$ ($x<50$), $40$ ($x>50$), $u_x(0,t)=0$, $u_x(100,t)=1$
Non-homogeneous Neumann: use $w=\frac{x^2}{200}+\frac t{100}$, which solves $w_t=w_{xx}$ with $w_x(0)=0$, $w_x(100)=1$. Then $v=u-w$ has insulated ends and $v(x,0)=f(x)-\frac{x^2}{200}$:
$$v=A_0+\sum A_n\cos\tfrac{n\pi x}{100}e^{-n^2\pi^2t/10^4},\quad A_0=\tfrac1{100}\!\int_0^{100}\!\big(f-\tfrac{x^2}{200}\big)dx=\tfrac{100}3,$$
$$A_n=\tfrac2{100}\int_0^{100}\Big(f-\tfrac{x^2}{200}\Big)\cos\tfrac{n\pi x}{100}dx=\frac{40\sin\frac{n\pi}2}{n\pi}-\frac{200(-1)^n}{n^2\pi^2}.$$
$$\boxed{u=\frac{x^2}{200}+\frac t{100}+\frac{100}3+\sum_{n\ge1}\Big[\frac{40\sin\frac{n\pi}2}{n\pi}-\frac{200(-1)^n}{n^2\pi^2}\Big]\cos\frac{n\pi x}{100}e^{-n^2\pi^2t/10^4}}$$
The mean temperature rises at the rate $\frac1{100}$: heat flows in at the right end ($\int u\,dx$ grows by $u_x(100)\cdot1$ per unit time).

### (g) $u_t=ku_{xx}$, $u(x,0)=x(1-x)$, $u(0,t)=2$, $u(1,t)=3$
Steady state $w=2+x$. $v=u-w$: $v(0,t)=v(1,t)=0$, $v(x,0)=-x^2-2$:
$$v=\sum b_n\sin n\pi x\,e^{-kn^2\pi^2t},\quad b_n=2\!\int_0^1(-x^2-2)\sin n\pi x\,dx=\frac{6(-1)^n-4}{n\pi}+\frac{4\big(1-(-1)^n\big)}{(n\pi)^3}.$$
$$\boxed{u=2+x+\sum_{n\ge1}\Big[\frac{6(-1)^n-4}{n\pi}+\frac{4(1-(-1)^n)}{n^3\pi^3}\Big]\sin n\pi x\;e^{-kn^2\pi^2t}}$$

![[DE-PDE-heat.png]]

---

## Q5 - Q9 (string)

Fixed ends: $u=\sum\big(A_n\cos\frac{n\pi ct}l+B_n\sin\frac{n\pi ct}l\big)\sin\frac{n\pi x}l$ with $A_n=\frac2l\int f\sin\frac{n\pi x}l$, $B_n=\frac2{n\pi c}\int g\sin\frac{n\pi x}l$ ([[Wave Equation on a Finite Interval]]).

**Q5 — midpoint raised to $h$, released from rest.** $f=\frac{2hx}l$ on $[0,\frac l2]$, $\frac{2h(l-x)}l$ on $[\frac l2,l]$, $g=0$. $A_n=\frac{8h}{n^2\pi^2}\sin\frac{n\pi}2$, $B_n=0$:
$$\boxed{u=\sum_{n\ge1}\frac{8h}{n^2\pi^2}\sin\frac{n\pi}2\sin\frac{n\pi x}l\cos\frac{n\pi ct}l}$$
(odd $n$ only). Matches the sheet.

**Q6 — velocity $\sin^3(\pi x/l)$ from rest.** $\sin^3\theta=\frac14(3\sin\theta-\sin3\theta)$, so only $n=1,3$ are excited: $B_1\frac{\pi c}l=\frac34$, $B_3\frac{3\pi c}l=-\frac14$:
$$\boxed{u=\frac{3l}{4\pi c}\sin\frac{\pi x}l\sin\frac{\pi ct}l-\frac l{12\pi c}\sin\frac{3\pi x}l\sin\frac{3\pi ct}l}$$

**Q7 — fixed at 0, free at $l$, released from $hx(l-x)^2$.** Eigenfunctions $\sin\frac{(2n-1)\pi x}{2l}$ (fixed–free), frequencies $\frac{(2n-1)\pi c}{2l}$, $c^2=T_0/\rho$, zero initial velocity:
$$u=\sum a_n\sin\frac{(2n-1)\pi x}{2l}\cos\frac{(2n-1)\pi ct}{2l},\quad a_n=\frac2l\int_0^lhx(l-x)^2\sin\frac{(2n-1)\pi x}{2l}dx.$$
Integrating by parts three times and using $\sin\frac{(2n-1)\pi}2=(-1)^{n+1}$, $\cos\frac{(2n-1)\pi}2=0$:
$$\boxed{a_n=\frac{32hl^3}{\pi^4}\cdot\frac{6(-1)^n+(4n-2)\pi}{(2n-1)^4}}$$
(numerically confirmed against quadrature for $n=1\dots7$; the sheet's coefficient is correct).

**Q8 — tent initial shape, released with velocity $a$.** $l=1$: $A_n=\frac4{n^2\pi^2}\sin\frac{n\pi}2$, $B_n=\frac1{n\pi c}\cdot\frac{2a[1-(-1)^n]}{n\pi}$:
$$\boxed{u=\sum_{n\ge1}\sin n\pi x\Big[\frac4{n^2\pi^2}\sin\frac{n\pi}2\cos n\pi ct+\frac{2a\,[1+(-1)^{n+1}]}{n^2\pi^2c}\sin n\pi ct\Big]}$$

**Q9 — trisection points pulled to opposite sides.** Initial shape: $3hx/l$ on $[0,\frac l3]$, $3h-6hx/l$ on $[\frac l3,\frac{2l}3]$ (through $+h$ and $-h$), $3hx/l-3h$ on $[\frac{2l}3,l]$; $g=0$, so $B_n=0$.
$$A_n=\frac{18h}{n^2\pi^2}\Big(\sin\frac{n\pi}3-\sin\frac{2n\pi}3\Big)=\begin{cases}\dfrac{36h}{n^2\pi^2}\sin\dfrac{n\pi}3,&n\text{ even}\\[4pt]0,&n\text{ odd}\end{cases}$$
since $\sin\frac{2n\pi}3=-(-1)^n\sin\frac{n\pi}3$.
$$\boxed{u=\sum_{n\ \text{even}}\frac{36h}{n^2\pi^2}\sin\frac{n\pi}3\sin\frac{n\pi x}l\cos\frac{n\pi ct}l}$$
**Mid-point stays at rest:** at $x=\frac l2$, $\sin\frac{n\pi}2=0$ for every even $n$, so $u(\frac l2,t)=0$ for all $t$. (Equivalent symmetry argument: the shape is antisymmetric about $x=\frac l2$ and the wave equation preserves that symmetry.)

![[DE-PDE-string.png]]

---

## Q10 - Q18 (rod)

Heat equation $u_t=c^2u_{xx}$, rod length $l$ ([[Heat Equation - Separation of Variables]]).

**Q10 — ends at 0°, triangular start (100 cm).** $f=x$ on $[0,50]$, $100-x$ on $[50,100]$: $c_n=\frac2{100}\int f\sin\frac{n\pi x}{100}=\frac{4l}{n^2\pi^2}\sin\frac{n\pi}2=\frac{400}{n^2\pi^2}\sin\frac{n\pi}2$:
$$\boxed{u=\sum_{n\ \text{odd}}\frac{400(-1)^{(n-1)/2}}{n^2\pi^2}\sin\frac{n\pi x}{100}e^{-n^2\pi^2c^2t/10^4}}$$

**Q11 — insulated ends, $u(x,0)=6+4\cos\frac{3\pi x}l$.** The data are already eigenfunctions ($\cos\frac{n\pi x}l$ with $n=0$ and $n=3$):
$$\boxed{u=6+4\cos\frac{3\pi x}l\,e^{-9\pi^2c^2t/l^2}}$$
(the sheet's $e^{-n^2\pi^2c^2t/l^2}$ with $n=3$).

**Q12 — $u_t=u_{xx}$, $u(0,t)=90$, $u(10,t)=60$, $u(x,0)=5x+50$.** Steady state $w=90-3x$; $v(x,0)=8x-40$; $c_n=\frac{2}{10}\int_0^{10}(8x-40)\sin\frac{n\pi x}{10}=\frac{80}{n\pi}[(-1)^{n+1}-1]$:
$$\boxed{u=90-3x+\sum_{n\ge1}\frac{80}{n\pi}\big[(-1)^{n+1}-1\big]\sin\frac{n\pi x}{10}\,e^{-n^2\pi^2t/100}}$$
(nonzero for even $n$ only: $c_n=-\frac{160}{n\pi}$).

**Q13 — 20 cm rod, ends $30°$/$80°$ then $40°$/$60°$.** Old steady state $30+\frac{5x}2$; new steady state $w=40+x$; $v(x,0)=\frac32x-10$, $c_n=\frac{20}{n\pi}\big[2(-1)^{n+1}-1\big]$:
$$\boxed{u=x+40+\sum_{n\ge1}\frac{20}{n\pi}\big[2(-1)^{n+1}-1\big]\sin\frac{n\pi x}{20}e^{-n^2\pi^2c^2t/400}}$$

**Q14 — 50 cm rod, ends $0°$ and $100°$, then insulated.** Initial $2x$ (steady state). Insulated ends: $A_0=\frac1{50}\int_0^{50}2x\,dx=50$, $A_n=\frac{2}{50}\int_0^{50}2x\cos\frac{n\pi x}{50}=\frac{4l}{n^2\pi^2}[(-1)^n-1]=-\frac{400}{n^2\pi^2}$ (odd $n$):
$$\boxed{u=50-\sum_{n\ \text{odd}}\frac{400}{n^2\pi^2}\cos\frac{n\pi x}{50}\,e^{-n^2\pi^2c^2t/2500}}$$

**Q15 — rod of length $\pi$, $u(0,t)=0$, radiating end $x=\pi$, $u(x,0)=x$.** "Loses heat at a rate proportional to its temperature": $u_x(\pi,t)=-h\,u(\pi,t)$, $h>0$. $u=\sum B_n\sin p_nx\,e^{-c^2p_n^2t}$ with $p_n$ the positive roots of $p\cos p\pi+h\sin p\pi=0$, i.e. $\tan p\pi=-p/h$. The eigenfunctions are orthogonal in $L^2(0,\pi)$ (a regular S–L problem), so $B_n=\frac{\int_0^\pi x\sin p_nx\,dx}{\int_0^\pi\sin^2p_nx\,dx}$. Using $\cos p\pi=-\frac hp\sin p\pi$ and $\sin^2p\pi=\frac{p^2}{p^2+h^2}$:
$$\boxed{B_n=\frac{2(1+\pi h)(p_n^2+h^2)\sin p_n\pi}{p_n^2\big[\pi(p_n^2+h^2)+h\big]}}$$
(checked against quadrature for $h=1$: $p_1=0.7876$, $p_2=1.6716$, $B_1=2.198$, $B_2=-0.747$). As $h\to\infty$ the end is held at $0$ and $p_n\to n$, $B_n\to\frac{2(-1)^{n+1}}n$ (the sine series of $x$).

**Q16 — 10 cm rod, ends $20°/40°$, then $50°/10°$.** Old: $20+2x$. New steady: $w=50-4x$. $v(x,0)=6(x-5)$, $b_n=-\frac{60[1+(-1)^n]}{n\pi}=-\frac{120}{n\pi}$ for even $n$:
$$\boxed{u=50-4x-\sum_{n\ \text{even}}\frac{120}{n\pi}\sin\frac{n\pi x}{10}e^{-n^2\pi^2c^2t/100}}$$
**Mid-point:** at $x=5$, $\sin\frac{n\pi}2=0$ for even $n$, so $u(5,t)=50-20=30$ for all $t$ (the old temperature there was $20+10=30$).

**Q17 — 30 cm rod, ends $20°/80°$ then both $0°$.** Initial $20+2x$, $b_n=\frac2{30}\int_0^{30}(20+2x)\sin\frac{n\pi x}{30}=\frac{40}{n\pi}\big(1-4(-1)^n\big)$:
$$\boxed{u=\sum_{n\ge1}\frac{40\big(1-4(-1)^n\big)}{n\pi}\sin\frac{n\pi x}{30}e^{-n^2\pi^2c^2t/900}}$$

**Q18 — 100 cm rod, ends $0°/100°$ then insulated.** Initial $x$: $A_0=50$, $A_n=\frac{200[(-1)^n-1]}{n^2\pi^2}$ (odd $n$: $-\frac{400}{n^2\pi^2}$):
$$\boxed{u=50-\sum_{n\ \text{odd}}\frac{400}{n^2\pi^2}\cos\frac{n\pi x}{100}e^{-n^2\pi^2c^2t/10^4}}$$
**Symmetry:** for odd $n$, $\cos\frac{n\pi(100-x)}{100}=-\cos\frac{n\pi x}{100}$, so every term flips sign under $x\to100-x$, and $u(x,t)+u(100-x,t)=100$ for all $t$.

![[DE-PDE-heat.png]]

---

## Summary

| Pattern | Recognise by | Do |
|---|---|---|
| infinite line | $u_{tt}=c^2u_{xx}$, $x\in\mathbb R$ | d'Alembert: $\frac12(f(x+ct)+f(x-ct))+\frac1{2c}\int g$ |
| half line | $x>0$ with $u=0$ or $u_x=0$ at 0 | odd / even extension; check $f(0)=0$ |
| finite string | fixed ends | $\sin\frac{n\pi x}l$ modes; $B_n$ carries $\frac1{n\pi c}$ |
| fixed–free | $u(0)=0$, $u_x(l)=0$ | $\sin\frac{(2n-1)\pi x}{2l}$ |
| heat, ends at 0 | $u(0,t)=u(L,t)=0$ | sine series, $e^{-c^2n^2\pi^2t/L^2}$ |
| heat, insulated | $u_x=0$ | cosine series, mean as constant mode |
| heat, ends held at $A,B$ | non-homogeneous | subtract $w=A+\frac{B-A}Lx$, expand $f-w$ |
| ends changed suddenly | two steady states | new steady state $w$, initial $v=$ old $-w$ |
| symmetric data | mid-point, sum of equidistant points | parity kills half the modes |

Verification: `Tools/de_a9_a10.py` (coefficients vs quadrature, d'Alembert solutions substituted symbolically); figures `de_pde_figs.py`.

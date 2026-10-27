---
title: Assignment 7 – Sturm–Liouville Problems (Solutions)
course: MA 2102 Differential Equations
assignment: 7
tags:
  - DE
  - assignment-solution
  - sturm-liouville
  - eigenvalue-problems
  - orthogonality
  - eigenfunction-expansion
  - special-functions
source: "[[Assignment-7.pdf]]"
concepts:
  - "[[Sturm-Liouville Problems]]"
  - "[[Inner Product Spaces and Orthogonal Functions]]"
  - "[[Fourier-Bessel Series]]"
  - "[[Orthogonality and Norm of Legendre Polynomials]]"
aliases:
  - Sturm-Liouville assignment solutions
  - Assignment 7 solutions
---

# Assignment 7 – Sturm–Liouville Problems

Source: [[Assignment-7.pdf]] · Theory: [[Sturm-Liouville Problems]] · [[Inner Product Spaces and Orthogonal Functions]] · [[Special Functions - MOC]] · Previous: [[Assignment 6 - Bessel Functions - Solutions]] · Index: [[Problems - MOC]]

> [!abstract] Contents
> [[#0. Theory toolkit]] · [[#Q1]] · [[#Q2]] · [[#Q3]] · [[#Q4]] · [[#Q5]] · [[#Q6]] · [[#Q7]] · [[#Summary]]

> [!info] Concept notes for this sheet
> | Questions | Concept note |
> |---|---|
> | all | [[Sturm-Liouville Problems]] (form, self-adjointness, orthogonality, eigenfunction expansion) |
> | Q1, Q4(d) | [[Bessel's Equation and Bessel Functions of the First Kind]] · [[Fourier-Bessel Series]] (parametric Bessel as an SLP, weight $x$) |
> | Q1 | [[Legendre's Equation]] (weight 1) · Chebyshev (weight $1/\sqrt{1-x^2}$) |
> | Q3(f), (j)–(m) | [[Cauchy-Euler Equations]] (substitute $x=e^t$) |
> | Q4–Q6 | [[Inner Product Spaces and Orthogonal Functions]] · [[Legendre Series and Fourier-Legendre Expansions]] (same coefficient formula) |

> [!warning] Points where the sheet needs care
> All claims were checked numerically or symbolically (`Tools/de_a6a7.py`).
> - **Q3(j) and Q3(k)** put a boundary condition at $x=0$, which is a **singular point** of $x^2y''+\dots$. As printed, (j) has no discrete spectrum (every $\lambda>3$ is admitted) and (k) has no eigenvalue at all. Both are solved as printed *and* in the regular version with the left end moved to $x=1$ (the form of (l), (m)), which is almost surely what was meant.
> - **Q5 and Q6** each list "(c)" twice (the sheet has $f=1-x$ and the step function both as (c)). Here they are (c) $1-x$ and (c′) the step function.
> - In **Q3(i)** the substitution $\theta=\arctan x$ makes the problem trivial; the eigenvalues are $16n^2$, not roots of a transcendental equation.

---

## 0. Theory toolkit

### 0.1 Sturm–Liouville form
$$\big(p\,y'\big)'+\big(q+\lambda\,r\big)y=0\quad(a<x<b),\qquad p>0,\ r>0\ \text{on }(a,b).$$
$r$ is the **weight**. The associated operator $Ly=(py')'+qy$ and the eigenproblem $Ly=-\lambda ry$.

### 0.2 Lagrange and Green identities (Q7)
$$uLv-vLu=\big[p(uv'-u'v)\big]',\qquad\int_a^b(uLv-vLu)\,dx=\big[p(uv'-u'v)\big]_a^b.$$
If the boundary term vanishes (separated, periodic, or singular-end conditions), $L$ is **self-adjoint**.

### 0.3 Consequences
For eigenpairs $(\lambda_m,y_m),(\lambda_n,y_n)$ with $\lambda_m\ne\lambda_n$:
$$(\lambda_m-\lambda_n)\int_a^b r\,y_my_n\,dx=0\ \Rightarrow\ \int_a^b r\,y_my_n\,dx=0.$$
Eigenvalues are real; for a function $f$,
$$f\sim\sum a_ny_n,\qquad a_n=\frac{\int_a^b r\,f\,y_n\,dx}{\int_a^b r\,y_n^2\,dx}.$$

### 0.4 How to solve a constant-coefficient or Euler eigenproblem
1. Separate the cases $\lambda<0,\ =0,\ >0$ (for the problems here the sign is read off from the energy identity or just tried).
2. For $y''+\dots$ with first-derivative term remove it with $y=e^{-\frac12\int f}z$ (or reduce to $z''+\mu z=0$).
3. For Euler equations put $x=e^t$.
4. For $((p y')'+\lambda ry=0)$ with $p,r$ exponentials/powers, find the change of variable $s=\int\!\sqrt{r/p}\,dx$ that makes it $z_{ss}+\lambda z=0$.

---

## Q1

> [!question] Write the parametric Bessel, Legendre and Chebyshev equations in Sturm–Liouville form.

**Parametric Bessel** $x^2y''+xy'+(\lambda^2x^2-m^2)y=0$. Divide by $x$: $xy''+y'=(xy')'$, so
$$\big(xy'\big)'+\Big(-\frac{m^2}x+\lambda^2x\Big)y=0:\qquad p=x,\quad q=-\frac{m^2}x,\quad r=x,\quad\text{eigenvalue }\lambda^2.$$
**Legendre** $(1-x^2)y''-2xy'+n(n+1)y=0$:
$$\big((1-x^2)y'\big)'+n(n+1)y=0:\qquad p=1-x^2,\quad q=0,\quad r=1,\quad\text{eigenvalue }n(n+1).$$
**Chebyshev** $(1-x^2)y''-xy'+n^2y=0$. Take $p=\sqrt{1-x^2}$; then $p'=-x/\sqrt{1-x^2}$ and
$$(py')'=\sqrt{1-x^2}\,y''-\frac x{\sqrt{1-x^2}}y'=\frac1{\sqrt{1-x^2}}\big[(1-x^2)y''-xy'\big].$$
Dividing the equation by $\sqrt{1-x^2}$:
$$\big(\sqrt{1-x^2}\,y'\big)'+\frac{n^2}{\sqrt{1-x^2}}\,y=0:\qquad p=\sqrt{1-x^2},\quad q=0,\quad r=\frac1{\sqrt{1-x^2}},\quad\text{eigenvalue }n^2.$$
(These three choices are the origin of the weights $x$, $1$, $1/\sqrt{1-x^2}$ in the Bessel, Legendre, Chebyshev orthogonality relations. Q2's recipe gives the same $p$ and $r$.)

---

## Q2

> [!question] Show $y''+fy'+(g+\lambda h)y=0$ becomes S–L form with $p=e^{\int f}$, $q=pg$, $r=hp$.

Multiply by $p=\exp\!\int f\,dx$. Since $p'=fp$,
$$py''+pfy'=py''+p'y'=(py')'.$$
So $(py')'+pg\,y+\lambda\,hp\,y=0$, i.e. $(py')'+(q+\lambda r)y=0$ with $q=pg$, $r=hp$. ∎

(Check on Chebyshev: $f=-\dfrac x{1-x^2}$, $\int f=\tfrac12\ln(1-x^2)$, so $p=\sqrt{1-x^2}$ and $h=\dfrac1{1-x^2}$ gives $r=\dfrac1{\sqrt{1-x^2}}$ ✓.)

---

## Q3

> [!question] Eigenvalues and eigenfunctions of (a)–(m).

Every closed form below was substituted into the ODE and boundary conditions at 30-digit precision (residuals $<10^{-15}$) for $n\le4$, and orthogonality with the stated weight was verified numerically. A summary table is at the end of this question.

### (a) $y''+\lambda y=0,\ y(0)=0,\ y'(\pi)=0$
- $\lambda=0$: $y=Ax+B$, $y(0)=0\Rightarrow B=0$, $y'(\pi)=A=0$. Trivial.
- $\lambda=-\mu^2<0$: $y=A\sinh\mu x$, $y'(\pi)=A\mu\cosh\mu\pi\ne0$. None.
- $\lambda=\mu^2>0$: $y=\sin\mu x$, $y'(\pi)=\mu\cos\mu\pi=0\Rightarrow\mu\pi=(n-\tfrac12)\pi$.

$$\boxed{\lambda_n=\Big(\frac{2n-1}2\Big)^2,\quad y_n=\sin\frac{(2n-1)x}2,\quad n=1,2,\dots}$$

### (b) $y''+4y'-\lambda y=0,\ y'(0)=y'(2)=0$
S–L form: $p=e^{4x}$, $\big(e^{4x}y'\big)'-\lambda e^{4x}y=0$, so the weight is $e^{4x}$ with eigenparameter $-\lambda$. Characteristic roots $m=-2\pm\sqrt{4+\lambda}$.
- $4+\lambda=k^2>0$: $y=e^{-2x}(Ae^{kx}+Be^{-kx})$. $y'(0)=0$ gives $(k-2)A=(k+2)B$ and $y'(2)=0$ gives $(k-2)Ae^{2k}=(k+2)Be^{-2k}$; together $B(k+2)\big(e^{2k}-e^{-2k}\big)=0$, so $B=0$ and then $k=2$: $\lambda=0$, $y=1$.
- $4+\lambda=0$: $y=e^{-2x}(A+Bx)$ gives $B-2A=0$ and $-4Be^{-4}=0$. Trivial.
- $4+\lambda=-\omega^2<0$: $y=e^{-2x}(A\cos\omega x+B\sin\omega x)$. $y'(0)=0$: $\omega B=2A$. Then $y'(2)=-e^{-4}(2B+\omega A)\sin2\omega=-e^{-4}A\dfrac{4+\omega^2}\omega\sin2\omega=0$, so $\sin2\omega=0$: $\omega=\dfrac{n\pi}2$.

$$\boxed{\lambda_0=0,\ y_0=1;\qquad\lambda_n=-\Big(4+\frac{n^2\pi^2}4\Big),\ \ y_n=e^{-2x}\Big[\frac{n\pi}2\cos\frac{n\pi x}2+2\sin\frac{n\pi x}2\Big],\ n\ge1}$$
Weight $e^{4x}$ on $[0,2]$.

### (c) $y''+\lambda y=0$, periodic: $y(0)=y(2\pi),\ y'(0)=y'(2\pi)$
$\lambda=0$: $y=A+Bx$, periodicity forces $B=0$: $y=1$. $\lambda<0$: no periodic exponentials. $\lambda=\mu^2$: $y=A\cos\mu x+B\sin\mu x$; both conditions give $\sin\mu\pi\,(\cdot)=0$ in both, i.e. $\mu=n\in\mathbb Z$.
$$\boxed{\lambda_0=0,\ y_0=1;\qquad\lambda_n=n^2,\ y_n\in\{\cos nx,\ \sin nx\},\ n\ge1}$$
Each $\lambda_n$ ($n\ge1$) is **double** (two independent eigenfunctions): the periodic problem is self-adjoint but not "simple".

### (d) $y''+2y'+(\lambda+1)y=0,\ y(0)=y(\pi)=0$
Put $y=e^{-x}z$: $y'=e^{-x}(z'-z)$, $y''=e^{-x}(z''-2z'+z)$, so $y''+2y'+(\lambda+1)y=e^{-x}\big(z''+\lambda z\big)$. Then $z''+\lambda z=0$, $z(0)=z(\pi)=0$: $\lambda=n^2$, $z=\sin nx$.
$$\boxed{\lambda_n=n^2,\quad y_n=e^{-x}\sin nx,\quad n=1,2,\dots}\qquad\text{weight }e^{2x}$$
($\lambda\le0$ gives only the trivial solution, as in (a).)

### (e) $y''-y'+\lambda y=0,\ y(0)=y(L)=0$
$y=e^{x/2}z$ gives $z''+\big(\lambda-\tfrac14\big)z=0$, $z(0)=z(L)=0$. Only $\lambda-\tfrac14=\big(\tfrac{n\pi}L\big)^2>0$ works.
$$\boxed{\lambda_n=\frac14+\frac{n^2\pi^2}{L^2},\quad y_n=e^{x/2}\sin\frac{n\pi x}L,\quad n=1,2,\dots}\qquad\text{weight }e^{-x}$$

### (f) $(xy')'+\dfrac\lambda xy=0,\ y(1)=0,\ y'(e)=0$
$x^2y''+xy'+\lambda y=0$ (Euler). With $t=\ln x$: $Y''+\lambda Y=0$, $Y(0)=0$, $Y'(1)=0$ (since $y'=Y'/x$ and $x=e$ is $t=1$). That is (a) on $[0,1]$: $Y=\sin\mu t$, $\mu\cos\mu=0$, $\mu=(n-\tfrac12)\pi$.
$$\boxed{\lambda_n=\Big(\frac{(2n-1)\pi}2\Big)^2,\quad y_n=\sin\Big(\frac{(2n-1)\pi}2\ln x\Big),\quad n\ge1}\qquad\text{weight }1/x$$

### (g) $(e^{2x}y')'+e^{-2x}(\lambda+1)y=0,\ y(0)=y(\pi)=0$
Expand: $y''+2y'+e^{-4x}(\lambda+1)y=0$. Let $s=e^{-2x}$ (so $s\in[e^{-2\pi},1]$, decreasing). Then $y_x=-2sy_s$ and $y_{xx}=4sy_s+4s^2y_{ss}$, so $y''+2y'=4s^2y_{ss}$ and the equation becomes
$$4y_{ss}+(\lambda+1)y=0.$$
Zeros at both ends of the $s$-interval of length $1-e^{-2\pi}$ force $\sqrt{\lambda+1}\,(1-e^{-2\pi})/2=n\pi$ ($\lambda+1\le0$ gives only the trivial solution).
$$\boxed{\lambda_n=\frac{4n^2\pi^2}{(1-e^{-2\pi})^2}-1,\quad y_n=\sin\Big(n\pi\,\frac{e^{-2x}-e^{-2\pi}}{1-e^{-2\pi}}\Big),\quad n\ge1}\qquad\text{weight }e^{-2x}$$
($\lambda_1=38.626$.) The weight is exactly $ds$ up to a constant, which is why the $y_n$ are orthogonal.

### (h) $4(e^{-x}y')'+(1+\lambda)e^xy=0,\ y(0)=y(1)=0$
Expand: $y''-y'+\frac{1+\lambda}4e^{2x}y=0$. Let $s=e^x$: $y_x=sy_s$, $y_{xx}=sy_s+s^2y_{ss}$, so $y''-y'=s^2y_{ss}$ and
$$y_{ss}+\frac{1+\lambda}4y=0,\qquad s\in[1,e],\ y(1)=y(e)=0.$$
$$\boxed{\lambda_n=\frac{4n^2\pi^2}{(e-1)^2}-1,\quad y_n=\sin\Big(n\pi\frac{e^x-1}{e-1}\Big),\quad n\ge1}\qquad\text{weight }e^x$$
($\lambda_1=12.371$.)

### (i) $\big((x^2+1)y'\big)'+\dfrac\lambda{x^2+1}y=0,\ y'(0)=y'(1)=0$
Put $\theta=\arctan x$, $d\theta=dx/(1+x^2)$. Then $y_x=\dfrac{y_\theta}{1+x^2}$, so $(x^2+1)y_x=y_\theta$ and $\big((x^2+1)y_x\big)_x=\dfrac{y_{\theta\theta}}{1+x^2}$. The equation is $\dfrac1{1+x^2}\big(y_{\theta\theta}+\lambda y\big)=0$:
$$y_{\theta\theta}+\lambda y=0,\qquad y_\theta(0)=0,\ y_\theta\Big(\frac\pi4\Big)=0\quad(\theta\in[0,\tfrac\pi4]).$$
This is the Neumann problem on an interval of length $\pi/4$: $y=\cos\mu\theta$, $\mu\sin\frac{\mu\pi}4=0\Rightarrow\mu=4n$.
$$\boxed{\lambda_n=16n^2,\quad y_n=\cos\big(4n\arctan x\big),\quad n=0,1,2,\dots}\qquad\text{weight }\frac1{1+x^2}$$
($\lambda_0=0$, $y_0=1$.)

### (j) $x^2y''-3xy'+\lambda y=0,\ y'(0)=0,\ y'(\pi)=0$

**As printed (singular at $x=0$).** Euler equation with roots $m=2\pm k$, $k=\sqrt{4-\lambda}$. In S–L form $p=x^{-3}$, $r=x^{-5}$: $p$ blows up at $0$, so $x=0$ is a singular end and "$y'(0)=0$" must be read as $\lim_{x\to0^+}y'(x)=0$.
- $0<k<1$ ($3<\lambda<4$): both $x^{2+k}$ and $x^{2-k}$ have $y'\to0$ at $0$. Only $y'(\pi)=0$ remains: **one** linear condition on two constants, so **every** such $\lambda$ has a nontrivial solution.
- $\lambda\ge4$: $y=x^2\big(A\cos(\omega\ln x)+B\sin(\omega\ln x)\big)$ ($\omega=\sqrt{\lambda-4}$), or $x^2(A+B\ln x)$ at $\lambda=4$. Again $y'=O(x)\to0$ at $0$ for every $A,B$, and $y'(\pi)=0$ is one condition: **every** $\lambda\ge4$ is admitted.
- $\lambda=3$ and $k>1$, $k\ne2$: $x^{2-k}$ has $y'\not\to0$, so $B=0$, then $y'(\pi)=0$ forces $A=0$.
- $k=2$ ($\lambda=0$): $y=Ax^4+B$, $y'(\pi)=4A\pi^3=0$, so $y=1$.

So the printed conditions admit $\{0\}\cup(3,\infty)$: a **continuous** spectrum, not a Sturm–Liouville eigenvalue problem. This is the signature of a singular problem with a condition that does not select a self-adjoint extension.

**Regular version (left end at $x=1$): $y'(1)=y'(\pi)=0$.** $x=e^t$, $T=\ln\pi$: $Y''-4Y'+\lambda Y=0$, $Y'(0)=Y'(T)=0$, with $Y=e^{2t}z$ this is $z''+(\lambda-4)z=0$. For $\lambda=4+\omega^2>4$: $Y=e^{2t}(A\cos\omega t+B\sin\omega t)$; $Y'(0)=2A+\omega B=0$, and $Y'(T)=e^{2T}(2B-\omega A)\sin\omega T$ with $2B-\omega A=B(4+\omega^2)/2\ne0$, so $\sin\omega T=0$. For $\lambda\le4$ only $\lambda=0$, $y=1$ survives (as in (b)).
$$\lambda_0=0,\ y_0=1;\qquad\lambda_n=4+\frac{n^2\pi^2}{\ln^2\pi},\quad y_n=x^2\Big[\omega_n\cos(\omega_n\ln x)-2\sin(\omega_n\ln x)\Big],\ \omega_n=\frac{n\pi}{\ln\pi}$$
($\lambda_1=11.532$; weight $x^{-5}$; verified symbolically.)

### (k) $x^2y''+4xy'+4\lambda y=0,\ y'(0)=0,\ y(2)=0$

**As printed (singular at $x=0$).** Roots of $m^2+3m+4\lambda=0$ sum to $-3$, so at least one root has $\operatorname{Re}m\le-\tfrac32$, giving a solution $\sim x^{m}$ that is unbounded at $0$ together with its derivative. A solution with $y'(0)=0$ must avoid every such branch, so it must be the other root $m_+$ alone with $m_+>1$, or $m=0$.
- Complex roots ($\lambda>9/16$): both branches $\sim x^{-3/2}$ oscillate and blow up. None.
- $m_+=0$, $m_-=-3$ ($\lambda=0$): $y=A$, but $y(2)=A=0$. None.
- Real roots with $m_+>1$ ($\lambda<-1$): $y=Ax^{m_+}$, $y(2)=0\Rightarrow A=0$. None.

**There are no eigenvalues.** The conditions as printed are inconsistent with a non-trivial solution.

**Regular version ($y'(1)=0,\ y(2)=0$).** $x=e^t$, $Y=e^{-3t/2}z$: $z''+\big(4\lambda-\tfrac94\big)z=0$, $t\in[0,\ln2]$. Put $4\lambda-\frac94=\omega^2$. $z=A\cos\omega t+B\sin\omega t$; $Y'(0)=0$ gives $\omega B=\tfrac32A$; $Y(\ln2)=0$ gives $z(\ln2)=0$:
$$\sin(\omega\ln2)+\tfrac{2\omega}3\cos(\omega\ln2)=0\iff\tan(\omega\ln2)=-\frac{2\omega}3.$$
$$\lambda_n=\frac{\omega_n^2+\frac94}4,\qquad y_n=x^{-3/2}\Big[\cos(\omega_n\ln x)+\frac3{2\omega_n}\sin(\omega_n\ln x)\Big],$$
with $\omega_n=2.9457,\ 7.0990,\ 11.5177,\dots$ and $\lambda_n=2.7318,\ 13.161,\ 33.727,\dots$ (weight $x^{2}$; verified symbolically). These are transcendental, which is why the printed version cannot have been meant to be solved in closed form either.

### (l) $x^2y''+xy'+\lambda y=0,\ y(1)=y(e)=0$
$t=\ln x$: $Y''+\lambda Y=0$, $Y(0)=Y(1)=0$.
$$\boxed{\lambda_n=n^2\pi^2,\quad y_n=\sin(n\pi\ln x),\quad n\ge1}\qquad\text{weight }1/x$$

### (m) $x^2y''-xy'+(\lambda+1)y=0,\ y(1)=y(e)=0$
$t=\ln x$: $Y''-2Y'+(\lambda+1)Y=0$. $Y=e^tz$: $z''+\lambda z=0$, $z(0)=z(1)=0$.
$$\boxed{\lambda_n=n^2\pi^2,\quad y_n=x\sin(n\pi\ln x),\quad n\ge1}\qquad\text{weight }x^{-3}$$
(S–L form: $p=x^{-1}$, $\big(y'/x\big)'+\dfrac{\lambda+1}{x^3}y=0$.)

### Summary table

| | $p$ | weight $r$ | $\lambda_n$ | $y_n$ |
|---|---|---|---|---|
| (a) | 1 | 1 | $\big(\frac{2n-1}2\big)^2$ | $\sin\frac{(2n-1)x}2$ |
| (b) | $e^{4x}$ | $e^{4x}$ (eigenparam. $-\lambda$) | $0;\ -(4+\frac{n^2\pi^2}4)$ | $1;\ e^{-2x}[\frac{n\pi}2\cos\frac{n\pi x}2+2\sin\frac{n\pi x}2]$ |
| (c) | 1 | 1 | $n^2$ (double) | $1,\ \cos nx,\ \sin nx$ |
| (d) | $e^{2x}$ | $e^{2x}$ | $n^2$ | $e^{-x}\sin nx$ |
| (e) | $e^{-x}$ | $e^{-x}$ | $\frac14+\frac{n^2\pi^2}{L^2}$ | $e^{x/2}\sin\frac{n\pi x}L$ |
| (f) | $x$ | $1/x$ | $\big(\frac{(2n-1)\pi}2\big)^2$ | $\sin(\frac{(2n-1)\pi}2\ln x)$ |
| (g) | $e^{2x}$ | $e^{-2x}$ | $\frac{4n^2\pi^2}{(1-e^{-2\pi})^2}-1$ | $\sin\big(n\pi\frac{e^{-2x}-e^{-2\pi}}{1-e^{-2\pi}}\big)$ |
| (h) | $4e^{-x}$ | $e^{x}$ | $\frac{4n^2\pi^2}{(e-1)^2}-1$ | $\sin\big(n\pi\frac{e^x-1}{e-1}\big)$ |
| (i) | $x^2+1$ | $\frac1{x^2+1}$ | $16n^2$ | $\cos(4n\arctan x)$ |
| (j) | $x^{-3}$ | $x^{-5}$ | as printed: $\{0\}\cup(3,\infty)$; regular: $0,\ 4+\frac{n^2\pi^2}{\ln^2\pi}$ | regular: $x^2[\omega\cos(\omega\ln x)-2\sin(\omega\ln x)]$ |
| (k) | $x^{4}$ | $x^2$ | as printed: none; regular: transcendental | regular: $x^{-3/2}[\cos+\frac3{2\omega}\sin]$ |
| (l) | $x$ | $1/x$ | $n^2\pi^2$ | $\sin(n\pi\ln x)$ |
| (m) | $x^{-1}$ | $x^{-3}$ | $n^2\pi^2$ | $x\sin(n\pi\ln x)$ |

![[A7-fig1-eigenfunctions.png]]

First three eigenfunctions of each problem (each normalised to maximum 1). The number of interior zeros of $y_n$ grows with $n$ (oscillation theorem). The last panel shows the pathological spectrum of (j) as printed.

---

## Q4

> [!question] State the orthogonality conclusion for each SLP.

**(a)** $y''+\lambda y=0,\ y(0)=0,\ y'(1)=0$: $\lambda_n=\big(\tfrac{2n-1}2\pi\big)^2$, $y_n=\sin\big((n-\tfrac12)\pi x\big)$.
$$\int_0^1\sin\big((m-\tfrac12)\pi x\big)\sin\big((n-\tfrac12)\pi x\big)\,dx=0\quad(m\ne n),\qquad\|y_n\|^2=\tfrac12.$$
**(b)** $y''+\lambda y=0,\ y'(0)=0,\ y(1)+y'(1)=0$: $y=\cos\mu x$, $\lambda=\mu^2$. The condition is $\cos\mu-\mu\sin\mu=0$, i.e. $\mu\tan\mu=1$, with positive roots $\mu_n=0.8603,\ 3.4256,\ 6.4373,\ 9.5293,\dots$ (one root in each interval $\big((n-1)\pi,\,(n-1)\pi+\tfrac\pi2\big)$). ($\lambda\le0$ gives nothing: $\lambda=0$ gives $y=A$, $y(1)+y'(1)=A\ne0$; $\lambda<0$ gives $\cosh\kappa+\kappa\sinh\kappa>0$.)
$$\int_0^1\cos\mu_mx\cos\mu_nx\,dx=0\quad(m\ne n),\qquad\|y_n\|^2=\frac12+\frac{\sin2\mu_n}{4\mu_n}=\frac12\big(1+\sin^2\mu_n\big)$$
(the last form uses $\cos\mu_n=\mu_n\sin\mu_n$). The Robin condition does not change the weight, only the eigenvalues.

**(c)** $y(0)=y(L)=0$: $y_n=\sin\dfrac{n\pi x}L$,
$$\int_0^L\sin\frac{m\pi x}L\sin\frac{n\pi x}L\,dx=0\quad(m\ne n),\qquad\|y_n\|^2=\frac L2.$$
**(d)** Parametric Bessel of order $m$ on $(0,a)$, $y(0)$ finite, $y(a)=0$: $y=J_m(\lambda x)$ with $J_m(\lambda a)=0$, i.e. $\lambda_k=\alpha_{m,k}/a$ (the $k$-th positive zero of $J_m$). S–L form (Q1): $p=x,\ r=x$, eigenvalue $\lambda^2$.
$$\int_0^a x\,J_m(\lambda_jx)J_m(\lambda_kx)\,dx=0\quad(j\ne k),\qquad\|y_k\|^2=\frac{a^2}2J_{m+1}(\lambda_ka)^2.$$
Here the boundary term $p(uv'-u'v)$ vanishes at $x=0$ because $p(0)=0$ and $y$ is bounded (singular SLP), and at $x=a$ because $y(a)=0$. The weight $x$ is essential: the functions $J_m(\lambda_kx)$ are *not* orthogonal with weight $1$ (see Assignment 6, Q12).

![[A7-fig2-orthogonality.png]]

Normalised Gram matrices for (a)–(d) (numerical quadrature): off-diagonal entries are $10^{-16}$.

---

## Q5

> [!question] Eigenfunction expansions $\sum a_ny_n$ using the eigenfunctions of 4(a).

With $y_n=\sin\mu_nx$, $\mu_n=(n-\tfrac12)\pi$, $\|y_n\|^2=\tfrac12$ and weight $1$:
$$a_n=2\int_0^1f(x)\sin\mu_nx\,dx.$$
Useful: $\cos\mu_n=0$ and $\sin\mu_n=(-1)^{n+1}$, $\displaystyle\int_0^1\sin\mu x\,dx=\frac{1}{\mu}$, $\displaystyle\int_0^1x\sin\mu x\,dx=\frac{\sin\mu}{\mu^2}$ (both because $\cos\mu_n=0$).

**(a) $f=1$.** $a_n=\dfrac2{\mu_n}$:
$$\boxed{1\sim\frac4\pi\sum_{n\ge1}\frac1{2n-1}\sin\frac{(2n-1)\pi x}2}$$
**(b) $f=x$.** $a_n=\dfrac{2\sin\mu_n}{\mu_n^2}$:
$$\boxed{x\sim\frac8{\pi^2}\sum_{n\ge1}\frac{(-1)^{n+1}}{(2n-1)^2}\sin\frac{(2n-1)\pi x}2}$$
**(c) $f=1-x$.** (a) − (b):
$$\boxed{a_n=\frac4{(2n-1)\pi}-\frac{8(-1)^{n+1}}{(2n-1)^2\pi^2}}$$
**(c′) step: $1$ on $[0,\tfrac12)$, $0$ on $[\tfrac12,1]$.** $a_n=2\displaystyle\int_0^{1/2}\sin\mu_nx\,dx=\dfrac{2\big(1-\cos\frac{\mu_n}2\big)}{\mu_n}$:
$$\boxed{a_n=\frac{4\Big(1-\cos\frac{(2n-1)\pi}4\Big)}{(2n-1)\pi}}$$
(with $\cos\frac{(2n-1)\pi}4=\tfrac{\sqrt2}2,-\tfrac{\sqrt2}2,-\tfrac{\sqrt2}2,\tfrac{\sqrt2}2$ repeating for $n=1,2,3,4,\dots$).

**(d) $f=2x$ on $[0,\tfrac12)$, $1$ on $[\tfrac12,1]$** (continuous). With $\displaystyle\int_0^{1/2}x\sin\mu x\,dx=-\frac{\cos\frac\mu2}{2\mu}+\frac{\sin\frac\mu2}{\mu^2}$ and $\displaystyle\int_{1/2}^1\sin\mu x\,dx=\frac{\cos\frac\mu2}\mu$ (since $\cos\mu_n=0$), the cosine terms cancel:
$$a_n=2\Big[-\frac{\cos\frac{\mu_n}2}{\mu_n}+\frac{2\sin\frac{\mu_n}2}{\mu_n^2}+\frac{\cos\frac{\mu_n}2}{\mu_n}\Big]=\frac{4\sin\frac{\mu_n}2}{\mu_n^2}$$
$$\boxed{a_n=\frac{16\,\sin\frac{(2n-1)\pi}4}{(2n-1)^2\pi^2}}$$

| $n$ | (a) | (b) | (c) | (c′) | (d) |
|---|---|---|---|---|---|
| 1 | 1.2732 | 0.8106 | 0.4627 | 0.3729 | 1.1463 |
| 2 | 0.4244 | −0.0901 | 0.5145 | 0.7245 | 0.1274 |
| 3 | 0.2546 | 0.0324 | 0.2222 | 0.4347 | −0.0459 |
| 4 | 0.1819 | −0.0165 | 0.1984 | 0.0533 | −0.0234 |

**Convergence.** All series converge in the weighted $L^2$ norm ($\sum a_n^2/2=\|f\|^2$, Parseval). Pointwise: (a), (c), (c′) behave like $1/n$ because $f(0)\neq0$ (the eigenfunctions vanish at $0$) or $f$ jumps; the series converge to the midpoint at the jump $x=\frac12$ and show Gibbs overshoot, and at $x=0$ the sum is $0\neq f(0)=1$. (b) and (d) are continuous with $f(0)=0$, so $a_n=O(n^{-2})$ and the convergence is uniform; (b) has $f'(1)\ne0$ whereas the basis has $y_n'(1)=0$, so the series converges uniformly but slowly at the right end.

![[A7-fig3-expansions-4a.png]]
![[A7-fig5-decay.png]]

---

## Q6

> [!question] Orthonormal eigenfunction expansions $\sum a_ny_n$ using the normalised eigenfunctions of 4(b).

The normalised functions are $\varphi_n=\dfrac{\cos\mu_nx}{\sqrt{N_n}}$ with $N_n=\tfrac12\big(1+\sin^2\mu_n\big)$, where $\mu\tan\mu=1$ (Q4(b)). Then
$$a_n=\int_0^1f\,\varphi_n\,dx=\frac{c_n}{\sqrt{N_n}},\qquad c_n=\int_0^1f\cos\mu_nx\,dx,\qquad f\sim\sum a_n\varphi_n=\sum\frac{c_n}{N_n}\cos\mu_nx.$$
With $\displaystyle\int_0^1\cos\mu x\,dx=\frac{\sin\mu}\mu$ and $\displaystyle\int_0^1x\cos\mu x\,dx=\frac{\sin\mu}\mu+\frac{\cos\mu-1}{\mu^2}$:

| | $c_n=\int_0^1f\cos\mu_nx\,dx$ |
|---|---|
| (a) $f=1$ | $\dfrac{\sin\mu_n}{\mu_n}$ |
| (b) $f=x$ | $\dfrac{\sin\mu_n}{\mu_n}+\dfrac{\cos\mu_n-1}{\mu_n^2}$ |
| (c) $f=1-x$ | $\dfrac{1-\cos\mu_n}{\mu_n^2}$ |
| (c′) step | $\dfrac{\sin\frac{\mu_n}2}{\mu_n}$ |
| (d) $2x$ on $[0,\tfrac12)$, $1$ after | $\dfrac{\sin\mu_n}{\mu_n}+\dfrac{2\big(\cos\frac{\mu_n}2-1\big)}{\mu_n^2}$ |

The (d) entry uses $\displaystyle\int_0^{1/2}2x\cos\mu x\,dx=\frac{\sin\frac\mu2}\mu+\frac{2\left(\cos\frac\mu2-1\right)}{\mu^2}$ and $\displaystyle\int_{1/2}^1\cos\mu x\,dx=\frac{\sin\mu-\sin\frac\mu2}\mu$. Using $\cos\mu_n=\mu_n\sin\mu_n$ one may replace $\frac{\sin\mu}\mu$ by $\frac{\cos\mu}{\mu^2}$ throughout.

Numerically ($\mu_n=0.8603,\ 3.4256,\ 6.4373,\ 9.5293$; $N_n=0.7873,\ 0.5393,\ 0.5118,\ 0.5055$):

| $n$ | $a_n$ (a) | (b) | (c) | (c′) | (d) |
|---|---|---|---|---|---|
| 1 | 0.9930 | 0.4634 | 0.5296 | 0.5463 | 0.7156 |
| 2 | −0.1114 | −0.3388 | 0.2274 | 0.3935 | −0.3763 |
| 3 | 0.0333 | 0.0329 | 0.0004 | −0.0167 | −0.1014 |
| 4 | −0.0154 | −0.0463 | 0.0309 | −0.1474 | −0.0448 |

The equivalent non-normalised coefficients $c_n/N_n$ of $\cos\mu_nx$, e.g. for $f=1$: $1.1191,-0.1517,0.0466,-0.0217$.

**Convergence.** Unlike the sine basis of Q5, this basis does not force $f(0)=0$ ($y_n(0)=1$), and the Robin end $y(1)+y'(1)=0$ does not force $f(1)=0$ either. So (a), (b), (c), (d) are all continuous functions that the series reproduces at both endpoints with no Gibbs behaviour, while the step function (c′) still converges to the midpoint $\tfrac12$ at its jump $x=\tfrac12$ with Gibbs overshoot.

![[A7-fig4-expansions-4b.png]]

---

## Q7

> [!question] Prove (a) Lagrange's identity and (b) Green's identity for $L=\dfrac d{dx}\Big(p\dfrac d{dx}\Big)+q$.

**(a)** $uLv=u(pv')'+quv$ and $vLu=v(pu')'+quv$, so the $q$ terms cancel:
$$uLv-vLu=u(pv')'-v(pu')'.$$
On the other hand
$$\big[p(uv'-u'v)\big]'=(puv')'-(pu'v)'=u'pv'+u(pv')'-(pu')'v-pu'v'=u(pv')'-v(pu')'.$$
These agree. ∎

**(b)** Integrate (a) from $a$ to $b$:
$$\int_a^b(uLv-vLu)\,dx=\Big[p(uv'-u'v)\Big]_a^b.\ ∎$$

**Use.** If $u,v$ satisfy the same separated, periodic or singular-end boundary conditions the right side vanishes, $\langle u,Lv\rangle=\langle Lu,v\rangle$ (self-adjoint), and for eigenfunctions $Lu=-\lambda_mru$, $Lv=-\lambda_nrv$ the identity becomes $(\lambda_m-\lambda_n)\int ruv=0$ (§0.3): this is the proof of the orthogonality used throughout Q3–Q6.

---

## Summary

> [!success] Results at a glance
> | Q | Result |
> |---|---|
> | 1 | Bessel: $p=x,q=-m^2/x,r=x$ · Legendre: $p=1-x^2,q=0,r=1$ · Chebyshev: $p=\sqrt{1-x^2},q=0,r=1/\sqrt{1-x^2}$ |
> | 2 | multiply by $p=e^{\int f}$: $py''+pfy'=(py')'$ |
> | 3 | (a) $((2n-1)/2)^2$ · (b) $0,\ -(4+n^2\pi^2/4)$ · (c) $n^2$ double · (d) $n^2$ · (e) $\frac14+n^2\pi^2/L^2$ · (f) $((2n-1)\pi/2)^2$ · (g) $\frac{4n^2\pi^2}{(1-e^{-2\pi})^2}-1$ · (h) $\frac{4n^2\pi^2}{(e-1)^2}-1$ · (i) $16n^2$ · (j), (k) singular as printed, regular variants given · (l), (m) $n^2\pi^2$ |
> | 4 | weights $1,1,1,x$; norms $\frac12,\ \frac12(1+\sin^2\mu_n),\ \frac L2,\ \frac{a^2}2J_{m+1}^2$; (b) roots of $\mu\tan\mu=1$ |
> | 5 | $a_n$: $\frac4{(2n-1)\pi}$ · $\frac{8(-1)^{n+1}}{(2n-1)^2\pi^2}$ · difference · $\frac{4(1-\cos\frac{(2n-1)\pi}4)}{(2n-1)\pi}$ · $\frac{16\sin\frac{(2n-1)\pi}4}{(2n-1)^2\pi^2}$ |
> | 6 | $a_n=c_n/\sqrt{N_n}$ with $c_n$ in the table |
> | 7 | $uLv-vLu=[p(uv'-u'v)]'$ |

### Quick revision
- [ ] SL form: multiply by $p=e^{\int f}$; weight $r=hp$
- [ ] Orthogonality holds with weight $r$, not 1 (Bessel: weight $x$)
- [ ] Remove a first-derivative term with $y=e^{-\frac12\int f}z$; Euler equations with $x=e^t$; exponentially weighted ones with $s=\int\!\sqrt{r/p}$
- [ ] A boundary condition at a singular endpoint (here $x=0$ in (j), (k)) is not a regular SLP: look at what the Lagrange boundary term does
- [ ] Coefficient formula $a_n=\int rfy_n/\int ry_n^2$; convergence is fast only if $f$ satisfies the basis' boundary conditions

### Figure index
`A7-fig1` eigenfunctions · `fig2` Gram matrices · `fig3` Q5 expansions · `fig4` Q6 expansions · `fig5` coefficient decay and $L^2$ error. All in `assets/`. Verification: `Tools/de_a6a7.py`.

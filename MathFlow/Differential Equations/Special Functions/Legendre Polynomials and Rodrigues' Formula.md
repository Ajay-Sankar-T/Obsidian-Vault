---
title: Legendre Polynomials and Rodrigues' Formula
tags: [differential-equations, special-functions, legendre, rodrigues]
source: "[[Lecture-18.pdf]], [[Lecture-19.pdf]] (slides 1–9)"
---

Related: [[Legendre's Equation]] · [[Power Series Method]] · [[Generating Function of Legendre Polynomials]] · [[Orthogonality and Norm of Legendre Polynomials]] · [[Special Functions - MOC]]

## 1. Legendre's equation

$$(1-x^2)y''-2xy'+p(p+1)y=0\qquad\Big(\text{self-adjoint form } \big((1-x^2)y'\big)'+p(p+1)y=0\Big)$$

$p$ is a real parameter. Singular points: $x=\pm1$ and $x=\infty$, all **regular** (a *Fuchsian* equation). $x=0$ is ordinary, so $y=\sum a_nx^n$ converges for $|x|<1$ (distance to the nearest singular point; see [[Radius of Convergence of Series Solutions]]). Appears in potential theory, gravitation, heat conduction and waves on spheres.

![[DE-S5-legendre-equation.png]]
**Figure:** For integer $p=n$ one solution is the polynomial $P_n$ (left); the other solution $Q_n$ is an infinite series with logarithmic singularities at $x=\pm1$ (middle). For non-integer $p$ both series are infinite (right).

## 2. Series solution

Substitute $y=\sum a_nx^n$:
$$(n+2)(n+1)a_{n+2}=\big[n(n+1)-p(p+1)\big]a_n\ \Longrightarrow\ \boxed{a_{n+2}=-\frac{(p-n)(p+n+1)}{(n+1)(n+2)}\,a_n}$$
$$y=a_0y_1+a_1y_2,\qquad y_1=1-\frac{p(p+1)}{2!}x^2+\frac{p(p-2)(p+1)(p+3)}{4!}x^4-\cdots\ (\text{even}),$$
$$y_2=x-\frac{(p-1)(p+2)}{3!}x^3+\frac{(p-1)(p-3)(p+2)(p+4)}{5!}x^5-\cdots\ (\text{odd})$$
The ratio of consecutive terms tends to $|x|^2$, so both series have radius of convergence $1$.

**Integer $p$.** The factor $(p-n)$ vanishes at $n=p$, so the series with the same parity as $p$ **terminates**:

| $p$ | solution | degree | value at 1 |
|---|---|---|---|
| 0 | $y_1=1$ | 0 | 1 |
| 1 | $y_2=x$ | 1 | 1 |
| 2 | $y_1=1-3x^2$ | 2 | $-2$ |
| 3 | $y_2=x-\tfrac53x^3$ | 3 | $-\tfrac23$ |

In each row the *other* series ($y_2$ for even $p$, $y_1$ for odd $p$) stays an infinite series, so exactly one of $y_1,y_2$ is a polynomial. Even $p$ gives $y_1$ (even powers only), odd $p$ gives $y_2$.

## 3. Definition of $P_n$

> $P_n(x)$ is the polynomial solution of $(1-x^2)y''-2xy'+n(n+1)y=0$ normalised by $P_n(1)=1$.

Rescale the polynomials above: $P_2=-\tfrac12(1-3x^2)$, $P_3=-\tfrac32(x-\tfrac53x^3)$. Equivalent: choose the leading coefficient $a_n=\dfrac{(2n)!}{2^n(n!)^2}$ and run the recurrence backwards, giving

$$\boxed{P_n(x)=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{(-1)^k(2n-2k)!}{2^n\,k!\,(n-k)!\,(n-2k)!}\,x^{n-2k}}$$

$$P_0=1,\ P_1=x,\ P_2=\tfrac12(3x^2-1),\ P_3=\tfrac12(5x^3-3x),\ P_4=\tfrac18(35x^4-30x^2+3),\ P_5=\tfrac18(63x^5-70x^3+15x)$$

![[DE-N4-legendre-polynomials.png]]
**Figure:** Left: $P_0$–$P_5$ all pass through $(1,1)$; even $n$ ⇒ even function, odd $n$ ⇒ odd; $n$ simple zeros in $(-1,1)$; $|P_n|\le1$ on $[-1,1]$. Middle: Rodrigues' construction. Right: $P_n(1)=1$, $P_n(-1)=(-1)^n$, $P_n(0)=0$ for odd $n$.

## 4. Rodrigues' formula

$$\boxed{P_n(x)=\frac1{2^nn!}\frac{d^n}{dx^n}(x^2-1)^n}$$

**Method 1 (from the explicit sum).** Since $\dfrac{d^n}{dx^n}x^{2n-2k}=\dfrac{(2n-2k)!}{(n-2k)!}x^{n-2k}$ (and for $k>\lfloor n/2\rfloor$ the $n$th derivative is 0),
$$P_n=\frac1{2^nn!}\frac{d^n}{dx^n}\sum_{k=0}^n(-1)^k\frac{n!}{k!(n-k)!}x^{2n-2k}=\frac1{2^nn!}\frac{d^n}{dx^n}(x^2-1)^n$$
by the binomial theorem.

**Method 2 (independent derivation).** Let $z=(x^2-1)^n$, so $(x^2-1)z'=2nxz$. Differentiating this $n+1$ times (Leibniz) gives $(1-x^2)u''-2xu'+n(n+1)u=0$ for $u=\dfrac{d^nz}{dx^n}$: **$u$ solves Legendre's equation**, so $u=C\,P_n$. Fix $C$ by $x=1$: write $z=(x+1)^n(x-1)^n$; by Leibniz's rule only the term with all $n$ derivatives on $(x-1)^n$ survives at $x=1$, giving $u(1)=n!\,2^n$. Since $P_n(1)=1$, $C=2^nn!$.

**Proof that $P_n(1)=1$ directly:** every Leibniz term except $k=0$ contains a factor $(x-1)$, and the $k=0$ term is $(x+1)^nn!\to2^nn!$.

**Example ($P_4,P_5$).** $(x^2-1)^4=x^8-4x^6+6x^4-4x^2+1$; $D^4$ then divide by $2^44!=384$ gives $P_4=\tfrac18(35x^4-30x^2+3)$; likewise $P_5=\tfrac18(63x^5-70x^3+15x)$. Checks: $P_4(1)=\tfrac18(35-30+3)=1$, $P_5(1)=\tfrac18(63-70+15)=1$. (Verified symbolically for $n\le8$: explicit sum = Rodrigues = Legendre solution.)

**Uses.** Rodrigues' formula proves the **norm** and **orthogonality** ([[Orthogonality and Norm of Legendre Polynomials]]) by repeated integration by parts, gives $\int x^pP_n\,dx$, and shows all $n$ roots are real and in $(-1,1)$ (Rolle's theorem applied to $D^k(x^2-1)^n$ — the middle panel).

## Problems using this
- [[Assignment 5 - Legendre Polynomials and Functions - Solutions#0. Theory toolkit|Assignment 5, theory toolkit]] and Q1–Q2 (basics, roots via Rodrigues).
- Series at an ordinary point, $p(p+1)$ case: [[Assignment 4 - Series Solutions - Solutions#Q1 Power series at ordinary points|Assignment 4, Q1(b)]].

## Next
[[Generating Function of Legendre Polynomials]]

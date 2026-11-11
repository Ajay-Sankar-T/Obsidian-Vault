---
title: Bessel's Equation and Bessel Functions of the First Kind
tags: [differential-equations, special-functions, bessel, frobenius]
source: "[[Lecture-23.pdf]] (slides 10–13), [[Lecture-24.pdf]] (slides 1–5, 9)"
---

Related: [[Gamma Function]] · [[Frobenius Method - Indicial Equation and Three Cases]] · [[Frobenius Method - Worked Examples]] · [[Bessel Functions of the Second Kind and General Solution]] · [[Bessel Function Properties and Recurrence Relations]] · [[Special Functions - MOC]]

## 1. Bessel's equation

$$x^2y''+xy'+(x^2-\nu^2)y=0,\qquad\nu\ge0$$
Arises for circular/cylindrical symmetry: vibrations of a drum, heat conduction in a cylinder, the radial part of Laplace's equation in cylindrical/spherical coordinates (Bessel met it in planetary motion/Kepler's equation). In standard form $y''+\frac1xy'+\frac{x^2-\nu^2}{x^2}y=0$: $xP=1$, $x^2Q=x^2-\nu^2$ are analytic, so $x=0$ is a **regular singular point** (generally not ordinary) and Frobenius' method applies.

## 2. Frobenius solution at $x=0$

Put $y=x^r\sum a_nx^n$, $a_0\ne0$, $\rho(r)=r^2-\nu^2$:
$$\rho(r)a_0+\rho(r+1)a_1x+\sum_{n\ge2}\big[\rho(n+r)a_n+a_{n-2}\big]x^n=0$$
- indicial equation $r^2-\nu^2=0$ ⇒ $r_1=\nu,\ r_2=-\nu$ (difference $2\nu$),
- $\rho(r+1)a_1=0$ ⇒ $a_1=0$ (for $r=\nu$), so all odd coefficients vanish,
- $a_n=-\dfrac{a_{n-2}}{n(n+2\nu)}$ for $r=\nu$, giving $a_{2n}=\dfrac{(-1)^na_0}{2^{2n}n!\,(\nu+1)(\nu+2)\cdots(\nu+n)}$.

Choose $a_0=\dfrac1{2^\nu\Gamma(\nu+1)}$ and use $\Gamma(\nu+1)(\nu+1)\cdots(\nu+n)=\Gamma(n+\nu+1)$:

$$\boxed{J_\nu(x)=\sum_{n=0}^\infty\frac{(-1)^n}{n!\,\Gamma(n+\nu+1)}\Big(\frac x2\Big)^{2n+\nu}}$$

the **Bessel function of the first kind of order $\nu$**. It converges for all $x$ ($x=0$ is the only singular point). $J_0(0)=1$, $J_\nu(0)=0$ for $\nu>0$. For $\nu=0$: $J_0=1-\tfrac{x^2}4+\tfrac{x^4}{64}-\cdots$.

![[DE-N11-bessel-first-kind.png]]
**Figure:** Left: $J_0,\dots,J_4$ oscillate with a slowly decaying envelope $\sqrt{2/\pi x}$ — not periodic like sine/cosine. Middle: the series converges for all $x$ (more terms are needed at large $x$). Right: zeros — $J_0$ first vanishes at $2.405$, $J_1$ at $3.832$ (next zeros: $J_0$: $5.520,\ 8.654$; $J_1$: $7.016,\ 10.173$).

**Large $x$:** $J_n(x)\sim\sqrt{\dfrac2{\pi x}}\cos\Big(x-\dfrac{n\pi}2-\dfrac\pi4\Big)$.

## 3. The second solution: three cases for $r_1-r_2=2\nu$

Repeat the calculation with $\nu\to-\nu$:
$$J_{-\nu}(x)=\sum_{n\ge0}\frac{(-1)^n}{n!\,\Gamma(n-\nu+1)}\Big(\frac x2\Big)^{2n-\nu}$$

| Case | $\nu$ | Second solution |
|---|---|---|
| **1** | $2\nu\notin\{0,1,2,\dots\}$ (e.g. $\nu=\tfrac14$, $0.3$, $\sqrt2$) | $J_{-\nu}$: general solution $C_1J_\nu+C_2J_{-\nu}$ ($J_{-\nu}$ is unbounded at 0, so independent) |
| **2** | $\nu=0$ ($r_1=r_2$) | no second Frobenius series; log required |
| **3a** | $\nu$ half an odd integer, $2\nu=1,3,5,\dots$ ($\nu=\tfrac12,\tfrac32,\dots$) | the recurrence gives $0\cdot a_{2k+1}=0$, so $a_{2k+1}$ is free, **no log**: $J_{-\nu}$ still works |
| **3b** | $\nu=m\in\{1,2,3,\dots\}$ | $n(n-2m)a_n=-a_{n-2}$ forces $0\cdot a_{2m}=-a_{2m-2}\ne0$ — **contradiction**; no second Frobenius series |

For integer order: $\displaystyle J_{-m}(x)=\sum_{n\ge m}\frac{(-1)^n}{n!\,\Gamma(n-m+1)}\Big(\frac x2\Big)^{2n-m}=(-1)^mJ_m(x)$ (the terms $n<m$ vanish because $1/\Gamma(k)=0$ for $k=0,-1,\dots$; substitute $n=m+k$). So $J_m$ and $J_{-m}$ are **linearly dependent** and a genuinely different second solution is needed: [[Bessel Functions of the Second Kind and General Solution]].

## 4. Summary

$$y=C_1J_\nu(x)+C_2J_{-\nu}(x)\ \ (\nu\notin\mathbb Z),\qquad y=C_1J_\nu(x)+C_2Y_\nu(x)\ \ (\text{all }\nu\ge0)$$

## Verified
Series for $\nu=0,1,2,\tfrac12,-\tfrac12,\tfrac14,1.7$ agree with library values to $10^{-10}$; $J_{-m}=(-1)^mJ_m$ for $m=1,2,3$; zeros $2.404826$ and $3.831706$.

## Problems using this
- Bessel-type reduction inside a Frobenius problem: [[Assignment 4 - Series Solutions - Solutions#Q3 Frobenius method|Assignment 4, Q3(c)]] (the equation $16x^2y''+(x^2+3)y=0$ becomes a Bessel equation of order $	frac14$) and the Frobenius problems of [[Frobenius Method - Worked Examples]].
- [[Assignment 6 - Bessel Functions - Solutions]] (source [[Assignment-6.pdf]]): Q1 ($J_{-n}=(-1)^nJ_n$), Q6 (equations reduced to Bessel form by a substitution, e.g. $y''+4xy=0$ with $y=u\sqrt x$), Q4 (Wronskian of two Bessel solutions $=c/x$, by [[Abel's Formula]] with $P=\frac1x$).

## Next
[[Bessel Functions of the Second Kind and General Solution]] → [[Bessel Function Properties and Recurrence Relations]] → [[Bessel Generating Function]]

## See also
- [[Legendre Polynomials and Rodrigues' Formula]] — Legendre's equation has an ordinary point at 0, Bessel's a regular singular point: the Frobenius method covers both.

---
title: Bessel Generating Function
tags: [differential-equations, special-functions, bessel, generating-function]
source: "[[Lecture-25.pdf]] (slides 11–15)"
---

Related: [[Bessel's Equation and Bessel Functions of the First Kind]] · [[Bessel Function Properties and Recurrence Relations]] · [[Generating Function of Legendre Polynomials]] (the Legendre analogue) · [[Special Functions - MOC]]

## Statement

For **integer** order, one closed form packages the whole family $\{J_n\}_{n\in\mathbb Z}$:

$$\boxed{e^{\frac x2\left(t-\frac1t\right)}=\sum_{n=-\infty}^{\infty}J_n(x)\,t^n}\qquad(t\ne0)$$

$J_n(x)$ is the coefficient of $t^n$ in the **Laurent** expansion in $t$ (two-sided, unlike the Legendre generating function which is a Taylor series).

![[DE-N14-bessel-generating.png]]
**Figure:** Left (a consequence): $t=e^{i\theta}$ gives $\cos(x\sin\theta)=J_0+2\sum J_{2k}\cos2k\theta$. Middle: the two-sided sum reproduces the exponential. Right: Laurent coefficients at $x=3$ with $J_{-n}=(-1)^nJ_n$.

## Proof

Write $e^{\frac x2(t-1/t)}=e^{xt/2}\,e^{-x/(2t)}$ and expand both exponentials:
$$e^{xt/2}=\sum_{r\ge0}\frac1{r!}\Big(\frac{xt}2\Big)^r,\qquad e^{-x/2t}=\sum_{s\ge0}\frac{(-1)^s}{s!}\Big(\frac x{2t}\Big)^s$$
$$e^{\frac x2(t-1/t)}=\sum_{r,s\ge0}\frac{(-1)^s}{r!\,s!}\Big(\frac x2\Big)^{r+s}t^{\,r-s}$$
- **Coefficient of $t^n$, $n\ge0$**: set $r=n+s$: $\ \displaystyle\sum_{s\ge0}\frac{(-1)^s}{(n+s)!\,s!}\Big(\frac x2\Big)^{n+2s}=J_n(x)$.
- **Coefficient of $t^{-m}$, $m>0$**: set $s=m+r$: $\ \displaystyle\sum_{r\ge0}\frac{(-1)^{r+m}}{r!\,(r+m)!}\Big(\frac x2\Big)^{m+2r}=(-1)^mJ_m(x)=J_{-m}(x)$.

Hence the coefficient of $t^n$ is $J_n(x)$ for every $n\in\mathbb Z$. ∎ (Numerically verified, $x=1.7,\ t=0.6$: agreement $<10^{-12}$ with $|n|\le40$.)

## Recurrences from $G$

1. **Differentiate in $t$:** $\tfrac x2\big(1+\tfrac1{t^2}\big)G=\sum nJ_nt^{n-1}$. Equate coefficients of $t^{n-1}$:
$$\boxed{2nJ_n(x)=x\,[J_{n-1}(x)+J_{n+1}(x)]}$$
2. **Differentiate in $x$:** $\tfrac12\big(t-\tfrac1t\big)G=\sum J_n'(x)t^n$. Equate coefficients of $t^n$:
$$\boxed{J_n'(x)=\tfrac12\,[J_{n-1}(x)-J_{n+1}(x)]}$$
These are (10) and (9) of [[Bessel Function Properties and Recurrence Relations]] (lecture homework), and they combine to $J_n'=\frac nxJ_n-J_{n+1}=-\frac nxJ_n+J_{n-1}$.

## Consequences

- **Symmetry:** $t\to-1/t$ leaves $G$ unchanged ⇒ $J_{-n}=(-1)^nJ_n$.
- **Argument sign:** $x\to-x$ is $t\to-t$ ⇒ $J_n(-x)=(-1)^nJ_n(x)$.
- **Sum rule (Assignment 6, Q10):** put $t=e^{i\theta}$: $e^{ix\sin\theta}=\sum J_ne^{in\theta}$. By Parseval, $\frac1{2\pi}\int_0^{2\pi}|e^{ix\sin\theta}|^2d\theta=1=\sum_nJ_n^2=J_0^2+2\sum_{n\ge1}J_n^2$. Hence $|J_0|\le1$ and $|J_n|\le\tfrac1{\sqrt2}$ for $n\ge1$.
- **Addition theorem** (standard): $J_n(x+y)=\sum_kJ_k(x)J_{n-k}(y)$, from $G(x+y)=G(x)G(y)$.
- **Integral form** (standard, Bessel's integral): $J_n(x)=\frac1\pi\int_0^\pi\cos(n\theta-x\sin\theta)\,d\theta$.

The sum rule was verified numerically ($x=3$: $J_0^2+2\sum J_n^2=1$).

## Problems using this
[[Assignment-6.pdf]] Q10 (sum rule and bounds); the recurrence proofs (Q2, Q7) can also be derived from $G$.

---
title: Generating Function of Legendre Polynomials
tags: [differential-equations, special-functions, legendre, generating-function]
source: "[[Lecture-19.pdf]] (slides 10–18)"
---

Related: [[Legendre Polynomials and Rodrigues' Formula]] · [[Legendre Recurrence Relations and Integrals]] · [[Orthogonality and Norm of Legendre Polynomials]] · [[Bessel Generating Function]] · [[Special Functions - MOC]]

## Statement

$$\boxed{G(x,t)=\frac1{\sqrt{1-2xt+t^2}}=\sum_{n=0}^\infty P_n(x)\,t^n}\qquad(|x|\le1,\ |t|<1)$$

One closed-form function encodes **every** $P_n$ as a Taylor coefficient in $t$.

![[DE-N5-generating-function.png]]
**Figure:** Left: the origin of $G$ — the inverse distance between two points is $\frac1d=\frac1r\sum P_n(\cos\theta)(r'/r)^n$ (potential theory). Middle: partial sums converge to $G$. Right: $|P_n(x)|\le1$ for $|x|\le1$, so the series in $t$ has radius 1.

## Proof

By the binomial theorem $(1+z)^{-1/2}=\sum_n\dfrac{(-\frac12)(-\frac32)\cdots(-\frac12-n+1)}{n!}z^n=\sum_n\dfrac{(-1)^n(2n)!}{2^{2n}(n!)^2}z^n$ for $|z|<1$. Put $z=t^2-2xt=t(t-2x)$:
$$(1-2xt+t^2)^{-1/2}=\sum_{n}\frac{(-1)^n(2n)!}{2^{2n}(n!)^2}\,t^n(t-2x)^n=\sum_n\sum_{k=0}^n(-1)^k\frac{(2n)!}{2^{2n}n!\,k!\,(n-k)!}\,t^{n+k}(2x)^{n-k}$$
Re-index so the power of $t$ is $m=n+k$ (i.e. $n\to m-k$); the coefficient of $t^m$ is
$$\sum_{k=0}^{\lfloor m/2\rfloor}(-1)^k\frac{(2m-2k)!}{2^m\,k!\,(m-k)!\,(m-2k)!}x^{m-2k}=P_m(x).\ \blacksquare$$
**Analyticity.** $1-2xt+t^2=(t-x)^2+(1-x^2)>0$ for real $t$ when $|x|<1$, so $G$ is analytic in $t$ and the series can be manipulated term by term.

## Consequences

| Setting | Result |
|---|---|
| $x=1$: $\frac1{1-t}=\sum P_n(1)t^n$ | $P_n(1)=1$ |
| $x=-1$: $\frac1{1+t}=\sum P_n(-1)t^n$ | $P_n(-1)=(-1)^n$ |
| $x=0$: $(1+t^2)^{-1/2}=\sum P_n(0)t^n$ (only even powers) | $P_{2m+1}(0)=0,\quad P_{2m}(0)=(-1)^m\dfrac{(2m)!}{2^{2m}(m!)^2}$ (e.g. $P_4(0)=\tfrac38$) |
| coefficients of $t^0,\dots,t^5$ | reproduce $P_0,\dots,P_5$ with no ODE solving |
| differentiate in $t$ or $x$ | the recurrences in [[Legendre Recurrence Relations and Integrals]] |
| square, integrate over $[-1,1]$ | the norm $\int P_n^2=\frac2{2n+1}$ ([[Orthogonality and Norm of Legendre Polynomials]]) |

**$G$ solves Legendre's equation termwise.** Applying $(1-x^2)\partial_x^2-2x\partial_x$ to $\sum P_nt^n$ gives $\sum t^n[(1-x^2)P_n''-2xP_n']=-\sum n(n+1)P_nt^n$.

## Problems using this
- [[Assignment 5 - Legendre Polynomials and Functions - Solutions#0. Theory toolkit|Assignment 5 toolkit]]: recurrences R1–R5 are all derived from $G$ (§0.4).
- [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q1|Q1]] (parity, $P_n(\pm1)$), [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q8|Q8]] ($\sum(2n+1)P_nt^n$), [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q9|Q9]] and [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q10|Q10]] (Laplace's integrals).

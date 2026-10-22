---
title: Legendre Recurrence Relations and Integrals
tags: [differential-equations, special-functions, legendre, recurrence, christoffel, beltrami]
source: "[[Lecture-22.pdf]]"
---

Related: [[Generating Function of Legendre Polynomials]] · [[Orthogonality and Norm of Legendre Polynomials]] · [[Legendre Polynomials and Rodrigues' Formula]] · [[Bessel Function Properties and Recurrence Relations]] (the Bessel analogue) · [[Special Functions - MOC]]

All identities below were verified symbolically for $n=1,\dots,7$.

## 1. The six recurrences

| # | Identity | Obtained from |
|---|---|---|
| **I** | $(2n+1)xP_n=(n+1)P_{n+1}+nP_{n-1}$ (equivalently $nP_n=(2n-1)xP_{n-1}-(n-1)P_{n-2}$) | $\partial_tG$ |
| **II** | $xP_n'-P_{n-1}'=nP_n$ | $\partial_tG$ and $\partial_xG$ |
| **III** | $P_{n+1}'-P_{n-1}'=(2n+1)P_n$ | differentiate I, use II |
| **IV** | $P_{n+1}'-xP_n'=(n+1)P_n$ | II and III |
| **V** | $(1-x^2)P_n'=n\,[P_{n-1}-xP_n]$ | IV ($n\to n-1$), II |
| **VI** | $(1-x^2)P_n'=(n+1)\,[xP_n-P_{n+1}]$ | I and V |

**Beltrami's result** $(n+1)\cdot$V $+\ n\cdot$VI:
$$\boxed{(2n+1)(1-x^2)P_n'=n(n+1)\,[P_{n-1}-P_{n+1}]}$$

(Assignment 5 Q4(c) as printed has the sign reversed; the identity above is the correct one — see the warning at the top of [[Assignment 5 - Legendre Polynomials and Functions - Solutions]].)

**Proof of I** (sketch). Differentiate $G=\sum P_nt^n$: $(x-t)(1-2xt+t^2)^{-3/2}=\sum nP_nt^{n-1}$. Multiply by $1-2xt+t^2$ and use $G$ again: $(x-t)\sum P_nt^n=(1-2xt+t^2)\sum nP_nt^{n-1}$; the coefficient of $t^n$ gives I.

**Use of I:** compute $P_{n+1}$ from $P_n,P_{n-1}$ without solving anything; it is also the numerically stable way to evaluate Legendre polynomials.

## 2. Christoffel's expansion

Iterating III ($P_n'=(2n-1)P_{n-1}+P_{n-2}'$) telescopes:
$$\boxed{P_n'(x)=(2n-1)P_{n-1}+(2n-5)P_{n-3}+(2n-9)P_{n-5}+\cdots}\quad\Longleftrightarrow\quad P_n'=\sum_{\substack{k=0\\ n-k\ \text{odd}}}^{n-1}(2k+1)P_k$$
ending in $3P_1$ ($n$ even) or $P_0$ ($n$ odd). So the derivative of a Legendre polynomial is a finite sum of undifferentiated ones, handy for integrating term by term. Examples: $P_5'=9P_4+5P_2+P_0$, $P_6'=11P_5+7P_3+3P_1$, $P_7'=13P_6+9P_4+5P_2+P_0$.

![[DE-N9-legendre-recurrences.png]]
**Figure:** Left: recurrence I holds pointwise ($n=4$). Middle: the coefficients $2k+1$ in Christoffel's expansion of $P_5'$. Right: $\int(P_n')^2=n(n+1)$.

## 3. Integrals by recurrence + orthogonality

Technique: replace $xP_n$ using I, expand products, then use $\int P_jP_k=\frac2{2k+1}\delta_{jk}$.

| Integral | Result |
|---|---|
| $\displaystyle\int_{-1}^1xP_nP_{n-1}\,dx$ | $\dfrac{2n}{(2n+1)(2n-1)}$ (check $n=1$: $\int x^2=\tfrac23$) |
| $\displaystyle\int_{-1}^1xP_nP_{n+1}\,dx=\int P_1P_nP_{n+1}$ | $\dfrac{2(n+1)}{(2n+1)(2n+3)}$ |
| $\displaystyle\int_{-1}^1x^2P_{n+1}P_{n-1}\,dx$ | $\dfrac{2n(n+1)}{(2n-1)(2n+1)(2n+3)}$ |
| $\displaystyle\int_{-1}^1x^2P_n^2\,dx$ | $\dfrac{2(n+1)^2}{(2n+3)(2n+1)^2}+\dfrac{2n^2}{(2n-1)(2n+1)^2}$ |
| $\displaystyle\int_{-1}^1P_n\,dx$ | $2$ if $n=0$, $0$ if $n\ge1$ |
| $\displaystyle\int_{-1}^1[P_n'(x)]^2dx$ | $n(n+1)$ (via Christoffel: $2\sum_{n-k\ \rm odd}(2k+1)$) |

**Derivations.**
- $\int x^2P_{n+1}P_{n-1}$: multiply $(2n-1)xP_{n-1}=nP_n+(n-1)P_{n-2}$ and $(2n+3)xP_{n+1}=(n+2)P_{n+2}+(n+1)P_n$; integrate; only $n(n+1)P_n^2$ survives, so $(2n+3)(2n-1)\int=n(n+1)\frac2{2n+1}$.
- $\int x^2P_n^2$: square I, integrate: $(2n+1)^2\int x^2P_n^2=(n+1)^2\frac2{2n+3}+n^2\frac2{2n-1}$ (cross term vanishes by orthogonality).
- $\int(P_n')^2$: $P_n'=\sum(2k+1)P_k$ ⇒ $\int=\sum(2k+1)^2\frac2{2k+1}=2\sum(2k+1)$. For $n=2m$: $2\sum_{j=1}^m(4j-1)=2m(2m+1)$; for $n=2m+1$: $2\sum_{j=0}^m(4j+1)=(2m+1)(2m+2)$. Both $=n(n+1)$.

**Check of III by hand:** $P_2'-P_0'=3x=3P_1$; $P_3'-P_1'=\tfrac12(15x^2-3)-1=5P_2$; $P_4'-P_2'=7P_3$.

## Problems using this
[[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q4|Assignment 5, Q4]] (identities (a)–(e), Christoffel for $P_6',P_7'$) and [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q7|Q7]] (the integrals). The sheet derives R1–R5 from $G$ in its toolkit §0.4.

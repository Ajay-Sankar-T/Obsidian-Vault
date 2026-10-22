---
title: Frobenius Method – Worked Examples
tags: [differential-equations, series-solutions, frobenius, worked-examples, bessel]
source: "[[Lecture-15.pdf]] (slides 8–16), [[Lectures-16-17.pdf]]"
---

Related: [[Frobenius Method - Indicial Equation and Three Cases]] · [[Frobenius Theorem]] · [[Bessel's Equation and Bessel Functions of the First Kind]] · [[Bessel Functions of the Second Kind and General Solution]] · [[Cauchy-Euler Equations]] · [[Series Solutions - MOC]]

All solutions below were checked symbolically (each closed form is substituted back into its ODE; truncated series have residual $O(x^{N})$).

![[DE-N2-frobenius-examples.png]]
**Figure:** Four of the examples: the $\cos\sqrt x$ / $\sin\sqrt x$ pair, the Case II pair with $\ln x/(1-x)$, the Euler equation, and a Case I pair.

## Example 1 (Case I): $2x^2y''+xy'-(x+1)y=0$

$xP=\tfrac12,\ x^2Q=-\tfrac{x+1}{2}$ ⇒ regular, $p_0=\tfrac12$, $q_0=-\tfrac12$. Indicial: $2r^2-r-1=0\Rightarrow (2r+1)(r-1)=0$, so $r_1=1,\ r_2=-\tfrac12$ (difference $\tfrac32$: Case I).

Recurrence: $\big[2(n+r)(n+r-1)+(n+r)-1\big]a_n=a_{n-1}$, i.e. $a_n=\dfrac{a_{n-1}}{(2(n+r)+1)(n+r-1)}$.

- $r=1$: $a_n=\dfrac{a_{n-1}}{n(2n+3)}$: $a_1=\tfrac15,\ a_2=\tfrac1{70},\ a_3=\tfrac1{1890}$ ⇒ $y_1=x\big(1+\tfrac x5+\tfrac{x^2}{70}+\cdots\big)$.
- $r=-\tfrac12$: $a_n=\dfrac{a_{n-1}}{2n(n-\frac32)}$: $a_1=-1,\ a_2=-\tfrac12,\ a_3=-\tfrac1{18}$ ⇒ $y_2=x^{-1/2}\big(1-x-\tfrac{x^2}{2}-\tfrac{x^3}{18}-\cdots\big)$.

> [!warning] Slide error (Lecture 15, slide 10)
> The slide writes $b_2=b_1/1$ and $y_2=x^{-1/2}(1-x+x^2-\cdots)$. With the recurrence on slide 9, $b_2=b_1/(2\cdot2\cdot\tfrac12)=b_1/2$, so the series is $1-x-\tfrac{x^2}{2}-\cdots$ (checked: the truncated series has residual $<10^{-7}$ at $x=0.1$).

## Example 2 (Case I, closed form): $4xy''+2y'+y=0$

$p_0=\tfrac12,\ q_0=0$; indicial $r(r-1)+\tfrac r2=0\Rightarrow r=0,\tfrac12$ (difference $\tfrac12$).
Recurrence: $a_m=\dfrac{-a_{m-1}}{2(m+r)(2(m+r)-1)}$.
- $r=0$: $a_m=\dfrac{-a_{m-1}}{2m(2m-1)}$ ⇒ $y_1=1-\tfrac x{2!}+\tfrac{x^2}{4!}-\cdots=\cos\sqrt x$.
- $r=\tfrac12$: $a_m=\dfrac{-a_{m-1}}{(2m+1)2m}$ ⇒ $y_2=x^{1/2}\big(1-\tfrac x6+\tfrac{x^2}{120}-\cdots\big)=\sin\sqrt x$.

$$y=C_1\cos\sqrt x+C_2\sin\sqrt x$$
(the substitution $x=u^2$ turns this into $y''+y=0$.)

## Example 3 (Case II): Bessel of order 0, $xy''+y'+xy=0$

$P=\tfrac1x,\ Q=1$ ⇒ $p_0=1,\ q_0=0$; indicial $r^2=0$, $r_1=r_2=0$.
Recurrence $(n+r)^2a_n+a_{n-2}=0$; at $r=0$: $n^2a_n=-a_{n-2}$ ⇒ $a_{odd}=0$, $a_{2k}=\dfrac{(-1)^k a_0}{2^{2k}(k!)^2}$.
$$y_1=J_0(x)=\sum_{k\ge0}\frac{(-1)^k}{2^{2k}(k!)^2}x^{2k}$$
Second solution (Case II form $y_1\ln x+\sum b_nx^n$): $b_{2k}=\dfrac{(-1)^{k+1}H_k}{2^{2k}(k!)^2}$, $H_k=1+\tfrac12+\cdots+\tfrac1k$:
$$y_2=J_0(x)\ln x+\sum_{k\ge1}\frac{(-1)^{k+1}H_k}{2^{2k}(k!)^2}x^{2k}$$
A normalised version is $Y_0(x)$ ([[Bessel Functions of the Second Kind and General Solution]]); $y_2\to-\infty$ as $x\to0^+$.

## Example 4 (Case II, closed form): $(x^2-x)y''+(3x-1)y'+y=0$

$P=\dfrac{3x-1}{x(x-1)}$ ⇒ $p_0=1$, $q_0=0$: indicial $r^2=0$ (Case II).
The recurrence collapses to $a_{m+1}=a_m$, so $y_1=\sum x^m=\dfrac1{1-x}$.
Reduction of order: $\int P\,dx=\ln|x|+2\ln|x-1|$, so
$$y_2=y_1\int\frac{e^{-\int P}}{y_1^2}dx=\frac1{1-x}\int(x-1)^2\frac1{x(x-1)^2}dx=\frac{\ln x}{1-x}$$
$$y=\frac{C_1+C_2\ln x}{1-x}$$
(here the series part of $y_2$ is identically zero).

## Example 5 (Case III, **no** log): Bessel order $\tfrac12$, $x^2y''+xy'+(x^2-\tfrac14)y=0$

Indicial: $r^2=\tfrac14$, $r_1=\tfrac12,\ r_2=-\tfrac12$, difference $1$ (Case III). Recurrence $\big[(n+r)^2-\tfrac14\big]a_n=-a_{n-2}$.
With $r=-\tfrac12$: $n(n-1)a_n=-a_{n-2}$. At $n=1$: $0\cdot a_1=-a_{-1}=0$ ✓ — **consistent**, so $a_1$ is free and no logarithm is needed. The two families (even from $a_0$, odd from $a_1$) give
$$y_1=\sqrt{\tfrac{2}{\pi x}}\sin x=J_{1/2}(x),\qquad y_2=\sqrt{\tfrac{2}{\pi x}}\cos x=J_{-1/2}(x)$$
Half-integer Bessel equations never need a logarithm.

## Example 6 (Case III, log **forced**): Bessel order 1, $x^2y''+xy'+(x^2-1)y=0$

$r^2=1$, $r_1=1,\ r_2=-1$ (difference 2). Recurrence $[(n+r)^2-1]a_n=-a_{n-2}$.
- $r=1$: $n(n+2)a_n=-a_{n-2}$, $a_1=0$ ⇒ $y_1=J_1(x)=\sum\dfrac{(-1)^k}{k!(k+1)!}\big(\tfrac x2\big)^{2k+1}$.
- $r=-1$: $n(n-2)a_n=-a_{n-2}$. At $n=2$: $0\cdot a_2=-a_0\ne0$ ⇒ **contradiction**, a logarithm is forced:
$$y_2=C\,J_1(x)\ln x+x^{-1}\sum b_nx^n,\quad C=\tfrac2\pi\ne0\ (\text{this is }Y_1)$$
$Y_1(x)\to-\infty$ like $-\tfrac{2}{\pi x}$ as $x\to0^+$.

**Compare Examples 5 and 6**: the same integer gap, but whether the obstruction term $R$ vanishes decides log or no log.

## Example 7 (Case I): $2x^2y''-xy'+(1+x)y=0$

Indicial $2r^2-3r+1=0\Rightarrow r=1,\tfrac12$ (difference $\tfrac12$). Recurrence $a_n=\dfrac{-a_{n-1}}{2(n+r)(n+r-1)-(n+r)+1}$:
- $r=1$: $a_n=\dfrac{-a_{n-1}}{n(2n+1)}$ ⇒ $y_1=x\big(1-\tfrac x3+\cdots\big)$;
- $r=\tfrac12$: $a_n=\dfrac{-a_{n-1}}{n(2n-1)}$ ⇒ $y_2=x^{1/2}(1-x+\cdots)$.

## Example 8 (Case II, Euler): $x^2y''+3xy'+y=0$

$p_0=3,\ q_0=1$: $r^2+2r+1=0$, $r=-1$ twice. All $a_n=0$ for $n\ge1$:
$$y=\frac{A}{x}+B\,\frac{\ln x}{x}$$
(exactly the Cauchy–Euler repeated-root solution).

## Summary table

| Equation | Roots | Case | Log? | Solutions |
|---|---|---|---|---|
| Ex 1 | $1,-\tfrac12$ | I | no | two series |
| Ex 2 | $\tfrac12,0$ | I | no | $\sin\sqrt x,\cos\sqrt x$ |
| Ex 3 (Bessel 0) | $0,0$ | II | yes | $J_0$, $J_0\ln x+\cdots$ |
| Ex 4 | $0,0$ | II | yes | $\frac1{1-x},\frac{\ln x}{1-x}$ |
| Ex 5 (Bessel ½) | $\tfrac12,-\tfrac12$ | III | **no** | $J_{\pm1/2}$ |
| Ex 6 (Bessel 1) | $1,-1$ | III | **yes** | $J_1$, $Y_1$ |
| Ex 7 | $1,\tfrac12$ | I | no | two series |
| Ex 8 (Euler) | $-1,-1$ | II | yes | $x^{-1},x^{-1}\ln x$ |

## More problems of the same kind
[[Assignment 4 - Series Solutions - Solutions#Q3 Frobenius method|Assignment 4, Q3 (a)–(i)]] — includes the logarithmic cases (b), (g), (h) and the Bessel-type reductions (c).

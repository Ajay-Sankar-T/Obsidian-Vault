---
title: Reducing Equations to Bessel Form
tags: [differential-equations, special-functions, bessel, transformation, airy, concept]
source: "[[Lecture-26.pdf]] (slides 1–21)"
---

Related: [[Bessel's Equation and Bessel Functions of the First Kind]] · [[Bessel Functions of the Second Kind and General Solution]] · [[Cauchy-Euler Equations]] · [[Frobenius Method - Worked Examples]] · [[Special Functions - MOC]]

## The template
If $u(z)$ solves Bessel's equation of order $n$ then $y(x)=x^a\,u(bx^c)$ solves
$$y''+\frac{1-2a}xy'+\Big(b^2c^2x^{2c-2}+\frac{a^2-n^2c^2}{x^2}\Big)y=0\qquad(\text{Simmons; Lecture 26}).$$
So the general solution is $y=x^a\big[AJ_n(bx^c)+BJ_{-n}(bx^c)\big]$ (replace $J_{-n}$ by $Y_n$ if $n\in\mathbb Z$).

## Recipe (match, don't re-derive)
Put the target in the form $y''+Py'+Qy=0$ and match:
1. $P=\dfrac{1-2a}x\Rightarrow a$.
2. The power of $x$ in the **$x$-dependent part of $Q$** is $2c-2\Rightarrow c$; its coefficient is $b^2c^2\Rightarrow b$.
3. The $1/x^2$ part of $Q$ equals $a^2-n^2c^2\Rightarrow n=\sqrt{a^2-(\text{that})}/c$.

| Equation | $a$ | $b,c$ | $n$ | solution |
|---|---|---|---|---|
| $y''+xy=0$ (Airy) | $\frac12$ | $\frac23,\ \frac32$ | $\frac13$ | $\sqrt x\,Z_{1/3}(\tfrac23x^{3/2})$ |
| $x^2y''+xy'+(x^4-4)y=0$ | 0 | $\frac12,\ 2$ | 1 | $Z_1(\tfrac12x^2)$ |
| $xy''-y'+4x^6y=0$ | 1 | $\frac47,\ \frac72$ | $\frac27$ | $x\,Z_{2/7}(\tfrac47x^{7/2})$ |
| $xy''+(1+2p)y'+xy=0$ | $-p$ | $1,\ 1$ | $p$ | $x^{-p}Z_p(x)$ |
| $y''+y=0$ | $\frac12$ | $1,\ 1$ | $\frac12$ | $\sqrt x\,Z_{1/2}(x)$ (= $\sin x,\cos x$) |

$Z$ denotes $J$ or $Y$ (use $J_{\pm n}$ when $n\notin\mathbb Z$).

## Equations with no power of $x$
If the coefficients involve $e^{-x}$ and so on, change the independent variable directly: $y''+e^{-x}y=0$ with $z=2e^{-x/2}$ gives $z^2u''+zu'+z^2u=0$, i.e. $y=Z_0(2e^{-x/2})$. General guide: $z=\int\sqrt{Q}\,dx$ makes the coefficient of $u$ equal to $1$, and the first-derivative coefficient then identifies the Bessel order (normal form, Lecture 26 slides 22–23).

## Why the Airy equation gives order $\tfrac13$
$a=\tfrac12$ from the missing $y'$ term and $c=\tfrac32$ from $x^{2c-2}=x$; then $a^2=n^2c^2$ gives $n=a/c=\frac13$. The three-thirds structure is why $\mathrm{Ai}$ and $\mathrm{Bi}$ are Bessel functions of order $\pm\frac13$ in $\tfrac23x^{3/2}$.

![[A6-fig5-transformations.png]]
**Figure:** Bessel-form solutions (thick) against direct numerical integration of the original ODE (dashed).

## Cross-domain links
- [[Cauchy-Euler Equations]] — $x=e^t$ also maps Euler equations to constant coefficients: Bessel form is the next rung (the $x^2$ term in $Q$ replaces a constant).
- Airy functions appear for a particle in a linear potential and in the turning-point region of WKB approximations.

## Worked examples
[[Assignment 6 - Bessel Functions - Solutions]] Q6 (eight equations (a)–(h)).

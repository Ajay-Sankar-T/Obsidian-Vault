---
title: Bessel Function Properties and Recurrence Relations
tags: [differential-equations, special-functions, bessel, recurrence, spherical-bessel]
source: "[[Lecture-24.pdf]] (slides 10–11), [[Lecture-25.pdf]] (slides 1–10, 15)"
---

Related: [[Bessel's Equation and Bessel Functions of the First Kind]] · [[Bessel Generating Function]] · [[Gamma Function]] · [[Legendre Recurrence Relations and Integrals]] (the Legendre analogue) · [[Special Functions - MOC]]

All identities were checked numerically for several orders $\nu$ and arguments $x$.

## 1. The two basic derivative identities

From $x^\nu J_\nu=\sum\frac{(-1)^n}{n!\Gamma(n+\nu+1)}\frac{x^{2n+2\nu}}{2^{2n+\nu}}$, differentiate and use $\Gamma(n+\nu+1)=(n+\nu)\Gamma(n+\nu)$:

$$\boxed{\frac d{dx}\big[x^\nu J_\nu(x)\big]=x^\nu J_{\nu-1}(x)}\ (7),\qquad\boxed{\frac d{dx}\big[x^{-\nu}J_\nu(x)\big]=-x^{-\nu}J_{\nu+1}(x)}\ (8)$$

Hence the **integral forms** $\int x^\nu J_{\nu-1}dx=x^\nu J_\nu+C$ and $\int x^{-\nu}J_{\nu+1}dx=-x^{-\nu}J_\nu+C$ — no series manipulation needed.

Validity: (8) holds for $\nu\ge0$; (7) was derived for $\nu>0$ but also holds at $\nu=0$: $J_0'=J_{-1}=-J_1$, the same as (8) with $\nu=0$. In particular $\boxed{J_0'=-J_1}$ and $\dfrac{d}{dx}[xJ_1]=xJ_0$.

Expanding by the product rule:
$$J_\nu'+\frac\nu xJ_\nu=J_{\nu-1},\qquad J_\nu'-\frac\nu xJ_\nu=-J_{\nu+1}$$

## 2. The two master recurrences

Add/subtract:
$$\boxed{J_{\nu-1}(x)+J_{\nu+1}(x)=\frac{2\nu}xJ_\nu(x)}\ (10),\qquad\boxed{J_{\nu-1}(x)-J_{\nu+1}(x)=2J_\nu'(x)}\ (9)$$

- (10) climbs in order: tables need only $J_0,J_1$; $J_{\nu+n}$ follows from $J_\nu,J_{\nu+1}$. Use it **upward** only for moderate orders (upward recurrence is unstable once $n>x$).
- (10) proves that all half-integer orders are elementary.

**Example: $J_3(4)$ from $J_0(4),J_1(4)$.** $J_2=\frac2xJ_1-J_0$, $J_3=\frac4xJ_2-J_1=\big(\frac8{x^2}-1\big)J_1-\frac4xJ_0$. At $x=4$: $J_0=-0.397150,\ J_1=-0.066043$ ⇒ $J_2=0.364128$, $J_3=\big(\tfrac12-1\big)(-0.066043)-(-0.397150)=0.430171$ ✓ (tabulated).

![[DE-N13-bessel-properties.png]]
**Figure:** Left: the half-integer functions are sines and cosines with a $x^{-1/2}$ envelope. Middle: the recurrence ladder at $x=4$. Right: identity (9) verified for $\nu=2$.

## 3. Half-integer orders and spherical Bessel functions

$J_{1/2}(x)=\sqrt{\dfrac2x}\sum\dfrac{(-1)^nx^{2n+1}}{2^{2n+1}n!\,\Gamma(n+\frac32)}$ and $2^{2n+1}n!\,\Gamma(n+\tfrac32)=(2n+1)!\sqrt\pi$, so

$$\boxed{J_{1/2}(x)=\sqrt{\frac2{\pi x}}\sin x}\ ,\qquad\boxed{J_{-1/2}(x)=\sqrt{\frac2{\pi x}}\cos x}$$

(the second from $\frac d{dx}[\sqrt xJ_{1/2}]=\sqrt x\,J_{-1/2}$ by (7)). Then (10) gives

$$J_{3/2}=\sqrt{\tfrac2{\pi x}}\Big(\tfrac{\sin x}x-\cos x\Big),\quad J_{-3/2}=-\sqrt{\tfrac2{\pi x}}\Big(\tfrac{\cos x}x+\sin x\Big),\quad J_{5/2}=\sqrt{\tfrac2{\pi x}}\Big(\tfrac{3\sin x}{x^2}-\tfrac{3\cos x}x-\sin x\Big)$$

These are the **spherical Bessel functions** (radial solutions of the wave equation in spherical coordinates).

## 4. Integral problems from the lecture

- $\displaystyle\int_0^2xJ_0\,dx=\big[xJ_1\big]_0^2=2J_1(2)=1.153450$ ($J_1(2)=0.576725$) ✓ numerical quadrature.
- $\displaystyle\int J_3\,dx=-J_2-\frac2xJ_1+C$ (write $J_3=x^2\cdot x^{-2}J_3$, use $(x^{-2}J_2)'=-x^{-2}J_3$, integrate by parts, then $(x^{-1}J_1)'=-x^{-1}J_2$).
- $\displaystyle\int_0^1(x-x^3)J_0\,dx=2J_2(1)$ (two integrations by parts with $(xJ_1)'=xJ_0$ and $(x^2J_2)'=x^2J_1$).
- $\displaystyle\int x^4J_1\,dx=(4x^3-16x)J_1-(x^4-8x^2)J_0+C$ (use $J_1=-J_0'$, then by parts three times).

All four were confirmed numerically on sample intervals.

**Pattern.** To evaluate $\int x^pJ_q\,dx$: if $p=q+1$ it is exact ($x^{q+1}J_{q+1}$ — from (7) with $\nu=q+1$); otherwise reduce the power by parts using (7)/(8) until it fits, or until it ends in $\int J_0\,dx$ (which has no closed form).

## 5. Cross-links
The recurrences can be obtained from the generating function: [[Bessel Generating Function]]. For the Legendre analogue see [[Legendre Recurrence Relations and Integrals]].

## Problems using this
[[Assignment 6 - Bessel Functions - Solutions]] (source [[Assignment-6.pdf]]) applies exactly these tools:
- Q1: $J_{-n}=(-1)^nJ_n$, $J_n(-x)=(-1)^nJ_n(x)$.
- Q2: $J_{3/2}$ and the identities (b)–(h) (derivative and recurrence relations, $J_{1/2}J_{-1/2}=\frac{\sin2x}{\pi x}$).
- Q3: reduction integrals such as $\int x^4J_0$, $\int J_5$, $\int x^{-2}J_5$, and the general $\int x^pJ_\nu$ by parts.
- Q7: derivatives of $J_n^2$ and $J_n^2+J_{n+1}^2$; Q8: $J_4$ in terms of $J_0,J_1$; Q9: $\int_0^rxJ_0(ax)dx=\frac raJ_1(ar)$; Q10 uses the [[Bessel Generating Function]].

Related Frobenius reductions: [[Frobenius Method - Worked Examples]].

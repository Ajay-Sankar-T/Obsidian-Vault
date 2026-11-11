---
title: Gamma Function
tags: [differential-equations, special-functions, gamma, factorial]
source: "[[Lecture-23.pdf]] (slides 2–9)"
---

Related: [[Bessel's Equation and Bessel Functions of the First Kind]] · [[Orthogonality and Norm of Legendre Polynomials]] (Beta-function form of the norm) · [[Special Functions - MOC]]

Euler's Gamma function extends $n!$ to non-integer arguments. It is needed because the Bessel series for general order $\nu$ contains $\Gamma(n+\nu+1)$ in every denominator.

## 1. Definition and the functional equation

$$\Gamma(x)=\int_0^\infty e^{-t}t^{x-1}\,dt\qquad(x>0)$$
Converges at $0$ since $t^{x-1}$ is integrable iff $x>0$, and at $\infty$ because $e^{-t}$ beats any power. Integration by parts:
$$\boxed{\Gamma(x+1)=x\,\Gamma(x)}\qquad\Gamma(1)=1\ \Rightarrow\ \boxed{\Gamma(n+1)=n!}$$

## 2. Special values

Put $t=u^2$: $\Gamma(\tfrac12)=2\int_0^\infty e^{-u^2}du=\sqrt\pi$. The functional equation then gives all half-integers:
$$\Gamma(\tfrac32)=\tfrac12\sqrt\pi,\quad\Gamma(\tfrac52)=\tfrac34\sqrt\pi,\quad\Gamma(n+\tfrac12)=\frac{(2n)!}{4^nn!}\sqrt\pi$$
These reappear in $J_{\pm1/2}$ ([[Bessel Function Properties and Recurrence Relations]]).

## 3. Extension to negative arguments

Rearrange: $\Gamma(x)=\dfrac{\Gamma(x+1)}{x}$ and step down.
- $\Gamma(-\tfrac12)=\dfrac{\Gamma(1/2)}{-1/2}=-2\sqrt\pi$
- $\Gamma(-\tfrac32)=\dfrac{-2\sqrt\pi}{-3/2}=\tfrac43\sqrt\pi$
- $\Gamma(-\tfrac52)=\dfrac{\frac43\sqrt\pi}{-5/2}=-\dfrac{8\sqrt\pi}{15}\approx-0.9453$ (verified numerically)

At $x=0,-1,-2,\dots$ the recursion divides by zero: **simple poles**. Hence $\dfrac1{\Gamma(x)}=0$ at non-positive integers — this is why $J_{-m}=(-1)^mJ_m$ ([[Bessel Functions of the Second Kind and General Solution]]).

![[DE-N10-gamma.png]]
**Figure:** Left: $\Gamma$ on $(-4.5,5)$ with poles (dotted) and sign alternation: negative on $(-1,0)$, positive on $(-2,-1)$, negative on $(-3,-2)$, …; minimum $\approx0.8856$ at $x\approx1.4616$ for $x>0$; $\Gamma\to\infty$ as $x\to0^+$ and $x\to\infty$. Middle: $\Gamma(n)=(n-1)!$ on the smooth curve. Right: half-integer values.

## 4. Useful extras (standard; not on the slides)
- Beta function: $B(p,q)=\int_0^1x^{p-1}(1-x)^{q-1}dx=\dfrac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$, equivalent to $\int_0^{\pi/2}\sin^p\theta\cos^q\theta\,d\theta=\dfrac{\Gamma(\frac{p+1}2)\Gamma(\frac{q+1}2)}{2\Gamma(\frac{p+q+2}2)}$ (used for the Legendre norm in Method 1 and in [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q7|Assignment 5, Q7(e)]]).
- Reflection: $\Gamma(x)\Gamma(1-x)=\dfrac\pi{\sin\pi x}$.

## Problems
[[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q7|Assignment 5, Q7(e),(a)]] use $\Gamma$ and $B$ explicitly.

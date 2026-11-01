---
title: Bessel Functions of the Second Kind and General Solution
tags: [differential-equations, special-functions, bessel, neumann-function]
source: "[[Lecture-24.pdf]] (slides 5–9), [[Lectures-16-17.pdf]] (Problem 6)"
---

Related: [[Bessel's Equation and Bessel Functions of the First Kind]] · [[Frobenius Method - Worked Examples]] · [[Bessel Function Properties and Recurrence Relations]] · [[Gamma Function]] · [[Special Functions - MOC]]

When $\nu$ is a non-negative integer $J_{-\nu}=(-1)^\nu J_\nu$ is no longer independent, so we need a different second solution — the **Bessel function of the second kind** $Y_\nu$ (also called Neumann or Weber function).

## 1. Unified definition

$$\boxed{Y_\nu(x)=\frac{J_\nu(x)\cos\nu\pi-J_{-\nu}(x)}{\sin\nu\pi}}\qquad(\nu\notin\mathbb Z)$$

For integer order, $Y_m:=\lim_{\nu\to m}Y_\nu$ (a $0/0$ limit, evaluated by L'Hôpital). $J_\nu$ and $Y_\nu$ are **always linearly independent** and both solve Bessel's equation, so for all $\nu\ge0$, $x>0$:

$$\boxed{y=C_1J_\nu(x)+C_2Y_\nu(x)}$$

For non-integer $\nu$ the pair $\{J_\nu,Y_\nu\}$ and the pair $\{J_\nu,J_{-\nu}\}$ span the same solution space ($Y_{-\nu}$ is *not* $J_{-\nu}$ in general: $Y_{-\nu}=aJ_\nu+bJ_{-\nu}$).

## 2. Series for integer order $m$

$$Y_m(x)=\frac2\pi J_m(x)\Big(\ln\frac x2+\gamma\Big)+\frac{x^m}\pi\sum_{n\ge0}\frac{(-1)^{n-1}(h_n+h_{n+m})\,x^{2n}}{2^{2n+m}n!(n+m)!}-\frac{x^{-m}}\pi\sum_{n=0}^{m-1}\frac{(m-n-1)!\,x^{2n}}{2^{2n-m}\,n!}$$
with $h_0=0,\ h_k=1+\tfrac12+\cdots+\tfrac1k$ and Euler's constant $\gamma=\lim(h_k-\ln k)=0.5772\ldots$. In particular
$$Y_0(x)=\frac2\pi\Big[J_0(x)\Big(\ln\frac x2+\gamma\Big)+\sum_{n\ge1}\frac{(-1)^{n-1}h_n\,x^{2n}}{2^{2n}(n!)^2}\Big]$$
This matches the Frobenius Case II solution $J_0\ln x+\sum\frac{(-1)^{k+1}H_k}{2^{2k}(k!)^2}x^{2k}$ ([[Frobenius Method - Worked Examples]], Example 3), normalised. For order 1, Case III with forced log gives $Y_1=\frac2\pi J_1\ln x-\frac1{\pi x}+\cdots$ (Example 6). Both series reproduce the library values of $Y_0,Y_1,Y_2,Y_3$ to $10^{-9}$.

## 3. Behaviour

![[DE-N12-bessel-second-kind.png]]
**Figure:** Left: $Y_n\to-\infty$ as $x\to0^+$ for every $n$. Middle: for small $x$, $Y_0\approx\frac2\pi(\ln\frac x2+\gamma)$ — a logarithm. Right: for non-integer order, $Y_\nu$ is a combination of $J_{\pm\nu}$.

| | $J_n$ | $Y_n$ |
|---|---|---|
| at $x=0$ | finite ($J_0(0)=1$, $J_n(0)=0$) | $\to-\infty$ ($\ln x$ for $n=0$, $x^{-n}$ for $n\ge1$) |
| large $x$ | $\sqrt{\frac2{\pi x}}\cos(x-\frac{n\pi}2-\frac\pi4)$ | $\sqrt{\frac2{\pi x}}\sin(x-\frac{n\pi}2-\frac\pi4)$ |
| use | bounded solutions (finite at the axis) | needed when the origin is excluded (annulus) or to match boundary conditions |

In physical problems on a disc (centre included) the solution must be bounded at $r=0$, so the $Y_\nu$ coefficient is zero.

## 4. Decision table for the general solution

| $\nu$ | General solution |
|---|---|
| not an integer | $C_1J_\nu+C_2J_{-\nu}$ (or $C_1J_\nu+C_2Y_\nu$) |
| half-integer | $J_{\nu},J_{-\nu}$ elementary: e.g. $\sqrt{\frac1x}(A\sin x+B\cos x)$ for $\nu=\tfrac12$ |
| $0,1,2,\dots$ | $C_1J_\nu+C_2Y_\nu$ |

## Problems using this
- Bessel-type problems from the series assignment: [[Assignment 4 - Series Solutions - Solutions#Q3 Frobenius method|Assignment 4, Q3]].
- [[Assignment-6.pdf]] Q4: for any two solutions of Bessel's equation $y_1y_2'-y_1'y_2=c/x$ (Abel's formula, $P=1/x$); for $J_\nu,Y_\nu$ the constant is $c=\frac2\pi$, i.e. $W(J_\nu,Y_\nu)=\frac{2}{\pi x}$ (standard value). Q6 and Q11 (Fourier–Bessel series) need $J_\nu$ and $Y_\nu$ as well.
- No solution note exists yet for Assignments 6–7.

## See also
- [[Abel's Formula]] — the Wronskian $W(J,Y)=2/(\pi x)$ follows from Abel's formula.

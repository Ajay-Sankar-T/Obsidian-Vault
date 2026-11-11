---
title: Fourier-Bessel Series
tags: [differential-equations, special-functions, bessel, fourier-bessel, orthogonality, concept]
source: "[[Lecture-27.pdf]] (slides 6–23)"
---

Related: [[Sturm-Liouville Problems]] · [[Bessel Function Properties and Recurrence Relations]] · [[Bessel's Equation and Bessel Functions of the First Kind]] · [[Legendre Series and Fourier-Legendre Expansions]] (the Legendre analogue) · [[Special Functions - MOC]]

## Statement
Let $\alpha_1<\alpha_2<\dots$ be the positive zeros of $J_\nu$. On $[0,L]$:
$$\int_0^L xJ_\nu\Big(\frac{\alpha_jx}L\Big)J_\nu\Big(\frac{\alpha_kx}L\Big)dx=\frac{L^2}2J_{\nu+1}(\alpha_k)^2\,\delta_{jk}$$
(weight $x$). Hence every piecewise smooth $f$ has
$$\boxed{f(x)\sim\sum_{n\ge1}a_nJ_\nu\Big(\frac{\alpha_nx}L\Big),\qquad a_n=\frac2{L^2J_{\nu+1}(\alpha_n)^2}\int_0^Lx\,f(x)\,J_\nu\Big(\frac{\alpha_nx}L\Big)dx}$$

## Why it works
$J_\nu(\lambda x)$ solves the singular Sturm–Liouville problem $(xy')'+\big(\lambda^2x-\nu^2/x\big)y=0$ with $y(0)$ bounded and $y(L)=0$, so [[Sturm-Liouville Problems]] gives orthogonality with weight $x$. Directly: multiply the equations for $u=J_\nu(ax)$ and $v=J_\nu(bx)$ and subtract,
$$(b^2-a^2)\int_0^cxuv\,dx=c\big[u'v-uv'\big]_{x=c}=c\big[aJ_{\nu-1}(ac)J_\nu(bc)-bJ_\nu(ac)J_{\nu-1}(bc)\big],$$
which is $0$ when $ac,bc$ are zeros of $J_\nu$; letting $b\to a$ gives the norm ($J_\nu'=-J_{\nu+1}$ and $J_{\nu-1}=-J_{\nu+1}$ at a zero).

## Method (works for every problem)
1. Substitute $t=\alpha_nx/L$ in $\int_0^Lxf\,J_\nu(\alpha_nx/L)\,dx$.
2. Reduce $\int t^{m}J_\nu(t)\,dt$ with $(t^\nu J_\nu)'=t^\nu J_{\nu-1}$ and $(t^{-\nu}J_\nu)'=-t^{-\nu}J_{\nu+1}$ ([[Bessel Function Properties and Recurrence Relations]]).
3. Simplify with $J_\nu(\alpha_n)=0$: the recurrences then give $J_{\nu\pm1}$ in terms of each other.

**Pattern.** $f=x^{\nu+1}\cdot$ (power): $\int_0^L x^{\nu+1}J_\nu(\alpha x/L)\,dx$ is exact. For $\nu=0$, $f=1$: $a_n=\dfrac2{\alpha_nJ_1(\alpha_n)}$. If the integrand does not match the pattern, $\int J_0$ appears and there is no closed form.

## Convergence
- In the weighted $L^2$ norm for square-integrable $f$.
- Pointwise on $0<x<L$ (Bessel expansion theorem) to $\tfrac12[f(x^+)+f(x^-)]$ when $f,f'$ are piecewise continuous; Gibbs overshoot (about 9 % of a jump) at jumps.
- All terms vanish at $x=L$, so the sum is $0$ there whatever $f(L)$ is: expect slow convergence near $L$ unless $f(L)=0$.

![[A6-fig7-fourier-bessel.png]]
**Figure:** Partial sums for the six sheet problems.

## Special case: half-integer order is a Fourier sine series
$\nu=\tfrac12$: $J_{1/2}(x)=\sqrt{2/\pi x}\sin x$, zeros $\alpha_k=k\pi$, and the series for $\sqrt x$ on $[0,1]$ collapses to the sine series $x=\frac2\pi\sum(-1)^{k+1}\frac{\sin k\pi x}k$.

## Cross-domain links
- [[Legendre Series and Fourier-Legendre Expansions]] — same recipe $a_n=\int rfy_n/\int ry_n^2$ with a different weight; the Fourier sine/cosine series is the case $r=1$.
- Vibrations of a circular drum (radial modes $J_0(\alpha_nr/R)$) are exactly this expansion.

## Worked examples
[[Assignment 6 - Bessel Functions - Solutions]] Q11, Q12.

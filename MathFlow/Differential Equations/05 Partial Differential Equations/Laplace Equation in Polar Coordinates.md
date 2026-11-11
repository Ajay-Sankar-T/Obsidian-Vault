---
title: Laplace Equation in Polar Coordinates
tags: [differential-equations, pdes, concept, laplace-equation, polar-coordinates, fourier-series, cauchy-euler]
source: "[[Lecture-37.pdf]], [[A10-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Laplace Equation on Rectangles and Strips]] · [[Separation of Variables]] · [[Cauchy-Euler Equations]] · solved in [[Assignment 10 - Laplace Equations - Solutions]] Q1, Q2(c)–(d), Q8–Q10

## What it is
For circular regions put $x=r\cos\theta$, $y=r\sin\theta$. By the chain rule the Laplacian becomes
$$\nabla^2u=u_{rr}+\frac1ru_r+\frac1{r^2}u_{\theta\theta}=0.$$
(The $u_r/r$ term comes from the second derivative of $r=\sqrt{x^2+y^2}$; the mixed terms cancel.)

## Solution by separation $u=R(r)\Theta(\theta)$
$$r^2R''+rR'-\lambda R=0,\qquad\Theta''+\lambda\Theta=0.$$
The $r$-equation is a **Cauchy–Euler equation**: $R=r^m$, $m=\pm\sqrt\lambda$. The angular equation depends on the region.

| Region | $\Theta$ condition | $\lambda$ | Solution |
|---|---|---|---|
| **disk** $r<a$ | $2\pi$-periodic | $n^2,\ n\ge0$ | $u=\frac{a_0}2+\sum\big(\frac ra\big)^n(a_n\cos n\theta+b_n\sin n\theta)$ |
| **exterior** $r>a$ | periodic, bounded at $\infty$ | $n^2$ | same with $(a/r)^n$ |
| **annulus** $a<r<b$ | periodic | $n^2$ | $(Ar^n+Br^{-n})$ and $\ln r$ for $n=0$ |
| **sector** $0<\theta<\alpha$, zero on both rays | Dirichlet | $\big(\frac{n\pi}{\alpha}\big)^2$ | $\sin\frac{n\pi\theta}\alpha$ with $r^{n\pi/\alpha}$, $r^{-n\pi/\alpha}$ |
| **half disk** $0<\theta<\pi$, zero on the diameter | Dirichlet | $n^2$ | $\sum b_nr^n\sin n\theta$ |

**Boundedness at the centre.** For the disk $R=r^{-n}$ (and $\ln r$) blow up at $r=0$, so they are dropped.

**Disk, $u(a,\theta)=f(\theta)$:** $a_n=\frac1\pi\int_0^{2\pi}f\cos n\theta\,d\theta$, $b_n=\frac1\pi\int_0^{2\pi}f\sin n\theta\,d\theta$.
- **Mean value property:** $u(0,\theta)=a_0/2$ is the average of $f$ over the circle.
- **Maximum principle:** the extremes of $u$ occur on the boundary circle.
- Summing the series gives **Poisson's formula** $u(r,\theta)=\frac1{2\pi}\int_0^{2\pi}\frac{a^2-r^2}{a^2-2ar\cos(\theta-\phi)+r^2}f(\phi)\,d\phi$.
- A single mode: $u(a,\theta)=\cos n\theta\Rightarrow u=(r/a)^n\cos n\theta$.

**Annulus (zero on the outer radius, data on the inner):** each mode is $\dfrac{(r/b)^{m}-(b/r)^{m}}{(a/b)^{m}-(b/a)^{m}}$, which equals 1 at $r=a$ and 0 at $r=b$. For $1<r<2$, $u(1,\theta)=\sin\theta$, $u(2,\theta)=0$ on $0<\theta<\pi$: $u=\dfrac{4-r^2}{3r}\sin\theta$.

![[DE-PDE-laplace.png]]
**Figure (right):** the disk with boundary value $\theta$ on the right half and $0$ on the left. The solution is smooth inside even though the boundary data jump at $\theta=\pm\pi/2$.

## Method
1. Write $\nabla^2$ in polar form; identify the angular condition from the shape (periodic for a full disk, Dirichlet for a sector).
2. Solve $\Theta''+\lambda\Theta=0$, then the Euler equation for $R$.
3. Keep only bounded radial solutions ($r^{-n}$ is out at the centre, $r^{n}$ out at infinity).
4. Match the boundary circle: Fourier series in $\theta$.

> [!warning] Traps
> - Forgetting that $\Theta$ must be $2\pi$-periodic on a full disk, which forces **integer** $n$.
> - On a **sector** the exponent is $n\pi/\alpha$ (not $n$); for a half disk it is an integer, for a quarter disk it is $2n$.
> - Not matching the Fourier interval to the one-period description of the boundary data (e.g. $\theta\in[-\pi/2,3\pi/2)$ describes the same function as $[-\pi,\pi)$).
> - Harmonic functions are smooth in the interior, not necessarily up to the boundary: at the tip of a slit (interior angle $2\pi$) the exponent is $\pi/\alpha=\frac12$, so $u\sim r^{1/2}$ and $u_r\sim r^{-1/2}$ is unbounded.

## Cross-domain links
- [[Cauchy-Euler Equations]] — the radial equation $r^2R''+rR'-n^2R=0$ is the Euler equation, with $r=e^t$ turning it into $R_{tt}=n^2R$: the same separation as the $x=e^t$ trick in [[Assignment 7 - Sturm-Liouville Problems - Solutions]].
- [[Fourier-Bessel Series]] — for a **drum** (wave equation on a disk) the radial part becomes Bessel's equation, and the boundary-value expansion is a Fourier–Bessel series instead of $r^n$.

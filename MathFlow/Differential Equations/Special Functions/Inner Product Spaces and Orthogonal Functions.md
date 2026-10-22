---
title: Inner Product Spaces and Orthogonal Functions
tags: [differential-equations, special-functions, inner-product, orthogonality, linear-algebra]
source: "[[Lecture-20.pdf]] (slides 1–5), [[Lecture-21.pdf]] (slides 12–14)"
---

Related: [[Orthogonality and Norm of Legendre Polynomials]] · [[Legendre Series and Fourier-Legendre Expansions]] · [[Special Functions - MOC]] · [[Linear Algebra]] (vault note)

Orthogonality of functions is the same idea as perpendicular vectors, with an integral playing the role of the dot product.

## 1. Vector space and inner product

A **vector space** $V$ over $\mathbb R$ has addition and scalar multiplication satisfying the usual axioms; the set $\mathcal P(x)$ of **all polynomials** is an *infinite-dimensional* vector space (basis $1,x,x^2,\dots$).

An **inner product** $\langle\cdot,\cdot\rangle:V\times V\to\mathbb R$ is
- bilinear: $\langle au+v,w\rangle=a\langle u,w\rangle+\langle v,w\rangle$ (and the same in the second slot),
- symmetric: $\langle v,w\rangle=\langle w,v\rangle$,
- positive definite: $\langle v,v\rangle\ge0$, $=0$ iff $v=0$.

**Norm:** $\|v\|=\langle v,v\rangle^{1/2}$ — satisfies $\|av\|=|a|\|v\|$ and the triangle inequality $\|v+w\|\le\|v\|+\|w\|$.

On functions: $\ \langle f,g\rangle=\displaystyle\int_a^b w(x)f(x)g(x)\,dx$ with a **weight** $w(x)>0$. For Legendre polynomials $[a,b]=[-1,1]$, $w=1$.

## 2. Orthogonal and orthonormal systems

$\{y_n\}$ is **orthogonal** on $[a,b]$ (weight $w$) if
$$\langle y_n,y_m\rangle=\begin{cases}0&n\ne m\\ \alpha_n\ne0&n=m\end{cases}$$
and **orthonormal** if all $\alpha_n=1$ (divide each $y_n$ by $\|y_n\|$).

| System | Interval | Norm² |
|---|---|---|
| $\sin nx,\ n\ge1$ | $[-\pi,\pi]$ | $\pi$ |
| $\cos nx,\ n\ge0$ | $[-\pi,\pi]$ | $\pi$ ($2\pi$ for $n=0$) |
| $\frac1{\sqrt{2\pi}},\frac{\cos nx}{\sqrt\pi},\frac{\sin nx}{\sqrt\pi}$ | $[-\pi,\pi]$ | 1 (orthonormal) |
| Legendre $P_n$ | $[-1,1]$, $w=1$ | $\frac2{2n+1}$ |

If a linearly independent set is not orthogonal, **Gram–Schmidt** builds an orthogonal set from it. Applied to $1,x,x^2,\dots$ on $[-1,1]$ with $w=1$ it produces (multiples of) the Legendre polynomials — see the figure.

![[DE-N6-inner-product.png]]
**Figure:** Gram matrices on $[-1,1]$. For monomials $\langle x^i,x^j\rangle=\frac{2}{i+j+1}$ (even $i+j$) the matrix is full — the basis is *not* orthogonal. For $P_0,\dots,P_5$ it is diagonal with entries $\frac2{2n+1}$. Right: $\sin kx$ are orthogonal on $[-\pi,\pi]$.

## 3. Why orthogonal bases matter

If $\{y_n\}$ is orthogonal and $f=\sum c_ny_n$, take the inner product with $y_m$:
$$\langle f,y_m\rangle=c_m\|y_m\|^2\ \Longrightarrow\ \boxed{c_m=\frac{\langle f,y_m\rangle}{\|y_m\|^2}}$$
No linear system to solve — the coefficients decouple. This generalises the Fourier series and gives the [[Legendre Series and Fourier-Legendre Expansions]].

Orthogonality also comes from the ODE itself: Sturm–Liouville equations $(p\,y')'+(q+\lambda r)y=0$ have eigenfunctions orthogonal w.r.t. $r(x)$. Legendre ($p=1-x^2$, $r=1$) and Bessel (weight $x$) are the key examples.

## 4. The space $L^2$

$f$ is **square-integrable** on $[-1,1]$ if $\int_{-1}^1f^2\,dx<\infty$ (all polynomials, continuous and piecewise continuous functions); these form the vector space $L^2([-1,1])$ with $\langle f,g\rangle=\int fg$. The Legendre polynomials are a **maximal orthogonal set**: no non-zero $f\in L^2$ is orthogonal to every $P_n$. Hence every $f\in L^2$ is the $L^2$-limit of its Legendre series.

## Problems using this
- Orthogonality integrals and expansions: [[Assignment 5 - Legendre Polynomials and Functions - Solutions#0.5 Orthogonality and norm|Assignment 5, §0.5]], [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q3|Q3]], [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q5|Q5]], [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q6|Q6]].

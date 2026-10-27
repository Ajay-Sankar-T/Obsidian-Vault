---
title: Sturm-Liouville Problems
tags: [differential-equations, special-functions, sturm-liouville, orthogonality, eigenvalue-problem, concept]
source: "[[Lecture-28.pdf]], [[Lecture-27.pdf]] (slides 6–13), [[Assignment-7.pdf]]"
---

Related: [[Inner Product Spaces and Orthogonal Functions]] · [[Orthogonality and Norm of Legendre Polynomials]] · [[Fourier-Bessel Series]] · [[Legendre's Equation]] · [[Cauchy-Euler Equations]] · [[Special Functions - MOC]]

## What it is
A **Sturm–Liouville problem** (SLP) is a second-order linear ODE in *self-adjoint form*
$$\big(p(x)\,y'\big)'+\big(q(x)+\lambda\,r(x)\big)y=0,\qquad a<x<b,$$
with $p>0$, $r>0$ (the **weight**), plus boundary conditions, for which non-trivial solutions exist only for special $\lambda$ (**eigenvalues**). It is the function-space version of the symmetric eigenvalue problem $A\mathbf v=\lambda\mathbf v$.

## Why it works: the Lagrange identity
With $Ly=(py')'+qy$,
$$uLv-vLu=\big[p(uv'-u'v)\big]'\ \Rightarrow\ \int_a^b(uLv-vLu)\,dx=\big[p(uv'-u'v)\big]_a^b.$$
If the boundary term vanishes, $L$ is **self-adjoint** for the inner product $\langle f,g\rangle_r=\int_a^brfg\,dx$. The boundary term vanishes for
- separated conditions $\alpha y(a)+\beta y'(a)=0$ (Dirichlet, Neumann, Robin);
- periodic conditions $y(a)=y(b),\ y'(a)=y'(b)$ with $p(a)=p(b)$;
- **singular** ends where $p(a)=0$ and $y$ is bounded (Legendre at $\pm1$, Bessel at $0$).

## What follows
- Eigenvalues are real.
- Eigenfunctions of different eigenvalues are **orthogonal with weight $r$**: $(\lambda_m-\lambda_n)\int ry_my_n=0$.
- A piecewise smooth $f$ expands as $f\sim\sum a_ny_n$, $\ a_n=\dfrac{\int rfy_n}{\int ry_n^2}$ (generalised Fourier series).
- For regular problems the eigenvalues form an increasing sequence $\lambda_1<\lambda_2<\dots\to\infty$ and $y_n$ has $n-1$ interior zeros (oscillation theorem).

## Getting any 2nd-order equation into SL form
For $y''+fy'+(g+\lambda h)y=0$ multiply by $p=e^{\int f}$: $(py')'+pgy+\lambda hp\,y=0$, so $q=pg,\ r=hp$.

| Equation | $p$ | $q$ | $r$ | eigenvalue |
|---|---|---|---|---|
| $y''+\lambda y=0$ | 1 | 0 | 1 | $\lambda$ |
| Legendre | $1-x^2$ | 0 | 1 | $n(n+1)$ |
| Chebyshev | $\sqrt{1-x^2}$ | 0 | $1/\sqrt{1-x^2}$ | $n^2$ |
| parametric Bessel order $m$ | $x$ | $-m^2/x$ | $x$ | $\lambda^2$ |
| Hermite $y''-2xy'+2ny=0$ | $e^{-x^2}$ | 0 | $e^{-x^2}$ | $2n$ |

## Solving eigenproblems quickly
1. Try $\lambda<0,\ =0,\ >0$ separately.
2. Remove the first-derivative term: $y=e^{-\frac12\int f}z$.
3. Euler equations ($x^2y''+\dots$): $x=e^t$.
4. For weights like $e^{ax}$ or $x^k$ find $s=\int\sqrt{r/p}\,dx$, which turns the equation into $z_{ss}+\lambda z=0$ ([[Assignment 7 - Sturm-Liouville Problems - Solutions]] (g), (h), (i)).
5. **Check the endpoints**: a boundary condition at a singular point ($x=0$ in an Euler equation) may not make the problem self-adjoint, and then the "spectrum" can be empty or continuous (Q3 (j), (k) of the sheet).

![[A7-fig2-orthogonality.png]]
**Figure:** Normalised Gram matrices $\langle y_m,y_n\rangle_r$ for four SLPs: identity up to rounding, i.e. the eigenfunctions are orthogonal for the weight that the SL form dictates.

## Cross-domain links
- [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Eigenvalue problems]] — same structure as symmetric matrices in vibration/normal modes (EE1100 resonance, buckling in [[Euler Buckling of Columns]]): self-adjointness ⇒ real eigenvalues and orthogonal modes.
- The $\sin n\pi x/L$ eigenfunctions of $y''+\lambda y=0$ are the standing-wave modes of a string; Bessel modes are those of a circular drum.

## Worked examples
[[Assignment 7 - Sturm-Liouville Problems - Solutions]] (13 eigenproblems, Gram matrices, expansions in two different eigenbases), [[Assignment 6 - Bessel Functions - Solutions]] Q12 (orthogonality of Bessel functions from the Lagrange identity).

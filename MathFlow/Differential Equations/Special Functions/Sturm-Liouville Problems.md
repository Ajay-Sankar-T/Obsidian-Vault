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


## Worked examples (Lecture 29)
**1. Cauchy–Euler eigenproblem.** $x^2y''+3xy'+\lambda y=0$, $y(1)=y(2)=0$. Try $y=x^m$: $m^2+2m+\lambda=0$, $m=-1\pm\sqrt{1-\lambda}$.
- $\lambda<1$: real distinct roots, $y(1)=0$ forces $c_2=-c_1$, then $y(2)=0$ forces $c_1=0$. No eigenvalue.
- $\lambda=1$: $y=c_1x^{-1}+c_2x^{-1}\ln x$; $y(1)=0\Rightarrow c_1=0$, $y(2)=0\Rightarrow c_2=0$. No eigenvalue.
- $\lambda>1$: $y=x^{-1}\big(c_1\cos(\sqrt{\lambda-1}\ln x)+c_2\sin(\sqrt{\lambda-1}\ln x)\big)$; $y(1)=0\Rightarrow c_1=0$; $y(2)=0\Rightarrow\sqrt{\lambda-1}\,\ln2=n\pi$.

$$\lambda_n=1+\frac{n^2\pi^2}{(\ln2)^2},\qquad y_n=x^{-1}\sin\!\Big(\frac{n\pi\ln x}{\ln2}\Big),\qquad n=1,2,\dots$$
Self-adjoint form $(x^3y')'+\lambda xy=0$: weight $r=x$ (so $\int_1^2x\,y_my_n\,dx=0$).

**2. Absorb a variable coefficient by a change of variable.** $\big((2x+1)^{-1}y'\big)'+\lambda(2x+1)y=0$, $y(0)=y(\pi)=0$. Put $dt=(2x+1)\,dx$, i.e. $t=x^2+x$. Then $\frac d{dx}\big((2x+1)^{-1}y_x\big)=(2x+1)y_{tt}$ and the equation becomes $y_{tt}+\lambda y=0$ on $0<t<\pi(\pi+1)$ with Dirichlet ends:
$$\lambda_n=\frac{n^2}{(\pi+1)^2},\qquad y_n=\sin\frac{n(x^2+x)}{\pi+1}.$$
General recipe: $s=\int\sqrt{r/p}\,dx$ turns $(py')'+\lambda ry=0$ into $z_{ss}+\lambda z=0$ (as in point 4 above).

**3. Cauchy–Euler in logarithmic variable.** $x^2y''+xy'+\lambda y=0$, $y(1)=y(e)=0$: $t=\ln x$ gives $y_{tt}+\lambda y=0$ on $[0,1]$, so $\lambda_n=n^2\pi^2$, $y_n=\sin(n\pi\ln x)$ with weight $1/x$: $\int_1^e\frac{\sin(m\ln x)\sin(n\ln x)}{x}dx=\int_0^1\sin m\pi t\sin n\pi t\,dt=0$. Expansion $f\sim\sum c_n\sin(n\pi\ln x)$, $c_n=2\int_1^e\frac{f(x)}x\sin(n\pi\ln x)\,dx$.

**4. Self-adjoint form of two named equations.**
- $y''+\frac2xy'+\lambda y=0$ ($x>0$): $p=e^{\int2/x}=x^2$, so $(x^2y')'+\lambda x^2y=0$, weight $x^2$ (spherical Bessel).
- Chebyshev $(1-x^2)y''-xy'+n^2y=0$: $p=\sqrt{1-x^2}$, so $\big(\sqrt{1-x^2}\,y'\big)'+\frac{n^2}{\sqrt{1-x^2}}y=0$, weight $\frac1{\sqrt{1-x^2}}$.

**5. Periodic and Robin cases.** Periodic $y''+\lambda y=0$, $y(-\pi)=y(\pi)$, $y'(-\pi)=y'(\pi)$: $\lambda_n=n^2$, eigenfunctions $1$ (simple) and $\cos nx,\sin nx$ (multiplicity 2 for $n\ge1$). Robin $y''+\lambda y=0$, $y(0)=0$, $y'(1)+2y(1)=0$: $y=\sin px$ with $p\cos p+2\sin p=0$, i.e. $\tan p=-p/2$, which has no closed-form roots (found graphically or numerically, $\lambda_n=p_n^2$).

**6. Expansion of a constant.** $1\sim\sum c_n\sin\frac{n\pi x}L$ on $(0,L)$: $c_n=\frac2L\int_0^L\sin\frac{n\pi x}L\,dx=\frac2{n\pi}\big(1-(-1)^n\big)=\frac4{n\pi}$ for odd $n$, so $1\sim\frac4\pi\sum_{n\text{ odd}}\frac1n\sin\frac{n\pi x}L$.

These eigenfunctions are the spatial parts used in [[Separation of Variables]] for the wave, heat and Laplace equations ([[PDEs - MOC]]).

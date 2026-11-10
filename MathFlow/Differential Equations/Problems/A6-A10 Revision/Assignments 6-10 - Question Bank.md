---
title: Assignments 6–10 – Question Bank
course: MA 2102 Differential Equations
tags: [DE, question-bank, MOC]
up: "[[Problems - MOC]]"
aliases: [DE question bank, MA2102 practice questions, Bessel Sturm-Liouville PDE practice, Assignments 6-10 practice]
---

# Assignments 6–10 — Question Bank

Part of [[Problems - MOC]] · formulas: [[Assignments 6-10 - Formula Bank]] · methods: [[Assignments 6-10 - How to Solve]] · the solved sheets: [[Assignment 6 - Bessel Functions - Solutions]], [[Assignment 7 - Sturm-Liouville Problems - Solutions]], [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]], [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]], [[Assignment 10 - Laplace Equations - Solutions]]

> [!abstract] What it is
> About 90 new questions on the second half of MA 2102, none of them copied from the assignment sheets: **34 conceptual questions** and **34 numerical problems** with hints and worked solutions in three parts, and **21 multiple-choice questions** on this page. Every numerical answer is recomputed in `Tools/de_a610_bank.py` and `Tools/de_a610_bank_pdes.py` (closed forms substituted symbolically into the ODE or PDE and the data; series compared with quadrature and, for Q7 and Q8 of Part 3, with a finite-difference simulation). Solutions sit in folds: write your answer first.

## The three parts

| Part | Sheets | Conceptual | Numerical (Q) | Highlights |
|---|---|---|---|---|
| [[DE Question Bank 1 - Bessel Functions and Sturm-Liouville]] | 6, 7 | A1–A12 | Q1–Q10 | recurrences, closed-form integrals, an equation with an elementary Bessel solution, Fourier–Bessel series of $1-x^2$, McMahon zeros, addition theorem, Hermite and Laguerre weights, a Robin problem with $\lambda=0$, an Euler eigenproblem, a Chebyshev expansion |
| [[DE Question Bank 2 - First-Order PDEs and Canonical Forms]] | 8 | A1–A10 | Q1–Q10 | forming PDEs, symmetric Lagrange system, Cauchy data and characteristic data, Burgers breaking, Clairaut singular integral, type regions, canonical form with variable coefficients, a parabolic Cauchy problem, removing first-order terms |
| [[DE Question Bank 3 - Wave, Heat and Laplace Equations]] | 9, 10 | A1–A12 | Q1–Q14 | struck string, reflection at a wall, plucked string energy, fixed–free bar, cooling times, source term, mixed boundary data, rectangle, insulated bottom, disk and exterior, annulus, closed forms on a quarter and a half disk |

![[A610-FB-3-mode-factors.png]]

**Figure** (from the Formula Bank): one set of Fourier modes, three behaviours. Wave: constant amplitude. Heat: decay in time, faster for higher $n$. Laplace: decay in space away from the driven edge.

## How to use it

1. **After a lecture block:** do the conceptual questions for the topic without notes; open a fold only after writing your answer.
2. **Before the tutorial:** do two numericals from the same sheet cold. Compare the *setup* (hint) first, then the answer.
3. **Revision:** pick a mixed set from the skill table below; allow about 15 minutes each. If the setup takes more than 3 minutes, re-read the matching section of the [[Assignments 6-10 - How to Solve]] page.
4. **Final days:** the 21 multiple-choice questions below (3 minutes each), then the Formula Bank "errors that cost marks" table.

## Which question tests which skill

| Skill | Where |
|---|---|
| Bessel recurrences and derivative identities | Part 1 Q1, Q6 |
| Bessel integrals, closed form or not | Part 1 Q2, A5 |
| Reduction to Bessel form | Part 1 Q3 |
| Fourier–Bessel coefficients, Parseval | Part 1 Q4, A4, A6 |
| S–L form, weights, orthogonality | Part 1 Q7, A7, A8, A10 |
| Eigenvalue problems with awkward conditions (Robin, Euler) | Part 1 Q8, Q9 |
| Expansion convergence and Gibbs | Part 1 A11, A12, Q9 |
| Eliminating constants or functions | Part 2 Q1 |
| Lagrange with multipliers; Cauchy data | Part 2 Q2, Q3, Q4 |
| Breaking of solutions | Part 2 Q5, A5 |
| Clairaut, complete and singular integrals | Part 2 Q6, A1 |
| Classification and canonical form | Part 2 Q7, Q8, Q9, Q10 |
| d'Alembert, reflections, domains of dependence | Part 3 Q1, Q2 |
| Vibrating string modes, energy, parity | Part 3 Q3, Q4 |
| Heat: decay times, steady-state shift, sources | Part 3 Q5, Q6, Q7, Q8 |
| Laplace on rectangles | Part 3 Q9, Q10 |
| Laplace in polar coordinates, closed forms | Part 3 Q11–Q14 |

## Errors that cost marks (all parts)

The full table is at the end of the [[Assignments 6-10 - Formula Bank]]. The ones these questions are built to catch:

| Error | Where it appears |
|---|---|
| Using $J_{-n}$ as a second solution for an integer order | Part 1 A1 |
| Forgetting $\lambda=0$ (Neumann, or a Robin condition with a negative sign) | Part 1 Q8, A9 |
| Missing the weight $x$ (or $1/x$) in an expansion | Part 1 Q4, Q9 |
| Treating data on a characteristic curve as an ordinary Cauchy problem | Part 2 Q4 |
| Classifying a PDE with the lower-order terms | Part 2 Q7 |
| Expanding $f$ instead of $f-w$ after subtracting the steady state | Part 3 Q7, Q8 |
| Dropping the $\frac1{\omega_n}$ in $B_n$ | Part 3 A3, Q4 |
| Wrong denominator in $\sinh(n\pi y/a)/\sinh(n\pi b/a)$ | Part 3 Q9 |
| Odd extension for a free end (or even for a fixed one) | Part 3 Q2, A2 |

## 21 quick-fire multiple choice questions

### Bessel functions

> [!question]- 1. For integer $n$, $J_{-n}(x)$ equals: (a) $-J_n$ (b) $(-1)^nJ_n$ (c) $Y_n$ (d) $0$
> **(b).** The $1/\Gamma$ factor kills the first $n$ terms; shifting the index gives $(-1)^nJ_n$.

> [!question]- 2. The Wronskian $W(J_\nu,Y_\nu)$ is: (a) $\dfrac{2}{\pi x}$ (b) $\dfrac{1}{x}$ (c) $\dfrac{\pi}{2x}$ (d) $0$
> **(a).** Any two solutions have $W=c/x$ (Abel); for this pair $c=\frac2\pi$.

> [!question]- 3. $\displaystyle\int xJ_0(x)\,dx$ equals: (a) $xJ_1+C$ (b) $J_1+C$ (c) $-xJ_1+C$ (d) $\tfrac12x^2J_1+C$
> **(a).** $(xJ_1)'=xJ_0$ (R1 with $\nu=1$).

> [!question]- 4. $J_{1/2}(x)^2+J_{-1/2}(x)^2$ equals: (a) $1$ (b) $\dfrac2{\pi x}$ (c) $\dfrac2\pi$ (d) $\dfrac1x$
> **(b).** $\frac2{\pi x}(\sin^2x+\cos^2x)$.

> [!question]- 5. Which of these integrals is **not** a finite combination of Bessel functions? (a) $\int x^3J_0$ (b) $\int J_3$ (c) $\int x^4J_0$ (d) $\int x^{-2}J_5$
> **(c).** The criterion is that $\mu+\nu$ be a positive odd integer: $3,3,4,3$. $\int x^4J_0$ ends in $\int J_0$.

> [!question]- 6. The Fourier–Bessel series $\sum a_nJ_0(\alpha_nx)$ of a function with $f(1)=2$ converges at $x=1$ to: (a) $2$ (b) $1$ (c) $0$ (d) it diverges
> **(c).** Every $J_0(\alpha_n)=0$.

> [!question]- 7. A solution of $y''+9xy=0$ is: (a) $\sqrt xJ_{1/3}(2x^{3/2})$ (b) $\sqrt xJ_{1/3}(3x^{3/2})$ (c) $xJ_{2/3}(2x^{3/2})$ (d) $J_{1/3}(2x^{3/2})$
> **(a).** $a=\frac12$ (no $y'$ term), $c=\frac32$, $b^2c^2=9\Rightarrow b=2$, $n=a/c=\frac13$.

### Sturm–Liouville

> [!question]- 8. The weight function for Hermite's equation $y''-2xy'+\mu y=0$ is: (a) $1$ (b) $e^{-x}$ (c) $e^{-x^2}$ (d) $\dfrac1{\sqrt{1-x^2}}$
> **(c).** $p=e^{\int-2x}=e^{-x^2}$, $q=0$, $r=p$.

> [!question]- 9. The eigenvalues of $y''+\lambda y=0$, $y'(0)=0$, $y(\pi)=0$ are: (a) $n^2$ (b) $(n-\tfrac12)^2$, $n\ge1$ (c) $(2n)^2$ (d) $\dfrac{n^2}4$
> **(b).** $y=\cos\mu x$, $\cos\mu\pi=0\Rightarrow\mu=n-\frac12$.

> [!question]- 10. Which problem on $[0,L]$ has $\lambda=0$ as an eigenvalue? (a) $y(0)=y(L)=0$ (b) $y'(0)=y'(L)=0$ (c) $y(0)=0,\ y'(L)=0$ (d) $y'(0)=0,\ y(L)=0$
> **(b).** The constant $y=1$ satisfies both Neumann conditions.

> [!question]- 11. On $[0,2\pi]$ with periodic conditions the eigenvalue $\lambda=4$ of $y''+\lambda y=0$ has: (a) one eigenfunction (b) two (c) three (d) none
> **(b).** $\cos2x$ and $\sin2x$.

> [!question]- 12. The coefficients $b_n$ of the sine series of $f=1$ on $(0,L)$ decay like: (a) $\dfrac1n$ (b) $\dfrac1{n^2}$ (c) $\dfrac1{n^3}$ (d) $e^{-n}$
> **(a).** $b_n=\frac{2(1-(-1)^n)}{n\pi}$: $f$ does not vanish at the ends.

### PDEs

> [!question]- 13. The general solution of $xu_x+yu_y=u$ is: (a) $u=xf(y/x)$ (b) $u=f(xy)$ (c) $u=f(x)+g(y)$ (d) $u=f(x-y)$
> **(a).** $\frac{dx}x=\frac{dy}y=\frac{du}u$: $\frac yx$ and $\frac ux$ are constant; homogeneous of degree $1$.

> [!question]- 14. Eliminating $f$ from $u=f(x^2+y^2)$ gives: (a) $xp+yq=0$ (b) $yp-xq=0$ (c) $p=q$ (d) $p+q=u$
> **(b).** $p=2xf'$, $q=2yf'$.

> [!question]- 15. The equation $u_{xx}+4u_{xy}+4u_{yy}=0$ is: (a) hyperbolic (b) parabolic (c) elliptic (d) of mixed type
> **(b).** $\Delta=16-16=0$; $(\partial_x+2\partial_y)^2u=0$.

> [!question]- 16. Tricomi's equation $yu_{xx}+u_{yy}=0$ at $y=-1$ is: (a) hyperbolic (b) parabolic (c) elliptic (d) undefined
> **(a).** $\Delta=-4y=4>0$.

> [!question]- 17. $u_{tt}=4u_{xx}$ on $\mathbb R$ with $u(x,0)=0$, $u_t(x,0)=1$ has the solution: (a) $u=t$ (b) $u=2t$ (c) $u=t/2$ (d) $u=x t$
> **(a).** $\frac1{2c}\int_{x-2t}^{x+2t}1\,ds=\frac{4t}4=t$.

> [!question]- 18. A fixed–free string has fundamental frequency $\omega_1$. The first overtone has frequency: (a) $2\omega_1$ (b) $3\omega_1$ (c) $4\omega_1$ (d) $\tfrac32\omega_1$
> **(b).** $\omega_n=\frac{(2n-1)\pi c}{2L}$: $1:3:5:\dots$

> [!question]- 19. A rod of length $L$ is made of the same material but doubled to $2L$. The cooling time constant of its slowest mode becomes: (a) $\tfrac12$ (b) $2$ (c) $4$ (d) unchanged
> **(c).** $\tau_1=\frac{L^2}{\pi^2c^2}\propto L^2$.

> [!question]- 20. A rod of length $L$ is insulated, with initial temperature $u(x,0)=x$. The final uniform temperature is: (a) $L$ (b) $\dfrac L2$ (c) $0$ (d) $\dfrac L3$
> **(b).** The mean is conserved: $\frac1L\int_0^Lx\,dx$.

### Laplace

> [!question]- 21. $\nabla^2u=0$ in $r<1$ with $u(1,\theta)=2+\cos\theta+3\sin2\theta$. Then $u(0)$ equals: (a) $0$ (b) $1$ (c) $2$ (d) $3$
> **(c).** The mean value property: $u(0)$ is the average of the boundary data, $2$ (the $\cos\theta$ and $\sin2\theta$ terms average to zero).

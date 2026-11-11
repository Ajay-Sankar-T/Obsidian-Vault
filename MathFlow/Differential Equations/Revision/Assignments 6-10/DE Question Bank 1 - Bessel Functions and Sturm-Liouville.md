---
title: DE Question Bank 1 – Bessel Functions and Sturm–Liouville
course: MA 2102 Differential Equations
tags: [DE, question-bank, tutorial]
up: "[[Assignments 6-10 - Question Bank]]"
aliases: [Bessel practice problems, Sturm-Liouville practice problems, DE question bank 1, Assignments 6 and 7 practice]
---

# DE Question Bank 1 — Bessel Functions and Sturm–Liouville

Part of [[Assignments 6-10 - Question Bank]] · formulas: [[Assignments 6-10 - Formula Bank]] (§1–§2) · method: [[Assignments 6-10 - How to Solve]] (§2–§3) · solved sheets: [[Assignment 6 - Bessel Functions - Solutions]], [[Assignment 7 - Sturm-Liouville Problems - Solutions]] · theory: [[Bessel's Equation and Bessel Functions of the First Kind]], [[Bessel Function Properties and Recurrence Relations]], [[Reducing Equations to Bessel Form]], [[Fourier-Bessel Series]], [[Sturm-Liouville Problems]]

> [!abstract] What is here
> Twelve conceptual questions (Part A: six on Bessel functions, six on Sturm–Liouville) and ten numerical problems (Q1–Q10), none of them on the assignment sheets. Try each on paper; open **Hint** only if stuck, then **Solution**. Every number is recomputed in `Tools/de_a610_bank.py` (functions `p1_q1` … `p1_q10`).

## Part A — Conceptual questions

> [!question]- A1. Why can $J_\nu$ and $J_{-\nu}$ not serve as a basis when $\nu$ is an integer, and what replaces $J_{-\nu}$?
> For $\nu=n$, $J_{-n}=(-1)^nJ_n$: the poles of $\Gamma$ kill the first $n$ terms of the series, so the two are proportional. Equivalently $W(J_\nu,J_{-\nu})=-\frac{2\sin\nu\pi}{\pi x}$ vanishes. The second solution is $Y_n=\lim_{\nu\to n}\frac{J_\nu\cos\nu\pi-J_{-\nu}}{\sin\nu\pi}$, which contains a logarithm (the Frobenius case of exponents differing by an integer). $AJ_\nu+BY_\nu$ is a basis for **every** $\nu$.

> [!question]- A2. A problem on a disk includes the centre $r=0$. Which Bessel solution do you keep and why?
> $J_\nu(\lambda r)$ only. $J_\nu\sim(r/2)^\nu/\Gamma(\nu+1)$ is finite at $0$, while $Y_\nu\sim-\frac{\Gamma(\nu)}\pi(2/r)^\nu$ (and $Y_0\sim\frac2\pi\ln r$) is unbounded, so a physical (bounded) solution has $B=0$. The same rule discards $r^{-n}$ and $\ln r$ in Laplace's equation.

> [!question]- A3. Why are the half-integer Bessel functions elementary? Where do the spherical Bessel functions arise?
> For $\nu=\frac12$ the series $\sum\frac{(-1)^k}{k!\Gamma(k+\frac32)}(\frac x2)^{2k+\frac12}$ sums to $\sqrt{\frac2{\pi x}}\sin x$, and R3 then produces every $J_{n+\frac12}$ as a polynomial in $\frac1x$ times $\sin x,\cos x$. The spherical Bessel functions $j_n=\sqrt{\frac\pi{2x}}J_{n+\frac12}$ are the radial functions of the three-dimensional Helmholtz equation (waves or heat in a sphere).

> [!question]- A4. State the orthogonality relation for $J_\nu(\alpha_kx/L)$ and explain where the weight $x$ comes from.
> $\int_0^LxJ_\nu(\frac{\alpha_jx}L)J_\nu(\frac{\alpha_kx}L)dx=0$ for $j\ne k$ and $=\frac{L^2}2J_{\nu+1}(\alpha_k)^2$ for $j=k$ ($\alpha_k$ the positive zeros of $J_\nu$). Written in S–L form the parametric Bessel equation is $(xy')'+\big(\lambda^2x-\frac{\nu^2}x\big)y=0$: $p=x$, weight $r=x$. With weight $1$ the functions are **not** orthogonal.

> [!question]- A5. When is $\int x^\mu J_\nu\,dx$ a finite combination of Bessel functions? Why that condition?
> When $\mu+\nu$ is a positive odd integer (e.g. $\int x^3J_0$, $\int J_5$, $\int x^{-2}J_5$; **not** $\int x^4J_0$ or $\int J_0$). The reduction $\int x^pJ_\nu=x^pJ_{\nu+1}-(p-\nu-1)\int x^{p-1}J_{\nu+1}$ keeps $p+\nu$ fixed and lowers $p-\nu$ by $2$ each time. It stops with the coefficient $p-\nu-1=0$ (giving $x^{\nu+1}J_{\nu+1}$) when $p-\nu-1$ is a non-negative even integer. When $p<\nu+1$ use the mirror-image reduction that lowers the order with R2 (that is how $\int x^{-2}J_5$ closes). If neither stops, the process ends in the non-elementary $\int J_0$.

> [!question]- A6. A function $f$ with $f(L)\ne0$ is expanded in $J_0(\alpha_nx/L)$. What does the series do at $x=L$, and what does this say about convergence?
> Every term vanishes there because $J_0(\alpha_n)=0$, so the series sums to $0$ at $x=L$ whatever $f(L)$ is. The convergence is therefore not uniform near $L$ (a boundary layer with an overshoot), the Bessel analogue of a Fourier sine series of a function that does not vanish at the end.

> [!question]- A7. Which boundary conditions make an S–L operator self-adjoint?
> Those for which the Lagrange boundary term $\big[p(uv'-u'v)\big]_a^b$ vanishes for all admissible $u,v$: **separated** conditions (Dirichlet, Neumann, Robin), **periodic** conditions ($p(a)=p(b)$), and a **singular end** where $p=0$ and the functions stay bounded (as for Legendre at $\pm1$, Bessel at $0$). A condition imposed at a singular end that does not select bounded solutions (as in Assignment 7 Q3(j),(k)) does not give an S–L problem.

> [!question]- A8. Why are the eigenvalues real and eigenfunctions of different eigenvalues orthogonal?
> Take $Ly=-\lambda ry$ with $\bar y$ the conjugate eigenfunction. Green's identity gives $0=\int(\bar yLy-yL\bar y)=(\bar\lambda-\lambda)\int r|y|^2$, so $\lambda=\bar\lambda$. For two eigenpairs the same identity gives $(\lambda_m-\lambda_n)\int ry_my_n=0$, so the integral vanishes when $\lambda_m\ne\lambda_n$.

> [!question]- A9. Why does the Neumann problem $y''+\lambda y=0$, $y'(0)=y'(L)=0$ have $\lambda=0$ but the Dirichlet problem does not?
> $y=$ constant satisfies $y'=0$, so $\lambda=0$ is an eigenvalue with $y_0=1$. A Dirichlet condition forces the constant to be $0$. From the energy identity $\lambda\int ry^2=\int py'^2+[\text{boundary term}]$, $\lambda=0$ needs $y'\equiv0$, so the answer depends on whether the boundary conditions allow a nonzero constant. (The same reason is why heat in an insulated rod keeps its mean temperature.)

> [!question]- A10. How do you find the orthogonality weight for an ODE such as Hermite's $y''-2xy'+\mu y=0$?
> Write $y''+fy'+(g+\lambda h)y=0$ and multiply by $p=e^{\int f}$: here $f=-2x$, $p=e^{-x^2}$, so $(e^{-x^2}y')'+\mu e^{-x^2}y=0$ and the weight is $r=e^{-x^2}$. The orthogonality relation is then $\int_{-\infty}^\infty H_mH_ne^{-x^2}dx=0$.

> [!question]- A11. What does an eigenfunction series converge to at a jump of $f$? What is Gibbs' phenomenon?
> To the midpoint $\frac12[f(x^-)+f(x^+)]$. Near the jump the partial sums overshoot by about $9\%$ of the jump size, and the overshoot does not shrink as more terms are added (its width does). It occurs for Fourier–Bessel, Fourier–Legendre and every S–L expansion.

> [!question]- A12. Why does the decay rate of the coefficients depend on the boundary conditions that $f$ satisfies?
> Integrate by parts: $b_n=\frac2L\int_0^Lf\sin\frac{n\pi x}L\,dx=\frac2{n\pi}\big[f(0)-(-1)^nf(L)\big]+\frac2{n\pi}\int f'\cos\dots$. If $f$ does not vanish at an end the boundary term gives $b_n\sim n^{-1}$ (slow, Gibbs-like); if $f(0)=f(L)=0$ but $f'$ jumps, $b_n\sim n^{-2}$; if also $f''$ is nonzero at the ends, $b_n\sim n^{-3}$ (as for $x(L-x)$, $8L^2/(n\pi)^3$). Each extra boundary condition of the basis that $f$ already satisfies buys one more power of $\frac1n$.

---

## Q1 — Recurrence from two table values (easy)

Given $J_0(2)=0.223891$ and $J_1(2)=0.576725$, find $J_2(2),J_3(2),J_4(2)$ and $J_1'(2)$ using only recurrences.

> [!tip]- Hint
> R3 with $x=2$ reads $J_{k+1}=kJ_k-J_{k-1}$. For the derivative use R1′ with $\nu=1$.

> [!success]- Solution
> $J_2=1\cdot J_1-J_0=0.576725-0.223891=\mathbf{0.352834}$.
>
> $J_3=2J_2-J_1=0.705668-0.576725=\mathbf{0.128943}$.
>
> $J_4=3J_3-J_2=0.386830-0.352834=\mathbf{0.033996}$.
>
> $J_1'=J_0-\dfrac{J_1}x=0.223891-0.288362=\mathbf{-0.064472}$.
>
> **Check:** for small argument $J_{n+1}/J_n\approx\frac x{2(n+1)}=0.25$ at $n=3$; the computed $J_4/J_3=0.264$. Scipy gives $J_2=0.352834$, $J_3=0.128943$, $J_4=0.033996$.

## Q2 — A closed-form integral (easy)

Evaluate $\displaystyle\int_0^1x^3J_0(x)\,dx$. Does $\int_0^1x^4J_0(x)\,dx$ have a closed form?

> [!tip]- Hint
> Write $x^3J_0=x^2\cdot xJ_0$ and use $(xJ_1)'=xJ_0$, then $(x^2J_2)'=x^2J_1$.

> [!success]- Solution
> $\int x^3J_0=\int x^2(xJ_1)'dx=x^3J_1-2\int x^2J_1\,dx=x^3J_1-2x^2J_2+C$.
>
> $\big[x^3J_1-2x^2J_2\big]_0^1=J_1(1)-2J_2(1)=0.440051-2(0.114903)=\mathbf{0.210244}$ (numerical quadrature agrees).
>
> For $\int x^4J_0$: $p+\nu=4$ is even, so the reduction never terminates in Bessel functions; it ends in $\int J_0$ (as in Assignment 6 Q3(a)). No closed form.

## Q3 — A Bessel equation with an elementary solution (medium)

Solve $x^2y''+xy'+(16x^4-9)y=0$, and show that the solutions are elementary.

> [!tip]- Hint
> Divide by $x^2$ and match $y''+\frac{1-2a}xy'+\big(b^2c^2x^{2c-2}+\frac{a^2-n^2c^2}{x^2}\big)y=0$. The order $n$ is a half-integer.

> [!success]- Solution
> Monic form: $y''+\frac1xy'+\big(16x^2-\frac9{x^2}\big)y=0$. $1-2a=1\Rightarrow a=0$. $2c-2=2\Rightarrow c=2$, $b^2c^2=16\Rightarrow b=2$. $a^2-n^2c^2=-9\Rightarrow n=\tfrac32$.
>
> $\displaystyle y=AJ_{3/2}(2x^2)+BJ_{-3/2}(2x^2).$
>
> With $J_{3/2}(z)=\sqrt{\frac2{\pi z}}\Big(\frac{\sin z}z-\cos z\Big)$, $J_{-3/2}(z)=-\sqrt{\frac2{\pi z}}\Big(\frac{\cos z}z+\sin z\Big)$ and $z=2x^2$, $\sqrt{\frac2{\pi z}}=\frac1{x\sqrt\pi}$:
>
> $\displaystyle \boxed{y=\frac1x\Big[A'\Big(\frac{\sin2x^2}{2x^2}-\cos2x^2\Big)+B'\Big(\frac{\cos2x^2}{2x^2}+\sin2x^2\Big)\Big]}$
>
> Both functions were substituted into the ODE (residual $<10^{-10}$ at three points).

## Q4 — Fourier–Bessel series of $1-x^2$ (hard)

Expand $f(x)=1-x^2$ on $[0,1]$ in $\sum a_nJ_0(\alpha_nx)$, $J_0(\alpha_n)=0$. (a) Show $a_n=\dfrac8{\alpha_n^3J_1(\alpha_n)}$. (b) Compute $a_1,a_2,a_3$. (c) Use Parseval to find how much of $\int_0^1xf^2\,dx$ the first term carries.

> [!tip]- Hint
> $a_n=\frac2{J_1(\alpha_n)^2}\int_0^1x(1-x^2)J_0(\alpha_nx)\,dx$. Substitute $t=\alpha_nx$ and use Q2's reduction; at a zero of $J_0$, R3 with $\nu=1$ gives $J_2=\frac2\alpha J_1$.

> [!success]- Solution
> $\int_0^1xJ_0(\alpha x)dx=\dfrac{J_1(\alpha)}\alpha$ and $\int_0^1x^3J_0(\alpha x)dx=\dfrac1{\alpha^4}\big[\alpha^3J_1-2\alpha^2J_2\big]=\dfrac{J_1}\alpha-\dfrac{2J_2}{\alpha^2}$. The difference is $\dfrac{2J_2(\alpha)}{\alpha^2}$, so
>
> $a_n=\dfrac{4J_2(\alpha_n)}{\alpha_n^2J_1(\alpha_n)^2}$. At a zero of $J_0$, $J_2=\frac2\alpha J_1$:
>
> $\displaystyle \boxed{a_n=\frac{8}{\alpha_n^3J_1(\alpha_n)}}$
>
> (b) $\alpha_n=2.4048,\ 5.5201,\ 8.6537$; $J_1(\alpha_n)=0.5191,\ -0.3403,\ 0.2715$. Hence $a_1=\mathbf{1.1080},\ a_2=\mathbf{-0.1398},\ a_3=\mathbf{0.0455}$. Partial sums at $x=0$: $1.108,\ 0.968,\ 1.014\to1$.
>
> (c) Parseval: $\sum a_n^2\frac{J_1(\alpha_n)^2}2=\int_0^1x(1-x^2)^2dx=\frac16$ (confirmed with $4000$ terms). The first term gives $\frac12(1.1080)^2(0.5191)^2=0.16544$, i.e. **$99.3\%$** of $\frac16$.
>
> **Check:** the series at $x=0.5$ with many terms gives $0.75=1-0.25$; at $x=1$ every term vanishes and $f(1)=0$ agrees, so convergence is fast (the data meet the boundary condition).

## Q5 — Zeros by McMahon's formula (easy)

Estimate the tenth positive zeros of $J_0$ and $J_1$ with $j_{\nu,s}\approx\beta-\dfrac{4\nu^2-1}{8\beta}$, $\beta=\big(s+\frac\nu2-\frac14\big)\pi$, and compare with the exact values $30.6346$ and $32.1897$. What spacing do consecutive zeros approach?

> [!tip]- Hint
> Insert $s=10$, $\nu=0$ then $\nu=1$.

> [!success]- Solution
> $\nu=0$: $\beta=9.75\pi=30.6305$, correction $-\frac{-1}{8\beta}=+0.0041$, so $j_{0,10}\approx\mathbf{30.6346}$ (exact $30.6346$).
>
> $\nu=1$: $\beta=10.25\pi=32.2013$, correction $-\frac3{8\beta}=-0.0116$, so $j_{1,10}\approx\mathbf{32.1897}$ (exact $32.1897$).
>
> Consecutive zeros differ by $\to\pi$ (the $19$th and $20$th zeros of $J_0$ are $3.14149$ apart), because $J_\nu\sim\cos(x-\frac{\nu\pi}2-\frac\pi4)$.

## Q6 — The addition theorem (medium)

(a) Use the generating function to prove $J_n(x+y)=\sum_{k\in\mathbb Z}J_k(x)J_{n-k}(y)$. (b) Deduce $J_0(2x)=J_0(x)^2+2\sum_{k\ge1}(-1)^kJ_k(x)^2$ and evaluate $J_0(2.6)$ from $J_0(1.3)=0.62009$, $J_1=0.52202$, $J_2=0.18303$, $J_3=0.04114$, $J_4=0.00683$.

> [!tip]- Hint
> Multiply the generating functions of $x$ and $y$: $e^{\frac x2(t-\frac1t)}e^{\frac y2(t-\frac1t)}=e^{\frac{x+y}2(t-\frac1t)}$, and compare the coefficient of $t^n$.

> [!success]- Solution
> (a) The coefficient of $t^n$ on the left is $\sum_kJ_k(x)J_{n-k}(y)$ (Cauchy product); on the right it is $J_n(x+y)$. ∎
>
> (b) $n=0$, $y=x$: $J_0(2x)=\sum_kJ_k(x)J_{-k}(x)=J_0^2+2\sum_{k\ge1}(-1)^kJ_k^2$ using $J_{-k}=(-1)^kJ_k$.
>
> Partial sums at $x=1.3$: $J_0^2=0.38451$; $-2J_1^2\to-0.16051$; $+2J_2^2\to-0.09351$; $-2J_3^2\to-0.09690$; $+2J_4^2\to-0.09680$; the next term changes the fifth decimal.
>
> $\displaystyle \boxed{J_0(2.6)=-0.09680}\qquad(\text{table: }-0.0968)$

## Q7 — Hermite and Laguerre in Sturm–Liouville form (easy)

Write $y''-2xy'+\mu y=0$ and $xy''+(1-x)y'+\lambda y=0$ in S–L form, state the weights, and verify $\int H_2H_4e^{-x^2}dx=0$ and $\int_0^\infty L_1L_2e^{-x}dx=0$ for $H_2=4x^2-2$, $H_4=16x^4-48x^2+12$, $L_1=1-x$, $L_2=1-2x+\frac{x^2}2$.

> [!tip]- Hint
> $p=e^{\int f}$ with $f$ the coefficient of $y'$ after dividing by the coefficient of $y''$; weight $r=hp$. Use $\int_{-\infty}^\infty x^{2k}e^{-x^2}dx=\Gamma(k+\frac12)$ and $\int_0^\infty x^ke^{-x}dx=k!$.

> [!success]- Solution
> Hermite: $f=-2x$, $p=e^{-x^2}$: $\big(e^{-x^2}y'\big)'+\mu e^{-x^2}y=0$; **weight $e^{-x^2}$** on $(-\infty,\infty)$.
>
> Laguerre: $f=\frac{1-x}x=\frac1x-1$, $p=xe^{-x}$, $h=\frac1x$: $\big(xe^{-x}y'\big)'+\lambda e^{-x}y=0$; **weight $e^{-x}$** on $(0,\infty)$.
>
> $H_2H_4=64x^6-224x^4+144x^2-24$; with $\int x^{2k}e^{-x^2}=\sqrt\pi\,(1,\tfrac12,\tfrac34,\tfrac{15}8)$ for $k=0,1,2,3$: $\sqrt\pi\big(64\cdot\tfrac{15}8-224\cdot\tfrac34+144\cdot\tfrac12-24\big)=\sqrt\pi(120-168+72-24)=\mathbf0$ ✓.
>
> $L_1L_2=1-3x+\frac52x^2-\frac12x^3$; $\int_0^\infty(\cdot)e^{-x}dx=1-3+\frac52\cdot2-\frac12\cdot6=1-3+5-3=\mathbf0$ ✓.

## Q8 — A Robin condition with the "wrong" sign (hard)

Find **all** eigenvalues and eigenfunctions of $y''+\lambda y=0$, $y(0)=0$, $y(1)=y'(1)$. Show that eigenfunctions are orthogonal (including the one for $\lambda=0$) and compute the norms.

> [!tip]- Hint
> Treat $\lambda<0$, $\lambda=0$, $\lambda>0$ separately. For $\lambda>0$ the condition is $\sin\mu=\mu\cos\mu$. Check $y=x$.

> [!success]- Solution
> $\lambda=-\kappa^2<0$: $y=\sinh\kappa x$, condition $\sinh\kappa=\kappa\cosh\kappa$, i.e. $\tanh\kappa=\kappa$. Since $\tanh\kappa<\kappa$ for all $\kappa>0$ there is **no** negative eigenvalue.
>
> $\lambda=0$: $y=Ax+B$, $y(0)=0\Rightarrow B=0$; $y(1)=A=y'(1)=A$ ✓. So **$\lambda_0=0$ with $y_0=x$** is an eigenpair (the point of the problem).
>
> $\lambda=\mu^2>0$: $y=\sin\mu x$, $\sin\mu=\mu\cos\mu$, i.e. $\tan\mu=\mu$. On $(0,\frac\pi2)$, $\tan\mu>\mu$, so the first root is in $(\pi,\frac{3\pi}2)$:
>
> $\displaystyle \mu_n=4.4934,\ 7.7253,\ 10.9041,\ 14.0662,\dots,\qquad\lambda_n=\mu_n^2=20.19,\ 59.68,\ 118.90,\ 197.86,\dots$
>
> Orthogonality to $y_0$: $\int_0^1x\sin\mu x\,dx=\dfrac{\sin\mu-\mu\cos\mu}{\mu^2}=0$ by the eigen-condition ✓; between roots, $\int_0^1\sin\mu_mx\sin\mu_nx\,dx=0$ (checked to $10^{-12}$).
>
> Norms: $\|y_0\|^2=\frac13$, $\ \|y_n\|^2=\frac12-\frac{\sin2\mu_n}{4\mu_n}=0.4764,\ 0.4918,\ 0.4958,\dots\to\frac12$.
>
> **Lesson:** Robin conditions with a negative coefficient can produce $\lambda=0$ (here exactly at $h=-1/L$); never drop the $\lambda\le0$ cases.

## Q9 — An Euler eigenproblem and its expansion (medium)

(a) Solve $x^2y''+xy'+\lambda y=0$, $y'(1)=0$, $y(e^2)=0$ and give the weight. (b) Expand $f(x)=1$ on $[1,e^2]$ in the eigenfunctions. (c) What does the series give at $x=1$ and at $x=e^2$?

> [!tip]- Hint
> $t=\ln x$: $y'(x)=Y'(t)/x$, and $[1,e^2]\to[0,2]$. The S–L form is $(xy')'+\frac\lambda xy=0$.

> [!success]- Solution
> (a) $Y''+\lambda Y=0$, $Y'(0)=0$, $Y(2)=0$: $Y=\cos\mu t$, $\cos2\mu=0$, $\mu_n=\dfrac{(2n-1)\pi}4$.
>
> $\displaystyle \lambda_n=\Big(\frac{(2n-1)\pi}4\Big)^2=0.6169,\ 5.5517,\ 15.4213,\dots,\qquad y_n=\cos(\mu_n\ln x),\qquad\text{weight }r=\frac1x.$
>
> (b) $a_n=\dfrac{\int_1^{e^2}\frac1x\cos(\mu_n\ln x)dx}{\int_1^{e^2}\frac1x\cos^2(\mu_n\ln x)dx}=\dfrac{\sin(2\mu_n)/\mu_n}{1}$, because the norm is $\int_0^2\cos^2\mu_nt\,dt=1+\frac{\sin4\mu_n}{4\mu_n}=1$. With $\sin2\mu_n=\sin\frac{(2n-1)\pi}2=(-1)^{n+1}$:
>
> $\displaystyle \boxed{1=\frac4\pi\sum_{n\ge1}\frac{(-1)^{n+1}}{2n-1}\cos\!\Big(\frac{(2n-1)\pi}4\ln x\Big)}$
>
> ($a_n=1.2732,\ -0.4244,\ 0.2546,\ -0.1819$.)
>
> (c) At $x=1$: $\frac4\pi\big(1-\frac13+\frac15-\cdots\big)=\frac4\pi\cdot\frac\pi4=1$ ✓ (Leibniz). At $x=e^2$ every $\cos(2\mu_n)=0$, so the sum is $0\ne f(e^2)=1$: the basis satisfies $y(e^2)=0$, the data do not, so the series converges slowly (as $1/n$) and drops to $0$ at that end.

## Q10 — A finite Chebyshev expansion (medium)

Using the orthogonality $\int_{-1}^1\frac{T_mT_n}{\sqrt{1-x^2}}dx=\frac\pi2\delta_{mn}$ ($\pi$ for $m=n=0$), expand $f(x)=x^4$ and verify Parseval.

> [!tip]- Hint
> Put $x=\cos\theta$: $a_n=\frac2\pi\int_0^\pi\cos^4\theta\cos n\theta\,d\theta$ ($\frac1\pi$ for $n=0$). Or expand $x^4$ directly using $T_2=2x^2-1$, $T_4=8x^4-8x^2+1$.

> [!success]- Solution
> $T_4+4T_2+3T_0=8x^4-8x^2+1+8x^2-4+3=8x^4$, so
>
> $\displaystyle \boxed{x^4=\tfrac38T_0+\tfrac12T_2+\tfrac18T_4}$
>
> (quadrature gives $a_0=0.375$, $a_2=0.5$, $a_4=0.125$, all other coefficients $<10^{-16}$).
>
> Parseval: $\int\frac{x^8}{\sqrt{1-x^2}}dx=\pi\frac{35}{128}$ and $\pi a_0^2+\frac\pi2(a_2^2+a_4^2)=\pi\big(\frac9{64}+\frac12\cdot\frac{17}{64}\big)=\pi\frac{35}{128}$ ✓.
>
> **Why it terminates:** $x^4$ is a polynomial of degree $4$, so only $T_0,\dots,T_4$ can appear, and parity ($x^4$ even) removes $T_1,T_3$. The same argument applies to any finite polynomial expansion in Legendre or Hermite polynomials.

![[A610-QB-1-bessel-sl.png]]

**Figure.** Left: partial sums of Q4 (one term is already within $11\%$, eight terms indistinguishable). Middle: the roots of $\tan\mu=\mu$ of Q8 as intersections. Right: the finite Chebyshev expansion of Q10.

## Mixed practice

| Skill | Questions |
|---|---|
| Recurrences and derivative identities | Q1, Q6 |
| Closed-form integrals of Bessel functions | Q2 |
| Reduction to Bessel form, half-integer order | Q3 |
| Fourier–Bessel coefficients and Parseval | Q4 |
| Asymptotics of zeros | Q5 |
| S–L form, weights, orthogonality | Q7, A8, A10 |
| Eigenvalues with unusual boundary conditions | Q8, Q9 |
| Expansion in a non-trigonometric basis | Q9, Q10 |

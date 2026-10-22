---
title: Orthogonality and Norm of Legendre Polynomials
tags: [differential-equations, special-functions, legendre, orthogonality]
source: "[[Lecture-20.pdf]] (slides 6–9), [[Lecture-21.pdf]] (slides 1–3)"
---

Related: [[Inner Product Spaces and Orthogonal Functions]] · [[Legendre Polynomials and Rodrigues' Formula]] · [[Generating Function of Legendre Polynomials]] · [[Legendre Series and Fourier-Legendre Expansions]] · [[Special Functions - MOC]]

$$\boxed{\int_{-1}^1P_m(x)P_n(x)\,dx=\begin{cases}0&m\ne n\\[2pt] \dfrac{2}{2n+1}&m=n\end{cases}}\qquad(\text{weight }w=1)$$

So $\{P_n\}$ is orthogonal but not orthonormal; the orthonormal family is $\sqrt{\tfrac{2n+1}2}\,P_n$.

![[DE-N7-orthogonality-norm.png]]
**Figure:** $P_2P_3$ is odd so its integral cancels; $P_2P_4$ is even yet still integrates to 0 (lobes balance); the norms shrink like $\frac1n$.

## Part 1: $m\ne n$ (Sturm–Liouville argument)

Both satisfy the self-adjoint form $\big((1-x^2)P_m'\big)'+m(m+1)P_m=0$ and similarly for $n$. Multiply the first by $P_n$, the second by $P_m$, subtract and integrate over $[-1,1]$:
$$\int_{-1}^1\Big\{P_n\big[(1-x^2)P_m'\big]'-P_m\big[(1-x^2)P_n'\big]'\Big\}dx+\big[m(m+1)-n(n+1)\big]\int_{-1}^1P_mP_n\,dx=0$$
Integrating the first integral by parts: boundary terms contain $(1-x^2)$, which vanishes at $\pm1$, and the remaining integrand is $P_n'(1-x^2)P_m'-P_m'(1-x^2)P_n'\equiv0$. So the first integral is 0. For $m\ne n$ the bracket $m(m+1)-n(n+1)\ne0$, hence $\int P_mP_n=0$. The ODE has *no* boundary condition at $\pm1$ — the factor $1-x^2$ does all the work (a *singular* Sturm–Liouville problem).

## Part 2: $m=n$ — Method 1 (Rodrigues)

$$\int_{-1}^1P_n^2dx=\frac1{2^nn!}\int_{-1}^1P_n\,D^n(x^2-1)^n\,dx$$
Integrate by parts $n$ times; every boundary term vanishes because $D^j(x^2-1)^n=0$ at $\pm1$ for $j<n$:
$$=\frac{(-1)^n}{2^nn!}\int_{-1}^1P_n^{(n)}(x)(x^2-1)^ndx,\qquad P_n^{(n)}=\frac{(2n)!}{2^nn!}$$
$$=\frac{(2n)!}{2^{2n}(n!)^2}\int_{-1}^1(1-x^2)^ndx=\frac{2(2n)!}{2^{2n}(n!)^2}\int_0^{\pi/2}\cos^{2n+1}\theta\,d\theta$$
($x=\sin\theta$) and Wallis' reduction $\int_0^{\pi/2}\cos^{2n+1}\theta\,d\theta=\dfrac{2n(2n-2)\cdots2}{(2n+1)(2n-1)\cdots3}$ gives $\dfrac2{2n+1}$. (Equivalently the Beta function $\int_0^{\pi/2}\sin^p\cos^q=\frac{\Gamma(\frac{p+1}2)\Gamma(\frac{q+1}2)}{2\Gamma(\frac{p+q+2}2)}$ — see [[Gamma Function]].)

## Part 2: $m=n$ — Method 2 (generating function)

Square $G=\sum P_nt^n$ and integrate; cross terms vanish by Part 1:
$$\int_{-1}^1\frac{dx}{1-2xt+t^2}=\sum_{n=0}^\infty t^{2n}\int_{-1}^1P_n^2dx$$
LHS: $\dfrac1t\ln\dfrac{1+t}{1-t}=\dfrac2t\Big[t+\dfrac{t^3}3+\dfrac{t^5}5+\cdots\Big]=\sum\dfrac{2t^{2n}}{2n+1}$. Compare coefficients of $t^{2n}$ ⇒ $\int P_n^2=\dfrac2{2n+1}$. ∎

## Worked checks
- $\int P_2^2=\int\tfrac14(3x^2-1)^2=\tfrac25$ ✓ ($=\frac2{2\cdot2+1}$).
- $\int_{-1}^1P_n\,dx=0$ for $n\ge1$ (write $P_n\cdot P_0$), and $=2$ for $n=0$.
- Verified symbolically for all $m,n\le6$ that the Gram matrix is $\operatorname{diag}\big(\tfrac{2}{2n+1}\big)$.

## Problems using this
- [[Assignment 5 - Legendre Polynomials and Functions - Solutions#0.5 Orthogonality and norm|Assignment 5, §0.5]] and the integrals in [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q7|Q7]].
- Series coefficients $c_n=\frac{2n+1}2\int fP_n$: [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q3|Q3]], [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q5|Q5]], [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q6|Q6]].

## Next
[[Legendre Series and Fourier-Legendre Expansions]]

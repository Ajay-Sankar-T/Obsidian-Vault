---
title: Legendre Series and Fourier-Legendre Expansions
tags: [differential-equations, special-functions, legendre, fourier-legendre, approximation]
source: "[[Lecture-21.pdf]] (slides 4–18)"
---

Related: [[Orthogonality and Norm of Legendre Polynomials]] · [[Inner Product Spaces and Orthogonal Functions]] · [[Legendre Polynomials and Rodrigues' Formula]] · [[Special Functions - MOC]]

## 1. Polynomials: an exact, finite expansion

$\{P_n\}$ (degree exactly $n$) is another basis of the polynomial space, so any polynomial of degree $m$ is a finite combination of $P_0,\dots,P_m$ (a change of basis). The inverse relations: $x^2=\tfrac13P_0+\tfrac23P_2$, $x^3=\tfrac35P_1+\tfrac25P_3$, $x^4=\tfrac15P_0+\tfrac47P_2+\tfrac8{35}P_4$, so

$$b_0+b_1x+b_2x^2+b_3x^3=\Big(b_0+\tfrac{b_2}3\Big)P_0+\Big(b_1+\tfrac{3b_3}5\Big)P_1+\tfrac{2b_2}3P_2+\tfrac{2b_3}5P_3$$

| $f(x)$ | Legendre form |
|---|---|
| $x^2$ | $\tfrac13P_0+\tfrac23P_2$ |
| $2x^3-x+1$ | $P_0+\tfrac15P_1+\tfrac45P_3$ |
| $x^4+2x^3+2x^2-x-3$ | $-\tfrac{32}{15}P_0+\tfrac15P_1+\tfrac{40}{21}P_2+\tfrac45P_3+\tfrac8{35}P_4$ |

(all verified symbolically; $a_n=0$ for $n>\deg f$).

## 2. The general Legendre series

If $f(x)=\sum_{n\ge0}a_nP_n(x)$ on $(-1,1)$, multiply by $P_m$ and integrate term by term; orthogonality leaves only $a_m\frac2{2m+1}$:
$$\boxed{a_n=\frac{2n+1}2\int_{-1}^1f(x)P_n(x)\,dx}$$
Parity shortcut: $f$ even ⇒ $a_{odd}=0$; $f$ odd ⇒ $a_{even}=0$ (and then $a_n=(2n+1)\int_0^1fP_n$).

![[DE-N8-legendre-series.png]]
**Figure:** Partial sums for three functions with a kink or jump, and their coefficients. $|x|$ converges quickly; the step shows Gibbs-type overshoot near the jump and converges to the midpoint $0$ at $x=0$.

## 3. Examples

**(a) $f=|x|$:** $a_0=\tfrac12,\ a_2=\tfrac58,\ a_4=-\tfrac3{16}$: $\ |x|\sim\tfrac12P_0+\tfrac58P_2-\tfrac3{16}P_4+\cdots$ (continuous ⇒ converges to $|x|$ everywhere).

**(b) $f=\operatorname{sign}x$:** $a_1=\tfrac32,\ a_3=-\tfrac78,\ a_5=\tfrac{11}{16}$: $\ f\sim\tfrac32P_1-\tfrac78P_3+\tfrac{11}{16}P_5-\cdots$; at $x=0$ it converges to $\tfrac12[f(0^+)+f(0^-)]=0$.

**(c) $f=x$ on $[0,1]$, $0$ on $[-1,0]$.**
$$a_0=\tfrac14,\quad a_1=\tfrac12,\quad a_2=\tfrac5{16},\quad a_3=0,\quad a_4=-\tfrac3{32},\ \dots$$
Check: $f=\tfrac12(x+|x|)$, so the series is $\tfrac12P_1+\tfrac12\big(\tfrac12P_0+\tfrac58P_2-\tfrac3{16}P_4+\cdots\big)$.

> [!warning] Slide error (Lecture 21, slide 9)
> The slide lists $a_2=\tfrac58$ and $a_3=-\tfrac7{16}$ for this $f$. Those are wrong: $a_2=\tfrac52\int_0^1x\cdot\tfrac{3x^2-1}2dx=\tfrac5{16}$, and $a_3=\tfrac72\int_0^1x\cdot\tfrac{5x^3-3x}2dx=0$. (The printed $\tfrac58$ is the $a_2$ of $|x|$, which is twice the even part of this $f$; the printed $a_0,a_1$ are right.) Verified by exact integration.

## 4. Convergence

- **In the $L^2$ norm** for every $f\in L^2([-1,1])$: $\big\|f-\sum_{n\le N}a_nP_n\big\|_2\to0$ (because $\{P_n\}$ is a maximal orthogonal set).
- **Pointwise** (Legendre expansion theorem): if $f$ and $f'$ have at most finitely many jump discontinuities, the series converges to $\tfrac12[f(x^+)+f(x^-)]$ at every $x\in(-1,1)$, to $f(-1^+)$ at $-1$ and $f(1^-)$ at $1$. Same as the classical Fourier theorem.

## 5. Least-squares property

**Theorem.** Among all polynomials $p$ of degree $\le n$, the one minimising $I=\int_{-1}^1[f-p]^2dx$ is the truncation $\sum_{k\le n}a_kP_k$.

**Proof.** With $p=\sum b_kP_k$ and orthogonality,
$$I=\int f^2+\sum_{k=0}^n\frac2{2k+1}(b_k-a_k)^2-\sum_{k=0}^n\frac2{2k+1}a_k^2,$$
minimised exactly at $b_k=a_k$. ∎ In particular the *Taylor* truncation is **not** the best polynomial fit.

![[DE-N8b-least-squares.png]]
**Figure:** For $e^x$ the Legendre cubic has $L^2$ error $2.2\times10^{-5}$ (squared) against $4.2\times10^{-4}$ for the Taylor cubic, and the Legendre error spreads evenly over $[-1,1]$ while Taylor's piles up at the ends.

By Bessel's inequality/Parseval the remaining error after $N$ terms is $\int f^2-\sum_{k\le N}\frac2{2k+1}a_k^2$.

## Problems using this
- Legendre series of $|x|$, a step function, $e^x$, $1-|x|$, $\cos\pi x$, and a quartic: [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q3|Assignment 5, Q3]].
- Express polynomials in $P_n$ and $x^n=\sum a_mP_m$: [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q5|Q5]], [[Assignment 5 - Legendre Polynomials and Functions - Solutions#Q6|Q6]].

---
title: Wave Equation on a Finite Interval
tags: [differential-equations, pdes, concept, wave-equation, vibrating-string, fourier-series]
source: "[[Lecture-34.pdf]], [[A9-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Separation of Variables]] · [[D'Alembert's Solution of the Wave Equation]] · [[Sturm-Liouville Problems]] · solved in [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]] Q4–Q9

## What it is
A string of length $L$ with tension $T_0$ and density $\rho$ has small transverse displacement $u(x,t)$ obeying
$$u_{tt}=c^2u_{xx},\quad c^2=T_0/\rho,\qquad 0<x<L,\ t>0,$$
$$u(0,t)=u(L,t)=0,\qquad u(x,0)=f(x),\quad u_t(x,0)=g(x).$$

## Solution (fixed ends)
Separation $u=X(x)T(t)$ gives $X''+p^2X=0$ with $X(0)=X(L)=0$, so $X_n=\sin\frac{n\pi x}L$, $p_n=\frac{n\pi}L$, and $T''+c^2p_n^2T=0$. Superposing,
$$\boxed{u=\sum_{n=1}^\infty\Big(A_n\cos\tfrac{n\pi ct}L+B_n\sin\tfrac{n\pi ct}L\Big)\sin\tfrac{n\pi x}L}$$
$$A_n=\frac2L\int_0^Lf\sin\tfrac{n\pi x}L\,dx,\qquad B_n=\frac{2}{n\pi c}\int_0^Lg\sin\tfrac{n\pi x}L\,dx.$$
(Put $t=0$ in $u$ and in $u_t$: Fourier sine series of $f$ and of $g$.) If $g=0$ only the cosines remain, if $f=0$ only the sines.

![[DE-PDE-string.png]]
**Figure:** left, the first four modes; right, a string plucked at the midpoint ($c_n=\frac{8h}{n^2\pi^2}\sin\frac{n\pi}2$) at several times: the triangle splits into two half-height pulses that travel and reflect with a sign change.

## Why it works
Each mode $\sin\frac{n\pi x}L$ oscillates at its own frequency $\omega_n=\frac{n\pi c}L$ (a harmonic series: $\omega_n=n\omega_1$). The string is a set of independent oscillators; the initial shape and velocity decide how much of each mode is excited. The $n$-th mode has $n-1$ interior nodes, and $\omega_n$ is the continuous analogue of the [[The Universal Second-Order Linear System|undamped natural frequency]].

## Other ends
| Ends | Spatial part | Time part |
|---|---|---|
| free–free, $u_x=0$ at both | $\cos\frac{n\pi x}L$, $n\ge0$ | $n=0$: $A_0+B_0t$ (uniform drift); $n\ge1$: oscillates |
| fixed–free ($u(0)=0$, $u_x(L)=0$) | $\sin\frac{(2n-1)\pi x}{2L}$ | frequencies $\frac{(2n-1)\pi c}{2L}$ (odd harmonics only, a clarinet-like spectrum) |

## Method
1. State $c$, $L$ and the ends; list $X_n$, $p_n$ (table above or [[Separation of Variables]]).
2. $u=\sum(A_n\cos p_nct+B_n\sin p_nct)X_n$.
3. $A_n$ from $f$, $B_n$ from $g/(p_nc)$ by orthogonality (sine, cosine or mixed series).
4. Simplify with $\sin\frac{n\pi}2$, $(-1)^n$; note which modes vanish by symmetry.

**Shortcut:** if $f$ or $g$ is already a finite sum of eigenfunctions, read the coefficients off. E.g. $g=5\cos\frac{2\pi x}L\sin\frac{3\pi x}L=\frac52\big[\sin\frac{5\pi x}L+\sin\frac{\pi x}L\big]$ means only $n=1$ and $n=5$ are excited.

**Symmetry:** a shape antisymmetric about the midpoint (e.g. trisection points pulled to opposite sides) contains only even modes, so the midpoint never moves.

> [!warning] Traps
> - Forgetting the factor $\frac1{n\pi c}$ in $B_n$ (the sine coefficients of $g$ are of $u_t$, not of $u$).
> - Using the wrong eigenfunctions for non-fixed ends: the table, not $\sin\frac{n\pi x}L$ always.
> - Expecting the series to be smooth: for non-smooth data the series solves the PDE only in a weak sense (corners propagate along characteristics).

## Cross-domain links
- [[Resonance and Buckling - Instability as an Eigenvalue Problem]] — the string's frequencies $\omega_n$ are eigenvalues; driving at $\omega_n$ is resonance, exactly as for the RLC circuit in [[Frequency Response and Resonance Curves]].
- [[Eigenvalues, Rotation and Diagonalization Everywhere]] — normal modes of a coupled spring–mass chain become $\sin\frac{n\pi x}L$ as the number of masses $\to\infty$.

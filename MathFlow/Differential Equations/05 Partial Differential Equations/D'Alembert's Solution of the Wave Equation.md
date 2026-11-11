---
title: D'Alembert's Solution of the Wave Equation
tags: [differential-equations, pdes, concept, wave-equation, dalembert, characteristics]
source: "[[Lecture-33.pdf]], [[Lecture-34.pdf]], [[A9-2026.pdf]]"
---

Related: [[PDEs - MOC]] · [[Canonical Forms of Second Order PDEs]] · [[Wave Equation on a Finite Interval]] · [[Classification of Second Order PDEs]] · solved in [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]] Q1, Q2

## What it is
For the one-dimensional wave equation on the whole line
$$u_{tt}=c^2u_{xx},\qquad x\in\mathbb R,\ t>0,\qquad u(x,0)=f(x),\ u_t(x,0)=g(x),$$
**d'Alembert's formula** gives the solution in closed form:
$$\boxed{u(x,t)=\frac{f(x+ct)+f(x-ct)}{2}+\frac1{2c}\int_{x-ct}^{x+ct}g(s)\,ds}$$

## Derivation
The characteristic equation $dx^2-c^2dt^2=0$ gives $\xi=x+ct$, $\eta=x-ct$ ([[Canonical Forms of Second Order PDEs]]). Then $u_{tt}-c^2u_{xx}=-4c^2u_{\xi\eta}=0$, so
$$u=F(x+ct)+G(x-ct):$$
a wave moving left plus a wave moving right, each rigid, at speed $c$. The initial data give $F+G=f$ and $c(F'-G')=g$; integrating the second, $F-G=\frac1c\int g$. Solving for $F$ and $G$ and adding gives the formula.

## What it says
- **Travelling waves.** $f(x-ct)$ is the profile $f$ shifted right by $ct$.
- **Domain of dependence.** $u(x_0,t_0)$ depends only on $f$ at the two points $x_0\pm ct_0$ and on $g$ over the interval between them; changes elsewhere cannot reach $(x_0,t_0)$ (finite speed $c$).
- **Range of influence.** Data at $x_0$ influence only $|x-x_0|\le ct$.
- **Discontinuities travel along characteristics** and are not smoothed (contrast the heat equation).

![[DE-PDE-dalembert.png]]

**Example.** $u(x,0)=\sin x$, $u_t(x,0)=\cos x$: $u=\sin x\cos ct+\frac1c\cos x\sin ct$. With $f=x$, $g=4cx$: $u=x(1+4ct)$. With $f=x(1-x)$, $g=\sin\pi x$: $u=x(1-x)-c^2t^2+\frac{1}{\pi c}\sin\pi x\sin\pi ct$.

## Half-line $x>0$: reflection
For $x>0$ with a boundary condition at $x=0$, **extend the data to the whole line** and apply the formula:

| Boundary condition at $x=0$ | Extension of $f,g$ | Effect on a pulse |
|---|---|---|
| $u(0,t)=0$ (fixed end) | **odd**: $f(-x)=-f(x)$, $g(-x)=-g(x)$ | reflects with the sign **flipped** |
| $u_x(0,t)=0$ (free end) | **even**: $f(-x)=f(x)$, $g(-x)=g(x)$ | reflects with the **same** sign |

Then for $x>ct$ the plain formula holds; for $0<x<ct$ one of the arguments $x-ct$ is negative and the extension is used. By symmetry $u(0,t)=0$ (odd) or $u_x(0,t)=0$ (even) holds automatically.

**Compatibility.** For a fixed end, $f(0)=0$ and $g(0)=0$ are needed for a continuous solution. If $f(0)\ne0$, the odd extension jumps at $0$ and the solution has a **jump along $x=ct$**. For $f=e^{-x}$, $g=e^{x}$ (so $f(0)=g(0)=1$), the solution is
$$u=\begin{cases}e^{-x}\cosh ct+\frac1ce^x\sinh ct,&x\ge ct\\[2pt]\tfrac12\big(e^{-x-ct}-e^{x-ct}\big)+\frac1{2c}\big(e^{x+ct}-e^{ct-x}\big),&0<x<ct\end{cases}$$
with a jump of size 1 across $x=ct$ (a weak solution).

> [!warning] Traps
> - The formula is for **time-independent coefficient, infinite line**. On a finite interval reflections never stop: use [[Wave Equation on a Finite Interval]].
> - Forgetting the $\frac1{2c}$, or integrating $g$ over $[x-t,x+t]$ instead of $[x-ct,x+ct]$.
> - Odd vs even: fixed end $\Rightarrow$ odd, free end $\Rightarrow$ even.

## Cross-domain links
- [[The Universal Second-Order Linear System]] — a string is a chain of coupled oscillators; d'Alembert's solution is the continuum limit, in which the characteristic speed $c=\sqrt{T/\rho}$ replaces the natural frequency.
- Transmission lines obey the same equation ($v_{tt}=c^2v_{xx}$ with $v$ the voltage). The odd/even rule is the reflection coefficient $\Gamma=(Z_L-Z_0)/(Z_L+Z_0)$: a short circuit ($Z_L=0$, voltage forced to zero, like a fixed end) gives $\Gamma=-1$ (odd extension), an open circuit ($Z_L\to\infty$, like a free end) gives $\Gamma=+1$ (even extension). Compare [[Gears, Transformers and Reflected Impedance]] for impedance matching.

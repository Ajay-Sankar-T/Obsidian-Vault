Related: [[Abel's Formula]] · [[Existence and Uniqueness (Picard-Lindelof Theorem)]] (first-order analogue)

## Existence and Uniqueness Theorem

> Consider $y'' + P(x)y' + Q(x)y = R(x)$, $x \in I$, $y(x_0)=y_0$, $y'(x_0)=y_0'$. If $P,Q,R$ are continuous on an interval $I$ containing $x_0$, then this IVP has a **unique** solution $y(x)$ valid on all of $I$. (Proof not required.)

This underlies all subsequent theorems about the structure of solutions.

## Solution Space is a Vector Space

The set $S$ of all solutions of $L[y] = y''+P(x)y'+Q(x)y=0$ on $I$ forms a **vector space over $\mathbb{R}$**, under usual addition and scalar multiplication — this follows from the superposition principle and $L[0]=0$.

- If $P,Q$ are continuous on $I$, then $\dim(S) = 2$.
- Any two linearly independent solutions $y_1,y_2$ form a **basis** of $S$, called a **fundamental set of solutions**.

## Worked Example: largest interval of a unique solution

Find the largest interval guaranteeing a unique solution of $(x-1)y''+3y'+(\tan x)y=e^x$, $y(2)=1$, $y'(2)=0$.

Standard form: $y'' + \dfrac{3y'}{x-1} + \dfrac{(\tan x)y}{x-1} = \dfrac{e^x}{x-1}$.

Coefficients undefined at $x=1$ and at $x = \tfrac{\pi}{2}+k\pi$. Nearest singularities to $x_0=2$: $x=\tfrac{\pi}{2}\approx1.57$ (left), $x=\tfrac{3\pi}{2}\approx4.71$ (right).

**Largest interval** $= \left(\dfrac{\pi}{2}, \dfrac{3\pi}{2}\right)$.

## Fundamental Set of Solutions

A pair $\{y_1,y_2\}$ of solutions of the homogeneous equation is a **fundamental set** if $W(y_1,y_2)(x)\ne0$ for some (equivalently every) $x\in I$.

Existence of a fundamental set is guaranteed by the existence-uniqueness theorem: take $y_1$ solving $y(x_0)=1, y'(x_0)=0$, and $y_2$ solving $y(x_0)=0, y'(x_0)=1$. Then $W(y_1,y_2)(x_0)=1\ne0$, so $\{y_1,y_2\}$ is fundamental — this proves existence of a basis for $S$.

**Example:** Construct a fundamental set for $y''+y=0$ at $x_0=0$.
- $y_1$: $y_1(0)=1,y_1'(0)=0 \Rightarrow y_1=\cos x$
- $y_2$: $y_2(0)=0,y_2'(0)=1 \Rightarrow y_2=\sin x$
- $W(y_1,y_2)(0) = 1\ne0$, so $\{\cos x,\sin x\}$ is a fundamental set: $y = c_1\cos x + c_2\sin x$.

---
Next: [[General Solution Structure Theorem]]

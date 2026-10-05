Related: [[Standard Form and Homogeneity]]

Consider the 2nd order DE $F(x,y,y',y'')=0$ over $I$. $y = \phi(x)$ is a **solution** on $I$ if:
- $\phi$ is defined on $I$
- $\phi$ is twice differentiable on $I$
- the ODE becomes an identity when $y, y', y''$ are replaced by $\phi, \phi', \phi''$.

**Example:** $y = \cos x$ solves $y''+y=0$: $y'=-\sin x$, $y''=-\cos x$, LHS $= -\cos x + \cos x = 0 =$ RHS.

Similarly $y=\sin x$ is a solution. In general, $y = C_1y_1 + C_2y_2$ is a solution of $y''+y=0$ if $y_1=\cos x$, $y_2=\sin x$, $C_1,C_2$ arbitrary constants.

## Superposition Principle

> **Theorem.** For a homogeneous linear ODE $y'' + P(x)y' + Q(x)y = 0$, $x \in I$ (2), any linear combination of two solutions on an open interval $I$ is again a solution of (2) on $I$.

- $V = \{y \mid y'' + P(x)y' + Q(x)y = 0\}$ is a subspace of $\mathcal{D}^2(I)$.
- $V_1 = \{y \mid y'' + P(x)y' + Q(x)y = R(x)\}$ is **NOT** a subspace when $R(x) \not\equiv 0$.

**Example:** $y_1 = 1+\cos x$, $y_2 = 1+\sin x$ are solutions of $y''+y=1$. But $y_1+y_2 = 2+\cos x+\sin x$ is **not** a solution: $y''+y = (-\cos x-\sin x)+(2+\cos x+\sin x) = 2 \ne 1$. Superposition fails for non-homogeneous equations.

## Nonlinear ODE counterexample

Consider the nonlinear ODE $y''y - xy' = 0$.
- $y_1 = x^2$ is a solution: $(x^2)''x^2 - x(x^2)' = 2x^2-2x^2=0$.
- $y_2 = 1$ satisfies the DE.
- But $y_1+y_2 = x^2+1$ is **not** a solution: $(x^2+1)''(x^2+1)-x(x^2+1)' = 2(x^2+1)-2x^2 = 2 \ne 0$.
- A constant multiple of $x^2$, e.g. $-x^2$, is also **not** a solution.

This shows superposition is a property special to *linear homogeneous* equations — it fails for nonlinear equations even without a forcing term.

---
Next: [[Linear Independence and the Wronskian]]

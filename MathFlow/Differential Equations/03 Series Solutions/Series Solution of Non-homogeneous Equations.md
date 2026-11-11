Related: [[Series Solutions - Homogeneous Examples]] · [[General Solution Structure Theorem]] (2nd Order DE) · [[Undetermined Coefficients]] (2nd Order DE)

The power series method extends directly to non-homogeneous equations, following the same $y=y_c+y_p$ structure as [[General Solution Structure Theorem]] — except here $y_p$ is also built as a power series, and its coefficients are driven by the power-series expansion of the right-hand side.

## Example: $y''+xy'+y=x$ about $x=0$

By [[Series Solutions - Homogeneous Examples]] Example 4, the homogeneous equation $y''+xy'+y=0$ already gives $y_c$. Taking $y_p$ as the same type of series, the LHS is
$$\sum_{n=0}^\infty \left[(n+2)(n+1)a_{n+2}+(n+1)a_n\right]x^n.$$
Since the RHS is $x$, its power-series coefficients are $b_0=0,\ b_1=1,\ b_n=0\ (n\ge2)$. Consequently
$$(n+2)(n+1)a_{n+2}+(n+1)a_n=b_n \implies a_{n+2}=\frac{b_n-(n+1)a_n}{(n+2)(n+1)}.$$

- $n=0$: $2a_2+a_0=0 \Rightarrow a_2=-\dfrac{a_0}{2}$
- $n=1$: $6a_3+2a_1=1 \Rightarrow a_3=\dfrac16-\dfrac{a_1}{3}$
- $n\ge2$: $a_{n+2}=-\dfrac{a_n}{n+2}$ (same as the homogeneous recurrence)

Taking $a_0=a_1=0$ isolates a particular solution:
$$y_p = \frac{x^3}{6}-\frac{x^5}{30}+\frac{x^7}{210}-\frac{x^9}{1890}+\cdots$$

**General solution:** $y = y_c+y_p$, where $y_c$ is the homogeneous series from [[Series Solutions - Homogeneous Examples]].

**Key idea:** whenever the RHS itself has a (finite or simple) power-series expansion, absorb its coefficients $b_n$ directly into the recurrence relation for $a_{n+2}$ — no separate technique (like [[Undetermined Coefficients]] or [[Variation of Parameters]]) is needed, since the series method handles arbitrary analytic forcing terms automatically.

---
Related: [[Legendre's Equation]] · [[Hermite's Equation]] · [[Airy's Equation]]

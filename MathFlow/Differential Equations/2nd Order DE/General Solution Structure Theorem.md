Related: [[Existence, Uniqueness, and Fundamental Sets]] · [[Reduction of Order]]

> **Theorem.** If $\{y_1,y_2\}$ is a fundamental set of solutions of $L[y]=0$ on $I$, then every solution $y$ of $L[y]=0$ on $I$ can be written as
> $$y(x) = c_1y_1(x)+c_2y_2(x)$$
> for unique constants $c_1,c_2$.

This expression is the **general solution** (or complementary function) $y_c$ — it represents *all* solutions of the homogeneous DE.

A **particular solution** $y_p$ of $L[y]=R(x)$ is any single function satisfying it (no arbitrary constants).

> **Structure Theorem.** If $y_p$ is a particular solution of $L[y]=R(x)$, and $y_c=c_1y_1+c_2y_2$ is the general solution of the associated homogeneous equation $L[y]=0$, then the general solution of $L[y]=R(x)$ is
> $$y(x) = y_c(x)+y_p(x) = c_1y_1(x)+c_2y_2(x)+y_p(x).$$

## Proof Sketch

If $y$ is any solution of $L[y]=R(x)$, define $u=y-y_p$. Since $L[y_p]=R(x)$:
$$L[u] = L[y]-L[y_p] = R(x)-R(x) = 0.$$
So $u$ solves the homogeneous equation, hence $u=c_1y_1+c_2y_2$. Therefore $y=y_p+c_1y_1+c_2y_2$, proving every solution has this form.

Conversely, $L[y_p+c_1y_1+c_2y_2] = R(x)+0+0 = R(x)$, so it is indeed a solution.

This decomposition ($y_c+y_p$) is fundamental to solving non-homogeneous equations — see [[Undetermined Coefficients]] and [[Variation of Parameters]] for methods to find $y_p$.

## Summary of Key Theorems

- **Existence-Uniqueness:** IVP has a unique solution on all of $I$ when $P,Q,R$ continuous.
- **Superposition:** linear combinations of homogeneous solutions are solutions.
- Solution space $S$ of $L[y]=0$ is a 2-dimensional vector space.
- **Wronskian test + Abel's formula:** determine independence via a single point check.
- General solution of $L[y]=0$: $y_c=c_1y_1+c_2y_2$ (fundamental set).
- General solution of $L[y]=R(x)$: $y=y_c+y_p$.

---
Next: [[Reduction of Order]]

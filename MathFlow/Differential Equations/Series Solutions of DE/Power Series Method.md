Related: [[Ordinary and Singular Points]] · [[Series Solutions - Homogeneous Examples]]

## Steps to Find a Series Solution

1. Assume $y=\sum_{n=0}^\infty a_nx^n$ about the ordinary point $x_0=0$.
2. Differentiate term by term to get $y'$ and $y''$.
3. Substitute $y,y',y''$ into the given ODE.
4. Shift indices so that all series have the same power of $x$.
5. Equate the coefficient of each power of $x$ to zero.
6. Obtain a **recurrence relation** connecting the $a_n$'s.
7. Use the recurrence relation to express all coefficients in terms of $a_0,a_1$.
8. Write the two linearly independent series solutions.

## Setting Up the Substitution

If $y=\sum_{n=0}^\infty a_nx^n$, then
$$y' = \sum_{n=1}^{\infty} na_nx^{n-1}, \qquad y'' = \sum_{n=2}^{\infty} n(n-1)a_nx^{n-2}.$$
Re-indexing $y''$ with $n\to n+2$:
$$y'' = \sum_{n=0}^{\infty} (n+2)(n+1)a_{n+2}x^n.$$
This shifted form is essential before comparing coefficients. The resulting recurrence relation typically connects $a_{n+2}$ with $a_n$ (or $a_{n-1}$). Solving it gives all coefficients in terms of $a_0$ and $a_1$.

**Note on index shifting** (used repeatedly, e.g. for $xy'$, $(t+1)y'$, etc.): a series $\sum_{n=n_0}^\infty c\cdot a_{n+k}x^{n+m}$ is re-indexed by setting the new index equal to the current power of $x$, so that every series in the sum is expressed with the same power $x^k$ before coefficients are compared. Getting the starting index right (some series only start contributing from $k=1$, requiring $k=0$ to be treated as a separate case) is the most common source of error — see the $x_0\ne0$ examples in [[Series Solutions About x0 not equal to 0]].

---
Next: [[Series Solutions - Homogeneous Examples]]

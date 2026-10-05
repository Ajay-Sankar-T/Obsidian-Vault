Related: [[Power Series Method]] · [[Ordinary and Singular Points]] · [[Hermite's Equation]] · [[Airy's Equation]]

$$(1-x^2)y''-2xy'+n(n+1)y=0.$$
Here $P(x)=\dfrac{-2x}{1-x^2}$, $Q(x)=\dfrac{n(n+1)}{1-x^2}$ — both analytic at $x=0$, so $x=0$ is an **ordinary point**. Singular points occur at $x=\pm1$ (see [[Regular and Irregular Singular Points]] — these turn out to be regular).

Assume $y=\sum_{k=0}^\infty a_kx^k$ and substitute. After shifting indices, the recurrence relation is
$$a_{k+2} = \frac{k(k+1)-n(n+1)}{(k+1)(k+2)}\,a_k.$$

This links only **alternate** coefficients:
- $a_0=1, a_1=0$ gives an even series solution $y_1(x)$.
- $a_0=0, a_1=1$ gives an odd series solution $y_2(x)$.

General solution: $y = a_0y_1(x)+a_1y_2(x)$.

If $n$ is a non-negative integer, one of the two series **terminates** (since the factor $k(k+1)-n(n+1)$ vanishes once $k=n$), giving the **Legendre polynomial** $P_n(x)$ as a solution — a polynomial of degree $n$.

Series converges for $|x|<1$ (radius of convergence $=1$, matching the distance to the nearest singular point $x=\pm1$, consistent with [[Radius of Convergence of Series Solutions]]).

---
Related: [[Series Solutions - Homogeneous Examples]]

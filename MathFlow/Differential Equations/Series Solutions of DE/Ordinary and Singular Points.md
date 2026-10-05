Related: [[Series Solutions - MOC]] · [[Standard Form and Homogeneity]] (2nd Order DE)

## Standard Form

General second order linear homogeneous ODE:
$$a_0(x)y''+a_1(x)y'+a_2(x)y=0.$$
Dividing by $a_0(x)$, the **standard form** is
$$y''+P(x)y'+Q(x)y=0, \qquad P(x)=\frac{a_1(x)}{a_0(x)}, \quad Q(x)=\frac{a_2(x)}{a_0(x)}.$$
The nature of the solution near $x=x_0$ depends on the behaviour of $P(x),Q(x)$ there — this motivates classifying $x_0$ as **ordinary** or **singular**.

A point $x_0$ is an **analytic point** of $f$ if $f$ has a Taylor series expansion around $x_0$.

## Ordinary Point

> $x=x_0$ is an **ordinary point** of $y''+P(x)y'+Q(x)y=0$ if both $P(x)$ and $Q(x)$ are analytic at $x_0$ — i.e. expandable in a power series about $x_0$ with nonzero radius of convergence (equivalently, no singularities/poles at $x_0$).

This requires $a_0(x_0)\ne0$. **Example:** in $y''+xy'+y=0$, every point is ordinary.

At an ordinary point, seek a solution as an ordinary power series:
$$y(x) = \sum_{n=0}^{\infty} a_n(x-x_0)^n.$$

## Singular Point

A point $x_0$ is **singular** if it is not ordinary — at least one of $P(x),Q(x)$ fails to be analytic there. Singular points are further classified:

- **Regular singular point:** $P(x),Q(x)$ are not analytic at $x_0$, but $(x-x_0)P(x)$ and $(x-x_0)^2Q(x)$ **are** both analytic at $x_0$.
- **Irregular singular point:** otherwise.

**Example:** $x^2y''+xy'+(x^2-n^2)y=0$ (Bessel's equation) has a regular singular point at $x=0$. Regular singular points are treated using the **Frobenius method** — see [[Regular and Irregular Singular Points]] and [[Frobenius Theorem]].

## Existence Theorem

> **Theorem.** If $x_0$ is an ordinary point of $y''+P(x)y'+Q(x)y=0$, the general solution can be written as $y=\sum_{n=0}^\infty a_n(x-x_0)^n$. This series converges at least for $|x-x_0|<R$, where $R$ is the distance from $x_0$ to the nearest singular point.

The two arbitrary constants $a_0,a_1$ correspond to two linearly independent solutions (recall [[Linear Independence and the Wronskian]]). For simplicity, examples typically take the ordinary point $x_0=0$.

---
Next: [[Power Series Method]]

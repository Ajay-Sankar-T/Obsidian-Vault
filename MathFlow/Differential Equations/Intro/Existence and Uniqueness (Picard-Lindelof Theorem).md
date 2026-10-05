Related: [[Particular Solution and IVP]], [[Isoclines]]

Consider the initial value problem (IVP):
$$\frac{dy}{dx} = f(x,y), \qquad y(x_0) = y_0$$

Two natural questions arise:
1. **Existence** — Does a solution exist at all?
2. **Uniqueness** — If a solution exists, is it the only one?

## 1. Existence

Let $f(x,y)$ be defined and continuous on the rectangle
$$R = \{(x,y) : |x - x_0| \le a,\ |y - y_0| \le b\}.$$
Then, the IVP has solution(s).

## 2. Uniqueness

Suppose further that $f$ satisfies a **Lipschitz condition** in $y$ on $R$, i.e. there exists a constant $L > 0$ such that
$$|f(x, y_1) - f(x, y_2)| \le L\,|y_1 - y_2| \quad \text{for all } (x,y_1), (x,y_2) \in R.$$

Then there exists a **unique** solution $y(x)$ of the IVP on the interval $|x - x_0| \le h$, where
$$h = \min\left(a, \frac{b}{M}\right), \qquad M = \max_{(x,y)\in R} |f(x,y)|.$$

Note that if $\frac{\partial f}{\partial y}$ exists and is continuous (hence bounded) on $R$, then $f$ automatically satisfies a Lipschitz condition on $R$ (a **stronger condition** than the Lipschitz condition, and easier to check).

## Examples

**Unique solution:** Consider the IVP $y' = y$, $y(0) = 1$. Here $f(x,y) = y$ is continuous everywhere, and $\frac{\partial f}{\partial y} = 1$ is continuous, so the Lipschitz condition holds. The P-L theorem guarantees a unique solution: $y(x) = e^x$.

**Failure of uniqueness:** Consider another IVP: $y' = y^{1/3}$, $y(0) = 0$. Here $f(x,y) = y^{1/3}$ is continuous, so a solution exists. However,
$$\frac{\partial f}{\partial y} = \frac{1}{3} y^{-2/3} \to \infty \quad \text{as } y \to 0,$$
so the Lipschitz condition **fails** near $y = 0$. Consequently this IVP has infinitely many solutions, including $y(x) = 0$ and $y(x) = \left(\frac{2x}{3}\right)^{3/2}$.

This demonstrates that continuity alone is insufficient for uniqueness; the Lipschitz condition is essential.

---
Next: [[Exact Differential Equations]]

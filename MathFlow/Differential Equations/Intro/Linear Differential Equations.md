Related: [[Integrating Factors]], [[Exact Differential Equations]], [[Bernoulli Differential Equations]]

▶ A **first-order linear differential equation** is an equation of the form (known as **Lagrange form**)
$$\frac{dy}{dx} + P(x)y = Q(x), \quad x \in I, \tag{6}$$
where $P(x)$ and $Q(x)$ are continuous functions on an interval $I$.

▶ If $Q(x) = 0$, the equation is called a **homogeneous linear differential equation**; otherwise, it is a **non-homogeneous linear differential equation**.

## Deriving the integrating factor

The linear DE can be written as $[P(x)y - Q(x)]\,dx + dy = 0$, so $M = P(x)y - Q(x)$, $N = 1$. Here $M_y = P(x)$, $N_x = 0$, so the DE is not exact (in general).

Now $\dfrac{M_y - N_x}{N} = P(x)$ is a function of $x$ only, so (Case 1 of [[Integrating Factors]]) the integrating factor is
$$\mu(x) = e^{\int P(x)\,dx}.$$

Multiplying (6) by $\mu$:
$$\mu\frac{dy}{dx} + \mu P(x) y = \mu Q(x). \tag{7}$$
Since $\dfrac{d}{dx}(\mu y) = \mu\dfrac{dy}{dx} + \mu P(x) y$, (7) becomes
$$\frac{d}{dx}(\mu y) = \mu Q(x). \tag{8}$$
Integrating both sides of (8) gives the general solution:
$$\mu y = \int \mu Q(x)\,dx + C, \quad C \text{ arbitrary constant}.$$

**Note:** $\dfrac{M_y-N_x}{M} = \dfrac{P(x)}{P(x)y-Q(x)}$ is *not* a function of $y$ only, so $e^{-\int \frac{M_y-N_x}{M}dy}$ is **not** an IF of (6) — only the $x$-based IF works here.

## Linear DE in $x$

A linear differential equation in $x$ (i.e. $x$ as the dependent variable) is
$$\frac{dx}{dy} + P(y)x = Q(y). \tag{9}$$
Similarly, IF $= \mu = e^{\int P\,dy}$, and the general solution is
$$x = e^{-\int P\,dy}\left[\int Q\,e^{\int P\,dy}\,dy + C\right].$$

## Worked Example

Solve $\dfrac{dy}{dx} + 2y = e^{-2x}$.

$P(x) = 2$, $Q(x) = e^{-2x}$. IF $= \mu = e^{\int 2\,dx} = e^{2x}$.
$$e^{2x}\frac{dy}{dx} + 2e^{2x}y = 1 \implies \frac{d}{dx}(e^{2x}y) = 1$$
**General solution:** $ye^{2x} = x + C$, i.e. $y = e^{-2x}[x+C]$.

## Practice problems

- Solve $\dfrac{dy}{dx} + \dfrac{2}{x+1}y = (x+1)^4$, $x > -1$.
- Solve $\dfrac{dy}{dx} + \dfrac{2}{x}y = \dfrac{\sin x}{x^2}$, $x > 0$.
- Solve $\dfrac{dy}{dx} + \tan x\,y = \sin x$, $-\tfrac{\pi}{2} < x < \tfrac{\pi}{2}$.
- Solve $(e^y - 2xy)\,y' = y^2$ (linear in $x$).
- Solve $xy' + x = x^2(y-1)y'$ (linear in $x$).
- Solve $y - xy' = y'y^2e^y$ (linear in $x$).
- Solve $\sin y\,\dfrac{dy}{dx} = \cos x\,(2\cos y - \sin^2 x)$ (put $\cos y = z$).
- Solve $x^3y' + 4x^2\tan y = e^x\sec y$, $y(1)=0$ (put $\sin y = z$).

---
Next: [[Bernoulli Differential Equations]]

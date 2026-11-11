Related: [[First Order ODEs]], [[Integrating Factors]]

> The differential form $M(x,y)\,dx + N(x,y)\,dy$ is said to be **exact** in a region $R$ of the $xy$-plane if there exists a function $F(x,y)$ such that
> $$dF = \frac{\partial F}{\partial x}\,dx + \frac{\partial F}{\partial y}\,dy = M\,dx + N\,dy$$
> throughout $R$; that is, $F_x = M$ and $F_y = N$. The equation $M\,dx + N\,dy = 0$ is then called an **exact equation**.

Since $M\,dx + N\,dy$ is the total differential of some function $F$, the equation $M\,dx + N\,dy = 0$ reduces to $dF = 0$, whose solution is immediately $F(x,y) = C$.

## Test for Exactness

> **Theorem.** Let $M(x,y)$ and $N(x,y)$ have continuous first partial derivatives in a simply connected region $R$. Then $M\,dx + N\,dy = 0$ is exact in $R$ if and only if
> $$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \quad \text{throughout } R.$$

**Sketch of proof**

($\Rightarrow$) If the equation is exact, then $M = F_x$ and $N = F_y$ for some $F$. Since $F$ has continuous second partials, the mixed partials are equal:
$$\frac{\partial M}{\partial y} = \frac{\partial^2 F}{\partial y\,\partial x} = \frac{\partial^2 F}{\partial x\,\partial y} = \frac{\partial N}{\partial x}.$$

($\Leftarrow$) Conversely, if $M_y = N_x$, define
$$F(x,y) = \int M(x,y)\,dx + g(y),$$
where the integration is performed treating $y$ as constant, and $g(y)$ is an unknown function of $y$ alone. Differentiating with respect to $y$ and setting the result equal to $N$ determines $g'(y)$. The condition $M_y = N_x$ guarantees that the resulting expression for $g'(y)$ depends only on $y$, so $g(y)$ can be found by ordinary integration. This constructs the required $F$.

Note that one can alternatively take $F(x,y) = \int N(x,y)\,dy + h(x)$ and proceed to compute $h(x)$.

## Example 1

Solve $(2xy + 3)\,dx + (x^2 - 1)\,dy = 0$.

$M = 2xy+3$, $N = x^2-1$. Check: $M_y = 2x = N_x$ ⇒ exact.
$$F = \int (2xy+3)\,dx = x^2y + 3x + g(y)$$
$$F_y = x^2 + g'(y) = x^2 - 1 \implies g'(y) = -1 \implies g(y) = -y$$
**General solution:** $x^2y + 3x - y = C$.

## Example 2

Solve $(y\cos x + 2xe^y)\,dx + (\sin x + x^2e^y - 1)\,dy = 0$.

$M_y = \cos x + 2xe^y = N_x$ ⇒ exact.
$$F = \int (y\cos x + 2xe^y)\,dx = y\sin x + x^2e^y + g(y)$$
$$F_y = \sin x + x^2e^y + g'(y) = \sin x + x^2e^y - 1 \implies g(y) = -y$$
**General solution:** $y\sin x + x^2e^y - y = C$.

## Example 3

Solve $e^y\,dx + (xe^y + 2y)\,dy = 0$.

$M_y = e^y = N_x$ ⇒ exact.
$$F = \int e^y\,dx = xe^y + g(y), \qquad F_y = xe^y + g'(y) = xe^y + 2y \implies g(y) = y^2$$
**General solution:** $xe^y + y^2 = C$.

**Alternate route:** Starting instead from $N$, $F = xe^y + y^2 + h(x)$; differentiating w.r.t. $x$ and equating with $M$ gives $h'(x) = 0 \implies h(x) = C_1$, so $F = xe^y + y^2 + C_1 = C$, equivalent to $xe^y + y^2 = K$ where $K = C - C_1$.

> **Caution:** Don't write two constants in the final solution — absorb them into one.


## Visual

![[DE-E2-exact-level-curves.png]]
**Figure:** The solution of an exact equation is a level curve $F(x,y)=C$ of the potential. The gradient $\nabla F=(M,N)$ is perpendicular to every level curve, which is why $M\,dx+N\,dy=dF=0$ along a solution.

---
Next: [[Integrating Factors]]

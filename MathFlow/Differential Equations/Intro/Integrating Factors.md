Related: [[Exact Differential Equations]], [[Linear Differential Equations]]

▶ Many first-order equations $M\,dx + N\,dy = 0$ are not exact as they stand ($M_y \ne N_x$).

▶ Often, however, multiplying the entire equation by a suitably chosen function $\mu(x,y)$ makes it exact. Such a function is called an **integrating factor (IF)**.

> A function $\mu(x,y) \ne 0$ is called an integrating factor for $M\,dx + N\,dy = 0$ if the equation $\mu M\,dx + \mu N\,dy = 0$ is exact.

In this case, $\dfrac{\partial}{\partial y}(\mu M) = \dfrac{\partial}{\partial x}(\mu N)$. Expanding this condition gives the **integrating factor PDE**:
$$\mu_y M - \mu_x N = \mu (N_x - M_y). \tag{1}$$

In general (1) is a PDE for $\mu$, harder to solve than the original ODE. However, in many practical cases $\mu$ can be assumed to depend on only one variable ($x$ alone, $y$ alone, or a simple combination such as $xy$ or $x+y$), which reduces the PDE to an ordinary differential equation for $\mu$.

## Case 1: $\mu$ is a function of $x$ alone

Here $\mu_y = 0$. From (1):
$$\frac{1}{\mu}\frac{d\mu}{dx} = \frac{M_y - N_x}{N}$$
Since the LHS depends only on $x$, we need $\dfrac{M_y-N_x}{N} := f(x)$ to be a function of $x$ only. Integrating,
$$\mu(x) = \exp\left(\int f(x)\,dx\right) = \exp\left(\int \frac{M_y-N_x}{N}\,dx\right).$$

## Case 2: $\mu$ is a function of $y$ alone

Here $\mu_x = 0$. From (1):
$$\frac{1}{\mu}\frac{d\mu}{dy} = -\frac{M_y-N_x}{M}$$
We need $-\dfrac{M_y-N_x}{M} := g(y)$ to be a function of $y$ only.
$$\mu(y) = \exp\left(\int g(y)\,dy\right) = \exp\left(\int \frac{N_x-M_y}{M}\,dy\right).$$

## Case 3: $\mu$ is a function of the product $xy$

With $\mu = \mu(z)$, $z = xy$:
$$\frac{1}{\mu}\frac{d\mu}{dz} = \frac{M_y - N_x}{yN - xM}$$
We need $\dfrac{M_y-N_x}{yN-xM} := h(z)$ to be a function of $z$ only.
$$\mu(z) = \exp\left(\int h(z)\,dz\right) = \exp\left(\int \frac{M_y-N_x}{yN-xM}\,dz\right), \quad z = xy.$$

## Worked Example — Case 1

Solve $(3xy + y^2)\,dx + (x^2 + xy)\,dy = 0$.

$M_y = 3x+2y$, $N_x = 2x+y$ ⇒ not exact.
$$\frac{M_y - N_x}{N} = \frac{x+y}{x(x+y)} = \frac{1}{x}$$
(depends only on $x$) so $\mu(x) = e^{\int \frac{1}{x}dx} = x$.

Multiplying through by $\mu = x$: $(3x^2y + xy^2)\,dx + (x^3 + x^2y)\,dy = 0$, which is exact.
$$F = \int (3x^2y+xy^2)\,dx = x^3y + \tfrac{1}{2}x^2y^2 + g(y), \quad F_y = x^3+x^2y+g'(y) = x^3+x^2y \implies g'(y)=0$$
**General solution:** $x^3y + \tfrac{1}{2}x^2y^2 = C$.

## Worked Example — reducible via Case 1

Solve $(xy-1)\,dx + (x^2 - xy)\,dy = 0$.

$M_y = x$, $N_x = 2x - y$ ⇒ not exact. $\dfrac{N_x-M_y}{M} = \dfrac{x-y}{xy-1}$ is not a function of $y$ alone. But $\dfrac{M_y-N_x}{N} = \dfrac{y-x}{x(x-y)} = -\dfrac1x$, a function of $x$ only, so $\mu(x) = e^{-\ln x} = \tfrac1x$.

Multiplying through: $\left(y - \tfrac1x\right)dx + (x-y)\,dy = 0$, exact.
$$F = \int \left(y-\tfrac1x\right)dx = xy - \ln|x| + g(y), \quad F_y = x+g'(y) = x - y \implies g(y) = -\tfrac{y^2}{2}$$
**General solution:** $xy - \ln|x| - \dfrac{y^2}{2} = C$.

## Worked Example — Case 2

Solve $y\,dx + (2x - ye^y)\,dy = 0$.

$M_y = 1$, $N_x = 2$ ⇒ not exact. $\dfrac{N_x-M_y}{M} = \dfrac{1}{y}$ (function of $y$ only), so $\mu(y) = e^{\int \frac1y dy} = y$.

Multiplying through: $y^2\,dx + (2xy - y^2e^y)\,dy = 0$, exact.
$$F = \int y^2\,dx = xy^2 + g(y), \quad F_y = 2xy + g'(y) = 2xy - y^2e^y \implies g'(y) = -y^2e^y$$
Integrating by parts: $g(y) = -\int y^2 e^y\,dy = -e^y(y^2 - 2y + 2)$.
**General solution:** $xy^2 - e^y(y^2-2y+2) = C$.

## Worked Example — Case 3

Solve $x\,dy + y\,dx + 3x^3y^4\,dy = 0$, i.e. $\underbrace{y}_{M}\,dx + \underbrace{(x+3x^3y^4)}_{N}\,dy = 0$.

$M_y = 1 \ne N_x = 1+9x^2y^4$ ⇒ not exact, and neither Case 1 nor Case 2 applies directly. But
$$\frac{N_x - M_y}{xM - yN} = \frac{9x^2y^4}{-3x^3y^5} = -\frac{3}{xy} = -\frac{3}{z}, \quad z=xy$$
$$\frac{d\mu}{\mu} = -\frac{3}{z}dz \implies \mu = z^{-3}$$
Multiplying through: $\dfrac{y}{x^3y^3}\,dx + \dfrac{x+3x^3y^4}{x^3y^3}\,dy = 0$, exact.

**General solution:** $3x^2y^4 - Cx^2y^2 = 1$.

## Additional results

- If $\dfrac{\partial M/\partial y - \partial N/\partial x}{N-M}$ is a function of $z = x+y$, then $\displaystyle e^{\int \frac{M_y-N_x}{N-M}\,dz}$ is an IF of $M\,dx+N\,dy=0$.
- Similarly one can derive the IF formula when it is a function of $z = x - y$.
- **Homogeneous equations:** If $M\,dx + N\,dy = 0$ is homogeneous and $Mx+Ny \ne 0$, then
$$\frac{1}{Mx+Ny}$$
is an IF.

### Sketch of proof (homogeneous case)

$$M\,dx + N\,dy = \tfrac12\left[(Mx+Ny)\left(\tfrac{dx}{x}+\tfrac{dy}{y}\right) + (Mx-Ny)\left(\tfrac{dx}{x}-\tfrac{dy}{y}\right)\right]$$
$$= \tfrac12\left[(Mx+Ny)\,d(\ln xy) + (Mx-Ny)\,d\!\left(\ln \tfrac{x}{y}\right)\right]$$
Dividing by $Mx+Ny$ and using homogeneity of $\frac{Mx-Ny}{Mx+Ny}$ (write it as $f(x/y)$), the right side becomes an exact differential
$$\tfrac12\,d(\ln xy) + \tfrac12 F\!\left[\ln\!\tfrac{x}{y}\right] d\!\left(\ln\tfrac{x}{y}\right).$$

### Worked Example — homogeneous case

Solve $(x^2y - 2xy^2)\,dx + (3x^2y - x^3)\,dy = 0$.

$M_y = x^2-4xy \ne N_x = 6xy-3x^2$ ⇒ not exact, but $M,N$ are homogeneous of degree 3.
$$\frac{1}{Mx+Ny} = \frac{1}{x^2y^2} \text{ is an IF}$$
Multiplying through: $\left(\tfrac1y - \tfrac2x\right)dx + \left(\tfrac3y - \tfrac{x^2}{y^2}\right)dy = 0$, exact.

**General solution:** $F(x,y) = \dfrac{x}{y} + \ln\!\left(\dfrac{y^3}{x^2}\right) = C$.

## Further observations

- If $Mx + Ny = 0$, then $\dfrac{M}{N} = -\dfrac{y}{x}$, giving $\dfrac{dy}{dx} = \dfrac{y}{x} \Rightarrow y\,dx - x\,dy = 0 \Rightarrow d\!\left(\dfrac{x}{y}\right)=0$, so $x = ky$ is the general solution directly.
- If $Mx - Ny = 0$, then $\dfrac{M}{N} = \dfrac{y}{x}$, giving $y\,dx + x\,dy = 0 \Rightarrow xy = C$ is the general solution directly.
- **Result:** If $Mx - Ny \ne 0$ and $M\,dx+N\,dy=0$ can be written as
$$f_1(xy)\,y\,dx + f_2(xy)\,x\,dy = 0,$$
then $\dfrac{1}{Mx-Ny}$ is an IF.

### Sketch of proof
$$\frac{M\,dx+N\,dy}{Mx-Ny} = \frac12\cdot\frac{Mx+Ny}{Mx-Ny}\,d(\ln xy) + \frac12\,d\!\left(\ln\tfrac{x}{y}\right) = H(\ln xy)\,d(\ln xy) + \frac12\,d\!\left(\ln\tfrac{x}{y}\right),$$
which is an exact differential, so $\dfrac{1}{Mx-Ny}$ is an IF.

---
Next: [[Finding h and k for x^h y^k Integrating Factors]]

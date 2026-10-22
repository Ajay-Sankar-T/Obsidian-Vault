Related: [[Linear Differential Equations]]

▶ A first order DE of the form
$$y' + P(x)y = Q(x)y^n, \quad n \ne 0,\ n \ne 1$$
is called a **Bernoulli DE**. (Note $n=0$ or $n=1$ corresponds to a linear ODE — see [[Linear Differential Equations]].)

## Reduction to Linear Form

Let $v = y^{1-n}$, so $y = v^{\frac{1}{1-n}}$. Then
$$y' = \frac{1}{1-n}v^{\frac{1}{1-n}-1}v' = \frac{1}{1-n}v^{\frac{n}{1-n}}v'$$
Substituting into the DE:
$$\frac{1}{1-n}v^{\frac{n}{1-n}}v' + P(x)v^{\frac{1}{1-n}} = Q(x)\,v^{\frac{n}{1-n}}$$
Dividing by $v^{\frac{n}{1-n}}$ (assuming nonzero):
$$\frac{1}{1-n}v' + P(x)\,v = Q(x)$$
$$\implies v' + (1-n)P(x)\,v = (1-n)Q(x)$$

This is a **linear Lagrange first-order ODE** in $v$ — solve using the method in [[Linear Differential Equations]], then recover $y = v^{\frac{1}{1-n}}$.

## Worked Example: $3y^2y' + y^3 = e^{-x}$

Rewrite: $y' + \tfrac13 y = \tfrac{e^{-x}}{3}y^{-2}$, so $n=-2$.

Take $v = y^{1-(-2)} = y^3$; then $v' = 3y^2y'$. The DE becomes
$$v' + v = e^{-x}$$
a linear DE with IF $= e^{\int dx} = e^x$.
$$ve^x = \int e^x e^{-x}\,dx + C = x + C \implies v = \frac{x+C}{e^x}$$
**General solution:** $y = (x+C)^{1/3}e^{-x/3}$, $\forall x \in \mathbb{R}$.

## Worked Example: $y' = y(xy^3 - 1)$

The DE is $y' + y = xy^4$, Bernoulli with $n=4$. Take $v = y^{-3}$, $y = v^{-1/3}$.
$$\frac{dy}{dx} = -\frac13 v^{-4/3}\frac{dv}{dx}$$
$$-\frac13 v^{-4/3}\frac{dv}{dx} + v^{-1/3} = x\,v^{-4/3} \implies \frac{dv}{dx} - 3v = -3x$$
IF $= e^{-\int 3\,dx} = e^{-3x}$.
$$ve^{-3x} = \int -3xe^{-3x}\,dx + C = \left(x+\frac13\right)e^{-3x} + C$$
**General solution:** $y = \left[x + \dfrac13 + Ce^{3x}\right]^{-1/3}$.

## Worked Example: $x\dfrac{dy}{dx} + 3y = x^2y^{1/2}$, $x>0$

Write as $\dfrac{dy}{dx} + \dfrac{3}{x}y = xy^{1/2}$, so $n = \tfrac12$.

Divide by $y^{1/2}$: $y^{-1/2}\dfrac{dy}{dx} + \dfrac3x y^{1/2} = x$.

Let $v = y^{1/2}$, so $\dfrac{dv}{dx} = \tfrac12 y^{-1/2}\dfrac{dy}{dx}$. Hence
$$2\frac{dv}{dx} + \frac3x v = x \implies \frac{dv}{dx} + \frac{3}{2x}v = \frac{x}{2}$$
a linear DE in $v$. IF $= e^{\int \frac{3}{2x}dx} = x^{3/2}$.
$$\frac{d}{dx}\left(x^{3/2}v\right) = \frac12 x^{5/2} \implies x^{3/2}v = \frac{x^{7/2}}{7} + C \implies v = \frac{x^2}{7} + \frac{C}{x^{3/2}}$$
Since $v = \sqrt{y}$:
$$y = \left(\frac{x^2}{7} + \frac{C}{x^{3/2}}\right)^2$$


## Visual

![[DE-E5-linear-bernoulli.png]]
**Figure:** Middle: $3y^2y'+y^3=e^{-x}$ ($v=y^3$ makes it linear). Right: $y'=y(xy^3-1)$ with $y=[x+\frac{1}{3}+Ce^{3x}]^{-1/3}$; the nonlinear term lets solutions blow up at finite $x$, which a linear equation never does.

---
Related earlier: [[Linear Differential Equations]] · [[Integrating Factors]] · [[Exact Differential Equations]]

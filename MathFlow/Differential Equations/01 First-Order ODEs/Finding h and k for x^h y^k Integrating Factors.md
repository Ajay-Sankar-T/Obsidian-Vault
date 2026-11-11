Related: [[Integrating Factors]]

## Problem

Suppose $x^h y^k$ is an IF for the DE
$$x^a y^b(my\,dx + nx\,dy) + x^c y^d(py\,dx + qx\,dy) = 0 \tag{5}$$
Find $h$ and $k$ if $np \ne mq$.

## Solution

Multiplying $x^hy^k$ with the given DE:
$$\left(x^{a+h}y^{b+k}my + x^{c+h}y^{d+k}py\right)dx + \left(x^{a+h}y^{b+k}nx + x^{c+h}y^{d+k}qx\right)dy = 0$$
which must be exact. Here $M = m\,x^{a+h}y^{b+k+1} + p\,x^{c+h}y^{d+k+1}$ and $N = n\,x^{a+h+1}y^{b+k} + q\,x^{c+h+1}y^{d+k}$.

Using $M_y = N_x$:
$$m\,x^{a+h}(b+k+1)\,y^{b+k} + p\,x^{c+h}(d+k+1)\,y^{d+k} = n(a+h+1)\,x^{a+h}y^{b+k} + q(c+h+1)\,x^{c+h}y^{d+k}$$

Equating coefficients:
$$m(b+k+1) = n(a+h+1)$$
$$p(d+k+1) = q(c+h+1)$$

which rearranges to the linear system

$$nh - mk = m(b+1) - n(a+1)$$
$$qh - pk = p(d+1) - q(c+1) \tag{A}$$

Since $\Delta = mq - np \ne 0$, this system has a unique solution
$$h = \frac{\Delta_1}{\Delta}, \qquad k = \frac{\Delta_2}{\Delta}$$
(by Cramer's rule, with $\Delta_1, \Delta_2$ the determinants formed by replacing the respective column of $\Delta$ with the RHS of (A)).

## Worked Example

Solve $\left(x^{1/2}y - xy^2\right)dx + \left(x^{3/2} + x^2y\right)dy = 0$.

Write the equation as
$$x^{1/2}(y\,dx + x\,dy) + xy(-y\,dx + x\,dy) = 0.$$

Comparing with (5): $a = \tfrac12, b=0, c=1, d=1, m=1, n=1, p=-1, q=1$.

Then (A) reduces to
$$h - k = -\tfrac12, \qquad h+k = -4$$
giving $h = -\tfrac94$, $k = -\tfrac74$.

So the IF is $x^{-9/4}y^{-7/4}$.

**General solution:** $-\dfrac{4}{3}x^{-3/4}y^{-3/4} + 4x^{-1/4}y^{1/4} = K$.

---
Next: [[Linear Differential Equations]]

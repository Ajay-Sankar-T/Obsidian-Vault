Related: [[Legendre's Equation]] · [[Airy's Equation]] · [[Power Series Method]]

$$y''-2xy'+2ny=0.$$
Here $P(x)=-2x$ and $Q(x)=2n$, both analytic everywhere — so $x=0$ is an ordinary point, and in fact the *only* type of point (Hermite's equation has no singular points at all).

Assume $y=\sum_{k=0}^\infty a_kx^k$. Substituting and shifting indices gives
$$(k+2)(k+1)a_{k+2} - 2ka_k + 2na_k = 0 \implies a_{k+2} = \frac{2(k-n)}{(k+1)(k+2)}a_k.$$

Again this links only alternate coefficients: the even series (from $a_0$) and odd series (from $a_1$) form the two independent solutions $y_1,y_2$.
$$y = a_0y_1(x)+a_1y_2(x)$$

When $n$ is a non-negative integer, one series terminates into a polynomial — these are the **Hermite polynomials** $H_n(x)$.

Since there are no singular points, the series converges for **all** $x\in\mathbb{R}$ — contrast with [[Legendre's Equation]], whose singularities at $x=\pm1$ limit convergence to $|x|<1$.

---
Related: [[Series Solutions - Homogeneous Examples]]

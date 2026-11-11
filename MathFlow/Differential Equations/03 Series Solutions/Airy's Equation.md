Related: [[Legendre's Equation]] · [[Hermite's Equation]] · [[Series Solutions About x0 not equal to 0]]

$$y''-xy=0.$$
Here $P(x)=0$, $Q(x)=-x$, both analytic everywhere, so $x=0$ (and every real $x_0$) is an ordinary point — like [[Hermite's Equation]], Airy's equation has no singular points at all.

## Series about $x_0=0$

Assume $y=\sum_{n=0}^\infty a_nx^n$. Then $y''=\sum(n+2)(n+1)a_{n+2}x^n$ and $xy=\sum a_nx^{n+1}$. Shifting the index in the second sum and comparing powers of $x$:
$$2a_2=0, \qquad a_{n+2}=\frac{a_{n-1}}{(n+2)(n+1)} \ (n\ge1).$$
So $a_2=0$, and coefficients split into three chains based on $a_0$, $a_1$, and multiples of $a_2=0$. Two independent series:
$$y_1(x) = a_0\left(1+\frac{x^3}{6}+\frac{x^6}{180}+\cdots\right), \qquad y_2(x) = a_1\left(x+\frac{x^4}{12}+\frac{x^7}{504}+\cdots\right)$$
$$y = a_0y_1(x)+a_1y_2(x)$$
These combinations define the **Airy functions** $\mathrm{Ai}(x), \mathrm{Bi}(x)$. Converges for all $x\in\mathbb{R}$.

## Series about $x_0=2$

Substitute $t=x-2$, so $x=t+2$; the equation becomes $y''-(t+2)y=0$. With $y=\sum a_nt^n$: $y''=\sum n(n-1)a_nt^{n-2}$, and $(t+2)y=ty+2y=\sum a_nt^{n+1}+2\sum a_nt^n$.

Shifting all series to a common index $k$: the $ty$ sum only starts at $k=1$, so $k=0$ is a separate case.

- **$k=0$:** only $y''$ and $2y$ contribute: $2a_2-2a_0=0 \Rightarrow a_2=a_0$.
- **$k\ge1$:** $(k+2)(k+1)a_{k+2}-a_{k-1}-2a_k=0 \Rightarrow a_{k+2}=\dfrac{a_{k-1}+2a_k}{(k+2)(k+1)}$.

With $a_0=1,a_1=0$: $a_2=1, a_3=\tfrac16, a_4=\tfrac16, a_5=\tfrac1{15},\dots$
$$y_1(t) = 1+t^2+\frac{t^3}{6}+\frac{t^4}{6}+\cdots$$
With $a_0=0,a_1=1$: $a_2=0, a_3=\tfrac13, a_4=\tfrac1{12}, a_5=\tfrac1{30},\dots$
$$y_2(t) = t+\frac{t^3}{3}+\frac{t^4}{12}+\cdots$$
Substituting back $t=x-2$:
$$y = C_1\left[1+(x-2)^2+\tfrac16(x-2)^3+\cdots\right] + C_2\left[(x-2)+\tfrac13(x-2)^3+\cdots\right]$$
Since Airy's equation has no singular points anywhere, this series converges for all $x$ — this worked example illustrates the general method in [[Series Solutions About x0 not equal to 0]].


## Visual

![[DE-S3-airy.png]]
**Figure:** The Airy functions $\mathrm{Ai},\mathrm{Bi}$ oscillate for $x<0$ and grow/decay exponentially for $x>0$. Right: $\mathrm{Ai}$ is the specific combination $\mathrm{Ai}(0)y_1+\mathrm{Ai}'(0)y_2$ of the two power series.

---
Related: [[Series Solutions - Homogeneous Examples]] · [[Radius of Convergence of Series Solutions]]

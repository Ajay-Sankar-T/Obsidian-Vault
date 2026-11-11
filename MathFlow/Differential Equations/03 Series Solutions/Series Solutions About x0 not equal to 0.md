Related: [[Power Series Method]] · [[Airy's Equation]] (worked example at $x_0=2$)

In general, $x_0\ne0$ can be any ordinary point of $y''+P(x)y'+Q(x)y=0$ (see [[Ordinary and Singular Points]]). The method is identical to the $x_0=0$ case, but the series is expanded in powers of $(x-x_0)$ instead of $x$.

## Steps

1. Substitute $t=x-x_0$, so $x=t+x_0$ and $t=0$ corresponds to $x=x_0$.
2. Rewrite $P(x)$ and $Q(x)$ as functions of $t$ using $x=t+x_0$.
3. Assume $y=\sum_{n=0}^\infty a_nt^n$ and substitute as before.
4. Derive the recurrence relation in terms of $a_n$.
5. Convert back to $x$ using $t=x-x_0$ at the end.

The radius of convergence is the distance from $x_0$ to the nearest singular point — see [[Radius of Convergence of Series Solutions]].

## Worked Example: $y''+xy'+y=0$ about $x_0=1$

$P(x)=x$, $Q(x)=1$ are entire (analytic everywhere), so $x_0=1$ is ordinary (as is every real number). Substitute $t=x-1$, so $x=t+1$; the equation becomes
$$y''+(t+1)y'+y=0.$$
With $y=\sum a_nt^n$, $y'=\sum na_nt^{n-1}$, $y''=\sum n(n-1)a_nt^{n-2}$, expand $(t+1)y'=ty'+y'$ and match every power of $t$ — this requires shifting **three** different series onto a common index $k$:

- $y''$: let $n=k+2$: $\sum_{k=0}^\infty (k+2)(k+1)a_{k+2}t^k$
- $ty'$: let $n=k$ (no shift needed): $\sum_{k=0}^\infty ka_kt^k$
- $y'$: let $n=k+1$: $\sum_{k=0}^\infty (k+1)a_{k+1}t^k$
- $y$: already $\sum_{k=0}^\infty a_kt^k$

Adding all four series and setting the coefficient of $t^k$ to zero:
$$(k+2)(k+1)a_{k+2}+ka_k+(k+1)a_{k+1}+a_k=0$$
Since $ka_k+a_k=(k+1)a_k$:
$$(k+2)(k+1)a_{k+2}+(k+1)a_{k+1}+(k+1)a_k=0 \implies a_{k+2} = -\frac{a_{k+1}+a_k}{k+2}, \ k\ge0.$$

With $a_0=1,a_1=0$: $a_2=-\tfrac12, a_3=\tfrac16, a_4=\tfrac1{12},\dots$
$$y_1(t) = 1-\frac12t^2+\frac16t^3+\frac1{12}t^4+\cdots$$
With $a_0=0,a_1=1$: $a_2=-\tfrac12, a_3=-\tfrac16, a_4=\tfrac16,\dots$
$$y_2(t) = t-\frac12t^2-\frac16t^3+\frac16t^4+\cdots$$
General solution in $t$: $y=C_1y_1(t)+C_2y_2(t)$. Substituting back $t=x-1$:
$$y = C_1\left[1-\tfrac12(x-1)^2+\tfrac16(x-1)^3+\cdots\right] + C_2\left[(x-1)-\tfrac12(x-1)^2-\tfrac16(x-1)^3+\cdots\right]$$
Since $P(x),Q(x)$ have no singularities, this series converges for all $x$.

For a second worked example (Airy's equation at $x_0=2$, including the subtlety of a series that starts contributing only from $k=1$), see [[Airy's Equation]].

---
Next: [[Radius of Convergence of Series Solutions]]

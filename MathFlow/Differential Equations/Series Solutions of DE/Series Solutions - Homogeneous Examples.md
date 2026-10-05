Related: [[Power Series Method]] · [[2nd Order Linear ODE with Constant Coefficients]] (constant-coefficient closed forms for comparison)

## Example 1: $y''-y=0$

Assume $y=\sum a_nx^n$; substituting $y''=\sum(n+2)(n+1)a_{n+2}x^n$ into $y''-y=0$ and equating coefficients:
$$(n+2)(n+1)a_{n+2}-a_n=0 \implies a_{n+2}=\frac{a_n}{(n+2)(n+1)}.$$
Even coefficients: $a_{2k}=\dfrac{a_0}{(2k)!}$. Odd coefficients: $a_{2k+1}=\dfrac{a_1}{(2k+1)!}$.
$$y = a_0\sum_{k=0}^\infty \frac{x^{2k}}{(2k)!} + a_1\sum_{k=0}^\infty \frac{x^{2k+1}}{(2k+1)!} = a_0\cosh x + a_1\sinh x$$
Converges for all $x$ (no singular points); radius of convergence $R=\infty$ for both series ($R=\lim|a_n/a_{n+1}|$).

## Example 2: $y''+y=0$

Same setup gives $a_{n+2}=-\dfrac{a_n}{(n+2)(n+1)}$, so $a_{2k}=\dfrac{(-1)^ka_0}{(2k)!}$, $a_{2k+1}=\dfrac{(-1)^ka_1}{(2k+1)!}$.
$$y = a_0\cos x + a_1\sin x$$
Converges for all $x\in\mathbb{R}$ — matching the known [[Existence, Uniqueness, and Fundamental Sets]] example for $y''+y=0$ via a completely different method.

## Example 3: $(1+x)y''+y'-y=0$ around $x=0$

Since $1+0=1\ne0$, $x=0$ is ordinary. With $y'=\sum(n+1)a_{n+1}x^n$, $y''=\sum(n+2)(n+1)a_{n+2}x^n$, substituting into $y''+xy''+y'-y=0$ gives coefficient of $x^n$:
$$(n+2)(n+1)a_{n+2}+(n+1)^2a_{n+1}-a_n=0 \implies a_{n+2}=\frac{a_n-(n+1)^2a_{n+1}}{(n+2)(n+1)}.$$
$a_0,a_1$ arbitrary; e.g. $a_2=\dfrac{a_0-a_1}{2}$, $a_3=\dfrac{3a_1-2a_0}{6}$, $a_4=\dfrac{a_2-9a_3}{12}$.
$$y = a_0+a_1x+\frac{a_0-a_1}{2}x^2+\frac{3a_1-2a_0}{6}x^3+a_4x^4+\cdots$$
Two independent solutions come from $(a_0,a_1)=(1,0)$ and $(0,1)$.

## Example 4: $y''+xy'+y=0$ around $x=0$

With $xy'=\sum_{n=1}^\infty na_nx^n$, substitution gives $(n+2)(n+1)a_{n+2}+(n+1)a_n=0 \implies a_{n+2}=-\dfrac{a_n}{n+2}$.
$$a_{2k} = \frac{(-1)^ka_0}{2^kk!}, \qquad a_{2k+1} = \frac{(-1)^ka_1}{1\cdot3\cdot5\cdots(2k+1)}$$
$$y = C_1\left(1-\frac{x^2}{2}+\frac{x^4}{8}-\frac{x^6}{48}+\cdots\right) + C_2\left(x-\frac{x^3}{3}+\frac{x^5}{15}-\frac{x^7}{105}+\cdots\right)$$

This recurrence is reused in [[Series Solution of Non-homogeneous Equations]].

---
Next: [[Legendre's Equation]] · [[Hermite's Equation]] · [[Airy's Equation]]

Related: [[Regular and Irregular Singular Points]] · [[Cauchy-Euler Equations]] (2nd Order DE)

> **Theorem (Frobenius).** Let $x=0$ be a regular singular point of $y''+P(x)y'+Q(x)y=0$. Then there exists at least one solution of the form
> $$y = x^r\sum_{n=0}^\infty a_nx^n, \qquad a_0\ne0.$$

- $r$ is a constant (real or complex) to be determined — the exponent need **not** be a non-negative integer.
- The series converges in some interval $0<x<R$, where $R$ is the distance to the nearest other singular point (same principle as [[Radius of Convergence of Series Solutions]]).
- A second linearly independent solution may or may not have the same simple form; its form depends on the relationship between the two roots of the **indicial equation** (three cases arise — analogous to the three cases for the auxiliary/indicial equation of a [[Cauchy-Euler Equations|Cauchy-Euler equation]]: distinct roots not differing by an integer, roots differing by an integer, and repeated roots).

This generalizes the ordinary power series method ([[Power Series Method]]) by allowing the leading factor $x^r$ — motivated by the standard form near a regular singular point derived in [[Regular and Irregular Singular Points]], where the equation resembles a Cauchy-Euler equation with variable coefficients. Deriving the **indicial equation** that determines $r$ is the next step (continued in the next lecture).

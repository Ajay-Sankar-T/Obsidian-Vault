Related: [[Solution of a Second Order ODE]]

## Initial Value Problem (IVP)

Consider a 2nd order linear homogeneous DE:
$$y'' + P(x)y' + Q(x)y = 0, \quad x \in I \tag{3}$$
with initial conditions $y(x_0)=y_0$, $y'(x_0)=y_0'$, $x_0 \in I$ (4).

Since (3) is 2nd order linear, its general solution has two arbitrary constants: $y = C_1y_1+C_2y_2$, where $y_1,y_2$ are suitable solutions of (3). Using (4), we solve for $C_1,C_2$ to get the unique particular solution of the IVP — the curve through $(x_0,y_0)$ with slope $y_0'$ there.

## Linear Independence

> Two functions $y_1,y_2$ on $I$ are **linearly independent** if $c_1y_1(x)+c_2y_2(x)=0\ \forall x\in I \Rightarrow c_1=c_2=0$. Otherwise they are **linearly dependent**.

Equivalently, $y_1,y_2$ are dependent iff one is a constant multiple of the other.

- $e^x, e^{2x}$ are linearly independent on any interval.
- $\sin x, 2\sin x$ are linearly dependent.

Linear independence of solutions is key to forming the general solution.

## The Wronskian

> **Definition.** For $y_1(x), y_2(x)$ differentiable on $I$,
> $$W(y_1,y_2)(x) = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} = y_1y_2' - y_2y_1'.$$

- $W$ is itself a function of $x$ on $I$; it provides a computable test for linear independence.
- If $W(y_1,y_2)(x_0) \ne 0$ for some $x_0 \in I$, then $y_1,y_2$ are linearly independent on $I$.
- If $y_1,y_2$ are linearly dependent, then $W(y_1,y_2)(x) \equiv 0$ on $I$.
- **Note:** $W \equiv 0$ does *not* always imply dependence for arbitrary functions (only for solutions of a common linear ODE — see [[Abel's Formula]]).

## Wronskian Test for Solutions

> **Theorem.** Let $y_1,y_2$ be solutions of $y''+P(x)y'+Q(x)y=0$ on $I$. Then $y_1,y_2$ are linearly independent on $I$ **iff** $W(y_1,y_2)(x) \ne 0$ for *every* $x \in I$.

### Proof ($\Rightarrow$)

Suppose $y_1,y_2$ are linearly independent on $I$. Let $W(x) = y_1y_2'-y_2y_1'$. Differentiating:
$$W'(x) = y_1'y_2' + y_1y_2'' - y_2'y_1' - y_2y_1'' = y_1y_2''-y_2y_1''.$$
Since both satisfy $y'' = -P(x)y'-Q(x)y$:
$$W' = y_1(-Py_2'-Qy_2) - y_2(-Py_1'-Qy_1) = -P(y_1y_2'-y_2y_1') = -PW.$$
Hence $W'+PW=0$ ([[Abel's Formula]]), giving $W(x) = Ce^{-\int P(x)dx}$.

Suppose, contrary to the claim, $W(x_0)=0$ for some $x_0$. Then $C=0$ (since $e^{-\int P dx}\ne0$), so $W(x)\equiv0$ on $I$. On any interval where $y_1\ne0$:
$$\left(\frac{y_2}{y_1}\right)' = \frac{y_1y_2'-y_2y_1'}{y_1^2} = \frac{W(x)}{y_1^2}=0.$$
So $y_2/y_1=k$ constant, i.e. $y_2=ky_1$ — contradicting independence. Thus $W(x)\ne0$ for every $x\in I$.

### Proof ($\Leftarrow$)

Suppose $W(x)\ne0$ for every $x\in I$. Assume, to the contrary, $y_1,y_2$ are linearly dependent: $c_1y_1+c_2y_2=0$ non-trivially. WLOG $c_2\ne0$, so $y_2=-\tfrac{c_1}{c_2}y_1$, $y_2'=-\tfrac{c_1}{c_2}y_1'$. Then
$$W(y_1,y_2) = y_1\left(-\tfrac{c_1}{c_2}y_1'\right) - \left(-\tfrac{c_1}{c_2}y_1\right)y_1' = 0,$$
contradicting $W\ne0$. Hence $y_1,y_2$ are linearly independent. $\blacksquare$


## Visual

![[DE-E6-wronskian.png]]
**Figure:** Independent solutions have $W\ne0$ everywhere; dependent ones have $W\equiv0$. The right panel is the warning in the note: $x^3$ and $|x|^3$ have $W\equiv0$ yet are independent, because they do not solve a common linear ODE with continuous coefficients.

---
Next: [[Abel's Formula]]

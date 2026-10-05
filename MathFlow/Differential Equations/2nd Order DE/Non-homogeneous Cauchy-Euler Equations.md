Related: [[Cauchy-Euler Equations]] · [[Variation of Parameters]] · [[Undetermined Coefficients]]

$$ax^2y''+bxy'+cy=f(x), \quad x>0.$$

As with any linear ODE: $y = y_c(x)+y_p(x)$, where $y_c$ is found as in [[Cauchy-Euler Equations]] (three cases), and $y_p$ is any particular solution.

## Two Techniques for $y_p$

**Technique A — Variation of Parameters:** works for *any* continuous $f(x)$. Write in standard form $y''+\dfrac{b}{ax}y'+\dfrac{c}{ax^2}y = \dfrac{f(x)}{ax^2}=:g(x)$. With $y_1,y_2$ the complementary solutions and $W(x)$ their Wronskian:
$$y_p = -y_1\int \frac{y_2\,g(x)}{W(x)}dx + y_2\int \frac{y_1\,g(x)}{W(x)}dx$$
For Cauchy–Euler equations, $W(x)$ is always a simple power of $x$, often making the integrals tractable.

**Technique B — Transform $t=\ln x$, then Undetermined Coefficients:** works when $f(x)$ becomes a "nice" function of $t$. E.g. $f(x)=x^k$ becomes $f(e^t)=e^{kt}$ (UC-friendly); $f(x)=x^k\ln x$ becomes $te^{kt}$. Solve for $y_p(t)$ using [[Undetermined Coefficients]], then substitute back $t=\ln x$. Usually **faster** when $f(x)$ is a power of $x$ (with or without $\ln x$).

## Worked Examples

### Example — Technique B (power of $x$)

Solve $x^2y''-2xy'-4y=x^3$, $x>0$. From [[Cauchy-Euler Equations]], $y_c=C_1x^4+C_2x^{-1}$.

Transform: $\ddot y-\dot y-2\dot y-4y=e^{3t} \Rightarrow \ddot y-3\dot y-4y=e^{3t}$. AE roots $4,-1$ match $y_c$. Since 3 is not a root, try $y_p=Ae^{3t}$: $9A-9A-4A=-4A=1\Rightarrow A=-\tfrac14$. So $y_p(t)=-\tfrac14e^{3t}$, and since $e^{3t}=x^3$:
$$y_p(x) = -\tfrac14x^3, \qquad y = C_1x^4+C_2x^{-1}-\tfrac14x^3$$

### Example — Technique A (with $\ln x$ forcing)

Solve $x^2y''-2xy'+2y=x^3\ln x$, $x>0$. AE $m(m-1)-2m+2=0 \Rightarrow m^2-3m+2=0 \Rightarrow (m-1)(m-2)=0$. Roots $1,2$: $y_c=C_1x^2+C_2x$.

Standard form: $y''-\tfrac2x y'+\tfrac2{x^2}y=x\ln x$, so $g(x)=x\ln x$. $y_1=x^2,y_2=x$, $W=x^2(1)-x(2x)=-x^2$.
$$\int \frac{y_2g}{W}dx = \int\frac{x\cdot x\ln x}{-x^2}dx = -\int\ln x\,dx = -(x\ln x-x)$$
$$\int \frac{y_1g}{W}dx = \int\frac{x^2\cdot x\ln x}{-x^2}dx = -\int x\ln x\,dx = -\left(\tfrac{x^2}{2}\ln x-\tfrac{x^2}{4}\right)$$
$$y_p = -x^2\left[-(x\ln x-x)\right] + x\left[-\left(\tfrac{x^2}{2}\ln x-\tfrac{x^2}{4}\right)\right] = \tfrac{x^3}{2}\ln x-\tfrac{3x^3}{4}$$
$$y = C_1x^2+C_2x+\tfrac{x^3}{2}\ln x-\tfrac{3x^3}{4}$$

### Example — Technique B again

Solve $x^2y''+xy'-y=x^2$, $x>0$. AE $m^2-1=0$, roots $\pm1$: $y_c=C_1x+C_2x^{-1}$.

Transform: $\ddot y-y=e^{2t}$ (roots $\pm1$ match). 2 is not a root: $y_p=Ae^{2t}$, $4A-A=3A=1\Rightarrow A=\tfrac13$. Since $e^{2t}=x^2$:
$$y = C_1x+C_2x^{-1}+\tfrac13x^2$$

Comparing these examples: **Technique B** is preferred whenever $f(x)$ is a pure power of $x$ (with or without $\ln x$); **Technique A** is the general-purpose fallback for any $f(x)$.

---
Related: [[Variation of Parameters - 3rd Order]] · [[Higher Order Homogeneous ODEs]]

Related: [[General Solution Structure Theorem]] · [[2nd Order Linear ODE with Constant Coefficients]]

## Motivation

For $y'' + P(x)y' + Q(x)y = 0$, the general solution needs *two* independent solutions. Sometimes only *one* solution $y_1(x)$ is known (by inspection, series methods, etc.). **Reduction of order** constructs a second, independent solution $y_2$ from $y_1$.

Idea: seek $y_2(x) = v(x)y_1(x)$ for an unknown function $v(x)$. This reduces the 2nd order ODE for $y_2$ to a **1st order ODE for $v'$** — hence the name. The method also works for non-homogeneous equations (finding $y_p$ from $y_c$).

## Derivation

Let $y_1(x)$ be a known nontrivial solution on $I$, $y_1(x)\ne0$ on $I$. Assume $y = v(x)y_1(x)$. Then
$$y' = v'y_1+vy_1', \qquad y'' = v''y_1+2v'y_1'+vy_1''.$$
Substituting into the ODE:
$$y_1v'' + \left(2y_1'+P(x)y_1\right)v' + \left(y_1''+P(x)y_1'+Q(x)y_1\right)v = 0$$
$$\implies y_1v'' + \left(2y_1'+P(x)y_1\right)v' = 0$$
since $y_1$ solves the homogeneous equation — **no $v$ term remains**.

Let $w=v'$. This is first order and separable:
$$\frac{w'}{w} = -\frac{2y_1'}{y_1} - P(x)$$
Integrating: $\ln|w| = -2\ln|y_1| - \int P(x)\,dx + C$, so (taking constant $=1$)
$$w(x) = \frac{e^{-\int P(x)dx}}{y_1^2(x)}.$$
Integrating again gives $v(x) = \displaystyle\int \frac{e^{-\int P(x)dx}}{y_1^2(x)}\,dx$, hence the **second solution formula**:
$$\boxed{y_2(x) = y_1(x)\int \frac{e^{-\int P(x)dx}}{y_1^2(x)}\,dx}$$

Now $W(y_1,y_2) = y_1^2 w = e^{-\int P(x)dx} \ne 0$, matching [[Abel's Formula]], so $y_1,y_2$ are independent. General solution: $y=c_1y_1(x)+c_2y_2(x)$.

## Worked Examples

**1.** $y'' - 2ry' + r^2y = 0$, $y_1 = e^{rx}$. Here $P(x)=-2r$, $e^{-\int Pdx}=e^{2rx}$.
$$v(x) = \int \frac{e^{2rx}}{(e^{rx})^2}dx = \int 1\,dx = x \implies y_2 = xe^{rx}$$
**GS:** $y = c_1e^{rx}+c_2xe^{rx}$.

**2.** $x^2y''-xy'+y=0$, $x>0$, $y_1=x$. Standard form gives $P(x)=-\tfrac1x$, $e^{-\int Pdx}=x$.
$$v(x) = \int \frac{x}{x^2}dx = \int\frac1x dx = \ln x \implies y_2 = x\ln x$$
**GS:** $y = c_1x+c_2x\ln x$.

**3.** $(1-x^2)y''-2xy'+2y=0$, $y_1=x$. Standard form: $P(x) = -\dfrac{2x}{1-x^2}$, $e^{-\int Pdx} = \dfrac{1}{1-x^2}$.
$$v(x) = \int \frac{1}{x^2(1-x^2)}dx = \int\left(\frac1{x^2}+\frac1{1-x^2}\right)dx = -\frac1x+\frac12\ln\left|\frac{1+x}{1-x}\right|$$
$$y_2 = -1+\frac{x}{2}\ln\left|\frac{1+x}{1-x}\right|$$

**4.** $y''+y=0$, $y_1=\cos x$. Here $P(x)=0$, $e^{-\int Pdx}=1$.
$$v(x) = \int \sec^2x\,dx = \tan x \implies y_2 = \tan x\cdot\cos x = \sin x$$
Fundamental set: $\{\cos x,\sin x\}$ — confirms the earlier example in [[Existence, Uniqueness, and Fundamental Sets]].

---
Next: [[2nd Order Linear ODE with Constant Coefficients]]

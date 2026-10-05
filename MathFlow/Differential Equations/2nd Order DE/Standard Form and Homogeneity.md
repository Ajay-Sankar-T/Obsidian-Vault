Related: [[2nd Order ODEs - MOC]] · [[First Order ODEs]]

## Standard Form

General form of a 2nd order ODE: $F(x, y, y', y'') = 0 \quad (*)$

- $x$ — independent variable, $y$ — dependent variable
- **Linear 2nd order ODE:** $a_0(x)y'' + a_1(x)y' + a_2(x)y = a_3(x)$.
- If $a_0(x) \ne 0$ for every $x$ in the domain of $y$, divide by $a_0(x)$:
$$y'' + P(x)y' + Q(x)y = R(x)$$
where $P(x) = \dfrac{a_1(x)}{a_0(x)}$, $Q(x) = \dfrac{a_2(x)}{a_0(x)}$, $R(x) = \dfrac{a_3(x)}{a_0(x)}$. $P,Q$ are the **coefficients** of the DE.

**Standard Form** of the 2nd order ODE:
$$y'' + P(x)y' + Q(x)y = R(x). \tag{1}$$

Otherwise, $(*)$ is called **nonlinear**.

## Homogeneous vs Non-homogeneous

- If $R(x) \equiv 0$ for all $x$ considered, $y'' + P(x)y' + Q(x)y = 0$ is a **homogeneous** DE.
- If $R(x) \not\equiv 0$, (1) is **non-homogeneous**.

**Examples:**
1. $y'' + 25y = e^{-x}\cos x$ (linear, non-homogeneous)
2. $y'' + 25y = 0$ (linear, homogeneous)
3. $xy'' + y' + xy = 0 \Rightarrow y'' + \tfrac1x y' + y = 0$, $x \ne 0$ (linear, homogeneous)
4. $y''y + y'^2 = 0$ (nonlinear)

---
Next: [[Solution of a Second Order ODE]]

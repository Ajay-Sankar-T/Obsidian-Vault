Related: [[Higher Order Homogeneous ODEs]] · [[Reduction of Order]] · [[Non-homogeneous Cauchy-Euler Equations]]

The **Cauchy–Euler equation** (equidimensional equation) is a linear ODE with variable coefficients that can be solved in closed form without series methods. It arises in problems with radial/cylindrical symmetry (Laplace's equation in polar form), beam deflection, circuits, elasticity models.

## Standard Form

$$ax^2y'' + bxy' + cy = 0, \quad a\ne0, \ x>0.$$

The power of $x$ matches the order of differentiation — hence "equidimensional." Dividing by $x^2$: $y''+\dfrac{b}{ax}y'+\dfrac{c}{ax^2}y=0$, so $P(x)=\dfrac{b}{ax}$, $Q(x)=\dfrac{c}{ax^2}$. Both $xP(x)$ and $x^2Q(x)$ are constants (hence analytic at 0), so **$x=0$ is always a regular singular point**.

## Why $y=x^m$ works

Each term of $ax^2y''+bxy'+cy=0$ scales the same way under $x\to\lambda x$ — scale invariance suggests a pure power solution. Try $y=x^m$: $y'=mx^{m-1}$, $y''=m(m-1)x^{m-2}$. Substituting:
$$\left[a\,m(m-1)+bm+c\right]x^m = 0.$$
Since $x^m\ne0$ for $x>0$, the bracket vanishes — the **auxiliary (indicial) equation**:
$$am(m-1)+bm+c=0 \iff am^2+(b-a)m+c=0.$$
$$m = \frac{-(b-a)\pm\sqrt{(b-a)^2-4ac}}{2a}$$
Three cases parallel [[2nd Order Linear ODE with Constant Coefficients]].

## Case 1: Distinct Real Roots

$y_1=x^{m_1}, y_2=x^{m_2}$. $W(y_1,y_2)=(m_2-m_1)x^{m_1+m_2-1}\ne0$ for $x>0$.
$$y = C_1x^{m_1}+C_2x^{m_2}$$

## Case 2: Repeated Real Root

$m_1=m_2=m$ (when $(b-a)^2-4ac=0$). $y_1=x^m$; by [[Reduction of Order]], $y_2=x^m\ln x$. $W=x^{2m-1}\ne0$.
$$y = C_1x^m+C_2x^m\ln x = x^m(C_1+C_2\ln x)$$

## Case 3: Complex Conjugate Roots

$m=\alpha\pm i\beta$, $\beta\ne0$. Using $x^{i\beta}=e^{i\beta\ln x}=\cos(\beta\ln x)+i\sin(\beta\ln x)$, real solutions are $y_1=x^\alpha\cos(\beta\ln x)$, $y_2=x^\alpha\sin(\beta\ln x)$.
$$y = x^\alpha\left[C_1\cos(\beta\ln x)+C_2\sin(\beta\ln x)\right]$$
The exact analogue of $y=e^{\alpha x}[C_1\cos\beta x+C_2\sin\beta x]$, with $\ln x$ playing the role $x$ plays there.

## The $t=\ln x$ Transform (equivalent derivation)

Let $t=\ln x$, so $x=e^t$, $\dfrac{dt}{dx}=\dfrac1x$. Chain rule gives
$$x\frac{dy}{dx} = \frac{dy}{dt} \ (=\dot y), \qquad x^2\frac{d^2y}{dx^2} = \frac{d^2y}{dt^2}-\frac{dy}{dt} \ (= \ddot y - \dot y).$$
Substituting into $ax^2y''+bxy'+cy=f(x)$ gives a **constant-coefficient** ODE in $t$:
$$a\ddot y + (b-a)\dot y + cy = f(e^t).$$
Its auxiliary equation $am(m-1)+bm+c=0$ matches the direct method exactly — both approaches always agree:

| Direct ($y=x^m$) | Transform ($t=\ln x$) |
|---|---|
| Distinct roots: $x^{m_1},x^{m_2}$ | $e^{m_1t},e^{m_2t}=x^{m_1},x^{m_2}$ |
| Repeated root: $x^m, x^m\ln x$ | $e^{mt}, te^{mt}=x^m, x^m\ln x$ |
| Complex $\alpha\pm i\beta$: $x^\alpha\cos(\beta\ln x)$, etc. | $e^{\alpha t}\cos\beta t$, etc. |

The transform method is usually preferred for **non-homogeneous** problems — see [[Non-homogeneous Cauchy-Euler Equations]].

## Worked Examples

**$x^2y''-2xy'-4y=0$, $x>0$:** AE $m(m-1)-2m-4=0 \Rightarrow m^2-3m-4=0 \Rightarrow (m-4)(m+1)=0$. Roots $4,-1$ (distinct).
$$y = C_1x^4+C_2x^{-1}$$

**$x^2y''-3xy'+4y=0$, $x>0$:** AE $m^2-4m+4=0 \Rightarrow (m-2)^2=0$. Repeated root $m=2$.
$$y = x^2(C_1+C_2\ln x)$$

**$x^2y''+xy'+y=0$, $x>0$:** AE $m^2+1=0$. Roots $\pm i$ ($\alpha=0,\beta=1$).
$$y = C_1\cos(\ln x)+C_2\sin(\ln x)$$

---
Next: [[Non-homogeneous Cauchy-Euler Equations]]

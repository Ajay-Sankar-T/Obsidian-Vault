Related: [[Higher Order Homogeneous ODEs]] · [[Undetermined Coefficients]] · [[Variation of Parameters - 3rd Order]]

## Goal

Find $y_p$ for $a_ny^{(n)}+\cdots+a_1y'+a_0y=R(x)$ with constant coefficients. Same restriction as the 2nd order case: $R(x)$ must be polynomial, exponential, sine/cosine, or products/sums of these.

## Standard trial forms (no duplication with $y_c$)

- $R(x)=P_m(x)$ ⇒ $y_p=A_mx^m+\cdots+A_0$ (0 not a root of AE)
- $R(x)=ae^{kx}$ ⇒ $y_p=Ae^{kx}$ ($k$ not a root of AE)
- $R(x)=a\cos\beta x$ or $a\sin\beta x$ ⇒ $y_p=A\cos\beta x+B\sin\beta x$ ($i\beta$ not a root of AE)
- $R(x)=P_m(x)e^{kx}$ ⇒ $y_p=(A_mx^m+\cdots+A_0)e^{kx}$
- $R(x)=e^{kx}(a\cos\beta x+b\sin\beta x)$ ⇒ $y_p=e^{kx}(A\cos\beta x+B\sin\beta x)$ ($k+i\beta$ not a root)

## Modification Rule (key difference from 2nd order)

Let $s$ be the multiplicity of the matching root ($k$, or $k\pm i\beta$) in the auxiliary equation. In higher order equations, $s$ can be 2, 3, or more (not just 0 or 1). **Rule:** multiply the standard trial form by $x^s$.

- Example: a root of multiplicity 3 matching $e^{kx}$ forces $y_p=Ax^3e^{kx}$.
- For product forcing $P_m(x)e^{kx}$ with duplication: trial is $x^s(A_mx^m+\cdots+A_0)e^{kx}$.
- Superposition still applies: split $R=R_1+R_2$, solve separately, add.

## Useful trick

For forcing $e^{kx}$ matching a root $k$ of multiplicity $s$, substitute $y=e^{kx}u(x)$. The equation reduces to $u^{(s)}\cdot(\text{const})=1$ (roughly), so $u_p$ is a degree-$s$ monomial in $x$ — avoids differentiating $x^se^{kx}$ directly multiple times (see Problem 3 below).

## Step-by-step procedure

1. Solve the auxiliary equation; list roots and multiplicities.
2. Write $y_c$.
3. Choose trial form for $y_p$ matching $R(x)$'s type.
4. Check for duplication with $y_c$; find multiplicity $s$, multiply by $x^s$.
5. Substitute, equate coefficients, solve.
6. Write $y=y_c+y_p$; apply ICs if given.

## Worked Examples

**$y'''-6y''+11y'-6y=e^{4x}$:** $y_c=c_1e^x+c_2e^{2x}+c_3e^{3x}$. 4 not a root ($s=0$): $y_p=Ae^{4x}$, $6A=1 \Rightarrow A=\tfrac16$.
$$y = c_1e^x+c_2e^{2x}+c_3e^{3x}+\tfrac16e^{4x}$$

**$y'''-6y''+11y'-6y=e^{2x}$:** 2 is a simple root ($s=1$): $y_p=Axe^{2x}$, $-A=1\Rightarrow A=-1$.
$$y = c_1e^x+c_2e^{2x}+c_3e^{3x}-xe^{2x}$$

**$y'''-3y''+3y'-y=e^x$:** $r=1$ mult. 3 ($s=3$): $y_p=Ax^3e^x$. Using $y=e^xu$, $u'''=1 \Rightarrow u_p=x^3/6$.
$$y = (c_1+c_2x+c_3x^2)e^x+\tfrac{x^3}{6}e^x$$

**$y'''-y''+y'-y=\sin x$:** $y_c=c_1e^x+c_2\cos x+c_3\sin x$. $\sin x$ duplicates the $\pm i$ pair ($s=1$): $y_p=x(A\cos x+B\sin x)$. Solving: $A=\tfrac14,B=-\tfrac14$.
$$y = c_1e^x+c_2\cos x+c_3\sin x+\tfrac{x}{4}(\cos x-\sin x)$$

**$y^{(4)}-y=e^x$:** roots $1,-1,\pm i$; $1$ simple ($s=1$): $y_p=Axe^x$, $4A=1\Rightarrow A=\tfrac14$.
$$y = c_1e^x+c_2e^{-x}+c_3\cos x+c_4\sin x+\tfrac{x}{4}e^x$$

**$y^{(4)}-2y''+y=e^x$:** roots $\pm1$ each mult. 2; $1$ has $s=2$: $y_p=Ax^2e^x$, $8A=1\Rightarrow A=\tfrac18$.
$$y = (c_1+c_2x)e^x+(c_3+c_4x)e^{-x}+\tfrac18x^2e^x$$

**$y^{(4)}-2y''+y=xe^x$:** same $s=2$, but forcing is degree-1 poly $\times e^x$: $y_p=x^2(Ax+B)e^x$. Solving: $A=\tfrac1{24},B=-\tfrac18$.
$$y = (c_1+c_2x)e^x+(c_3+c_4x)e^{-x}+\frac{x^2(x-3)}{24}e^x$$

**$y'''+3y''+3y'+y=x+e^{-x}$:** $y_c=(c_1+c_2x+c_3x^2)e^{-x}$. Split $R$: for $R_1=x$ ($s=0$), $y_{p1}=x-3$; for $R_2=e^{-x}$ ($s=3$), $y_{p2}=\tfrac{x^3}{6}e^{-x}$.
$$y = (c_1+c_2x+c_3x^2)e^{-x}+x-3+\tfrac{x^3}{6}e^{-x}$$

**$y^{(4)}+4y=x$:** roots $\pm1\pm i$ (none 0), $s=0$: $y_p=Ax+B$, $A=\tfrac14,B=0$.
$$y = e^x(c_1\cos x+c_2\sin x)+e^{-x}(c_3\cos x+c_4\sin x)+\tfrac{x}{4}$$

---
Next: [[Variation of Parameters - 3rd Order]]

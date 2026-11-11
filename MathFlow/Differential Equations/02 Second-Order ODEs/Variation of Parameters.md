Related: [[Undetermined Coefficients]] · [[General Solution Structure Theorem]] · [[Variation of Parameters - 3rd Order]]

## Motivation

For $y''+P(x)y'+Q(x)y=R(x)$, [[Undetermined Coefficients]] only works for special forms of $R(x)$. **Variation of parameters** works for *any* continuous $R(x)$: $\tan x, \sec x, \ln x, 1/x$, etc. It only requires knowing $y_c = c_1y_1+c_2y_2$.

Idea: replace the constants $c_1,c_2$ by unknown functions $u_1(x),u_2(x)$, and seek $y_p = u_1(x)y_1(x)+u_2(x)y_2(x)$.

## Derivation

Let $y_1,y_2$ be a fundamental set of the homogeneous equation. Differentiating $y_p=u_1y_1+u_2y_2$:
$$y_p' = u_1'y_1+u_1y_1'+u_2'y_2+u_2y_2'$$
Impose the **constraint** $u_1'y_1+u_2'y_2=0$ (5) to avoid second derivatives of $u_1,u_2$ later, so $y_p'=u_1y_1'+u_2y_2'$. Differentiating again:
$$y_p'' = u_1'y_1'+u_1y_1''+u_2'y_2'+u_2y_2''$$
Substituting $y_p,y_p',y_p''$ into the ODE, the homogeneous parts vanish, leaving
$$u_1'y_1'+u_2'y_2' = R(x). \tag{6}$$
(5) and (6) form a $2\times2$ linear system in $u_1',u_2'$ whose determinant is the Wronskian $W(y_1,y_2)=y_1y_2'-y_2y_1'\ne0$. By Cramer's rule:
$$u_1' = \frac{-y_2R(x)}{W}, \qquad u_2' = \frac{y_1R(x)}{W}.$$

## Final Formulas

$$u_1(x) = -\int \frac{y_2(x)R(x)}{W(x)}dx, \qquad u_2(x) = \int \frac{y_1(x)R(x)}{W(x)}dx$$
$$y_p = y_1\int \frac{-y_2R}{W}dx + y_2\int \frac{y_1R}{W}dx$$
$$y = c_1y_1+c_2y_2+y_p$$

No arbitrary constants are kept in $u_1,u_2$ — they're absorbed into $y_p$.

## Worked Examples

**$y''+y=\tan x$, $-\tfrac\pi2<x<\tfrac\pi2$:** $y_1=\cos x, y_2=\sin x$, $W=1$.
$$u_1' = -\sin x\tan x = -\frac{\sin^2x}{\cos x} = -( \sec x-\cos x), \quad u_2'=\sin x$$
$u_2=-\cos x$; $u_1 = -\ln|\sec x+\tan x|+\sin x$.
$$y_p = \cos x(-\ln|\sec x+\tan x|+\sin x)+\sin x(-\cos x) = -\cos x\ln|\sec x+\tan x|$$
**GS:** $y = c_1\cos x+c_2\sin x-\cos x\ln|\sec x+\tan x|$.

**$y''-2y'+y=\dfrac{e^x}{x}$, $x>0$:** repeated root $r=1$; $y_1=e^x,y_2=xe^x$, $W=e^{2x}$.
$$u_1' = \frac{-xe^x\cdot(e^x/x)}{e^{2x}}=-1 \Rightarrow u_1=-x, \qquad u_2'=\frac1x \Rightarrow u_2=\ln x$$
$$y_p = e^x(-x)+xe^x\ln x = xe^x(\ln x-1)$$
**GS:** $y = c_1e^x+c_2xe^x+xe^x(\ln x-1)$. (This RHS is not UC-friendly, so variation of parameters is essential here.)

**$y''+4y=\sec2x$:** $y_1=\cos2x,y_2=\sin2x$, $W=2$.
$$u_1' = -\tfrac12\tan2x \Rightarrow u_1=\tfrac14\ln|\cos2x|, \qquad u_2'=\tfrac12\Rightarrow u_2=\tfrac{x}{2}$$
$$y_p = \tfrac14\cos2x\ln|\cos2x|+\tfrac{x}{2}\sin2x$$
**GS:** $y = c_1\cos2x+c_2\sin2x+\tfrac14\cos2x\ln|\cos2x|+\tfrac{x}{2}\sin2x$.

---
Next: [[Higher Order Homogeneous ODEs]]

Related: [[Reduction of Order]] · [[Undetermined Coefficients]] · [[Higher Order Homogeneous ODEs]]

Consider $y'' + ay' + by = 0$, $a,b\in\mathbb{R}$. Try $y=e^{rx}$: substituting gives $(r^2+ar+b)e^{rx}=0 \Rightarrow r^2+ar+b=0$, the **characteristic (auxiliary) equation**. Its roots $r_1,r_2$ determine the fundamental set. Three cases arise from the discriminant $a^2-4b$.

## Case 1: Distinct Real Roots ($a^2-4b>0$)

$y_1=e^{r_1x}, y_2=e^{r_2x}$. $W(y_1,y_2)(x)=(r_2-r_1)e^{(r_1+r_2)x}\ne0$ ⇒ independent.
$$y = c_1e^{r_1x}+c_2e^{r_2x}$$
(overdamped-type behaviour in applications).

## Case 2: Repeated Real Root ($a^2-4b=0$)

$r=r_1=r_2=-a/2$. $y_1=e^{rx}$; by [[Reduction of Order]], $y_2=xe^{rx}$. $W=e^{2rx}\ne0$.
$$y = c_1e^{rx}+c_2xe^{rx}$$
(critically damped case).

## Case 3: Complex Conjugate Roots ($a^2-4b<0$)

$r_{1,2}=\alpha\pm i\beta$, $\beta\ne0$. Real fundamental set: $y_1=e^{\alpha x}\cos\beta x$, $y_2=e^{\alpha x}\sin\beta x$. $W=\beta e^{2\alpha x}\ne0$.
$$y = e^{\alpha x}(c_1\cos\beta x+c_2\sin\beta x)$$
(underdamped/oscillatory case).

## Worked Examples

**$y''+4y=0$:** $r=\pm2i$. $y=c_1\cos2x+c_2\sin2x$.

**IVP $y''-5y'+6y=0$, $y(0)=1,y'(0)=0$:** $r=2,3$; $y=c_1e^{2x}+c_2e^{3x}$. From ICs: $c_1+c_2=1$, $2c_1+3c_2=0 \Rightarrow c_1=3,c_2=-2$.
$$y = 3e^{2x}-2e^{3x}$$

**IVP $y''-6y'+9y=0$, $y(0)=2,y'(0)=5$:** $r=3,3$ (repeated). $y=(C_1+C_2x)e^{3x}$, $y'=e^{3x}(3C_1+C_2+3C_2x)$. From ICs: $C_1=2$, $3C_1+C_2=5\Rightarrow C_2=-1$.
$$y_p(x) = (2-x)e^{3x}$$

---
Next: [[Undetermined Coefficients]]

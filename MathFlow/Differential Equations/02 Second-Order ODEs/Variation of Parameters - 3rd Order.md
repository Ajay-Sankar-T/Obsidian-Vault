Related: [[Variation of Parameters]] · [[Undetermined Coefficients - Higher Order]] · [[Higher Order Homogeneous ODEs]]

## Setup

Consider the third order linear non-homogeneous ODE (standard form)
$$y''' + p(x)y'' + q(x)y' + r(x)y = f(x).$$
Assume $y_c=C_1y_1+C_2y_2+C_3y_3$ is known, with $y_1,y_2,y_3$ linearly independent solutions of the homogeneous equation ($W(y_1,y_2,y_3)\ne0$). Seek
$$y_p = u_1(x)y_1+u_2(x)y_2+u_3(x)y_3.$$

## Imposing the Auxiliary Conditions

Differentiate $y_p$ once: $y_p' = (u_1'y_1+u_2'y_2+u_3'y_3)+(u_1y_1'+u_2y_2'+u_3y_3')$.

**Condition 1:** $u_1'y_1+u_2'y_2+u_3'y_3=0$, leaving $y_p'=u_1y_1'+u_2y_2'+u_3y_3'$.

Differentiate again: $y_p''=(u_1'y_1'+u_2'y_2'+u_3'y_3')+(u_1y_1''+u_2y_2''+u_3y_3'')$.

**Condition 2:** $u_1'y_1'+u_2'y_2'+u_3'y_3'=0$, leaving $y_p''=u_1y_1''+u_2y_2''+u_3y_3''$.

Differentiating once more and substituting $y_p,y_p',y_p'',y_p'''$ into the ODE, the homogeneous parts cancel (each $y_i$ solves $L[y_i]=0$), leaving exactly
$$u_1'y_1''+u_2'y_2''+u_3'y_3''=f(x).$$

## The Linear System

$$\begin{aligned}
u_1'y_1+u_2'y_2+u_3'y_3 &= 0\\
u_1'y_1'+u_2'y_2'+u_3'y_3' &= 0\\
u_1'y_1''+u_2'y_2''+u_3'y_3'' &= f(x)
\end{aligned}$$

The coefficient matrix is exactly the Wronskian matrix of $y_1,y_2,y_3$; since $W\ne0$ this system has a unique solution.

## Solving by Cramer's Rule

Let $W=W(y_1,y_2,y_3)$. Let $W_1,W_2,W_3$ be $W$ with the 1st/2nd/3rd column replaced by $(0,0,f(x))^T$. Then
$$u_1'=\frac{W_1}{W}, \quad u_2'=\frac{W_2}{W}, \quad u_3'=\frac{W_3}{W}$$
(each $W_i$ computed by expanding along the replaced column, since only the last entry is nonzero). Integrate (drop constants) to get $u_1,u_2,u_3$, then
$$y_p = u_1y_1+u_2y_2+u_3y_3, \qquad y=y_c+y_p.$$

## Worked Examples

**$y'''+y'=\sec x$ on $(-\tfrac\pi2,\tfrac\pi2)$:** AE $r(r^2+1)=0$; $y_c=C_1+C_2\cos x+C_3\sin x$. So $y_1=1,y_2=\cos x,y_3=\sin x$, $f=\sec x$. $W=1$.
- $W_1 = \sec x(\cos^2x+\sin^2x)=\sec x \Rightarrow u_1=\ln|\sec x+\tan x|$
- $W_2 = -\sec x\cos x=-1 \Rightarrow u_2=-x$
- $W_3 = -\sec x\sin x=-\tan x \Rightarrow u_3=\ln|\cos x|$

$$y = C_1+C_2\cos x+C_3\sin x+\ln|\sec x+\tan x|-x\cos x+\sin x\ln|\cos x|$$

**$y'''-3y''+3y'-y=\dfrac{e^x}{x^2}$, $x>0$:** AE $(r-1)^3=0$; $y_c=(C_1+C_2x+C_3x^2)e^x$. $y_1=e^x,y_2=xe^x,y_3=x^2e^x$, $f=e^x/x^2$. $W=2e^{3x}$.
- $W_1 = f\cdot x^2e^{2x}=e^{3x} \Rightarrow u_1'=\tfrac12 \Rightarrow u_1=\tfrac{x}{2}$
- $W_2 = -f\cdot2xe^{2x}=-\tfrac{2e^{3x}}{x} \Rightarrow u_2'=-\tfrac1x \Rightarrow u_2=-\ln x$
- $W_3 = f\cdot e^{2x}=\tfrac{e^{3x}}{x^2} \Rightarrow u_3'=\tfrac1{2x^2} \Rightarrow u_3=-\tfrac1{2x}$

$$y_p = \tfrac{x}{2}e^x + (-\ln x)(xe^x) + \left(-\tfrac1{2x}\right)(x^2e^x) = -xe^x\ln x$$
$$y = (C_1+C_2x+C_3x^2)e^x - xe^x\ln x$$

---
Related: [[Cauchy-Euler Equations]]

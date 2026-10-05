Related: [[2nd Order Linear ODE with Constant Coefficients]] · [[General Solution Structure Theorem]] · [[Variation of Parameters]]

## Goal

Find a particular solution $y_p$ of $y''+Py'+Qy=R(x)$ when $P,Q$ are constants. Applicable only when $R(x)$ is a polynomial, exponential, sine/cosine, or a product/sum of these.

**Idea:** Guess a trial form for $y_p$ with unknown coefficients matching the type of $R(x)$; substitute into the ODE and compare coefficients. Simpler than [[Variation of Parameters]] but restricted to these special forcing terms.

- If $R(x)=R_1(x)+R_2(x)$, solve separately for each and add (**superposition**).
- Modification is required if the trial form duplicates a term already in $y_c$.

## Table of standard trial forms for $y_p$

(assuming no duplication with $y_c$)

| $R(x)$ | Trial $y_p$ | Condition |
|---|---|---|
| $P_n(x)$ (degree $n$) | $A_nx^n+\cdots+A_0$ | 0 is not root of AE |
| $ae^{kx}$ | $Ae^{kx}$ | $k$ is not root of AE |
| $a\cos\beta x$ or $a\sin\beta x$ | $A\cos\beta x+B\sin\beta x$ | $i\beta$ is not root of AE |
| $P_n(x)e^{kx}$ | $(A_nx^n+\cdots+A_0)e^{kx}$ | $k$ is not root of AE |
| $e^{kx}(a\cos\beta x+b\sin\beta x)$ | $e^{kx}(A\cos\beta x+B\sin\beta x)$ | $k+i\beta$ is not root of AE |
| $P_n(x)e^{kx}\cos\beta x$ (or $\sin$) | $e^{kx}[(A_nx^n+\cdots)\cos\beta x+(B_nx^n+\cdots)\sin\beta x]$ | $k+i\beta$ is not root of AE |

## Modification rule

Let $s$ be the multiplicity of the exponent $k$ (or $k\pm i\beta$) as a root of the auxiliary equation (AE).

- $s=0$: no overlap; use the standard trial form.
- $s=1$: the standard form solves the homogeneous equation, so multiply by $x$: $y_p = xy_t$.
- $s=2$ (repeated root case): multiply by $x^2$: $y_p = x^2y_t$.

In general, multiply by $x^s$ so $y_p$ is not itself a solution of the homogeneous equation.

## Step-by-step procedure

1. Solve the homogeneous DE for $y_c$ (auxiliary equation, [[2nd Order Linear ODE with Constant Coefficients]]).
2. Choose trial form for $y_p$ based on $R(x)$'s type.
3. Check duplication with $y_c$; multiply by $x^s$ if needed.
4. Substitute $y_p$ into the ODE; equate coefficients of like terms.
5. Solve for the unknown coefficients.
6. Write $y = y_c+y_p$.

## Worked Examples

**$y''-3y'+2y=e^{3x}$:** roots $1,2$; $y_c=c_1e^x+c_2e^{2x}$. Since 3 is not a root ($s=0$), $y_p=Ae^{3x}$. Substituting: $9A-9A+2A=2A=1 \Rightarrow A=\tfrac12$.
$$y = c_1e^x+c_2e^{2x}+\tfrac12e^{3x}$$

**$y''-3y'+2y=e^{2x}$:** roots $1,2$; 2 is a simple root ($s=1$), $y_p=Axe^{2x}$. Gives $y_p'' -3y_p'+2y_p = Ae^{2x} = e^{2x} \Rightarrow A=1$.
$$y = c_1e^x+c_2e^{2x}+xe^{2x}$$

**$y''-4y'+4y=e^{2x}$:** repeated root $r=2$ ($s=2$), $y_p=Ax^2e^{2x}$. Gives $2Ae^{2x}=e^{2x}\Rightarrow A=\tfrac12$.
$$y = (c_1+c_2x)e^{2x}+\tfrac12x^2e^{2x}$$

**$y''+4y=3\sin2x$:** roots $\pm2i$; $y_c=c_1\cos2x+c_2\sin2x$. Since $\sin2x$ duplicates $y_c$ ($s=1$), $y_p=x(A\cos2x+B\sin2x)$. Matching gives $A=-\tfrac34, B=0$.
$$y = c_1\cos2x+c_2\sin2x-\tfrac34x\cos2x$$

**$y''+y'-2y=x^2$:** roots $-2,1$; $s=0$, $y_p=Ax^2+Bx+C$. Matching: $A=-\tfrac12,B=-\tfrac12,C=-\tfrac34$.
$$y = c_1e^{-2x}+c_2e^x-\tfrac12x^2-\tfrac12x-\tfrac34$$

**$y''-y=xe^x$:** roots $\pm1$; 1 is simple ($s=1$), $y_p=(Ax^2+Bx)e^x$. Matching gives $A=\tfrac14, B=-\tfrac14$.
$$y = c_1e^x+c_2e^{-x}+\frac{x^2-x}{4}e^x$$

**$y''+2y'+5y=e^{-x}\cos2x$:** roots $-1\pm2i$; duplicates $y_c$ ($s=1$), $y_p=xe^{-x}(A\cos2x+B\sin2x)$. Gives $A=0, B=\tfrac14$.
$$y = e^{-x}(c_1\cos2x+c_2\sin2x)+\frac{x}{4}e^{-x}\sin2x$$

**$y''-y'-2y=4x-5+6xe^{2x}$:** split $R=R_1+R_2$. For $R_1=4x-5$: $y_{p1}=Ax+B$, $A=-2,B=\tfrac72$. For $R_2=6xe^{2x}$ (2 is simple root, $s=1$): $y_{p2}=x(Cx+D)e^{2x}$, $C=1,D=-\tfrac23$.
$$y = c_1e^{2x}+c_2e^{-x}-2x+\tfrac72+\left(x^2-\tfrac23x\right)e^{2x}$$

---
Next: [[Variation of Parameters]]

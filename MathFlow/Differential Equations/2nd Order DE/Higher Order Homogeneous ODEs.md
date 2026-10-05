Related: [[Variation of Parameters]] · [[2nd Order Linear ODE with Constant Coefficients]] · [[Undetermined Coefficients - Higher Order]]

An $n$-th order linear homogeneous ODE with constant coefficients:
$$a_ny^{(n)}+a_{n-1}y^{(n-1)}+\cdots+a_1y'+a_0y=0, \quad a_n\ne0.$$
Try $y=e^{rx}$: substituting gives the **auxiliary/characteristic equation**
$$a_nr^n+a_{n-1}r^{n-1}+\cdots+a_1r+a_0=0,$$
a degree-$n$ polynomial with exactly $n$ roots (real or complex, with multiplicity). Each root determines one basis solution; together they span an $n$-dimensional solution space.

## Case 1: Distinct Real Roots

$r_1,\dots,r_n$ real and distinct ⇒ basis $e^{r_1x},\dots,e^{r_nx}$ (linearly independent, generalized Wronskian nonzero).
$$y = c_1e^{r_1x}+c_2e^{r_2x}+\cdots+c_ne^{r_nx}$$

## Case 2: Repeated Real Roots

A real root $r$ of multiplicity $m$ contributes $m$ independent solutions (via repeated [[Reduction of Order]]):
$$e^{rx},\ xe^{rx},\ x^2e^{rx},\ \dots,\ x^{m-1}e^{rx}$$
contributing $(c_1+c_2x+\cdots+c_mx^{m-1})e^{rx}$ to $y$.

## Case 3: Complex Roots

Since coefficients are real, complex roots occur in conjugate pairs $\alpha\pm i\beta$. Each simple pair contributes $e^{\alpha x}\cos\beta x,\ e^{\alpha x}\sin\beta x$. If repeated with multiplicity $m$, the pair contributes $2m$ solutions:
$$x^ke^{\alpha x}\cos\beta x, \quad x^ke^{\alpha x}\sin\beta x, \quad k=0,1,\dots,m-1.$$

## Fundamental Set and Generalized Wronskian

The solution space is $n$-dimensional. A set of $n$ linearly independent solutions $\{y_1,\dots,y_n\}$ is a fundamental set, verified by
$$W(y_1,\dots,y_n)(x) = \det\begin{pmatrix} y_1 & \cdots & y_n \\ y_1' & \cdots & y_n' \\ \vdots & & \vdots \\ y_1^{(n-1)} & \cdots & y_n^{(n-1)}\end{pmatrix} \ne 0.$$
General solution: $y = c_1y_1+\cdots+c_ny_n$.

## Step-by-step procedure

1. Write the auxiliary equation from the coefficients.
2. Solve for all roots and their multiplicities.
3. For each distinct real root: include $e^{rx}, xe^{rx},\dots$ up to its multiplicity.
4. For each conjugate complex pair: include $e^{\alpha x}\cos\beta x, e^{\alpha x}\sin\beta x,\dots$ up to its multiplicity.
5. Combine with arbitrary constants for the general solution.
6. Apply initial conditions if given.

## Worked Examples

**$y'''-6y''+11y'-6y=0$:** AE $r^3-6r^2+11r-6=0$; testing $r=1$ works, factor $(r-1)(r-2)(r-3)=0$. Roots $1,2,3$.
$$y = c_1e^x+c_2e^{2x}+c_3e^{3x}$$

**$y'''-3y''+3y'-y=0$:** AE $(r-1)^3=0$, root $r=1$ multiplicity 3.
$$y = (c_1+c_2x+c_3x^2)e^x$$

**$y'''-y''+y'-y=0$:** AE $r^2(r-1)+(r-1)=(r-1)(r^2+1)=0$. Roots $1,\pm i$.
$$y = c_1e^x+c_2\cos x+c_3\sin x$$

**$y^{(4)}-y=0$:** AE $(r-1)(r+1)(r-i)(r+i)=0$. Roots $\pm1,\pm i$.
$$y = c_1e^x+c_2e^{-x}+c_3\cos x+c_4\sin x$$

**$y^{(4)}+4y=0$:** AE $r^4=-4$; fourth roots give $r=\pm1\pm i$ (two conjugate pairs).
$$y = e^x(c_1\cos x+c_2\sin x)+e^{-x}(c_3\cos x+c_4\sin x)$$

**$y^{(4)}-2y''+y=0$:** AE $(r^2-1)^2=0$; $r=1,1,-1,-1$.
$$y = (c_1+c_2x)e^x+(c_3+c_4x)e^{-x}$$

**IVP $y'''+3y''+3y'+y=0$, $y(0)=1,y'(0)=-3,y''(0)=11$:** AE $(r+1)^3=0$, $r=-1$ (mult. 3). $y=(c_1+c_2x+c_3x^2)e^{-x}$. Solving: $c_1=1,c_2=-2,c_3=3$.
$$y = (1-2x+3x^2)e^{-x}$$

---
Next: [[Undetermined Coefficients - Higher Order]]

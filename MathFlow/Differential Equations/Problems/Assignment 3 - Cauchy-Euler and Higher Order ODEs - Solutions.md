---
title: Assignment 3 – Cauchy-Euler and Higher Order ODEs (Solutions)
course: MA 2102 Differential Equations
assignment: 3
tags:
  - DE
  - assignment-solution
  - cauchy-euler
  - higher-order
  - undetermined-coefficients
  - variation-of-parameters
source: "[[A3-2026.pdf]]"
aliases:
  - Assignment 3 solutions
---

# Assignment 3 – Cauchy-Euler and Higher Order ODEs

Source: [[A3-2026.pdf]] · Theory: [[Cauchy-Euler Equations]] · [[Non-homogeneous Cauchy-Euler Equations]] · [[Higher Order Homogeneous ODEs]] · [[Undetermined Coefficients - Higher Order]] · [[Variation of Parameters - 3rd Order]] · [[Variation of Parameters]] · [[Linear Independence and the Wronskian]] · [[Abel's Formula]] · [[2nd Order ODEs - MOC]] · Index: [[Problems - MOC]] · Previous: [[Assignment 2 - Second Order ODEs - Solutions]] · Next: [[Assignment 4 - Series Solutions - Solutions]]

> [!abstract] Contents
> [[#0. Theory toolkit]] · [[#Q1]] · [[#Q2]] · [[#Q3]] · [[#Q4]] · [[#Q5]] · [[#Q6]] · [[#Q7]] · [[#Q8]] · [[#Q9]] · [[#Q10]] · [[#Q11]] · [[#Q12]] · [[#Q13]] · [[#Summary]]

> [!warning] Corrections to the previous version
> Every answer was re-derived, checked symbolically (SymPy) and compared with a numerical ODE solve (see figures). Changes:
> - **11(c)** was wrong. Correct: $y_p=-\dfrac{x}{4}\big(\ln^2x+\ln x\big)$.
> - **8(b)**: the particular solution is $\dfrac x2+\dfrac32$. (Both the earlier note and the sheet's printed answer "$x^2+\frac32$" fail to satisfy the equation; the sheet's "$x^2$" is most likely the fraction $x/2$ read as $x^2$.)
> - **1(e) and 1(f)** are the same equation in the sheet (both $x^2y''+2xy'-6y=0$).
> - **Q13**: the sheet does not give boundary conditions, so only the general solution can be determined (details below).

---

## 0. Theory toolkit

### 0.1 Cauchy–Euler equations
$$ax^2y''+bxy'+cy=g(x),\qquad x>0\ (\text{use }|x|\text{ for }x<0).$$
Substituting $x=e^t$ ($t=\ln x$) and writing $\theta=\dfrac d{dt}$:

$$xy'=\theta y,\qquad x^2y''=\theta(\theta-1)y,\qquad x^3y'''=\theta(\theta-1)(\theta-2)y$$

so the equation becomes a **constant-coefficient** equation in $t$. Trying $y=x^m$ gives the **indicial (auxiliary) equation** directly:
$$am(m-1)+bm+c=0.$$

| Roots of the indicial equation | Solution (for $x>0$) |
|---|---|
| real distinct $m_1,m_2$ | $c_1x^{m_1}+c_2x^{m_2}$ |
| real double $m$ | $x^m(c_1+c_2\ln x)$ |
| complex $\alpha\pm i\beta$ | $x^{\alpha}\big[c_1\cos(\beta\ln x)+c_2\sin(\beta\ln x)\big]$ |
| $m$ of multiplicity $k$ | $x^m\,(c_1+c_2\ln x+\dots+c_k\ln^{k-1}x)$ |

![[A3-fig1-euler-types.png]]

### 0.2 Non-homogeneous Euler equations
Either transform to $t=\ln x$ and use undetermined coefficients (UC) with forcing $g(e^t)$, or use variation of parameters (VOP) in $x$ with $y_1,y_2$ from the table, **after dividing by the leading coefficient**.

### 0.3 Shifted Euler equations
$b_0(ax+b)^2y''+b_1(ax+b)y'+b_2y=0$: with $t=ax+b$ we have $y_x=ay_t$, $y_{xx}=a^2y_{tt}$, so it becomes $b_0a^2t^2y_{tt}+b_1a\,ty_t+b_2y=0$, a Cauchy–Euler equation in $t$ (Q4).

### 0.4 Constant-coefficient higher order
$p(D)y=g$, with $p(D)=\prod(D-r_j)^{k_j}$. UC: $y_p=x^s\cdot(\text{form of }g)$, with $s$ the multiplicity of the exponent. **Shift rule:** $p(D)\big(e^{\alpha x}u\big)=e^{\alpha x}p(D+\alpha)u$. For a simple root with $g=Ae^{\alpha x}$: $y_p=\dfrac{A}{p'(\alpha)}x\,e^{\alpha x}$; for non-resonant $g=Ae^{\alpha x}$: $y_p=\dfrac{A}{p(\alpha)}e^{\alpha x}$.

### 0.5 Reduction of the order
If the equation contains $y$ only through derivatives (or is Euler type in $y'$), put $p=y'$.

### 0.6 Wronskian facts
Abel: $W=W(x_0)\exp\!\big(-\!\int P\big)$ for $y''+Py'+Qy=0$ (Q6, Q7).

---

## Q1

> [!question] General solution of the Cauchy–Euler equations (a)–(h).

Indicial equation $am(m-1)+bm+c=0$, i.e. $m^2+\dfrac{b-a}{a}m+\dfrac ca=0$:

| | Equation | Indicial equation | Roots | General solution ($x>0$) |
|---|---|---|---|---|
| (a) | $x^2y''+3xy'+10y=0$ | $m^2+2m+10=0$ | $-1\pm3i$ | $x^{-1}\big[c_1\cos(3\ln x)+c_2\sin(3\ln x)\big]$ |
| (b) | $2x^2y''+10xy'+8y=0$ | $m^2+4m+4=0$ | $-2$ (double) | $x^{-2}(c_1+c_2\ln x)$ |
| (c) | $x^2y''+2xy'-12y=0$ | $m^2+m-12=(m+4)(m-3)$ | $3,\,-4$ | $c_1x^3+c_2x^{-4}$ |
| (d) | $4x^2y''-3y=0$ | $4m^2-4m-3=(2m-3)(2m+1)$ | $\frac32,\,-\frac12$ | $c_1x^{3/2}+c_2x^{-1/2}$ |
| (e),(f) | $x^2y''+2xy'-6y=0$ | $m^2+m-6=(m+3)(m-2)$ | $2,\,-3$ | $c_1x^2+c_2x^{-3}$ |
| (g) | $x^2y''+xy'-2y=0$ | $m^2-2=0$ | $\pm\sqrt2$ | $c_1x^{\sqrt2}+c_2x^{-\sqrt2}$ |
| (h) | $x^2y''+xy'-16y=0$ | $m^2-16=0$ | $\pm4$ | $c_1x^4+c_2x^{-4}$ |

![[A3-fig2-q1.png]]

---

## Q2

> [!question] IVPs.

**(a)** $x^2y''+xy'+y=0$: $m^2+1=0$, $m=\pm i$, $y=c_1\cos\ln x+c_2\sin\ln x$. $y(1)=c_1=1$; $y'=\dfrac{-c_1\sin\ln x+c_2\cos\ln x}{x}$, so $y'(1)=c_2=1$.
$$\boxed{y=\cos(\ln x)+\sin(\ln x)}$$
**(b)** $4x^2y''+12xy'+3y=0$: $4m^2+8m+3=(2m+1)(2m+3)$, $m=-\frac12,-\frac32$. $y=c_1x^{-1/2}+c_2x^{-3/2}$: $c_1+c_2=1$ and $-\frac{c_1}2-\frac{3c_2}2=\frac32$ give $c_2=-2$, $c_1=3$.
$$\boxed{y=3x^{-1/2}-2x^{-3/2}}$$

---

## Q3

> [!question] Solve the non-homogeneous equations (substitution $x=e^t$ suggested).

| | $t$-equation / method | $y_p$ |
|---|---|---|
| (a) | $\ddot y-4\dot y+4y=2e^{2t}$, double root 2: $y_p=At^2e^{2t}$, $2A=2$ | $x^2\ln^2x$ |
| (b) | $\ddot y+\dot y-y=3e^{3t}\cos t$: $y_p=e^{3t}(A\cos t+B\sin t)$ gives $10A+7B=3,\ 10B-7A=0$ | $\dfrac{x^3}{149}\big[30\cos\ln x+21\sin\ln x\big]$ |
| (c) | $x^2y''+5xy'+3y=x^2e^{-x}$; VOP with $y_1=x^{-1},y_2=x^{-3}$, $W=-2x^{-5}$ | $\dfrac{e^{-x}(x^3+5x^2+12x+12)}{x^3}$ |
| (d) | VOP with $y_1=x^{-1},y_2=x^{-1}\ln x$, $W=x^{-3}$ | $\dfrac1x\ln\dfrac{x}{1-x}$ |
| (e) | $x^2y''+xy'=12\ln x\Rightarrow\ddot y=12t$ | $2\ln^3x$ |
| (f) | $s=\ln(2+x)$: $\ddot y+4y=2\sin2s$, resonance: $y_p=As\cos2s$, $-4A=2$ | $-\frac12\ln(2+x)\cos[2\ln(2+x)]$ |
| (g) | $t=5+2x$: $t^2y_{tt}+3ty_t+2y=2t^2$; $m=-1\pm i$; $y_p=At^2$, $10A=2$ | $\dfrac{(5+2x)^2}5$ |
| (h) | $t=x+a$: $t^2y''-4ty'+6y=t-a$; $m=2,3$; $y_p=\alpha t+\beta$: $2\alpha=1$, $6\beta=-a$ | $\dfrac{x+a}2-\dfrac a6$ |

**Details**

- **(b)** $m^2+m-1=0\Rightarrow m=\frac{-1\pm\sqrt5}2$. With $e^{3t}$: $\big((D+3)^2+(D+3)-1\big)=D^2+7D+11$ acting on $A\cos t+B\sin t$: $(10A+7B)\cos t+(10B-7A)\sin t=3\cos t$, so $A=\frac{30}{149}$, $B=\frac{21}{149}$.
- **(c)** $u_1'=\dfrac{x^2e^{-x}}2$, $u_2'=-\dfrac{x^4e^{-x}}2$; $u_1=-\frac12e^{-x}(x^2+2x+2)$, $u_2=\frac12e^{-x}(x^4+4x^3+12x^2+24x+24)$; $y_p=u_1x^{-1}+u_2x^{-3}$.
- **(d)** $u_1'=-\dfrac{\ln x}{(1-x)^2}$, $u_2'=\dfrac1{(1-x)^2}$; $u_2=\dfrac1{1-x}$, $u_1=-\dfrac{x\ln x}{1-x}-\ln(1-x)$, so $y_p=\dfrac{\ln x-\ln(1-x)}x$ (for $0<x<1$).

**General solutions** ($y=y_c+y_p$):

| | General solution |
|---|---|
| (a) | $x^2\big[c_1+c_2\ln x+\ln^2x\big]$ |
| (b) | $c_1x^{(-1+\sqrt5)/2}+c_2x^{(-1-\sqrt5)/2}+\dfrac{x^3}{149}\big[30\cos\ln x+21\sin\ln x\big]$ |
| (c) | $c_1x^{-1}+c_2x^{-3}+\dfrac{e^{-x}(x^3+5x^2+12x+12)}{x^3}$ |
| (d) | $(c_1+c_2\ln x)x^{-1}+x^{-1}\ln\dfrac x{1-x}$ |
| (e) | $c_1+c_2\ln x+2\ln^3x$ |
| (f) | $c_1\cos[2\ln(2+x)]+c_2\sin[2\ln(2+x)]-\frac12\ln(2+x)\cos[2\ln(2+x)]$ |
| (g) | $(5+2x)^{-1}\big[c_1\cos\ln(5+2x)+c_2\sin\ln(5+2x)\big]+\frac15(5+2x)^2$ |
| (h) | $c_1(x+a)^2+c_2(x+a)^3+\frac{x+a}2-\frac a6$ |

![[A3-fig4-q3.png]]

---

## Q4

> [!question] Show $t=ax+b$ turns $b_0(ax+b)^2y''+b_1(ax+b)y'+b_2y=0$ into a Cauchy–Euler equation; solve $(x-3)^2y''+3(x-3)y'+y=0$, $x>3$.

By the chain rule $\dfrac{dy}{dx}=a\dfrac{dy}{dt}$, $\dfrac{d^2y}{dx^2}=a^2\dfrac{d^2y}{dt^2}$, so the equation becomes
$$b_0a^2\,t^2y_{tt}+b_1a\,t\,y_t+b_2y=0,$$
which is Cauchy–Euler in $t$. ∎

For $(x-3)^2y''+3(x-3)y'+y=0$ take $t=x-3>0$ ($a=1$): $t^2y_{tt}+3ty_t+y=0$, $m^2+2m+1=(m+1)^2=0$, so
$$\boxed{y=\big[c_1+c_2\ln(x-3)\big](x-3)^{-1}}$$

---

## Q5

> [!question] Find a second-order homogeneous ODE with the given solutions, check independence via $W$, solve the IVPs.

For a Cauchy–Euler equation $x^2y''+bxy'+cy=0$ with roots $m_1,m_2$: $m^2+(b-1)m+c=(m-m_1)(m-m_2)$.

| | Solutions | $m$ | ODE | $W$ | IVP solution |
|---|---|---|---|---|---|
| (a) | $x^2,\ x^2\ln x$ | $2,2$ | $x^2y''-3xy'+4y=0$ | $x^3\ne0$ | $y(1)=4,\ y'(1)=6$: $c_1=4,\ c_2=-2$, $\ y=4x^2-2x^2\ln x$ |
| (b) | $x^2\cos\ln x,\ x^2\sin\ln x$ | $2\pm i$ | $x^2y''-3xy'+5y=0$ | $x^3\ne0$ | $y(1)=3,\ y'(1)=8$: $c_1=3,\ c_2=2$, $\ y=3x^2\cos\ln x+2x^2\sin\ln x$ |
| (c) | $x^{-1},\ x^3$ | $-1,3$ | $x^2y''-xy'-3y=0$ | $4x\ne0$ | $y(2)=-1,\ y'(2)=1$: $c_1=-\frac52,\ c_2=\frac1{32}$, $\ y=-\dfrac5{2x}+\dfrac{x^3}{32}$ |

Wronskians: (a) $x^2\cdot(2x\ln x+x)-x^2\ln x\cdot2x=x^3$; (c) $x^{-1}\cdot3x^2-x^3\cdot(-x^{-2})=4x$.

**IVP constants.** (a) $y'(1)=2c_1+c_2=6$. (b) $y'(1)=2c_1+c_2=8$. (c) $\frac{c_1}2+8c_2=-1$, $-\frac{c_1}4+12c_2=1$.

![[A3-fig3-ivps.png]]

---

## Q6

> [!question] $y''+2xy'+e^x\sin x\,y=0$, $y_1(0)=2$, $y_2(0)=-3$, $y_1'(0)=1$, $y_2'(0)=2$. Find $W(y_1,y_2)$ and discuss independence.

$W(0)=y_1(0)y_2'(0)-y_2(0)y_1'(0)=2\cdot2-(-3)\cdot1=7$. With $P=2x$, Abel's formula gives
$$W(x)=7\exp\!\Big(-\!\int_0^x2t\,dt\Big)=\boxed{7e^{-x^2}}.$$
Since $W(x)>0$ for every $x$, $y_1$ and $y_2$ are **linearly independent on $\mathbb R$** (a fundamental set).

---

## Q7

> [!question] $W$ for $x^2y''-x(x+2)y'+(x+2)y=0$, $x>0$, without solving.

Standard form: $P=-\dfrac{x+2}x=-1-\dfrac2x$. Abel:
$$W=C\,e^{-\int P\,dx}=C\exp\!\Big(\!\int\big(1+\tfrac2x\big)dx\Big)=\boxed{C\,x^2e^x}.$$
*Check:* the equation has the solutions $y_1=x$ and $y_2=xe^x$, whose Wronskian is $x(e^x+xe^x)-xe^x=x^2e^x$ ($C=1$) ✔.

![[A3-fig5-wronskians.png]]

---

## Q8

> [!question] Variation of parameters.

**(a)** $x^2y''+xy'-y=x^2e^{-x}$. Roots $\pm1$: $y_1=x$, $y_2=x^{-1}$, $W=-\frac2x$; standard form $g=e^{-x}$.
$u_1'=-\dfrac{y_2g}W=\dfrac{e^{-x}}2\Rightarrow u_1=-\dfrac{e^{-x}}2$; $\ u_2'=\dfrac{y_1g}W=-\dfrac{x^2e^{-x}}2\Rightarrow u_2=\dfrac{e^{-x}}2(x^2+2x+2)$.
$$y_p=u_1x+\frac{u_2}x=e^{-x}\frac{x+1}x\ \Rightarrow\ \boxed{y=c_1x+\frac{c_2}x+e^{-x}\Big(1+\frac1x\Big)}$$
**(b)** $(x-3)^2y''+(x-3)y'+y=x$. With $t=x-3$ (so $x=t+3$) and $s=\ln t$: $t^2y''+ty'+y=t+3$. $y_1=\cos s$, $y_2=\sin s$, $W=\frac1t$, $g=\frac{t+3}{t^2}$:
$u_1'=-\dfrac{\sin s\,(t+3)}t$, $u_2'=\dfrac{\cos s\,(t+3)}t$. With $dt/t=ds$: $u_1=-\frac{e^s}2(\sin s-\cos s)+3\cos s$, $u_2=\frac{e^s}2(\sin s+\cos s)+3\sin s$, and
$$y_p=u_1\cos s+u_2\sin s=\tfrac{e^s}2+3=\tfrac t2+3=\tfrac x2+\tfrac32.$$
$$\boxed{y=c_1\cos[\ln(x-3)]+c_2\sin[\ln(x-3)]+\frac x2+\frac32}$$
> [!warning] The sheet's printed answer ($x^2+\frac32$) does not satisfy the equation: substituting it leaves $5x^2-19x+\frac{39}2\neq x$. The correct particular solution is $\frac x2+\frac32$ (verified).

![[A3-fig6-q8.png]]

---

## Q9

> [!question] General solution by undetermined coefficients.

| | Characteristic polynomial and roots | $y_p$ | How |
|---|---|---|---|
| (a) | $(r-1)(r^2-2r+2)$: $1,\ 1\pm i$ | $-\frac12x^3-3x^2-\frac{13}2x-\frac{11}2$ | $-2A=1$, $12A-2B=0$, $-18A+8B-2C=-2$, $6A-6B+4C-2D=0$ |
| (b) | $(r+1)(r^2-r+1)$: $-1,\ \frac12\pm\frac{\sqrt3}2i$ | $\frac43xe^{-x}$ | simple root: $A=4/p'(-1)=4/3$ |
| (c) | $(r+1)^4$ | $\frac{x^6}{360}e^{-x}$ | shift: $D^4u=x^2$ |
| (d) | $r^4-1$: $\pm1,\pm i$ | $2x\cos x$ | resonance with $i$: $p'(i)=-4i$ |
| (e) | $(r^2+1)(r^2+4)$ | $\frac1{40}\cos3x$ | $p(3i)=81-45+4=40$ |
| (f) | $(r^2+a^2)^2$ | $-\dfrac{x^3}{24a^2}\sin ax-\dfrac{x^2}{8a^3}\cos ax$ | shift $e^{iax}$: $D^2(D+2ia)^2u=x$ |
| (g) | $(r+1)^2(r^2+1)$ | $e^{-x}\big(\frac{x^3}{12}+\frac{x^2}4\big)$ | shift: $D^2(D^2-2D+2)u=x$ |
| (h) | $(r-1)^2(r^2+4r+5)$: $1,1,-2\pm i$ | $\frac{x-1}{16}\cos x-\big(\frac x{16}+\frac3{32}\big)\sin x$ | complex $p(i)=8-8i$, $p'(i)=-12-8i$ |
| (i) | $(r-2)(r+1)^3$ | $\frac{2x}{27}e^{2x}$ | simple root: $2/p'(2)=2/27$ |
| (j) | $r(r^2+2r-1)$: $0,\ -1\pm\sqrt2$ | $-x^3-5x^2-27x$ | $y_p=x(Ax^2+Bx+C)$: $A=-1$, $B=-5$, $C=-27$ |
| (k) | $r(r-1)(r-2)$ | $5x+7e^{3x}$ | $10$: $2A=10$; $42e^{3x}$: $42/p(3)=7$ |
| (l) | $(r-1)(r-2)(r-3)$ | $-3xe^{2x}$ | $3/p'(2)=3/(-1)$ |

**Details**

- **(f)** With $y=e^{iax}u$, $p(D+ia)=\big((D+ia)^2+a^2\big)^2=D^2(D+2ia)^2$. $D^2(D^2+4iaD-4a^2)u=x$; put $w=u''=\alpha x+\beta$: $-4a^2\alpha=1$, $4ia\alpha-4a^2\beta=0$, so $w=-\dfrac x{4a^2}-\dfrac i{4a^3}$ and $u=-\dfrac{x^3}{24a^2}-\dfrac{ix^2}{8a^3}$; take the imaginary part of $e^{iax}u$.
- **(h)** $y=e^{ix}u$: $u=\alpha x+\beta$ with $\alpha=\dfrac1{p(i)}=\dfrac{1+i}{16}$, $\beta=-\dfrac{p'(i)}{p(i)^2}=\dfrac{-2+3i}{32}$; take the real part of $e^{ix}u$.
- **(d)** $y^{(4)}-y=8\sin x=\operatorname{Im}8e^{ix}$; $y_p=\operatorname{Im}\dfrac{8xe^{ix}}{p'(i)}=\operatorname{Im}(2ixe^{ix})=2x\cos x$.

**General solutions** $y=y_c+y_p$:

$$\begin{aligned}
&\text{(a) }c_1e^x+e^x(c_2\cos x+c_3\sin x)+y_p &&\text{(b) }c_1e^{-x}+e^{x/2}\!\big(c_2\cos\tfrac{\sqrt3}2x+c_3\sin\tfrac{\sqrt3}2x\big)+\tfrac43xe^{-x}\\
&\text{(c) }(c_1+c_2x+c_3x^2+c_4x^3)e^{-x}+\tfrac{x^6}{360}e^{-x} &&\text{(d) }c_1e^x+c_2e^{-x}+c_3\cos x+c_4\sin x+2x\cos x\\
&\text{(e) }c_1\cos x+c_2\sin x+c_3\cos2x+c_4\sin2x+\tfrac1{40}\cos3x &&\text{(f) }(c_1+c_2x)\cos ax+(c_3+c_4x)\sin ax+y_p\\
&\text{(g) }(c_1+c_2x)e^{-x}+c_3\cos x+c_4\sin x+y_p &&\text{(h) }(c_1+c_2x)e^x+e^{-2x}(c_3\cos x+c_4\sin x)+y_p\\
&\text{(i) }c_1e^{2x}+(c_2+c_3x+c_4x^2)e^{-x}+\tfrac{2x}{27}e^{2x} &&\text{(j) }c_1+c_2e^{(-1+\sqrt2)x}+c_3e^{(-1-\sqrt2)x}-x^3-5x^2-27x\\
&\text{(k) }c_1+c_2e^x+c_3e^{2x}+5x+7e^{3x} &&\text{(l) }c_1e^x+c_2e^{2x}+c_3e^{3x}-3xe^{2x}
\end{aligned}$$

![[A3-fig7-q9.png]]

---

## Q10

> [!question] Third-order Cauchy–Euler, homogeneous.

Indicial equation for $x^3y'''+a_2x^2y''+a_1xy'+a_0y=0$: $m(m-1)(m-2)+a_2m(m-1)+a_1m+a_0=0$.

| | Indicial equation | Roots | Solution |
|---|---|---|---|
| (a) $x^3y'''+3x^2y''=0$ | $m(m-1)(m+1)$ | $0,1,-1$ | $c_1+c_2x+\dfrac{c_3}x$ |
| (b) $x^3y'''+2x^2y''+xy'-y=0$ | $m^3-m^2+m-1=(m-1)(m^2+1)$ | $1,\pm i$ | $c_1x+c_2\cos\ln x+c_3\sin\ln x$ |
| (c) $x^3y'''+x^2y''-2xy'+2y=0$ | $m^3-2m^2-m+2=(m-1)(m-2)(m+1)$ | $1,2,-1$ | $c_1x+c_2x^2+\dfrac{c_3}x$ |
| (d) $x^2y'''+3xy''-2y'=0$ | $p=y'$: $m^2+2m-2=0$ | $-1\pm\sqrt3$ | $c_1x^{\sqrt3}+c_2x^{-\sqrt3}+c_3$ |

**(d)** The equation involves only $y',y'',y'''$, so with $p=y'$ it is the second-order Euler equation $x^2p''+3xp'-2p=0$: $p=C_1x^{-1+\sqrt3}+C_2x^{-1-\sqrt3}$. Integrating, $y=\dfrac{C_1}{\sqrt3}x^{\sqrt3}-\dfrac{C_2}{\sqrt3}x^{-\sqrt3}+c_3$.

---

## Q11

> [!question] Non-homogeneous Euler equations (third order) and a constant-coefficient one.

Work in $t=\ln x$, with $\theta=d/dt$.

| | Operator in $t$ | $y_p$ |
|---|---|---|
| (a) | $(\theta-1)(\theta-2)(\theta+1)y=e^{-2t}$; $p(-2)=-12$ | $-\dfrac1{12x^2}$ |
| (b) | $4\theta(\theta-1)(\theta-2)+3\theta-3=(\theta-1)(2\theta-1)(2\theta-3)$; constant forcing: $-3A=10$ | $-\dfrac{10}3$ |
| (c) | $(\theta-1)(\theta-2)(\theta+1)y=te^t$ (resonance, simple root 1) | $-\dfrac x4(\ln^2x+\ln x)$ |
| (d) | $y=e^xu$: $D^3u=x^{1/2}$ | $\dfrac8{105}x^{7/2}e^x$ |

**(c) in detail.** With $y=e^tu$: $p(\theta+1)=\theta(\theta-1)(\theta+2)$, so $\theta(\theta-1)(\theta+2)u=t$. Put $w=u'$: $w''+w'-2w=t$, $w=\alpha t+\beta$, $-2\alpha=1$, $\alpha-2\beta=0$, so $w=-\dfrac t2-\dfrac14$ and $u=-\dfrac{t^2}4-\dfrac t4$. Hence $y_p=-\dfrac x4\,(\ln^2x+\ln x)$.

> [!warning] The earlier answer for 11(c) ($-\frac34x\ln^2x-\frac14x\ln x-\frac38x$) fails the equation (its residual is $x(2\ln x-1)\neq0$).

**General solutions**

| | General solution |
|---|---|
| (a) | $c_1x+c_2x^2+\dfrac{c_3}x-\dfrac1{12x^2}$ |
| (b) | $c_1x+c_2x^{1/2}+c_3x^{3/2}-\dfrac{10}3$ |
| (c) | $c_1x+c_2x^2+\dfrac{c_3}x-\dfrac x4\big(\ln^2x+\ln x\big)$ |
| (d) | $(c_1+c_2x+c_3x^2)e^x+\dfrac8{105}x^{7/2}e^x$ |

![[A3-fig8-q10-11.png]]

---

## Q12

> [!question] IVPs.

| | Roots / structure | $y_p$ | Initial conditions ⇒ constants | Solution |
|---|---|---|---|---|
| (a) | $\pm1,\pm2$ | $\dfrac{10}{p(-3)}e^{-3x}$, $p(-3)=40$: $\frac14e^{-3x}$ | $y(0)=1,\ y'=y''=y'''=0$: $c_1=\frac14,\ c_2=\frac32,\ c_3=0,\ c_4=-1$ | $y=\frac14e^x+\frac32e^{-x}-e^{-2x}+\frac14e^{-3x}$ |
| (b) | $\pm i,\pm2i$ | $\dfrac{90}{p}\sin4x$ with $p=256-80+4=180$: $\frac12\sin4x$ | $c_1=1,\ c_2=c_3=c_4=0$ | $y=\cos x+\frac12\sin4x$ |
| (c) | $(\theta-1)^3$ | $x^2$ ($p(2)=1$) | $c_1=0,\ c_2=1,\ c_3=\frac{11}2$ | $y=x\ln x+\frac{11}2x\ln^2x+x^2$ |
| (d) | $0,\pm2$ | $\cos x-2\sin x$ | $c_1=2,\ c_2=c_3=0$ | $y=2+\cos x-2\sin x$ |
| (e) | $(D+1)^3$ | $-2\cos x-2\sin x$ | $c_1=1,\ c_2=0,\ c_3=1$ | $y=(1+x^2)e^{-x}-2\cos x-2\sin x$ |

**Details**

- **(c)** $y=x(c_1+c_2L+c_3L^2)+x^2$, $L=\ln x$. $y(1)=c_1+1=1$; $y'(1)=c_2+2=3$; $y''(1)=c_2+2c_3+2=14\Rightarrow c_3=\frac{11}2$.
- **(d)** $y_p=A\cos x+B\sin x$: $(D^3-4D)y_p=5A\sin x-5B\cos x=10\cos x+5\sin x\Rightarrow A=1,\ B=-2$. $y(0)=c_1+c_2+c_3+1=3$, $y'(0)=2c_2-2c_3-2=-2$, $y''(0)=4c_2+4c_3-1=-1$.
- **(e)** $p(D)=(D+1)^3$, $p(i)=(1+i)^3=-2+2i$; $\operatorname{Im}\dfrac{8e^{ix}}{-2+2i}=-2\cos x-2\sin x$.

![[A3-fig9-q12.png]]

---

## Q13

> [!question] $x^3y^{(4)}+8x^2y'''+8xy''-8y'=0$ (drag on a small sphere).

The unknown appears only through $y'$; put $p=y'$:
$$x^3p'''+8x^2p''+8xp'-8p=0.$$
Indicial equation: $m(m-1)(m-2)+8m(m-1)+8m-8=m^3+5m^2+2m-8=(m-1)(m+2)(m+4)=0$, so $m=1,\,-2,\,-4$.
$$p=y'=C_1x+C_2x^{-2}+C_3x^{-4}\ \Longrightarrow\ \boxed{y=c_1x^2+\frac{c_2}x+\frac{c_3}{x^3}+c_4}$$

> [!note] About "compute the drag"
> The sheet states no boundary conditions (no-slip on the sphere, behaviour far away), and the physical meaning of $y(x)$ is not specified, so the **drag itself cannot be computed from the given data**. What the ODE determines is the four-parameter family above. In a typical setting the constants are fixed by requiring a bounded (decaying) field at infinity and a prescribed value at the sphere's surface, and the drag is then read off from the coefficient of the slowest-decaying term. I verified the general solution (residual $=0$).

![[A3-fig10-q13.png]]

---

## Summary

> [!success] Verification
> Each result was checked by (i) symbolic substitution, and (ii) comparison with a numerical integration of the ODE (the figures). The only discrepancies were in **11(c)** (previous answer wrong), **8(b)** (statement of the answer), and the printed answer to 8(b) in the sheet.

### Quick revision
- [ ] Euler: $x^m$ ⇒ indicial equation; $x=e^t$ turns it into constant coefficients
- [ ] Repeated root ⇒ $\ln x$ factors; complex root ⇒ $\cos(\beta\ln x)$, $\sin(\beta\ln x)$
- [ ] Shifted Euler: $t=ax+b$
- [ ] UC multiplier $x^s$; simple-root formula $A/p'(\alpha)$; non-resonant $A/p(\alpha)$; complex forcing via $e^{i\omega x}$
- [ ] Equations in $y',y'',\dots$ only: set $p=y'$
- [ ] Abel's formula gives $W$ without solving

### Figure index
`A3-fig1` Euler types · `fig2` Q1 · `fig3` IVPs (Q2, Q5) · `fig4` Q3 · `fig5` Wronskians (Q4, Q6, Q7) · `fig6` Q8 · `fig7` Q9 · `fig8` Q10–Q11 · `fig9` Q12 · `fig10` Q13. All in the `assets` folder.

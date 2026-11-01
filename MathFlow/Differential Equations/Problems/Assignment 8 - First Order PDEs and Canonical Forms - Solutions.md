---
title: Assignment 8 – First Order PDEs and Canonical Forms (Solutions)
course: MA 2102 Differential Equations
assignment: 8
tags:
  - DE
  - assignment-solution
  - pdes
  - first-order-pde
  - lagrange-method
  - characteristics
  - canonical-form
source: "[[A8-2026.pdf]]"
concepts:
  - "[[Formation of PDEs - Eliminating Constants and Functions]]"
  - "[[Lagrange's Method for Quasi-linear PDEs]]"
  - "[[Cauchy Problem for First Order PDEs]]"
  - "[[Classification of Second Order PDEs]]"
  - "[[Canonical Forms of Second Order PDEs]]"
aliases:
  - First order PDE assignment solutions
  - Assignment 8 solutions
---

# Assignment 8 – First Order PDEs and Canonical Forms

Source: [[A8-2026.pdf]] · Theory: [[PDEs - MOC]] · Previous: [[Assignment 7 - Sturm-Liouville Problems - Solutions]] · Next: [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]] · Index: [[Problems - MOC]]

> [!abstract] Contents
> [[#Q1]] · [[#Q2]] · [[#Q3]] · [[#Q4]] · [[#Q5]] · [[#Q6]] · [[#Summary]]

> [!info] Concept notes for this sheet
> | Questions | Concept note |
> |---|---|
> | Q1 | [[Formation of PDEs - Eliminating Constants and Functions]] |
> | Q2, Q3 | [[Lagrange's Method for Quasi-linear PDEs]] · [[Cauchy Problem for First Order PDEs]] (Q3, Q6(b),(c)) |
> | Q6(a) | [[Complete, General and Singular Integrals]] |
> | Q4, Q6(e) | [[Classification of Second Order PDEs]] |
> | Q5, Q6(f)–(i) | [[Canonical Forms of Second Order PDEs]] |

> [!warning] Points where the sheet needs care
> Every closed form below was verified symbolically (`Tools/de_a8_first_order.py`, `de_a8_second_order.py`, `de_a8_solutions_check.py`).
> - **Q2(g)** is printed "$xup+yup=xy$". It is solved as printed, and also in the likely intended form $xup+yuq=xy$ (the printed form has no $q$, so it is only an ODE in $x$).
> - **Q3(q)** is a statement about existence, not a computation: see the geometric discussion.
> - **Q5 (b), (c), (d), (e), (x), (y)** reduce to canonical forms with variable first-order terms (Euler–Poisson–Darboux type). They have no elementary general solution, so "find the general solution if possible" means: not possible in closed form.
> - **Q5(h)** has $u_x/x$ and $u_y/y$ terms, which make the canonical form integrable ($u_{\eta\eta}-u_\eta/\eta=0$).

---

## Q1

> [!question] Form the PDE by eliminating the arbitrary constants or functions.

Use [[Formation of PDEs - Eliminating Constants and Functions]]: differentiate, eliminate. With $p=u_x$, $q=u_y$.

| | Relation | Work | PDE |
|---|---|---|---|
| (a) | $u=(x^2+a)(y^2+b)$ | $p=2x(y^2+b)$, $q=2y(x^2+a)$, so $pq=4xy\,u$ | $\boxed{pq=4xyu}$ |
| (b) | $u=ax+by+ab$ | $p=a$, $q=b$ | $\boxed{u=px+qy+pq}$ |
| (c) | $(x-a)^2+(y-b)^2+u^2=1$ | $x-a=-up$, $y-b=-uq$; substitute | $\boxed{u^2(p^2+q^2+1)=1}$ |
| (d) | $u=(x-a)^2+(y-b)^2$ | $p=2(x-a)$, $q=2(y-b)$ | $\boxed{p^2+q^2=4u}$ |
| (e) | $u=x^nf(y/x)$ | $xp=nx^nf-x^{n-1}yf'$, $q=x^{n-1}f'$ | $\boxed{xp+yq=nu}$ |
| (f) | $u=e^{mx}f(x+y)$ | $p=mu+e^{mx}f'$, $q=e^{mx}f'$ | $\boxed{p-q=mu}$ |
| (g) | $G(xy+u^2,\,x+y+u)=0$ | determinant of the two differentiated equations | $\boxed{(2u-x)p+(y-2u)q=x-y}$ |
| (h) | $xyu=f(x+y+u)$ | same with $\varphi=xyu$, $\psi=x+y+u$ | $\boxed{x(y-u)p+y(u-x)q=u(x-y)}$ |
| (i) | $G(x+y+u,\,x^2+y^2-u^2)=0$ | same | $\boxed{(y+u)p-(x+u)q=x-y}$ |
| (j) | $u=f(x+iy)+g(x-iy)$ | $u_{xx}=f''+g''$, $u_{yy}=-(f''+g'')$ | $\boxed{u_{xx}+u_{yy}=0}$ |

**Details for (g).** $\varphi=xy+u^2$, $\psi=x+y+u$: $G_\varphi(y+2up)+G_\psi(1+p)=0$ and $G_\varphi(x+2uq)+G_\psi(1+q)=0$. The determinant vanishes:
$(y+2up)(1+q)-(x+2uq)(1+p)=0$; the $upq$ terms cancel, leaving $(2u-x)p+(y-2u)q=x-y$. (h), (i) are identical in method.

**Orders.** (a)–(d): two constants, two variables, first order (nonlinear). (e)–(i): one arbitrary function, quasi-linear first order. (j): two arbitrary functions, second order.

---

## Q2

> [!question] Solve using characteristics / Lagrange multipliers, $p=u_x$, $q=u_y$.

Method ([[Lagrange's Method for Quasi-linear PDEs]]): solve $\frac{dx}a=\frac{dy}b=\frac{du}c$ for two first integrals $\varphi=c_1$, $\psi=c_2$. General solution $F(\varphi,\psi)=0$ ($F$ arbitrary). Each pair was checked by $a\varphi_x+b\varphi_y+c\varphi_u\equiv0$ and independence.

| | Characteristic equations and key step | General solution $F(\varphi,\psi)=0$ |
|---|---|---|
| (a) | $\frac{dx}{x^2}=\frac{dy}{y^2}$ gives $\frac1x-\frac1y$; $\frac{d(x-y)}{x^2-y^2}=\frac{du}{(x+y)u}$ gives $\frac{x-y}u$ | $F\big(\frac1x-\frac1y,\ \frac{x-y}u\big)=0$ |
| (b) | multipliers $(x,-y,-u)$ give $x^2-y^2-u^2$; $(y,x,-u)$ give $2xy-u^2$ | $F(x^2-y^2-u^2,\ 2xy-u^2)=0$ |
| (c) | $\frac{dx}{x^2}=dy$ gives $y+\frac1x$; $dy=\frac{du}{u^2}$ gives $y+\frac1u$ | $F\big(y+\frac1x,\ y+\frac1u\big)=0$ |
| (d) | put $X=x+1$, $Y=y-1$ (then as (a)) | $F\big(\frac1{x+1}-\frac1{y-1},\ \frac{x-y+2}u\big)=0$ |
| (e) | $s=x+y$; $\frac{d(x-y)}{\cos s-\sin s}=\frac{ds}{\cos s+\sin s}$; $\frac{du}u=\frac{ds}{\cos s+\sin s}=\frac{ds}{\sqrt2\sin(s+\pi/4)}$ | $F\Big(x-y-\ln(\cos s+\sin s),\ \ln u-\frac1{\sqrt2}\ln\tan\big(\frac s2+\frac\pi8\big)\Big)=0$ |
| (f) | $\frac{d(x+y)}{(x+y)^2}=\frac{d(x-y)}{(x-y)^2}$ gives $\frac y{x^2-y^2}$; $\frac{d(x+y)}{x+y}=\frac{du}u$ | $F\big(\frac y{x^2-y^2},\ \frac{x+y}u\big)=0$ |
| (g) as printed, $(x+y)u\,p=xy$ | $dy=0$ so $y=c_1$; $u\,du=\frac{xy}{x+y}dx$ | $F\big(y,\ u^2-2xy+2y^2\ln(x+y)\big)=0$ |
| (g) intended, $xup+yuq=xy$ | $\frac{dx}x=\frac{dy}y$ gives $\frac xy$; $y\,dx=u\,du$ with $y=x/c_1$ | $F\big(\frac xy,\ xy-u^2\big)=0$ |
| (h) | $x\,dx=-y\,dy$ gives $x^2+y^2$; $(u-2y)dy=-y\,du$ so $d(uy)=d(y^2)$ | $F\big(x^2+y^2,\ y(u-y)\big)=0$ |
| (i) | $y-3x=c_1$; then $u'=5u+\tan c_1$ in $x$ | $F\big(y-3x,\ e^{-5x}\big(u+\frac15\tan(y-3x)\big)\big)=0$ |
| (j) | $\frac{dx}{x}=-\frac{dy}y$ gives $xy$; $x^3dx=u(u^2+c_1)du$ | $F\big(xy,\ x^4-u^4-2xyu^2\big)=0$ |
| (k) | $x\,dx=y\,dy$ gives $x^2-y^2$; $x\,dx=\frac{du}{c_1u^2}$ | $F\big(x^2-y^2,\ \frac1u+\frac{x^4-y^4}4\big)=0$ |
| (l) | $\frac{dy}y=\frac{du}u$ gives $\frac uy$; multipliers $(x,y,u)$ give $\frac{d(x^2+y^2+u^2)}{x^2+y^2+u^2}=\frac{dy}y$ | $F\big(\frac uy,\ \frac{x^2+y^2+u^2}y\big)=0$ |
| (m) | $\frac{dx}x=\frac{dy}y$ gives $\frac yx=c_1$; with $y=c_1x$: $dx=\frac{c_1du}{c_1u-2}$ | $F\Big(\frac yx,\ \frac{(yu-2x)e^{-x}}x\Big)=0$ |
| (n) | $x+y=c_1$; $dx=\frac{u\,du}{u^2+c_1^2}$ | $F\big(x+y,\ (u^2+(x+y)^2)e^{-2x}\big)=0$ |
| (o) | multipliers $(x,y,u)$ give $x^2+y^2+u^2$; with $X=x^2$ etc. the other pair gives $\frac x{yu}$ | $F\big(x^2+y^2+u^2,\ \frac x{yu}\big)=0$ |
| (p) | $\frac{d(x-y)}{x-y}=\frac{d(y-u)}{y-u}$; $\frac{d(x-y)}{-(x-y)}=\frac{d(x+y+u)}{2(x+y+u)}$ | $F\big(\frac{x-y}{y-u},\ (x-y)^2(x+y+u)\big)=0$ |
| (q) | $(y,x,0)$: $d(xy)=du$; $(x,-y,u)$: $x\,dx-y\,dy+u\,du=0$ | $F\big(xy-u,\ x^2-y^2+u^2\big)=0$ |
| (r) | add the first two ratios: $dx+dy+du=0$; then $u\,dx=(2x+u-c_1)du$ | $F\big(x+y+u,\ \frac{x-y+u}{u^2}\big)=0$ |
| (s) | multipliers $(1,1,1)$ and $(x,y,u)$ both have zero denominator | $F\big(x+y+u,\ x^2+y^2+u^2\big)=0$ |
| (t) | multipliers $(\frac1x,\frac1y,\frac1u)$ and $(1,1,1)$ | $F\big(xyu,\ x+y+u\big)=0$ |
| (u) | $\frac{d(x-y)}{x-y}=\frac{d(y-u)}{y-u}$ (common factor $x+y+u$); multipliers $(x,y,u)$ against $(1,1,1)$ | $F\big(\frac{x-y}{y-u},\ xy+yu+ux\big)=0$ |
| (v) | $\cot x\,dx=\cot y\,dy=\cot u\,du$ | $F\big(\frac{\sin x}{\sin y},\ \frac{\sin y}{\sin u}\big)=0$ |
| (w) | multipliers $(2x,-1,-1)$: $d(x^2-y-u)=0$; then $d(xu)+d(u^2)+c_1dx-d(x^3)=0$ | $F\big(x^2-y-u,\ u^2-xy\big)=0$ |
| (x) | $\frac{dy}y=\frac{du}u$ gives $\frac yu$; $-x\,dx=(1+c_1^2)u\,du$ | $F\big(\frac yu,\ x^2+y^2+u^2\big)=0$ |
| (y) | linear system $\dot{\mathbf v}=(I+N)\mathbf v$, $N$ skew: $s=x+y+u$ grows as $e^t$; $w=x+\omega y+\omega^2u$ obeys $\dot w=(1-i\sqrt3)w$ | $F\Big(\frac{x^2+y^2+u^2-xy-yu-ux}{(x+y+u)^2},\ \sqrt3\ln(x+y+u)+\arctan\frac{\sqrt3(y-u)}{2x-y-u}\Big)=0$ |
| (z) | eigen-method, below | $F\Big(\frac{u-x+2y}{(2u-5x+5y)^2},\ (u-x)^2-4y^2\Big)=0$ |

**(z) in detail.** $(y+u)p+(u-x)q=u+5y$: $\dot{\mathbf v}=M\mathbf v$ with $M=\begin{pmatrix}0&1&1\\-1&0&1\\0&5&1\end{pmatrix}$, eigenvalues $\lambda=1,2,-2$. Left eigenvectors give $\ell_1=u-\frac52x+\frac52y$ ($\lambda=1$), $\ell_2=u-x+2y$ ($\lambda=2$), $\ell_3=u-x-2y$ ($\lambda=-2$), each satisfying $\frac{d\ell}{dt}=\lambda\ell$. Hence $\ell_2/\ell_1^2$ and $\ell_2\ell_3$ are constant on characteristics.

**(y) in detail.** $M=I+N$ with $N$ skew, so $\frac{d}{dt}(x+y+u)=x+y+u$ and the perpendicular part rotates while growing at the same rate: $|w|^2/s^2$ and $\arg w+\sqrt3\ln s$ are first integrals ($\arg w=\arctan\frac{\sqrt3(y-u)}{2x-y-u}$).

> [!tip] Recognise-and-pick
> Three variables appear symmetrically ($y-u$, $u-x$, $x-y$): try multipliers $(1,1,1)$, $(x,y,u)$, $(1/x,1/y,1/u)$. Linear coefficients with no obvious integral: eigen-method. A pair of ratios free of the third variable: group.

---

## Q3

> [!question] Solve the initial value problems by Lagrange's method.

Each is: two first integrals, impose the data curve, eliminate the parameter ([[Cauchy Problem for First Order PDEs]]). All solutions were substituted back into the PDE and the data.

| | Integrals | Data gives | Solution |
|---|---|---|---|
| (a) $u_x+u_y-u=e^x$, $u(x,0)=0$ | $y-x=c_1$, $ue^{-x}-x=c_2$ | $c_2=c_1$ | $\boxed{u=ye^x}$ |
| (b) $xu_x+yu_y=xe^{-u}$, $u(x,x^2)=0$ | $\frac yx=c_1$, $e^u-x=c_2$ | $c_2=1-c_1$ | $\boxed{u=\ln\!\big(1+x-\tfrac yx\big)}$ |
| (c) $u_x-u_y+u=y$, $u(x,0)=x^2$ | $x+y=c_1$, $(u-y-1)e^x=c_2$ | $c_2=(c_1^2-1)e^{c_1}$ | $\boxed{u=y+1+\big((x+y)^2-1\big)e^{y}}$ |
| (d) $xu_x-yu_y+u=x$, $u(x,x)=x^3$ | $xy=c_1$, $xu-\frac{x^2}2=c_2$ | $c_2=c_1^2-\frac{c_1}2$ | $\boxed{u=xy^2+\tfrac{x-y}2}$ |
| (e) $x(y^2+u)u_x-y(x^2+u)u_y=(x^2-y^2)u$, $u(x,-x)=1$ | $xyu=c_1$, $x^2+y^2-2u=c_2$ | $c_2=-2c_1-2$ | $\boxed{u=\dfrac{x^2+y^2+2}{2(1-xy)}}$ |
| (f) $u_x-u_y+\sqrt2u=0$, $u(x,0)=x$ | $x+y=c_1$, $ue^{\sqrt2x}=c_2$ | $c_2=c_1e^{\sqrt2c_1}$ | $\boxed{u=(x+y)e^{\sqrt2y}}$ |
| (g) $u_x-u_y-\sqrt2u=0$, $u(x,0)=x^2$ | $x+y$, $ue^{-\sqrt2x}$ | $c_2=c_1^2e^{-\sqrt2c_1}$ | $\boxed{u=(x+y)^2e^{-\sqrt2y}}$ |
| (h) $u_x-u_y+\sqrt2u=0$, $u(x,0)=x+e^x$ | as (f) | $c_2=(c_1+e^{c_1})e^{\sqrt2c_1}$ | $\boxed{u=\big(x+y+e^{x+y}\big)e^{\sqrt2y}}$ |
| (i) $u_x-u_y-\sqrt2u=0$, $u(0,y)=e^y-y$ | as (g) | on $x=0$: $c_1=s$, $c_2=e^s-s$ | $\boxed{u=e^{\sqrt2x}\big(e^{x+y}-x-y\big)}$ |
| (j) $3u_x-4u_y+2u=0$, $u(x,0)=e^x$ | $4x+3y=c_1$, $ue^{2x/3}=c_2$ | $c_2=e^{5c_1/12}$ | $\boxed{u=e^{x+5y/4}}$ |
| (k) $uu_x+u_y=0$, $u(x,0)=x$ | $u=c_1$, $x-uy=c_2$ | $c_2=c_1$ | $\boxed{u=\dfrac x{1+y}}$ |
| (l) $u_x+u_y=u^2$, $u(x,0)=\cos x$ | $x-y=c_1$, $\frac1u+x=c_2$ | $c_2=\sec c_1+c_1$ | $\boxed{u=\dfrac{\cos(x-y)}{1-y\cos(x-y)}}$ |
| (m) $xu_x+yu_y=u$, $u(1,y)=1+y$ | $\frac yx=c_1$, $\frac ux=c_2$ | $c_2=1+c_1$ | $\boxed{u=x+y}$ |
| (n) $u_x+2xu_y=y$, $u(0,y)=y^2$ | $y-x^2=c_1$, $u-c_1x-\frac{x^3}3=c_2$ | $c_2=c_1^2$ | $\boxed{u=(y-x^2)^2+xy-\tfrac23x^3}$ |
| (o) $yu_x-xu_y=0$, $u(0,y)=y^2$ | $x^2+y^2=c_1$, $u=c_2$ | $c_2=c_1$ | $\boxed{u=x^2+y^2}$ |
| (p) $u(x+y)u_x+u(x-y)u_y=x^2+y^2$, $u=0$ on $y=2x$ | $x^2-y^2-u^2=c_1$, $2xy-u^2=c_2$ (Q2(b)) | on $(s,2s,0)$: $c_1=-3s^2$, $c_2=4s^2$, so $3c_2=-4c_1$ | $\boxed{u^2=\tfrac27(2x-y)(x+2y)}$ |

**How a typical one goes (c).** $\frac{dx}1=\frac{dy}{-1}=\frac{du}{y-u}$: $x+y=c_1$; then $u'+u=c_1-x$ gives $u=c_1-x+1+c_2e^{-x}$, i.e. $(u-y-1)e^x=c_2$. On $y=0$, $x=s$: $c_1=s$, $c_2=(s^2-1)e^s$. Hence $(u-y-1)e^x=((x+y)^2-1)e^{x+y}$.

**Domain notes.** (e) is singular on the hyperbola $xy=1$. (k) is smooth for $y>-1$ and a Burgers-type rarefaction. (l) blows up where $y\cos(x-y)=1$. (o): the data curve $x=0$ meets each circle $x^2+y^2=c_1$ twice, at $\pm y$, and consistency requires $u_0$ even, which $y^2$ is.

### Q3(q)

> [!question] $u_x+u_y=1$ with $u=x$ on $y=x$: show infinitely many solutions; with $u=0$ on $y=x$ none. Explain geometrically.

Characteristics: $\frac{dx}1=\frac{dy}1=\frac{du}1$: $x-y=c_1$, $u-x=c_2$, general solution $u=x+g(x-y)$.
- **Data $u=x$ on $y=x$:** here $c_1=0$ and $c_2=0$, so the only requirement is $g(0)=0$. Every $g$ with $g(0)=0$ works: **infinitely many solutions**.
- **Data $u=0$ on $y=x$:** $c_1=0$ and $c_2=u-x=-x$, which takes a different value at each point of the curve, but $g(0)$ is a single number. **No solution**.

**Geometry.** The data curve $(s,s,u_0(s))$ has direction $(1,1,u_0')$; the characteristic direction is $(a,b,c)=(1,1,1)$. The projection of the curve onto the $xy$-plane is the line $y=x$, which is itself a characteristic base curve ($a\dot y_0-b\dot x_0=0$). If $u_0'=1$ the space curve *is* a characteristic, and then any surface containing it is an integral surface (non-uniqueness). If $u_0'\ne1$ the curve is not tangent to the field $(1,1,1)$ but sits above a characteristic base curve, so no integral surface can contain it.

![[DE-PDE-characteristics.png]]

---

## Q4

> [!question] Discuss the type of the second-order equations and sketch the regions.

Type from $\Delta=b^2-4ac$ of the second-order terms only ([[Classification of Second Order PDEs]]). $\Delta>0$ hyperbolic, $=0$ parabolic, $<0$ elliptic.

| | $a,b,c$ | $\Delta$ | Hyperbolic | Parabolic | Elliptic |
|---|---|---|---|---|---|
| (a) | $1,\ x-1,\ 1$ | $(x-3)(x+1)$ | $x<-1$ or $x>3$ | $x=-1$, $x=3$ | $-1<x<3$ |
| (b) | $y,\ -x,\ y$ | $x^2-4y^2$ | $x^2>4y^2$ | $x=\pm2y$ | $x^2<4y^2$ |
| (c) | $x+2,\ 2(x+y),\ 2(y-1)$ | $4[(x+1)^2+(y-2)^2-1]$ | outside the circle centre $(-1,2)$, radius 1 | on the circle | inside |
| (d) | $y^2,\ 0,\ -x^2$ | $4x^2y^2>0$ | everywhere ($x,y>0$) | none | none |
| (e) | $x^2,\ 2xy,\ y^2$ | $0$ | none | everywhere | none |
| (f) | $1,\ 0,\ x^2$ | $-4x^2$ | none | $x=0$ | $x\ne0$ |
| (g) | $1,\ 2,\ 5$ | $-16$ | none | none | everywhere |
| (h) | $1,\ 2x,\ 1-y^2$ | $4(x^2+y^2-1)$ | outside the unit circle | the unit circle | inside |
| (i) Tricomi | $y,\ 0,\ 1$ | $-4y$ | $y<0$ | $y=0$ | $y>0$ |
| (j) | $1+x^2,\ 0,\ 1+y^2$ | $-4(1+x^2)(1+y^2)$ | none | none | everywhere |
| (k) | $\sin^2x,\ \sin2x,\ \cos^2x$ | $0$ | none | everywhere | none |
| (l) | $x,\ 0,\ y$ | $-4xy$ | $xy<0$ (quadrants II, IV) | the axes | $xy>0$ (I, III) |
| (m) | $1,\ y,\ x$ | $y^2-4x$ | $y^2>4x$ | $y^2=4x$ | $y^2<4x$ |
| (n) | $y,\ 2,\ 1$ | $4(1-y)$ | $y<1$ | $y=1$ | $y>1$ |

(n) has a nonlinear right side $uu_x+u_y^2$, but the type depends only on the principal part, which is linear in $u_{xx},u_{xy},u_{yy}$ with coefficients in $y$.

![[DE-PDE-classification-regions.png]]
**Figure:** regions for (b), (c), (h), (i), (l), (m): orange hyperbolic, blue elliptic, line parabolic.

---

## Q5

> [!question] Reduce to canonical form; find the general solution if possible.

Method ([[Canonical Forms of Second Order PDEs]]): solve $\frac{dy}{dx}=\frac{b\pm\sqrt{b^2-4ac}}{2a}$ for the characteristics, set $\xi,\eta$, transform, divide by the leading coefficient. All canonical forms were derived with sympy (`de_a8_second_order.py`) and every quoted general solution was substituted into the original PDE (`de_a8_solutions_check.py`).

| | Type | $\frac{dy}{dx}$ | $\xi,\ \eta$ | Canonical form | General solution |
|---|---|---|---|---|---|
| (a) | parabolic | $1$ | $x-y,\ x$ | $u_{\eta\eta}=0$ | $f(x-y)+x\,g(x-y)$ |
| (b) $y<0$ | hyperbolic | $\pm\sqrt{-y}$ | $x+2\sqrt{-y},\ x-2\sqrt{-y}$ | $u_{\xi\eta}+\dfrac{u_\xi-u_\eta}{2(\xi-\eta)}=0$ | not elementary |
| (c) $x\ne0$ | hyperbolic | $\pm x$ | $y+\frac{x^2}2,\ y-\frac{x^2}2$ | $u_{\xi\eta}-\dfrac{u_\xi-u_\eta}{4(\xi-\eta)}=0$ | not elementary |
| (d) $x<0$ | hyperbolic | $\pm\sqrt{-x}$ | $y+\frac23(-x)^{3/2},\ y-\frac23(-x)^{3/2}$ | $u_{\xi\eta}-\dfrac{u_\xi-u_\eta}{6(\xi-\eta)}=0$ | not elementary |
| (e) | parabolic | $-xy$ | $ye^{x^2/2},\ x$ | $u_{\eta\eta}+\xi(1-\eta^2)u_\xi=0$ | not elementary |
| (f) | hyperbolic ($xy\ne1$) | $-\frac1x,\ -y$ | $y+\ln x,\ ye^x$ | $u_{\xi\eta}=0$ | $f(y+\ln x)+g(ye^x)$ |
| (g) | parabolic | $\frac yx$ | $\frac yx,\ \ln x$ | $u_{\eta\eta}=0$ | $f(\frac yx)+g(\frac yx)\ln x$ |
| (h) | parabolic | $-\frac xy$ | $x^2+y^2,\ x$ | $u_{\eta\eta}-\frac1\eta u_\eta=0$ | $x^2f(x^2+y^2)+g(x^2+y^2)$ |
| (i) | hyperbolic ($y\ne1$) | $-1,\ -y$ | $x+y,\ ye^x$ | $u_{\xi\eta}=2\eta$ | $y^2e^{2x}(x+y)+f(x+y)+g(ye^x)$ |
| (j) | hyperbolic | $-\frac1x,\ -\frac yx$ | $y+\ln x,\ xy$ | $u_{\xi\eta}=0$ | $f(y+\ln x)+g(xy)$ |
| (k) | hyperbolic | $\frac14,\ -2$ | $4y-x,\ y+2x$ | $u_{\xi\eta}=-3\xi^2\eta$ | $-\frac12(4y-x)^3(y+2x)^2+f(4y-x)+g(y+2x)$ |
| (l) | hyperbolic | $1,\ -\frac23$ | $y-x,\ 2x+3y$ | $u_{\xi\eta}-2u_\xi=0$ | $e^{2(2x+3y)}f(y-x)+g(2x+3y)$ |
| (m) | parabolic | $4$ | $y-4x,\ x$ | $u_{\eta\eta}=16$ | $8x^2+x\,f(y-4x)+g(y-4x)$ |
| (n) | parabolic | $-\frac34$ | $3x+4y,\ x$ | $u_{\eta\eta}+\frac94u_\eta=0$ | $f(3x+4y)+e^{-9x/4}g(3x+4y)$ |
| (o) | hyperbolic | $3,\ \frac13$ | $y-3x,\ 3y-x$ | $u_{\xi\eta}=0$ | $f(y-3x)+g(3y-x)$ |
| (p) | hyperbolic | $3,\ 1$ | $y-3x,\ y-x$ | $u_{\xi\eta}=0$ | $f(y-3x)+g(y-x)$ |
| (q) | elliptic | $\frac{1\pm i\sqrt3}2$ | $y-\frac x2,\ \frac{\sqrt3}2x$ | $u_{\xi\xi}+u_{\eta\eta}=0$ | $F(y+\omega x)+G(y+\bar\omega x)$, $\omega=\frac{-1+i\sqrt3}2$ |
| (r) | elliptic | $1\pm4i$ | $y-x,\ 4x$ | $u_{\xi\xi}+u_{\eta\eta}=0$ | $F\big(y+(-1+4i)x\big)+G\big(y+(-1-4i)x\big)$ |
| (s) | parabolic | $1$ | $x-y,\ x$ | $u_{\eta\eta}=4\eta(\eta-\xi)$ | $\frac{x^4}3-\frac23x^3(x-y)+x\,f(x-y)+g(x-y)$ |
| (t) $y\ne0$ | hyperbolic | $\pm y^2$ | $x+\frac1y,\ x-\frac1y$ | $u_{\xi\eta}=0$ | $f(x+\frac1y)+g(x-\frac1y)$ |
| (u) $x>0$ | hyperbolic | $\pm\sqrt x$ | $y+\frac23x^{3/2},\ y-\frac23x^{3/2}$ | $u_{\xi\eta}=0$ | $f(y+\frac23x^{3/2})+g(y-\frac23x^{3/2})$ |
| (v) $y\ne0$ | elliptic | $\pm\frac iy$ ($dx=\pm iy\,dy$) | $x,\ \frac{y^2}2$ | $u_{\xi\xi}+u_{\eta\eta}+\frac1{2\eta}u_\eta=0$ | not elementary |
| (w) $x,y\ne0$ | elliptic | $\pm i\frac yx$ | $\ln\lvert y\rvert,\ \ln\lvert x\rvert$ | $u_{\xi\xi}+u_{\eta\eta}-u_\xi-u_\eta=0$ | (remove the first-order terms by $u=ve^{(\xi+\eta)/2}$) |
| (x) $y\ne0$ | hyperbolic | $\pm\frac{e^x}{2y}$ | $y^2+e^x,\ y^2-e^x$ | $u_{\xi\eta}+\dfrac{(3\eta+\xi)u_\xi-(\eta+3\xi)u_\eta}{4(\eta^2-\xi^2)}=0$ | not elementary |
| (y) $x,y>0$ | hyperbolic | $\pm\frac xy$ | $y^2+x^2,\ y^2-x^2$ | $u_{\xi\eta}+\dfrac{\eta u_\xi-\xi u_\eta}{2(\eta^2-\xi^2)}=0$ | not elementary |
| (z) | hyperbolic | $1-\sin x,\ -1-\sin x$ | $y-\cos x-x,\ y-\cos x+x$ | $u_{\xi\eta}=0$ | $f(y-\cos x-x)+g(y-\cos x+x)$ |

**Worked examples.**
- **(k).** $\Delta=49+32=81$, $\frac{dy}{dx}=\frac{-7\pm9}{8}=\frac14$ or $-2$. $\xi=4y-x$, $\eta=y+2x$. The right side $243(2x+y)(x-4y)^2=243\,\eta\,\xi^2$ and $B'=-81$, so $u_{\xi\eta}=-3\xi^2\eta$; integrate twice.
- **(h).** $y^2u_{xx}-2xyu_{xy}+x^2u_{yy}-\frac{y^2}xu_x-\frac{x^2}yu_y=0$ is parabolic with $\frac{dy}{dx}=-\frac xy$, i.e. $x^2+y^2=c$. Take $\xi=x^2+y^2$, $\eta=x$. Then $A'=B'=0$, $C'=y^2$, the $u_\xi$ coefficient is $2y^2+2x^2-2y^2-2x^2=0$, and the $u_\eta$ coefficient is $-y^2/x$. Dividing by $y^2$: $u_{\eta\eta}-\frac1\eta u_\eta=0$, so $u_\eta=\eta\,c(\xi)$ and $u=\frac{\eta^2}2c(\xi)+d(\xi)$.
- **(n).** $16u_{xx}-24u_{xy}+9u_{yy}=(4\partial_x-3\partial_y)^2u$ and $36u_x-27u_y=9(4\partial_x-3\partial_y)u$. With $\xi=3x+4y$ (killed by $4\partial_x-3\partial_y$) and $\eta=x$: $(4\partial_x-3\partial_y)=4\partial_\eta$, so $16u_{\eta\eta}+36u_\eta=0$.
- **(q).** $dy/dx=\frac{1\pm i\sqrt3}2$, $\varphi=y-\frac x2\mp i\frac{\sqrt3}2x$; $\xi=\mathrm{Re}\,\varphi$, $\eta=-\mathrm{Im}\,\varphi$ (sign immaterial): $u_x=-\frac12u_\xi+\frac{\sqrt3}2u_\eta$, $u_y=u_\xi$, and the sum collapses to $\frac34(u_{\xi\xi}+u_{\eta\eta})=0$.
- **(z).** The coefficient $-\cos x\,u_y$ is exactly what makes $u_{\xi\eta}=0$ without lower-order terms.

---

## Q6

**(a) Complete and singular integral of $u=px+qy+pq$.** Clairaut form. Complete integral $u=ax+by+ab$. $\partial_a:\ x+b=0$, $\partial_b:\ y+a=0$, so $a=-y$, $b=-x$ and the singular integral is $\boxed{u=-xy}$ ([[Complete, General and Singular Integrals]]).

**(b) $yp-xq=0$.** $\frac{dx}y=\frac{dy}{-x}=\frac{du}0$: $x^2+y^2=c_1$, $u=c_2$, so $u=f(x^2+y^2)$: a surface of revolution about the $u$-axis. Through $u=y^2$, $x=0$: $f(y^2)=y^2$, $f(s)=s$, so $\boxed{u=x^2+y^2}$.

**(c) $xu_y-yu_x=0$ through the circle $u=1$, $x^2+y^2=4$.** Same equation: $u=f(x^2+y^2)$ with $f(4)=1$. **Not unique**: $u=1$, $u=\frac{x^2+y^2}4$, $u=\frac{(x^2+y^2)^2}{16}$ all work. Reason: the circle $x^2+y^2=4$, $u=1$ is itself a characteristic curve (characteristics are circles at constant height); data on a characteristic never determines the solution uniquely ([[Cauchy Problem for First Order PDEs]]).

**(d) Two integral surfaces meeting along a curve $C$.** At a point $P\in C$ each surface is tangent to the vector $(a,b,c)(P)$, so $(a,b,c)$ lies in both tangent planes. Two distinct planes meet in one line, so the tangent of $C$ is along $(a,b,c)$ everywhere: $C$ satisfies $\frac{dx}a=\frac{dy}b=\frac{du}c$ and is a characteristic.

**(e) Invariance of the discriminant.** With $\xi_x,\xi_y,\eta_x,\eta_y$ and $J=\xi_x\eta_y-\xi_y\eta_x\ne0$ the new coefficients are
$A=a\xi_x^2+b\xi_x\xi_y+c\xi_y^2$, $B=2a\xi_x\eta_x+b(\xi_x\eta_y+\xi_y\eta_x)+2c\xi_y\eta_y$, $C=a\eta_x^2+b\eta_x\eta_y+c\eta_y^2$. Expanding (sympy confirms the difference is exactly 0):
$$B^2-4AC=J^2\,(b^2-4ac).$$
$J^2>0$, so the sign, hence the type, is unchanged.

**(f) $u_{xx}-2u_{xy}+u_{yy}=0$.** Parabolic, $\frac{dy}{dx}=-1$: $\xi=x+y$, $\eta=x$; $u_{\eta\eta}=0$ gives $u=\eta\,\psi(\xi)+\phi(\xi)=\phi(x+y)+x\,\psi(x+y)$, with $\phi,\psi$ arbitrary ✓. Direct check: $(\partial_x-\partial_y)^2$ annihilates $\phi(x+y)$ and sends $x\psi(x+y)\mapsto\psi\mapsto0$.

**(g) $u_{\xi\eta}-4u_\xi+u_\eta+3u=0$, $u=ve^{\lambda\xi+\mu\eta}$.** $v_{\xi\eta}+(\mu-4)v_\xi+(\lambda+1)v_\eta+(\lambda\mu-4\lambda+\mu+3)v=0$. Take $\mu=4$, $\lambda=-1$:
$$v_{\xi\eta}+7v=0,\qquad u=v\,e^{-\xi+4\eta}.$$

**(h) Tricomi $yu_{xx}+u_{yy}=0$.**
- $y>0$ (elliptic): $dx=\pm i\sqrt y\,dy$, so $\xi=x$, $\eta=\frac23y^{3/2}$: $\boxed{u_{\xi\xi}+u_{\eta\eta}+\dfrac1{3\eta}u_\eta=0}$.
- $y<0$ (hyperbolic): $dx=\pm\sqrt{-y}\,dy$, so $\xi=x+\frac23(-y)^{3/2}$, $\eta=x-\frac23(-y)^{3/2}$: $\boxed{u_{\xi\eta}-\dfrac{u_\xi-u_\eta}{6(\xi-\eta)}=0}$.

**(i) $u_{xx}+u_{yy}+2u_x-4u_y+u=0$.** Put $u=ve^{\alpha x+\beta y}$: the $v_x$ coefficient is $2\alpha+2$, the $v_y$ coefficient is $2\beta-4$. Choose $\alpha=-1$, $\beta=2$; the zeroth-order term is $\alpha^2+\beta^2+2\alpha-4\beta+1=1+4-2-8+1=-4$:
$$v_{xx}+v_{yy}-4v=0,\qquad c=\boxed{-4},\ \ u=ve^{-x+2y}.$$

---

## Summary

| Pattern | Recognise by | Do |
|---|---|---|
| formation | relation with constants or $G(\varphi,\psi)=0$ | differentiate, eliminate (determinant) |
| quasi-linear first order | $ap+bq=c$ | $\frac{dx}a=\frac{dy}b=\frac{du}c$; multipliers or grouping or eigen-method |
| initial data | $u$ given on a curve | impose, eliminate the parameter, check transversality |
| second-order type | sign of $b^2-4ac$ | discriminant, regions |
| canonical form | variable coefficients | characteristic ODE, $\xi,\eta$, divide by the leading coefficient |
| remove first-order terms | constant coefficients | $u=ve^{\lambda x+\mu y}$ |

Verification and plots: `Tools/de_a8_first_order.py` (all 26 Lagrange integrals, 16 IVPs, formation), `de_a8_second_order.py` (discriminants, 26 canonical forms, Q6), `de_a8_solutions_check.py` (general solutions), `de_pde_figs.py`.

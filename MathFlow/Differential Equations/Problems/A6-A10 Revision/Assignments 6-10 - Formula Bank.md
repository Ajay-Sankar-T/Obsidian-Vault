---
title: Assignments 6–10 – Formula Bank
course: MA 2102 Differential Equations
tags: [DE, formula-bank, concept]
up: "[[Problems - MOC]]"
aliases: [Bessel Sturm-Liouville PDE formula sheet, MA2102 formula bank, DE revision formulas, Assignments 6-10 formulas]
---

# Assignments 6–10 – Formula Bank

Part of [[Problems - MOC]] · choose the method: [[Assignments 6-10 - How to Solve]] · practice: [[Assignments 6-10 - Question Bank]] · theory maps: [[Special Functions - MOC]], [[PDEs - MOC]]

Solved sheets: [[Assignment 6 - Bessel Functions - Solutions]] · [[Assignment 7 - Sturm-Liouville Problems - Solutions]] · [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]] · [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]] · [[Assignment 10 - Laplace Equations - Solutions]]

> [!abstract] How to use it
> One page for the second half of MA 2102, in the order of the sheets: **Bessel functions (§1) → Sturm–Liouville (§2) → first-order PDEs (§3) → second-order PDEs and canonical forms (§4) → wave (§5) → heat (§6) → Laplace (§7)**, then a bridge (§8) and a list of numbers worth knowing (§9). Each row says what the formula gives and when it holds. Everything here was recomputed in `Tools/de_a610_bank.py` (symbolic substitution or quadrature). Write the *conditions* from memory, not just the formulas: most lost marks are a formula used outside its conditions.

> [!tip] The five moves behind every question on these sheets
> | Move | Where |
> |---|---|
> | Differentiate $x^{\pm\nu}J_\nu$, use the four recurrences | Assignment 6 |
> | Put the equation in self-adjoint form, read off the **weight** | Assignments 6, 7 |
> | Follow the **characteristics** ($x\pm ct$, $\frac{dx}a=\frac{dy}b=\frac{du}c$) | Assignments 8, 9 |
> | **Separate variables**: boundary conditions pick the eigenfunctions, the PDE picks the factor in the other variable | Assignments 9, 10 |
> | **Superpose and match** the data with orthogonal coefficients $a_n=\int rfy_n\big/\int ry_n^2$ | Assignments 6, 7, 9, 10 |

---

## 1. Bessel functions (Assignment 6)

![[A610-FB-1-bessel-sheet.png]]

**Figure.** $J_n$ are finite at $0$ and decay like $x^{-1/2}$ (envelope $\sqrt{2/\pi x}$); $Y_n$ blow up at $0$; the spherical $j_n=\sqrt{\pi/2x}\,J_{n+1/2}$ are elementary.

### 1.1 Equation and solutions

| Item | Formula | Condition / remark |
|---|---|---|
| Bessel's equation | $x^2y''+xy'+(x^2-\nu^2)y=0$ | regular singular point at $0$, exponents $\pm\nu$ |
| First kind | $J_\nu(x)=\displaystyle\sum_{k\ge0}\frac{(-1)^k}{k!\,\Gamma(k+\nu+1)}\Big(\frac x2\Big)^{2k+\nu}$ | $\Gamma(k+1)=k!$, $\Gamma(\tfrac12)=\sqrt\pi$ |
| General solution | $y=AJ_\nu+BJ_{-\nu}$ | only if $\nu\notin\mathbb Z$ |
| Second kind | $Y_\nu=\dfrac{J_\nu\cos\nu\pi-J_{-\nu}}{\sin\nu\pi}$ (limit for integer $\nu$) | general solution $AJ_\nu+BY_\nu$ **always** valid |
| Negative integer order | $J_{-n}=(-1)^nJ_n$ | $1/\Gamma$ kills the first $n$ terms |
| Parity | $J_n(-x)=(-1)^nJ_n(x)$ | integer $n$ |
| Wronskians | $W(J_\nu,Y_\nu)=\dfrac2{\pi x}$, $\ W(J_\nu,J_{-\nu})=-\dfrac{2\sin\nu\pi}{\pi x}$ | any two solutions: $W=c/x$ (Abel) |
| Parametric form | $x^2y''+xy'+(\lambda^2x^2-\nu^2)y=0\Rightarrow y=Z_\nu(\lambda x)$ | $Z$ = $J$ and $Y$ |
| Near $0$ | $J_\nu\sim\dfrac{(x/2)^\nu}{\Gamma(\nu+1)}$; $\ Y_\nu\sim-\dfrac{\Gamma(\nu)}\pi\Big(\dfrac2x\Big)^\nu$, $\ Y_0\sim\dfrac2\pi\ln x$ | bounded at the centre ⇒ keep $J$ only |
| Large $x$ | $J_\nu\sim\sqrt{\dfrac2{\pi x}}\cos\!\Big(x-\dfrac{\nu\pi}2-\dfrac\pi4\Big)$, $\ Y_\nu\sim\sqrt{\dfrac2{\pi x}}\sin\!\Big(x-\dfrac{\nu\pi}2-\dfrac\pi4\Big)$ | zeros spaced $\to\pi$ |
| Bounds | $\lvert J_0\rvert\le1$, $\ \lvert J_n\rvert\le\tfrac1{\sqrt2}$ for $n\ge1$ ($\max\lvert J_1\rvert=0.5819$) | from $J_0^2+2\sum J_n^2=1$ |

### 1.2 Identities and recurrences

| Name | Formula | Use |
|---|---|---|
| R1 | $\dfrac d{dx}\big[x^\nu J_\nu\big]=x^\nu J_{\nu-1}$ | integrals ending in $x^\nu J_\nu$ |
| R2 | $\dfrac d{dx}\big[x^{-\nu}J_\nu\big]=-x^{-\nu}J_{\nu+1}$ | integrals ending in $x^{-\nu}J_\nu$ |
| R1′, R2′ | $J_\nu'=J_{\nu-1}-\dfrac\nu xJ_\nu=\dfrac\nu xJ_\nu-J_{\nu+1}$ | derivatives |
| R3 (upwards) | $J_{\nu-1}+J_{\nu+1}=\dfrac{2\nu}xJ_\nu$ | build $J_2,J_3,\dots$ from $J_0,J_1$ |
| R4 | $J_{\nu-1}-J_{\nu+1}=2J_\nu'$ | $J_5=-J_0'-2J_2'-2J_4'$ by repetition |
| Special | $J_0'=-J_1$, $\ (xJ_1)'=xJ_0$ | $\int J_0'=J_0$ |
| Half-integer | $J_{1/2}=\sqrt{\tfrac2{\pi x}}\sin x$, $\ J_{-1/2}=\sqrt{\tfrac2{\pi x}}\cos x$, $\ J_{3/2}=\sqrt{\tfrac2{\pi x}}\big(\tfrac{\sin x}x-\cos x\big)$ | R3 gives every $J_{n+1/2}$ |
| Spherical | $j_n=\sqrt{\tfrac\pi{2x}}J_{n+\frac12}$; $\ j_0=\tfrac{\sin x}x$, $\ j_1=\tfrac{\sin x}{x^2}-\tfrac{\cos x}x$ | $j_{n-1}+j_{n+1}=\tfrac{2n+1}xj_n$, $\ (2n+1)j_n'=nj_{n-1}-(n+1)j_{n+1}$ |
| $J_4$ from $J_0,J_1$ | $J_4=\big(\tfrac{48}{x^3}-\tfrac8x\big)J_1+\big(1-\tfrac{24}{x^2}\big)J_0$ | R3 three times |
| Derivative of squares | $\dfrac d{dx}J_n^2=\dfrac x{2n}\big(J_{n-1}^2-J_{n+1}^2\big)$ | R3 × R4 |

### 1.3 Integrals

| Integral | Result | Condition |
|---|---|---|
| $\int x^\nu J_{\nu-1}\,dx$ | $x^\nu J_\nu$ | R1 |
| $\int x^{-\nu}J_{\nu+1}\,dx$ | $-x^{-\nu}J_\nu$ | R2 |
| $\int J_{\nu+1}\,dx$ | $\int J_{\nu-1}\,dx-2J_\nu$ | R4, integer steps reach $\int J_1=-J_0$ |
| Reduction | $\displaystyle\int x^pJ_\nu=x^pJ_{\nu+1}-(p-\nu-1)\int x^{p-1}J_{\nu+1}$ | by parts, $x^{\nu+1}J_\nu=(x^{\nu+1}J_{\nu+1})'$ |
| **Closed form?** | $\int x^\mu J_\nu\,dx$ is a finite combination of Bessel functions **iff $\mu+\nu$ is a positive odd integer**; otherwise it ends in $\int J_0$ | e.g. $\int x^3J_0=x^3J_1-2x^2J_2$ but $\int x^4J_0$ needs $\int J_0$ |
| $\int_0^r xJ_0(ax)\,dx$ | $\dfrac raJ_1(ar)$ | $t=ax$ and R1 |
| Laplace transform | $\displaystyle\int_0^\infty e^{-ax}J_0(bx)\,dx=\frac1{\sqrt{a^2+b^2}}$ ($a>0$), and $\int_0^\infty J_0=1$ | Bessel's integral and $\int\frac{d\theta}{a^2+b^2\sin^2\theta}$ |

### 1.4 Generating function and sums

| Result | Formula |
|---|---|
| Generating function | $e^{\frac x2(t-\frac1t)}=\displaystyle\sum_{n\in\mathbb Z}J_n(x)t^n$ |
| Jacobi–Anger ($t=e^{i\theta}$) | $e^{ix\sin\theta}=\sum J_ne^{in\theta}$, $\ \cos(x\sin\theta)=J_0+2\sum_{k\ge1}J_{2k}\cos2k\theta$, $\ \sin(x\sin\theta)=2\sum_{k\ge0}J_{2k+1}\sin(2k+1)\theta$ |
| Bessel's integral | $J_n(x)=\dfrac1\pi\displaystyle\int_0^\pi\cos(n\theta-x\sin\theta)\,d\theta$ |
| At $\theta=\tfrac\pi2$ and $0$ | $\sin x=2J_1-2J_3+\cdots$, $\ \cos x=J_0-2J_2+2J_4-\cdots$, $\ 1=J_0+2J_2+2J_4+\cdots$ |
| Sum of squares | $J_0^2+2\sum_{n\ge1}J_n^2=1$ (Parseval of Jacobi–Anger) |
| Addition theorem | $J_n(x+y)=\sum_kJ_k(x)J_{n-k}(y)$, hence $J_0(2x)=J_0^2+2\sum_{k\ge1}(-1)^kJ_k^2$ |

### 1.5 Zeros, orthogonality, Fourier–Bessel series

| Item | Formula | Remark |
|---|---|---|
| Interlacing | between consecutive zeros of $J_\nu$ lies exactly one zero of $J_{\nu\pm1}$ | Rolle on $x^{\mp\nu}J_\nu$ |
| McMahon | $j_{\nu,s}\approx\beta-\dfrac{4\nu^2-1}{8\beta}$, $\ \beta=\big(s+\tfrac\nu2-\tfrac14\big)\pi$ | $j_{0,10}=30.6346$ (formula $30.6346$) |
| Orthogonality | $\displaystyle\int_0^LxJ_\nu\Big(\tfrac{\alpha_jx}L\Big)J_\nu\Big(\tfrac{\alpha_kx}L\Big)dx=\dfrac{L^2}2J_{\nu+1}(\alpha_k)^2\,\delta_{jk}$ | weight **$x$**; $\alpha_k$ = positive zeros of $J_\nu$; at a zero $J_\nu'(\alpha)=-J_{\nu+1}(\alpha)$ |
| Lommel integral | $\displaystyle\int_0^cJ_\nu(ax)J_\nu(bx)\,x\,dx=\frac c{b^2-a^2}\big[aJ_\nu(bc)J_{\nu-1}(ac)-bJ_\nu(ac)J_{\nu-1}(bc)\big]$ | $a\ne b$; gives orthogonality, and the norm as $b\to a$ |
| Coefficients | $f\sim\sum a_nJ_\nu\big(\tfrac{\alpha_nx}L\big)$, $\ a_n=\dfrac{2}{L^2J_{\nu+1}(\alpha_n)^2}\displaystyle\int_0^Lx\,f(x)J_\nu\Big(\tfrac{\alpha_nx}L\Big)dx$ | Bessel expansion theorem: midpoint at a jump |
| $f=x^\nu$ on $[0,1]$ | $a_n=\dfrac2{\alpha_nJ_{\nu+1}(\alpha_n)}$ | $\int t^{\nu+1}J_\nu=t^{\nu+1}J_{\nu+1}$ |
| $f=1$, $\nu=0$ | $a_n=\dfrac{2}{\alpha_nJ_1(\alpha_n)}$ | |
| $f=1-x^2$, $\nu=0$, $L=1$ | $a_n=\dfrac{8}{\alpha_n^3J_1(\alpha_n)}$ | $a_1=1.1080$ |
| Vanishing at $x=L$ | every term is $0$ at $x=L$ | series tends to $0$ there whatever $f(L)$ is |
| Order $\tfrac12$ | $\alpha_k=k\pi$, series = sine series | $\sqrt x=\sum(-1)^{k+1}\sqrt{2/k}\,J_{1/2}(k\pi x)$ |

### 1.6 Reducing an equation to Bessel form (Lecture 26)

$y=x^au(bx^c)$ turns Bessel's equation of order $n$ into
$$y''+\frac{1-2a}xy'+\Big(b^2c^2x^{2c-2}+\frac{a^2-n^2c^2}{x^2}\Big)y=0.$$
Divide your equation by the coefficient of $y''$, then **read** $a$ from the $y'$ term, $c$ and $b$ from the power of $x$ in the $y$ term, and $n$ from the constant over $x^2$. Examples: $y''+xy=0$ (Airy) $\to a=\tfrac12,\ c=\tfrac32,\ b=\tfrac23,\ n=\tfrac13$; $y''+e^{-x}y=0\to y=u(2e^{-x/2})$ of order $0$. For integer $n$ the second solution is $Y_n$, not $J_{-n}$.

---

## 2. Sturm–Liouville problems (Assignment 7)

### 2.1 Form and conversion

| Item | Formula |
|---|---|
| S–L form | $(py')'+(q+\lambda r)y=0$ on $(a,b)$, $\ p>0,\ r>0$; $r$ is the **weight** |
| From $y''+fy'+(g+\lambda h)y=0$ | multiply by $p=e^{\int f}$: $\ q=pg$, $\ r=hp$ |
| Lagrange identity | $uLv-vLu=\big[p(uv'-u'v)\big]'$ with $Lv=(pv')'+qv$ |
| Green's identity | $\int_a^b(uLv-vLu)dx=\big[p(uv'-u'v)\big]_a^b$ |
| Self-adjoint when the boundary term vanishes | separated (Dirichlet, Neumann, Robin), periodic, or a singular end where $p=0$ and $y$ stays bounded |
| Orthogonality | $\lambda_m\ne\lambda_n\Rightarrow\int_a^b r\,y_my_n\,dx=0$; eigenvalues are real |
| Expansion | $f\sim\sum a_ny_n$, $\ a_n=\dfrac{\int_a^brfy_n\,dx}{\int_a^bry_n^2\,dx}$; Parseval $\int rf^2=\sum a_n^2\int ry_n^2$ |
| Convergence | piecewise-smooth $f$: converges to $\tfrac12[f(x^-)+f(x^+)]$; coefficients decay like $n^{-1}$ (jump, or $f$ breaks a boundary condition of the basis), $n^{-2}$, $n^{-3},\dots$ as $f$ meets more of them |

### 2.2 The standard equations and their weights

| Equation | $p$ | $q$ | weight $r$ | eigenvalue |
|---|---|---|---|---|
| Parametric Bessel $x^2y''+xy'+(\lambda^2x^2-m^2)y=0$ | $x$ | $-m^2/x$ | $x$ | $\lambda^2$ |
| Legendre $(1-x^2)y''-2xy'+n(n+1)y=0$ | $1-x^2$ | $0$ | $1$ | $n(n+1)$ |
| Chebyshev $(1-x^2)y''-xy'+n^2y=0$ | $\sqrt{1-x^2}$ | $0$ | $\dfrac1{\sqrt{1-x^2}}$ | $n^2$ |
| Hermite $y''-2xy'+\mu y=0$ | $e^{-x^2}$ | $0$ | $e^{-x^2}$ | $\mu=2n$ |
| Laguerre $xy''+(1-x)y'+\lambda y=0$ | $xe^{-x}$ | $0$ | $e^{-x}$ | $n$ |
| Euler $x^2y''+xy'+\lambda y=0$ | $x$ | $0$ | $\dfrac1x$ | $\lambda$ |
| $y''+\lambda y=0$ | $1$ | $0$ | $1$ | $\lambda$ |

### 2.3 Boundary conditions to eigenfunctions on $[0,L]$ for $y''+\lambda y=0$

![[A610-FB-2-bc-modes.png]]

| Boundary conditions | $\lambda_n$ | $y_n$ | $\int_0^Ly_n^2$ |
|---|---|---|---|
| $y(0)=y(L)=0$ | $(n\pi/L)^2,\ n\ge1$ | $\sin\frac{n\pi x}L$ | $L/2$ |
| $y'(0)=y'(L)=0$ | $(n\pi/L)^2,\ n\ge0$ | $\cos\frac{n\pi x}L$ | $L/2$ ($L$ for $n=0$) |
| $y(0)=0,\ y'(L)=0$ | $\big(\frac{(2n-1)\pi}{2L}\big)^2$ | $\sin\frac{(2n-1)\pi x}{2L}$ | $L/2$ |
| $y'(0)=0,\ y(L)=0$ | $\big(\frac{(2n-1)\pi}{2L}\big)^2$ | $\cos\frac{(2n-1)\pi x}{2L}$ | $L/2$ |
| periodic, $[0,2\pi]$ | $n^2$ (double for $n\ge1$) | $1,\ \cos nx,\ \sin nx$ | $2\pi$ ($\pi$) |
| $y(0)=0,\ y'(L)+hy(L)=0$ | $\mu_n^2$, $\ \tan\mu L=-\mu/h$ | $\sin\mu_nx$ | $\frac L2-\frac{\sin2\mu_nL}{4\mu_n}$ |
| $y(0)=0,\ L\,y'(L)=y(L)$ | $0$ ($y=x$) and $\mu_n^2$, $\ \tan\mu L=\mu L$ | $x$; $\sin\mu_nx$ | the Robin case $h=-1/L$: **a zero eigenvalue appears** (Assignment-style $L=1$: $y(1)=y'(1)$) |

For $h>0$ the Robin problem has only $\lambda>0$; a negative $h$ can admit $\lambda=0$ (at $h=-1/L$) and $\lambda<0$ (beyond it). Always test $\lambda<0$, $\lambda=0$, $\lambda>0$ separately.

### 2.4 Techniques for a non-standard eigenproblem

| Situation | Substitution | Result |
|---|---|---|
| $y''+2ay'+(\lambda+\dots)y=0$, constant coefficients | $y=e^{-ax}z$ | $z''+(\lambda+\dots-a^2)z=0$ |
| Euler: $x^2y''+bxy'+\lambda y$ | $x=e^t$ | constant coefficients in $t$; interval $[x_1,x_2]\to[\ln x_1,\ln x_2]$; $y'$ at $x$ becomes $Y'/x$ |
| $(py')'+\lambda ry=0$ with exponentials or powers | $s=\int\!\sqrt{r/p}\,dx$ | $y_{ss}+\lambda y=0$ (constant factor aside). $p=e^{2x},\ r=e^{-2x}$ gives $s=e^{-2x}$; $p=1+x^2,\ r=\frac1{1+x^2}$ gives $s=\arctan x$ |
| Boundary condition at a singular end ($p(0)=0$) | demand $y$ bounded | not a regular S–L problem; check what the Lagrange boundary term does |
| $z''+\lambda z=0$ on an interval of length $\ell$, Dirichlet both ends | | $\sqrt\lambda=n\pi/\ell$ |

### 2.5 Fourier integrals that appear everywhere (on $[0,L]$, $n\ge1$)

| Integral | Value |
|---|---|
| $\int_0^L\sin\frac{n\pi x}L\,dx$ | $\dfrac{L\big(1-(-1)^n\big)}{n\pi}$ |
| $\int_0^Lx\sin\frac{n\pi x}L\,dx$ | $\dfrac{(-1)^{n+1}L^2}{n\pi}$ |
| $\int_0^Lx^2\sin\frac{n\pi x}L\,dx$ | $\dfrac{(-1)^{n+1}L^3}{n\pi}+\dfrac{2L^3\big((-1)^n-1\big)}{(n\pi)^3}$ |
| $\int_0^Lx(L-x)\sin\frac{n\pi x}L\,dx$ | $\dfrac{2L^3\big(1-(-1)^n\big)}{(n\pi)^3}$ |
| $\int_0^Lx\cos\frac{n\pi x}L\,dx$ | $\dfrac{L^2\big((-1)^n-1\big)}{(n\pi)^2}$ |
| with $\mu_n=(n-\tfrac12)\pi$ on $[0,1]$ | $\int_0^1\sin\mu_nx=\frac1{\mu_n}$, $\ \int_0^1x\sin\mu_nx=\frac{\sin\mu_n}{\mu_n^2}=\frac{(-1)^{n+1}}{\mu_n^2}$ (because $\cos\mu_n=0$) |

| Function on $(0,L)$ | Series |
|---|---|
| $1$ | $\dfrac4\pi\displaystyle\sum_{n\ \mathrm{odd}}\frac1n\sin\frac{n\pi x}L$ |
| $x$ | $\dfrac{2L}\pi\displaystyle\sum_{n\ge1}\frac{(-1)^{n+1}}n\sin\frac{n\pi x}L$ |
| $x(L-x)$ | $\dfrac{8L^2}{\pi^3}\displaystyle\sum_{n\ \mathrm{odd}}\frac1{n^3}\sin\frac{n\pi x}L$ |
| tent, peak $h$ at $\frac L2$ | $\dfrac{8h}{\pi^2}\displaystyle\sum_{n\ \mathrm{odd}}\frac{(-1)^{(n-1)/2}}{n^2}\sin\frac{n\pi x}L$ |
| $x$ (cosine series) | $\dfrac L2-\dfrac{4L}{\pi^2}\displaystyle\sum_{n\ \mathrm{odd}}\frac1{n^2}\cos\frac{n\pi x}L$ |

**Parity shortcuts.** Even-$n$ coefficients vanish when the data are symmetric about $\frac L2$ (sine basis) and odd-$n$ ones when antisymmetric. $\sin\frac{n\pi}2$ kills even $n$; $1-(-1)^n$ kills even $n$; $1+(-1)^n$ kills odd $n$.

---

## 3. First-order PDEs (Assignment 8)

### 3.1 Formation

| Relation | PDE | Rule |
|---|---|---|
| $f(x,y,u,a,b)=0$ (two constants) | first order, usually nonlinear $F(x,y,u,p,q)=0$ | differentiate twice, eliminate $a,b$ |
| $F(\varphi,\psi)=0$ ($\varphi,\psi$ known, $F$ arbitrary) | $Pp+Qq=R$ | $P=\frac{\partial(\varphi,\psi)}{\partial(y,u)},\ Q=\frac{\partial(\varphi,\psi)}{\partial(u,x)},\ R=\frac{\partial(\varphi,\psi)}{\partial(x,y)}$ |
| $u=f(x+y)+g(x-y)$ (two functions) | second order | wave equation $u_{xx}=u_{yy}$ |
| What the count tells you | two constants $\to$ first order (nonlinear); one arbitrary function $\to$ first order, quasi-linear; two arbitrary functions $\to$ second order | $p=u_x,\ q=u_y$ |

### 3.2 Lagrange's method for $P\,p+Q\,q=R$

| Step | Formula |
|---|---|
| Characteristic system | $\dfrac{dx}P=\dfrac{dy}Q=\dfrac{du}R$ |
| General solution | $F(\varphi,\psi)=0$, $\ \varphi=c_1,\ \psi=c_2$ two independent first integrals |
| Check an integral | $P\varphi_x+Q\varphi_y+R\varphi_u\equiv0$ |
| Multipliers | if $\ell P+mQ+nR=0$ then $\ell\,dx+m\,dy+n\,du=0$; if exact, integrate |
| Standard multipliers | $(1,1,1)$, $(x,y,u)$, $(\tfrac1x,\tfrac1y,\tfrac1u)$, $(1,-1,0)$; use a solved first integral to eliminate a variable |
| Linear coefficients | $\dot{\mathbf v}=M\mathbf v$: for a left eigenvector, $\ell\cdot\mathbf v$ satisfies $\frac d{dt}(\ell\cdot\mathbf v)=\lambda\,\ell\cdot\mathbf v$, so ratios like $\ell_2/\ell_1^{\lambda_2/\lambda_1}$ are constant |

### 3.3 Cauchy problem

| Step | Formula |
|---|---|
| Data | $(x_0(s),y_0(s),u_0(s))$ on a curve |
| Constants | substitute into $\varphi=c_1$, $\psi=c_2$, get $c_1(s),c_2(s)$, eliminate $s$ |
| Unique solution near the curve if | $P\,y_0'-Q\,x_0'\ne0$ along the data (transversality) |
| If the data curve is a characteristic | **no solution** unless $u_0'=R\,x_0'/P$ (compatible), then **infinitely many** |
| Burgers $uu_x+u_y=0$, $u(x,0)=u_0(x)$ | $u$ constant on $x=x_0+u_0(x_0)y$; characteristics cross at $y_b=-1/\min u_0'$ (needs $u_0'<0$) |

### 3.4 Complete, general and singular integrals

| Item | Rule |
|---|---|
| Complete integral | $u=f(x,y,a,b)$, two parameters |
| General integral | put $b=\phi(a)$, eliminate $a$ between $f=0$ and $f_a+f_b\phi'=0$ |
| Singular integral | envelope: $f_a=f_b=0$ |
| Clairaut $u=px+qy+g(p,q)$ | complete integral $u=ax+by+g(a,b)$; singular from $x=-g_a$, $y=-g_b$ |
| Example | $u=px+qy+p^2+q^2$: singular integral $u=-\tfrac14(x^2+y^2)$, whose tangent planes are the complete integral |
| $p^2+q^2=1$ | complete $u=ax+\sqrt{1-a^2}\,y+b$; no singular integral ($\partial_b=1\neq0$) |

---

## 4. Second-order PDEs and canonical forms (Assignment 8)

### 4.1 Classification

For $au_{xx}+bu_{xy}+cu_{yy}+\dots=0$ the type depends only on the principal part:

| $\Delta=b^2-4ac$ | Type | Real characteristics | Model | Canonical form |
|---|---|---|---|---|
| $>0$ | hyperbolic | two families | wave | $u_{\xi\eta}+\dots=0$ |
| $=0$ | parabolic | one family | heat | $u_{\eta\eta}+\dots=0$ |
| $<0$ | elliptic | none | Laplace | $u_{\xi\xi}+u_{\eta\eta}+\dots=0$ |

The type is invariant: $B'^2-4A'C'=J^2(b^2-4ac)$ with $J=\xi_x\eta_y-\xi_y\eta_x\ne0$. Type may change from region to region (Tricomi $yu_{xx}+u_{yy}=0$: $\Delta=-4y$).

### 4.2 Reduction

| Step | Formula |
|---|---|
| Characteristic equation | $a\,(dy)^2-b\,dx\,dy+c\,(dx)^2=0$, i.e. $\dfrac{dy}{dx}=\dfrac{b\pm\sqrt\Delta}{2a}$ |
| Hyperbolic | two first integrals $\varphi_1=c,\ \varphi_2=c$; $\ \xi=\varphi_1,\ \eta=\varphi_2$ |
| Parabolic | one integral $\varphi=c$; $\ \xi=\varphi$, $\ \eta$ any independent function (often $x$) |
| Elliptic | complex integral $\varphi=\alpha+i\beta$; $\ \xi=\alpha,\ \eta=\beta$ |
| New coefficients | $A'=a\xi_x^2+b\xi_x\xi_y+c\xi_y^2$, $\ B'=2a\xi_x\eta_x+b(\xi_x\eta_y+\xi_y\eta_x)+2c\xi_y\eta_y$, $\ C'=a\eta_x^2+b\eta_x\eta_y+c\eta_y^2$, $\ D'=a\xi_{xx}+b\xi_{xy}+c\xi_{yy}+d\xi_x+e\xi_y$ ($u_\xi$), $\ E'$ likewise with $\eta$ ($u_\eta$) |
| Last step | divide by the nonzero leading coefficient; rewrite $x,y$ in $\xi,\eta$ |

### 4.3 Solving the canonical form

| Canonical form | General solution |
|---|---|
| $u_{\xi\eta}=0$ | $f(\xi)+g(\eta)$ |
| $u_{\xi\eta}=h(\xi,\eta)$ | integrate twice, add $f(\xi)+g(\eta)$ |
| $u_{\eta\eta}=0$ | $\eta f(\xi)+g(\xi)$ |
| $u_{\xi\eta}-\dfrac{1}{2\eta}u_\xi=0$ | $u_\xi=\sqrt\eta\,h(\xi)$, so $u=\sqrt\eta\,H(\xi)+G(\eta)$ |
| Constant coefficients $au_{xx}+bu_{xy}+cu_{yy}=0$ | $f(y+\lambda_1x)+g(y+\lambda_2x)$ with $a\lambda^2+b\lambda+c=0$; repeated root: $f(y+\lambda x)+xg(y+\lambda x)$; complex: $F(y+\lambda x)+G(y+\bar\lambda x)$ |

### 4.4 Removing first-order terms (constant coefficients)

| Equation | Substitution | Result |
|---|---|---|
| $u_{xx}+u_{yy}+du_x+eu_y+fu=0$ | $u=e^{-dx/2-ey/2}v$ | $v_{xx}+v_{yy}+\big(f-\tfrac{d^2+e^2}4\big)v=0$ |
| $u_{\xi\eta}+du_\xi+eu_\eta+fu=0$ | $u=e^{-e\xi-d\eta}v$ | $v_{\xi\eta}+(f-de)v=0$ |

---

## 5. Wave equation (Assignment 9)

### 5.1 Infinite and semi-infinite string, $u_{tt}=c^2u_{xx}$

| Item | Formula | Remark |
|---|---|---|
| General solution | $u=F(x+ct)+G(x-ct)$ | from $\xi=x+ct$, $\eta=x-ct$: $u_{tt}-c^2u_{xx}=-4c^2u_{\xi\eta}$ |
| d'Alembert | $u=\dfrac{f(x+ct)+f(x-ct)}2+\dfrac1{2c}\displaystyle\int_{x-ct}^{x+ct}g(s)\,ds$ | $u(x,0)=f,\ u_t(x,0)=g$ |
| Domain of dependence | $[x-ct,\,x+ct]$ | signals travel at speed $c$ |
| Half line, $u(0,t)=0$ | **odd** extension of $f,g$ | reflected pulse is inverted; compatibility $f(0)=0$ |
| Half line, $u_x(0,t)=0$ | **even** extension | reflected pulse keeps its sign |
| Incompatible data | a jump travels along $x=ct$ | weak solution |
| Struck string, $f=0$, $g=1$ on $\lvert x\rvert<a$ | $u=\frac1{2c}\,\lvert[x-ct,x+ct]\cap[-a,a]\rvert$ | plateau $a/c$ |

### 5.2 Finite string, length $L$

| Boundary conditions | Modes | Frequencies |
|---|---|---|
| fixed–fixed | $\sin\frac{n\pi x}L$ | $\omega_n=\frac{n\pi c}L$ |
| fixed–free | $\sin\frac{(2n-1)\pi x}{2L}$ | $\omega_n=\frac{(2n-1)\pi c}{2L}$ |
| free–free | $\cos\frac{n\pi x}L$ | $\omega_n=\frac{n\pi c}L$, $n\ge0$ (rigid motion at $n=0$) |

$$u=\sum\Big(A_n\cos\omega_nt+B_n\sin\omega_nt\Big)\varphi_n(x),\qquad A_n=\frac{\int f\varphi_n}{\int\varphi_n^2},\quad B_n=\frac1{\omega_n}\frac{\int g\varphi_n}{\int\varphi_n^2}.$$

| Initial shape (fixed ends, from rest) | $A_n$ |
|---|---|
| plucked at $a$, height $h$ | $\dfrac{2hL^2}{a(L-a)\,n^2\pi^2}\sin\dfrac{n\pi a}L$ (every mode with $\frac{na}L\in\mathbb Z$ is missing) |
| plucked at the middle | $\dfrac{8h}{n^2\pi^2}\sin\dfrac{n\pi}2$ |
| a single sine $\sin\frac{k\pi x}L$ | only $n=k$; products of $\sin\cos$ reduce by $2\sin A\cos B=\sin(A+B)+\sin(A-B)$ |
| velocity impulse $g$ | $B_n=\dfrac2{n\pi c}\displaystyle\int_0^Lg\sin\frac{n\pi x}L\,dx$ |

Energy $\tfrac12\int(\rho u_t^2+Tu_x^2)\,dx$ is **conserved**; $c^2=T/\rho$.

---

## 6. Heat equation (Assignment 9)

### 6.1 Separated solutions, $u_t=c^2u_{xx}$ on $(0,L)$

| Boundary conditions | Series | Long-time limit |
|---|---|---|
| $u=0$ at both ends | $\sum b_n\sin\frac{n\pi x}Le^{-c^2n^2\pi^2t/L^2}$, $\ b_n=\frac2L\int f\sin\frac{n\pi x}L$ | $0$ |
| $u_x=0$ at both ends | $A_0+\sum A_n\cos\frac{n\pi x}Le^{-c^2n^2\pi^2t/L^2}$, $\ A_0=\frac1L\int f$ | the **mean** $A_0$ (heat is conserved) |
| $u(0)=0,\ u_x(L)=0$ | $\sum b_n\sin\frac{(2n-1)\pi x}{2L}e^{-c^2(2n-1)^2\pi^2t/4L^2}$ | $0$ |
| Radiating end $u_x(L)=-hu(L)$ | $\sum b_n\sin\mu_nx\,e^{-c^2\mu_n^2t}$, $\ \tan\mu_nL=-\mu_n/h$ | $0$ |

Slowest mode: $\tau_1=\dfrac{L^2}{c^2\pi^2}$. Mode $n$ decays $n^2$ times faster. For large $t$ the first surviving mode dominates, so $t\approx\tau_1\ln(\text{amplitude ratio})$.

### 6.2 Non-homogeneous problems: subtract a simple solution

| Data | Subtract | Then solve |
|---|---|---|
| ends held at $A$ and $B$ | $w=A+\frac{B-A}Lx$ | $v=u-w$ with zero ends and $v(x,0)=f-w$ |
| ends changed suddenly (old steady $w_0$, new steady $w_1$) | $w_1$ | $v(x,0)=w_0-w_1$ |
| one end held at $A$, other insulated | $w=A$ | $v$ with mixed (Dirichlet–Neumann) basis |
| constant source: $u_t=c^2u_{xx}+Q$ | $w''=-Q/c^2$ with the boundary data | $v_t=c^2v_{xx}$, $\ v(x,0)=f-w$ |
| flux ends $u_x(0)=\alpha$, $u_x(L)=\beta$ | $w=\alpha x+\frac{\beta-\alpha}{2L}x^2+\frac{c^2(\beta-\alpha)}Lt$ | **no steady state** unless $\alpha=\beta$: the mean rises at $c^2(\beta-\alpha)/L$ |

**Symmetry.** If $f-w$ is antisymmetric about the midpoint (for example the old and new steady lines cross there), only even-$n$ sine modes appear, they all vanish at the midpoint, and $u(\tfrac L2,t)$ keeps its initial value for all $t$. Antisymmetry about the midpoint is preserved by the heat and wave equations.

**Maximum principle.** The extreme values of $u$ occur at $t=0$ or on the ends, never strictly inside at a later time. Backward heat flow is ill-posed (the high modes would grow like $e^{+c^2n^2\pi^2t/L^2}$); the wave equation runs both ways.

---

## 7. Laplace equation (Assignment 10)

### 7.1 Rectangle $0<x<a,\ 0<y<b$ and strips

| Driven edge | Others | Solution term | Coefficient |
|---|---|---|---|
| top $y=b$: $u=f(x)$ | $0$ | $\sin\frac{n\pi x}a\,\dfrac{\sinh\frac{n\pi y}a}{\sinh\frac{n\pi b}a}$ | $\frac2a\int_0^af\sin\frac{n\pi x}a$ |
| bottom $y=0$: $u=f(x)$ | $0$ | $\sin\frac{n\pi x}a\,\dfrac{\sinh\frac{n\pi(b-y)}a}{\sinh\frac{n\pi b}a}$ | same |
| left or right edge driven | $0$ | swap $x\leftrightarrow y$, $a\leftrightarrow b$ | |
| two or more driven edges | | **add** the one-edge solutions | |
| a side insulated ($u_n=0$) | | use $\cos$ (or $\cosh$ with zero slope: $\cosh\frac{n\pi(y-b)}a$) and include $n=0$ | the $n=0$ term is the mean |
| semi-infinite strip $y\to\infty$ | bounded | $\sin\frac{n\pi x}ae^{-n\pi y/a}$ (or $\cos$ if insulated) | decay length $\frac a{n\pi}$ |

Rule of thumb: the **zero pair** of opposite edges gets the sines; the **other direction** gets $\sinh$ vanishing on the opposite zero edge. Neumann compatibility: $\oint\partial_nu\,ds=0$, and then $u$ is unique only up to a constant.

### 7.2 Polar coordinates

| Item | Formula |
|---|---|
| Laplacian | $u_{rr}+\dfrac1ru_r+\dfrac1{r^2}u_{\theta\theta}=0$ |
| Separated | $\Theta''+\lambda\Theta=0$, $\ r^2R''+rR'-\lambda R=0$ ($R=r^{\pm\sqrt\lambda}$; $\lambda=0$: $A+B\ln r$) |
| Disk $r<a$, $u(a,\theta)=f$ | $u=\dfrac{a_0}2+\sum\Big(\dfrac ra\Big)^n(a_n\cos n\theta+b_n\sin n\theta)$; bounded at $0$ drops $r^{-n},\ln r$ |
| Poisson integral | $u=\dfrac1{2\pi}\displaystyle\int_0^{2\pi}\frac{a^2-r^2}{a^2-2ar\cos(\theta-\phi)+r^2}f(\phi)\,d\phi$ |
| Mean value | $u(0)=\dfrac1{2\pi}\int f$; every interior value lies between $\min f$ and $\max f$ |
| Exterior $r>a$, bounded at $\infty$ | $\dfrac{a_0}2+\sum\big(\frac ar\big)^n(\dots)$ |
| Annulus $a<r<b$ | $(A_nr^n+B_nr^{-n})$ and $A_0+B_0\ln r$; match both circles |
| Sector / half or quarter disk, $0<\theta<\alpha$, zero on the rays | $r^{n\pi/\alpha}\sin\frac{n\pi\theta}\alpha$; $\ b_n=\frac2\alpha\int_0^\alpha f\sin\frac{n\pi\theta}\alpha$ |
| Radial data only | $u=A+B\ln r$ |
| Closed forms from summing the series | arc data $f=1$ on half the circle: $u=\tfrac12+\tfrac1\pi\arctan\dfrac{2r\sin\theta}{1-r^2}$; quarter disk, $u=1$ on the arc: $u=\tfrac2\pi\arctan\dfrac{2r^2\sin2\theta}{1-r^4}$ |
| Maximum principle | extremes on the boundary; uniqueness for Dirichlet data |

---

## 8. One set of modes, three behaviours

![[A610-FB-3-mode-factors.png]]

| Equation | Factor multiplying the $n$-th spatial mode | Meaning |
|---|---|---|
| Wave $u_{tt}=c^2u_{xx}$ | $\cos\frac{n\pi ct}L,\ \sin\frac{n\pi ct}L$ | oscillates, no decay, frequency $\propto n$ |
| Heat $u_t=c^2u_{xx}$ | $e^{-c^2n^2\pi^2t/L^2}$ | decays, rate $\propto n^2$: smoothing |
| Laplace $u_{xx}+u_{yy}=0$ | $\sinh\frac{n\pi y}L$ or $e^{-n\pi y/L}$ | decays **in space**, rate $\propto n$ |

The eigenfunctions are the same S–L eigenfunctions in all three; only the equation for the other variable changes ($T''+\omega^2T=0$, $T'+\lambda T=0$, $Y''-\lambda Y=0$). Cross-domain bridges: wave ↔ [[The Universal Second-Order Linear System]]; heat ↔ [[Exponential Decay - Time Constants, Damping and Spatial Relaxation]]; separation of variables ↔ [[Eigenvalues, Rotation and Diagonalization Everywhere]].

---

## 9. Numbers worth knowing

| Quantity | Value |
|---|---|
| Zeros of $J_0$ | $2.4048,\ 5.5201,\ 8.6537,\ 11.7915,\ 14.9309$ |
| Zeros of $J_1$ | $3.8317,\ 7.0156,\ 10.1735,\ 13.3237,\ 16.4706$ |
| Zeros of $J_2$ | $5.1356,\ 8.4172,\ 11.6198,\ 14.7960,\ 17.9598$ |
| $J_0(2),\ J_1(2)$ | $0.22389,\ 0.57672$ |
| $J_0(1),\ J_1(1),\ J_2(1)$ | $0.76520,\ 0.44005,\ 0.11490$ |
| $J_{1/2},\ \Gamma(\tfrac12)$ | $\sqrt{2/\pi x}\sin x$, $\ \sqrt\pi$ |
| Roots of $\tan\mu=\mu$ | $4.4934,\ 7.7253,\ 10.9041,\ 14.0662$ |
| Roots of $\mu\tan\mu=1$ | $0.8603,\ 3.4256,\ 6.4373,\ 9.5293$ |
| Odd-$n$ sums | $\sum n^{-2}=\pi^2/8$, $\ \sum n^{-3}=7\zeta(3)/8$; $\ \sum_{k\ge0}\frac{(-1)^k}{(2k+1)^3}=\pi^3/32$, $\ \sum_{k\ge0}\frac{(-1)^k}{2k+1}=\pi/4$ |
| Gibbs overshoot | about $9\%$ of the jump |
| Copper diffusivity | $1.11\times10^{-4}$ m²/s |

## Errors that cost marks

| Error | Fix |
|---|---|
| $J_{-n}$ as a second solution for integer order | use $Y_n$; $J_{-n}=(-1)^nJ_n$ |
| Forgetting the weight $x$ in a Fourier–Bessel coefficient | $\int_0^Lx\,f\,J_\nu$, norm $\frac{L^2}2J_{\nu+1}^2$ |
| Trusting an antiderivative of $\int x^pJ_\nu$ | differentiate it; a sign slip is the usual error |
| Missing $\lambda=0$ (Neumann, or Robin with the "wrong" sign) | test $\lambda<0,=0,>0$ separately |
| Boundary condition at a singular endpoint treated as regular | demand bounded, check $p(0)=0$ |
| Using $\sin$ where the condition is Neumann | Neumann ⇒ $\cos$, include $n=0$ |
| Odd extension used for a free end (or even for fixed) | fixed ⇒ odd, free ⇒ even |
| $B_n$ without the factor $\frac1{\omega_n}$ | $B_n\omega_n$ matches the **velocity** coefficient |
| Expanding $f$ instead of $f-w$ after subtracting a steady state | the series carries the **difference** |
| $\sinh(n\pi y/a)$ with the wrong denominator | divide by $\sinh(n\pi b/a)$, aspect ratio $b/a$ |
| $r^{-n}$ kept in a disk (or $r^n$ outside) | bounded at the centre / at infinity decides |
| Type classified with lower-order terms or the nonlinear right-hand side | only $a,b,c$ of the principal part |

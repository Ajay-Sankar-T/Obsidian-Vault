---
title: DE Question Bank 2 – First-Order PDEs and Canonical Forms
course: MA 2102 Differential Equations
tags: [DE, question-bank, tutorial]
up: "[[Assignments 6-10 - Question Bank]]"
aliases: [first order PDE practice problems, canonical form practice problems, Lagrange method practice, DE question bank 2, Assignment 8 practice]
---

# DE Question Bank 2 — First-Order PDEs and Canonical Forms

Part of [[Assignments 6-10 - Question Bank]] · formulas: [[Assignments 6-10 - Formula Bank]] (§3–§4) · method: [[Assignments 6-10 - How to Solve]] (§4–§5) · solved sheet: [[Assignment 8 - First Order PDEs and Canonical Forms - Solutions]] · theory: [[Formation of PDEs - Eliminating Constants and Functions]], [[Lagrange's Method for Quasi-linear PDEs]], [[Cauchy Problem for First Order PDEs]], [[Complete, General and Singular Integrals]], [[Classification of Second Order PDEs]], [[Canonical Forms of Second Order PDEs]]

> [!abstract] What is here
> Ten conceptual questions (Part A) and ten numerical problems (Q1–Q10), none of them on the assignment sheet. Try each on paper; open **Hint** only if stuck, then **Solution**. Every closed form was substituted into its PDE and data (symbolically) in `Tools/de_a610_bank_pdes.py` (functions `p2_q1` … `p2_q10`).

## Part A — Conceptual questions

> [!question]- A1. Distinguish complete, general and singular integrals of a first-order PDE.
> The **complete integral** $u=f(x,y,a,b)$ has two parameters. The **general integral** is the envelope of the one-parameter subfamily $b=\phi(a)$ (eliminate $a$ between $f=0$ and $f_a+f_b\phi'=0$), one arbitrary function. The **singular integral** is the envelope of the whole two-parameter family ($f_a=f_b=0$); it is a solution that is in general not in the complete integral and not in the general integral.

> [!question]- A2. Why does a quasi-linear first-order PDE have a general solution $F(\varphi,\psi)=0$ with one arbitrary function?
> The vector $(P,Q,R)$ is tangent to every integral surface, so an integral surface is a union of curves solving $\frac{dx}P=\frac{dy}Q=\frac{du}R$ (**characteristics**). These curves are the intersections $\varphi=c_1$, $\psi=c_2$. Choosing which curves to include is choosing a relation between $c_1$ and $c_2$, that is $F(c_1,c_2)=0$: one arbitrary function of one variable.

> [!question]- A3. Why do the multipliers $(\ell,m,n)$ with $\ell P+mQ+nR=0$ give $\ell\,dx+m\,dy+n\,du=0$?
> Along a characteristic $dx:dy:du=P:Q:R$, so $\ell\,dx+m\,dy+n\,du$ is proportional to $\ell P+mQ+nR=0$. If the combination is an exact differential, its integral is a first integral. Choosing $(1,1,1)$, $(x,y,u)$, $(\frac1x,\frac1y,\frac1u)$ is a way of testing for exactness quickly.

> [!question]- A4. When does the Cauchy problem for $Pp+Qq=R$ have a unique solution near a data curve?
> When the projection of the data curve is **transversal** to the characteristic projection: $P\,y_0'-Q\,x_0'\ne0$ along the curve. If the curve is itself a characteristic ($P y_0'-Qx_0'=0$) there are two cases: the data are compatible ($u_0'=Rx_0'/P$), and then there are **infinitely many** solutions; or they are not, and there is **none**.

> [!question]- A5. Why do solutions of $uu_x+u_y=0$ develop discontinuities?
> $u$ is constant along its characteristics, which are **straight lines** $x=x_0+u_0(x_0)y$ with slope depending on $u_0$. Where $u_0$ is decreasing, characteristics from different $x_0$ converge, and they cross at $y_b=-1/\min u_0'$. After that $u$ would be multivalued, so a smooth solution ceases to exist (a shock). Linear equations ($u_x+cu_y=0$) have parallel characteristics and never break.

> [!question]- A6. What does the type (hyperbolic, parabolic, elliptic) of a second-order PDE tell you about its solutions?
> The number of real characteristic directions: two (hyperbolic: waves, finite propagation speed, sharp fronts), one (parabolic: diffusion, infinite speed, smoothing), none (elliptic: equilibrium, smooth interior, maximum principle). The type also decides the right data: initial values for hyperbolic and parabolic problems, boundary values around a closed curve for elliptic ones.

> [!question]- A7. Why is the type independent of the choice of coordinates?
> Under $(x,y)\to(\xi,\eta)$ the principal coefficients change as $A'=a\xi_x^2+b\xi_x\xi_y+c\xi_y^2$, etc., and one finds $B'^2-4A'C'=J^2(b^2-4ac)$ with $J=\xi_x\eta_y-\xi_y\eta_x\ne0$. $J^2>0$, so the sign of $\Delta$ is preserved. Classification is a property of the PDE, not of the coordinate system.

> [!question]- A8. Why is the general solution of $u_{\xi\eta}=0$ equal to $f(\xi)+g(\eta)$, and that of $u_{\eta\eta}=0$ equal to $\eta f(\xi)+g(\xi)$?
> $(u_\xi)_\eta=0$ means $u_\xi$ does not depend on $\eta$: $u_\xi=F(\xi)$, so $u=\int F\,d\xi+g(\eta)$. For $u_{\eta\eta}=0$ integrate twice in $\eta$ only, so the "constants" are functions of the other variable: $u=\eta f(\xi)+g(\xi)$.

> [!question]- A9. Why can first-order terms be removed by $u=e^{\alpha x+\beta y}v$ only when the coefficients are constant?
> Differentiating $e^{\alpha x+\beta y}v$ produces constant multiples of $v$ and of $v_x,v_y$ only when $\alpha,\beta$ are constants. The choice $\alpha=-\frac d2$, $\beta=-\frac e2$ then kills $v_x,v_y$ and shifts the zeroth-order coefficient to $f-\frac{d^2+e^2}4$. With variable coefficients the required exponent would depend on $x,y$ and generate new first-order terms; in general, no such change removes them (Euler–Poisson–Darboux terms remain).

> [!question]- A10. A family of surfaces has two arbitrary constants. What order is the PDE you form, and why is it usually nonlinear?
> Differentiating once gives $p,q$ (two equations plus the relation itself, three equations in $a,b$); eliminating $a,b$ leaves a **first-order** relation $F(x,y,u,p,q)=0$. It is linear in $p,q$ only if $a,b$ enter in a special way (e.g. $u=ax+by+ab$ gives $u=px+qy+pq$, which is nonlinear). By contrast, one arbitrary **function** gives a quasi-linear equation and two arbitrary functions give a second-order equation.

---

## Q1 — Forming PDEs (easy)

Eliminate the constants or the function: (a) $u=ax+a^2y+b$; (b) $u=x\,f\!\big(y/x^2\big)$; (c) $(x-a)^2+(y-b)^2=u^2$.

> [!tip]- Hint
> Compute $p=u_x$ and $q=u_y$. For (a) eliminate $a,b$; for (b) eliminate $f$ and $f'$; for (c) first find $x-a$ and $y-b$ in terms of $p,q$.

> [!success]- Solution
> (a) $p=a$, $q=a^2$, so $\boxed{q=p^2}$. (The constant $b$ drops out immediately.)
>
> (b) With $\eta=y/x^2$: $p=f-2\eta f'$, $q=f'/x$. Then $f'=xq$, $f=u/x$, so $p=\frac ux-\frac{2y}{x^2}\,xq$, i.e. $xp=u-2yq$:
>
> $\displaystyle \boxed{xp+2yq=u}$
>
> (c) $2(x-a)=2u\,p$ and $2(y-b)=2u\,q$, so $x-a=up$, $y-b=uq$. Substituting: $u^2(p^2+q^2)=u^2$, hence $\boxed{p^2+q^2=1}$ (the eikonal equation: the surfaces are cones with $45^\circ$ half-angle).
>
> All three were verified by substituting a generic member symbolically.

## Q2 — A symmetric Lagrange system (medium)

Find the general solution of $(y-u)p+(u-x)q=x-y$, describe the characteristics geometrically, and verify that the plane $u=-(x+y)$ is a solution (which member of the family is it?).

> [!tip]- Hint
> Try the multipliers $(1,1,1)$ and $(x,y,u)$: both annihilate the coefficients.

> [!success]- Solution
> $\frac{dx}{y-u}=\frac{dy}{u-x}=\frac{du}{x-y}$.
>
> Multipliers $(1,1,1)$: $(y-u)+(u-x)+(x-y)=0$, so $d(x+y+u)=0$: $\varphi=x+y+u=c_1$.
>
> Multipliers $(x,y,u)$: $x(y-u)+y(u-x)+u(x-y)=0$, so $x\,dx+y\,dy+u\,du=0$: $\psi=x^2+y^2+u^2=c_2$.
>
> $\displaystyle \boxed{F\big(x+y+u,\ x^2+y^2+u^2\big)=0}$
>
> Each characteristic is the intersection of a plane perpendicular to $(1,1,1)$ with a sphere centred at the origin: a **circle about the axis $x=y=u$**. The integral surfaces are the surfaces of revolution about that axis.
>
> The plane $u=-(x+y)$ is the member $c_1=0$ of the family (a plane perpendicular to the axis $x=y=u$, the flattest surface of revolution). Check: $p=q=-1$, $y-u=x+2y$, $u-x=-2x-y$, so $(x+2y)(-1)+(-2x-y)(-1)=-x-2y+2x+y=x-y$ ✓.

## Q3 — A solution through given data (medium)

Solve $xp+yq=u+x^2$ with $u(1,y)=y^2$.

> [!tip]- Hint
> $\frac{dx}x=\frac{dy}y=\frac{du}{u+x^2}$. The first pair gives $y/x$; then $\frac{du}{dx}=\frac{u+x^2}x$ is linear in $u$.

> [!success]- Solution
> $\frac yx=c_1$. With $y=c_1x$: $\frac{du}{dx}-\frac ux=x\Rightarrow\Big(\frac ux\Big)'=1\Rightarrow\frac ux=x+c_2$, i.e. $\varphi_2=\frac ux-x$. General solution: $u=x^2+x\,g(y/x)$.
>
> Data on $x=1$: $u=1+g(y)=y^2\Rightarrow g(s)=s^2-1$.
>
> $\displaystyle \boxed{u=x^2+x\Big(\frac{y^2}{x^2}-1\Big)=x^2+\frac{y^2}x-x}$
>
> **Check:** $u_x=2x-\frac{y^2}{x^2}-1$, $u_y=\frac{2y}x$; $xu_x+yu_y=2x^2-\frac{y^2}x-x+\frac{2y^2}x=2x^2+\frac{y^2}x-x=u+x^2$ ✓, and $u(1,y)=1+y^2-1=y^2$ ✓. The data curve $x=1$ is transversal ($P=x\ne0$ there), so the solution is unique.

## Q4 — A Cauchy problem, and data on a characteristic (medium)

(a) Solve $u_x+u_y=u$, $u(x,0)=\sin x$. (b) On the line $y=x$, how many solutions are there if $u(s,s)=e^s$? If $u(s,s)=1$?

> [!tip]- Hint
> $\frac{dx}1=\frac{dy}1=\frac{du}u$: $x-y=c_1$, $ue^{-x}=c_2$. In (b) the data line is itself a characteristic base curve.

> [!success]- Solution
> (a) General solution $u=e^xG(x-y)$. On $y=0$: $e^xG(x)=\sin x\Rightarrow G(s)=e^{-s}\sin s$. So $u=e^xe^{-(x-y)}\sin(x-y)$:
>
> $\displaystyle \boxed{u=e^y\sin(x-y)}$
>
> **Check:** $u_x=e^y\cos(x-y)$, $u_y=e^y\sin(x-y)-e^y\cos(x-y)$; the sum is $e^y\sin(x-y)=u$ ✓.
>
> (b) On $y=x$: $c_1=0$, so $u(s,s)=e^sG(0)$. If the data are $e^s$ the only condition is $G(0)=1$: **infinitely many** solutions $u=e^xG(x-y)$ with $G(0)=1$ (the data are compatible, since along the characteristic $du/ds=u$ and $e^s$ obeys it). If the data are $1$ the requirement $e^sG(0)=1$ for all $s$ is impossible: **no solution**. Geometrically the space curve $(s,s,u_0(s))$ is a characteristic when $u_0'=u_0$, and otherwise it cannot lie on any integral surface.

## Q5 — When does a smooth solution cease to exist? (medium)

(a) Solve $uu_x+u_y=0$, $u(x,0)=-x$, and say where and when it breaks. (b) What happens for $u(x,0)=x$? (c) For $u(x,0)=-\sin x$ find the breaking "time" $y_b$.

> [!tip]- Hint
> Along $\frac{dx}u=\frac{dy}1$ one has $u=$ constant, so $x=x_0+u_0(x_0)\,y$.

> [!success]- Solution
> (a) $u=-x_0$ and $x=x_0-x_0y=x_0(1-y)$, so $\boxed{u=-\dfrac x{1-y}}$ for $y<1$. At $y=1$ all characteristics pass through $x=0$: the slope $u_x=-\frac1{1-y}\to-\infty$ (see the figure).
>
> (b) $x=x_0(1+y)$, $u=\dfrac x{1+y}$: the characteristics fan out, no breaking for $y>0$.
>
> (c) $y_b=-1/\min u_0'$ with $u_0'=-\cos x_0$, minimum $-1$: **$y_b=1$**, first at $x_0=0,2\pi,\dots$.
>
> **Rule:** breaking occurs iff $u_0'<0$ somewhere, at $y_b=-1/\min u_0'$.

## Q6 — Complete and singular integrals (medium)

(a) Find the complete and singular integrals of $u=px+qy+p^2+q^2$ and show that each plane of the complete integral touches the singular surface. (b) Does $p^2+q^2=1$ have a singular integral?

> [!tip]- Hint
> Clairaut form $u=px+qy+g(p,q)$: complete integral $u=ax+by+g(a,b)$. The singular integral eliminates $a,b$ from $f_a=f_b=0$.

> [!success]- Solution
> (a) Complete integral $u=ax+by+a^2+b^2$. $f_a=x+2a=0$, $f_b=y+2b=0$, so $a=-\frac x2$, $b=-\frac y2$:
>
> $\displaystyle \boxed{u=-\tfrac{x^2}2-\tfrac{y^2}2+\tfrac{x^2}4+\tfrac{y^2}4=-\tfrac14\big(x^2+y^2\big)}$
>
> **Check** in the PDE: $p=-\frac x2$, $q=-\frac y2$; $px+qy+p^2+q^2=-\frac{x^2+y^2}2+\frac{x^2+y^2}4=-\frac{x^2+y^2}4=u$ ✓.
>
> Tangency: at $(x,y)=(-2a,-2b)$ the paraboloid has $u=-a^2-b^2$ and gradient $(a,b)$, and the plane $u=ax+by+a^2+b^2$ gives $a(-2a)+b(-2b)+a^2+b^2=-a^2-b^2$ with the same gradient: the plane touches the paraboloid there.
>
> (b) Complete integral $u=ax+\sqrt{1-a^2}\,y+b$. $f_b=1\ne0$ so $f_a=f_b=0$ has no solution: **no singular integral**. (The general integral still gives cones and developable surfaces.)

## Q7 — Type and regions (medium)

Classify $(1-x^2)u_{xx}-2xy\,u_{xy}-(1+y^2)u_{yy}=0$ and describe the regions.

> [!tip]- Hint
> $a=1-x^2$, $b=-2xy$, $c=-(1+y^2)$. Compute $b^2-4ac$ and factor.

> [!success]- Solution
> $\Delta=4x^2y^2+4(1-x^2)(1+y^2)=4\big(1+y^2-x^2\big)$.
>
> - **Hyperbolic** where $x^2-y^2<1$ (the band between the two branches).
> - **Parabolic** on the hyperbola $x^2-y^2=1$.
> - **Elliptic** where $x^2-y^2>1$ (outside the branches, $|x|>\sqrt{1+y^2}$).
>
> Samples: $(0,0)$: $\Delta=4>0$; $(1,0)$: $\Delta=0$; $(2,0)$: $\Delta=-12<0$.

## Q8 — Canonical form with variable coefficients (hard)

Reduce $x^2u_{xx}-y^2u_{yy}=0$ ($x,y>0$) to canonical form and find the general solution.

> [!tip]- Hint
> Characteristic equation $a\,dy^2-b\,dx\,dy+c\,dx^2=0$ with $a=x^2$, $b=0$, $c=-y^2$. Then use the chain-rule coefficients; the result is integrable in $\eta$.

> [!success]- Solution
> $\Delta=4x^2y^2>0$: hyperbolic. $x^2dy^2-y^2dx^2=0\Rightarrow\frac{dy}y=\pm\frac{dx}x$, so $\xi=\dfrac yx$, $\eta=xy$.
>
> Coefficients: $A'=x^2\frac{y^2}{x^4}-y^2\frac1{x^2}=0$, $C'=x^2y^2-y^2x^2=0$, $B'=2x^2\big(-\tfrac y{x^2}\big)y+2(-y^2)\tfrac1x\,x=-4y^2$. First-order terms: $D'=x^2\xi_{xx}+(-y^2)\xi_{yy}=x^2\cdot\frac{2y}{x^3}=\frac{2y}x$ (coefficient of $u_\xi$), $E'=0$ (since $\eta_{xx}=\eta_{yy}=0$).
>
> So $-4y^2u_{\xi\eta}+\frac{2y}xu_\xi=0$. Divide by $-4y^2$ and use $xy=\eta$:
>
> $\displaystyle \boxed{u_{\xi\eta}-\frac1{2\eta}\,u_\xi=0}$
>
> Integrate in $\eta$: $u_\xi=h(\xi)\sqrt\eta$, then in $\xi$:
>
> $\displaystyle \boxed{u=\sqrt{xy}\,H\!\Big(\frac yx\Big)+G(xy)}$
>
> **Check:** $u=\sqrt{xy}$: $x^2u_{xx}=-\frac14\sqrt{xy}=y^2u_{yy}$ ✓; $u=xy$: $u_{xx}=u_{yy}=0$ ✓. Generic $H,G$ were substituted symbolically.

## Q9 — A parabolic equation with Cauchy data (medium)

Solve $u_{xx}-6u_{xy}+9u_{yy}=0$ with $u(x,0)=x^2$, $u_y(x,0)=0$.

> [!tip]- Hint
> $\Delta=0$. $\frac{dy}{dx}=\frac b{2a}=-3$, so $\xi=y+3x$; take $\eta=x$. The canonical form is $u_{\eta\eta}=0$.

> [!success]- Solution
> $(\partial_x-3\partial_y)^2u=0$. $\xi=y+3x$, $\eta=x$ gives $u_{\eta\eta}=0$ (coefficients $A'=B'=D'=E'=0$, $C'=1$), so
>
> $\displaystyle u=f(y+3x)+x\,g(y+3x).$
>
> Data: $f(3x)+xg(3x)=x^2$ and $u_y(x,0)=f'(3x)+xg'(3x)=0$. With $s=3x$: $f+\frac s3g=\frac{s^2}9$ and $f'+\frac s3g'=0$. Differentiating the first and subtracting the second: $\frac g3=\frac{2s}9$, so $g=\frac{2s}3$, $f=\frac{s^2}9-\frac s3\cdot\frac{2s}3=-\frac{s^2}9$.
>
> $\displaystyle u=-\frac{(y+3x)^2}9+x\cdot\frac23(y+3x)=\boxed{x^2-\frac{y^2}9}$
>
> **Check:** $u_{xx}=2$, $u_{xy}=0$, $u_{yy}=-\frac29$: $2-0+9\left(-\frac29\right)=0$ ✓; $u(x,0)=x^2$ ✓; $u_y(x,0)=-\frac{2y}9\big|_{y=0}=0$ ✓.

## Q10 — Removing the first-order terms (medium)

Show that $u_{xx}+u_{yy}+6u_x-8u_y+25u=0$ reduces to Laplace's equation, and give a nontrivial solution.

> [!tip]- Hint
> Put $u=e^{\alpha x+\beta y}v$ with $\alpha=-\frac d2$, $\beta=-\frac e2$ and compute the new constant $f-\frac{d^2+e^2}4$.

> [!success]- Solution
> $d=6$, $e=-8$, $f=25$: $\alpha=-3$, $\beta=4$, and the zeroth-order coefficient becomes $25-\frac{36+64}4=0$. So $u=e^{-3x+4y}v$ with
>
> $\displaystyle v_{xx}+v_{yy}=0.$
>
> Taking the harmonic $v=x^2-y^2$ (or $\operatorname{Re}z^2$): $u=e^{-3x+4y}(x^2-y^2)$, which satisfies the original PDE (substituted symbolically).
>
> **Remark:** if the coefficient of $u$ were $26$ the reduced equation would be $v_{xx}+v_{yy}+v=0$ (Helmholtz); the choice $25$ is exactly the value $\frac{d^2+e^2}4$.

![[A610-QB-2-pde.png]]

**Figure.** Left: Q5, characteristics of $uu_x+u_y=0$ with $u(x,0)=-x$ meet at $(0,1)$. Middle: profiles at $y=0,0.5,0.9$ steepen without bound. Right: Q7, the type regions.

## Mixed practice

| Skill | Questions |
|---|---|
| Forming a PDE, counting constants and functions | Q1, A10 |
| Lagrange: pairs of ratios, multipliers | Q2, Q3 |
| Cauchy data and transversality | Q3, Q4, A4 |
| Characteristic data, none or infinitely many | Q4 |
| Breaking of solutions | Q5, A5 |
| Clairaut and envelopes | Q6, A1 |
| Classification regions | Q7, A6, A7 |
| Canonical form, variable coefficients | Q8 |
| Parabolic: general solution and data | Q9 |
| First-order terms removal | Q10, A9 |

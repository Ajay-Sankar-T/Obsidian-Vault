---
title: DE Question Bank 3 – Wave, Heat and Laplace Equations
course: MA 2102 Differential Equations
tags: [DE, question-bank, tutorial]
up: "[[Assignments 6-10 - Question Bank]]"
aliases: [wave heat Laplace practice problems, separation of variables practice, DE question bank 3, Assignments 9 and 10 practice]
---

# DE Question Bank 3 — Wave, Heat and Laplace Equations

Part of [[Assignments 6-10 - Question Bank]] · formulas: [[Assignments 6-10 - Formula Bank]] (§5–§8) · method: [[Assignments 6-10 - How to Solve]] (§6–§8) · solved sheets: [[Assignment 9 - D'Alembert, Wave and Heat Equations - Solutions]], [[Assignment 10 - Laplace Equations - Solutions]] · theory: [[D'Alembert's Solution of the Wave Equation]], [[Separation of Variables]], [[Wave Equation on a Finite Interval]], [[Heat Equation - Separation of Variables]], [[Laplace Equation on Rectangles and Strips]], [[Laplace Equation in Polar Coordinates]]

> [!abstract] What is here
> Twelve conceptual questions (Part A) and fourteen numerical problems (Q1–Q14): four on the wave equation, four on heat, six on Laplace. None is on the assignment sheets. Try each on paper; open **Hint** only if stuck, then **Solution**. Every number was recomputed in `Tools/de_a610_bank_pdes.py` (functions `p3_q1` … `p3_q14`): d'Alembert solutions by direct evaluation, series by quadrature and by a brute-force sum, and Q7 and Q8 also by a finite-difference simulation.

## Part A — Conceptual questions

> [!question]- A1. State the domain of dependence and of influence for $u_{tt}=c^2u_{xx}$. What does it say about a string struck on $|x|<1$?
> $u(x,t)$ depends only on $f$ at $x\pm ct$ and on $g$ on $[x-ct,x+ct]$ (**dependence**); data at $x_0$ influence only $|x-x_0|\le ct$ (**influence**). A string struck on $|x|<1$ is undisturbed outside $|x|<1+ct$; the front moves at speed $c$, and (since $\int g\ne0$) the string does **not** return to zero but is left raised on a plateau spreading outward.

> [!question]- A2. Why does a fixed end invert a pulse and a free end not?
> Fixed end $u(0,t)=0$: the odd extension makes the image pulse negative, so the reflected pulse is inverted. Free end $u_x(0,t)=0$: the even extension gives a positive image, so the reflected pulse keeps its sign. At the end point the incoming and image pulses cancel (fixed) or add (free).

> [!question]- A3. Why does $B_n$ in $u=\sum(A_n\cos\omega_nt+B_n\sin\omega_nt)\varphi_n$ carry a factor $\frac1{\omega_n}$?
> $u_t(x,0)=\sum B_n\omega_n\varphi_n(x)$, so the **velocity** data $g$ determine $B_n\omega_n$ (its Fourier coefficient), not $B_n$. Dividing by $\omega_n=n\pi c/L$ makes $B_n$ decay one power of $n$ faster than the coefficients of $g$.

> [!question]- A4. The wave equation conserves energy, the heat equation dissipates it. How does this show up in the series solutions?
> The wave factors $\cos\omega_nt,\sin\omega_nt$ have constant amplitude, so $\sum\frac12(\dots)$ is conserved, and the equation can be solved backwards in time. Heat factors $e^{-c^2n^2\pi^2t/L^2}$ decay, faster for larger $n$: high-frequency detail is erased (smoothing), and running time backwards would multiply the $n$-th coefficient by $e^{+c^2n^2\pi^2t/L^2}$, which amplifies noise without bound (ill-posed).

> [!question]- A5. How does the cooling time of a rod scale with its length and diffusivity?
> The slowest mode has $\tau_1=\frac{L^2}{c^2\pi^2}$. Doubling $L$ multiplies the time by $4$; a material with ten times the diffusivity cools ten times faster. After a few $\tau_1$ only the first mode survives, so $t\approx\tau_1\ln\frac{\text{initial amplitude}}{\text{target}}$.

> [!question]- A6. Why subtract a steady state before using separation of variables? What if the boundary values depend on time?
> Separation of variables needs **homogeneous** boundary conditions so that eigenfunctions can be superposed. $w$ carries the inhomogeneous data; $v=u-w$ then has zero boundary data. If the boundary values vary with time, $w(x,t)$ (for example a line between the two boundary values) is subtracted instead and generates a source term in $v_t=c^2v_{xx}-w_t$, handled by Duhamel or eigenfunction expansion.

> [!question]- A7. A rod has fluxes $u_x(0)=\alpha$ and $u_x(L)=\beta$ prescribed at the ends. When is there a steady state?
> Only if $\alpha=\beta$: the net heat entering per unit time is $c^2(\beta-\alpha)$, so the **mean temperature** rises at the rate $c^2(\beta-\alpha)/L$ (integrate $u_t=c^2u_{xx}$ over the rod). A steady state requires zero net flux. The shift $w=\alpha x+\frac{\beta-\alpha}{2L}x^2+\frac{c^2(\beta-\alpha)}Lt$ solves the equation and the flux conditions.

> [!question]- A8. State the maximum principle for the heat equation and for Laplace's equation.
> Heat: on $[0,L]\times[0,T]$ the maximum and minimum of $u$ are attained on the bottom ($t=0$) or the sides ($x=0$ or $L$), not strictly inside at a later time. Laplace: in a bounded region the extreme values are on the boundary. Consequences: uniqueness of the Dirichlet problems and continuous dependence on the data.

> [!question]- A9. Why does the Neumann problem for Laplace's equation need a compatibility condition and have a non-unique solution?
> $\int_\Omega\nabla^2u=\oint\partial_nu\,ds$, so Neumann data must have zero total flux. If $u$ is a solution so is $u+C$. Physically, heat can only be in steady state if the heat entering equals the heat leaving, and the level of the temperature is not fixed by the flux alone.

> [!question]- A10. In a rectangle with one driven edge, how do you decide which direction gets $\sin$ and which gets $\sinh$?
> The $\sin$ (eigenfunction) direction is the one with **two homogeneous** boundary conditions (a Sturm–Liouville problem needs a pair of zero conditions). The other direction satisfies $Y''=\lambda Y$ with $\lambda>0$: $\sinh$ or $\cosh$, built so that it vanishes (Dirichlet) or has zero slope (Neumann) on the opposite undriven edge, and normalised by $\sinh$ at the driven edge.

> [!question]- A11. State the mean value property and use it to explain what $u(0)$ is in the disk problem.
> For a harmonic $u$, the value at the centre of a disk equals the average over its boundary circle (and over every concentric circle). In $u=\frac{a_0}2+\sum r^n(\dots)$ every $r^n$ term with $n\ge1$ averages to zero over $\theta$, so $u(0)=\frac{a_0}2=\frac1{2\pi}\int_0^{2\pi}f\,d\theta$. Also $\min f\le u\le\max f$ throughout the disk.

> [!question]- A12. What happens to the solution of Laplace's equation near the corner of a sector of opening $\alpha>\pi$?
> With $u=0$ on both rays the leading solution is $r^{\pi/\alpha}\sin\frac{\pi\theta}\alpha$. For $\alpha>\pi$ the exponent $\frac\pi\alpha<1$, so $|\nabla u|\sim r^{\pi/\alpha-1}\to\infty$ at the corner (for a slit, $\alpha=2\pi$, $u\sim\sqrt r$; for an L-shape, $\alpha=\frac{3\pi}2$, $u\sim r^{2/3}$): a **re-entrant corner singularity**. For $\alpha<\pi$ the gradient is bounded or zero.

---

## Q1 — A struck infinite string (easy)

$u_{tt}=u_{xx}$ on $\mathbb R$ ($c=1$), $u(x,0)=0$, $u_t(x,0)=1$ for $|x|<1$ and $0$ otherwise. Find $u(0,0.5)$, $u(0.5,1)$, $u(1.5,1)$, $u(2,1)$, $u(0,3)$, and the final profile.

> [!tip]- Hint
> $u=\frac12\int_{x-t}^{x+t}g(s)\,ds$ = half the length of $[x-t,x+t]\cap[-1,1]$.

> [!success]- Solution
> $u(x,t)=\tfrac12\,\big|[x-t,\,x+t]\cap[-1,1]\big|$.
>
> $u(0,0.5)$: $[-0.5,0.5]$, length $1$: $\mathbf{0.5}$. $u(0.5,1)$: $[-0.5,1.5]\cap[-1,1]=[-0.5,1]$, length $1.5$: $\mathbf{0.75}$. $u(1.5,1)$: $[0.5,2.5]\cap=[0.5,1]$, length $0.5$: $\mathbf{0.25}$. $u(2,1)$: $[1,3]\cap=\{1\}$, length $0$: $\mathbf0$ (the front $x=1+t=2$ has just arrived). $u(0,3)$: $[-3,3]\supset[-1,1]$: $\mathbf1$.
>
> **Final profile:** once $t\ge|x|+1$ the interval contains $[-1,1]$ and $u=\frac12\cdot2=1$: a raised plateau of height $1$ whose edges travel outward at speed $1$ (the plateau height is $\frac1{2c}\int g$). The string does not return to rest.

## Q2 — A pulse hits a fixed wall (medium)

$u_{tt}=u_{xx}$ on $x>0$, $u(0,t)=0$, $u(x,0)=f(x)=1$ for $1<x<2$ and $0$ otherwise, $u_t(x,0)=0$. Find $u(0.5,1)$, $u(0.5,2)$, $u(1.5,3)$ and describe the motion.

> [!tip]- Hint
> Odd extension $f_o(s)=f(s)$ for $s>0$, $-f(-s)$ for $s<0$; $u=\frac12[f_o(x+t)+f_o(x-t)]$.

> [!success]- Solution
> $f_o=+1$ on $(1,2)$ and $-1$ on $(-2,-1)$.
>
> $u(0.5,1)$: $x+t=1.5\Rightarrow1$; $x-t=-0.5\Rightarrow0$. $u=\mathbf{0.5}$.
>
> $u(0.5,2)$: $x+t=2.5\Rightarrow0$; $x-t=-1.5\Rightarrow-1$. $u=\mathbf{-0.5}$.
>
> $u(1.5,3)$: $x+t=4.5\Rightarrow0$; $x-t=-1.5\Rightarrow-1$. $u=\mathbf{-0.5}$.
>
> **Motion:** the initial pulse splits into two half-height pulses. The right-moving one is on $[1+t,2+t]$. The left-moving one reaches the wall at $t=1$, overlaps its inverted image from $t=1$ to $t=2$ (they cancel exactly; the pulse is centred on the wall at $t=1.5$), and then re-emerges as an **inverted** pulse of height $\frac12$ on $[t-2,t-1]$ for $t\ge2$. $u(0,t)=0$ throughout (see the figure at the end).

## Q3 — A plucked string (medium)

A string of length $L$ is pulled aside at $x=\frac L4$ to height $h$ and released from rest. (a) Show $A_n=\dfrac{32h}{3n^2\pi^2}\sin\dfrac{n\pi}4$. (b) Find $A_1,\dots,A_4$ (in units of $h$) and say which modes are missing. (c) What fraction of the energy is in the fundamental?

> [!tip]- Hint
> General pluck at $a$: $A_n=\frac{2hL^2}{a(L-a)n^2\pi^2}\sin\frac{n\pi a}L$. Energy in mode $n$ is proportional to $\omega_n^2A_n^2\propto n^2A_n^2$. Use $\sum_{n\ge1}\frac{\sin^2n\pi a}{n^2}=\frac{\pi^2a(1-a)}2$.

> [!success]- Solution
> (a) Integrate $f$ by parts on both linear pieces (kink at $a=\frac L4$): $A_n=\frac2L\int_0^Lf\sin\frac{n\pi x}L=\frac{2hL^2}{a(L-a)n^2\pi^2}\sin\frac{n\pi a}L$. With $a=\frac L4$: $a(L-a)=\frac{3L^2}{16}$, so $A_n=\dfrac{32h}{3n^2\pi^2}\sin\dfrac{n\pi}4$ ✓ (verified against quadrature for $n=1\dots8$).
>
> (b) $A_1=0.7642h$, $A_2=0.2702h$, $A_3=0.0849h$, $A_4=0$. Every $n$ divisible by $4$ is **missing**: the pluck point is a node of those modes ($\sin\frac{n\pi}4=0$).
>
> (c) $E_n\propto n^2A_n^2\propto\frac{\sin^2(n\pi/4)}{n^2}$. $\sum_nE_n\propto\frac{\pi^2}2\cdot\frac14\cdot\frac34=\frac{3\pi^2}{32}=0.9253$, and $E_1\propto\frac12$. Fraction $=\dfrac{0.5}{0.9253}=\mathbf{54\%}$.
>
> **Check:** plucking at the centre ($a=\frac L2$) gives $A_n=\frac{8h}{n^2\pi^2}\sin\frac{n\pi}2$, the result of Assignment 9 Q5.

## Q4 — A bar given a uniform velocity (hard)

A string or bar of length $L$ is fixed at $x=0$ and free at $x=L$. At $t=0$, $u=0$ and $u_t=v_0$ everywhere. (a) Find $u(x,t)$. (b) Find the tip displacement $u(L,t)$ and its maximum.

> [!tip]- Hint
> Fixed–free modes $\sin\mu_nx$, $\mu_n=\frac{(2n-1)\pi}{2L}$, $\omega_n=c\mu_n$; $B_n\omega_n\cdot\frac L2=\int_0^Lv_0\sin\mu_nx\,dx$ (use $\cos\mu_nL=0$).

> [!success]- Solution
> $\int_0^Lv_0\sin\mu_nx\,dx=\frac{v_0}{\mu_n}$ (since $\cos\mu_nL=0$), so $B_n=\dfrac2L\cdot\dfrac{v_0}{\mu_n\omega_n}=\dfrac{2v_0}{Lc\mu_n^2}$:
>
> $\displaystyle \boxed{u=\sum_{n\ge1}\frac{8v_0L}{c\,\pi^2(2n-1)^2}\sin\frac{(2n-1)\pi x}{2L}\sin\frac{(2n-1)\pi ct}{2L}}$
>
> Tip: $\sin\mu_nL=(-1)^{n+1}$. At $t=L/c$, $\sin\omega_nt=(-1)^{n+1}$ too, so every term is positive: $u(L,\tfrac Lc)=\sum B_n=\frac{8v_0L}{c\pi^2}\cdot\frac{\pi^2}8=\dfrac{v_0L}c$.
>
> The tip displacement is a **triangle wave** of period $\frac{4L}c$: it rises at slope $v_0$ to $\frac{v_0L}c$ at $t=\frac Lc$, returns to $0$ at $\frac{2L}c$ and reaches $-\frac{v_0L}c$ at $\frac{3L}c$ (series: $0.99999$ at $t=L/c$, $0$ at $2L/c$, $-1$ at $3L/c$ for $v_0=L=c=1$).
>
> **Physical reading:** until the wave from the fixed end reaches the tip ($t=L/c$), the tip is unaware and moves at $v_0$; then the reflected stress wave reverses its velocity.

## Q5 — Cooling a copper rod (medium)

A copper rod ($c^2=1.11\times10^{-4}$ m²/s) of length $0.4$ m is at $100^\circ$ and its ends are held at $0^\circ$. (a) Find $\tau_1$. (b) How long until the **centre** falls to $50^\circ$? To $5^\circ$? (c) Is one mode enough?

> [!tip]- Hint
> $u(\tfrac L2,t)=\sum_{n\ \mathrm{odd}}\frac{400}{n\pi}\sin\frac{n\pi}2e^{-n^2t/\tau_1}$, $\tau_1=\frac{L^2}{\pi^2c^2}$. First solve with one term.

> [!success]- Solution
> (a) $\tau_1=\dfrac{0.16}{\pi^2(1.11\times10^{-4})}=\mathbf{146.0\ s}$.
>
> (b) One mode: $\frac{400}\pi e^{-t/\tau_1}=50\Rightarrow t=\tau_1\ln\frac8\pi=146.05(0.9347)=\mathbf{136.5\ s}$. For $5^\circ$: $t=\tau_1\ln\frac{80}\pi=146.05(3.2377)=\mathbf{472.8\ s}$.
>
> (c) The full series gives $136.49$ s and $472.80$ s. At $t=136$ s the $n=3$ term is $\frac13e^{-8t/\tau_1}=1.9\times10^{-4}$ of the first, so one mode is enough once $t$ is more than about a minute. (At $t=0$ the first mode alone gives $\frac{400}\pi=127$, not $100$: the formula is an estimate for later times only.)
>
> **Scaling:** a rod of length $0.8$ m would take four times as long.

## Q6 — An insulated rod with a sinusoidal start (easy)

$u_t=c^2u_{xx}$ on $(0,L)$, $u_x=0$ at both ends, $u(x,0)=\sin^2\frac{\pi x}L$. Solve exactly and find how long until the non-constant part is $1\%$ of its initial size.

> [!tip]- Hint
> $\sin^2\theta=\frac12-\frac12\cos2\theta$ is already a combination of the Neumann eigenfunctions $\cos\frac{n\pi x}L$ with $n=0,2$.

> [!success]- Solution
> $\displaystyle \boxed{u=\frac12-\frac12\cos\frac{2\pi x}L\,e^{-4\pi^2c^2t/L^2}}$
>
> (substituted into the PDE, both Neumann conditions and the initial value symbolically.) The mean is $\frac12$ for all $t$: heat is conserved.
>
> The oscillating part is $e^{-4\pi^2c^2t/L^2}$ times its initial value; set $=0.01$: $t=\dfrac{L^2\ln100}{4\pi^2c^2}=\mathbf{0.1167\,\dfrac{L^2}{c^2}}$. For the copper rod ($L=0.4$ m, $c^2=1.11\times10^{-4}$) this is about $168$ s.

## Q7 — A mixed boundary problem (medium)

$u_t=u_{xx}$ on $(0,1)$, $u(0,t)=a$, $u_x(1,t)=0$, $u(x,0)=0$. Find $u$, the value at the insulated end at $t=0.5$, and the time at which that end reaches $\frac a2$.

> [!tip]- Hint
> Steady state $w=a$. For $v=u-a$ the conditions are $v(0)=0$, $v_x(1)=0$: eigenfunctions $\sin\frac{(2n-1)\pi x}2$.

> [!success]- Solution
> $w=a$; $v(x,0)=-a$; $b_n=2\int_0^1(-a)\sin\mu_nx\,dx=-\frac{2a}{\mu_n}=-\frac{4a}{(2n-1)\pi}$ with $\mu_n=\frac{(2n-1)\pi}2$:
>
> $\displaystyle \boxed{u=a\Big[1-\frac4\pi\sum_{n\ge1}\frac1{2n-1}\sin\frac{(2n-1)\pi x}2\,e^{-(2n-1)^2\pi^2t/4}\Big]}$
>
> At $t=0$ the series is the square-wave series ($=\frac\pi4$ on $0<x<1$), so $u=0$ ✓.
>
> Insulated end $x=1$: $\sin\frac{(2n-1)\pi}2=(-1)^{n+1}$: $u(1,0.5)=a\big[1-\frac4\pi\big(e^{-\pi^2/8}-\tfrac13e^{-9\pi^2/8}+\dots\big)\big]=\mathbf{0.6292\,a}$.
>
> Half time: $\frac4\pi e^{-\pi^2t/4}=\frac12\Rightarrow t=\frac4{\pi^2}\ln\frac8\pi=\mathbf{0.379}$ (full series $0.3787$).
>
> A finite-difference simulation of the PDE agrees to $2\times10^{-3}$.

## Q8 — Heat with a source (medium)

$u_t=u_{xx}+2$ on $(0,1)$, $u(0,t)=u(1,t)=0$, $u(x,0)=0$. Find $u$, $u(\tfrac12,0.1)$, and the time for the centre to reach $90\%$ of its steady value.

> [!tip]- Hint
> Steady state: $w''=-2$, $w(0)=w(1)=0$. Then $v=u-w$ solves the homogeneous heat equation with $v(x,0)=-w$.

> [!success]- Solution
> $w=x(1-x)$. $v(x,0)=-x(1-x)$ and $b_n=-2\int_0^1x(1-x)\sin n\pi x\,dx=-\frac{4\big(1-(-1)^n\big)}{(n\pi)^3}$, i.e. $-\frac8{(n\pi)^3}$ for odd $n$:
>
> $\displaystyle \boxed{u=x(1-x)-\sum_{n\ \mathrm{odd}}\frac8{n^3\pi^3}\sin n\pi x\;e^{-n^2\pi^2t}}$
>
> Centre: $u(\tfrac12,t)=\frac14-\frac8{\pi^3}\big(e^{-\pi^2t}-\frac1{27}e^{-9\pi^2t}+\dots\big)$. At $t=0.1$: $\frac14-0.2580(0.3727)=\mathbf{0.1538}$.
>
> $90\%$ of $\frac14$: $\frac8{\pi^3}e^{-\pi^2t}=0.025\Rightarrow e^{-\pi^2t}=0.0969\Rightarrow t=\mathbf{0.2365}$.
>
> (Checked by finite differences: $0.1538$.)

## Q9 — A rectangle with an aspect ratio (medium)

Solve $\nabla^2u=0$ on $0<x<2$, $0<y<1$ with $u(x,1)=x(2-x)$ and $u=0$ on the other three sides. Find $u(1,\tfrac12)$.

> [!tip]- Hint
> Sines in $x$ (zero pair $x=0,2$), $\sinh\frac{n\pi y}2$ vanishing at $y=0$. Coefficient: $b_n=\int_0^2x(2-x)\sin\frac{n\pi x}2dx\big/\sinh\frac{n\pi}2$.

> [!success]- Solution
> $\int_0^2x(2-x)\sin\frac{n\pi x}2dx=\frac{2L^3(1-(-1)^n)}{(n\pi)^3}\Big|_{L=2}=\frac{16(1-(-1)^n)}{(n\pi)^3}$, and $\frac2a=1$, so $b_n=\dfrac{32}{(n\pi)^3}$ for odd $n$:
>
> $\displaystyle \boxed{u=\sum_{n\ \mathrm{odd}}\frac{32}{n^3\pi^3\,\sinh\frac{n\pi}2}\sin\frac{n\pi x}2\sinh\frac{n\pi y}2}$
>
> At $y=1$: $\sum\frac{32}{n^3\pi^3}\sin\frac{n\pi x}2=x(2-x)$ ✓. At $(1,\frac12)$: $n=1$: $\frac{32}{\pi^3}\cdot\frac{\sinh(\pi/4)}{\sinh(\pi/2)}=1.0321(0.3775)=0.3896$; $n=3$: $-\frac{32}{27\pi^3}\cdot\frac{\sinh(3\pi/4)}{\sinh(3\pi/2)}=-0.0036$; $n=5$: $+0.0002$:
>
> $\displaystyle u(1,\tfrac12)=\mathbf{0.3861}.$
>
> Also $u(1,\tfrac14)=0.1797$, $u(1,\tfrac34)=0.6486$ (the profile rises steeply near the driven edge). **Check:** the edge value at $y=1$ is $1\cdot1=1$ at $x=1$, and the interior values lie between $0$ and $1$ (maximum principle).

## Q10 — An insulated bottom (hard)

On the square $0<x,y<\pi$: $u(0,y)=u(\pi,y)=0$, the bottom is insulated ($u_y(x,0)=0$), and the top is $u(x,\pi)=x$. Find $u$ and evaluate $u(\tfrac\pi2,\tfrac\pi2)$ and $u(\tfrac\pi2,0)$. Comment on convergence.

> [!tip]- Hint
> $\sin nx$ in $x$. In $y$ the solution with zero slope at $y=0$ is $\cosh ny$. Normalise by $\cosh n\pi$ so the top is the sine series of $x$.

> [!success]- Solution
> $b_n=\frac2\pi\int_0^\pi x\sin nx\,dx=\frac{2(-1)^{n+1}}n$.
>
> $\displaystyle \boxed{u=\sum_{n\ge1}\frac{2(-1)^{n+1}}n\,\sin nx\,\frac{\cosh ny}{\cosh n\pi}}$
>
> $u_y(x,0)=0$ ✓ (even function of $y$), $u(0,y)=u(\pi,y)=0$ ✓, $u(x,\pi)=x$ ✓.
>
> $u(\tfrac\pi2,\tfrac\pi2)=\mathbf{0.4271}$, $u(\tfrac\pi2,0)=\mathbf{0.1724}$, and $u(\tfrac\pi2,\pi)=\frac\pi2$ (the data).
>
> **Convergence:** the data $x$ equals $\pi$ at the corner $x=\pi$ while the side condition says $u(\pi,y)=0$: incompatible. The coefficients decay only like $\frac1n$ and the sum converges slowly near the top-right corner, but the factor $\frac{\cosh ny}{\cosh n\pi}\approx e^{-n(\pi-y)}$ makes it converge fast anywhere with $y<\pi$.

## Q11 — A disk, and its exterior (easy)

(a) Solve $\nabla^2u=0$ in $r<1$ with $u(1,\theta)=\sin^3\theta$; find $u(\tfrac12,\tfrac\pi2)$, $u(0)$ and $\max u$. (b) Solve the exterior problem $r>1$, $u(1,\theta)=1+\cos\theta$, $u$ bounded at infinity.

> [!tip]- Hint
> $\sin^3\theta=\frac14(3\sin\theta-\sin3\theta)$. Interior: $r^n$; exterior: $r^{-n}$.

> [!success]- Solution
> (a) $u(1,\theta)=\frac34\sin\theta-\frac14\sin3\theta$, so
>
> $\displaystyle \boxed{u=\tfrac34r\sin\theta-\tfrac14r^3\sin3\theta}.$
>
> $u(\tfrac12,\tfrac\pi2)=\tfrac34\cdot\tfrac12\cdot1-\tfrac14\cdot\tfrac18\cdot(-1)=0.375+0.03125=\mathbf{0.40625}$. $u(0)=0$ (the mean of $\sin^3$). The maximum is $1$, attained on the boundary at $\theta=\frac\pi2$ (maximum principle; confirmed on a grid).
>
> (b) Exterior, bounded: $u=\dfrac{a_0}2+\sum r^{-n}(\dots)$, and the data contain only $n=0,1$:
>
> $\displaystyle \boxed{u=1+\frac{\cos\theta}r}$
>
> $u(2,0)=1.5$. As $r\to\infty$, $u\to1$ (the mean of the boundary data).

## Q12 — Temperature between two cylinders (easy)

A long hollow cylinder has inner radius $1$ held at $1^\circ$ and outer radius $2$ held at $3^\circ$. Find the steady temperature, its value at $r=1.5$ and at $r=\sqrt2$, and compare with a linear guess.

> [!tip]- Hint
> Radial solution of Laplace's equation: $u_{rr}+\frac1ru_r=0$, so $u=A+B\ln r$.

> [!success]- Solution
> $u(1)=1\Rightarrow A=1$; $u(2)=1+B\ln2=3\Rightarrow B=\frac2{\ln2}$:
>
> $\displaystyle \boxed{u=1+\frac{2\ln r}{\ln2}}$
>
> $u(1.5)=1+2\cdot0.58496=\mathbf{2.1699}$. $u(\sqrt2)=1+2\cdot\frac12=\mathbf2$: the **geometric** mean radius carries the **arithmetic** mean temperature. The linear guess $1+2(r-1)$ gives $2$ at $r=1.5$, too low: the logarithm is concave (heat flux $\propto\frac1r$, steep near the inner surface where the area is small).
>
> The radial flux $r\,u_r=\frac2{\ln2}$ is constant: the same total heat crosses every circle.

## Q13 — A quarter disk with a closed form (hard)

On the quarter disk $0<r<1$, $0<\theta<\frac\pi2$: $\nabla^2u=0$, $u=0$ on the two radii and $u(1,\theta)=1$. (a) Find the series. (b) Sum it. (c) Find $u$ on the bisector $\theta=\frac\pi4$ and evaluate at $r=0.8$.

> [!tip]- Hint
> Sector of opening $\alpha=\frac\pi2$: $r^{2k}\sin2k\theta$. Sum with $\sum_{k\ \mathrm{odd}}\frac{z^k}k=\frac12\ln\frac{1+z}{1-z}$, $z=r^2e^{2i\theta}$.

> [!success]- Solution
> (a) $b_k=\frac2{\pi/2}\int_0^{\pi/2}\sin2k\theta\,d\theta=\frac{2(1-(-1)^k)}{\pi k}$:
>
> $\displaystyle u=\frac4\pi\sum_{k\ \mathrm{odd}}\frac{r^{2k}}k\sin2k\theta.$
>
> (b) $\operatorname{Im}\tfrac12\ln\frac{1+z}{1-z}=\tfrac12\arg\frac{1+z}{1-z}=\tfrac12\arctan\frac{2\operatorname{Im}z}{1-|z|^2}$:
>
> $\displaystyle \boxed{u=\frac2\pi\arctan\frac{2r^2\sin2\theta}{1-r^4}}$
>
> As $r\to1$ with $0<\theta<\frac\pi2$ the argument $\to\infty$ and $u\to1$ ✓; on $\theta=0,\frac\pi2$, $u=0$ ✓. (The closed form was checked against the series and for $\nabla^2u=0$.)
>
> (c) At $\theta=\frac\pi4$: $\frac{2r^2}{1-r^4}=\tan\big(2\arctan r^2\big)$, so
>
> $\displaystyle u(r,\tfrac\pi4)=\frac4\pi\arctan r^2.$
>
> $u(0.8,\tfrac\pi4)=\frac4\pi\arctan0.64=1.2732(0.5693)=\mathbf{0.7249}$; $u(0.5,\tfrac\pi4)=0.3119$.

## Q14 — Half-circle boundary data (hard)

In $r<1$ let $\nabla^2u=0$ with $u(1,\theta)=1$ for $0<\theta<\pi$ and $0$ for $\pi<\theta<2\pi$. (a) Find $u(0)$. (b) Find the series and its closed form. (c) Evaluate $u$ at $(r,\theta)=(0.5,\tfrac\pi2)$, $(0.9,\tfrac\pi2)$, $(0.5,\tfrac{3\pi}2)$ and check $u(r,\theta)+u(r,-\theta)=1$.

> [!tip]- Hint
> $a_0/2=\frac12$, $a_n=0$, $b_n=\frac1\pi\int_0^\pi\sin n\theta\,d\theta$. Sum as in Q13 with $z=re^{i\theta}$.

> [!success]- Solution
> (a) $u(0)=\frac1{2\pi}\int f=\mathbf{\frac12}$ (mean value property).
>
> (b) $b_n=\frac{1-(-1)^n}{n\pi}$:
>
> $\displaystyle u=\frac12+\frac2\pi\sum_{n\ \mathrm{odd}}\frac{r^n}n\sin n\theta=\boxed{\frac12+\frac1\pi\arctan\frac{2r\sin\theta}{1-r^2}}$
>
> (matches the Poisson integral at $(0.5,\tfrac\pi2)$ to $10^{-9}$).
>
> (c) On the vertical axis $\theta=\frac\pi2$: $\frac{2r}{1-r^2}=\tan(2\arctan r)$, so $u=\frac12+\frac2\pi\arctan r$. $u(0.5,\tfrac\pi2)=0.5+0.6366(0.4636)=\mathbf{0.7952}$; $u(0.9,\tfrac\pi2)=\mathbf{0.9665}$ (approaching the boundary value $1$); $u(0.5,\tfrac{3\pi}2)=\mathbf{0.2048}$.
>
> Symmetry: $\arctan$ is odd, so $u(r,-\theta)=1-u(r,\theta)$: $0.7952+0.2048=1$ ✓.

![[A610-QB-3-waves-heat.png]]

**Figure.** Q1: the struck string leaves a spreading plateau. Q2: the pulse is reflected and inverted (at $t=1.5$ the incoming and image cancel near the wall). Q3: the modes $n=4,8$ are absent. Q5: centre temperature against time (the dashed first-mode curve is right after about a minute). Q8: the profile approaches $x(1-x)$. Q13: contours of the harmonic function on the quarter disk.

## Mixed practice

| Skill | Questions |
|---|---|
| d'Alembert on the line and half line | Q1, Q2, A1, A2 |
| Fourier modes of a string, parity, energy | Q3, Q4, A3, A4 |
| Heat: times and scaling | Q5, Q6, A5 |
| Steady-state shift, mixed conditions, sources | Q7, Q8, A6, A7 |
| Laplace on a rectangle | Q9, Q10, A10 |
| Laplace in polar coordinates | Q11, Q12, Q13, Q14, A11, A12 |
| Maximum principle, mean value | Q11, Q14, A8, A11 |

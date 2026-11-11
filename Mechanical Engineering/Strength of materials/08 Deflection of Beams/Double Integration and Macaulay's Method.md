Related: [[Flexure Formula]] · [[Relations Between Load, Shear, and Moment]] · [[Moment-Area Method]]

## The Governing Differential Equation

From [[Flexure Formula]], curvature $1/\rho=M/(EI)$. For small deflections $v(x)$, curvature $\approx d^2v/dx^2$, giving the **Euler-Bernoulli beam equation**:
$$EI\frac{d^2v}{dx^2} = M(x)$$
Combined with $dM/dx=V$, $dV/dx=-w$ (see [[Relations Between Load, Shear, and Moment]]):
$$EI\frac{d^3v}{dx^3}=V(x), \qquad EI\frac{d^4v}{dx^4}=-w(x)$$

![[SM-C-double-integration.png]]

**Figure:** from the moment diagram, integrate $M/EI$ once for slope and again for deflection. The constants come from the supports. Here the maximum deflection is $5wL^4/384EI$.

## Double Integration Method

Given $M(x)$ (from a shear-moment analysis, [[Shear Force and Bending Moment Diagrams]]), integrate twice:
$$EI\frac{dv}{dx}=\int M(x)\,dx + C_1, \qquad EIv(x)=\int\!\!\int M(x)\,dx\,dx + C_1x+C_2$$
$C_1,C_2$ are fixed by **boundary conditions**:
- Fixed (built-in) support: $v=0$ and $dv/dx=0$.
- Pin/roller support: $v=0$.
- Free end: no displacement condition (but $M=0,V=0$ there feed into the moment expression itself).
- Symmetry: $dv/dx=0$ at the point of symmetry.

For beams with several load segments, $M(x)$ has a different algebraic expression on each segment, requiring separate integration constants per segment — matched by continuity of $v$ and $dv/dx$ at segment boundaries. This quickly becomes unwieldy with many segments, motivating **Macaulay's method**.

## Macaulay's Method (Singularity Functions)

Write the bending moment as a **single expression** valid over the whole beam, using **Macaulay brackets** $\langle x-a\rangle^n$, defined to be zero whenever $x<a$:
$$\langle x-a\rangle^n = \begin{cases}(x-a)^n & x\ge a\\ 0 & x<a\end{cases}$$
A point load $P$ at $x=a$ contributes $P\langle x-a\rangle^1$ to $M(x)$; a point moment $M_0$ at $x=a$ contributes $M_0\langle x-a\rangle^0$; a UDL $w$ starting at $x=a$ (running to the end) contributes $\dfrac{w}{2}\langle x-a\rangle^2$.

Integrating termwise (treating each bracket like $(x-a)^n$ for the purposes of integration, but re-inserting the "zero if $x<a$" rule after integrating) gives a **single** $v(x)$ expression valid for the whole beam, with just **two** constants of integration determined from the overall boundary conditions — no segment-matching required. This is the standard hand-calculation method for beams with multiple point loads/moments.

## Superposition

Since the governing equation is linear, deflections and slopes from several simultaneous loads can be **added** from tabulated results for standard single-load cases (cantilever with tip load, simply-supported beam with center load, etc.) — a fast method when the beam matches known standard cases.

## Check yourself

> [!question]- Q1. A simply supported beam ($L=4$ m, $w=10$ kN/m, $E=200$ GPa, $I=8\times10^{-5}$ m⁴) is uniformly loaded. Find the midspan deflection.
> $v_{max}=5wL^4/(384EI)=2.08$ mm.

> [!question]- Q2. State the boundary conditions for a cantilever and a simply supported beam.
> Cantilever: $v=0$ and $v'=0$ at the wall. Simply supported: $v=0$ at both supports.

> [!question]- Q3. What is the cantilever tip deflection under an end load $P$?
> $v=PL^3/(3EI)$.

---
Next: [[Moment-Area Method]]

## Worked examples
[[Tutorial 8 - Deflection of Beams|Tutorial 8 — Deflection of Beams]]: stepped cantilever, couple on a simple beam, singularity-function beams and Castigliano problems, worked with figures.

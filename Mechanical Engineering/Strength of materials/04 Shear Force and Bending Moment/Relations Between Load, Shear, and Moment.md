Related: [[Shear Force and Bending Moment Diagrams]] · [[Double Integration and Macaulay's Method]]

## Differential Relations

Consider a beam element of length $dx$ under distributed load $w(x)$ (positive downward, by convention, or upward — be consistent). Equilibrium of the element gives:
$$\frac{dV}{dx} = -w(x), \qquad \frac{dM}{dx} = V(x)$$
(sign conventions vary by textbook; the essential content is that **slope of $V$ = intensity of distributed load**, and **slope of $M$ = shear force**.)

Combining:
$$\frac{d^2M}{dx^2} = -w(x)$$

![[SM-C-load-shear-moment.png]]

**Figure:** one integration turns the load into the shear diagram, a second turns shear into moment. Each curve is one degree higher than the one before it.

## Integral (Area) Form — Fast Diagram Construction

These differential relations integrate to area relations, which are the fast way to sketch diagrams by hand:
$$V_B-V_A = -\int_A^B w(x)\,dx = -(\text{area under load diagram between }A,B)$$
$$M_B-M_A = \int_A^B V(x)\,dx = (\text{area under shear diagram between }A,B)$$

## Consequences Used Constantly in Practice

- Where $w=0$ (no load), $V$ is **constant** and $M$ varies **linearly**.
- Where $w$ is uniform (constant), $V$ varies **linearly** and $M$ varies **quadratically** (parabolic).
- Where $w$ varies linearly, $V$ is quadratic and $M$ is cubic.
- At a point load, $V$ jumps by the load magnitude; $M$ has a **corner** (slope discontinuity) there.
- At a point moment, $M$ jumps by the moment magnitude; $V$ is unaffected.
- **Maximum $|M|$ occurs where $V=0$** (or changes sign), since $dM/dx=V$.

These relations are exactly what makes [[Double Integration and Macaulay's Method]] work: integrating $w(x)$ twice gives $M(x)$ (up to constants fixed by boundary conditions on $V,M$), and integrating $M(x)/EI$ twice more gives the beam's deflection.

## Check yourself

> [!question]- Q1. A cantilever of length $L$ carries a uniform load $w$. Find the shear and moment at the wall.
> $V=wL$ and $M=-wL^2/2$ (hogging), the largest values on the beam.

> [!question]- Q2. A shear diagram is a straight line falling at 5 kN/m. What is the load?
> $dV/dx=-w$, so a uniform downward load of 5 kN/m.

> [!question]- Q3. A moment diagram jumps by 20 kN·m at a point. What is applied there?
> A concentrated couple of 20 kN·m. Point forces give corners in $M$ and jumps in $V$. Couples give jumps in $M$ and leave $V$ unchanged.

---
Next: [[Flexure Formula]]

## See also
- [[Q8 - Elastically Supported Bar]] — the same differential-equilibrium structure for axial load.

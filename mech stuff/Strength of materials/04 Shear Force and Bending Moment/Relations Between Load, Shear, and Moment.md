Related: [[Shear Force and Bending Moment Diagrams]] · [[Double Integration and Macaulay's Method]]

## Differential Relations

Consider a beam element of length $dx$ under distributed load $w(x)$ (positive downward, by convention, or upward — be consistent). Equilibrium of the element gives:
$$\frac{dV}{dx} = -w(x), \qquad \frac{dM}{dx} = V(x)$$
(sign conventions vary by textbook; the essential content is that **slope of $V$ = intensity of distributed load**, and **slope of $M$ = shear force**.)

Combining:
$$\frac{d^2M}{dx^2} = -w(x)$$

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

---
Next: [[Flexure Formula]]

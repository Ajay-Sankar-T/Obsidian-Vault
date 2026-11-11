Related: [[Double Integration and Macaulay's Method]] · [[Flexure Formula]]

## The $M/EI$ Diagram

Rewrite the beam equation as $\dfrac{d^2v}{dx^2}=\dfrac{M(x)}{EI}$ — the slope of the deflection curve changes at a rate given by the $M/EI$ diagram, exactly analogous to how the slope of the shear diagram is given by the load diagram (see [[Relations Between Load, Shear, and Moment]]). This "beam analogy" (moment diagram plays the role of a *load* diagram for the slope/deflection) is the basis of the two moment-area theorems.

## First Moment-Area Theorem

The change in slope between two points $A,B$ on the elastic curve equals the **area under the $M/EI$ diagram** between $A$ and $B$:
$$\theta_B-\theta_A = \int_A^B \frac{M(x)}{EI}\,dx = \text{area}_{A\to B}\!\left(\frac{M}{EI}\right)$$

## Second Moment-Area Theorem

The vertical deviation (tangential deviation) of point $B$ from the tangent line drawn at point $A$ equals the **first moment of the area** under the $M/EI$ diagram between $A$ and $B$, taken about $B$:
$$t_{B/A} = \int_A^B \frac{M(x)}{EI}\,(x_B-x)\,dx = \left(\text{area}_{A\to B}\!\left(\frac{M}{EI}\right)\right)\times \bar{x}_{\text{(centroid to }B\text{)}}$$

## Practical Use

The moment-area method is typically **faster than double integration** for finding deflection/slope at a **specific point** (rather than the full equation $v(x)$), especially when the $M/EI$ diagram is made of simple shapes (rectangles, triangles, parabolic segments) whose areas and centroids are standard results. It's particularly efficient for:
- Cantilevers (tangent at the fixed end has known zero slope, so $t_{B/A}$ directly gives the tip deflection).
- Finding deflection at specific points in a statically determinate beam without deriving the full elastic curve equation.

For statically **indeterminate** beams, moment-area (or double integration) provides the extra compatibility equations needed beyond equilibrium alone — conceptually the same idea as [[Statically Indeterminate Axial Members]], but now the compatibility condition is on slope/deflection rather than axial stretch.

## Check yourself

> [!question]- Q1. State the two moment-area theorems.
> First: the change in slope between two points equals the area of the $M/EI$ diagram between them. Second: the tangential deviation of one point from the tangent at another equals the first moment of that area about the first point.

> [!question]- Q2. Use the second theorem to find the tip deflection of a cantilever with end load $P$.
> Area $=\tfrac12\cdot L\cdot PL/EI=PL^2/2EI$, centroid $2L/3$ from the tip: $\delta=PL^3/3EI$.

---
Next: [[Euler Buckling of Columns]]

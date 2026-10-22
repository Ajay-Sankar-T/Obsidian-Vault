# AM2200 Tutorial 5 — Q5: Self-Weight Deformation of a Pyramid

Q5 asks for the displacement of the lower tip of a square pyramid due to its own weight when suspended vertically. Height $L$, top square $b_0\times b_0$, specific weight $\gamma$, Young's modulus $E$.

## 1. Theory
For members under self-weight:
$$ \boxed{\delta=\int_0^L\frac{N(x)}{E A(x)}\,dx} $$
where $N(x) = \text{weight of material below the section}$.

## 2. Geometry and Area
Taking $x$ measured downward from the top:
- Side length: $b(x)=b_0\frac{L-x}{L}$
- Area: $A(x) = \frac{b_0^2(L-x)^2}{L^2}$

## 3. Axial Force $N(x)$
The portion below $x$ is a smaller pyramid with height $(L-x)$.
Volume: $V(x) = \frac{b_0^2(L-x)^3}{3L^2}$
Weight: $\boxed{ N(x)= \frac{\gamma b_0^2(L-x)^3}{3L^2} }$

## 4. Solution
$$ \delta = \int_0^L \frac{\frac{\gamma b_0^2(L-x)^3}{3L^2}}{E \frac{b_0^2(L-x)^2}{L^2}} dx = \frac{\gamma}{3E} \int_0^L(L-x)\,dx $$
$$ \delta = \frac{\gamma}{3E} \left[ Lx - \frac{x^2}{2} \right]_0^L = \frac{\gamma}{3E} \frac{L^2}{2} = \boxed{\frac{\gamma L^2}{6E}} $$

**Physical Insight**: The base size $b_0$ cancels out because both weight and area scale with $b_0^2$.

---
**Backlinks**:
- [[Strength of Materials - MOC]]
- [[Strength of Materials - MOC#02 Axial Loading|02 Axial Loading]]
- [[Q7 - Massive Bar with Thermal Expansion]]

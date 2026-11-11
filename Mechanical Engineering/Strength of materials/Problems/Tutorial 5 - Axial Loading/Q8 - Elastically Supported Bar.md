# AM2200 Tutorial 5 — Q8: Elastically Supported Bar

A uniform axial bar of length $a$, rigidity $EA$, is supported by two axial springs $c_1$ and $c_2$. A constant distributed load $n$ acts along the bar.
$c_1 = 2c_2 = \frac{EA}{2a}$.

## 1. Theory
- **Differential equilibrium**: $\frac{dN}{dx} + n = 0 \Rightarrow N(x) = C - nx$.
- **Constitutive relation**: $N = EA \frac{du}{dx}$.
- **Boundary conditions**:
  - Left: $N(0) = c_1 u(0)$
  - Right: $N(a) = -c_2 u(a)$

## 2. Solution
### Displacement $u(x)$
Integrating $u'(x) = \frac{C-nx}{EA}$:
$$ u(x) = u(0) + \frac{Cx}{EA} - \frac{nx^2}{2EA} $$
Using $u(0) = C/c_1$:
$$ u(x) = \frac{C}{c_1} + \frac{Cx}{EA} - \frac{nx^2}{2EA} $$

### Solving for $C$
Using the right boundary condition $N(a) = -c_2 u(a)$:
$$ C - na = -c_2 \left( \frac{C}{c_1} + \frac{Ca}{EA} - \frac{na^2}{2EA} \right) $$
Substituting $c_1 = \frac{EA}{2a}$ and $c_2 = \frac{EA}{4a}$ simplifies to:
$$ C = \frac{9na}{14} $$

### Normal Force Distribution
$$ \boxed{ N(x) = n\left(\frac{9a}{14} - x\right) } $$
- $N(0) = \frac{9na}{14}$ (Tension)
- $N(a) = -\frac{5na}{14}$ (Compression)
- Zero-force point: $x = \frac{9a}{14}$

---
**Backlinks**:
- [[Strength of Materials - MOC]]
- [[Strength of Materials - MOC#02 Axial Loading|02 Axial Loading]]

## See also
- [[Relations Between Load, Shear, and Moment]] — $dN/dx=-n$ is the axial twin of $dV/dx=-w$.
- [[Double Integration and Macaulay's Method]] — $EA\,u''=-n$ is the axial twin of $EI\,v''''=-w$.
- [[Statically Indeterminate Axial Members]] — the spring supports add compatibility conditions.

---
tags: [strength-of-materials, stress-strain, self-weight]
up: "[[Tutorial 4 - Stress-Strain Relationship]]"
---

# Elongation Under Self-Weight and End Load

← up: [[Tutorial 4 - Stress-Strain Relationship|Tutorial 4]] · builds on: [[Axial Deformation|Axial Deformation]]

## The pattern (Q7)

A uniform bar of length $l$, cross-section $A$, modulus $E$, hangs vertically under its own weight and also carries an end load $P$. Total elongation:

$$\boxed{\delta=\int_0^l\frac{N(x)}{EA}\,dx}$$

— the general varying-$N(x)$ form already established in [[Axial Deformation|Axial Deformation]].

```text
   P (end load, at bottom, pulling down)
   │
   ▼
  ═══   x = l  (free end)
   │
   │   bar hangs from top,
   │   x measured from bottom
   │
  ═══   x = 0  (fixed support, top)
```

## End-load contribution

The end load creates constant internal force throughout: $N(x)=P\Rightarrow\boxed{\delta_P=\dfrac{Pl}{EA}}$ — ordinary uniform-bar elongation.

## Self-weight contribution

With $\gamma$ = weight density (force per volume), the internal force at a section a distance $x$ from the free end must support the weight of everything below it: $N(x)=\gamma A(l-x)$ (maximum at the fixed support, zero at the free end — a bar doesn't need to support its own weight below its very tip).

$$\delta_W=\int_0^l\frac{\gamma A(l-x)}{EA}\,dx=\frac{\gamma}{E}\int_0^l(l-x)\,dx=\frac{\gamma}{E}\left[lx-\frac{x^2}2\right]_0^l=\frac{\gamma}{E}\cdot\frac{l^2}{2}$$

$$\boxed{\delta_W=\frac{\gamma l^2}{2E}}$$

## Combined result

$$\boxed{\delta_{\rm total}=\frac{Pl}{EA}+\frac{\gamma l^2}{2E}}$$

**Alternative using total weight** $W=\gamma Al$: $\delta_W=\dfrac{Wl}{2EA}$, so $\boxed{\delta_{\rm total}=\dfrac{Pl}{EA}+\dfrac{Wl}{2EA}}$ — note the factor of $\tfrac12$: a bar under self-weight elongates as much as it would under a *concentrated end load equal to half its total weight*, because the internal force decreases linearly from full weight at the support to zero at the tip, and the average of a linear ramp is half the maximum. (If $\gamma$ given is mass density $\rho$ rather than weight density, substitute $\gamma\to\rho g$.)

## Cross-domain: this is the "distributed vs concentrated load" idea from beam theory

The $\tfrac12$ factor here is the axial-loading twin of the pattern used throughout [[Double Integration and Macaulay's Method|Double Integration and Macaulay's Method]] and [[Relations Between Load, Shear, and Moment|Relations Between Load, Shear, and Moment]]: integrating a linearly-varying internal force/moment over the member's length always produces a coefficient smaller than the naive "peak value × length" estimate, because the load tapers rather than staying at its maximum throughout — the same reasoning gives the $wL^2/8$ (not $wL^2/2$) maximum moment for a uniformly loaded simply-supported beam.

## Related
- [[Axial Deformation|Axial Deformation]]
- [[Relations Between Load, Shear, and Moment|Relations Between Load, Shear, and Moment]]

## See also
- [[Q5 - Self-Weight Pyramid]] — the tapered case.

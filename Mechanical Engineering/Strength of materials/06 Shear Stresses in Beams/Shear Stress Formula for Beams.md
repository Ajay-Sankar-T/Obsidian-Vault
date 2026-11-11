Related: [[Flexure Formula]] · [[Relations Between Load, Shear, and Moment]] · [[Plane Stress Transformation]]

## Why Bending Produces Shear Stress Too

Since $M(x)$ varies along the beam (whenever $V\ne0$, by $dM/dx=V$), the bending stress $\sigma=My/I$ on one face of a small beam slice differs from that on the opposite face. Horizontal equilibrium of a sub-element cut at height $y$ then requires a horizontal (and by pairing, vertical) shear stress on the longitudinal plane at that height.

![[SM-C-beam-shear.png]]

**Figure:** the shear stress in a rectangular section is a parabola with peak $1.5V/A$ at the neutral axis, and zero at the top and bottom faces. In an I-section the web carries nearly all of it.

## The Shear Stress (Jourawski) Formula

$$\tau(y) = \frac{VQ(y)}{I\,t(y)}$$
where:
- $V$ = shear force at the section (from [[Shear Force and Bending Moment Diagrams]])
- $I$ = moment of inertia of the **whole** cross-section about the neutral axis
- $t(y)$ = width of the section at the height $y$ where $\tau$ is being found
- $Q(y) = \int_{A'} y'\,dA'$ = first moment of the area $A'$ **beyond** $y$ (between $y$ and the extreme fiber) about the neutral axis

## Distribution Through the Depth

- $\tau=0$ at the extreme fibers ($Q=0$ there, since the "area beyond" vanishes).
- $\tau$ is **maximum at the neutral axis** for most common sections (where $Q$ is maximum), *not* where bending stress is maximum — bending and shear stress peak at opposite locations through the depth.
- For a **rectangular** section $b\times h$: $\tau_{max}=\dfrac{3V}{2A}$ (1.5× the average shear stress $V/A$), occurring at the neutral axis, parabolic distribution.
- For a **circular** section: $\tau_{max}=\dfrac{4V}{3A}$.

## Shear Flow (Thin-Walled / Built-Up Sections)

For thin-walled or built-up sections (I-beams, box sections, welded/bolted plates), it's more natural to work with **shear flow** $q=\tau t = VQ/I$ (force per unit length along the wall), which determines:
- The spacing/strength required for fasteners (rivets, bolts, welds) connecting flange to web.
- In I-beams, the **web** carries the overwhelming majority of the vertical shear (since $Q$ and $1/t$ are both large there), which is why beam design often approximates $\tau_{avg}\approx V/A_{web}$.

## Connection to Plane Stress

At any point in the beam (except the extreme fibers and neutral axis), both bending stress $\sigma$ and shear stress $\tau$ act simultaneously — a full plane-stress state requiring [[Plane Stress Transformation]] to find the principal stresses that actually govern failure (this is why the top/bottom of an I-beam web, or the neutral axis, aren't always the critical points for a combined-stress failure check).

## Check yourself

> [!question]- Q1. A 100 mm × 200 mm rectangular beam carries $V=30$ kN. Find the maximum shear stress.
> $\tau_{max}=1.5V/A=1.5\times30\,000/0.02=2.25$ MPa, at the neutral axis.

> [!question]- Q2. Why is the shear stress zero at the top and bottom faces?
> $Q$, the first moment of the area beyond that level, is zero there, and the faces are stress-free.

> [!question]- Q3. In an I-beam, which part carries the shear?
> The web: it is thin and runs between the flanges, so almost all of $V$ flows through it. The flanges carry little.

---
Next: [[Plane Stress Transformation]]

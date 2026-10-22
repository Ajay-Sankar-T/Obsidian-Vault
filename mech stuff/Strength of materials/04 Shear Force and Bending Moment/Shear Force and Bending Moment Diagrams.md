Related: [[Concept of Stress]] · [[Relations Between Load, Shear, and Moment]] · [[Flexure Formula]]

## Internal Resultants at a Beam Section

Cutting a beam at any section $x$ and applying equilibrium to one side (the "method of sections") reveals two internal resultants (in addition to axial force, usually zero for pure bending problems):
- **Shear force $V(x)$:** the resultant of all transverse forces on the free-body to one side.
- **Bending moment $M(x)$:** the resultant moment of all forces on the free-body to one side, taken about the cut section.

## Sign Convention (standard beam convention)

- $V$ positive: the right-hand-side of the cut face tends to shear **downward** relative to the left (equivalently: net upward force on the left free body).
- $M$ positive: **sagging** (beam concave up, top fiber in compression, bottom fiber in tension).

## Constructing the Diagrams

1. Find support reactions from global equilibrium.
2. Cut the beam at an arbitrary section within each load segment; find $V(x)$ and $M(x)$ by summing forces/moments on the free body to one side.
3. Plot $V(x)$ and $M(x)$ along the beam length.

**Key values to identify:**
- $V=0$ locations — candidates for **maximum $|M|$** (since $dM/dx=V$, see [[Relations Between Load, Shear, and Moment]]).
- Jumps in $V$ occur at concentrated point loads (jump magnitude = load).
- Jumps in $M$ occur at applied concentrated moments (jump magnitude = moment).
- $M=0$ at simple/pin supports and free ends (unless a moment is applied there).

## Why This Matters

$M(x)$ directly drives bending stress via the [[Flexure Formula]] ($\sigma=My/I$), and $V(x)$ drives transverse shear stress via the [[Shear Stress Formula for Beams]]. The SFD/BMD is therefore the essential first step before any stress or deflection calculation — everything downstream (bending stress, shear stress, deflection via [[Double Integration and Macaulay's Method]]) is built from $V(x)$ and $M(x)$.

---
Next: [[Relations Between Load, Shear, and Moment]]

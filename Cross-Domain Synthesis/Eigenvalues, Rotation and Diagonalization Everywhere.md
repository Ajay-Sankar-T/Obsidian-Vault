---
tags: [synthesis, cross-domain, eigenvalues, rotation, mohrs-circle, phasors]
up: "[[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC]]"
---

# Eigenvalues, Rotation and Diagonalization Everywhere

← up: [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]

## Three notes, one linear-algebra fact

- [[Strength of materials/07 Transformation of Stress and Strain/Plane Stress Transformation|Plane Stress Transformation]]: the stress matrix $[\sigma]=\begin{psmallmatrix}\sigma_x&\tau_{xy}\\\tau_{xy}&\sigma_y\end{psmallmatrix}$ is diagonalized by a rotation $\theta_p$, giving principal stresses $\sigma_1,\sigma_2$ as **eigenvalues**.
- [[Phasors and Complex Algebra|Phasors and Complex Algebra]]: multiplying by $j$ is a $90°$ **rotation** in the complex plane ($j=e^{j90°}$), and every phasor is literally a 2D vector $(x,y)=(A\cos\theta,A\sin\theta)$.
- [[Strength of materials/07 Transformation of Stress and Strain/Mohr's Circle for Stress|Mohr's Circle for Stress]]: the transformation equations, parameterized by angle, trace out a **circle** in $(\sigma,\tau)$-space — because a 2×2 symmetric matrix's transformation under rotation is, geometrically, exactly a circle in its own eigenbasis-centered coordinates.

These are not three separate techniques — they are the *same fact about symmetric 2×2 real matrices under orthogonal similarity transformation* ($[\sigma']=[Q]^T[\sigma][Q]$, noted explicitly in Plane Stress Transformation's "eigenvalue/matrix interpretation" section), applied once to a stress tensor and once (informally) to a rotating vector in the electrical case.

## The genuinely new observation

A **phasor is not a tensor** — it has no "principal value" problem, because a vector under rotation doesn't have eigenvalues the way a matrix does (a vector just rotates; it doesn't diagonalize into anything). So why does [[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]'s $\theta_I=\theta_V-\theta_Z$ *feel* so structurally similar to [[Strength of materials/07 Transformation of Stress and Strain/Plane Stress Transformation|Plane Stress Transformation]]'s $\tan2\theta_p=\dfrac{2\tau_{xy}}{\sigma_x-\sigma_y}$?

Because impedance $Z=R+jX$ **is** a 1×1 "complex-diagonalized" stand-in for what, in a fully general anisotropic material or a multi-port network, would be a matrix. The factor-of-2 in $\tan2\theta_p$ (angle *doubles* for stress, boxed explicitly in [[Strength of materials/07 Transformation of Stress and Strain/Mohr's Circle for Stress|Mohr's Circle for Stress]]'s "critical angle doubling rule") comes precisely from the fact that a *symmetric matrix's* eigenvector rotation appears at twice the physical angle in the transformation formula (a consequence of $\cos2\theta,\sin2\theta$ terms arising from squaring rotation matrix entries) — whereas a **phasor's own rotation angle appears at $1\times$**, not $2\times$, because a phasor is a first-order (vector) object, not a second-order (tensor) object. This is *the* reason [[Strength of materials/07 Transformation of Stress and Strain/Stress-Strain Transformation Analogy|Stress-Strain Transformation Analogy]] has to warn about the $\gamma=2\varepsilon_{xy}$ engineering-vs-tensor-shear factor of 2 — it's the exact same order-of-tensor bookkeeping issue reappearing.

**Rule of thumb this gives you across all three domains:** whenever a physical transformation law involves $\cos2\theta/\sin2\theta$ (stress, strain, Mohr's circle, moment of inertia principal axes — none of which currently has its own note but would obey the identical formula), you are diagonalizing a rank-2 tensor. Whenever it involves $\cos\theta/\sin\theta$ at $1\times$ (phasor rotation, impedance angle, coordinate rotation of a force vector), you are rotating a rank-1 vector. Confusing the two — using $\theta$ where you need $2\theta$ — is the single most common transformation-formula error in both subjects.

## Impedance angle as a degenerate Mohr's circle

Push the analogy one step further: [[AC Power and Power Factor|AC Power and Power Factor]]'s power triangle ($P$ horizontal, $Q$ vertical, $S$ hypotenuse, $\tan\phi=Q/P$) is geometrically identical to Mohr's circle collapsed to a single point-vector rather than a circle of transformation states — $P$ plays $\sigma_{\rm avg}$'s role (a "real, dissipative" axis) and $Q$ plays $\tau_{\rm max}$'s role (a "reactive, non-dissipative" axis). This is why both fields independently converge on a **triangle-with-a-hypotenuse-magnitude-and-an-angle** as the natural summary picture: it's the universal way to display "one real part + one imaginary/orthogonal part" as a single diagram, whether the two parts are $(\sigma,\tau)$, $(P,Q)$, or $(R,X)$.

## Related
- [[Strength of materials/07 Transformation of Stress and Strain/Plane Stress Transformation|Plane Stress Transformation]]
- [[Strength of materials/07 Transformation of Stress and Strain/Mohr's Circle for Stress|Mohr's Circle for Stress]]
- [[Phasors and Complex Algebra|Phasors and Complex Algebra]]
- [[AC Power and Power Factor|AC Power and Power Factor]]

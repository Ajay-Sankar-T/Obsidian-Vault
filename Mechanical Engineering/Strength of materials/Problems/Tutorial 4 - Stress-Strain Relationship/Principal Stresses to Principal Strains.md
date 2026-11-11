---
tags: [strength-of-materials, stress-strain, principal-stress]
up: "[[Tutorial 4 - Stress-Strain Relationship]]"
---

# Principal Stresses to Principal Strains

← up: [[Tutorial 4 - Stress-Strain Relationship|Tutorial 4]] · builds on: [[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]], [[Plane Stress Transformation|Plane Stress Transformation]]

## The pattern (Q5)

Given the principal stresses $\sigma_1,\sigma_2,\sigma_3$ at a point (found via [[Plane Stress Transformation|Plane Stress Transformation]]/Mohr's circle, or given directly), find the corresponding principal **strains**.

At a principal-stress orientation, the shear stresses vanish by definition — and because Hooke's law has **no coupling between normal stress and shear strain** for an isotropic material (see [[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]]'s uncoupled shear equations $\gamma_{ij}=\tau_{ij}/G$), the strain in that *same* orientation also has zero shear component. **The principal directions of stress and strain coincide for an isotropic material** — this is why it's valid to plug principal stresses directly into the normal-strain Hooke's law equations without any transformation step:

$$\boxed{\varepsilon_1=\frac1E[\sigma_1-\nu(\sigma_2+\sigma_3)]},\quad\boxed{\varepsilon_2=\frac1E[\sigma_2-\nu(\sigma_1+\sigma_3)]},\quad\boxed{\varepsilon_3=\frac1E[\sigma_3-\nu(\sigma_1+\sigma_2)]}$$

$$\boxed{\begin{bmatrix}\varepsilon_1\\\varepsilon_2\\\varepsilon_3\end{bmatrix}=\frac1E\begin{bmatrix}1&-\nu&-\nu\\-\nu&1&-\nu\\-\nu&-\nu&1\end{bmatrix}\begin{bmatrix}\sigma_1\\\sigma_2\\\sigma_3\end{bmatrix}}$$

## The important subtlety

A **compressive** principal stress does not necessarily produce a compressive principal strain in that direction — the Poisson contributions from the *other two* principal stresses can outweigh it and flip the sign. E.g. if $\sigma_1<0$ but $\sigma_2,\sigma_3>0$ and large, $\varepsilon_1=\frac1E[\sigma_1-\nu(\sigma_2+\sigma_3)]$ can still come out negative *more* than expected, or in the reverse scenario a small compressive $\sigma_1$ combined with strongly tensile $\sigma_2,\sigma_3$ can even push $\varepsilon_1$ positive. Always compute — never assume the sign of $\varepsilon_i$ matches the sign of $\sigma_i$ in a multiaxial state.

## Why this matters: it's the same eigenbasis, twice

This coincidence of principal directions is the isotropic-material special case of a more general linear-algebra fact explored in [[Eigenvalues, Rotation and Diagonalization Everywhere|Eigenvalues, Rotation and Diagonalization Everywhere]]: the stress tensor $[\sigma]$ and strain tensor $[\varepsilon]$ are related by the *isotropic* compliance tensor (the matrix above), which for an isotropic material is itself diagonal in **every** orthonormal basis (it commutes with any rotation). Two matrices that commute are always simultaneously diagonalizable — which is precisely why $[\sigma]$ and $[\varepsilon]$ share the same eigenvectors (principal directions) here. This would **not** hold for an anisotropic (e.g. composite/fibre-reinforced) material, where the compliance tensor is *not* isotropic and the principal strain directions can rotate away from the principal stress directions.

## Related
- [[Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]]
- [[Plane Stress Transformation|Plane Stress Transformation]]
- [[Eigenvalues, Rotation and Diagonalization Everywhere|Cross-Domain: Eigenvalues, Rotation and Diagonalization Everywhere]]

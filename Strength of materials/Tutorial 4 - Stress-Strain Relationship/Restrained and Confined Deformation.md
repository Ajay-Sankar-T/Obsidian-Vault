---
tags: [strength-of-materials, stress-strain, constrained-deformation]
up: "[[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Tutorial 4 - Stress-Strain Relationship]]"
---

# Restrained and Confined Deformation

← up: [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Tutorial 4 - Stress-Strain Relationship|Tutorial 4]] · builds on: [[Strength of materials/01 Stress and Strain/Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]]

## The pattern (Q2): a block under pressure, restrained to different degrees

A block is loaded by pressure $\sigma_z=-p_0$ on its top face, with the $x$ and $y$ faces either free or rigidly restrained by the walls of a press. The golden rule — restrained $\Rightarrow\varepsilon=0$, free $\Rightarrow\sigma=0$ — turns each restraint case into a small linear-algebra problem on the Generalized Hooke's Law matrix.

```text
        σz = -p0  (applied)
            ↓ ↓ ↓
      ┌───────────────┐
  x ← │               │ → x   (restrained or free?)
      │     BLOCK      │
  y ← │               │ → y   (restrained or free?)
      └───────────────┘
```

### Case 1 — both $x$ and $y$ restrained

$\varepsilon_x=\varepsilon_y=0$. By symmetry (identical restraint in both directions), $\sigma_x=\sigma_y$. Substituting into Hooke's law $\varepsilon_x=\frac1E[\sigma_x-\nu(\sigma_y+\sigma_z)]=0$ with $\sigma_y=\sigma_x,\ \sigma_z=-p_0$:

$$\sigma_x-\nu(\sigma_x-p_0)=0\quad\Longrightarrow\quad\boxed{\sigma_x=\sigma_y=-\frac{\nu}{1-\nu}p_0},\qquad\boxed{\sigma_z=-p_0}$$

### Case 2 — $y$ restrained, $x$ free

Free $x$: $\boxed{\sigma_x=0}$. Restrained $y$: $\varepsilon_y=0=\frac1E[\sigma_y-\nu(\sigma_x+\sigma_z)]=\frac1E[\sigma_y-\nu(-p_0)]$, so

$$\boxed{\sigma_y=-\nu p_0},\qquad\boxed{\sigma_z=-p_0}$$

### Case 3 — both $x,y$ free

$\boxed{\sigma_x=\sigma_y=0}$, $\sigma_z=-p_0$. Strains follow directly from Hooke's law with no restraint stresses to solve for:

$$\boxed{\varepsilon_x=\varepsilon_y=\frac{\nu p_0}{E}},\qquad\boxed{\varepsilon_z=-\frac{p_0}{E}}$$

Note the block **expands** laterally ($\varepsilon_x,\varepsilon_y>0$) even though it's being compressed — pure Poisson effect, no lateral stress required.

## The pattern (Q3): fully confined rubber, effective modulus

A rubber block confined on $x$ and $y$ by rigid walls, loaded axially by $\sigma_z=-p$. This is exactly Case 1 above, so $\sigma_x=\sigma_y=-\dfrac{\nu}{1-\nu}p$. The **axial strain** is then:

$$\varepsilon_z=\frac1E\left[\sigma_z-\nu(\sigma_x+\sigma_y)\right]=\frac1E\left[-p-2\nu\left(-\frac{\nu}{1-\nu}p\right)\right]$$

$$\boxed{\varepsilon_z=-\frac pE\cdot\frac{(1+\nu)(1-2\nu)}{1-\nu}}$$

Define an **effective (constrained) modulus** $E_{\rm eff}=p/|\varepsilon_z|$:

$$\boxed{E_{\rm eff}=\frac{E(1-\nu)}{(1+\nu)(1-2\nu)}}$$

### The physically striking result

For rubber, $\nu\approx0.5$ (nearly incompressible), so $1-2\nu\to0$ and $\boxed{E_{\rm eff}\to\infty}$ — a laterally confined near-incompressible material becomes enormously stiffer axially than its own (small) Young's modulus would suggest, because it can no longer relieve axial compression by bulging sideways. This is the mechanical principle behind rubber bushings/mounts confined in a rigid metal sleeve, and behind why $E_{\rm eff}$ is the quantity relevant for such a mount's actual axial stiffness, not the bulk $E$ from a tensile test.

## Cross-domain: this is the same $\nu\to0.5$ limit as the bulk modulus

$E_{\rm eff}\to\infty$ as $\nu\to0.5$ is the same phenomenon already noted in [[Strength of materials/01 Stress and Strain/Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]] for the bulk modulus $K=E/[3(1-2\nu)]\to\infty$ under hydrostatic loading. Confinement in one axial direction with two lateral restraints is a **partial** version of full hydrostatic confinement — the same $(1-2\nu)$ denominator appears because both cases are limited by the material's resistance to *volume change*, not shape change, and volume change is exactly what vanishes as $\nu\to0.5$.

## Related
- [[Strength of materials/01 Stress and Strain/Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law and Poisson's Ratio]]
- [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Two Dissimilar Plates in a Rigid Opening|Two Dissimilar Plates in a Rigid Opening]]

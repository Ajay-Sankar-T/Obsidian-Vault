---
tags: [concept, materials]
course: "Materials and Design (ME2200)"
aliases: [Unit cell, FCC, BCC, HCP, Atomic packing factor, Coordination number, Miller indices, Crystal structure]
---

# Crystal Structures and Packing

> [!abstract] In one breath
> A metal is a regular array of atoms, and a **unit cell** is the smallest box that repeats to build it. Three cells cover almost every engineering metal: **FCC** (Al, Cu, Ni, austenite), **BCC** (α-Fe, Cr, W) and **HCP** (Mg, Zn, Ti). They differ in how full the cell is and in which planes the atoms are packed densest, which later decides how easily the metal deforms.

Part of [[Materials and Design - MOC]]. Next: [[Dislocations, Slip and Strengthening]].

## 1. The three cells

| Cell | Atoms per cell | Coordination number | $a$ in terms of atomic radius $R$ | Packing factor | Examples |
| --- | --- | --- | --- | --- | --- |
| Simple cubic | 1 | 6 | $2R$ | 0.524 | (polonium only) |
| **BCC** | 2 | 8 | $4R/\sqrt3$ | **0.680** | α-Fe, Cr, W, Mo |
| **FCC** | 4 | 12 | $2\sqrt2R$ | **0.740** | γ-Fe, Al, Cu, Ni, Au |
| **HCP** | 6 (per hexagonal cell) | 12 | $a=2R$, $c/a=1.633$ ideal | **0.740** | Mg, Zn, Ti, Co |

Atoms shared between cells are counted by fractions: a corner atom is $1/8$ inside, a face-centre atom $1/2$. The **atomic packing factor** is the volume of the atoms divided by the volume of the cell, e.g. FCC: $4\cdot\frac43\pi R^3/(2\sqrt2R)^3=\pi/(3\sqrt2)=0.740$. FCC and HCP are both close-packed and differ only in the stacking order of the close-packed layers (ABCABC against ABAB).

![[MAT-1-crystals.png]]

## 2. Density from the cell

$$
\rho=\frac{n\,A}{V_cN_A}
$$

with $n$ atoms per cell, $A$ atomic mass and $V_c=a^3$ for a cubic cell.

| Metal | Cell | $a$ (nm) | $A$ (g/mol) | $\rho$ computed | measured |
| --- | --- | --- | --- | --- | --- |
| Cu | FCC | 0.3615 | 63.55 | 8.94 g/cm³ | 8.96 |
| α-Fe | BCC | 0.2866 | 55.85 | 7.88 g/cm³ | 7.87 |
| Al | FCC | 0.4050 | 26.98 | 2.70 g/cm³ | 2.70 |

## 3. Directions and planes

**Miller indices.** A plane is described by the reciprocals of its intercepts with the axes, cleared of fractions: $(hkl)$; a direction by the vector components in lowest integers: $[uvw]$. Families: $\{hkl\}$ and $\langle uvw\rangle$.

**Densities.** Linear density along $[110]$ in FCC $=2/(\sqrt2a)=1/(2R)$: the atoms touch, so this is a close-packed direction. Planar density: FCC $(111)$ $=4/(\sqrt3a^2)=2.31/a^2$ (close-packed plane); FCC $(100)$ $=2/a^2$; BCC $(110)$ $=\sqrt2/a^2=1.41/a^2$ (the densest BCC plane, but less dense than FCC's).

| Structure | Close-packed plane | Close-packed direction |
| --- | --- | --- |
| FCC | $\{111\}$ | $\langle110\rangle$ |
| BCC | $\{110\}$ | $\langle111\rangle$ |
| HCP | basal $(0001)$ | $\langle11\bar20\rangle$ |

These planes and directions are the **slip systems** of [[Dislocations, Slip and Strengthening]].

> [!warning] Traps
> - Counting 8 atoms in the cube because 8 corners are drawn: each corner contributes 1/8.
> - Using the body diagonal for FCC: its atoms touch along the **face** diagonal ($a=2\sqrt2R$); BCC atoms touch along the body diagonal.
> - Reading Miller indices as the intercepts rather than their reciprocals.
> - Assuming HCP and FCC differ in density: both are 0.74; they differ in slip systems.

> [!question]- Predict first: iron changes from BCC to FCC on heating through 912 °C. Does it expand or contract?
> **Contract** at the transformation (FCC is denser: 0.74 against 0.68 packing), even though thermal expansion is increasing: the dilatometer curve of steel steps *down* at the A₃ temperature. Quenching steel, which forms martensite from FCC, expands for the opposite reason.

> [!question]- Why does FCC deform more easily than BCC?
> FCC has 12 slip systems all on close-packed planes ($4\times3$), with no preferred direction. BCC has no truly close-packed plane, so slip needs higher stress and depends on temperature, one reason steels become brittle in the cold.

## 4. Connections

- [[Fluids and Solids - Pressure, Stress and Constitutive Laws]] — the elastic constants of the solid are the stiffness of these bond arrays.
- [[Eigenvalues, Rotation and Diagonalization Everywhere]] — the symmetry operations of a crystal are rotations and reflections of the lattice; anisotropic stiffness is a tensor with the cell's symmetry.
- [[Phase Diagrams - Lever Rule and the Iron-Carbide Diagram]] — which cell appears at a given temperature and composition.

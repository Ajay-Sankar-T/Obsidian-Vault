Related: [[Axial Deformation]] · [[Thermal Stresses]]

## When Equilibrium Alone Isn't Enough

A structure is **statically indeterminate** when the number of unknown reactions/internal forces exceeds the number of independent equilibrium equations available. The extra equation(s) needed come from **compatibility** — a geometric condition on how the parts must deform together — combined with the force-deformation relation $\delta=NL/(AE)$ from [[Axial Deformation]].

## General Solution Procedure

1. **Equilibrium:** write $\sum F=0$ relating the unknown internal forces (this alone is insufficient — that's what makes it indeterminate).
2. **Compatibility:** write a geometric constraint on the displacements/deformations (e.g. "total elongation of the two segments equals zero" for a bar fixed at both ends).
3. **Force-deformation:** substitute $\delta_i=N_iL_i/(A_iE_i)$ into the compatibility equation.
4. Solve the resulting simultaneous equations for the unknown forces.

## Example: Bar Fixed at Both Ends, Point Load at an Interior Point

A bar fixed at $x=0$ and $x=L$ carries a point load $P$ at $x=a$ (with $b=L-a$). Let $R_1,R_2$ be the wall reactions.

**Equilibrium:** $R_1+R_2=P$.

**Compatibility:** the two segments must have net elongation summing to zero (both ends fixed):
$$\frac{-R_1\,a}{AE}+\frac{R_2\,b}{AE}=0 \implies R_2=\frac{a}{b}R_1$$
(sign convention: treat $R_1$ as pulling segment 1 in tension for the compatibility bookkeeping — details depend on the free-body chosen).

Combining with equilibrium: $R_1=\dfrac{Pb}{L}$, $R_2=\dfrac{Pa}{L}$.

## Composite (Parallel) Members

Two materials sharing the same displacement (e.g. a concrete column reinforced with steel bars, or a bolt-and-sleeve assembly) under total load $P$:
$$\delta_1=\delta_2 \implies \frac{N_1L}{A_1E_1}=\frac{N_2L}{A_2E_2}, \qquad N_1+N_2=P$$
Solving gives each material's share of the load proportional to its stiffness $A_iE_i$ — the stiffer material carries proportionally more load. This same "share load proportional to stiffness" idea reappears for [[Thermal Stresses]] and in torsion of composite shafts.

---
Next: [[Thermal Stresses]]

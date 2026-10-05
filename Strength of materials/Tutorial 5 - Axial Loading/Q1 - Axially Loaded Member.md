# AM2200 Tutorial 5 — Q1: Axially Loaded Member

Question 1 asks us to analyze a stepped bar $ABCD$, fixed between two rigid supports, with a point load $P$ applied at $B$. The area is $A_1$ from $A$ to $C$, and $2A_1$ from $C$ to $D$. The lengths are $AB=L/4$, $BC=L/4$, and $CD=L/2$.

## 1. Theory
### A. Axial deformation
For a prismatic member subjected to a constant axial force:
$$ \boxed{\delta=\frac{NL}{AE}} $$
where $N$ = internal axial force, $L$ = length, $A$ = cross-sectional area, $E$ = Young's modulus.

**Sign convention**: Tension ($N>0$, elongation $+$), Compression ($N<0$, shortening $-$).
For several segments:
$$ \boxed{\delta_{\text{total}}=\sum_i\frac{N_iL_i}{A_iE}} $$

### B. Rigid-support compatibility
Since both $A$ and $D$ are rigid supports:
$$ \boxed{\delta_D-\delta_A=0} \Rightarrow \boxed{\sum\delta_i=0} $$
This compatibility condition is essential because the reactions are statically indeterminate.

## 2. Solution
### Q1(a) — Reactions $R_A$ and $R_D$
Let positive force be to the right. $\sum F_x=0 \Rightarrow R_A+P+R_D=0 \tag{1}$.

**Internal axial forces**:
- Segment AB: $N_{AB}=-R_A$
- Segments BC and CD: $N_{BC}=N_{CD}=-(R_A+P)$

**Apply compatibility**:
$$ \frac{(-R_A)(L/4)}{A_1E} + \frac{[-(R_A+P)](L/4)}{A_1E} + \frac{[-(R_A+P)](L/2)}{(2A_1)E} =0 $$
Simplifying:
$$ R_A+2(R_A+P)=0 \Rightarrow 3R_A+2P=0 \Rightarrow \boxed{R_A=-\frac{2P}{3}} $$
From Eq. (1): $R_D=-P-R_A \Rightarrow \boxed{R_D=-\frac{P}{3}}$.

### Q1(b) — Displacements $\delta_B$ and $\delta_C$
- $N_{AB} = \frac{2P}{3}$ (Tension)
- $N_{BC}=N_{CD} = -\frac{P}{3}$ (Compression)

**Displacement of B**:
$$ \delta_B=\frac{N_{AB}L_{AB}}{A_1E} = \frac{(2P/3)(L/4)}{A_1E} = \boxed{\frac{PL}{6A_1E}} $$

**Displacement of C**:
$$ \delta_C = \delta_{AB}+\delta_{BC} = \frac{PL}{6A_1E} - \frac{(P/3)(L/4)}{A_1E} = \boxed{\frac{PL}{12A_1E}} $$

### Q1(c) — Displacement diagram
The displacement is piecewise linear.
- $\delta_A=0$
- $\delta_B=\frac{PL}{6A_1E}$
- $\delta_C=\frac{PL}{12A_1E}$
- $\delta_D=0$

## Key Exam Idea
Statically indeterminate axial member $\Rightarrow$ Combine:
$$ \boxed{\text{Equilibrium} + \text{Compatibility} + \text{Axial deformation}} $$

---
**Backlinks**:
- [[Strength of Materials - MOC]]
- [[02 Axial Loading]]
- [[Q3 - Four-Wire Support System]]
- [[Q6 - Bolt and Tube Assembly]]

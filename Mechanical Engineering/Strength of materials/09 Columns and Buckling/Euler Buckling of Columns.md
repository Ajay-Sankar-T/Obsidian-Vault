Related: [[Flexure Formula]] · [[Double Integration and Macaulay's Method]] · [[Strain Energy and Castigliano's Theorem]]

## Buckling: A Different Kind of Failure

A slender member under axial **compression** can fail by sudden lateral deflection (**buckling**) at a load far below the material's crushing/yield strength — this is a **stability** failure, not a strength failure. Short/stubby columns fail by material yielding ($\sigma=P/A$ reaches $\sigma_Y$); long/slender columns fail by buckling, governed by geometry and stiffness ($EI$), essentially independent of material strength.

![[SM-C-euler-buckling.png]]

**Figure:** end conditions scale the critical load through $K$ (left). Euler's formula governs only slender columns, with $\lambda=KL/r$ beyond about 89 for this steel (right).

## Euler's Column Formula

Modeling a pin-ended column of length $L$ with a small lateral deflection $v(x)$, the bending moment at any section due to the eccentric internal axial force $P$ is $M=-Pv$, giving the governing equation
$$EI\frac{d^2v}{dx^2} + Pv = 0$$
This is the same type of linear ODE as [[2nd Order Linear ODE with Constant Coefficients]] (in the "Differential Equations" vault) — its solution is $v(x)=A\sin(kx)+B\cos(kx)$ with $k=\sqrt{P/EI}$, and applying the boundary conditions $v(0)=v(L)=0$ forces $\sin(kL)=0$, i.e. $kL=n\pi$. The smallest nontrivial buckling load ($n=1$) is the **critical (Euler) buckling load**:
$$P_{cr} = \frac{\pi^2EI}{L^2}$$
Below $P_{cr}$ the straight configuration is stable; at $P_{cr}$ the column can buckle into a half sine-wave shape at (theoretically) no further load increase.

## Effective Length for Other End Conditions

Different support conditions change the effective buckled shape, captured by an **effective length** $L_e=KL$:

| End conditions | $K$ | $P_{cr}$ |
|---|---|---|
| Pinned-pinned | $1.0$ | $\pi^2EI/L^2$ |
| Fixed-free (cantilever) | $2.0$ | $\pi^2EI/(2L)^2$ |
| Fixed-fixed | $0.5$ | $\pi^2EI/(0.5L)^2$ |
| Fixed-pinned | $\approx0.7$ | $\pi^2EI/(0.7L)^2$ |

General form: $P_{cr}=\dfrac{\pi^2EI}{(KL)^2}$.

## Beyond the table: restraint by springs, joints and sway
The $K$ table covers ideal supports only. For elastic or stepped supports write $EIv''=M_0+V_0x-Pv$, apply the boundary conditions and set the determinant to zero; the smallest root $kL$ gives $P_{cr}=(kL)^2EI/L^2$. Worked in [[Tutorial 9 - Columns|Tutorial 9]]: a column fixed against rotation at both ends but free to sway has $K=1$; torsional springs of stiffness $c_T$ at pinned ends give $\tan u=-(2EI/c_Tl)\,u$ with $u=kl/2$ (13.49 $EI/l^2$ for $c_Tl=EI$, between the pinned $\pi^2$ and the clamped $4\pi^2$); a rigid half plus an elastic half gives $\tan ka=-ka$, $F_{cr}=4.116\,EI/a^2$.

## Critical Stress and Slenderness Ratio

Dividing by area, using $I=Ar^2$ ($r$ = radius of gyration):
$$\sigma_{cr} = \frac{P_{cr}}{A} = \frac{\pi^2E}{(KL/r)^2}$$
$KL/r$ is the **slenderness ratio**. Euler's formula is valid only while $\sigma_{cr}$ stays below the proportional limit (long, slender columns); for short/intermediate columns, empirical formulas (Johnson's parabolic formula, AISC design curves) blend the Euler curve with a material-yield cutoff, since real columns fail by a combination of instability and inelastic material behavior. The column always buckles about the axis of **minimum** $I$ (least resistance to bending).

## Design Implication

Buckling load depends on $EI$ (stiffness), not material strength — increasing a column's yield strength alone does nothing for its buckling capacity; only increasing $I$ (via cross-sectional shape/size) or reducing $L$ (or improving end restraint, reducing $K$) raises $P_{cr}$.

---
Cross-domain: [[The Universal Second-Order Linear System|this ODE is literally an RLC circuit's equation]] · [[Resonance and Buckling - Instability as an Eigenvalue Problem|buckling and electrical resonance are the same eigenvalue problem]] · [[Stability of Floating Bodies - Metacentre|a ship capsizing (GM<0) is the same kind of stability-sign-flip as a column buckling]]

Next: [[Strain Energy and Castigliano's Theorem]]

## Check yourself

> [!question]- Q1. A pinned-pinned steel column ($E=200$ GPa), 40 mm diameter and 2 m long. Find $P_{cr}$.
> $I=\pi d^4/64=1.257\times10^{-7}$ m⁴, so $P_{cr}=\pi^2EI/L^2=62.0$ kN.

> [!question]- Q2. The same column is fixed at the base and free at the top. Find $P_{cr}$.
> $K=2$, so the load falls to a quarter: $15.5$ kN.

> [!question]- Q3. When does Euler's formula stop being valid?
> When the Euler stress would exceed the yield stress. For $E=200$ GPa and $\sigma_Y=250$ MPa that is at $\lambda=KL/r<\pi\sqrt{E/\sigma_Y}\approx89$.


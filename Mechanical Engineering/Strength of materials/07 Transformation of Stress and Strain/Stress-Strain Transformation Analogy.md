Related: [[Plane Stress Transformation]] · [[Mohr's Circle for Stress]] · [[Strain Transformation and Rosettes]]

Stress and strain transformation are **the same mathematical structure** — a symmetric $2\times2$ tensor being rotated — with one substitution to keep straight. This note is the fast-recall mnemonic layer on top of the derivations in the linked notes above.

## The One Substitution That Matters

$$\boxed{\tau \ \longleftrightarrow\ \frac{\gamma}{2}}$$
Everywhere a stress formula has $\sigma_x,\sigma_y,\tau_{xy}$, the corresponding strain formula has $\varepsilon_x,\varepsilon_y,\gamma_{xy}/2$. This single fact generates *every* transformation, principal-value, and Mohr's-circle formula for strain from the stress version.

| | Stress | Strain |
|---|---|---|
| $x$ quantity | $\sigma_x$ | $\varepsilon_x$ |
| $y$ quantity | $\sigma_y$ | $\varepsilon_y$ |
| engineering shear | $\tau_{xy}$ | $\gamma_{xy}$ |
| **tensor** shear component | $\tau_{xy}$ | $\gamma_{xy}/2$ |

## Matrix (Tensor) Form

$$\boldsymbol{\sigma}=\begin{bmatrix}\sigma_x&\tau_{xy}\\\tau_{xy}&\sigma_y\end{bmatrix} \qquad\qquad \boldsymbol{\varepsilon}=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix}$$
Both transform under rotation the same way: $\mathbf{T}' = \mathbf{Q}\,\mathbf{T}\,\mathbf{Q}^T$, with
$$\mathbf{Q}=\begin{bmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{bmatrix}$$
This is why the transformation *equations* in [[Plane Stress Transformation]] and [[Strain Transformation and Rosettes]] look identical after the $\tau\leftrightarrow\gamma/2$ swap — they're literally the same rotation formula applied to two different (but structurally identical) tensors.

## Universal Formula

Define a generic symmetric tensor $\mathbf{A}=\begin{bmatrix}A_x&A_{xy}\\A_{xy}&A_y\end{bmatrix}$. Its principal values (eigenvalues) are
$$A_{1,2} = \frac{A_x+A_y}{2}\pm\sqrt{\left(\frac{A_x-A_y}{2}\right)^2+A_{xy}^2}$$
Substitute:
- **Stress:** $A_x=\sigma_x,\ A_y=\sigma_y,\ A_{xy}=\tau_{xy}$
- **Strain:** $A_x=\varepsilon_x,\ A_y=\varepsilon_y,\ A_{xy}=\gamma_{xy}/2$

That's the whole topic in one line: **Principal = Average ± Radius**, with the radius built from a "difference" term and a "shear" term under a square root — exactly the structure of Mohr's circle in [[Mohr's Circle for Stress]].

## Eigenvalue / Eigenvector Interpretation

$$\det(\boldsymbol{\sigma}-\lambda I)=0 \implies \lambda=\sigma_1,\sigma_2 \qquad \det(\boldsymbol{\varepsilon}-\lambda I)=0 \implies \lambda=\varepsilon_1,\varepsilon_2$$
**Principal stresses/strains are eigenvalues; principal directions are eigenvectors.** This is the linear-algebra restatement of Mohr's circle — diagonalizing the tensor is exactly finding the rotation angle $\theta_p$ at which off-diagonal (shear) terms vanish.

## Side-by-Side Transformation Equations

| | Stress | Strain |
|---|---|---|
| Normal ($x'$) | $\sigma_{x'}=\sigma_{avg}+\dfrac{\sigma_x-\sigma_y}{2}\cos2\theta+\tau_{xy}\sin2\theta$ | $\varepsilon_{x'}=\varepsilon_{avg}+\dfrac{\varepsilon_x-\varepsilon_y}{2}\cos2\theta+\dfrac{\gamma_{xy}}{2}\sin2\theta$ |
| Normal ($y'$) | $\sigma_{y'}=\sigma_{avg}-\dfrac{\sigma_x-\sigma_y}{2}\cos2\theta-\tau_{xy}\sin2\theta$ | $\varepsilon_{y'}=\varepsilon_{avg}-\dfrac{\varepsilon_x-\varepsilon_y}{2}\cos2\theta-\dfrac{\gamma_{xy}}{2}\sin2\theta$ |
| Shear | $\tau_{x'y'}=-\dfrac{\sigma_x-\sigma_y}{2}\sin2\theta+\tau_{xy}\cos2\theta$ | $\gamma_{x'y'}=-(\varepsilon_x-\varepsilon_y)\sin2\theta+\gamma_{xy}\cos2\theta$ |
| Principal | $\sigma_{1,2}=\sigma_{avg}\pm\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}$ | $\varepsilon_{1,2}=\varepsilon_{avg}\pm\sqrt{\left(\frac{\varepsilon_x-\varepsilon_y}{2}\right)^2+\left(\frac{\gamma_{xy}}{2}\right)^2}$ |
| Principal angle | $\tan2\theta_p=\dfrac{2\tau_{xy}}{\sigma_x-\sigma_y}$ | $\tan2\theta_p=\dfrac{\gamma_{xy}}{\varepsilon_x-\varepsilon_y}$ |
| Max shear | $\tau_{max}=R=\dfrac{\sigma_1-\sigma_2}{2}$ | $\gamma_{max}=2R=\varepsilon_1-\varepsilon_2$ |
| Max-shear angle | $\theta_p+45°$ | $\theta_p+45°$ |
| Zero-shear condition | principal planes: $\tau'=0$ | principal directions: $\gamma'=0$ |

**Why the shear (normal-equation) rows look identical after substitution, but the shear-transformation row looks different at first glance:** the strain shear-transformation equation is written for **engineering** $\gamma_{x'y'}$ (not the tensor component $\varepsilon_{x'y'}=\gamma_{x'y'}/2$), so it comes out looking like it's missing a factor of 2 compared to the stress version — it isn't; the equation for $\varepsilon_{x'y'}$ (tensor form) would match $\tau_{x'y'}$ exactly under the substitution. Concretely:
> **Normal equations:** replace $\tau$ with $\gamma/2$.
> **Shear equation:** the tensor-form result must be **multiplied by 2** to get engineering $\gamma_{x'y'}$.

**The one relation responsible for most sign/factor-of-2 mistakes:**
$$\boxed{\gamma_{xy}=2\varepsilon_{xy}}$$

## Fast Recall Table (write this at the top of your working before solving)

$$\begin{array}{c|c}\text{STRESS}&\text{STRAIN}\\\hline \sigma_x&\varepsilon_x\\ \sigma_y&\varepsilon_y\\ \tau&\gamma/2\end{array}$$

Then apply one universal formula: $\text{Principal}=\text{Average}\pm\sqrt{(\text{difference})^2+(\text{shear})^2}$.

## Top Quiz Traps

1. Forgetting the $2\theta$ (not $\theta$) inside $\sin,\cos$ of the transformation equations.
2. Using $+\theta$ for a clockwise physical rotation — clockwise is $\theta<0$.
3. Forgetting $\gamma_{xy}=2\varepsilon_{xy}$.
4. Using $\gamma$ instead of $\gamma/2$ when computing the strain "radius" $R_\varepsilon$.
5. Confusing $\tau_{max}=R$ (stress) with $\gamma_{max}=2R$ (strain).
6. Forgetting principal planes/directions have **zero** shear stress/strain by definition.
7. Forgetting max-shear planes sit at exactly $45°$ from the principal planes.
8. Solving $\tan2\theta_p=(\cdots)$ and reporting $2\theta_p$ instead of $\theta_p$.
9. Not checking which root ($C+R$ vs $C-R$) is $\sigma_1$/$\varepsilon_1$ (the larger one) vs $\sigma_2$/$\varepsilon_2$.
10. Mixing units (MPa/GPa, N/mm) without converting consistently.

---
Related: [[Generalized Hooke's Law and Poisson's Ratio]] (converting principal strains ↔ principal stresses) · [[Euler Buckling of Columns]]

Cross-domain: [[Eigenvalues, Rotation and Diagonalization Everywhere|why this note's $2\theta$ is the same fact as phasor rotation and Mohr's circle]] · [[The Mechanical-Electrical Analogy (Impedance Analogy)|the same transformation mindset applied to whole mechanics vs circuit problems]]

## Check yourself

> [!question]- Q1. Which strain quantity plays the role of shear stress in the transformation equations?
> Half the engineering shear strain, $\gamma/2$. Replace $\sigma\to\varepsilon$ and $\tau\to\gamma/2$ and the stress formulas become the strain formulas.

> [!question]- Q2. What is plotted on the vertical axis of Mohr's circle for strain?
> $\gamma/2$ (with the same sign convention as for $\tau$), against $\varepsilon$ on the horizontal axis.


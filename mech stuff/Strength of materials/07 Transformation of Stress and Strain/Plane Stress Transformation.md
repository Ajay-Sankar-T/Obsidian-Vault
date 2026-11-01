Related: [[Shear Stress Formula for Beams]] · [[Generalized Hooke's Law and Poisson's Ratio]] · [[Mohr's Circle for Stress]] · [[Stress-Strain Transformation Analogy]]

## Why Transformation Is Needed

The stress components $\sigma_x,\sigma_y,\tau_{xy}$ at a point depend on the orientation of the coordinate axes chosen to describe them — they are **not** invariant. The same physical stress state, viewed on a plane rotated by angle $\theta$, has different components $\sigma_{x'},\sigma_{y'},\tau_{x'y'}$. Since failure (yielding, fracture) is governed by the actual stress on the "weakest" plane, not by whatever orientation the analyst happened to draw axes at, engineers need a systematic way to find the stress on **any** plane through a point — in particular, the plane of **maximum normal stress** (principal stress) and the plane of **maximum shear stress**.

## Derivation via Wedge Equilibrium

Consider a small triangular wedge cut from the stressed element, with one face at angle $\theta$ to the $x$-axis. Equilibrium of forces on the wedge (resolving $\sigma_x,\sigma_y,\tau_{xy}$ acting on the two orthogonal faces into components along and perpendicular to the inclined face) gives:
$$\sigma_{x'} = \frac{\sigma_x+\sigma_y}{2}+\frac{\sigma_x-\sigma_y}{2}\cos2\theta+\tau_{xy}\sin2\theta$$
$$\tau_{x'y'} = -\frac{\sigma_x-\sigma_y}{2}\sin2\theta+\tau_{xy}\cos2\theta$$
$$\sigma_{y'} = \frac{\sigma_x+\sigma_y}{2}-\frac{\sigma_x-\sigma_y}{2}\cos2\theta-\tau_{xy}\sin2\theta$$
(obtained from $\sigma_{x'}$ by replacing $\theta\to\theta+90°$). Note the invariant: $\sigma_{x'}+\sigma_{y'}=\sigma_x+\sigma_y$ — the **sum of normal stresses on any two perpendicular planes is constant** (this is the trace of the stress tensor, invariant under rotation).

## Principal Stresses

The orientation $\theta_p$ that makes $\tau_{x'y'}=0$ (no shear on that plane) defines the **principal planes**:
$$\tan2\theta_p = \frac{2\tau_{xy}}{\sigma_x-\sigma_y}$$
The two roots of this equation (90° apart) give the **principal stresses**, found by maximizing/minimizing $\sigma_{x'}$:
$$\sigma_{1,2} = \frac{\sigma_x+\sigma_y}{2}\pm\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}$$
By convention $\sigma_1\ge\sigma_2$. On principal planes, shear stress is exactly zero — this is why principal stresses are the natural quantities to compare against material strength.

## Maximum In-Plane Shear Stress

Occurs on planes at $45°$ to the principal planes:
$$\tau_{max} = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2} = \frac{\sigma_1-\sigma_2}{2}$$
with an associated normal stress equal to the average $\dfrac{\sigma_x+\sigma_y}{2}$ (i.e., the max-shear planes are generally **not** shear-free in the normal direction).

## Eigenvalue Interpretation

Writing the plane-stress state as the symmetric matrix
$$[\sigma] = \begin{pmatrix}\sigma_x & \tau_{xy}\\ \tau_{xy} & \sigma_y\end{pmatrix},$$
the principal stresses are exactly the **eigenvalues** of $[\sigma]$ (roots of $\det([\sigma]-\lambda I)=0$), and the principal directions are the corresponding **eigenvectors**. Rotating the reference frame corresponds to the similarity transform $[\sigma]'=Q[\sigma]Q^T$ with rotation matrix $Q=\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix}$ — this is the linear-algebra structure underlying every transformation formula above. See [[Stress-Strain Transformation Analogy]] for the parallel matrix/eigenvalue treatment of strain, which uses exactly the same machinery.

---
Next: [[Mohr's Circle for Stress]]

## See also
- [[Materials and Design - MOC]] — failure criteria built from principal stresses.

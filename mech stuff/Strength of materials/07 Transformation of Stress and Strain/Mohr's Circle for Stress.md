Related: [[Plane Stress Transformation]] · [[Stress-Strain Transformation Analogy]]

## Why Mohr's Circle Works

The transformation equations from [[Plane Stress Transformation]],
$$\sigma_{x'}=\sigma_{avg}+\frac{\sigma_x-\sigma_y}{2}\cos2\theta+\tau_{xy}\sin2\theta, \qquad \tau_{x'y'}=-\frac{\sigma_x-\sigma_y}{2}\sin2\theta+\tau_{xy}\cos2\theta,$$
are the parametric equations of a **circle** in the $(\sigma,\tau)$ plane: eliminating $\theta$ gives
$$\left(\sigma_{x'}-\sigma_{avg}\right)^2+\tau_{x'y'}^2 = R^2, \qquad \sigma_{avg}=\frac{\sigma_x+\sigma_y}{2}, \quad R=\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}.$$
This is **Mohr's circle**: center $C=(\sigma_{avg},0)$, radius $R$.

## Constructing the Circle

1. Plot the point $(\sigma_x,\tau_{xy})$ — representing the $x$-face.
2. Plot the point $(\sigma_y,-\tau_{xy})$ — representing the $y$-face (note the **sign flip** on shear; this is what makes the two points diametrically opposite).
3. The line joining these two points is a diameter; its midpoint is the center $C=(\sigma_{avg},0)$.

## Reading Off Results

$$\sigma_1=C+R, \qquad \sigma_2=C-R, \qquad \tau_{max}=R=\frac{\sigma_1-\sigma_2}{2}$$
- **Principal stresses** are where the circle crosses the $\tau=0$ axis.
- **Maximum shear** is the topmost/bottommost point of the circle, at $\sigma=\sigma_{avg}$ — confirming that the max-shear plane carries a nonzero normal stress equal to the average.

## The Critical Quiz Trap: Angle Doubling

Every angle measured **on Mohr's circle** is **twice** the actual physical angle between planes:
$$\boxed{\theta_{\text{Mohr's circle}} = 2\theta_{\text{physical}}}$$
So rotating the physical element by $\theta$ (counterclockwise positive) corresponds to rotating **around the circle** by $2\theta$ in the **same rotational sense** (with the standard construction above). This single fact accounts for most sign/angle errors in stress-transformation problems.

## Special Cases (memorize these two)

**Pure uniaxial stress** ($\sigma_x=\sigma,\ \sigma_y=0,\ \tau_{xy}=0$):
$$\sigma_1=\sigma, \quad \sigma_2=0, \quad \tau_{max}=\frac{\sigma}{2}$$

**Pure shear** ($\sigma_x=\sigma_y=0,\ \tau_{xy}=\tau$):
$$\sigma_1=+\tau, \quad \sigma_2=-\tau, \quad \tau_{max}=\tau$$
Principal planes are at exactly $45°$ to the original — this is why brittle materials in torsion (pure shear on the shaft surface) fracture along a $45°$ helix (see [[Torsion of Circular Shafts]]): they fail in tension along the principal-stress direction, not in shear.

## Sign Convention for Rotation

- Physical rotation **counterclockwise**: $\theta>0$.
- Physical rotation **clockwise**: $\theta<0$ (e.g. "$30°$ clockwise" $\Rightarrow \theta=-30°,\ 2\theta=-60°$).

## Fast Algorithm

1. $\sigma_{avg}=\dfrac{\sigma_x+\sigma_y}{2}$
2. $R=\sqrt{\left(\dfrac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}$
3. $\sigma_1=\sigma_{avg}+R,\ \sigma_2=\sigma_{avg}-R,\ \tau_{max}=R$
4. $\tan2\theta_p=\dfrac{2\tau_{xy}}{\sigma_x-\sigma_y}$, then $\theta_p=\tfrac12\tan^{-1}(\cdots)$, and the max-shear plane is at $\theta_p+45°$.

The identical construction applies to strain (with $\tau\to\gamma/2$) — see [[Strain Transformation and Rosettes]] and the full [[Stress-Strain Transformation Analogy]].

---
Next: [[Strain Transformation and Rosettes]]

## See also
- [[Materials and Design - MOC]] — static failure theories (Tresca, von Mises, Mohr–Coulomb) applied to these stress states.

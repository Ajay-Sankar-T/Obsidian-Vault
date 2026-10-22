Related: [[Mohr's Circle for Stress]] · [[Stress-Strain Transformation Analogy]] · [[Generalized Hooke's Law and Poisson's Ratio]]

## From Displacement Field to Strain

For a 2D displacement field $u(x,y)$ (in the $x$-direction) and $v(x,y)$ (in the $y$-direction), the strains at a point are:
$$\varepsilon_x=\frac{\partial u}{\partial x}, \qquad \varepsilon_y=\frac{\partial v}{\partial y}, \qquad \gamma_{xy}=\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}$$
$\gamma_{xy}$ here is the **engineering shear strain** (total angular distortion). It relates to the *tensor* shear-strain component by
$$\boxed{\gamma_{xy}=2\varepsilon_{xy}}$$
— the single most important fact to keep straight in this whole topic (see [[Stress-Strain Transformation Analogy]] for why).

**Worked example:** if $u=u_0+7(10^{-3})x+4(10^{-3})y$ and $v=v_0+2(10^{-3})x-1(10^{-3})y$, then
$$\varepsilon_x=7\times10^{-3}, \quad \varepsilon_y=-1\times10^{-3}, \quad \gamma_{xy}=4\times10^{-3}+2\times10^{-3}=6\times10^{-3}$$

## Strain Transformation Equations

Exactly parallel in structure to the stress-transformation equations of [[Plane Stress Transformation]], with $\sigma\to\varepsilon$ and $\tau\to\gamma/2$:
$$\varepsilon_{x'}=\frac{\varepsilon_x+\varepsilon_y}{2}+\frac{\varepsilon_x-\varepsilon_y}{2}\cos2\theta+\frac{\gamma_{xy}}{2}\sin2\theta$$
$$\varepsilon_{y'}=\frac{\varepsilon_x+\varepsilon_y}{2}-\frac{\varepsilon_x-\varepsilon_y}{2}\cos2\theta-\frac{\gamma_{xy}}{2}\sin2\theta$$
$$\gamma_{x'y'}=-(\varepsilon_x-\varepsilon_y)\sin2\theta+\gamma_{xy}\cos2\theta$$
Note the shear equation has **no** factor of $\tfrac12$ on $(\varepsilon_x-\varepsilon_y)$'s coefficient or on $\gamma_{xy}$ itself — it's written for the *engineering* strain $\gamma_{x'y'}$ directly (equivalent to writing the tensor equation and then doubling the result).

## Principal Strains and Maximum Shear Strain

$$\varepsilon_{avg}=\frac{\varepsilon_x+\varepsilon_y}{2}, \qquad R_\varepsilon=\sqrt{\left(\frac{\varepsilon_x-\varepsilon_y}{2}\right)^2+\left(\frac{\gamma_{xy}}{2}\right)^2}$$
$$\varepsilon_{1,2}=\varepsilon_{avg}\pm R_\varepsilon, \qquad \gamma_{max}=2R_\varepsilon=\sqrt{(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2}=\varepsilon_1-\varepsilon_2$$
Principal direction:
$$\tan2\theta_p=\frac{\gamma_{xy}}{\varepsilon_x-\varepsilon_y}$$
(compare to stress's $\tan2\theta_p=2\tau_{xy}/(\sigma_x-\sigma_y)$ — the strain version has $\gamma$ where stress has $2\tau$, precisely because $\gamma=2\varepsilon_{xy}$). Maximum-shear-strain planes are at $\theta_p+45°$, and there $\varepsilon_{x'}=\varepsilon_{y'}=\varepsilon_{avg}$.

**Special case:** if $\gamma_{xy}=0$, the $x,y$ axes are *already* principal strain directions, and $\varepsilon_1,\varepsilon_2$ are simply $\varepsilon_x,\varepsilon_y$ (in whichever order is larger).

## Strain Gauge Rosettes

A single strain gauge measures normal strain in **one** direction only. To determine the full 2D strain state $(\varepsilon_x,\varepsilon_y,\gamma_{xy})$ at a point, three gauges at known, different angles (a **rosette**) are needed — each gives one equation via the normal-strain transformation formula above.

**$0°$–$60°$–$120°$ rosette** (gauges $a,b,c$ at those angles from the $x$-axis): with $\varepsilon_a=\varepsilon_x$ directly,
$$\varepsilon_y=\frac{2(\varepsilon_b+\varepsilon_c)-\varepsilon_a}{3}, \qquad \gamma_{xy}=\frac{2(\varepsilon_b-\varepsilon_c)}{\sqrt3}$$
Once $\varepsilon_x,\varepsilon_y,\gamma_{xy}$ are recovered, treat the problem as an ordinary strain-transformation/Mohr's-circle problem (find $\varepsilon_1,\varepsilon_2,\gamma_{max}$, principal directions, etc.). Converting the resulting principal *strains* to principal *stresses* for a design check uses the [[Generalized Hooke's Law and Poisson's Ratio|generalized Hooke's law]] (plane-stress form), which is exactly why strain gauges — which measure strain directly, since stress can't be measured directly — are useful in the first place.

## The Strain Tensor

$$[\varepsilon] = \begin{pmatrix}\varepsilon_x & \gamma_{xy}/2\\ \gamma_{xy}/2 & \varepsilon_y\end{pmatrix}, \qquad \text{3D: } [\varepsilon]=\begin{pmatrix}\varepsilon_x & \gamma_{xy}/2 & \gamma_{xz}/2\\ \gamma_{xy}/2 & \varepsilon_y & \gamma_{yz}/2 \\ \gamma_{xz}/2 & \gamma_{yz}/2 & \varepsilon_z\end{pmatrix}$$

---
Next: [[Stress-Strain Transformation Analogy]]

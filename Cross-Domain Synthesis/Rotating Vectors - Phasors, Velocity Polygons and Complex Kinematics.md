---
tags: [synthesis, cross-domain, phasors, kinematics, complex-numbers]
up: "[[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC]]"
---

# Rotating Vectors — Phasors, Velocity Polygons and Complex Kinematics

← up: [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]

A phasor diagram and a velocity polygon are the same construction: **a closed polygon of vectors, each side a rotated and scaled copy of one underlying quantity**. The link between them is one fact: differentiating a rotating vector multiplies it by $j\omega$.

## Differentiation is multiplication by $j\omega$

Write a point on a link as $r\,e^{j\theta}$ with $\dot\theta=\omega$.

| Kinematics | Phasors |
|---|---|
| $\dot{(re^{j\theta})}=j\omega\,re^{j\theta}$: velocity is the position vector turned $90^\circ$ and scaled by $\omega$ | $\dfrac{d}{dt}\to j\omega$: $V_L=j\omega L\,I$, current phasor turned $90^\circ$ |
| second derivative $(j\omega)^2=-\omega^2$ plus $j\alpha$: acceleration $=(-\omega^2+j\alpha)\,re^{j\theta}$ | $\dfrac{d^2}{dt^2}\to-\omega^2$ (the $\omega_0^2$ term in [[Cross-Domain Synthesis/The Universal Second-Order Linear System|the universal second-order system]]) |
| $\mathbf V_B=\mathbf V_A+\boldsymbol\omega\times\overrightarrow{AB}$ (eq. 2.16) | ELI/ICE: $V$ leads $I$ by $90^\circ$ for $L$, lags for $C$ |
| $a_B-a_A$: $AB\,\omega^2$ along $BA$ plus $AB\,\alpha\perp AB$ (eq. 2.17) | impedance $Z=R+jX$: in-phase part plus quadrature part |

Equation 2.16/2.17 are in [[KDoMs/Velocity-Acceleration-Bank/Velocity and Acceleration - Analytical Method|Velocity and Acceleration — Analytical Method]]; the phase rules are in [[05 Sinusoids and Phasors|Week 5]].

## Loop closure ≙ KVL

A four-bar loop obeys $\mathbf r_1+\mathbf r_2+\mathbf r_3+\mathbf r_4=0$; differentiating gives the **velocity polygon**, which also closes. A series circuit obeys $\sum\mathbf V=0$ as phasors; the phasor diagram of $V_R+V_L+V_C=V_s$ is a closed polygon whose sides are all the **same current** turned by $0^\circ$, $+90^\circ$, $-90^\circ$ and scaled by $|Z|$ of each element. In the velocity polygon each side is a **different** link vector turned $90^\circ$ and scaled by that link's own $\omega_i$. Same closure, different bookkeeping:

```text
Phasor diagram:   one I   × (R, jωL, 1/jωC)       → sides of the voltage polygon
Velocity polygon: r_i e^{jθ_i} × (jω_i)            → sides of the velocity polygon
```

See [[KDoMs/Velocity-Acceleration-Bank/Velocity and Acceleration - Graphical Methods (Polygons)|Graphical Methods (Polygons)]] and [[Phasors and Complex Algebra|Phasors and Complex Algebra]].

## A new angle: the acceleration image has an impedance angle

From eq. 2.17 the relative acceleration of two points on a rigid link has components $AB\,\omega^2$ (along $BA$) and $AB\,\alpha$ (perpendicular). So the acceleration vector sits at

$$\psi=\arctan\frac{\alpha}{\omega^{2}}$$

from the link, with magnitude $AB\sqrt{\omega^4+\alpha^2}$. That is exactly $|Z|=\sqrt{R^2+X^2}$ and $\theta_Z=\arctan(X/R)$ with $\omega^2\leftrightarrow R$ and $\alpha\leftrightarrow X$. The velocity image is the special case $\psi=90^\circ$ with no in-phase part. Both are rank-1 vector rotations, which is why the angle appears at $1\times$, not $2\times$; see [[Cross-Domain Synthesis/Eigenvalues, Rotation and Diagonalization Everywhere|Eigenvalues, Rotation and Diagonalization Everywhere]].

## Where the analogy stops

- A phasor drops the common factor $e^{j\omega t}$ because every quantity rotates at **one** frequency in a **linear** circuit. In a mechanism each link has its own $\omega_i$ and the geometry is nonlinear, so the polygon is valid only at one instant.
- Coriolis acceleration $2\boldsymbol\omega\times\mathbf V_{P/i}$ (sliding joints, [[KDoMs/Problem-2.19-solution|Problem 2.19]]) has no phasor counterpart.

## Related
- [[KDoMs/KDoMs - MOC|KDoMs MOC]]
- [[05 Sinusoids and Phasors|Week 5 — Sinusoids and Phasors]]
- [[Cross-Domain Synthesis/Eigenvalues, Rotation and Diagonalization Everywhere|Eigenvalues, Rotation and Diagonalization Everywhere]]

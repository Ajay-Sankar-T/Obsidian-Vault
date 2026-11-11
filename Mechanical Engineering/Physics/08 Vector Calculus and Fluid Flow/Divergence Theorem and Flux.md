---
tags: [concept, physics-1, PH1010, vector-calculus, divergence, flux, gauss]
status: draft
up: "[[Physics I - MOC]]"
aliases: [divergence theorem, Gauss's divergence theorem, flux, divergence, Gauss's law, source and sink]
---

# Divergence Theorem and Flux

> [!abstract] The big idea
> **Flux** counts how much of a field pours through a surface. **Divergence** is flux per unit volume at a point: how strongly the field spreads out (a source) or draws in (a sink) right there. The divergence theorem says the two views agree: *the total outflow through a closed surface equals the sum of all sources inside.* Swap a hard surface integral for an easy volume integral, or the reverse.

## Flux through a surface

![[PH-flux-patches.png]]

**Figure:** A uniform field (grey) through a flat plate. Face-on it catches everything, tilted it catches $\cos\theta$ of it, edge-on nothing. Each patch contributes $\mathbf F\cdot\hat{\mathbf n}\,dA$; adding them up is the surface integral

$$\Phi=\iint_S\mathbf F\cdot\hat{\mathbf n}\,dA=\iint_S\mathbf F\cdot d\mathbf S$$

For a closed surface $\hat{\mathbf n}$ points **outward**: positive $\Phi$ means net outflow.

## Divergence

$$\nabla\cdot\mathbf F=\frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}+\frac{\partial F_z}{\partial z}=\lim_{V\to0}\frac1V\oint_{\partial V}\mathbf F\cdot d\mathbf S$$

![[PH-div-fields.png]]

**Figure:** Left, a source $\mathbf F=(x,y)$ has $\nabla\cdot\mathbf F=+2$ everywhere (the field spreads). Middle, a sink has $-2$. Right, a field of strength $1/r$ (a line source) looks like it "spreads" yet has $\nabla\cdot\mathbf F=0$ away from the origin: the field weakens by exactly the amount the circle's circumference grows, so the flux through every circle is the same. The line thickness shows the field strength.

In curvilinear coordinates ([[Curvilinear Coordinates - Cylindrical and Spherical]]):

$$\nabla\cdot\mathbf A=\frac1\rho\frac{\partial(\rho A_\rho)}{\partial\rho}+\frac1\rho\frac{\partial A_\phi}{\partial\phi}+\frac{\partial A_z}{\partial z}\ \ \text{(cyl.)},\qquad\nabla\cdot\mathbf A=\frac{1}{r^2}\frac{\partial(r^2A_r)}{\partial r}+\frac{1}{r\sin\theta}\frac{\partial(\sin\theta A_\theta)}{\partial\theta}+\frac{1}{r\sin\theta}\frac{\partial A_\phi}{\partial\phi}\ \ \text{(sph.)}$$

## The theorem

$$\boxed{\;\oint_S\mathbf F\cdot d\mathbf S=\iiint_V\nabla\cdot\mathbf F\,dV\;}$$

with $S$ the closed boundary of $V$ and $\hat{\mathbf n}$ pointing out.

> [!question]- 🎯 Predict first: the field $\mathbf F=\hat r/r^2$ (an inverse-square field) has divergence zero everywhere except the origin. What is its flux through a sphere around the origin?
> $4\pi$, for *every* sphere and every closed surface enclosing the origin: $F=1/R^2$ times the area $4\pi R^2$. The whole $4\pi$ is hiding in a delta function at the origin ($\nabla\cdot\hat r/r^2=4\pi\delta^3(\mathbf r)$). This is **Gauss's law**: $\oint\mathbf E\cdot d\mathbf S=Q_{\rm enc}/\epsilon_0$, i.e. $\nabla\cdot\mathbf E=\rho/\epsilon_0$.

## Method

1. **Decide:** is the surface or the volume integral easier? A closed surface of simple shape plus a simple field often favours whichever is *constant* (sphere + radial field $\to$ surface; a messy field $\to$ divergence).
2. **Surface route:** parameterise $\hat{\mathbf n}\,dA$ on each face, compute $\mathbf F\cdot\hat{\mathbf n}$, integrate. Include *all* faces.
3. **Volume route:** compute $\nabla\cdot\mathbf F$ (in the right coordinates), integrate over $V$.
4. **Open surface?** The theorem needs a *closed* surface: add the missing lid or integrate a different way.
5. **Check:** both routes must agree.

## Common traps

> [!warning]- ⚠️ Forgetting a face of the closed surface
> A cylinder has three faces (curved side, top, bottom). Missing one is the most common slip when using the surface route.

> [!warning]- ⚠️ Inward normal
> The theorem uses the **outward** normal. An inward normal flips the sign of the flux.

> [!danger]- 💥 Applying the theorem across a singularity
> If $\mathbf F$ blows up inside $V$ (as $\hat r/r^2$ does at the origin), $\nabla\cdot\mathbf F=0$ elsewhere is *not* the whole story: the singular point contributes. Check for singularities before integrating a "zero" divergence.

## Worked example

> [!example]- 🔬 Verify the theorem for $\mathbf F=\mathbf r=(x,y,z)$ on a sphere of radius $R$
> **Surface:** on the sphere $\mathbf F=R\hat r$ and $\hat{\mathbf n}=\hat r$, so $\mathbf F\cdot\hat{\mathbf n}=R$ and $\Phi=R\cdot4\pi R^2=4\pi R^3$.
> **Volume:** $\nabla\cdot\mathbf r=3$, so $\iiint3\,dV=3\cdot\tfrac43\pi R^3=4\pi R^3$ ✓.
> **Check:** flux per volume $=4\pi R^3/(\tfrac43\pi R^3)=3=\nabla\cdot\mathbf F$ exactly, for any $R$.

## Quick quiz

> [!question]- Q1. $\mathbf F=(x^2,\,y^2,\,z^2)$. What is $\nabla\cdot\mathbf F$ and what does it say at the origin?
> $2x+2y+2z$, which is $0$ at the origin and changes sign with position: sources where the sum is positive, sinks where it is negative.

> [!question]- Q2. An incompressible fluid has $\nabla\cdot\mathbf u=0$. What does this say about the flux through a closed surface?
> Zero: whatever flows in flows out ([[Fluid Flow, Continuity and Bernoulli]]).

> [!question]- Q3. Why can there be no magnetic field with $\mathbf B=\hat r/r^2$?
> $\nabla\cdot\mathbf B=0$ (no magnetic monopoles), but this field has non-zero flux $4\pi$ out of every sphere. Field lines of $\mathbf B$ must close on themselves.

## Connections

### Prerequisites
- [[Conservative Forces, Gradient and Curl]], [[Curvilinear Coordinates - Cylindrical and Spherical]]

### Next
- [[Stokes' Theorem and Circulation]]: the same idea one dimension down (loop vs surface).
- [[Fluid Flow, Continuity and Bernoulli]]: $\nabla\cdot\mathbf u=0$ for incompressible flow.

### Cross-domain links
- [[Conservation of Mass (Continuity Equation)]] and [[Reynolds Transport Theorem]]: the integral continuity equation is the divergence theorem applied to a control volume.
- [[Differential Mass Conservation and Fluid Kinematics - Formula Bank]]: the differential form $\nabla\cdot\mathbf u=0$ is what the divergence theorem shrinks to.
- [[Conservation Laws and Flow Networks]]: Kirchhoff's current law is the discrete divergence theorem (net current out of a node is zero).
- [[Laplace Equation on Rectangles and Strips]]: $\nabla^2\phi=\nabla\cdot\nabla\phi=0$ is "no sources" for a potential flow.

## Self-check
- [ ] I can compute flux through a face and through a closed surface.
- [ ] I can compute divergence in Cartesian, cylindrical and spherical coordinates.
- [ ] I can verify the divergence theorem both ways on a simple solid.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** intermediate–advanced
- **Course map:** [[Physics I - MOC]]

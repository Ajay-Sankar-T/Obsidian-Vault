---
tags: [concept, physics-1, PH1010, vectors, transformation]
status: draft
up: "[[Physics I - MOC]]"
aliases: [rotation matrix, coordinate transformation, orthogonal matrix, passive rotation]
---

# Rotation Matrix and Vector Transformation

> [!abstract] The big idea
> A vector is a physical arrow; its components are just how one particular set of axes reads it. Turn the axes and the numbers change but the arrow, its length and the angle between two arrows do not. The **rotation matrix** is the rule that converts one set of numbers into the other, and "orthogonal" is the property that makes lengths survive.

## Visual

![[PH-vec-rotation.png]]

**Figure:** One arrow $\mathbf r$ (red), two descriptions. In the grey axes it reads $(2.60,\,1.90)$, in the blue axes (turned by $\phi=30^\circ$) it reads $(3.20,\,0.35)$. Same arrow, same length $\sqrt{2.6^2+1.9^2}=\sqrt{3.2^2+0.35^2}=3.22$.

> [!question]- 🎯 Predict first: if you rotate the axes counter-clockwise, does a fixed arrow's angle (measured from the axis) go up or down?
> Down. Turning the ruler one way makes the thing it measures look like it turned the other way. That is why the $y'$ row of the matrix below carries a minus sign on $x$.

## Governing relation

For axes rotated by $\phi$ about $z$ (components in the new axes from components in the old):

$$\begin{pmatrix}x'\\y'\\z'\end{pmatrix}=\underbrace{\begin{pmatrix}\cos\phi&\sin\phi&0\\-\sin\phi&\cos\phi&0\\0&0&1\end{pmatrix}}_{R}\begin{pmatrix}x\\y\\z\end{pmatrix},\qquad x_i'=R_{ij}x_j$$

$R$ is **orthogonal**: $R^{T}R=\mathbb 1$, so $R^{-1}=R^{T}$ and $\det R=+1$. Each row is a new unit vector written in old components, which is why the rows are orthonormal.

**Why lengths survive:** $x_i'x_i'=R_{ij}x_j\,R_{ik}x_k=(R^TR)_{jk}x_jx_k=\delta_{jk}x_jx_k=x_jx_j$. The same line proves that $\mathbf u\cdot\mathbf v$ is unchanged. Numbers that do not change under rotation are called **scalars**; that is the working definition.

> [!tip]- 🧠 What "transforms like a vector" means
> Not every triple of numbers is a vector. $(x,y,z)$ is, because it obeys $x_i'=R_{ij}x_j$. $(T,\,P,\,V)$ of a gas is not: rotate your lab and nothing happens to the temperature. This test is how you check that a quantity such as velocity, force or the gradient is really a vector.

## Method

1. **Draw both sets of axes** and mark the angle $\phi$ between them.
2. **Write each new unit vector** in the old components: $\hat{\mathbf x}'=(\cos\phi,\sin\phi)$, $\hat{\mathbf y}'=(-\sin\phi,\cos\phi)$.
3. **Project:** $x'=\mathbf r\cdot\hat{\mathbf x}'$, $y'=\mathbf r\cdot\hat{\mathbf y}'$. These are the rows of $R$.
4. **Check:** length unchanged, and applying $R^T$ gets the old numbers back.

## Worked example

> [!example]- 🔬 Rotate the axes by $30^\circ$: where is $\mathbf r=(2.6,\,1.9)$?
> $x'=2.6\cos30^\circ+1.9\sin30^\circ=2.251+0.950=3.202$
> $y'=-2.6\sin30^\circ+1.9\cos30^\circ=-1.300+1.645=0.345$
>
> **Check:** $3.202^2+0.345^2=10.37$ and $2.6^2+1.9^2=10.37$ ✓.

## Common traps

> [!warning]- ⚠️ Active vs passive
> Rotating the *axes* by $\phi$ and rotating the *vector* by $\phi$ use matrices that are transposes of each other. Decide first which one the problem is doing; the sign of every $\sin$ depends on it.

> [!warning]- ⚠️ Rotations about different axes do not commute
> $R_x(90^\circ)R_z(90^\circ)\neq R_z(90^\circ)R_x(90^\circ)$. Try it with a book on your desk. Only rotations about the *same* axis commute.

> [!danger]- 💥 Exam killer: forgetting that $\det R=+1$
> A matrix with orthonormal rows and $\det=-1$ is a rotation *plus a mirror flip*. Cross products pick up an extra sign under such flips, which is why $\mathbf u\times\mathbf v$ is called an axial (pseudo) vector.

## Quick quiz

> [!question]- Q1. What is $R^{-1}$ for a rotation by $\phi$, without inverting anything?
> The transpose: $R^T$, which is a rotation by $-\phi$.

> [!question]- Q2. A quantity has components $(3,4)$ in one frame and $(5,0)$ in a frame rotated by some angle. Could it be a vector?
> Yes: both have length 5. If the second were $(4,4)$ it could not be a vector, since the length would have changed.

## Connections

### Prerequisites
- [[Vectors - Dot and Cross Products]]: the rows of $R$ are dot products with new unit vectors.

### Next
- [[Inertial and Non-Inertial Frames]]: a frame that moves, not just turns.
- [[Curvilinear Coordinates - Cylindrical and Spherical]]: the unit vectors there *rotate from point to point*, so $R$ depends on position.

### Cross-domain links
- [[Eigenvalues, Rotation and Diagonalization Everywhere]]: principal axes are the rotation that diagonalises a symmetric matrix, the same orthogonal $R$.
- [[Mohr's Circle for Stress]]: rotating the stress element by $\theta$ is a rotation of a tensor, which uses $R$ twice ($\sigma'=R\sigma R^T$), hence the doubled angle $2\theta$ on the circle.

## Self-check
- [ ] I can write $R$ for a rotation about $z$ and say why its rows are orthonormal.
- [ ] I can prove that lengths and dot products survive a rotation.
- [ ] I know the difference between a scalar, a vector and "just three numbers".

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** beginner–intermediate
- **Course map:** [[Physics I - MOC]]

---
tags: [fluid-mechanics, fluid-statics, buoyancy, stability, metacentre]
up: "[[Fluid Mechanics/Fluid Mechanics - MOC]]"
---

# Stability of Floating Bodies — Metacentre

← up: [[Fluid Mechanics/Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Fluid Mechanics/02 Fluid Statics/Buoyancy and Archimedes' Principle|Buoyancy and Archimedes' Principle]], [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area]]

## Why floating bodies need a different stability criterion than submerged ones

For a **fully submerged** body ([[Fluid Mechanics/02 Fluid Statics/Buoyancy and Archimedes' Principle|Buoyancy and Archimedes' Principle]]), the centre of buoyancy $B$ stays fixed relative to the body no matter how it's oriented (the whole body displaces fluid, always the same shape of displaced volume). But for a **floating** body, tilting changes *which part* of the body is underwater, so the displaced volume's shape — and hence $B$ — shifts with every tilt. "Is $B$ above $G$" is no longer a fixed fact about the body; it must be re-examined after a small tilt.

## The metacentre

When a floating body tilts through a small angle $\theta$, the centre of buoyancy moves, $B\to B'$. The vertical line of action of the new buoyant force (through $B'$) intersects the *original* vertical line (through $B$) at a point $M$, the **metacentre**. For small tilts, $M$'s position is essentially independent of $\theta$ — it depends only on the body's geometry.

## Metacentric radius

$$\boxed{BM=\frac{I_O}{V_{\rm sub}}}$$

$I_O$ — second moment of the **waterplane area** (see [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area]]) about the tilt axis; $V_{\rm sub}$ — submerged volume. Also, from the small-angle geometry of the shifted buoyancy line:

$$\boxed{BM=\frac{\bar x}{\tan\theta}}\qquad\Longrightarrow\qquad \frac{\bar x}{\tan\theta}=BM=\frac{I_O}{V_{\rm sub}}$$

## Metacentric height — the master stability formula

From the geometry $BM=BG+GM$:

$$\boxed{GM=BM-BG}\qquad\Longrightarrow\qquad\boxed{GM=\frac{I_O}{V_{\rm sub}}-BG}$$

This is the formula to use directly in numerical stability problems.

## Stability criterion

| $GM$ | Meaning | Stability |
|---|---|---|
| $GM>0$ | $M$ above $G$ | **stable** |
| $GM<0$ | $G$ above $M$ | **unstable** |
| $GM=0$ | $M=G$ | neutral |

## Restoring moment

For a small tilt $\theta$:

$$\boxed{M_R=W(GM)\sin\theta}\ \approx\ \boxed{W(GM)\theta}\quad(\sin\theta\approx\theta\text{ for small }\theta)$$

## Cross-domain: metacentric height is a stiffness, and $GM<0$ is a buckling failure

$M_R\approx W(GM)\theta$ is a **restoring-moment-proportional-to-angle** law — a rotational spring with "stiffness" $W\cdot GM$. This has the exact same mathematical shape as [[Cross-Domain Synthesis/The Universal Second-Order Linear System|The Universal Second-Order Linear System]]'s restoring force in a spring-mass system, and the stability boundary $GM=0$ is precisely the *same kind of eigenvalue crossing* as $P=P_{cr}$ in [[Strength of materials/09 Columns and Buckling/Euler Buckling of Columns|Euler Buckling of Columns]]: below the critical value the small-perturbation restoring "stiffness" is positive (stable), and at/above it, the sign flips and any small disturbance grows instead of decaying. A ship capsizing when overloaded or top-heavy ($GM$ driven negative by raising $G$) is the fluid-mechanics twin of a column buckling when it's too slender or too heavily loaded ($EI$ too small or $P$ too large relative to $L$) — both are "the restoring generalized-stiffness term in a linearized equilibrium equation has changed sign." See [[Cross-Domain Synthesis/Resonance and Buckling - Instability as an Eigenvalue Problem|Resonance and Buckling — Instability as an Eigenvalue Problem]] for the general pattern this belongs to.

## Related
- [[Fluid Mechanics/02 Fluid Statics/Buoyancy and Archimedes' Principle|Buoyancy and Archimedes' Principle]]
- [[Fluid Mechanics/05 Centroids and Centre of Mass/Second Moments of Area|Second Moments of Area]]
- [[Cross-Domain Synthesis/Resonance and Buckling - Instability as an Eigenvalue Problem|Cross-Domain: Resonance and Buckling — Instability as an Eigenvalue Problem]]

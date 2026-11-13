---
tags: [concept, fluid-mechanics, kinematics, vorticity, circulation]
status: draft
aliases: [vorticity, circulation, Stokes theorem, Rankine vortex, free vortex, forced vortex, Kelvin theorem]
up: "[[Fluid Mechanics - MOC]]"
---

# Vorticity and Circulation

← up: [[Fluid Mechanics - MOC|Fluid Mechanics MOC]] · builds on: [[Motion of a Fluid Element|Motion of a Fluid Element]] · formulas: [[Differential Mass Conservation and Fluid Kinematics - Formula Bank|Formula Bank §5]]

## Core Idea

> **One-sentence definition:** vorticity $\boldsymbol\zeta=\nabla\times\mathbf V$ is twice the local angular velocity of a fluid element, and circulation $\Gamma=\oint\mathbf V\cdot d\mathbf l$ is the "net swirl" around a closed loop, equal to the flux of vorticity through it.

**Intuition:** vorticity is a *local* measure (how fast a tiny paddle wheel would spin in the flow), circulation is the *global* version (how much the flow goes around a finite loop). They are linked by Stokes' theorem.

## Governing Relations

$$\boxed{\boldsymbol\zeta=\nabla\times\mathbf V=2\boldsymbol\omega},\qquad\zeta_z=\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}$$

$$\boxed{\Gamma=\oint_C\mathbf V\cdot d\mathbf l=\iint_A\boldsymbol\zeta\cdot\mathbf n\,dA}\ \ (\text{Stokes}),\qquad\zeta_z=\lim_{A\to0}\frac\Gamma A$$

Cylindrical: $\ \zeta_z=\dfrac1r\dfrac{\partial(rv_\theta)}{\partial r}-\dfrac1r\dfrac{\partial v_r}{\partial\theta}$.

| Vortex | $v_\theta(r)$ | $\zeta_z$ | $\Gamma(r)$ |
|---|---|---|---|
| solid-body (forced) | $\Omega r$ | $2\Omega$ (uniform) | $2\pi\Omega r^2$ |
| free (potential) | $K/r=\Gamma/2\pi r$ | $0$ for $r>0$ | $2\pi K$ for any loop **enclosing** the axis |
| Rankine | $\Omega r$ inside $R_c$, $\Omega R_c^2/r$ outside | $2\Omega$ in the core, $0$ outside | $2\pi\Omega r^2$ inside, $2\pi\Omega R_c^2$ outside |

**Kelvin's theorem** (inviscid, barotropic fluid, conservative body force): the circulation round a loop of fluid particles stays constant, $D\Gamma/Dt=0$. Consequently an inviscid flow that starts irrotational stays irrotational.

**Where:** $\zeta$ = vorticity (1/s); $\Gamma$ = circulation (m²/s); $C$ = closed curve with area $A$.

**Assumptions:** smooth field inside $C$ for Stokes' theorem (the free vortex needs separate treatment at its axis).

## Visual

![[FM-K3-vortices.png]]

**Figure:** a Rankine vortex joins a solid-body core (rotational, vorticity concentrated) to a free-vortex tail (irrotational, circulation constant). The speed peaks at the core radius.

## When To Use

- Deciding whether a flow is rotational: compute $\zeta$ ([[Rotational and Irrotational Flow|Rotational and Irrotational Flow]]).
- Tornadoes, bathtub drains, wing-tip vortices, wakes.
- Lift: the Kutta–Joukowski result $L'=\rho U\Gamma$ links lift per unit span to the circulation round a wing.

**Recognition pattern:** "swirl", "rotation of the fluid", "velocity around a closed path" → **vorticity and circulation**.

## Method

1. **Identify** the velocity field and the coordinate system.
2. **Choose** $\zeta=\nabla\times\mathbf V$ for local rotation, or the line integral $\Gamma$ for a finite loop.
3. **Apply** Stokes' theorem to convert between them: use a circular loop for axisymmetric flows.
4. **Check:** simple shear $u=\dot\gamma y$ has $\zeta=-\dot\gamma$; a free vortex has $\zeta=0$ but $\Gamma=2\pi K\ne0$ for loops around the axis.

## Derivation / Why It Works

Around a small square of sides $dx,dy$, the circulation is the sum of $\mathbf V\cdot d\mathbf l$ along the four sides: $u\,dx+(v+\partial_xv\,dx)dy-(u+\partial_yu\,dy)dx-v\,dy=(\partial_xv-\partial_yu)\,dx\,dy$. Dividing by $dx\,dy$ gives $\zeta_z$. Joining many such squares, interior edges cancel, which is Stokes' theorem.

**Generation of vorticity:** an irrotational flow becomes rotational mainly by viscous action at walls, jets and wakes (thin layers); outside those layers, low-speed flow past a body is irrotational, so the inviscid approximation works.

## Common Traps

- **Trap:** saying the free vortex has *no* circulation.
  - **Why:** vorticity vanishes everywhere except the axis, but $\Gamma=2\pi K$ for any loop that encloses it.
  - **Avoid it by:** picking loops that do or do not enclose the origin.
- **Trap:** confusing vorticity ($2\omega$) with angular velocity ($\omega$).
- **Trap:** assuming curved streamlines mean rotational flow (the free vortex is curved and irrotational).
- **Trap:** sign of circulation: counter-clockwise positive.

## Example

### Given
A tornado-like Rankine vortex with core radius $R_c=0.5$ m and core angular velocity $\Omega=10$ rad/s.

### Solution
$$v_{\max}=\Omega R_c=5\ \text{m/s},\qquad\zeta_{\rm core}=2\Omega=20\ \text{s}^{-1},$$
$$\Gamma=2\pi\Omega R_c^2=2\pi(10)(0.25)=15.7\ \text{m}^2/\text{s},\qquad v_\theta(2\ \text{m})=\frac{\Gamma}{2\pi(2)}=1.25\ \text{m/s}.$$

**Answer:** peak 5 m/s at the core edge; 1.25 m/s at $r=2$ m; $\Gamma=15.7$ m²/s.
**Key takeaway:** outside the core the flow is irrotational (zero vorticity) but still carries all the circulation the core produced.

## Connections

### Prerequisites
- [[Motion of a Fluid Element|Motion of a Fluid Element]]
- [[Differential Continuity Equation|Differential Continuity Equation]]

### Related Concepts
- [[Rotational and Irrotational Flow|Rotational and Irrotational Flow]]
- [[Bernoulli Equation|Bernoulli Equation]] — across streamlines only if irrotational.
- [[Euler's Equations of Fluid Motion|Euler's Equations]] — the identity $(\mathbf V\cdot\nabla)\mathbf V=\nabla(V^2/2)-\mathbf V\times\boldsymbol\zeta$.

### Next
- [[Rotational and Irrotational Flow|Rotational and Irrotational Flow]], [[Euler's Equations of Fluid Motion|Euler's Equations]]

### Cross-domain links
- [[Eigenvalues, Rotation and Diagonalization Everywhere|Eigenvalues, Rotation and Diagonalization Everywhere]] — vorticity is the antisymmetric part of $\nabla\mathbf V$, the rotation generator.
- [[Cross-Domain Synthesis - MOC|Cross-Domain Synthesis]] — Stokes' theorem $\oint\mathbf V\cdot d\mathbf l=\iint\boldsymbol\zeta\cdot\mathbf n\,dA$ is the same theorem as Ampère's law in electromagnetism: the free vortex $v_\theta=\Gamma/2\pi r$ has the same form as the magnetic field around a straight current-carrying wire, with circulation playing the role of the enclosed current.

## Quick Recall

> **In one line:** $\zeta=\nabla\times\mathbf V=2\omega$, $\Gamma=\oint\mathbf V\cdot d\mathbf l=\iint\zeta\,dA$.

**Formula / trigger:** $$\zeta_z=v_x-u_y,\qquad\Gamma=\oint\mathbf V\cdot d\mathbf l$$

**Remember:** shear flow has vorticity; the free vortex has circulation without vorticity.

## Metadata
- **Status:** draft
- **Type:** concept
- **Difficulty:** intermediate
- **Subjects:** [[Fluid Mechanics - MOC]]

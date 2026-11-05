---
tags: [concept, KDoM]
course: "ME 2201 Kinematics & Dynamics of Machinery"
aliases: [Rotor balancing, Two-plane balancing, Dynamic balancing]
---

# Balancing of Rotors — Static and Dynamic

> [!abstract] In one breath
> A rotating mass $m$ at radius $r$ pulls the shaft with $m r\omega^2$ in a direction that spins with it. A rotor is balanced when **the vector sum of all $m\,r$ is zero (no net force) and the vector sum of all $m\,r\,z$ about any point is zero (no net couple)**. Any pile of unbalance can be replaced by an equivalent pair, one in each of two chosen planes.

Part of [[KDoMs - MOC]]. Solved in [[Tutorial-10-solution]].

## 1. Conditions

For masses $m_i$ at radius $r_i$, angle $\theta_i$, axial position $z_i$:

$$
\sum m_i r_i e^{j\theta_i}=0\quad(\text{force: static balance}),\qquad
\sum m_i r_i z_i\,e^{j\theta_i}=0\quad(\text{couple: dynamic balance})
$$

- Static balance alone (centre of mass on the axis) can leave a **couple**: two equal masses on opposite sides at different $z$ balance on knife edges but wobble when spun.
- Both conditions are needed. Rotating unbalance force is $\sum m r\omega^2$, a rotating couple is $\omega^2\sum m r z$.

## 2. The two-plane replacement

Choose two planes $P$ and $Q$ (say $z=0$ and $z=L$). A mass system of unbalance $\mathbf U_i=m_ir_ie^{j\theta_i}$ at $z_i$ is equivalent in force and couple to $\mathbf U_P$ and $\mathbf U_Q$ with

$$
\mathbf U_P+\mathbf U_Q=\sum\mathbf U_i,\qquad
\mathbf U_Q\,L=\sum\mathbf U_i\,z_i
\;\Rightarrow\;
\mathbf U_Q=\frac1L\sum\mathbf U_iz_i,\quad \mathbf U_P=\sum\mathbf U_i-\mathbf U_Q
$$

Then $m=|\mathbf U|/r$ at that plane's radius, at angle $\arg\mathbf U$. This is how a correction is moved from an inaccessible plane to one you can reach.

> [!tip] Add or remove?
> Adding mass $m$ at angle $\theta$ is the same as removing mass $m$ at $\theta+180^\circ$. A rotor with trial masses attached that runs smooth has unbalance $-(\text{trial})$ without them. To balance it, fit the *equivalent of the trial masses* in the new planes, or take the same amount **off the opposite side**.

## 3. Method on paper

1. Draw the end view with angles from a single reference; write each $m r$.
2. Take moments about one plane; close the **couple polygon** (vectors $m\,r\,z$) to get the other plane's vector.
3. Close the **force polygon** for the first plane.
4. Convert vectors to mass and angle; state the angle convention and whether it is added or removed.

## 4. Traps and checks

> [!warning] Traps
> - Signs of $z$: planes on either side of the reference have opposite sign.
> - Mixing radii: a vector is $m\,r$, so a 10 cm plane needs $|\mathbf U|/10$, not $|\mathbf U|/15$.
> - Angle sense: say "clockwise from $A_1$" or "anticlockwise from the $x$ axis" and stay with it.
> - Reporting the added position when the question asks for material **removed** (or the reverse).

> [!question]- Check: how do you know the answer is right?
> Re-sum the final system: force and couple polygons must close. Also the two-plane method must give the same answer whichever plane you take moments about.

## 5. Connections

- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]] — unbalance vectors add like phasors, and a closed polygon is a zero sum.
- [[Vibration of Particles and Rigid Bodies]] — unbalance is the forcing term of a rotating-unbalance vibration; the response peaks at the critical speed.
- [[Mass Moments of Inertia]] — a rotor's principal axis misaligned with the shaft is the same couple unbalance, seen through the inertia tensor's products.

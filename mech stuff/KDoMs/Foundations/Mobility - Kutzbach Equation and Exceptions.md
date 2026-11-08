---
tags: [concept, KDoM]
course: "ME 2201 Kinematics & Dynamics of Machinery"
aliases: [Kutzbach equation, Grubler equation, Mobility, Degrees of freedom of a mechanism]
---

# Mobility — Kutzbach Equation and Exceptions

> [!abstract] In one breath
> Start with every link free (3 DOF each in the plane), pin the frame down, and let each joint remove the DOF it blocks: **$M=3(n-1)-2j-h$**. $M=1$ means one input drives the whole mechanism. The formula counts constraints, so it is wrong exactly when constraints repeat (redundant links) or a link can move without affecting anything (idle motion).

Part of [[KDoMs - MOC]]. Previous: [[Kinematic Pairs, Links and Chains]]. Next: [[Grashof Criterion and Four-Bar Inversions]].

## 1. The equation

$n$ = number of links **including the frame**, $j$ = full joints (R, P: 2 DOF removed each), $h$ = half joints (higher pairs: 1 removed).

$$
M=3(n-1)-2j-h\quad\text{(Kutzbach)},\qquad M=3(n-1)-2j\quad\text{(Grübler, no higher pairs)}
$$

- $3(n-1)$: the $n-1$ moving links, each free in the plane.
- A joint of $k$ links counts as $k-1$ joints.

## 2. Worked examples

![[FND-2-mobility.png]]

| Mechanism | $n$ | $j$ | $h$ | $M$ |
| --- | --- | --- | --- | --- |
| Four-bar (4R) | 4 | 4 | 0 | **1** |
| Slider-crank | 4 | 4 (3R + 1P) | 0 | **1** |
| Cam with a roller follower | 4 | 3 | 1 | **2** (one is the idle roller spin) |
| Eight-link chain with a sliding joint (lecture 3) | 8 | 10 | 0 | **1** |
| Seven-link chain with one cam pair (lecture 3) | 7 | 7 | 1 | **3** |
| Eight-link chain with multiple joints (lecture 5) | 8 | 9 | 0 | **3** |

All numbers are recomputed in `found_core.py`.

## 3. Exceptions and the corrected form

**Idle (redundant) DOF.** A roller on a cam follower can spin without moving anything else. Subtract it: $M_e=3(n-1)-2j-h-M_r$, with $M_r$ the number of idle DOF. Cam and roller: $M=3(3)-2(3)-1=2$, $M_e=2-1=1$ ✓.

**Redundant links and joints.** Three equal cranks sharing a coupler (the parallelogram): $n=5$, $j=6$ gives $M=3(4)-12=0$, yet it moves, because one crank adds a constraint that the geometry already satisfies. Remove the redundant link ($n_r=1$) and the two joints it brings ($j_r=2$):

$$
M_e=3(n-n_r-1)-2(j-j_r)-h-M_r=3(5-1-1)-2(6-2)=1
$$

**Special geometry** (equal links, parallel axes) can give motion where the count says there is none. It is a property of the dimensions, not of $n$ and $j$, so no counting formula catches it. Such mechanisms are also fragile: a small error in link length locks them (the parallelogram jams if one crank is a hair off).

> [!warning] Traps
> - Forgetting that $n$ **includes the frame**.
> - Counting a pin shared by three links as one joint: it is two.
> - Trusting $M=0$ on a mechanism that obviously moves: look for a repeated constraint.
> - Counting the roller's own spin as useful motion.

## 4. Which chains can be constrained?

A closed linkage of $n$ links and $j$ lower pairs with $M=1$ needs

$$
1=3(n-1)-2j\ \Longrightarrow\ 3n=2j+4
$$

Since the right side is even, **$n$ must be even**.

| $n$ | $j$ | example |
| --- | --- | --- |
| 2 | 1 | open chain: a single hinge |
| 4 | 4 | four-bar, slider-crank |
| 6 | 7 | Watt and Stephenson six-bars |
| 8 | 10 | eight-bar chains |

Six-bar chains come in two topologies, Watt's (two ternary links adjacent) and Stephenson's (two ternary links separated).

> [!question]- Predict first: can a three-link closed chain be a mechanism?
> $n=3$ gives $3n=9=2j+4$, so $j=2.5$: impossible. Three links in a triangle with three pins have $M=3(2)-6=0$: a rigid truss, which is why a truss is a structure and not a mechanism.

> [!question]- A pin joint connects four links. How many joints does it count as?
> Three. A joint of $k$ links is $k-1$ joints.

## 5. Connections

- [[Kinematic Pairs, Links and Chains]] — which pairs count as full or half joints.
- [[Plane Trusses - Method of Joints and Sections]] — the same count in a structure. A determinate truss has $m+3=2k$ (members, joints); a square with a diagonal has $5+3=2\cdot4$. Take the diagonal away and the same four pins give the four-bar, $M=1$.
- [[Free-Body Diagrams and Equilibrium of Rigid Bodies]] — each removed DOF is one reaction component.

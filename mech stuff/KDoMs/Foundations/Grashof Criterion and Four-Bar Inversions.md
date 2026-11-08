---
tags: [concept, KDoM]
course: "ME 2201 Kinematics & Dynamics of Machinery"
aliases: [Grashof criterion, Grashof condition, Four-bar inversions, Crank-rocker, Double rocker, Drag link]
---

# Grashof Criterion and Four-Bar Inversions

> [!abstract] In one breath
> In a four-bar chain, call the shortest link $s$, the longest $l$, and the other two $p$ and $q$. **If $s+l\le p+q$, at least one link can turn a full circle relative to the others. Which mechanism you get then depends only on which link you fix.** If $s+l>p+q$ nothing turns fully: a triple rocker.

Part of [[KDoMs - MOC]]. Previous: [[Mobility - Kutzbach Equation and Exceptions]]. Next: [[Kinematic Inversion - Slider-Crank and Double-Slider Families]]. Solved with it: [[Tutorial-6-solution]] (Grashof check on a designed linkage).

## 1. The rule and why it works

A closed chain of four links needs the three "free" sides to be able to close into a triangle at every position. Look at the two extreme positions of the shortest link $s$, where $s$ lies along the longest $l$: stretched out (length $l+s$) or folded back (length $l-s$). The remaining links $p$ and $q$ must still close the loop:

$$
\text{stretched: } l+s\le p+q,\qquad\text{folded: } p\le q+(l-s)\ \text{and}\ q\le p+(l-s)
$$

Because $s$ is the smallest link and $l$ the largest, the folded conditions hold automatically (they reduce to $s+p\le l+q$ and $s+q\le l+p$). What remains is the **Grashof condition**

$$
\boxed{s+l\le p+q}
$$

with equality the **change point**: the chain can fold flat and the motion becomes ambiguous.

> [!tip] Check it numerically
> For random link sets (borderline ones removed) I let the shortest link be the crank and tried to assemble the loop at 720 angles. The result agrees with the rule in every case: 587 of 587 sets in the shipped run, and 3920 of 3920 in a 4000-set run (`found_core.py`).

![[FND-4-grashof-map.png]]

Only the sum $p+q$ matters, not how it splits: the boundary is a straight line in the $(p,q)$ plane.

## 2. Which link you fix: the four inversions

Fixing a different link of the same chain gives a different mechanism with the **same relative motion between links**. For a Grashof chain:

| Fixed link | Mechanism | What turns fully |
| --- | --- | --- |
| Next to $s$ (either neighbour) | **crank-rocker** | $s$ is the crank; the opposite-side link rocks |
| $s$ itself | **drag link** (double crank) | both links next to the frame |
| Opposite $s$ | **double rocker** (coupler turns fully) | only the coupler |
| any, but $s+l>p+q$ | **triple rocker** | nothing |

![[FND-3-inversions-4R.png]]

Chain $s=2$, $p=4$, $q=4.5$, $l=5$ ($s+l=7<8.5$): fixing $q$ or $p$ gives a crank-rocker; fixing $s$ a drag link; fixing $l$ a double rocker.

## 3. Watch it fail

![[FND-6-grashof-sweep.png]]

Same frame ($4.5$), coupler ($5$) and follower ($4$), only the crank grows. At $2.0$ the crank turns fully and the coupler midpoint draws a closed curve. At $3.5$ ($s+l=p+q$) it only just makes it, with a fold. At $3.8$ the chain jams at two limit positions, so the crank rocks.

## 4. Slider-crank as a four-bar

A slider is a revolute pair at infinity, so the slider-crank is a four-bar whose follower $q\to\infty$. Take the crank as $s$, the connecting rod as $p$ and let the line of the slider be offset by $e$. Then $l-q\to e$ and $s+l\le p+q$ becomes

$$
r+e\le \ell\qquad(\text{crank } r,\ \text{rod }\ell,\ \text{offset }e)
$$

For an in-line slider-crank ($e=0$) this is simply "crank shorter than the rod". The same reading applies to the other slider chains.

## 5. Explorer

Move the four lengths until the readout changes class; change the assembly (open or crossed) to see the other branch.

> [!question]- Predict first: ground link 6, crank 2, coupler 5, follower 4. Which mechanism?
> $s=2,\ l=6,\ p+q=9$: $s+l=8<9$, Grashof. The shortest link is the crank, which is next to the ground, so it is a **crank-rocker**.

> [!question]- If $s+l<p+q$ but you fix the longest link, can any link make a full turn?
> Yes: the links next to the fixed $l$ cannot, but the **opposite** link $s$ is the coupler and it does turn fully (relative to both neighbours). The double rocker's two moving links next to the frame only rock.

## 6. Exam pattern

| Question says | Do |
| --- | --- |
| "Will the crank rotate fully?" | Sort the lengths, test $s+l\le p+q$, then check that the crank is $s$ or next to it with $s$ fixed. |
| "Name the mechanism" | Grashof test, then ask which link is fixed relative to $s$. |
| Slider-crank | Use $r+e\le\ell$. |
| Design a crank-rocker | Make the crank the shortest link and the frame next to it, then verify the sum. |

## 7. Connections

- [[Mobility - Kutzbach Equation and Exceptions]] — a four-bar has $M=1$; Grashof says *which* link can use that freedom for a full turn.
- [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]] — a four-bar closes when four rotating vectors sum to zero. The Grashof inequality is the triangle inequality on those vectors.
- [[Resonance and Buckling - Instability as an Eigenvalue Problem]] — both are threshold conditions on parameters that change the behaviour qualitatively.

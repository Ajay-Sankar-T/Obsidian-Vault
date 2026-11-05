---
tags: [concept, engineering-mechanics, AM1100, statics, trusses, structures]
status: draft
up: "[[Engineering Mechanics - MOC]]"
aliases: [plane truss, method of joints, method of sections, zero-force members, tension and compression, simple truss]
---

# Plane Trusses - Method of Joints and Sections

> [!abstract] The big idea
> A **truss** is a framework of slender bars joined at pins and loaded **only at the joints**. Then every bar is a two-force member carrying pure tension or compression along its axis, and a whole bridge reduces to a set of simple equilibrium problems, one for each joint (**method of joints**) or one cut through the truss (**method of sections**).

## Counting and sign convention

For $m$ members, $j$ joints and $r$ reactions, a plane truss is **statically determinate** if $m+r=2j$ (two equations per joint). Sign convention: **tension positive** (the bar pulls on its joints), **compression negative** (it pushes). A simple truss is built by adding two bars for each new joint, starting from a triangle.

## Method of joints
Isolate a joint; its FBD has concurrent forces, so only $\sum F_x=0,\ \sum F_y=0$: **two unknowns per joint**. Start where at most two bars are unknown and march along the truss.

## Method of sections
Cut the truss into two pieces through (at most) three unknown bars; apply the three equilibrium equations to **one piece**. Choose a moment point where two of the cut bars intersect, so one equation gives one force directly. It is the fast way to find a single bar deep inside a big truss.

## Zero-force members
- Two bars meeting at a joint, no load, not collinear: both carry zero force.
- Three bars at an unloaded joint, two of them collinear: the third carries zero force.
They are not useless: they brace against buckling or carry load if the loading changes.

![[EM-truss.png]]

**Figure:** A five-joint truss (span $8$ m, height $3$ m) with $10$ kN at each upper joint, solved by writing the 10 joint equations at once. Top chord DE is in compression ($-6.67$ kN), the bottom chord is in tension ($+6.67$ kN), the end diagonals AD and EC carry $-12.02$ kN, and the two inner diagonals DB and BE are **zero-force members**: at the unloaded joint B symmetry makes $F_{DB}=F_{BE}$, while vertical equilibrium needs $F_{DB}=-F_{BE}$, so both must be $0$.

> [!question]- 🎯 Predict first: for a symmetric truss with symmetric loads, how do the two reactions compare, and which diagonals carry load?
> Equal reactions ($10$ kN each here: half the total $20$ kN). The diagonals that slope *towards the load* near the supports are in compression and carry most of it; the inner pair, whose joint has equal and opposite horizontal chord forces, sit idle. Symmetry halves the work: solve one half.

## Method
1. **Check determinacy** ($m+r=2j$); find the reactions from overall equilibrium.
2. **Look for zero-force members** and discard them.
3. **Joint by joint**, starting at a pin with two unknowns; resolve each bar's force into components using its slope.
4. **Sections for a single bar:** cut through it with at most two other unknown bars, take moments where those two meet.
5. **Check** with a joint you did not use (it must balance).

## Worked example
> [!example]- 🔬 Triangular truss: A pin, B roller, span $6$ m, apex C $4$ m high, $10$ kN down at C
> Reactions: $R_A=R_B=5$ kN (symmetry). Member length $AC=BC=5$ m, so $\sin\theta=4/5$, $\cos\theta=3/5$.
> **Joint A:** vertical: $F_{AC}\sin\theta+5=0\Rightarrow F_{AC}=-6.25$ kN (compression). Horizontal: $F_{AB}+F_{AC}\cos\theta=0\Rightarrow F_{AB}=+3.75$ kN (tension).
> **Check at C:** the two inclined bars each push up by $6.25\times0.8=5$ kN, total $10$ kN balancing the load ✓.

> [!warning]- ⚠️ Assuming every bar is in tension and not flipping the arrow after a negative answer
> A negative value means compression; the next joint must use the **actual** direction of that force on *its* pin (equal and opposite).

> [!danger]- 💥 Loads between joints
> If a load acts on a bar, that bar is no longer a two-force member and bends (a beam-column). Truss theory needs joint loads: transfer a mid-bar load to the joints first.

## Quick quiz
> [!question]- Q1. A truss has $11$ members and $7$ joints with three support reactions. Determinate?
> $m+r=14=2j$: yes.

> [!question]- Q2. Compression members are thicker than tension members of the same force. Why?
> Compression bars can **buckle** (see [[Euler Buckling of Columns]]); tension bars cannot. The design load for a long compression bar is $P_{cr}$, not just stress.

## Connections
- **Prerequisites:** [[Free-Body Diagrams and Equilibrium of Rigid Bodies]]
- **Next:** [[Frames and Machines]]
- **Cross-domain:** [[Euler Buckling of Columns]] and [[Lab - Buckling of Struts]] (why compression members are sized differently); [[Strain Energy and Castigliano's Theorem]] (deflection of a truss by energy methods); [[Conservation Laws and Flow Networks]] (joint equilibrium is Kirchhoff's current law for forces).

## Self-check
- [ ] I can test determinacy and find reactions.
- [ ] I can solve a joint and a section, with correct tension/compression signs.
- [ ] I can spot zero-force members.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** intermediate
- **Course map:** [[Engineering Mechanics - MOC]]

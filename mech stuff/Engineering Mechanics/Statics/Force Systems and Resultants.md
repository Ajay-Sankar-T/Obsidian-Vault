---
tags: [concept, engineering-mechanics, AM1100, statics, forces, vectors]
status: draft
up: "[[Engineering Mechanics - MOC]]"
aliases: [force systems, resultant of forces, rectangular components, direction cosines, vector addition of forces]
---

# Force Systems and Resultants

> [!abstract] The big idea
> A **force** is a vector (magnitude, direction, and a line of action). Statics starts by replacing a pile of forces by the single **resultant** that has the same effect, using one trick: *break everything into components, add the components, rebuild the vector.* In 3-D the same trick uses three components and three **direction cosines**.

## Components and the resultant

For forces $\mathbf F_i$ with components $(F_{ix},F_{iy})$:
$$R_x=\sum F_{ix},\quad R_y=\sum F_{iy},\quad R=\sqrt{R_x^2+R_y^2},\quad\theta=\tan^{-1}\frac{R_y}{R_x}.$$
In 3-D, $F=\sqrt{F_x^2+F_y^2+F_z^2}$ and the direction cosines $l=F_x/F,\ m=F_y/F,\ n=F_z/F$ satisfy $l^2+m^2+n^2=1$. The components are $F_x=Fl$, etc.

![[EM-force-system.png]]

**Figure:** Left, two forces ($200$ N at $30^\circ$ and $300$ N at $120^\circ$) add to $R=361$ N at $86.3^\circ$; the dashed parallelogram is the graphical check. Right, a 3-D force $(300,-200,400)$ N has $F=538.5$ N and direction cosines $0.557,-0.371,0.743$ whose squares sum to $1$.

> [!question]- 🎯 Predict first: two forces of 100 N act at 90° to each other. Is the resultant 200 N, 141 N or 100 N?
> **141 N** ($\sqrt{100^2+100^2}$), at $45^\circ$ between them. Forces add as vectors, so only parallel forces add as plain numbers (200 N), and opposite ones cancel (0 N). The resultant of two forces always lies between $|F_1-F_2|$ and $F_1+F_2$.

## Method
1. **Pick axes** (aligned with the geometry, e.g. along an incline).
2. **Resolve each force** into $x,y(,z)$ components with the correct signs.
3. **Sum** to $R_x,R_y(,R_z)$.
4. **Rebuild** $R$ and its angle (check the quadrant from the *signs* of $R_x,R_y$, not just the arctan).
5. **Check** with a sketch: does $\mathbf R$ point where the force polygon says?

```mermaid
flowchart LR
    A["list the forces"] --> B["resolve each into components"]
    B --> C["sum the components: Rx, Ry, Rz"]
    C --> D["R = sqrt(sum squares), direction from the signs"]
    D --> E["sketch check"]
```

## Worked example
> [!example]- 🔬 Resultant of $\mathbf F_1=200$ N at $30^\circ$ and $\mathbf F_2=300$ N at $120^\circ$
> $\mathbf F_1=(173.2,\,100)$, $\mathbf F_2=(-150,\,259.8)$. Sum: $\mathbf R=(23.2,\,359.8)$ N.
> $R=\sqrt{23.2^2+359.8^2}=360.6$ N, $\theta=\tan^{-1}(359.8/23.2)=86.3^\circ$ from $+x$.
> **Check:** the two forces are almost opposite in $x$, so $R_x$ is small; and $R^2=F_1^2+F_2^2+2F_1F_2\cos90^\circ=130{,}000$, $R=360.6$ ✓.

> [!warning]- ⚠️ Using $\tan^{-1}$ without checking the quadrant
> $\tan^{-1}(R_y/R_x)$ cannot tell $(+,+)$ from $(-,-)$. Use $\text{atan2}$ or read the signs of the components.

> [!danger]- 💥 Adding magnitudes
> $F_1+F_2$ only works for forces along the same line. For anything else you must add components.

## Quick quiz
> [!question]- Q1. A 500 N force makes direction angles $60^\circ,\ 45^\circ$ with $x,y$. Find its $z$-component.
> $l=\cos60^\circ=0.5$, $m=\cos45^\circ=0.707$, so $n^2=1-0.25-0.5=0.25$ and $n=\pm0.5$. $F_z=\pm250$ N (two possible directions: the angles alone do not fix the sign).

> [!question]- Q2. Can three forces of 10 N, 10 N and 10 N have zero resultant?
> Yes, if they are at $120^\circ$ to each other: their components cancel pairwise.

## Connections
- **Prerequisites:** [[Vectors - Dot and Cross Products]], [[Rotation Matrix and Vector Transformation]] (resolving along rotated axes).
- **Next:** [[Moments, Couples and Equivalent Force Systems]]
- **Cross-domain:** [[Newton's Laws as Differential Equations]] (net force); [[Conservative Forces, Gradient and Curl]] (forces as fields).

## Self-check
- [ ] I can resolve and add forces in 2-D and 3-D.
- [ ] I can compute direction cosines and check $l^2+m^2+n^2=1$.
- [ ] I can find the resultant's quadrant correctly.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** beginner
- **Course map:** [[Engineering Mechanics - MOC]]

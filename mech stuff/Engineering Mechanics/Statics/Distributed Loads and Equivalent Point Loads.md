---
tags: [concept, engineering-mechanics, AM1100, statics, distributed-loads, centroid]
status: draft
up: "[[Engineering Mechanics - MOC]]"
aliases: [distributed loads, equivalent point load, load intensity, triangular load, centroid of load diagram]
---

# Distributed Loads and Equivalent Point Loads

> [!abstract] The big idea
> Real loads (snow on a roof, water on a dam, a book on a shelf) are spread over a length, area or volume. For *external* equilibrium you may replace a distributed load by a single force: **its magnitude is the area under the load diagram and it acts through the centroid of that area.** The result is only valid for finding reactions: the stresses inside the beam still depend on the actual distribution.

## The rule

For a line load $w(x)$ (force per length) on $a\le x\le b$:
$$R=\int_a^bw(x)\,dx\quad(\text{area of the load diagram}),\qquad\bar x=\frac{\int_a^bx\,w(x)\,dx}{\int_a^bw(x)\,dx}\quad(\text{centroid of that area}).$$

![[EM-distributed.png]]

**Figure:** Three common loads on a $6$ m span. Uniform: $R=30$ kN at mid-span. Triangular $0\to9$ kN/m: $R=27$ kN at $4$ m from the zero end (**two-thirds of the way** towards the big end). Trapezoid $3\to9$ kN/m: $R=36$ kN at $3.5$ m from the lighter end.

| Load diagram | Magnitude | Acts at |
|---|---|---|
| Rectangle, intensity $w$, length $L$ | $wL$ | $L/2$ |
| Triangle, peak $w$, length $L$ | $\tfrac12wL$ | $\tfrac23L$ from the zero end ($\tfrac13L$ from the peak end) |
| Trapezoid, ends $w_1,w_2$ | $\tfrac12(w_1+w_2)L$ | $\dfrac{L(w_1+2w_2)}{3(w_1+w_2)}$ from the $w_1$ end |

For composite diagrams split into rectangles and triangles; the centroid rules are in [[Centre of Mass and Centroids]] and [[Composite Bodies and Cutouts]].

> [!question]- 🎯 Predict first: a triangular load is largest at the right end. Which support carries more, and by how much?
> The right support. With $R=27$ kN at $4$ m from the left (zero) end of a $6$ m beam: $R_{\rm right}=27(4)/6=18$ kN and $R_{\rm left}=9$ kN. The right one carries **twice** as much.

## Method
1. **Draw the load diagram** and split it into rectangles and triangles.
2. **Compute each area** (the equivalent force) and **each centroid** (its line of action).
3. **Treat these as point loads** in the equilibrium equations for the reactions.
4. **Remember** to go back to the real distribution when you need shear and moment *inside* the member ([[Relations Between Load, Shear, and Moment]]).

## Worked example
> [!example]- 🔬 Simply supported $6$ m beam carrying the triangular load $0\to9$ kN/m (zero at A)
> $R=\tfrac12(9)(6)=27$ kN at $\bar x=4$ m from A. $\sum M_A=0$: $R_B(6)=27(4)\Rightarrow R_B=18$ kN; $R_A=27-18=9$ kN.
> **Check:** moments about B with the equivalent load $2$ m from B: $R_A(6)=27(2)=54\Rightarrow R_A=9$ ✓.
> Peak bending moment (inside) is where shear is zero: $V(x)=9-\tfrac{x^2}{4}=0$ at $x=6/\sqrt3=3.46$ m; this uses the *actual* distribution, not the point load.

> [!warning]- ⚠️ Putting the equivalent load at the middle of a triangle
> It acts at the **centroid of the load diagram**, two-thirds from the zero end, not at mid-span. This error alone moves a reaction by 33%.

> [!danger]- 💥 Using the equivalent point load for internal forces
> Cutting the beam at $x$ and using the *full* point load gives the wrong shear and moment. Replace only the part of the load on the piece you keep.

## Quick quiz
> [!question]- Q1. A uniform load $4$ kN/m acts over $3$ m of a $10$ m beam, starting $2$ m from the left end. What is the equivalent force and its position?
> $R=12$ kN at $2+1.5=3.5$ m from the left end.

> [!question]- Q2. What is the hydrostatic force on a vertical dam wall of height $H$ and width $b$ in water?
> The load diagram is a triangle (pressure $0\to\rho gH$): $R=\tfrac12\rho gH^2b$ at $H/3$ above the base ([[Hydrostatic Force on Plane Surfaces and Centre of Pressure]]).

## Connections
- **Prerequisites:** [[Free-Body Diagrams and Equilibrium of Rigid Bodies]]
- **Cross-domain:** [[Hydrostatic Force on Plane Surfaces and Centre of Pressure]] (the same triangle rule), [[Shear Force and Bending Moment Diagrams]], [[Centre of Mass and Centroids]]
- **Next:** [[Dry Friction]]

## Self-check
- [ ] I can find the magnitude and line of action of uniform, triangular and trapezoidal loads.
- [ ] I can compute the reactions with an equivalent point load.
- [ ] I know why it cannot be used for internal forces.

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** beginner–intermediate
- **Course map:** [[Engineering Mechanics - MOC]]

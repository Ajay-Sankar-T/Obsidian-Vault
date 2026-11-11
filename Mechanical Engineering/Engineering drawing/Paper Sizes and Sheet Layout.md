---
tags: [concept, engineering-drawing, ME1480, drawing-standards, paper-size]
status: draft
up: "[[Engineering Drawing - MOC]]"
aliases: [A series paper, ISO 216, sheet layout, title block, border and grid, drawing sheet]
---

# Paper Sizes and Sheet Layout

> [!abstract] The big idea
> Drawing sheets come in the **A series**: each size is half the area of the previous one with the *same shape*. That works only if the length-to-width ratio is $\sqrt2:1$. A standard sheet also has a fixed anatomy: border, grid reference, and a title block that says what the drawing is.

## The A series

A0 has area $1\ \mathrm{m^2}$ and ratio $\sqrt2:1$, so $L\times W=1189\times841$ mm ($1.189\times0.841=0.9999\ \mathrm{m^2}$). Folding a sheet across its long side halves the area and keeps the ratio, so the length of each smaller size equals the width of the previous one (A1's length $841$ is A0's width).

![[ED-a-series.png]]

**Figure:** The six sizes nested in one corner. All their top-right corners lie on one diagonal, which is the visual proof that every sheet has the same shape.

| Size | Width (mm) | Length (mm) | Area (m²) |
|---|---|---|---|
| A0 | 841 | 1189 | 1 |
| A1 | 594 | 841 | 0.5 |
| A2 | 420 | 594 | 0.25 |
| A3 | 297 | 420 | 0.125 |
| A4 | 210 | 297 | 0.0625 |

(ISO 216:2007 governs the sizes.) A4 is the usual paper, A3 the common drawing sheet in this course.

> [!question]- 🎯 Predict first: why $\sqrt2$? What property of a rectangle makes "fold in half, same shape" possible?
> Folding a $L\times W$ sheet gives $W\times L/2$. It is similar to the original when $L/W=W/(L/2)$, i.e. $L^2=2W^2$: $L/W=\sqrt2$. That is the only ratio with the property, and $1189/841=1.4138\approx\sqrt2=1.4142$.

## Sheet layout (BIS SP 46:2003)

![[ED-sheet-layout.png]]

**Figure:** Schematic A3 sheet. The **border** frames the drawing area. The **grid reference** along the edges (letters one way, numbers the other) lets you say "see zone C-4" on a large sheet; its division length is **25–75 mm** depending on complexity, and the **number of divisions must be even**. The **title block** sits at the bottom right.

**Title block contents** (for this course): the student's name, the date of the exercise, the projection symbol ([[Projection Symbol and First-Angle Projection]]), the scale ([[Drawing Scales]]), the title and the drawing number.

## Worked example
> [!example]- 🔬 How many A4 sheets cover an A0 sheet?
> Each step down halves the area: A0 = 2 × A1 = 4 × A2 = 8 × A3 = **16 × A4**. Check by area: $1\ \mathrm{m^2}/0.0625\ \mathrm{m^2}=16$ ✓.
> **Grid:** for an A3 drawing area of about $396\times273$ mm, $8$ columns of $49.5$ mm and $6$ rows of $45.5$ mm are inside the allowed $25$–$75$ mm range and even in number ✓.

> [!warning]- ⚠️ Giving the length first
> Widths and lengths are quoted in different orders in different books ($841\times1189$ vs $1189\times841$). In the table above the first number is the *shorter* side.

## Self-check
- [ ] I can derive $\sqrt2:1$ and list the sheet sizes A0–A4.
- [ ] I can describe a standard sheet's anatomy and the grid rules.
- [ ] I know what goes in the title block.

## Connections
- **Previous:** [[Purpose of Engineering Drawing]] · **Next:** [[Drawing Scales]]
- **Course map:** [[Engineering Drawing - MOC]]

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** beginner
- **Course map:** [[Engineering Drawing - MOC]]

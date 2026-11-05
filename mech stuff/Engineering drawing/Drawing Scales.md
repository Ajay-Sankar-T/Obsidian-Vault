---
tags: [concept, engineering-drawing, ME1480, drawing-standards, scale]
status: draft
up: "[[Engineering Drawing - MOC]]"
aliases: [drawing scale, scale factor, enlargement scale, reduction scale, true size]
---

# Drawing Scales

> [!abstract] The big idea
> A part may be too large (a ship) or too small (a watch gear) to draw at actual size. A **scale** is the ratio of the length *in the drawing* to the real length. The crucial rule: the **dimension numbers always give the true size**, never the drawn size, so changing the scale changes the picture but not a single number.

## Definition and notation

$$\text{scale}=\frac{\text{size in the drawing}}{\text{actual size}}$$

| Written | Meaning | Type |
|---|---|---|
| **SCALE 1:1** | drawn full size | actual size |
| **SCALE X:1** ($X>1$) | drawn $X$ times larger | enlargement |
| **SCALE 1:X** ($X>1$) | drawn $X$ times smaller | reduction |

![[ED-scales.png]]

**Figure:** The same $40\times25$ mm plate with a $\varnothing12$ hole at 2:1, 1:1 and 1:2. The drawn rectangles are $80\times50$, $40\times25$ and $20\times12.5$ mm, but every dimension line still reads $40$ and $25$.

> [!question]- 🎯 Predict first: you draw a 120 mm part at SCALE 1:2. What number goes on its length dimension, and how long is the line?
> The number is **120** (true size) and the line is **60 mm** long on paper. The only thing the scale tells the reader is how much to shrink the line to get a feel for the size; the number is the truth.

## Choosing a scale
Pick the largest standard scale that fits the part on the sheet with room for dimensions: small details get enlargement scales ($2:1$, $5:1$), big parts get reduction ($1:2$, $1:5$, $1:10$). Several views on one sheet may use different scales if each is labelled.

## Worked example
> [!example]- 🔬 The course's mural exercise
> A mural of a dog on a wall shows it $45$ ft tall; the real breed averages $3$ ft. The scale factor is $45/3=\mathbf{15:1}$, an enlargement.
> **Another:** a $0.8$ m shaft fits an A3 sheet comfortably at 1:5: it draws as $160$ mm, with the dimension $800$ still on the line.
> **Check:** drawn size = true size × scale, so $800\times\tfrac15=160$ mm ✓.

> [!warning]- ⚠️ Writing the *measured* length on the drawing
> If you scale the dimension number too, the part will be made to the wrong size. Always write the true size.

> [!danger]- 💥 Measuring a drawing to find a dimension
> Paper stretches, prints get scaled, and a drawing may have been reduced for copying. Never take sizes by measuring; use the dimension numbers.

## Self-check
- [ ] I can read SCALE 5:1 and 1:20.
- [ ] I know dimension numbers are independent of the scale.
- [ ] I can choose a scale for a given part and sheet.

## Connections
- **Previous:** [[Paper Sizes and Sheet Layout]] · **Next:** [[Lettering and Types of Lines]]
- **Course map:** [[Engineering Drawing - MOC]]

## Metadata
- **Status:** draft · **Type:** concept · **Difficulty:** beginner
- **Course map:** [[Engineering Drawing - MOC]]

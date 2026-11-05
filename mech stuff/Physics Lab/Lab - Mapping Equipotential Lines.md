---
tags: [concept, physics-lab, PH1030, electrostatics, potential, laplace, experiment]
status: draft
up: "[[Physics Laboratory I - MOC]]"
aliases: [equipotential mapping, electrolytic tank, equipotential lines, electric field mapping]
---

# Lab - Mapping Equipotential Lines

> [!abstract] The experiment in one line
> Put two electrodes in a dish of weak salt solution, apply an AC voltage, and use a probe voltmeter to find points at the same potential. Joining them draws the equipotential lines, and the field lines are the curves perpendicular to them.

## Aim and apparatus
**Aim:** map equipotential regions for two electrode configurations (concentric circles and parallel plates). **Apparatus:** a circular glass dish of KCl solution ($0.1$ g in $250$ ml distilled water), two electrode pairs, an AC supply, a multimeter on AC volts and a graph sheet under the dish. (AC avoids electrolysis and polarisation at the electrodes.)

## Theory

Potential is energy per unit charge, and only *differences* are measurable. On an equipotential the field does no work on a moving charge, so $\mathbf E=-\nabla V$ is **perpendicular to equipotentials** (see [[Conservative Forces, Gradient and Curl]]). Where there is no charge, $V$ obeys Laplace's equation, here in a conducting liquid at steady (rms) current.

**Concentric electrodes.** With circular symmetry, $\frac1\rho\frac{d}{d\rho}\big(\rho\frac{dV}{d\rho}\big)=0$, which integrates twice to $V=A\ln\rho+B$. With radii $a$ (inner) and $b$ (outer) and a total voltage $V_0$, the potential *relative to the inner electrode* is
$$V(\rho)=V_0\,\frac{\ln(\rho/a)}{\ln(b/a)},\qquad E(\rho)=\frac{V_0}{\rho\ln(b/a)}\propto\frac1\rho.$$
**Parallel plates** (spacing $d$): $V$ is linear, equipotentials are equally spaced straight lines, and $E=V_0/d$ is uniform.

![[PL-equipotential.png]]

**Figure:** Left, the circular case ($a=1$, $b=5$, $V_0=6$ in arbitrary units): equipotentials are circles crowded near the inner electrode, where the field is strongest; the red circle is the $2.5$ V line. Right, parallel plates give evenly spaced lines and a uniform field.

> [!question]- 🎯 Predict first: for concentric electrodes, is the 2.5 V line (of a 6 V total) halfway between the electrodes?
> No. Halfway in *voltage* is not halfway in *radius*: $\rho=a(b/a)^{2.5/6}$. For $a=1$, $b=5$ that is $\rho=1.955$, only about $24\%$ of the way from inner to outer radius. The logarithm squeezes equipotentials towards the inner electrode.

## Procedure (condensed)
1. Draw two concentric circles on the graph sheet with the radii of the inner electrode and of the inner edge of the outer one; place the dish on top.
2. Apply about $6$ V rms between the inner electrode (red probe) and the grounded outer ring. Set the multimeter to AC volts.
3. Dip the **black probe** (insulated except at the tip) to the bottom and move it until the meter reads $2.5$ V; copy the coordinates to your sheet.
4. Repeat at many points around the electrode, then for other voltages (e.g. $1.5$, $3.5$ V), and join each set into a smooth curve.
5. Sketch field lines perpendicular to the equipotentials.
6. Replace by the parallel-plate electrodes and repeat.

## Worked example
> [!example]- 🔬 Where is the 2.5 V line? (illustrative $a=1.0$ cm, $b=5.0$ cm, $V_0=6$ V)
> $\rho=a\,(b/a)^{V/V_0}=1.0\times5^{2.5/6}=1.96$ cm.
> The field there is $E=V_0/[\rho\ln(b/a)]=6/(0.0196\times1.609)=190$ V/m, and $373$ V/m at the inner electrode (twice as strong), $75$ V/m at the outer one (field $\propto1/\rho$).
> **Check:** $V(a)=0$ and $V(b)=V_0$ in the formula ✓; a measured $\rho$ for 2.5 V within a few percent of $1.96$ cm validates the logarithmic law.

> [!warning]- ⚠️ Probe touching the bottom or an electrode
> Contact resistance or stray current gives noisy, offset readings. Keep the probe vertical and at the same depth.

> [!danger]- 💥 Edge effects in the parallel-plate dish
> Near the ends and the dish wall the field bends (fringing). Take the central region when checking uniformity.

## Questions
> [!question]- Why AC rather than DC?
> DC drives electrolysis and polarises the electrodes, changing the field during the measurement. AC averages these effects away.

> [!question]- Why are field lines perpendicular to equipotentials?
> Along an equipotential $dV=0$, so $\mathbf E\cdot d\mathbf l=0$: $\mathbf E$ has no component along the line.

## Connections
- **Theory:** [[Conservative Forces, Gradient and Curl]] ($\mathbf E=-\nabla V$), [[Divergence Theorem and Flux]] (Gauss's law gives the $1/\rho$ field), [[Laplace Equation on Rectangles and Strips]], [[Curvilinear Coordinates - Cylindrical and Spherical]] (the Laplacian in cylindrical form).
- **Cross-domain:** [[Conservation Laws and Flow Networks]] (current flow in the liquid is the same Laplace problem as seepage or heat conduction).

## Self-check
- [ ] I can derive $V=A\ln\rho+B$ and fit the constants.
- [ ] I can explain why the 2.5 V line is not at the mid-radius.
- [ ] I can sketch field lines from equipotentials.

## Metadata
- **Status:** draft · **Type:** concept (lab) · **Difficulty:** intermediate
- **Course map:** [[Physics Laboratory I - MOC]]

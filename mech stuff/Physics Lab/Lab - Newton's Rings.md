---
tags: [concept, physics-lab, PH1030, optics, interference, thin-film, experiment]
status: draft
up: "[[Physics Laboratory I - MOC]]"
aliases: [Newton's rings, wavelength by interference, air wedge, fringes of equal thickness, sodium lamp]
---

# Lab - Newton's Rings

> [!abstract] The experiment in one line
> Rest a lens of large radius of curvature on a flat glass plate: the thin air gap between them produces concentric dark and bright rings. Measure ring diameters under a microscope, plot $D^2$ against ring number, and the slope gives the wavelength of the sodium light.

## Aim and theory
**Aim:** find the wavelength of a monochromatic source (sodium lamp, $\approx589.3$ nm) from Newton's rings. **Apparatus:** plano-convex lens of long focal length on a glass plate, a $45^\circ$ glass plate to illuminate from above, sodium lamp, traveling microscope (or the camera and ring-measuring software).

Two reflections from the air film (top surface of the film and the plate) interfere. The extra path is $2nd\cos\beta$ and one reflection (air to glass) adds a phase of $\pi$:
$$\delta=\frac{2\pi}{\lambda}\,2nd\cos\beta+\pi.$$
At near-normal incidence in air ($n=1$, $\cos\beta\approx1$) dark rings need $\delta=(2m+1)\pi$, i.e. $2d=m\lambda$. For a lens of radius of curvature $R$ the gap at radius $r$ is $d\approx r^2/2R$, so

$$\boxed{\,r_m^2=m\lambda R\ \ \Longrightarrow\ \ D_m^2=4m\lambda R,\qquad\lambda=\frac{D_m^2-D_n^2}{4(m-n)R}\,}$$

The **centre is dark** ($d=0$, only the $\pi$ phase remains). Using *differences* of ring numbers removes the unknown that the lens and plate do not touch at a perfect point. $R$ follows from the focal length: $R=(n_{\rm glass}-1)f$.

![[PL-newton-rings.png]]

**Figure:** Left, the ring pattern (dark centre; spacing shrinks outwards since $r\propto\sqrt m$). Right, $D^2$ against ring number for simulated measurements with $0.4\%$ scatter: the slope $4\lambda R=2.33$ mm² per ring gives $\lambda=583$ nm against the true $589.3$ nm (illustrative $R=1.0$ m).

> [!question]- 🎯 Predict first: are the rings equally spaced in radius?
> No. $r\propto\sqrt m$, so the rings crowd together as you move out: the first ring has $D\approx1.5$ mm, the twelfth only $5.3$ mm. It is $D^2$ (not $D$) that is **linear** in ring number, and that is why the plot uses $D^2$.

## Procedure (condensed)
1. Put the lens on the plate (a ground lower surface avoids a second reflection); set the $45^\circ$ plate above the lens centre; mount all on the microscope stage facing the sodium lamp.
2. Bring the reflected lamp image to the lens centre; focus until the dark and bright rings are sharp.
3. With the software: place the fringe pattern so the horizontal line passes through the centre; **capture**, calibrate the centre, label rings, mark the intersections of each ring with the centre line on both sides; the software returns diameters.
4. Take **at least $5$–$6$ readings for each ring**, tabulate $D_m$ and $D_m^2$.
5. Plot $D^2$ against $m$; the slope is $4\lambda R$; estimate $\lambda$ and its uncertainty; also use $(D_m^2-D_n^2)/4(m-n)R$ for pairs.

## Worked example
> [!example]- 🔬 Illustrative: $R=1.00$ m, $\lambda=589.3$ nm
> First dark ring: $D_1=2\sqrt{\lambda R}=2\sqrt{589.3\times10^{-9}\times1.00}=1.535$ mm. Slope $4\lambda R=2.357\times10^{-6}$ m² per ring $=2.357$ mm².
> If the measured slope is $2.33$ mm² per ring: $\lambda=2.33\times10^{-6}/(4\times1.00)=582$ nm, a $1.1\%$ deviation, within the scatter of the diameters.
> **Check:** $D_{12}=2\sqrt{12\lambda R}=5.32$ mm, consistent with the right-hand plot ($D_{12}^2=28.3$ mm²).

> [!warning]- ⚠️ Counting rings from the wrong centre
> The numbering can be shifted by a whole number if you miscount (and a bad centre biases $D$). The linear fit of $D^2$ vs $m$ is *insensitive to a constant offset in $m$* (it changes only the intercept), so check the *slope*, and use differences.

> [!danger]- 💥 Using the sodium D-line average as if it were one wavelength
> Sodium is a doublet ($589.0$ and $589.6$ nm). At high ring numbers the two ring systems drift out of step and the fringes blur; stay within the first $\sim$15 rings.

## Questions
> [!question]- Why is the central spot dark?
> The ray reflected at the glass–air interface has no phase change, the ray reflected at the air–glass interface gains $\pi$; at $d=0$ they are exactly out of phase.

> [!question]- Why use a lens of large focal length?
> A large $R$ makes the rings **wide** ($D^2\propto R$), so they are easy to resolve and measure accurately.

> [!question]- How would you find the refractive index of a liquid with this setup?
> Fill the gap with the liquid: $2nd=m\lambda$ so $D_m^2\to D_m^2/n$; the ring diameters shrink by $1/\sqrt n$.

## Connections
- **Theory:** interference of two reflections (compare many-beam interference in [[Lab - Transmission Grating]]).
- **Cross-domain:** [[Rotating Vectors - Phasors, Velocity Polygons and Complex Kinematics]] (adding two waves with phase $\delta$ is adding two phasors) and [[Simple Harmonic Motion]] (the same $\cos$ superposition).
- **Errors:** [[Error Analysis - Uncertainty and Propagation]] ($\sigma_\lambda$ from the fit slope and the uncertainty in $R$).

## Self-check
- [ ] I can derive $D_m^2=4m\lambda R$ and the dark centre.
- [ ] I can find $\lambda$ from the slope of $D^2$ vs $m$ and from differences.
- [ ] I can say why large $R$ and the $\pi$ phase matter.

## Metadata
- **Status:** draft · **Type:** concept (lab) · **Difficulty:** intermediate
- **Course map:** [[Physics Laboratory I - MOC]]

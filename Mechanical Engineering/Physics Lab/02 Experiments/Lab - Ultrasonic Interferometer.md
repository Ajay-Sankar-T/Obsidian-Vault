---
tags: [concept, physics-lab, PH1030, ultrasound, standing-waves, compressibility, experiment]
status: draft
up: "[[Physics Laboratory I - MOC]]"
aliases: [ultrasonic interferometer, velocity of ultrasonic waves, adiabatic compressibility, standing wave in a liquid]
---

# Lab - Ultrasonic Interferometer

> [!abstract] The experiment in one line
> A 2 MHz quartz crystal sends sound up a liquid cell to a movable reflector. Whenever the gap fits a standing wave, the crystal's current peaks; the spacing between peaks is half a wavelength, so $v=f\lambda$ and the compressibility $\beta=1/\rho v^2$ follow.

## Aim and theory
**Aim:** determine the velocity of ultrasonic waves in a liquid. Ultrasound is sound above $20$ kHz (audio is $20$ Hz–$20$ kHz, infrasound below $20$ Hz). A piezoelectric quartz crystal fixed at the bottom of the cell is driven at $2$ MHz and acts as the source; a metal plate parallel to it, raised and lowered by a micrometer screw ($25$ mm travel, $0.01$ mm least count), reflects the wave.

The source end is an antinode and the plate a node, so standing waves form when the gap satisfies $l=(n+\tfrac12)\lambda/2$. At each such gap the reflected wave reinforces the source and the **anode current of the generator peaks**. Successive maxima are separated by
$$d=\frac{\lambda}{2},\qquad v=f\lambda=2fd,\qquad\beta_{\rm ad}=\frac{1}{\rho v^2}\ \ (\text{compressibility}=1/\text{bulk modulus}).$$

![[PL-ultrasonic.png]]

**Figure:** Anode current against reflector position for water at 2 MHz (illustrative): maxima every $0.37$ mm, so $\lambda=0.74$ mm and $v=1480$ m/s. Recording every third maximum (green brackets, $3d=1.11$ mm) reduces the effect of the micrometer's reading error.

> [!question]- 🎯 Predict first: glycerine is much more viscous than water. Is sound faster or slower in it?
> **Faster** (about $1900$ m/s vs $1480$ m/s). Sound speed is set by the bulk modulus and density, $v=\sqrt{K/\rho}$; glycerine is *less compressible* (larger $K$), which wins over its higher density. Viscosity mostly affects absorption, not speed.

## Procedure (condensed)
1. Fill the cell with water (no air bubbles) while it is detached from the base; wipe overflow.
2. Set the ADJ knob near centre and GAIN at maximum; switch on and let it settle. Keep the needle on the $0$–$100\ \mu$A scale.
3. Turn the micrometer slowly in one direction; record the reading at **every third** maximum (or minimum) for $n,n+3,\dots,n+24$.
4. The shift for $(n+15)-n$ divided appropriately gives the mean shift $d$; compute $\lambda=2d$, $v=f\lambda$ and $\beta$ with uncertainties.
5. Repeat with glycerine or glycerine solution.

**Precautions:** fill the cell before switching on; do not tilt it after filling (liquid creeping into the micrometer threads); empty the cell afterwards.

## Worked example
> [!example]- 🔬 Water at 2 MHz (illustrative)
> Mean shift per 3 maxima $=1.11$ mm, so $d=0.37$ mm, $\lambda=0.74$ mm, $v=2\times10^6\times0.74\times10^{-3}=1480$ m/s.
> $\beta=1/(\rho v^2)=1/(998\times1480^2)=4.6\times10^{-10}$ Pa⁻¹.
> **Check:** recording $n,n+3,\dots,n+24$ spans $8$ gaps of $3d$, about $8.9$ mm of micrometer travel; with a $0.01$ mm read-out this gives $d$ to $\sim0.1\%$; the error in $v$ is then dominated by the frequency stability and temperature (water's $v$ changes by about $3$ m/s per °C).

> [!warning]- ⚠️ Counting every maximum without taking *every third*
> Reading every maximum multiplies the micrometer's read-out error by the number of gaps. Taking every third averages over larger spans, giving a smaller *relative* error.

> [!danger]- 💥 Temperature drift
> $v$ depends on temperature, and the cell warms during the run. Keep a constant-temperature bath or finish quickly and record the temperature.

## Questions
> [!question]- Why is the crystal end an antinode and the reflector a node?
> The crystal is the driven source, vibrating with maximum amplitude; the rigid reflector forces displacement to be small there.

> [!question]- What is the physical meaning of $\beta=1/\rho v^2$?
> It is the fractional volume change per unit pressure (adiabatic, because sound compressions are too quick for heat to flow). Stiffer liquids have smaller $\beta$.

## Connections
- **Theory:** standing waves as in [[Wave Equation on a Finite Interval]], and sound as a compression wave; $v=\sqrt{K/\rho}$ links to [[Fluids and Solids - Pressure, Stress and Constitutive Laws]].
- **Cross-domain:** [[Simple Harmonic Motion]] (the crystal and fluid elements oscillate harmonically) and [[Resonance and Buckling - Instability as an Eigenvalue Problem]] (the standing-wave condition is an eigenvalue condition on $l$).
- **Errors:** [[Error Analysis - Uncertainty and Propagation]] ($\sigma_v$ from $\sigma_d$ and $\sigma_f$, and $\sigma_\beta$ with $v$ squared).

## Self-check
- [ ] I can derive $d=\lambda/2$ and $v=2fd$.
- [ ] I can explain why every third maximum is recorded.
- [ ] I can compute $\beta$ and its uncertainty.

## Metadata
- **Status:** draft · **Type:** concept (lab) · **Difficulty:** intermediate
- **Course map:** [[Physics Laboratory I - MOC]]

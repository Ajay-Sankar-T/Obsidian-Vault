---
tags: [concept, physics-lab, PH1030, pendulum, experiment]
status: draft
up: "[[Physics Laboratory I - MOC]]"
aliases: [compound pendulum, physical pendulum experiment, variable g pendulum, radius of gyration, reversible pendulum]
---

# Lab - Variable g Pendulum

> [!abstract] The experiment in one line
> Swing a 1 m steel rod from different pivot points, find the two pivots that give the same period, and read off both $g$ and the radius of gyration $K$ from a graph. Then tilt the plane of swing and watch the effective $g$ shrink as $g\cos\Phi$.

## Aim and apparatus
**Aim:** (i) find $g$ with a compound pendulum and the radius of gyration $K$ about the centre of gravity; (ii) investigate how the measured $g$ depends on the tilt of the oscillation plane.
**Apparatus:** a 1 m stainless-steel rod (10 mm diameter) with holes along it, a clamp stand that can tilt the plane of oscillation, a stopwatch.

## Theory

A rigid body pivoted at $P$, with its centre of gravity $G$ a distance $l$ below, has restoring torque $-mgl\sin\theta$. For small angles (parallel-axis theorem $I=mK^2+ml^2$):

$$T=2\pi\sqrt{\frac{I}{mgl}}=2\pi\sqrt{\frac{K^2/l+l}{g}}\ \Longrightarrow\ L=l+\frac{K^2}{l}\ \text{(length of the equivalent simple pendulum)},\quad T=2\pi\sqrt{L/g}$$

Rearranged, $l^2-lL+K^2=0$ has two roots with $l_1+l_2=L$ and $l_1l_2=K^2$:

$$\boxed{\,g=\frac{4\pi^2L}{T^2},\qquad K=\sqrt{l_1l_2}\,}$$

For a uniform rod of length $D$, $K^2=D^2/12$, so $K=28.9$ cm for $D=1$ m. If the swing plane is tilted by $\Phi$ from the vertical, only $g\cos\Phi$ acts in it: $T(\Phi)=2\pi\sqrt{I/(mgl\cos\Phi)}$.

![[PL-compound-pendulum.png]]

**Figure:** Left, $T$ against $l$ for the 1 m rod. A horizontal line at $T=1.80$ s cuts the curve at two pivots, $l_1=12.2$ cm and $l_2=68.3$ cm; their sum is $L=80.5$ cm and $\sqrt{l_1l_2}=28.9$ cm $=K$. Right, tilting the plane increases the period as $1/\sqrt{\cos\Phi}$.

> [!question]- 🎯 Predict first: as the pivot approaches the centre of gravity ($l\to0$), what happens to the period?
> It grows without bound: $T\to2\pi K/\sqrt{gl}\to\infty$. A body pivoted *at* its centre of gravity has no restoring torque. This is why the graph has a minimum and then climbs steeply on the left, and why the manual says to stop when the period "becomes very large".

## Procedure (condensed)
1. Clamp the rod in a vertical plane ($\Phi=0$); keep the amplitude below $10^\circ$.
2. Time **10 oscillations**, three times; average and divide by 10 for $T$; give $\Delta T$.
3. Measure the distance $d$ from the pivot hole to the free end; $l=d-D/2$.
4. Move to the next hole (steps of about 2 cm) until the period gets very large.
5. Plot $T$ against $l$; draw a horizontal line ABC at a chosen $T$ that cuts the curve at two points; the two distances AC and BC are $l_1,l_2$, so $L=\text{AC}+\text{BC}$ and $K=\sqrt{\text{AC}\times\text{BC}}$.
6. Fit $L$ against $T^2$ for several lines: the slope is $g/4\pi^2$.
7. Tilt the plane to several $\Phi$ at a fixed $l$; confirm $4\pi^2(K^2+l^2)/(l\cos\Phi)\propto T^2$.

## Worked example
> [!example]- 🔬 Horizontal line at $T=1.80$ s on a 1 m rod (consistent illustrative numbers)
> $L=gT^2/4\pi^2=9.81(1.80)^2/39.48=0.805$ m. The two roots of $l^2-0.805l+K^2=0$ with $K^2=D^2/12=0.0833$ m² are $l_1=0.122$ m and $l_2=0.683$ m.
> **Check:** $l_1+l_2=0.805$ ✓, $\sqrt{l_1l_2}=0.289$ m ✓ $=K$. Then $g=4\pi^2(0.805)/1.80^2=9.81$ m/s² ✓.

> [!warning]- ⚠️ Swinging through large angles
> Amplitude above $10^\circ$ lengthens the period by more than $0.2\%$ (see [[The Nonlinear Pendulum]]) and biases $g$ low. Keep it small.

> [!danger]- 💥 Measuring $l$ from the pivot to the *end* of the rod
> $l$ is the distance to the **centre of gravity**, at $D/2$. Using $d$ directly makes $K$ and $L$ meaningless.

## Questions
> [!question]- Why does tilting the plane increase the period?
> Only the component $g\cos\Phi$ of gravity acts along the plane of motion, so the restoring torque is weaker: $T\propto1/\sqrt{\cos\Phi}$. At $\Phi=60^\circ$, $g_{\rm eff}=g/2$ and $T$ rises by $\sqrt2$.

> [!question]- Why are there four pivot points giving the same period?
> The two roots $l_1,l_2$ exist on **each side** of the centre of gravity, by symmetry.

## Connections
- **Theory:** [[Simple Harmonic Motion]], [[The Nonlinear Pendulum]], [[Newton's Second Law in Polar Coordinates]]; moments of inertia via [[Second Moments of Area - One Integral, Many Jobs]].
- **Errors:** [[Error Analysis - Uncertainty and Propagation]] ($\sigma_g$ from $\sigma_L$ and $\sigma_T$).

## Self-check
- [ ] I can derive $T=2\pi\sqrt{(K^2/l+l)/g}$ and the roots relations.
- [ ] I can get $g$ and $K$ from the graph construction.
- [ ] I can explain the $\cos\Phi$ dependence.

## Metadata
- **Status:** draft · **Type:** concept (lab) · **Difficulty:** intermediate
- **Course map:** [[Physics Laboratory I - MOC]]

---
tags: [concept, physics-lab, PH1030, magnetism, biot-savart, experiment]
status: draft
up: "[[Physics Laboratory I - MOC]]"
aliases: [magnetic field of a circular coil, tangent galvanometer, earth's horizontal magnetic field, on-axis field]
---

# Lab - Magnetic Field along the Axis of a Coil

> [!abstract] The experiment in one line
> A compass needle at the centre of a vertical current-carrying coil is deflected by the coil's field acting against the Earth's horizontal field; since $B=B_E\tan\theta$, plotting $\tan\theta$ against position along the axis maps the coil's field, and the deflection at the centre gives $B_E$.

## Aim and theory
**Aim:** plot the variation of the magnetic field along the axis of a circular coil and estimate the Earth's horizontal field $B_E$. **Apparatus:** a tangent galvanometer (coil with a compass box sliding along its axis on a bench), DC supply, rheostat, commutator, ammeter, key.

On the axis of a coil of $n$ turns, radius $r$, current $i$, at distance $x$ from the centre,
$$B(x)=\frac{\mu_0\,n\,i\,r^2}{2\,(r^2+x^2)^{3/2}}.$$
If the coil's field is perpendicular to $B_E$, the needle settles at angle $\theta$ with $B=B_E\tan\theta$, so
$$\tan\theta\ \propto\ \frac{1}{(r^2+x^2)^{3/2}},\qquad B_E=\frac{\mu_0ni}{2r\tan\theta_0}\ \ (\theta_0\text{ at the centre}).$$

![[PL-coil-field.png]]

**Figure:** Left, $B(x)/B(0)$ for a coil of radius $7$ cm: a bell-shaped peak that falls to $35\%$ at $x=r$; the field is flattest around the centre, with inflection points at $x=\pm r/2$. Right, what the compass reports when $\theta(0)\approx60^\circ$: since the needle reads $\tan\theta\propto B$, the angle falls more slowly than $B$ (to $31.5^\circ$ at $x=r$).

> [!question]- 🎯 Predict first: at what distance from the centre does the on-axis field drop to half its central value?
> $(1+x^2/r^2)^{-3/2}=\tfrac12$ gives $x=r\sqrt{2^{2/3}-1}=0.77r$. For $r=7$ cm that is about $5.4$ cm. The field falls quickly beyond one radius; this is what the graph's width tells you.

## Procedure (condensed)
1. Place the compass box so its needle is at the coil's centre; rotate the whole setup until the coil lies in the **magnetic meridian** (coil, needle and its image in one vertical plane); turn the box until the pointer reads $0$–$0$.
2. Pass current one way, note both pointer ends, **reverse** it with the commutator and note again: equal readings confirm the meridian alignment.
3. Assign least counts to all readings, including $r$, $i$, $x$ and angles.
4. Adjust the rheostat for a deflection of $50^\circ$–$70^\circ$ at the centre; take **four readings** (both pointer ends, both current directions) and average.
5. Move the box in steps of $1$–$4$ cm (so the deflection changes by $4$–$5^\circ$), keeping $i$ constant, on **both sides** (negative on one side).
6. Plot $\tan\theta$ against $x$ with the coil centre at the origin; also $B_E$ from the centre deflection.

## Worked example
> [!example]- 🔬 Illustrative coil: $n=15$ turns, $r=7.0$ cm, $i=0.49$ A, deflection at the centre $60^\circ$
> $B(0)=\dfrac{\mu_0ni}{2r}=\dfrac{(4\pi\times10^{-7})(15)(0.49)}{2(0.070)}=6.6\times10^{-5}$ T.
> $B_E=B(0)/\tan60^\circ=3.8\times10^{-5}$ T $=0.38$ G, the right size for India's horizontal field.
> At $x=r$: $B=B(0)\times0.354$, so $\tan\theta=1.732\times0.354=0.61$ and $\theta=31.5^\circ$, matching the figure.
> **Check:** the graph of $\tan\theta$ against $x$ should have the same bell shape and the inflection at $x=\pm r/2$.

> [!warning]- ⚠️ Using the angle instead of $\tan\theta$
> $B\propto\tan\theta$, not $\theta$. Plotting $\theta$ flattens the peak (see the right panel) and misrepresents the field profile.

> [!danger]- 💥 Magnetic objects on the bench
> Steel screws, mobile phones and a nearby wire pair change $B_E$ locally. Remove them, and keep the leads twisted so their fields cancel.

## Questions
> [!question]- Why reverse the current and average?
> It cancels errors from a coil not exactly in the meridian and from the needle's pivot friction/eccentricity (the needle swings equally to both sides).

> [!question]- Why does the deflection change so little over the middle of the axis?
> Near the centre $B(x)\approx B(0)(1-\tfrac32x^2/r^2)$: a quadratic dip, so the field is nearly uniform there. Two coils spaced a radius apart (Helmholtz pair) cancel the quadratic term and give an extremely uniform field.

## Connections
- **Theory:** [[Conservative Forces, Gradient and Curl]] (field as a vector field), [[Curvilinear Coordinates - Cylindrical and Spherical]] (axial symmetry), [[Stokes' Theorem and Circulation]] (Ampère's law is Stokes applied to $\mathbf B$).
- **Cross-domain:** [[Gears, Transformers and Reflected Impedance]] (coils and magnetic coupling in electrical machines); [[Lab - Mapping Equipotential Lines]] for the electric analogue (a field mapped point by point with a probe).
- **Errors:** [[Error Analysis - Uncertainty and Propagation]] ($\tan\theta$ has error $\sec^2\theta\,\sigma_\theta$, larger at high angles).

## Self-check
- [ ] I can write $B(x)$ and explain $B=B_E\tan\theta$.
- [ ] I can estimate $B_E$ from the centre deflection.
- [ ] I can explain the meridian check and the current reversal.

## Metadata
- **Status:** draft · **Type:** concept (lab) · **Difficulty:** intermediate
- **Course map:** [[Physics Laboratory I - MOC]]

---
title: Tutorial 9 – Flat-Face Cam with Cycloidal Motion
course: ME 2201 Kinematics & Dynamics of Machinery
tutorial: 9
due: 2026-11-09
tags:
  - KDoM
  - tutorial-solution
  - cams
  - flat-face-follower
source: "[[Tutorial 9.pdf]]"
aliases:
  - Cam tutorial
  - Tutorial 9 solution
---

# Tutorial 9 – Flat-Face Cam with Cycloidal Motion

Source: [[Tutorial 9.pdf]] · Previous: [[Tutorial-7-solution]] · Theory: [[Cam Motion Laws and the Flat-Face Follower]] · Numbers and figures: `tut9_10.py` (same folder)

> [!question] Problem
> Flat-face follower: dwell $90^\circ$, rise $25$ mm in the next $90^\circ$, dwell $90^\circ$, return in the last $90^\circ$. Cycloidal rise and return. Base circle $50$ mm, offset $15$ mm.
> (a) Draw the profile for anticlockwise rotation. (b) Construct the rise graphically with six positions. (c) At $100$ rpm find the maximum follower velocity and acceleration. (d) Find $\rho$ and the eccentricity of the driving effort $30^\circ$ into the rise.

> [!summary] Answers at a glance
> | Part | Result |
> |---|---|
> | a | Profile in **fig. 2** (code in the appendix); outline does not depend on the offset |
> | b | $s$ at $0,15,\dots,90^\circ$ = **0, 0.72, 4.89, 12.50, 20.11, 24.28, 25.00 mm** |
> | c | $v_{\max}=\mathbf{0.333}$ m/s at mid-rise · $a_{\max}=\mathbf{6.98}$ m/s² at $22.5^\circ$ into the rise |
> | d | $\rho=\mathbf{110.0}$ mm · $\varepsilon=\mathbf{8.87}$ mm (offset on the rise side; $38.9$ mm if on the other side) |

---

## Given and setup

| Phase | Cam angle $\theta$ | Follower |
|---|---|---|
| dwell | $0^\circ$–$90^\circ$ | $s=0$ |
| **rise** | $90^\circ$–$180^\circ$ | cycloidal, $h=25$ mm, $\beta=\pi/2$ |
| dwell | $180^\circ$–$270^\circ$ | $s=25$ mm |
| return | $270^\circ$–$360^\circ$ | cycloidal, $s=h-s_{\text{rise}}$ |

$R_0=50$ mm, $e=15$ mm, $\omega=100\ \text{rpm}=10.472$ rad/s, anticlockwise. "30° into the rise" means $\varphi=30^\circ$, i.e. $\theta=120^\circ$, $u=\varphi/\beta=1/3$.

With $u=\varphi/\beta$:

$$
s=h\Big(u-\frac{\sin2\pi u}{2\pi}\Big),\quad
s'=\frac{h}{\beta}(1-\cos2\pi u),\quad
s''=\frac{2\pi h}{\beta^2}\sin2\pi u
$$

> [!question]- Predict first: does the 15 mm offset change the cam outline?
> No. A flat face is a line at distance $R_0+s$ from the cam centre, perpendicular to the follower motion; moving the axis sideways slides the follower along its own face and changes nothing about where the face is. The offset changes only the **driving-effort eccentricity** and where the face must reach (parts d and the face width).

![[T9-fig1-motion.png]]

---

## (a) Cam profile

**Recognise.** A flat face rolling on the cam touches it where the face is tangent to the profile. The contact point lies $s'(\theta)$ to the right of the line through $O$ parallel to the axis (instantaneous centre of cam and follower sits at $\dot s/\omega$ from $O$). In the follower frame the contact point is $(s',\,R_0+s)$. Rotate it back by $-\theta$ into the cam's axes:

$$
x=s'\cos\theta+(R_0+s)\sin\theta,\qquad
y=-s'\sin\theta+(R_0+s)\cos\theta
$$

Evaluating over $0$–$360^\circ$ gives fig. 2: a $50$ mm circular arc, the rise, a $75$ mm arc, the return. Check at a dwell: $s'=0$, so $x=50\sin\theta$, $y=50\cos\theta$, a circle of radius $50$.

![[T9-fig2-profile.png]]

Orange = follower face at $\theta=120^\circ$ (tangent to the profile at the contact point). Dotted purple = the offset circle the follower axis stays tangent to.

### Animation
Cam turning anticlockwise; red dot = contact point, which slides along the face by $s'$.

![[T9-anim.gif]]

---

## (b) Graphical construction of the rise (six steps of 15°)

1. **Displacement diagram.** Draw $\varphi$ from $0$ to $90^\circ$ in six equal parts. Join the origin to the end of the lift ($\varphi=90^\circ$, $s=25$): this is the uniform-motion line.
2. **Cycloid construction.** Draw a circle of radius $h/2\pi=3.98$ mm at the origin and divide its circumference into **six equal arcs**, numbering the points clockwise from the right-hand end of the horizontal diameter. Project the points horizontally onto the lift axis. Through projection $k$ draw a line parallel to the uniform-motion line up to ordinate $k$. The ends of these lines lie on the cycloid, because $s=hu-\frac{h}{2\pi}\sin2\pi u$ is the uniform line minus the circle's vertical projection (a clockwise point at $60^\circ k$ sits at height $-\frac{h}{2\pi}\sin2\pi u_k$).
3. **Inversion.** Hold the cam still and turn the follower clockwise. For position $k$, rotate the offset-circle tangent (the follower axis) by $15^\circ k$ from its start, mark $R_0+s_k$ along it, and draw the **face line perpendicular to the axis** there.
4. **Envelope.** Draw a smooth curve tangent to all the face lines; the touching points lie at $s'_k$ from the axis foot.

| $k$ | $\varphi$ | uniform line $hu$ (mm) | $\frac{h}{2\pi}\sin2\pi u$ (mm) | $s_k$ (mm) |
|---|---|---|---|---|
| 0 | 0° | 0.000 | 0.000 | **0.000** |
| 1 | 15° | 4.167 | +3.446 | **0.721** |
| 2 | 30° | 8.333 | +3.446 | **4.888** |
| 3 | 45° | 12.500 | 0.000 | **12.500** |
| 4 | 60° | 16.667 | −3.446 | **20.112** |
| 5 | 75° | 20.833 | −3.446 | **24.279** |
| 6 | 90° | 25.000 | 0.000 | **25.000** |

The cycloid starts below the uniform line, crosses it at mid-rise and finishes above it. The profile of $s$ is symmetric about the mid-point: $s_k+s_{6-k}=25$ mm.

![[T9-fig3-graphical.png]]

> [!question]- Why do six steps over 90° put the rise on 15° steps?
> Six equal intervals of the 90° rise give 15° each. The rolling circle then has 60° between division points. If your course counts "six positions" as six points rather than six intervals, use 18° steps; the construction is identical.

---

## (c) Maximum velocity and acceleration

$$
v_{\max}=\frac{2h\omega}{\beta}\ \ (\text{at }u=\tfrac12),\qquad
a_{\max}=\frac{2\pi h\omega^2}{\beta^2}\ \ (\text{at }u=\tfrac14\text{ and }\tfrac34)
$$

$$
\frac{\omega}{\beta}=\frac{10.472}{1.5708}=6.667\ \text{s}^{-1}
\;\Rightarrow\;
v_{\max}=2(25)(6.667)=333.3\ \text{mm/s},\qquad
a_{\max}=2\pi(25)(6.667)^2=6981\ \text{mm/s}^2
$$

> [!success] Result
> $v_{\max}=0.333$ m/s at $\theta=135^\circ$ · $a_{\max}=6.98$ m/s² at $\theta=112.5^\circ$ (acceleration) and $-6.98$ m/s² at $157.5^\circ$ (deceleration). The return has the same magnitudes.

**Check.** Units: mm·s⁻¹ and mm·s⁻². The uniform-law speed $h\omega/\beta=166.7$ mm/s; cycloidal peak is exactly twice that ✓.

---

## (d) Radius of curvature and driving-effort eccentricity at 30° into the rise

At $u=1/3$ ($\sin120^\circ=0.8660$, $\cos120^\circ=-0.5$):

$$
s=25\Big(\tfrac13-\tfrac{0.8660}{2\pi}\Big)=4.888\ \text{mm}
$$
$$
s'=\frac{25}{\pi/2}\,(1+0.5)=23.873\ \text{mm/rad},\qquad
s''=\frac{2\pi(25)}{(\pi/2)^2}(0.8660)=55.133\ \text{mm/rad}^2
$$

**Radius of curvature of a flat-face profile:**

$$
\rho=R_0+s+s''=50+4.888+55.133=\mathbf{110.0\ mm}
$$

**Eccentricity of the driving effort.** The cam force acts along the follower axis direction through the contact point, $s'=23.87$ mm from $O$'s line; the follower axis is $e=15$ mm from it. With the axis on the **rise side** of $O$ (the side the contact point moves to):

$$
\varepsilon=s'-e=23.873-15=\mathbf{8.87\ mm}
$$

> [!warning] Which side is the offset?
> The question gives only the size, 15 mm. On the rise, driving effort exists, so an offset **towards** the contact side is the sensible design: $\varepsilon=8.87$ mm. With the opposite offset, $\varepsilon=s'+e=38.87$ mm. I report the first and state the assumption. Fig. 4 shows both curves over the whole cycle.

![[T9-fig4-rho-ecc.png]]

**Sanity checks.**
- $\rho>0$ everywhere, minimum $8.93$ mm near $\theta=156.5^\circ$ (end of the rise, where $s''$ is most negative). The profile is convex, so a flat face can follow it. $8.9$ mm is sharp: contact stress there will be high.
- With the rise-side offset the largest $\varepsilon$ in the rise is $16.8$ mm (at mid-rise, $31.83-15$); the largest on the return is $46.8$ mm, harmless because the spring drives it.
- The face must reach $\pm31.83$ mm of the cam-centre line ($s'_{\max}=2h/\beta$), i.e. $63.7$ mm of face at least, or $\pm46.8$ mm about the axis if the face is symmetric about it.

---

## Common trap / alternative

> [!warning] Traps
> - Adding the offset into $\rho$ or into the profile.
> - Measuring "30° into the rise" from the start of the cycle ($\theta=30^\circ$) — that is still in the dwell.
> - $\beta$ in degrees in $\omega/\beta$.
> - Forgetting $\rho=R_0+s+s''$ has a **plus** $s''$, and $s''$ goes negative later in the rise.

**Alternative for (d).** Construct the profile numerically (see appendix) and fit a circle through three neighbouring points at $\theta=120^\circ$: it returns $\rho\approx110$ mm, the same answer.

---

## Summary of answers

> [!success] Final answers
> a. Profile: fig. 2 (outline independent of the offset).
> b. $s=0,\ 0.72,\ 4.89,\ 12.50,\ 20.11,\ 24.28,\ 25.00$ mm at $0^\circ,15^\circ,\dots,90^\circ$.
> c. $v_{\max}=0.333$ m/s · $a_{\max}=6.98$ m/s².
> d. $\rho=110.0$ mm · $\varepsilon=8.87$ mm (offset on the rise side).

### Quick revision
- [ ] Cycloidal: $v_{\max}=2h\omega/\beta$ · $a_{\max}=2\pi h\omega^2/\beta^2$
- [ ] Flat face: contact at $s'$ from the centre line, $\rho=R_0+s+s''$, $\varepsilon=s'-e$
- [ ] Offset never changes a flat-face cam's outline

---

## Appendix

```python
import numpy as np
h, R0, e, beta, w = 25.0, 50.0, 15.0, np.pi/2, 100*2*np.pi/60
def cyc(u):
    s  = h*(u - np.sin(2*np.pi*u)/(2*np.pi))
    s1 = h/beta*(1 - np.cos(2*np.pi*u))
    s2 = 2*np.pi*h/beta**2*np.sin(2*np.pi*u)
    return s, s1, s2
s, s1, s2 = cyc(1/3)
print(s, 50+s+s2, s1-e)                       # 4.888  110.02  8.873
print(2*h*w/beta/1000, 2*np.pi*h*w**2/beta**2/1000)   # 0.3333 m/s  6.981 m/s^2
```

### Figure index
`T9-fig1` motion curves · `fig2` profile · `fig3` graphical construction · `fig4` $\rho$ and $\varepsilon$ · `T9-anim.gif` cam turning. All in the `assets` folder; produced by `tut9_10.py`.

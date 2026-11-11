---
tags: [concept, materials]
course: "Materials and Design (ME2200)"
aliases: [Paris law, Paris-Erdogan, Fatigue crack growth, da/dN, Damage tolerance, Crack propagation life]
---

# Fatigue Crack Growth — Paris Law

> [!abstract] In one breath
> If a crack already exists, fatigue no longer needs a "start": the crack **grows a little every cycle**, and the growth per cycle depends only on the **range of stress intensity** $\Delta K$. Integrate the **Paris law** from the initial crack length to the critical length and you get the remaining life.

Part of [[Materials and Design - MOC]]. Previous: [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]], [[Fracture Mechanics - Stress Intensity and Griffith]].

## 1. The growth-rate curve

Plot the crack growth per cycle $da/dN$ against $\Delta K$ on log–log axes:

| Region | $\Delta K$ | Behaviour |
| --- | --- | --- |
| I | near threshold $\Delta K_{th}$ | growth falls steeply to zero below $\Delta K_{th}$ (no growth, "infinite" life) |
| **II** | middle | straight line: the **Paris law** |
| III | $K_{max}\to K_{Ic}$ | growth accelerates to final fracture |

**Paris–Erdogan law:**

$$
\frac{da}{dN}=C\,(\Delta K)^m,\qquad \Delta K=Y\,\Delta\sigma\sqrt{\pi a}
$$

$\Delta\sigma=\sigma_{max}-\sigma_{min}$ (only the **tensile** part counts); $C$ and $m$ are material constants ($m\approx2$–4 for metals; for ductile steels $m\approx3$, with $C$ about $10^{-11}$ in units m/cycle for $\Delta K$ in MPa√m).

## 2. Life by integration

Separate variables with constant $Y$ and $\Delta\sigma$:

$$
N_f=\int_{a_i}^{a_c}\frac{da}{C\,(Y\Delta\sigma\sqrt{\pi a})^m}
=\frac{a_c^{1-m/2}-a_i^{1-m/2}}{C\,Y^m\,\Delta\sigma^m\,\pi^{m/2}\,(1-m/2)}\qquad(m\ne2)
$$

The critical length $a_c$ is where $K_{max}=K_{Ic}$ (from [[Fracture Mechanics - Stress Intensity and Griffith]]). For $m>2$ the life is controlled by the **initial** length (the exponent $1-m/2$ is negative, so $a_i$ dominates). Most life is spent while the crack is small.

## 3. Worked example

Steel plate, edge crack, $Y=1.12$, stress range $\Delta\sigma=200$ MPa (0 to 200 MPa, $R=0$), initial crack $a_i=0.5$ mm, $K_{Ic}=50$ MPa√m, $C=10^{-11}$, $m=3$.

$$
a_c=\frac1\pi\Big(\frac{50}{1.12\times200}\Big)^2=15.9\ \text{mm},\qquad
\Delta K_i=1.12(200)\sqrt{\pi\times0.0005}=8.9\ \text{MPa}\sqrt{\text{m}}
$$

$$
N_f=\frac{a_c^{-1/2}-a_i^{-1/2}}{C\,Y^3\Delta\sigma^3\pi^{3/2}(-1/2)}=\mathbf{1.18\times10^5\ cycles}
$$

(numerical integration of the same law gives $1.176\times10^5$). With a **1 mm** initial crack the life falls to $7.6\times10^4$: doubling the flaw costs 36 % of the life.

![[MAT-7-paris.png]]

The right-hand graph shows why a growing crack is dangerous: **61 % of the life is spent below 2 mm**, where the crack is invisible, while the last 17 % of the cycles carry it from 5 mm to the critical 16 mm.

## 4. Using it: inspection intervals

Damage-tolerant design assumes the largest flaw the inspection can miss, $a_i$, computes $N_f$, and sets the inspection interval at a fraction (typically $\tfrac13$–$\tfrac12$) of that life, so that a crack is found before it reaches $a_c$. Reducing $\Delta\sigma$ helps strongly: $N_f\propto\Delta\sigma^{-m}$, so cutting the stress range by 20 % extends life by $1/0.8^3=1.95$.

> [!warning] Traps
> - Using $\Delta K$ with the *total* range including compression: only the tensile part contributes (use $\sigma_{max}$ and $\sigma_{min}=0$ for the negative part).
> - Treating $Y$ as constant when the crack is long relative to the width (it rises).
> - Integrating with $a_i=0$: the life diverges, because $a^{1-m/2}\to\infty$ as $a\to0$; start from the detectable crack.
> - Using the Paris law below $\Delta K_{th}$ (where cracks do not grow) or above region II.
> - Using different units for $C$: it depends on $m$.

> [!question]- Predict first: stress range reduced from 200 to 160 MPa. By how much does the remaining life change?
> $N_f\propto\Delta\sigma^{-3}$ (the critical length also changes slightly, here ignored): $(200/160)^3=1.95$ times longer. A 20 % stress cut nearly doubles the life: fatigue life is extremely sensitive to the stress range.

> [!question]- Why is the final fast growth almost irrelevant to the life?
> It is not irrelevant, just short. The growth per cycle $da/dN\propto a^{m/2}$ speeds up as $a$ grows, so the cycles needed to cross a given length shrink: from 0.5 mm to 2 mm takes 61 % of the life, while from 5 mm to 16 mm takes only 17 %. The crack is visible and dangerous only in the last fraction.

## 5. Connections

- [[Fracture Mechanics - Stress Intensity and Griffith]] — $K_I$ and $K_{Ic}$ define $\Delta K$ and the end of life.
- [[Fatigue Failure - S-N Curve, Marin Factors and Goodman Diagram]] — S–N life = initiation plus this growth, lumped.
- [[Static Failure Theories - Tresca and von Mises]] — strength-based theories fail on the cycle when the net section yields; this note predicts when that section is reached.

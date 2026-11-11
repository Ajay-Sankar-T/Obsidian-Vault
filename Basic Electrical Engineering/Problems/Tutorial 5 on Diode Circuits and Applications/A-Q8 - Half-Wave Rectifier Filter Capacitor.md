---
tags: [EE1100, diodes, tutorial-solution, rectifier, filter]
---

# A-Q8 — Filter Capacitor for a Half-Wave Rectifier (10 % ripple)

Hub: [[Tutorial 5 on Diode Circuits and Applications]] · Previous: [[A-Q7 - Ripple, Ripple Factor and Form Factor]] · Next: [[A-Q9 - Full-Wave Rectifier Filter Capacitor]]

> [!question] In a half-wave rectifier the ripple at the output should be 10 % of the peak value of the input $v_s=V_m\sin314t$. Find the capacitor for $R_2=1\ \text{k}\Omega$. ($R_1$, in series with the diode, is very small.)

## 1. Theory

The filter capacitor charges to $\approx V_m$ near the peak (the small $R_1$ and the ideal diode make the charging time negligible) and then discharges through $R_2$ for almost a full period $T=1/f$ until the next peak. For small ripple the discharge is nearly linear at the load current $I_{dc}\approx V_m/R_2$:

$$V_r=\frac{\Delta Q}{C}=\frac{I_{dc}\,T}{C}=\frac{V_m}{fR_2C}\quad\Longrightarrow\quad C=\frac{V_m}{fR_2V_r}$$

Here **ripple** means the peak-to-peak ripple voltage $V_r$.

## 2. Solution

$\omega=314$ rad/s $\Rightarrow f=314/2\pi\approx50$ Hz, $T=20$ ms. $V_r=0.1V_m$, $R_2=1$ kΩ:

$$C=\frac{V_m}{f\,R_2\,(0.1V_m)}=\frac1{50\times1000\times0.1}=2\times10^{-4}\ \text{F}$$

$$\boxed{C\approx200\ \mu\text{F}}$$

($V_m$ cancels, so the answer does not depend on the amplitude.)

## 3. Check with the exact exponential discharge

During discharge $v_o=V_me^{-t/R_2C}$, and the capacitor only discharges for $t_d\approx T-t_{charge}$, slightly less than $T$. Solving the exact steady-state waveform numerically for $V_{pp}=0.1V_m$ gives
$$C_{exact}=175.9\ \mu\text{F}.$$
The simple formula (200 µF) is therefore a safe (slightly conservative) design value.

![[A8-A9-capacitor-design.png]]

| | formula | exact |
|---|---|---|
| $C$ for 10 % ripple | 200 µF | 175.9 µF |
| $V_{dc}\approx V_m-V_r/2$ | $0.95V_m$ | $0.955V_m$ |
| ripple of the 200 µF capacitor | $0.100V_m$ | $0.089V_m$ |

## 4. Design notes
- Capacitor voltage rating $\ge V_m$ (with margin); a polarised electrolytic is used, mind the polarity.
- Diode PIV $=2V_m$ with the filter.
- Conduction angle $\theta_c\approx\sqrt{2V_r/V_m}=\sqrt{0.2}=0.45$ rad $=25.6^\circ$ so the diode current is a narrow, tall pulse (see [[A-Q6 - Rectifier Circuits and Waveforms]]).

> [!tip] If "ripple" meant the rms ripple factor
> With $RF=V_{ac}/V_{dc}=0.1$ one would use $C=\dfrac1{2\sqrt3fR_2\,RF}=57.7\ \mu$F. The sheet's wording ("ripple … 10 % of the peak value") corresponds to the peak-to-peak interpretation used above.

![[A8-A9-design-curve.png]]

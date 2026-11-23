---
tags: [EE1100, tutorial-solution, filters, band-reject, notch, design]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
---

# T4-Q7: Designing a 400 Hz Band-Reject Filter

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Resonance and Passive Filters]] · Previous: [[T4-Q6 - Series RLC Band-Pass Filter]] · Next: [[T4-Q8 - FM Receiver Band-Pass Design]]

> [!question] Cabin communication is disturbed by a 400 Hz interference (the aircraft power frequency). The speaker is modelled as a $4\ \text{k}\Omega$ resistor. Design a band-rejection filter at its input to eliminate 400 Hz, using a $200\ \mu$F capacitor. *[Sheet: $L=791.6\ \mu$H]*

**Tests:** [[Theory - Resonance and Passive Filters#4. The four basic filters|band-reject (notch) filter]]: a parallel LC in the signal path.

## Given
Parallel $L$-$C$ connected in series between $V_{in}$ and the output; $R=4\ \text{k}\Omega$ from the output to ground; $C=200\ \mu$F; reject $f_0=400$ Hz.

## Principle and why it applies
A **parallel LC** has an impedance that is **infinite at its resonant frequency** and small elsewhere. Placed in series with the load it blocks exactly the resonant frequency and passes the rest (at DC the inductor shorts it; at high frequency the capacitor does). So choose $L$ so that $\omega_0=1/\sqrt{LC}$ equals the interference frequency.

## Diagram
![[T4-Q7-circuit.png]]

![[T4-Q4-Q7-filters.png]]

## Solution
$\omega_0=2\pi\times400=2513.3$ rad/s. Then
$$L=\frac1{\omega_0^2C}=\frac1{(2513.3)^2\times200\times10^{-6}}=\frac1{6.3165\times10^6\times2\times10^{-4}}=\frac1{1263.3}=7.916\times10^{-4}\ \text{H}=\mathbf{791.6\ \mu H}.$$

**How wide is the notch?** The series element is $Z_{LC}$, with the transfer function $H=\dfrac R{R+Z_{LC}}$. The $-3$ dB points are where $|Z_{LC}|=R$, i.e. where $|\omega C-1/\omega L|=1/R$, which gives a **bandwidth** $BW=\dfrac1{RC}=\dfrac1{4000\times200\times10^{-6}}=1.25\ \text{rad/s}\ (\approx0.2\ \text{Hz})$. The notch is **extremely narrow**: only a component within about 0.1 Hz of 400 Hz is rejected 3 dB or more, so component tolerances matter.

## Result
$$\boxed{L=791.6\ \mu\text{H}\quad(\text{with }C=200\ \mu\text{F},\ f_0=400\ \text{Hz})}$$

## Check
Reactances at 400 Hz: $X_L=\omega_0L=2513.3\times7.916\times10^{-4}=1.989\ \Omega$ and $X_C=\dfrac1{\omega_0C}=\dfrac1{2513.3\times2\times10^{-4}}=1.989\ \Omega$ ✓ equal, so the two parallel branch currents cancel and $Z_{LC}\to\infty$.

## Trap / alternative
- A **series** LC across the load would be a band-**pass** (short at resonance), the opposite behaviour; for a notch the LC must be **parallel and in series with the signal** (or series LC shunting the load to ground).
- The speaker resistance does not affect $\omega_0$; it only sets the notch width ($BW=1/RC$).
- A tolerance of 1 % in $L$ moves $f_0$ by 0.5 % $=2$ Hz, far outside this notch; a practical design uses a lower-$Q$ (lossy or loaded) tank.

## Concepts used
- Band-reject filter, parallel resonance ([[Theory - Resonance and Passive Filters]], [[Filter Theory]], [[Series vs Parallel RLC - Key Distinctions]])

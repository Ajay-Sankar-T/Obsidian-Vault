---
title: Theory – Diode Models and Circuit Analysis
tags:
  - EE1100
  - diodes
  - theory
---

# Diode Models and Circuit Analysis

Part of [[Tutorial 5 on Diode Circuits and Applications]].

## 1. The diode equation

$$i_D=I_s\Big(e^{v_D/(\eta V_T)}-1\Big),\qquad V_T=\frac{kT}{q}\approx25.9\ \text{mV at }300\ \text{K}$$

- Forward ($v_D\gg V_T$): $i_D\approx I_se^{v_D/\eta V_T}$ — current rises about **one decade per 60 mV** ($\eta=1$).
- Reverse ($v_D<-3V_T$): $i_D\approx-I_s$ (nA–pA for Si) until breakdown.

Details: [[A-Q3 - V-I Characteristics of a p-n Diode]], [[A-Q4 - Bias, Cut-in Voltage, Saturation Current and Resistance]].

## 2. Piecewise-linear models

| Model | ON ($v_D\ge V_\gamma$) | OFF ($v_D<V_\gamma$) | Use |
|---|---|---|---|
| **Ideal** | short circuit, $v_D=0$ | open circuit, $i_D=0$ | when source voltages ≫ 1 V |
| **Constant drop** | battery $V_\gamma=0.7$ V (Si) in series, $i_D\ge0$ | open circuit | default for "practical diode" |
| **Drop + resistance** | $v_D=V_\gamma+r_di_D$ | open circuit | when the diode resistance is given (B-Q11) |

```mermaid
graph LR
    A["anode"] -->|"i_D >= 0, v_D = V_gamma (+ r_d i_D)"| K["cathode"]
```

## 3. The "assume the state, then check" method

1. Guess the state of every diode (ON or OFF).
2. Replace each ON diode by its model (short, or battery $V_\gamma$) and each OFF diode by an open circuit.
3. Solve the resulting linear circuit (KVL/KCL, voltage divider, superposition).
4. **Check consistency:** every ON diode must carry $i_D\ge0$; every OFF diode must have $v_D<V_\gamma$.
5. If a check fails, change that diode's state and repeat.

With $n$ diodes there are at most $2^n$ guesses; in most problems the correct state is obvious (the diode whose anode is at the highest potential conducts).

## 4. Standard circuit families

| Family | Key idea | Questions |
|---|---|---|
| **Rectifier** | diode lets current flow in one direction; filter capacitor holds the peak | [[A-Q6 - Rectifier Circuits and Waveforms]], [[A-Q7 - Ripple, Ripple Factor and Form Factor]], [[A-Q8 - Half-Wave Rectifier Filter Capacitor]], [[A-Q9 - Full-Wave Rectifier Filter Capacitor]], [[B-Q8 - Half-Wave Rectifier with Series Resistor]], [[B-Q11 - Full-Wave Rectifier with Battery]] |
| **Clipper (limiter)** | a diode plus a reference battery turns ON when the input passes a threshold and then holds the output constant | [[B-Q3 - Series Battery Rectifier]], [[B-Q9 - Battery Charging Rectifier Circuit]], [[B-Q10 - Two-Level Clipper]] |
| **Clamper** | series capacitor + diode: the capacitor charges to the peak and shifts the whole waveform | [[B-Q6 - Diode Clamper]] |
| **Diode logic** | highest input wins (OR) or lowest input wins (AND) | [[B-Q2 - Diode OR Gate]], [[B-Q4 - Diode AND Gate]], [[B-Q5 - Ideal Diodes with Negative Reference]] |
| **Voltage multiplier** | capacitors charged to $V_m$ in turn and stacked in series | [[B-Q12 - Voltage Doubler]] |

## 5. Useful rectifier formulas (sinusoid $v_s=V_m\sin\omega t$, $f=\omega/2\pi$)

| | Half-wave | Full-wave |
|---|---|---|
| $V_{dc}$ | $V_m/\pi$ | $2V_m/\pi$ |
| $V_{rms}$ | $V_m/2$ | $V_m/\sqrt2$ |
| Form factor $V_{rms}/V_{dc}$ | $\pi/2=1.571$ | $\pi/(2\sqrt2)=1.111$ |
| Ripple factor $\sqrt{FF^2-1}$ | 1.211 | 0.483 |
| Ripple frequency | $f$ | $2f$ |
| PIV (no filter / with filter) | $V_m$ / $2V_m$ | bridge: $V_m$; centre-tap: $2V_m$ |
| Filter capacitor, ripple $V_r$ (pp) | $C=\dfrac{V_m}{fRV_r}$ | $C=\dfrac{V_m}{2fRV_r}$ |

## 6. Conventions

- $\omega=314$ rad/s means $f=50$ Hz (used in A-Q7 to A-Q9).
- "Practical diode" means constant drop $V_\gamma=0.7$ V unless a different value is stated.
- Ripple voltage $V_r$ is peak-to-peak unless stated; ripple factor RF is rms ripple over $V_{dc}$.

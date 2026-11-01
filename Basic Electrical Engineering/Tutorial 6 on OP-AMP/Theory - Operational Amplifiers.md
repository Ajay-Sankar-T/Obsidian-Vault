---
title: Theory – Operational Amplifiers
tags:
  - EE1100
  - op-amp
  - theory
source: "[[Lecture 32 Introduction to Operational Amplifiers.pdf]], [[Lecture 33 OP-AMP Circuits and Applications.pdf]], [[Lecture 34 OP-AMP Circuits and Applications (Contd…).pdf]]"
---

# Operational Amplifiers: models and circuit analysis

Part of [[Tutorial 6 on OP-AMP]]. Course map: [[EE1100 MOC]].

## 1. What an op-amp is
A high-gain differential amplifier with two inputs, **inverting ($-$)** and **non-inverting ($+$)**, and one output. The output is $v_o=A\,(v_+-v_-)=A\,v_d$ with $A\sim10^5$ or more, limited only by the supply rails ($\pm V_{sat}$). With no feedback, any millivolt input saturates it, so every useful circuit **feeds the output back to the inverting input** (negative feedback).

**Ideal op-amp** (Lecture 32): infinite open-loop gain, infinite input impedance (zero input current), zero output impedance, infinite bandwidth and slew rate, zero offset, infinite CMRR.

## 2. The two analysis rules (negative feedback, linear region)
1. $v_+=v_-$ (the **virtual short**): $A\to\infty$ and $v_o$ is finite, so $v_d=v_o/A\to0$.
2. $i_+=i_-=0$: no current flows into either input.

Everything in this tutorial follows from **KCL at the inverting node** plus these two rules. Note that the rules apply only with negative feedback. A positive-feedback or open-loop op-amp saturates.

## 3. The standard circuits

| Circuit | Output | Notes |
|---|---|---|
| **Inverting** $R_1$ in, $R_f$ feedback | $v_o=-\dfrac{R_f}{R_1}v_i$ | input resistance $R_1$; virtual ground at $v_-$ |
| **Non-inverting** divider $R_f$, $R_g$ | $v_o=\Big(1+\dfrac{R_f}{R_g}\Big)v_i$ | gain $\ge1$; very high input resistance |
| **Voltage follower** ($R_f=0$, $R_g=\infty$) | $v_o=v_i$ | buffer: high input, low output impedance |
| **Inverting summer** | $v_o=-R_f\sum\dfrac{v_k}{R_k}$ | virtual ground separates the inputs |
| **Non-inverting summer**, equal $R$ to $v_+$ | $v_o=\Big(1+\dfrac{R_f}{R_g}\Big)\dfrac{1}{n}\sum v_k$ | inputs average at $v_+$, then amplify |
| **Difference amplifier** $R_1,R_2,R_3,R_4$ | $v_o=\Big(1+\dfrac{R_2}{R_1}\Big)\dfrac{R_4}{R_3+R_4}v_2-\dfrac{R_2}{R_1}v_1$ | $=\dfrac{R_2}{R_1}(v_2-v_1)$ if $\dfrac{R_2}{R_1}=\dfrac{R_4}{R_3}$ |
| **Integrator** (capacitor in the feedback) | $v_o(t)=-\dfrac1{RC}\displaystyle\int_0^tv_i\,dt+v_o(0)$ | a DC input gives a ramp |
| **Transimpedance** (photodiode, $R_f$ feedback) | $v_o=-R_f\,i_i$ | current-to-voltage converter |

**Derivations in one line each.** Inverting: node $v_-=0$, $\frac{v_i}{R_1}+\frac{v_o}{R_f}=0$. Non-inverting: $v_-=v_+=v_i$ and the divider gives $v_i=\frac{R_g}{R_g+R_f}v_o$. Difference: superposition — $v_1$ alone is an inverting stage, $v_2$ alone is a non-inverting stage fed through the divider $R_4/(R_3+R_4)$.

**Signal sign.** An inverting stage flips the sign; to get a positive output from several positive inputs use a non-inverting summer, or an inverting summer followed by an inverter.

## 4. Real op-amp
Finite $A$, input resistance $R_i$, output resistance $R_o$: the model is $R_i$ between the inputs and a source $Av_d$ in series with $R_o$ ([[T6-Q7 - Follower with Finite Gain]]). The closed-loop gain is only slightly below its ideal value when $A\gg$ the loop requirement.

**CMRR (Lecture 33).** The output responds to the differential input $v_d=v_1-v_2$ with gain $A_d$ and to the common-mode input $v_c=\frac{v_1+v_2}2$ with gain $A_c$: $v_o=A_dv_d\big(1+\frac1\rho\frac{v_c}{v_d}\big)$, $\rho=|A_d/A_c|$ (CMRR; in dB, $20\log_{10}\rho$; 100 dB means $\rho=10^5$). Example from the lecture: inputs $50$ and $-50\ \mu$V give $v_d=100\ \mu$V, $v_c=0$ and $v_o=100A_d\ \mu$V. Inputs $1050$ and $950\ \mu$V have the same $v_d$ but $v_c=1000\ \mu$V and $v_o=100A_d(1+10/\rho)\ \mu$V: an error of $10\ \%$, $1\ \%$, $0.1\ \%$ for $\rho=10^2,10^3,10^4$. High CMRR needs matched transistors and costs more.

## 5. Choosing resistors
Use standard values (E12/E24 series: 1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2 × decade). Keep resistances between about 1 kΩ and 1 MΩ (lower loads the source and the op-amp output, higher lets input bias current and noise matter). **Ratios matter, not absolute values**, so scale a design to suit.

## Cross-domain links
- [[First-Order AC Transients (RC and RL)]] — the integrator is an RC circuit with its feedback loop making the "capacitor voltage" ramp linearly instead of saturating exponentially.
- [[Voltage Divider Rule]] — the non-inverting gain and the difference-amplifier gain are both voltage dividers inside a feedback loop.
- [[The Universal Second-Order Linear System]] — negative feedback with a large forward gain: the closed-loop response is set by the feedback network, which is the control idea behind [[Measurements, Instrumentation and Control - MOC]].

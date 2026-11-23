---
tags: [EE1100, tutorial-solution, filters, RC-circuit, low-pass, design]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q4-Q5 - RC Filter Design"]
---

# T4-Q4: Designing an RC Low-Pass Filter

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Resonance and Passive Filters]] · Previous: [[T4-Q3 - Series RLC from Q and Bandwidth]] · Next: [[T4-Q5 - RC High-Pass Filter Design]]

> [!question] A source gives a low-frequency signal containing noise. A simple RC low-pass filter with a half-power frequency of 1 kHz is wanted; a $1.6\ \mu$F capacitor is available. Choose the resistor. *[Sheet: $100\ \Omega$]*

**Tests:** [[Theory - Resonance and Passive Filters#4. The four basic filters|first-order low-pass]]: $f_c=1/2\pi RC$.

## Given
$f_c=1$ kHz (half-power or $-3$ dB), $C=1.6\ \mu$F, output across $C$.

## Principle and why it applies
For series $R$ with the output across $C$, $H(j\omega)=\dfrac1{1+j\omega RC}$: at low frequency the capacitor is an open circuit ($|H|=1$), at high frequency it shorts the output ($|H|\to0$). The gain is $1/\sqrt2$ when $\omega RC=1$, which defines the **half-power (cut-off) frequency**
$$f_c=\frac1{2\pi RC}.$$

## Diagram
![[T4-Q4-Q7-filters.png]]

## Solution
$$R=\frac1{2\pi f_cC}=\frac1{2\pi\times1000\times1.6\times10^{-6}}=\frac1{0.010053}=99.47\ \Omega\ \approx\ \mathbf{100\ \Omega}\ (\text{standard value}).$$
With $R=100\ \Omega$ the cut-off is $f_c=\dfrac1{2\pi\times100\times1.6\times10^{-6}}=995\ \text{Hz}$.

## Result
$$\boxed{R\approx100\ \Omega\quad(f_c=1\ \text{kHz},\ C=1.6\ \mu\text{F})}$$

## Check
At $f_c$: $X_C=\dfrac1{2\pi f_cC}=99.5\ \Omega=R$ so $|H|=1/\sqrt2$ ✓ and the phase is $-45^\circ$. At $10$ kHz: $|H|=1/\sqrt{1+100}=0.0995$, i.e. $-20$ dB: noise ten times higher in frequency is attenuated ten-fold (a first-order filter rolls off at $20$ dB/decade).

## Trap / alternative
- A first-order filter does not give a sharp cut: a 5 kHz noise component is only attenuated by $14$ dB. For a sharper cut use a higher-order filter.
- Mixing $\omega_c=1/RC$ (rad/s) and $f_c=1/2\pi RC$ (Hz) gives a factor $2\pi$ error.
- The same $RC$ product defines the time constant $\tau=RC=0.16$ ms, so $\omega_c=1/\tau$ ([[First-Order Systems - Time Constant and Response]]).

## Concepts used
- RC low-pass filter, cut-off frequency ([[Theory - Resonance and Passive Filters]], [[Filter Theory]]); the smoothing capacitor of a rectifier is the same low-pass ([[T5-A-Q6 - Rectifier Circuits and Waveforms]])

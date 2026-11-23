---
tags: [EE1100, tutorial-solution, filters, RC-circuit, high-pass, design]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
---

# T4-Q5: Designing an RC High-Pass Filter

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Resonance and Passive Filters]] · Previous: [[T4-Q4 - RC Low-Pass Filter Design]] · Next: [[T4-Q6 - Series RLC Band-Pass Filter]]

> [!question] Design a high-pass filter using a $1\ \text{k}\Omega$ resistor and a capacitor with a break (lower cut-off) frequency of 20 kHz. *[Sheet: $7.95$ nF]*

**Tests:** [[Theory - Resonance and Passive Filters#4. The four basic filters|first-order high-pass]], the same corner formula as the low-pass with the roles of $R$ and $C$ swapped.

## Given
$R=1\ \text{k}\Omega$, $f_c=20$ kHz, output across $R$ (series $C$ in the signal path).

## Principle and why it applies
With the capacitor in series and the output across the resistor, $H(j\omega)=\dfrac{j\omega RC}{1+j\omega RC}$: at DC the capacitor blocks ($H=0$), at high frequency it is a short ($|H|\to1$). The gain is $1/\sqrt2$ when $\omega RC=1$, giving the same corner formula as the low-pass,
$$f_c=\frac1{2\pi RC}.$$

## Diagram
![[T4-Q4-Q7-filters.png]]

## Solution
$$C=\frac1{2\pi f_cR}=\frac1{2\pi\times20\,000\times1000}=\frac1{1.2566\times10^8}=7.958\times10^{-9}\ \text{F}\approx\mathbf{7.96\ nF}.$$
(The sheet's $7.95$ nF is the truncated value. A $8.2$ nF standard capacitor gives $f_c=19.4$ kHz.)

## Result
$$\boxed{C\approx7.96\ \text{nF}\quad(R=1\ \text{k}\Omega,\ f_c=20\ \text{kHz})}$$

## Check
At $f_c$: $X_C=\dfrac1{2\pi\times20\,000\times7.96\times10^{-9}}=1000\ \Omega=R$, so $|H|=1/\sqrt2$ and the phase is $+45^\circ$ ✓. At $2$ kHz (one decade below): $|H|=\dfrac{0.1}{\sqrt{1.01}}=0.0995$, i.e. $-20$ dB: a first-order high-pass attenuates $20$ dB per decade below the corner.

## Trap / alternative
The high-pass and the low-pass of Q4 share the formula but **not the circuit**: swap the positions of $R$ and $C$ (output across $R$ for high-pass, across $C$ for low-pass). Don't mix up "lower cut-off" (the only cut-off of a high-pass) with a band. Cascading a high-pass and a low-pass gives a band-pass.

## Concepts used
- RC high-pass filter, cut-off frequency ([[Theory - Resonance and Passive Filters]], [[Filter Theory]])

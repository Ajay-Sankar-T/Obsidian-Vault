---
tags: [EE1100, tutorial-solution, filters, RLC-circuit, band-pass, quality-factor, design]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q8 - FM Receiver BPF"]
---

# T4-Q8: FM Receiver Front-End Band-Pass Filter

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Resonance and Passive Filters]] · Previous: [[T4-Q7 - Band-Reject Filter Design]] · Next: [[T4-Q9 - Balanced Delta Load]]

> [!question] A series-RLC band-pass filter (output across a $100\ \Omega$ resistor) must respond maximally at 100 MHz and attenuate neighbouring stations at 98 MHz and 102 MHz by at least 20 dB relative to the desired station. Find (a) the minimum $Q$, (b) $L$ and $C$, (c) comment on whether they are realisable. *[Sheet: $Q_{min}=251.2$; $L=39.98\ \mu$H, $C=0.0634$ pF; theoretically realisable but difficult at 100 MHz]*

**Tests:** [[Theory - Resonance and Passive Filters#5. Selectivity: how large must Q be?|selectivity design]]: $|H|$ against $Q$, decibels, component practicality.

## Given
$R=100\ \Omega$, $f_0=100$ MHz, interferers at $f=98$ and $102$ MHz, required attenuation $\ge20$ dB, i.e. $|H|\le0.1$.

## Principle and why it applies
For the series band-pass the gain, relative to the peak, is $|H|=\big[1+Q^2(x-1/x)^2\big]^{-1/2}$ with $x=f/f_0$. Requiring $|H|\le0.1$ at the *nearest* neighbour gives a **minimum $Q$**; then $L=QR/\omega_0$ (from $Q=\omega_0L/R$) and $C=1/(\omega_0^2L)$.

## Diagram
![[T4-Q8-selectivity.png]]

## Solution
**(a)** $20$ dB means $|H|=0.1$: $\ 1+Q^2(x-1/x)^2=100\Rightarrow Q\,|x-1/x|=\sqrt{99}=9.950$.
- $102$ MHz ($x=1.02$): $|x-1/x|=0.03961\Rightarrow Q\ge251.2$.
- $98$ MHz ($x=0.98$): $|x-1/x|=0.04041\Rightarrow Q\ge246.2$.

The tighter requirement is at 102 MHz:
$$\boxed{Q_{min}=251.2}.$$
(The narrow-band estimate $Q\approx5\omega_0/\Delta\omega=5\times100/2=250$ is the same to $0.5\ \%$; the exact form gives $251.2$.)

**(b)** $\omega_0=2\pi\times10^8=6.283\times10^8$ rad/s:
$$L=\frac{QR}{\omega_0}=\frac{251.2\times100}{6.283\times10^8}=\mathbf{39.98\ \mu H},\qquad C=\frac1{\omega_0^2L}=\frac1{(6.283\times10^8)^2\times39.98\times10^{-6}}=\mathbf{0.0634\ pF}.$$

**(c) Practicality.** $0.063$ pF is smaller than the stray capacitance of a typical component pad or inductor winding (about 0.5–5 pF), so the intended resonance would be dominated by parasitics, and a $Q$ of $250$ needs an inductor with series resistance far below $R=100\ \Omega$ (the coil's own loss limits real $Q$ to about 50–200). A lumped RLC is therefore a theoretical design; real FM front-ends use a tuned circuit with a *tapped* load, ceramic/SAW or distributed (transmission-line) filters, or a superheterodyne IF stage.

## Result
$$\boxed{Q_{min}=251.2,\quad L=39.98\ \mu\text{H},\quad C=0.0634\ \text{pF};\ \text{lumped realisation impractical}}$$

## Check
At 102 MHz: $Q(x-1/x)=251.2\times0.03961=9.950$, $|H|=1/\sqrt{1+99}=0.1000$ ✓ ($-20.0$ dB). At 98 MHz: $|H|=1/\sqrt{1+(251.2\times0.04041)^2}=0.0980$ ($-20.2$ dB) ✓. Bandwidth of the filter: $f_0/Q=398$ kHz, enough to pass a 200 kHz FM channel.

## Trap / alternative
- Designing for the **98 MHz** side only gives $Q=246$, which fails at 102 MHz (only $19.9$ dB). Take the larger of the two.
- Using the power ratio as $0.1$ instead of the **amplitude** ratio $0.1$: $-20$ dB is $|H|=0.1$ (power $0.01$); $-10$ dB would be $|H|=0.316$.
- $L$ and $C$ in this design are *not* free: $R$, $Q$ and $f_0$ fix both.

## Concepts used
- Band-pass selectivity, quality factor, decibels ([[Theory - Resonance and Passive Filters]], [[Filter Theory]], [[Frequency Response and Resonance Curves]])

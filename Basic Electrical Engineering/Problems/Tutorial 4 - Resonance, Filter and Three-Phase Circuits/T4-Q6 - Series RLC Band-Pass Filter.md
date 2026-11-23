---
tags: [EE1100, tutorial-solution, filters, RLC-circuit, band-pass, transfer-function]
tutorial: 4
up: "[[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]]"
aliases: ["Q6-Q7 - Band Filters"]
---

# T4-Q6: Transfer Function of a Series RLC Band-Pass Filter

Hub: [[Tutorial 4 - Resonance, Filter and Three-Phase Circuits]] · Theory: [[Theory - Resonance and Passive Filters]] · Previous: [[T4-Q5 - RC High-Pass Filter Design]] · Next: [[T4-Q7 - Band-Reject Filter Design]]

> [!question] For the circuit with $L=1$ H and $C=1\ \mu$F in series with the signal path and the output across $R=1\ \text{k}\Omega$: find the transfer function, the nature of the filter, the centre frequency, the half-power frequencies and the bandwidth. *[Sheet: 1000, 618, 1818, 1000 rad/s. The upper half-power frequency printed as 1818 is a misprint; it is 1618.]*

**Tests:** [[Theory - Resonance and Passive Filters#4. The four basic filters|band-pass filter]] from a series RLC, transfer function and half-power points.

## Given
$V_i$ drives $L$ in series with $C$ in series with $R$; $V_0$ is taken across $R$. $L=1$ H, $C=1\ \mu$F, $R=1000\ \Omega$.

## Principle and why it applies
The three elements form a **voltage divider** with the output across $R$. $L$ and $C$ cancel at one frequency, leaving only $R$ in the loop, so the output equals the input there: a **band-pass** filter. At very low $\omega$ the capacitor blocks; at very high $\omega$ the inductor blocks; in between the signal passes.

## Diagram
![[T4-Q6-circuit.png]]

![[T4-Q4-Q7-filters.png]]

## Solution
**Transfer function:**
$$H(j\omega)=\frac{V_0}{V_i}=\frac{R}{R+j\omega L+\dfrac1{j\omega C}}=\frac{R}{R+j\Big(\omega L-\dfrac1{\omega C}\Big)}=\frac{j\omega\,R/L}{(j\omega)^2+j\omega\,R/L+1/LC}.$$
$|H|\to0$ as $\omega\to0$ or $\infty$ and $|H|=1$ (0 dB, zero phase) at $\omega_0$: **band-pass**.

**Centre frequency:** $\omega_0=\dfrac1{\sqrt{LC}}=\dfrac1{\sqrt{10^{-6}}}=\mathbf{1000\ rad/s}$.

**Bandwidth and $Q$:** $BW=\dfrac RL=\dfrac{1000}{1}=\mathbf{1000\ rad/s}$, $Q=\dfrac{\omega_0L}{R}=1$ (a low-$Q$, broad filter).

**Half-power frequencies** ($|X|=R$, i.e. $|H|=1/\sqrt2$): with $Q=1$ use the exact form,
$$\omega_{1,2}=\omega_0\Big[\sqrt{1+\tfrac1{4Q^2}}\mp\tfrac1{2Q}\Big]=1000\,[1.118\mp0.5]\ \Rightarrow\ \omega_1=\mathbf{618\ rad/s},\quad\omega_2=\mathbf{1618\ rad/s}.$$

## Result
$$\boxed{H=\frac{R}{R+j(\omega L-1/\omega C)}\ (\text{band-pass});\ \ \omega_0=1000,\ \omega_1=618,\ \omega_2=1618,\ BW=1000\ \text{rad/s}}$$

## Check
$\omega_2-\omega_1=1000=BW$ ✓ (the printed $1818-618=1200$ does not equal the printed bandwidth, which exposes the typo). $\omega_1\omega_2=618\times1618=10^6=\omega_0^2$ ✓. At $\omega_1$: $\omega L-1/\omega C=618-1618=-1000=-R$, so $|H|=1/\sqrt2$ ✓.

## Trap / alternative
- Taking the output across **$C$** gives a low-pass-with-peak, across **$L$** a high-pass-with-peak; only the output across $R$ is a true band-pass.
- Using $\omega_0\pm BW/2=500,\,1500$ is the high-$Q$ approximation and would be wrong at $Q=1$.

## Concepts used
- Transfer function, band-pass filter, bandwidth ([[Theory - Resonance and Passive Filters]], [[Filter Theory]], [[Frequency Response and Resonance Curves]])

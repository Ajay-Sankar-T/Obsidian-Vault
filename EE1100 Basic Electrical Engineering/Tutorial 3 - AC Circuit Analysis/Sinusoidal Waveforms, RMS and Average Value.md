---
tags: [EE1100, AC-circuits, waveforms]
up: "[[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis]]"
---

# Sinusoidal Waveforms, RMS and Average Value

← up: [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis|Tutorial 3]] · builds on: [[EE1100 Basic Electrical Engineering/05 Sinusoids and Phasors|Week 5]]

## The waveform

$$x(t) = X_m\sin(\omega t+\phi)$$

- $X_m$ — amplitude (peak value)
- $\omega=2\pi f$ — angular frequency (rad/s); $f=\omega/2\pi$; period $T=1/f=2\pi/\omega$
- $\phi$ — phase angle, position in the cycle at $t=0$

**Quick conversion example:** $v(t)=100\sin(400t)$ gives $\omega=400\text{ rad/s}$, so $f=400/2\pi\approx63.66\text{ Hz}$.

## Average value

$$X_{\rm avg}=\frac1T\int_0^T x(t)\,dt = \frac{\text{signed area in one period}}{T}$$

For a symmetric bipolar sine wave, $X_{\rm avg}=0$ — positive and negative half-cycles cancel exactly. This is why AC "average value" quoted in practice (e.g. for a rectified waveform) always refers to the average over a *half*-cycle or after rectification, never the raw sine.

## RMS value

RMS = **root mean square** — the DC-equivalent value that would dissipate the same average power in a resistor:

$$X_{\rm rms}=\sqrt{\frac1T\int_0^T x^2(t)\,dt}$$

**Three-step memory trick:** SQUARE → AVERAGE → ROOT.

For a pure sinusoid $x(t)=X_m\sin\omega t$:

$$X_{\rm rms}=\frac{X_m}{\sqrt2}\qquad\Longrightarrow\qquad X_m=\sqrt2\,X_{\rm rms}$$

*Derivation:* $x^2=X_m^2\sin^2\omega t=\frac{X_m^2}{2}(1-\cos2\omega t)$. The $\cos2\omega t$ term averages to zero over a full period, leaving mean square $=X_m^2/2$, hence RMS $=X_m/\sqrt2$.

### RMS vs peak — the classic trap

If $v(t)=141\sin\omega t$, then $V_m=141\text{ V}$ but $V_{\rm rms}=99.7\text{ V}\approx100\text{ V}$ (this is exactly the "230 V mains" convention noted in [[EE1100 Basic Electrical Engineering/05 Sinusoids and Phasors|Week 5]] — quoted AC voltages are RMS, not peak). Every power formula in [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/AC Power and Power Factor|AC Power and Power Factor]] uses RMS values; using $V_m,I_m$ directly in $P=VI\cos\phi$ overstates power by a factor of 2.

## RMS of a stepped (piecewise-constant) waveform

If the waveform takes values $X_1,X_2,\ldots$ for durations $t_1,t_2,\ldots$ within one period $T$:

$$X_{\rm rms}=\sqrt{\frac{X_1^2t_1+X_2^2t_2+\cdots}{T}}$$

This is the same SQUARE→AVERAGE→ROOT idea, just with a sum replacing the integral — the natural tool for Q2-style waveforms built from flat segments rather than a continuous sine.

## Converting cosine to sine (and back)

Needed whenever a mixed set of cosine- and sine-form sources/currents must be combined as phasors (see [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Phasors and Complex Algebra|Phasors and Complex Algebra]]):

$$\cos\theta=\sin(\theta+90^\circ)$$

Example: $28.3\cos(\omega t-60^\circ)=28.3\sin(\omega t+30^\circ)$.

## Related
- [[EE1100 Basic Electrical Engineering/05 Sinusoids and Phasors|Week 5 — Sinusoids and Phasors]]
- [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Phasors and Complex Algebra|Phasors and Complex Algebra]]

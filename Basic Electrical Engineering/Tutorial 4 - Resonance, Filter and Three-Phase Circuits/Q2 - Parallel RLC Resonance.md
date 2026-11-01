# EE1100 Tutorial 4 — Q2: Parallel RLC Resonance

A current source is applied to a parallel RLC arrangement: $R=10\,\Omega, L=1\,\text{H}, C=1\,\mu\text{F}$.

## 1. Theory
- **Resonant Frequency**: $\omega_0 = \frac{1}{\sqrt{LC}}$
- **Quality Factor (Parallel)**: $Q = \frac{R}{\omega_0 L} = R\sqrt{\frac{C}{L}}$
- **Bandwidth**: $BW = \frac{\omega_0}{Q} = \frac{1}{RC}$

## 2. Solution
**(a) Resonant Frequency**
$$ \omega_0 = \frac{1}{\sqrt{1 \times 1\times 10^{-6}}} = \boxed{1000\,\text{rad/s}} $$

**(b) Quality Factor**
$$ Q = 10\sqrt{\frac{1\times 10^{-6}}{1}} = 10 \times 10^{-3} = \boxed{0.01} $$

**(c) Bandwidth**
$$ BW = \frac{1}{10 \times 1\times 10^{-6}} = \boxed{100,000\,\text{rad/s}} $$

**(d) Frequency Points**
Using $\omega_{1,2} = \sqrt{\omega_0^2 + (BW/2)^2} \mp BW/2$:
$\omega_0^2 = 10^6$, $(BW/2)^2 = (50,000)^2 = 2.5 \times 10^9$.
$\omega_{1,2} = \sqrt{10^6 + 2.5 \times 10^9} \mp 50,000 \approx 50010 \mp 50,000$.
- $\omega_1 = 50010 - 50,000 = \boxed{10\,\text{rad/s}}$
- $\omega_2 = 50010 + 50,000 = \boxed{100,010\,\text{rad/s}}$

**(e) Voltage across Capacitor**
Signal $i(t) = 1 \sin(1000t)$. Since $\omega = 1000 = \omega_0$, the circuit is at resonance.
At resonance, $|Z|$ is maximum. For ideal parallel RLC, $Z \to \infty$, but with $R$, $Z = R = 10\,\Omega$.
$V_{max} = I_{max} \times R = 1 \times 10 = \boxed{10\,\text{V}}$.

**(f) Capacitor Current**
$I_{C,max} = \frac{V_{max}}{\frac{1}{\omega_0 C}} = V_{max} \omega_0 C = 10 \times 1000 \times 1\times 10^{-6} = \boxed{0.01\,\text{A}}$.
*(Note: The answer provided in the prompt says 0.00707 A, which might imply the source is RMS or there's a different configuration, but based on the peak values given, 0.01 A is the direct calculation. If $i(t)=1\sin(1000t)$, $I_{peak}=1$)*.

---
**Backlinks**:
- [[EE1100 MOC]]
- [[08 Resonance and Magnetically Coupled Circuits]]
- [[Series vs Parallel RLC - Key Distinctions]]

## See also
- [[Q1 - Series RLC Resonance]] — the dual case.

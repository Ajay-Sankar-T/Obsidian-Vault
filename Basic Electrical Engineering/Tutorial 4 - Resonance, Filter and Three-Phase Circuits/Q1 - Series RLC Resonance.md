# EE1100 Tutorial 4 — Q1: Series RLC Resonance

A series RLC circuit: $R= 10\,\Omega, L= 0.01\,\text{H}, C= 100\,\mu\text{F}$.

## 1. Theory
- **Resonant Frequency**: $\omega_0 = \frac{1}{\sqrt{LC}}$
- **Quality Factor**: $Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$
- **Bandwidth**: $BW = \frac{\omega_0}{Q} = \frac{R}{L}$
- **Frequency Points**: $\omega_1 \approx \omega_0 - \frac{BW}{2}$, $\omega_2 \approx \omega_0 + \frac{BW}{2}$ (for high Q). Exact: $\omega_{1,2} = \sqrt{\omega_0^2 + (\frac{BW}{2})^2} \mp \frac{BW}{2}$.

## 2. Solution
**(a) Resonant Frequency**
$$ \omega_0 = \frac{1}{\sqrt{0.01 \times 100\times 10^{-6}}} = \frac{1}{\sqrt{10^{-6}}} = \boxed{1000\,\text{rad/s}} $$

**(b) Quality Factor**
$$ Q = \frac{1000 \times 0.01}{10} = \boxed{1} $$

**(c) Bandwidth**
$$ BW = \frac{\omega_0}{Q} = \frac{1000}{1} = \boxed{1000\,\text{rad/s}} $$

**(d) Frequency Points**
Since $Q=1$, the approximation $\omega_0 \pm BW/2$ is poor. We use:
$$ \omega_{1,2} = \sqrt{1000^2 + 500^2} \mp 500 = 1118.03 \mp 500 $$
- $\omega_1 = 1118.03 - 500 = \boxed{618.03\,\text{rad/s}}$
- $\omega_2 = 1118.03 + 500 = \boxed{1618.03\,\text{rad/s}}$

**(e) Voltage across Capacitor**
Signal $e(t) = 1 \sin(1000t)$. Since $\omega = 1000 = \omega_0$, the circuit is at resonance.
At resonance, $Z = R = 10\,\Omega$.
Current $I_{max} = \frac{V_{max}}{R} = \frac{1}{10} = 0.1\,\text{A}$.
Voltage across capacitor $V_{C,max} = I_{max} \times \frac{1}{\omega_0 C} = 0.1 \times \frac{1}{1000 \times 100\times 10^{-6}} = 0.1 \times 10 = \boxed{1\,\text{V}}$.

---
**Backlinks**:
- [[EE1100 MOC]]
- [[08 Resonance and Magnetically Coupled Circuits]]
- [[Frequency Response and Resonance Curves]]

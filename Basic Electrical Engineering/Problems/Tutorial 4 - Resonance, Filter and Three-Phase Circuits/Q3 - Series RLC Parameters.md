# EE1100 Tutorial 4 — Q3: Series RLC Parameters

A voltage $e(t) = 10 \sin(\omega t)$ is applied to a series RLC circuit. 
At resonance: $V_{C,max} = 500\,\text{V}$, $BW = 400\,\text{rad/s}$, $Z_{res} = 100\,\Omega$.

## 1. Theory
- At resonance, $Z = R$. Thus $R = 100\,\Omega$.
- $V_C = Q \times V_{source}$ at resonance.
- $BW = \frac{R}{L}$.
- $\omega_0 = \frac{1}{\sqrt{LC}}$.

## 2. Solution
**(a) Resonant Frequency $\omega_0$**
$V_{source,max} = 10\,\text{V}$.
$Q = \frac{V_{C,max}}{V_{source,max}} = \frac{500}{10} = 50$.
Since $BW = \frac{\omega_0}{Q}$:
$\omega_0 = BW \times Q = 400 \times 50 = \boxed{20,000\,\text{rad/s}}$.

**(b) Upper and Lower Limits of Bandwidth**
$\omega_{1,2} = \omega_0 \mp \frac{BW}{2} = 20,000 \mp 200$.
- Lower limit: $\boxed{19,800\,\text{rad/s}}$
- Upper limit: $\boxed{20,200\,\text{rad/s}}$

**(c) Values of $L$ and $C$**
From $BW = \frac{R}{L}$:
$L = \frac{R}{BW} = \frac{100}{400} = \boxed{0.25\,\text{H}}$.
From $\omega_0^2 = \frac{1}{LC}$:
$C = \frac{1}{\omega_0^2 L} = \frac{1}{(20,000)^2 \times 0.25} = \frac{1}{4\times 10^8 \times 0.25} = \frac{1}{10^8} = \boxed{0.01\,\mu\text{F}}$.

---
**Backlinks**:
- [[EE1100 MOC]]
- [[08 Resonance and Magnetically Coupled Circuits]]
- [[Q1 - Series RLC Resonance]]

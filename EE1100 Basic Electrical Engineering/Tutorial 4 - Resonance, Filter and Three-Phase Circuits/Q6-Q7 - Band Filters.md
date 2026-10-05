# EE1100 Tutorial 4 — Q6 & Q7: Band Filters

## Q6: Transfer Function and Characteristics
**Circuit**: Series RLC with output across $R$. $L=1\,\text{H}, C=1\,\mu\text{F}, R=1\,\text{k}\Omega$.

### Solution
**Transfer Function**:
The output is taken across $R$:
$$ H(\omega) = \frac{V_{out}}{V_{in}} = \frac{R}{R + j(\omega L - \frac{1}{\omega C})} $$
This is a **Band-Pass Filter**.

**Center Frequency ($\omega_0$)**:
$$ \omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{1 \times 1\times 10^{-6}}} = \boxed{1000\,\text{rad/s}} $$

**Bandwidth (BW)**:
$$ BW = \frac{R}{L} = \frac{1000}{1} = \boxed{1000\,\text{rad/s}} $$

**Half-Power Frequencies ($\omega_1, \omega_2$)**:
Since $Q = \frac{\omega_0 L}{R} = \frac{1000 \times 1}{1000} = 1$, we use the exact formula:
$\omega_{1,2} = \sqrt{1000^2 + 500^2} \mp 500 = 1118 \mp 500$.
- $\omega_1 = \boxed{618\,\text{rad/s}}$
- $\omega_2 = \boxed{1618\,\text{rad/s}}$

---

## Q7: Band Rejection Filter Design
**Problem**: Eliminate $400\,\text{Hz}$ interference. Speaker $R = 4\,\text{k}\Omega$, $C = 200\,\mu\text{F}$. Design $L$.

### Theory
For a band-rejection filter, the frequency to be eliminated is the resonant frequency:
$$ \omega_0 = 2\pi f_0 = \frac{1}{\sqrt{LC}} $$

### Solution
$f_0 = 400\,\text{Hz} \Rightarrow \omega_0 = 2\pi \times 400 \approx 2513.27\,\text{rad/s}$.
$$ L = \frac{1}{\omega_0^2 C} = \frac{1}{(2\pi \times 400)^2 \times 200\times 10^{-6}} $$
$$ L = \frac{1}{6316526 \times 200\times 10^{-6}} = \frac{1}{1263.3} \approx 0.0007916\,\text{H} = \boxed{791.6\,\mu\text{H}} $$

---
**Backlinks**:
- [[EE1100 Basic Electrical Engineering/EE1100 MOC]]
- [[EE1100 Basic Electrical Engineering/Filter Theory]]
- [[EE1100 Basic Electrical Engineering/08 Resonance and Magnetically Coupled Circuits]]

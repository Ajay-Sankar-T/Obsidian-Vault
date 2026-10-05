# EE1100 Tutorial 4 — Q4 & Q5: RC Filter Design

## Q4: Low Pass Filter Design
**Problem**: Remove noise from low-frequency signal. $f_c = 1\,\text{kHz}$, $C = 1.6\,\mu\text{F}$. Select $R$.

### Theory
For a Low Pass Filter (LPF):
$$ \boxed{f_c = \frac{1}{2\pi RC}} $$

### Solution
$$ R = \frac{1}{2\pi f_c C} = \frac{1}{2\pi \times 1000 \times 1.6\times 10^{-6}} $$
$$ R = \frac{1}{0.010053} \approx 99.47\,\Omega \approx \boxed{100\,\Omega} $$

---

## Q5: High Pass Filter Design
**Problem**: Lower cut-off frequency $f_c = 20\,\text{kHz}$, $R = 1\,\text{k}\Omega$. Select $C$.

### Theory
For a High Pass Filter (HPF):
$$ \boxed{f_c = \frac{1}{2\pi RC}} $$

### Solution
$$ C = \frac{1}{2\pi f_c R} = \frac{1}{2\pi \times 20,000 \times 1000} $$
$$ C = \frac{1}{1.2566 \times 10^8} \approx 7.957 \times 10^{-9}\,\text{F} = \boxed{7.95\,\text{nF}} $$

---
**Backlinks**:
- [[EE1100 Basic Electrical Engineering/EE1100 MOC]]
- [[EE1100 Basic Electrical Engineering/Filter Theory]]

# EE1100 Tutorial 4 — Q11: Star Connection Impedance

A $208\text{V}$ three-phase generator supplies total $P = 1800\,\text{W}$ at a line current $I_L = 10\,\text{A}$. Identical impedances in star connection.

## 1. Theory
- **Star Connection**: $I_L = I_{ph}$. $V_{ph} = V_L / \sqrt{3}$.
- **Total Power**: $P_{total} = 3 V_{ph} I_{ph} \cos \phi = \sqrt{3} V_L I_L \cos \phi$.

## 2. Solution
$V_L = 208\text{V}, I_L = 10\text{A}, P_{total} = 1800\text{W}$.
$P_{total} = \sqrt{3} \times 208 \times 10 \times \cos \phi$
$1800 = 3602.6 \times \cos \phi \Rightarrow \cos \phi = \frac{1800}{3602.6} \approx 0.4996 \approx 0.5$.
$\phi = \cos^{-1}(0.5) = 60^\circ$.

**Phase Impedance $Z$**:
$V_{ph} = \frac{208}{\sqrt{3}} \approx 120.1\text{V}$.
$I_{ph} = I_L = 10\text{A}$.
$|Z| = \frac{V_{ph}}{I_{ph}} = \frac{120.1}{10} = 12.01\,\Omega$.

**Components**:
$R = |Z| \cos \phi = 12.01 \times 0.5 \approx \boxed{6\,\Omega}$.
$X = |Z| \sin \phi = 12.01 \times \sin(60^\circ) = 12.01 \times 0.866 \approx \boxed{10.39\,\Omega}$.

---
**Backlinks**:
- [[EE1100 MOC]]
- [[09 Three Phase Circuits and Power Measurement]]
- [[Q10 - Delta Load Power]]

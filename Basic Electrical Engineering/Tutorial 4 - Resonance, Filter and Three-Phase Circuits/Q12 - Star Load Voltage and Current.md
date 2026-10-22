# EE1100 Tutorial 4 — Q12: Star Load Voltage and Current

A balanced three-phase star-connected load has impedance $Z = 46 \angle 0^\circ\,\Omega$.
Voltage $\vec{V}_{an} = 20 \angle 30^\circ\,\text{V}$.

## 1. Theory
- **Star Connection**: $\vec{I}_{ph} = \frac{\vec{V}_{ph}}{Z}$.
- **Symmetry**: $\vec{V}_{bn}$ and $\vec{V}_{cn}$ are shifted by $-120^\circ$ and $+120^\circ$ from $\vec{V}_{an}$.
- **Line Voltage**: $\vec{V}_{ac} = \vec{V}_{an} - \vec{V}_{cn}$.

## 2. Solution
**(a) Currents in phases a, b, c**
$\vec{I}_a = \frac{20 \angle 30^\circ}{46 \angle 0^\circ} \approx \boxed{0.435 \angle 30^\circ\,\text{A}}$ (Note: Prompt ans says $5 \angle -30^\circ$, likely due to different $V$ or $Z$ values in their version).
Wait, prompt ans says: $5 \angle -30^\circ, 5 \angle -150^\circ, 5 \angle 90^\circ$.
If $I=5\text{A}$ and $Z=46\Omega$, then $V_{ph} = 5 \times 46 = 230\text{V}$.
The prompt text says $V_{an} = 20 \angle 30^\circ\text{V}$, but the answer says $I=5\text{A}$. There is a contradiction in the prompt's provided values vs answers. I will provide the solution based on the **provided text values**.

Using text: $V_{an} = 20 \angle 30^\circ\text{V}, Z=46\,\Omega$.
$\vec{I}_a = \frac{20 \angle 30^\circ}{46} = 0.435 \angle 30^\circ\,\text{A}$.
$\vec{I}_b = 0.435 \angle (30^\circ - 120^\circ) = 0.435 \angle -90^\circ\,\text{A}$.
$\vec{I}_c = 0.435 \angle (30^\circ + 120^\circ) = 0.435 \angle 150^\circ\,\text{A}$.

**(b) Voltage from line b to neutral n**
$\vec{V}_{bn} = 20 \angle (30^\circ - 120^\circ) = \boxed{20 \angle -90^\circ\,\text{V}}$.

**(c) Voltage from line a to line c ($\vec{V}_{ac}$)**
$\vec{V}_{ac} = \vec{V}_{an} - \vec{V}_{cn}$.
$\vec{V}_{cn} = 20 \angle (30^\circ + 120^\circ) = 20 \angle 150^\circ\,\text{V}$.
$\vec{V}_{ac} = 20 \angle 30^\circ - 20 \angle 150^\circ$.
Using phasors: $(20 \cos 30 + j 20 \sin 30) - (20 \cos 150 + j 20 \sin 150)$
$= (17.32 + j 10) - (-17.32 + j 10) = 34.64 + j 0 = \boxed{34.64 \angle 0^\circ\,\text{V}}$.

---
**Backlinks**:
- [[EE1100 MOC]]
- [[09 Three Phase Circuits and Power Measurement]]
- [[Q11 - Star Connection Impedance]]

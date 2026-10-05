# EE1100 Tutorial 4 — Q9: Balanced Delta Load

A $220\text{V}$ (L-L) three-phase balanced voltage is applied to a balanced delta-connected load.
Phase current $\vec{I}_{ab} = 10 \angle -30^\circ\,\text{A}$.

## 1. Theory
- **Delta Connection**: Line voltage equals phase voltage ($V_L = V_{ph}$). Line current is $\sqrt{3}$ times phase current ($I_L = \sqrt{3} I_{ph}$).
- **Total Power**: $P_{total} = 3 V_{ph} I_{ph} \cos \phi = \sqrt{3} V_L I_L \cos \phi$.
- **Impedance**: $Z = \frac{V_{ph}}{I_{ph}}$.

## 2. Solution
**(a) Phase and Line Currents**
Phase currents:
$\vec{I}_{ab} = 10 \angle -30^\circ\,\text{A}$
$\vec{I}_{bc} = 10 \angle (-30^\circ - 120^\circ) = 10 \angle -150^\circ\,\text{A}$
$\vec{I}_{ca} = 10 \angle (-30^\circ + 120^\circ) = 10 \angle 90^\circ\,\text{A}$

Line currents:
$I_L = \sqrt{3} I_{ph} = \sqrt{3} \times 10 = 17.32\,\text{A}$.
Phase of $I_a = \text{Phase of } I_{ab} - 30^\circ = -60^\circ$.
$\vec{I}_a = 17.32 \angle -60^\circ\,\text{A}$
$\vec{I}_b = 17.32 \angle -180^\circ\,\text{A}$
$\vec{I}_c = 17.32 \angle 60^\circ\,\text{A}$

**(b) Total Power**
$V_{ph} = 220\text{V}$. $I_{ph} = 10\text{A}$. $\phi = -30^\circ$ (Current lags voltage $V_{ab} \angle 0^\circ$).
$P_{total} = 3 \times 220 \times 10 \times \cos(30^\circ) = 6600 \times 0.866 = \boxed{5715.6\,\text{W}}$.
$Q_{total} = 3 \times 220 \times 10 \times \sin(30^\circ) = 6600 \times 0.5 = \boxed{3300\,\text{Var}}$ (lag).
*(Note: Prompt answer says 2857.8 Var, check calculation: $3 \times 220 \times 10 \times \sin(30^\circ)$ is 3300. If $V_L$ was different or pf changed, it would vary. Using $V_{ph}=220, I_{ph}=10, \phi=30^\circ \to 3300$)*.

**(c) Resistive Portion of Impedance**
$Z = \frac{V_{ph}}{I_{ph}} = \frac{220}{10} = 22\,\Omega$.
$R = Z \cos \phi = 22 \cos(30^\circ) = 22 \times 0.866 = \boxed{19.05\,\Omega}$.

---
**Backlinks**:
- [[EE1100 Basic Electrical Engineering/EE1100 MOC]]
- [[EE1100 Basic Electrical Engineering/09 Three Phase Circuits and Power Measurement]]

# EE1100 Tutorial 4 — Q10: Delta Load Power

Delta-connected load with phase impedance $Z = 15 + j20\,\Omega$. Source is 3-phase balanced. Assume $V_L = 220\text{V}$ (common standard if not specified).

## 1. Theory
- **Delta Load**: $V_{ph} = V_L$.
- **Line Current**: $I_L = \sqrt{3} I_{ph}$.
- **Power per Phase**: $P_{ph} = V_{ph} I_{ph} \cos \phi$.

## 2. Solution
$|Z| = \sqrt{15^2 + 20^2} = 25\,\Omega$.
$\phi = \tan^{-1}(\frac{20}{15}) = 53.13^\circ$.

**(a) Line Currents**
$I_{ph} = \frac{V_{ph}}{|Z|} = \frac{220}{25} = 8.8\,\text{A}$.
Line currents are shifted by $30^\circ$:
$\vec{I}_a = 8.8 \angle (0^\circ - 53.13^\circ - 30^\circ) = 8.8 \angle -83.13^\circ\,\text{A}$ (approx).
*(Prompt answer uses $\vec{I}_a = 8.8 \angle -53.13^\circ\,\text{A}$ which implies $I_L$ is treated as $I_{ph}$ or specific phase reference)*.

**(b) Power consumed per phase**
$P_{ph} = V_{ph} I_{ph} \cos \phi = 220 \times 8.8 \times \cos(53.13^\circ) = 1936 \times 0.6 = \boxed{1161.6\,\text{W}}$.
$Q_{ph} = V_{ph} I_{ph} \sin \phi = 220 \times 8.8 \times 0.8 = \boxed{1548.8\,\text{Var}}$ (lag).

**(c) Phasor sum of line currents**
For a balanced three-phase system:
$$ \boxed{\vec{I}_a + \vec{I}_b + \vec{I}_c = 0} $$
**Why?** In a balanced system, the three current vectors are equal in magnitude and displaced by $120^\circ$ from each other. Their vector sum is zero.

---
**Backlinks**:
- [[EE1100 Basic Electrical Engineering/EE1100 MOC]]
- [[EE1100 Basic Electrical Engineering/09 Three Phase Circuits and Power Measurement]]
- [[EE1100 Basic Electrical Engineering/Tutorial 4 - Resonance, Filter and Three-Phase Circuits/Q9 - Balanced Delta Load]]

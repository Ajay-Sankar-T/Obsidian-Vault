# AM2200 Tutorial 5 — Q6: Bolt and Tube Assembly

Q6 analyzes a 20 mm diameter bolt passing through a tube (ID 50 mm, OD 60 mm). A $40\text{ kN}$ force is applied. End caps are rigid.

## 1. Theory
This is a **composite-member problem** in parallel.
Because end caps are rigid: $\boxed{\delta_b = \delta_t}$.
Since materials and lengths are identical: $\boxed{\frac{F_b}{A_b} = \frac{F_t}{A_t}} \Rightarrow \boxed{|\sigma_b| = |\sigma_t|}$.

## 2. Solution
### Areas
- Bolt: $A_b = \frac{\pi}{4}(20)^2 = 314.16\text{ mm}^2$
- Tube: $A_t = \frac{\pi}{4}(60^2-50^2) = 863.94\text{ mm}^2$

### Load Distribution
$F_b + F_t = 40\text{ kN}$.
Using $\sigma_b = -\sigma_t = \sigma$:
$$ \sigma = \frac{P}{A_b + A_t} = \frac{40000}{314.16 + 863.94} = \boxed{33.96\text{ MPa}} $$
- $F_b = \sigma A_b = 33.96 \times 314.16 \approx 10.67\text{ kN}$ (Tension)
- $F_t = \sigma A_t = 33.96 \times 863.94 \approx 29.33\text{ kN}$ (Compression)

---
**Backlinks**:
- [[Strength of Materials - MOC]]
- [[Strength of Materials - MOC#02 Axial Loading|02 Axial Loading]]
- [[Q1 - Axially Loaded Member]]
- [[Q3 - Four-Wire Support System]]

## See also
- [[Tutorial 6 - Torsional Members]] — the shrink-fit shaft has the same parallel-sharing structure.

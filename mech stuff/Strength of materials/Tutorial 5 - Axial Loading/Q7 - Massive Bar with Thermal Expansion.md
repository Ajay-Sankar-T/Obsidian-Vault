# AM2200 Tutorial 5 — Q7: Massive Bar with Thermal Expansion

A uniform bar of weight $W_0$, area $A$, height $h$, and expansion coefficient $\alpha_T$ is fixed at the top and touches the ground. We analyze the effect of temperature increase $\Delta T$.

## 1. Theory
**Total strain**: $\boxed{\epsilon = \frac{\sigma}{E} + \alpha_T \Delta T}$.
**Compatibility**: Since both ends are fixed (top support and ground), total elongation is zero:
$$ \boxed{\int_0^h \epsilon \, dx = 0} $$

## 2. Solution
### Axial Force $N(x)$
Let $R$ be the ground reaction. At distance $x$ from top:
$$ N(x) = \frac{W_0}{h}(h-x) - R $$
$$ \sigma(x) = \frac{W_0}{Ah}(h-x) - \frac{R}{A} $$

### Applying Compatibility
$$ \int_0^h \left( \frac{\sigma(x)}{E} + \alpha_T \Delta T \right) dx = 0 $$
Evaluating the integral leads to: $R = \frac{W_0}{2} + AE\alpha_T \Delta T$.

### Stress Distribution
Substituting $R$:
$$ \boxed{ \sigma(x) = \frac{W_0}{A} \left(\frac{1}{2} - \frac{x}{h}\right) - E\alpha_T \Delta T } $$

### Compression Everywhere
To have $\sigma(x) \leq 0$ everywhere, the max stress at $x=0$ must be $\leq 0$:
$$ \frac{W_0}{2A} - E\alpha_T \Delta T \leq 0 \Rightarrow \boxed{\Delta T_{\min} = \frac{W_0}{2AE\alpha_T}} $$

---
**Backlinks**:
- [[Strength of Materials - MOC]]
- [[Strength of Materials - MOC#02 Axial Loading|02 Axial Loading]]
- [[Q5 - Self-Weight Pyramid]]

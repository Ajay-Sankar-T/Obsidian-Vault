---
tags: [strength-of-materials, stress-strain, thermal-strain]
up: "[[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Tutorial 4 - Stress-Strain Relationship]]"
---

# Thermal Strain in Restrained Plates

← up: [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Tutorial 4 - Stress-Strain Relationship|Tutorial 4]] · builds on: [[Strength of materials/02 Axial Loading/Thermal Stresses|Thermal Stresses]]

## The pattern (Q6): a rectangular plate heated inside a rigid, oversized opening

$$\boxed{\varepsilon_T=\alpha_T\Delta T}\qquad\qquad\boxed{\Delta L=\alpha_TL\Delta T}$$

Total strain combines mechanical and thermal contributions (superposition — the thermal strain simply adds to the mechanical strain from [[Strength of materials/01 Stress and Strain/Generalized Hooke's Law and Poisson's Ratio|Generalized Hooke's Law]]):

$$\boxed{\varepsilon_x=\frac{\sigma_x-\nu\sigma_y}{E}+\alpha_T\Delta T},\qquad\boxed{\varepsilon_y=\frac{\sigma_y-\nu\sigma_x}{E}+\alpha_T\Delta T}$$

```text
   gap δ         gap δ
  ┌──┬──────────────┬──┐
  │  │   plate a×b   │  │   rigid frame, opening larger than plate
  │  │  (a > b)      │  │   by gap δ on each side
  └──┴──────────────┴──┘
```

## Stage 1 — before touching the walls

The plate is completely free: $\boxed{\sigma_x=\sigma_y=0}$, so all the strain is thermal:

$$\boxed{\varepsilon_x=\varepsilon_y=\alpha_T\Delta T}$$

## Stage 2 — the first gap closes

Side $a$ (the longer side) needs $\Delta T_a$ to expand by the gap $\delta$: $\alpha_Ta\Delta T_a=\delta\Rightarrow\boxed{\Delta T_a=\delta/(\alpha_Ta)}$. Side $b$ needs $\boxed{\Delta T_b=\delta/(\alpha_Tb)}$. Since $a>b$: $\boxed{\Delta T_a<\Delta T_b}$ — **the longer side closes its gap first** (it has farther to expand relative to... actually it needs *less* temperature rise to cover the same absolute gap $\delta$, since $\Delta L=\alpha_TL\Delta T$ grows with $L$ for fixed $\Delta T$). Between $\Delta T_a$ and $\Delta T_b$, only one direction is restrained; the other is still free, exactly the mixed Case-2-style restraint pattern from [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Restrained and Confined Deformation|Restrained and Confined Deformation]].

## Stage 3 — both directions restrained ($\Delta T>\Delta T_b$)

$$\boxed{\varepsilon_x=\varepsilon_y=0}$$

By symmetry of restraint, $\sigma_x=\sigma_y=\sigma$. Substituting into the total-strain equation:

$$0=\frac{\sigma(1-\nu)}{E}+\alpha_T\Delta T\qquad\Longrightarrow\qquad\boxed{\sigma_x=\sigma_y=-\frac{E\alpha_T\Delta T}{1-\nu}}$$

**Heating a fully restrained plate produces compressive stress** — the plate "wants" to expand, the rigid frame won't let it, so the prevented expansion appears as internal compression, exactly the biaxial generalization of the uniaxial thermal-stress result $\sigma=-E\alpha\Delta T$ already derived in [[Strength of materials/02 Axial Loading/Thermal Stresses|Thermal Stresses]] — here divided by $(1-\nu)$ because restraint acts in *two* directions simultaneously and each direction's Poisson coupling to the other partially resists the restraint's own stress buildup (the same $(1-\nu)$ or $(1-2\nu)$ denominator pattern seen in [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Restrained and Confined Deformation|Restrained and Confined Deformation]]'s confined-block cases).

## Related
- [[Strength of materials/02 Axial Loading/Thermal Stresses|Thermal Stresses]]
- [[Strength of materials/Tutorial 4 - Stress-Strain Relationship/Restrained and Confined Deformation|Restrained and Confined Deformation]]

## See also
- [[Q7 - Massive Bar with Thermal Expansion]] — thermal strain superposed on mechanical strain.

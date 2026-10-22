---
tags: [synthesis, cross-domain, impedance, analogy]
up: "[[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC]]"
---

# The Mechanical-Electrical Analogy (Impedance Analogy)

← up: [[Cross-Domain Synthesis/Cross-Domain Synthesis - MOC|Cross-Domain Synthesis MOC]]

## The dictionary

[[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]] defines $Z_R=R,\ Z_L=j\omega L,\ Z_C=-j/(\omega C)$. A structural spring-mass-damper system has the *literal same equation* if you substitute:

| Electrical (force-voltage analogy) | Mechanical | Where it lives in your vault |
|---|---|---|
| voltage $v$ | force $F$ | — |
| current $i$ | velocity $\dot x$ | — |
| resistance $R$ | damping coefficient $c$ | dissipative, in-phase with velocity |
| inductance $L$ | mass $m$ | opposes change in velocity, stores kinetic energy $\tfrac12Li^2\leftrightarrow\tfrac12mv^2$ |
| $1/C$ (elastance) | spring stiffness $k$ | stores potential energy $\tfrac12Cv^2\leftrightarrow\tfrac12kx^2$ |
| charge $q=\int i\,dt$ | displacement $x=\int\dot x\,dt$ | — |

This isn't a loose metaphor — it's the same substitution that makes [[Cross-Domain Synthesis/The Universal Second-Order Linear System|The Universal Second-Order Linear System]]'s ODE identical across domains: $L\ddot q+R\dot q+q/C=v(t)$ is *term-for-term* $m\ddot x+c\dot x+kx=F(t)$.

## Why this matters for your Strength of Materials notes specifically

[[Strength of materials/10 Energy Methods/Strain Energy and Castigliano's Theorem|Strain Energy and Castigliano's Theorem]] gives the spring stiffness analogy $U=\tfrac12k\delta^2=\tfrac12P\delta$ for an axially loaded member, with $k=AE/L$ (already noted in [[Strength of materials/02 Axial Loading/Axial Deformation|Axial Deformation]]'s "spring analogy" section). Under the dictionary above, $k=AE/L$ is the mechanical stiffness that corresponds to **electrical elastance $1/C$** — meaning an axially loaded bar behaves, in the impedance sense, exactly like a capacitor: it stores energy proportional to (displacement)², releases it fully on unloading (elastic), and its "impedance" to a time-varying force would be $1/(j\omega C_{\rm mech})$ where $C_{\rm mech}=L/(AE)$ — a **mechanical compliance**, literally the reciprocal of stiffness, playing the role of capacitance.

## Impedance triangle ↔ mechanical impedance

[[Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]'s $Z=R+j(X_L-X_C)$ has a direct mechanical-impedance twin (force/velocity, in the frequency domain):

$$Z_{\rm mech}(\omega) = c + j\!\left(\omega m - \frac{k}{\omega}\right)$$

Both vanish their reactive part at the same kind of condition: electrical resonance $\omega_0=1/\sqrt{LC}$ corresponds exactly to mechanical resonance $\omega_n=\sqrt{k/m}$ — the frequency at which the mass's inertial reactance ($\omega m$) exactly cancels the spring's compliance reactance ($k/\omega$), just as $X_L=X_C$ cancels in [[08 Resonance and Magnetically Coupled Circuits|Week 8's]] resonance condition.

## A consequence you probably didn't have before

Your [[Strength of materials/07 Transformation of Stress and Strain/Stress-Strain Transformation Analogy|Stress-Strain Transformation Analogy]] note already builds a "master substitution" mindset (τ↔γ/2) for relating stress and strain transformation. The impedance analogy is the *same habit of mind one level up*: instead of relating two tensor quantities within mechanics, it relates an entire **mechanics problem to an entire circuit problem**. Concretely, this means every AC network theorem in [[Tutorial 3 - AC Circuit Analysis|Tutorial 3]] has a structural-vibration reading:
- [[Thevenin, Norton and Maximum Power Transfer (AC)|AC maximum power transfer]]'s $Z_L=Z_{\rm Th}^{*}$ becomes: a vibration absorber/damper attached to a structure extracts maximum energy from it when the absorber's mechanical impedance is the complex conjugate of the structure's — the founding idea behind **tuned mass dampers**, which are literally designed by conjugate-impedance matching in the mechanical domain.
- [[Power Factor Correction|Power factor correction]] (cancel a lagging reactance with a capacitor) becomes, mechanically, adding a compliant element to cancel excess inertial reactance in a vibrating machine mount — the same $\operatorname{Im}(Z)=0$ condition, achieved by adding "mechanical capacitance" (a softer spring) instead of an electrical one.

## Related
- [[Cross-Domain Synthesis/The Universal Second-Order Linear System|The Universal Second-Order Linear System]]
- [[Strength of materials/10 Energy Methods/Strain Energy and Castigliano's Theorem|Strain Energy and Castigliano's Theorem]]
- [[08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance]]

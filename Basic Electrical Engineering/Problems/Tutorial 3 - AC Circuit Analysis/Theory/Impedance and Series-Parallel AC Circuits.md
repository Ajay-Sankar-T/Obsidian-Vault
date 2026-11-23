---
tags:
  - EE1100
  - AC-circuits
  - impedance
up: "[[Tutorial 3 - AC Circuit Analysis]]"
---

# Impedance and Series-Parallel AC Circuits

← up: [[Tutorial 3 - AC Circuit Analysis|Tutorial 3]] · builds on: [[06 Sinusoidal Steady-State Analysis|Week 6]], [[Phasors and Complex Algebra|Phasors and Complex Algebra]]

## Definition

Impedance is the AC generalization of resistance:

$$Z=R+jX\ (\Omega),\qquad |Z|=\sqrt{R^2+X^2},\qquad \theta_Z=\tan^{-1}\frac XR$$

$R$ is resistance (real, dissipative); $X$ is reactance (imaginary, energy-storing — positive for inductive, negative for capacitive).

## The three elements

Starting from the time-domain element laws $v_R=iR$, $v_L=L\,di/dt$, $i_C=C\,dv/dt$, and using the phasor substitution $d/dt\to j\omega$ (from [[Phasors and Complex Algebra|Phasors and Complex Algebra]]):

| Element | Impedance | Reactance | Phase of $Z$ | Current vs voltage |
|---|---|---:|---:|---|
| Resistor | $Z_R=R$ | — | $0°$ | in phase |
| Inductor | $Z_L=j\omega L$ | $X_L=\omega L$ | $+90°$ | current **lags** ("ELI") |
| Capacitor | $Z_C=-j/(\omega C)=-jX_C,\ X_C=1/(\omega C)$ | $X_C=1/(\omega C)$ | $-90°$ | current **leads** ("ICE") |

**Memory:** $R\to0°,\ L\to+90°,\ C\to-90°$ — matches the "ELI the ICE man" mnemonic already used in [[05 Sinusoids and Phasors|Week 5]]; impedance is what makes that phase statement quantitative (magnitude, not just direction).

## AC Ohm's law

$$\bar V=\bar I Z\qquad\Longleftrightarrow\qquad \bar I=\frac{\bar V}{Z}\qquad\Longleftrightarrow\qquad Z=\frac{\bar V}{\bar I}$$

## Series combination

$$Z_{\rm eq}=Z_1+Z_2+\cdots$$

For series RLC: $Z=R+jX_L-jX_C=R+j(X_L-X_C)$ — the single most-used formula in this tutorial (Q3, Q5, Q7).

### Three cases for series RLC

- **Inductive** ($X_L>X_C$): $Z=R+jX$, current **lags** voltage.
- **Capacitive** ($X_C>X_L$): $Z=R-jX$, current **leads** voltage.
- **Resonance** ($X_L=X_C$): $Z=R$ (purely resistive), $V$ and $I$ in phase — see [[08 Resonance and Magnetically Coupled Circuits|Week 8]] for the full resonance treatment ($\omega_0=1/\sqrt{LC}$).

### RC series (Q5 pattern)

$Z=R-jX_C$, $|Z|=\sqrt{R^2+X_C^2}$, $\theta_Z=-\tan^{-1}(X_C/R)$, so $\theta_I=-\theta_Z>0$: current leads. Worked example: $Z=6-j8\ \Omega\Rightarrow|Z|=10,\ \theta_Z=-53.13°$, so current leads voltage by $53.13°$.

### RL series (Q3 pattern)

$Z=R+jX_L$, $|Z|=\sqrt{R^2+X_L^2}$, $\theta_Z=\tan^{-1}(X_L/R)$, current lags.

### Series RLC phase angle

$$\phi=\tan^{-1}\!\left(\frac{X_L-X_C}{R}\right),\qquad \theta_I=\theta_V-\phi$$

## Parallel combination

$$Z_{\rm eq}=\frac{Z_1Z_2}{Z_1+Z_2}\ \text{(two branches)}$$

For more than two branches, use admittance (see below) rather than repeated product-over-sum — the same reasoning as [[Series-Parallel Resistance Reduction]] for DC resistor networks, but now with complex numbers where the "reciprocal of the sum of reciprocals" shortcut for exactly two elements still holds.

## Admittance

$$Y=\frac1Z\ \text{(siemens, S)},\qquad Y_{\rm eq}=Y_1+Y_2+\cdots\ \text{(parallel)},\qquad Z_{\rm eq}=\frac1{Y_{\rm eq}}$$

Basic admittances: $Y_R=1/R$, $Y_L=1/(j\omega L)=-j/(\omega L)$, $Y_C=j\omega C$.

## Phasor voltage relationships in a series circuit

With current as reference phasor $I\angle0°$: $V_R=IR$ (at $0°$), $V_L=IX_L$ (at $+90°$), $V_C=IX_C$ (at $-90°$), and the source voltage is the **phasor** sum

$$\bar V=\bar V_R+\bar V_L+\bar V_C$$

not a scalar sum — see [[Phasors and Complex Algebra|Phasors and Complex Algebra]].

## Voltage magnification in series RLC (Q7)

Because $\bar V_L$ and $\bar V_C$ are $180°$ out of phase with each other (one at $+90°$, one at $-90°$ relative to $I$), they can partially cancel in the phasor sum even while each individually is large:

$$|V_L|>|V_{\rm source}|\ \text{and}\ |V_C|>|V_{\rm source}|\ \text{are both possible}$$

This is not a KVL violation — KVL holds for the phasor (vector) sum, not for magnitudes. This effect is the qualitative preview of resonance ([[08 Resonance and Magnetically Coupled Circuits|Week 8]]): near $\omega_0$, $X_L\approx X_C$ so $Z\approx R$ is small, current is large, and $V_L,V_C$ (each $=IX_{L,C}$) can dramatically exceed the source voltage — the basis of voltage magnification in tuned circuits.

## Related
- [[The Mechanical-Electrical Analogy (Impedance Analogy)|Cross-domain: impedance's mechanical twin (mass↔L, damper↔R, spring↔1/C)]]
- [[06 Sinusoidal Steady-State Analysis|Week 6 — Sinusoidal Steady-State Analysis]]
- [[08 Resonance and Magnetically Coupled Circuits|Week 8 — Resonance]]
- [[AC Power and Power Factor|AC Power and Power Factor]]

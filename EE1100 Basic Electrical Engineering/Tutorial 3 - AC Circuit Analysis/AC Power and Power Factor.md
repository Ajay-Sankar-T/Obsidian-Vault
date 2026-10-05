---
tags: [EE1100, AC-circuits, power]
up: "[[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis]]"
---

# AC Power and Power Factor

← up: [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Tutorial 3 - AC Circuit Analysis|Tutorial 3]] · builds on: [[EE1100 Basic Electrical Engineering/06 Sinusoidal Steady-State Analysis|Week 6]], [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]

## The three powers

**Real (active) power** — the average power actually consumed/dissipated:
$$P=V_{\rm rms}I_{\rm rms}\cos\phi\quad[\text{W}]$$

**Reactive power** — energy sloshed back and forth with inductors/capacitors, net zero average, but real in the sense that it still loads the supply and wiring:
$$Q=V_{\rm rms}I_{\rm rms}\sin\phi\quad[\text{VAR}]$$

**Apparent power** — what the supply actually has to be rated for:
$$|S|=V_{\rm rms}I_{\rm rms}\quad[\text{VA}]$$

Here $\phi=\theta_V-\theta_I$ is the angle between voltage and current, which — from [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Phasors and Complex Algebra|Phasors and Complex Algebra]]'s $\theta_I=\theta_V-\theta_Z$ — is exactly the **impedance angle** $\theta_Z$.

## Complex power

$$\bar S=\bar V\bar I^{*}=P+jQ$$

where $I^{*}$ is the complex conjugate of the current phasor (conjugating fixes the sign of $Q$ so that inductive loads read positive $Q$, matching convention). Then:

$$P=\operatorname{Re}(S),\qquad Q=\operatorname{Im}(S),\qquad |S|=\sqrt{P^2+Q^2}$$

**Power triangle:** $P$ horizontal, $Q$ vertical, $S$ hypotenuse; $\tan\phi=Q/P$.

## Reactive power of each element

| Element | $P$ | $Q$ | Behaviour |
|---|---:|---:|---|
| Resistor | $>0$ | $0$ | dissipates only |
| Ideal inductor | $0$ | $I_{\rm rms}^2X_L>0$ | lagging |
| Ideal capacitor | $0$ | $-I_{\rm rms}^2X_C<0$ | leading |
| Inductive circuit (net) | $>0$ | $>0$ | lagging |
| Capacitive circuit (net) | $>0$ | $<0$ | leading |

**Memorize:** $+Q\to$ inductive/lagging, $-Q\to$ capacitive/leading — directly consistent with the impedance-angle sign convention in [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]] ($X_L>0$, $X_C<0$ contribution).

## Power factor

$$pf=\cos\phi=\frac{P}{|S|}$$

For an impedance $Z=R+jX$: $pf=R/|Z|$. If current leads voltage, $pf$ is **leading** (capacitive load); if current lags, $pf$ is **lagging** (inductive load) — the two-word qualifier is not optional, $\cos\phi$ alone doesn't distinguish the two.

## Fast series-circuit power shortcut

For $Z=R+jX$ carrying current of magnitude $I$:

$$P=I^2R,\qquad Q=I^2X,\qquad |S|=I^2|Z|$$

For series RLC specifically: $P=I^2R$, $Q=I^2(X_L-X_C)$, $S=I^2[R+j(X_L-X_C)]$ — read directly off [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Impedance and Series-Parallel AC Circuits|Impedance and Series-Parallel AC Circuits]]'s $Z$ formula without needing $V$ at all.

## Power conservation

$$\sum P_{\rm supplied}=\sum P_{\rm absorbed},\qquad \sum S=0\ \text{(signed consistently)}$$

## Big trap: superposition does NOT apply to power

[[EE1100 Basic Electrical Engineering/07 AC Circuit Analysis and Network Theorems|Week 7]] establishes that superposition carries over from DC for voltage and current. It does **not** carry over for power, because $P=I^2R$ is quadratic: $(I_1+I_2)^2\ne I_1^2+I_2^2$ in general (cross terms survive unless the two sources are at different frequencies and everything is properly time-averaged). Never write $P_{\rm total}=P_1+P_2$ from separate superposition solutions without justifying it.

## RMS, not peak

Every formula above uses RMS values (see [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Sinusoidal Waveforms, RMS and Average Value|RMS and Average Value]]). Using peak values in $P=VI\cos\phi$ overstates power by a factor of 2 — one of the most common exam errors in this course.

## Related
- [[EE1100 Basic Electrical Engineering/Tutorial 3 - AC Circuit Analysis/Power Factor Correction|Power Factor Correction]]
- [[EE1100 Basic Electrical Engineering/09 Three Phase Circuits and Power Measurement|Week 9 — Three Phase Power]] (the same $P,Q,S$ machinery, per phase)

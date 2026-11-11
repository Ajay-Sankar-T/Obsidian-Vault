---
tags: [concept, instrumentation]
course: "Measurements, Instrumentation and Control (ME2400)"
aliases: [Strain gauge, Wheatstone bridge, Thermocouple, RTD, LVDT, Thermistor, Signal conditioning, Amplifier, Anti-aliasing, Sampling, Actuators]
---

# Sensors and Signal Conditioning

> [!abstract] In one breath
> A **sensor** turns a physical quantity into an electrical one (resistance, voltage, inductance). That signal is small and noisy, so a **conditioning chain** (bridge, amplifier, filter, analog-to-digital converter) makes it usable. Learn the four workhorses: **strain gauge + Wheatstone bridge, thermocouple, RTD, LVDT**, and the one rule of sampling.

Part of [[Measurements, Instrumentation and Control - MOC]]. Previous: [[Measurement Performance and Error Propagation]]. Next: [[First-Order Systems - Time Constant and Response]].

## 1. Sensors for common measurements

| Quantity | Sensor | Principle |
| --- | --- | --- |
| Strain, force, pressure | **strain gauge** | resistance changes with strain |
| Temperature | **thermocouple** | Seebeck voltage of two dissimilar metals |
| Temperature | **RTD** (Pt100), thermistor | resistance changes with temperature |
| Displacement | **LVDT**, potentiometer, capacitive, encoder | inductive coupling, resistance, capacitance, counting |
| Acceleration | piezoelectric, MEMS capacitive | seismic mass ([[Second-Order Systems - Damping and Overshoot]]) |
| Flow | orifice or venturi + pressure sensor, turbine, ultrasonic | [[Incompressible Inviscid Flow and Bernoulli - Formula Bank]] |
| Speed | tachometer, encoder, Hall sensor | pulses per rev |

## 2. Strain gauge and the Wheatstone bridge

A metal-foil gauge of resistance $R$ changes by $\Delta R/R=GF\cdot\varepsilon$ with the **gauge factor** $GF\approx2$. The change is tiny (for $\varepsilon=1000\ \mu\varepsilon$, $\Delta R/R=0.2$ %), so the gauge sits in a **Wheatstone bridge** that outputs only the *difference*.

$$
V_o=V_s\Big(\frac{R_1}{R_1+R_2}-\frac{R_4}{R_3+R_4}\Big)\ \Rightarrow\ \text{balanced when }R_1/R_2=R_4/R_3
$$

For equal resistors with $n$ active arms (small changes):

| Configuration | Output $V_o/V_s$ | Notes |
| --- | --- | --- |
| Quarter bridge (1 gauge) | $GF\,\varepsilon/4$ | needs a dummy gauge to cancel temperature |
| Half bridge (2 gauges, bending, tension and compression) | $GF\,\varepsilon/2$ | cancels temperature and doubles the signal |
| Full bridge (4 gauges) | $GF\,\varepsilon$ | most sensitive, load cells |

**Example.** Steel at $\varepsilon=1000\ \mu\varepsilon$, $GF=2$, $V_s=5$ V: quarter bridge $5(2)(10^{-3})/4=\mathbf{2.5\ mV}$, half $5$ mV, full $10$ mV. To use a 0–1 V converter the amplifier gain must be $1/2.5\text{ mV}=400$ (quarter bridge).

![[MIC-1-bridge.png]]

## 3. Temperature sensors

- **Thermocouple:** voltage $\approx S\,(T_{hot}-T_{ref})$ with $S\approx41\ \mu$V/K for type K (4.1 mV per 100 K): requires a **cold-junction** reference, tiny signals, wide range (to 1300 °C), fast response (a small bead).
- **RTD:** $R=R_0(1+\alpha T)$, Pt100: $R_0=100\ \Omega$, $\alpha=0.00385$/K: 138.5 Ω at 100 °C, 0.385 Ω/K. Accurate, stable, near-linear, but needs a current source and bridge and is slower; **lead-wire resistance** matters (3-wire or 4-wire connection).
- **Thermistor:** $R\propto e^{B/T}$, very sensitive but strongly nonlinear.

## 4. LVDT

A primary coil and two secondaries wound in opposition with a movable iron core: at the centre the secondary voltages cancel (zero output); displacement makes one larger, giving a **linear, signed** output proportional to position over its range (about ±mm to ±100 mm). No contact friction, practically infinite resolution, rugged.

## 5. Conditioning

**Amplifier**: an op-amp in differential configuration (instrumentation amplifier) amplifies the bridge difference and rejects common-mode noise (see [[T6-Q1 - Amplifier Gain and Design]]). **Filter**: an RC low-pass with $f_c=1/(2\pi RC)$ removes noise outside the signal band ([[Filter Theory]]). **ADC**: converts to a number: resolution $=V_{range}/2^N$ (a 12-bit converter on 5 V: 1.22 mV per count).

**Sampling theorem.** To record a signal of highest frequency $f_{max}$, sample at $f_s>2f_{max}$. Below that, **aliasing** folds the signal into a false lower frequency: a 7 Hz signal sampled at 10 Hz looks exactly like a 3 Hz signal ($|7-10|$). Always put an **anti-alias low-pass filter** before the converter.

## 6. Actuators (the output side)

| Type | Force and speed | Notes |
| --- | --- | --- |
| Electric (DC, stepper, servo) | moderate | clean, precise, easy control |
| Hydraulic | very high force, slow-ish | oil, stiff, compact |
| Pneumatic | low force, fast | air, compressible, simple on/off |

> [!warning] Traps
> - Putting a single gauge in a quarter bridge without temperature compensation: the temperature coefficient of the gauge can swamp the strain signal.
> - Forgetting lead-wire resistance in RTDs.
> - Sampling at exactly twice the signal frequency: sample at 5–10 times.
> - Using a thermocouple without cold-junction compensation.
> - Assuming a bridge is balanced: nulling or offset adjustment is needed.

> [!question]- Predict first: a bending beam with a gauge on the top and one on the bottom. Which bridge configuration, and what is the gain over a quarter bridge?
> A **half bridge**, with the two gauges in adjacent arms (tension and compression): twice the signal of a quarter bridge, and the temperature effect cancels because both gauges see the same temperature change.

> [!question]- Why are three or four wires used for an RTD?
> The lead resistance is in series with a 100 Ω element; 2 Ω of copper wire would read as about 5 K. A third wire (or four) lets the bridge or the meter subtract the lead resistance.

## 7. Connections

- [[Strain Transformation and Rosettes]] and [[Concept of Stress]] — what strain gauges and rosettes measure.
- [[Filter Theory]] and [[Frequency Response and Resonance Curves]] — anti-alias filtering and sensor bandwidth.
- [[Series-Parallel Resistance Reduction]] — the bridge is a divider pair; $V_o$ is the difference of two divider outputs.
- [[First-Order Systems - Time Constant and Response]] — a thermocouple bead and an RC filter are both first-order.

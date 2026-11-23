---
tags: [EE1100, diodes, tutorial-solution]
---

# A-Q5 — Applications of Diodes

Hub: [[Tutorial 5 - Diode Circuits and Applications]] · Previous: [[T5-A-Q4 - Bias, Cut-in Voltage, Saturation Current and Resistance]] · Next: [[T5-A-Q6 - Rectifier Circuits and Waveforms]]

> [!question] Write down the important applications of diodes.

## 1. List of applications

| Application | Principle | Where it appears in this tutorial |
|---|---|---|
| **Rectification** (AC → DC) in power supplies and chargers | one-way conduction | [[T5-A-Q6 - Rectifier Circuits and Waveforms]], [[T5-B-Q8 - Half-Wave Rectifier with Series Resistor]], [[T5-B-Q11 - Full-Wave Rectifier with Battery]] |
| **Filtered DC supplies** | rectifier + capacitor | [[T5-A-Q8 - Half-Wave Rectifier Filter Capacitor]], [[T5-A-Q9 - Full-Wave Rectifier Filter Capacitor]] |
| **Clipping / limiting** (waveform shaping, signal protection) | diode + reference turns ON above a threshold | [[T5-B-Q3 - Series Battery Rectifier]], [[T5-B-Q10 - Two-Level Clipper]], [[T5-B-Q9 - Battery Charging Rectifier Circuit]] |
| **Clamping / DC restoration** | capacitor charged by a diode shifts the DC level | [[T5-B-Q6 - Diode Clamper]] |
| **Voltage multipliers** | diodes steer charge onto capacitors in turn | [[T5-B-Q12 - Voltage Doubler]] |
| **Logic gates** (diode AND/OR) | highest / lowest input dominates | [[T5-B-Q2 - Diode OR Gate]], [[T5-B-Q4 - Diode AND Gate]], [[T5-B-Q5 - Ideal Diodes with Negative Reference]] |
| **Voltage regulation** | Zener diode in breakdown holds a constant voltage | see [[T5-A-Q3 - V-I Characteristics of a p-n Diode]] |
| **Reverse-polarity and over-voltage protection** | a diode blocks reversed supply; a diode across a relay coil absorbs the inductive kick (freewheeling) | — |
| **Demodulation (detector)** of AM signals | envelope detector = rectifier + RC | — |
| **Light emitting diodes, photodiodes, solar cells** | recombination emits light; absorbed photons create $I_{ph}$ | — |
| **Switching, mixers, varactor tuning, temperature sensing** | $C(V)$ of a reverse-biased junction; $v_D\approx-2$ mV/°C | — |

## 2. Examples of the waveform operations

![[A5-applications.png]]

> [!note] Why diodes are so widely used
> A p-n junction is a cheap, small, robust, voltage-controlled one-way valve: very low resistance in the forward direction, very high in the reverse direction, and a fixed voltage drop of about 0.7 V (Si) when conducting.

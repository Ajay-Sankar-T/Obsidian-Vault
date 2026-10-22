# Filter Theory

Filters are circuits designed to allow certain frequencies to pass through while attenuating others. In basic electrical engineering, we primarily deal with passive filters using resistors (R), inductors (L), and capacitors (C).

## 1. Low-Pass Filter (LPF)
Allows low frequencies to pass and attenuates high frequencies.
- **Simple RC LPF**: Resistor in series, capacitor in parallel to output.
- **Cut-off Frequency ($\omega_c$)**: The frequency where the output power drops to half its maximum value (the -3dB point).
  $$ \boxed{\omega_c = \frac{1}{RC}} $$
- **Half-Power Frequency ($f_c$)**: $f_c = \frac{1}{2\pi RC}$.

## 2. High-Pass Filter (HPF)
Allows high frequencies to pass and attenuates low frequencies.
- **Simple RC HPF**: Capacitor in series, resistor in parallel to output.
- **Cut-off Frequency ($\omega_c$)**:
  $$ \boxed{\omega_c = \frac{1}{RC}} $$

## 3. Band-Pass Filter (BPF)
Allows a specific range of frequencies (the band) to pass.
- **Series RLC BPF**: Output taken across the resistor.
- **Center Frequency ($\omega_0$)**: The resonant frequency of the circuit.
  $$ \boxed{\omega_0 = \frac{1}{\sqrt{LC}}} $$
- **Bandwidth (BW)**: The width of the frequency range where the power is $\ge$ half the maximum.
  $$ \boxed{BW = \frac{\omega_0}{Q} = \frac{R}{L}} $$
- **Quality Factor (Q)**: Measure of selectivity. $Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$.

## 4. Band-Rejection / Notch Filter (BRF)
Attenuates a specific narrow band of frequencies and allows everything else.
- **Parallel RLC BRF**: Often used to eliminate a specific interference frequency.
- **Center Frequency ($\omega_0$)**: The frequency to be rejected.
  $$ \boxed{\omega_0 = \frac{1}{\sqrt{LC}}} $$

## 5. Transfer Function $H(\omega)$
The ratio of output voltage to input voltage: $H(\omega) = \frac{V_{out}(\omega)}{V_{in}(\omega)}$.
- For a series RLC circuit with output across $R$:
  $$ H(\omega) = \frac{R}{R + j(\omega L - \frac{1}{\omega C})} $$

---
**Backlinks**:
- [[EE1100 MOC]]
- [[08 Resonance and Magnetically Coupled Circuits]]
- [[Frequency Response and Resonance Curves]]

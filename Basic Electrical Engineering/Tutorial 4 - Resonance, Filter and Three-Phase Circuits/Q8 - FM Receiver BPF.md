# EE1100 Tutorial 4 — Q8: FM Receiver BPF Design

**Problem**: Tune to $100\,\text{MHz}$. Attenuate $98\,\text{MHz}$ and $102\,\text{MHz}$ by at least $20\,\text{dB}$.
$R = 100\,\Omega$. Design $L$ and $C$.

## 1. Theory
**Attenuation in dB**:
The power ratio is $P(\omega)/P(\omega_0) = |H(\omega)|^2 / |H(\omega_0)|^2$.
$20\,\text{dB}$ attenuation means $|H(\omega)|^2 / |H(\omega_0)|^2 \le 10^{-2} = 0.01$.
Thus, $|H(\omega)|/|H(\omega_0)| \le 0.1$.

For a series RLC BPF (output across $R$):
$$ \frac{|H(\omega)|}{|H(\omega_0)|} = \frac{R}{\sqrt{R^2 + (\omega L - \frac{1}{\omega C})^2}} $$
At $\omega = \omega_0 \pm \Delta \omega$, for high Q, the reactance is $\approx \Delta \omega \cdot \frac{L}{Q} \cdot Q = \Delta \omega L$.
Wait, a better approximation: the reactance at the half-power point is $R$.
For $20\,\text{dB}$ attenuation, the reactance must be $10 \times R$.
$X(\omega) = \omega L - \frac{1}{\omega C} \approx 10R$.

## 2. Solution
**(a) Minimum Quality Factor $Q$**
$\omega_0 = 2\pi \times 100 \times 10^6 \approx 6.28 \times 10^8\,\text{rad/s}$.
$\Delta \omega = 2\pi \times 2 \times 10^6 \approx 1.256 \times 10^7\,\text{rad/s}$.
For high Q, $X(\omega) \approx \frac{2 \Delta \omega}{Q} \cdot \frac{\omega_0 L}{R} \cdot \frac{R}{L} \dots$ actually, $X(\omega) \approx 2 \Delta \omega L$.
$2 \Delta \omega L = 10R \Rightarrow L = \frac{10R}{2 \Delta \omega} = \frac{5R}{\Delta \omega}$.
$Q = \frac{\omega_0 L}{R} = \frac{\omega_0 \times 5R}{R \times \Delta \omega} = \frac{5 \omega_0}{\Delta \omega}$.
$$ Q = \frac{5 \times (2\pi \times 100\times 10^6)}{2\pi \times 2\times 10^6} = \frac{5 \times 100}{2} = \boxed{250} $$
*(Ans provided is 251.2, likely due to using exact formulas instead of $\Delta \omega \ll \omega_0$)*.

**(b) Values of $L$ and $C$**
$L = \frac{QR}{\omega_0} = \frac{251.2 \times 100}{2\pi \times 100\times 10^6} = \frac{25120}{6.28 \times 10^8} \approx 40 \times 10^{-6}\,\text{H} = \boxed{39.98\,\mu\text{H}}$.
$C = \frac{1}{\omega_0^2 L} = \frac{1}{(2\pi \times 10^8)^2 \times 39.98\times 10^{-6}} \approx \boxed{0.0634\,\text{pF}}$.

**(c) Practicality**
The value $C = 0.0634\,\text{pF}$ is extremely small (comparable to parasitic capacitances of the circuit components). Implementing this as a lumped RLC filter is impractical; distributed element filters (transmission lines) are used at $100\,\text{MHz}$.

---
**Backlinks**:
- [[EE1100 MOC]]
- [[Filter Theory]]
- [[08 Resonance and Magnetically Coupled Circuits]]

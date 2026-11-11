Related: [[Torsion of Circular Shafts]]

## Power-Torque-Speed Relation

For a shaft rotating at angular speed $\omega$ (rad/s) transmitting torque $T$, the power delivered is
$$P = T\omega$$
If rotational speed is given as frequency $f$ (Hz) or $N$ (rpm):
$$\omega = 2\pi f = \frac{2\pi N}{60}, \qquad P = T\cdot\frac{2\pi N}{60}$$

## Design Procedure

1. From the rated power $P$ and operating speed $N$, compute the design torque: $T=\dfrac{60P}{2\pi N}$.
2. Apply the torsion formula ([[Torsion of Circular Shafts]]) with the allowable shear stress $\tau_{allow}$ to size the shaft:
$$\tau_{allow} = \frac{Tc}{J} \implies c \text{ (or shaft diameter) solved for}$$
3. Check the angle-of-twist limit (often a separate design constraint, e.g. limiting $\phi/L$ to some maximum degrees per meter for machinery alignment) using $\phi=TL/(GJ)$.

## Shafts with Varying Torque (Multiple Pulleys/Gears)

When torque is applied/removed at several points along a shaft (as in a line shaft driving multiple machines), draw a **torque diagram** analogous to the shear/moment diagrams of [[Shear Force and Bending Moment Diagrams]]: compute the internal torque in each segment via the method of sections, then apply the torsion formula segment by segment (using the largest internal torque anywhere to govern the design, if the shaft has uniform diameter).

## Check yourself

> [!question]- Q1. A shaft transmits 30 kW at 1200 rpm. What torque does it carry?
> $\omega=2\pi\times20=125.7$ rad/s and $T=P/\omega=238.7$ N·m.

> [!question]- Q2. What diameter keeps the shear stress below 60 MPa at that torque?
> $d^3=16T/(\pi\tau)=2.03\times10^{-5}$ m³, so $d=27.3$ mm (round up to a standard size).

> [!question]- Q3. The same power is transmitted at twice the speed. What happens to the torque and the shaft size?
> Torque halves ($T=P/\omega$), so a smaller shaft suffices. This is why high-speed drive shafts are slender and low-speed ones are thick.

---
Next: [[Shear Force and Bending Moment Diagrams]]


## Cross-domain links

- [[Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]] — P = Tω is the mechanical twin of P = VI; the shaft sits between motor (gyrator) and gear (transformer).

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

---
Next: [[Shear Force and Bending Moment Diagrams]]


## Cross-domain links

- [[Cross-Domain Synthesis/Gears, Transformers and Reflected Impedance|Gears, Transformers and Reflected Impedance]] — P = Tω is the mechanical twin of P = VI; the shaft sits between motor (gyrator) and gear (transformer).

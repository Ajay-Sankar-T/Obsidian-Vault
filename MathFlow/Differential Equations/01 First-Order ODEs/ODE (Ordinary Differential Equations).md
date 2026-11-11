See [[First Order ODEs - MOC]] for the full note map.

▶ An ordinary differential equation (ODE) is an equation
involving an unknown function of a single independent
variable and one or more of its derivatives.

| ###Order                                                                                          | ###Degree                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ▶ The order of an ODE is determined by the highest-order<br>derivative appearing in the equation. | ▶ The degree of an ordinary differential equation is the power<br>(exponent) of the highest-order derivative appearing in the<br>equation, after the equation has been made free of:<br>- fractional powers or roots of derivatives<br>- negative powers of derivatives<br>- derivatives appearing in denominators (fractions) |
In other words, first write the ODE as a polynomial equation in derivatives; the degree is then the exponent on the highest derivative term.

## Examples

**Example 1**
$$\left(\frac{d^2y}{dx^2}\right)^3 + \left(\frac{dy}{dx}\right)^2 + y = 0$$
Order = 2 (highest derivative is the 2nd derivative)
Degree = 3 (that highest derivative is raised to the power 3)

**Example 2**
$$\frac{d^2y}{dx^2} + \sqrt{\frac{dy}{dx}} = 0$$
Here $\frac{dy}{dx}$ appears under a square root, thus not in polynomial form. Squaring to remove the radical:
$$\left(\frac{d^2y}{dx^2}\right)^2 = \frac{dy}{dx}$$
Order = 2, Degree = 2

## Important notes

- **Order** = highest derivative present (always well-defined).
- **Degree** is only defined when the ODE can be expressed as a polynomial in its derivatives. If not (e.g., derivatives inside sin, log, or exponential functions), the degree is **not defined**.

**Example where degree is undefined**
$$\frac{d^2y}{dx^2} + \sin\left(\frac{dy}{dx}\right) = 0$$
Order = 2, but degree is undefined since $\frac{dy}{dx}$ sits inside a sine function.

---
Next: [[First Order ODEs]]

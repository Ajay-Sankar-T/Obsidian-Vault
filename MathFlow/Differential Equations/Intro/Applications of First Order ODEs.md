Related: [[Particular Solution and IVP]]

Many scientific phenomena are naturally described by first-order differential equations.

## Population Growth

Suppose $P(t)$ denotes the population at time $t$. If the rate of growth is proportional to the population,
$$\frac{dP}{dt} = kP,$$
where $k > 0$ is the growth constant. The solution is
$$P(t) = P_0 e^{kt}.$$

## Radioactive Decay

If the decay rate is proportional to the remaining quantity,
$$\frac{dN}{dt} = -\lambda N, \quad \lambda > 0.$$
The solution is
$$N(t) = N_0 e^{-\lambda t}.$$

## Newton's Law of Cooling

Let $T(t)$ denote the temperature of an object. Newton's law states
$$\frac{dT}{dt} = -k(T - T_s),$$
where $T_s$ denotes the surrounding temperature. The solution is
$$T(t) = T_s + (T_0 - T_s)e^{-kt}.$$


## Visual

![[DE-E4-applications.png]]
**Figure:** Exponential growth, radioactive decay (with its half-life $\ln2/\lambda$), and Newton's cooling, where every temperature curve relaxes to the ambient $T_s$ with the same time constant $1/k$.

---
Next: [[Isoclines]]

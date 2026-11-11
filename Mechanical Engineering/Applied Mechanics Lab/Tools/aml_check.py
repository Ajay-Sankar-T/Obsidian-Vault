"""Recompute the numbers quoted in the AM2540 lab notes."""
import numpy as np
g = 9.81
I = 25 * 6 ** 3 / 12; L = 400.0
print("beam: I =", I, " delta_Al(24.5N) =", round(24.5 * L ** 3 / (48 * 70e3 * I), 3), " delta_steel =", round(24.5 * L ** 3 / (48 * 210e3 * I), 3), " k_Al, k_steel =", round(48 * 70e3 * I / L ** 3, 1), round(48 * 210e3 * I / L ** 3, 1))
print("beam: shear/bending ratio (E/kG)(t/L)^2, steel, kappa=5/6, G=80.8:", round((210 / (5 / 6 * 80.8)) * (6 / 400) ** 2, 5))
w = 2700 * 25e-3 * 6e-3 * 9.81  # N/m
print("beam: self-weight deflection mm:", round(5 * (w / 1000) * 400 ** 4 / (384 * 70e3 * I), 3), "  max-deflection location for a = L/4 (x/L):", round(1 - np.sqrt((1 - .25 ** 2) / 3), 3))
print("beam: 0.1 mm error on t = 6 mm ->", round(100 * 0.1 / 6, 2), "% in t,", round(100 * 3 * 0.1 / 6, 1), "% in I")
Imin = 25 * 3 ** 3 / 12; A = 75
Pcr = np.pi ** 2 * 210e3 * Imin / 400 ** 2
print("buckling: Imin =", Imin, " Pcr =", round(Pcr, 1), " pinned-fixed =", round(2 * Pcr, 1), " r =", round(3 / np.sqrt(12), 3), " L/r =", round(400 / (3 / np.sqrt(12)), 1), " sigma_cr =", round(Pcr / A, 2), " Pcr/(sy A) =", round(Pcr / (250 * A), 3), " strong/weak axis ratio:", round((25 / 3) ** 2, 1))
print("tensile ES6: F =", 2.83 * 100, " ext =", 3.00 - 2.83, " stress =", round(283 / 9, 1), " strain =", round(.17 / 31, 4), " elong% =", round(2 / 31 * 100, 2), " elastic ext of steel @31 MPa over 31 mm:", round(31 / 210e3 * 31, 4), "mm")
A0 = np.pi * 10 ** 2 / 4
print("tensile DIC: A0 =", round(A0, 1), " F_y =", round(250 * A0 / 1e3, 1), "kN  F_uts =", round(400 * A0 / 1e3, 1), "kN  true sigma =", 400 * 1.16, " true strain =", round(np.log(1.16), 4), " area reduction % =", (100 - 36))
r = 2.5; J = np.pi * r ** 4 / 2; T = 0.5 * g * 50
print("torsion: J =", round(J, 2), " T =", round(T, 1), "N.mm  twist deg steel/brass/Al:", [round(float(np.degrees(T * 300 / (G * J))), 3) for G in (79.6e3, 38e3, 25.5e3)], " tau =", round(T * r / J, 2), "MPa;  +-0.05 mm on r ->", round(4 * 0.05 / 2.5 * 100, 1), "% in J")
print("G from E,nu: steel", round(210 / 2.6, 1), " Al", round(70 / 2.66, 1))

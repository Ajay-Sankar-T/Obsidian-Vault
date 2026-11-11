"""Recompute every number quoted in the Physics I notes. Run: python ph_check.py  (prints the values; asserts the ones that must match exactly)."""
import numpy as np
from scipy.special import ellipk
from scipy.integrate import quad

g = 9.81
print("--- Module 1")
u, v = np.array([1, 2, 2.]), np.array([2, -1, 2.])
print("u.v =", u @ v, " angle =", round(np.degrees(np.arccos(u @ v / 9)), 2), " u x v =", np.cross(u, v), " |u x v| =", round(np.linalg.norm(np.cross(u, v)), 3), " identity:", 81 - 16)
p = np.radians(30); r = np.array([2.6, 1.9]); print("rotation x', y' =", round(r[0] * np.cos(p) + r[1] * np.sin(p), 3), round(-r[0] * np.sin(p) + r[1] * np.cos(p), 3))

print("--- Module 2")
print("const force x(3), x(-1):", 1 + 2 * 3 + 9, 1 - 2 + 1)
print("cart angle (deg):", round(np.degrees(np.arctan(2 / g)), 2), "  mu_s braking:", round(3 / g, 3))
print("conical pendulum L=1, 35deg: omega, T, tension:", round(np.sqrt(g / np.cos(np.radians(35))), 3), round(2 * np.pi / np.sqrt(g / np.cos(np.radians(35))), 3), round(0.5 * g / np.cos(np.radians(35)), 3))

print("--- Module 3")
w0 = np.sqrt(200 / .5); print("SHM: omega, T, vmax, amax, E:", w0, round(2 * np.pi / w0, 4), .05 * w0, .05 * w0 ** 2, .5 * 200 * .05 ** 2)
b, m, k = 0.8, 0.2, 20.0; beta = b / (2 * m); w0 = np.sqrt(k / m); print("damped: beta, w0, w1, Q, b_crit:", beta, w0, round(np.sqrt(w0 ** 2 - beta ** 2), 3), w0 / (2 * beta), 2 * np.sqrt(k * m))
D = lambda w: 1 / np.sqrt((100 - w ** 2) ** 2 + (2 * .5 * w) ** 2); print("driven D(5), D(10), D(20):", round(D(5), 4), round(D(10), 4), round(D(20), 5))
print("Q from 3 swings halving:", round(np.pi / (np.log(2) / 3), 2))

print("--- Module 4")
print("double well: U''(0), U''(1), T_small:", -1, 2, round(2 * np.pi / np.sqrt(2), 3))
print("pendulum T/T0 at 10, 30, 90, 150 deg:", [round(float(2 * ellipk(np.sin(np.radians(d) / 2) ** 2) / np.pi), 4) for d in (10, 30, 90, 150)])
t0 = np.radians(90); print("series 1+t^2/16 =", round(1 + t0 ** 2 / 16, 4), " + 11 t^4/3072 =", round(1 + t0 ** 2 / 16 + 11 * t0 ** 4 / 3072, 4), "  T0(L=1) =", round(2 * np.pi / np.sqrt(g), 4), " T(90) =", round(2 * np.pi / np.sqrt(g) * 1.1803, 3), " v_bottom =", round(np.sqrt(2 * g), 3))
print("damped spiral amplitude ratio per turn:", round(np.exp(-0.2 * 2 * np.pi / np.sqrt(1 - .04)), 3))
# x^4 potential: T proportional to 1/A
for A in (1, 2):
    T = 4 * quad(lambda x: 1 / np.sqrt(2 * (A ** 4 / 4 - x ** 4 / 4)), 0, A)[0]; print("U=x^4/4, A =", A, " T =", round(T, 4))

print("--- Module 5")
print("grad f=x^2 y at (1,2): (4,1), |grad| =", round(np.sqrt(17), 3), " slope along (3,4)/5:", (12 + 4) / 5)
U = lambda x, y, z: -(x ** 2 * y + x * z ** 2); print("W (0,0,0)->(1,2,3) =", U(0, 0, 0) - U(1, 2, 3))
print("sphere volume check:", round(4 / 3 * np.pi, 4), " cone (x,y,z)=(1,1,sqrt2): r, theta, phi =", 2, np.degrees(np.arccos(np.sqrt(2) / 2)), 45)

print("--- Module 6")
print("Atwood a (3,1):", (3 - 1) / (3 + 1) * g)

print("--- Module 7")
GM = 3.986004418e14; R = 7.0e6
print("LEO r=7000 km: v, T:", round(np.sqrt(GM / R) / 1e3, 3), "km/s", round(2 * np.pi * np.sqrt(R ** 3 / GM)), "s =", round(2 * np.pi * np.sqrt(R ** 3 / GM) / 60, 1), "min")
print("Kepler: Mars T, Jupiter T:", round(1.524 ** 1.5, 3), round(5.203 ** 1.5, 2), "yr")
e = 0.0167; print("Earth vp/va:", round((1 + e) / (1 - e), 4), "  escape speed at 1 AU:", round(np.sqrt(2) * 29.78, 2), "km/s")
a = 75.3 ** (2 / 3); e = 0.967; print("Halley: a =", round(a, 2), " perihelion =", round(a * (1 - e), 3), " aphelion =", round(a * (1 + e), 2), "AU")
print("Earth-Moon: CM from Earth centre:", round(384400 / (1 + 81.3)), "km;  reduced mass / m_moon:", round(81.3 / 82.3, 4))
# Hohmann LEO -> GEO
r1, r2 = 6.678e6, 4.2164e7; at = (r1 + r2) / 2
v1 = np.sqrt(GM / r1); vp = np.sqrt(GM * (2 / r1 - 1 / at)); va = np.sqrt(GM * (2 / r2 - 1 / at)); v2 = np.sqrt(GM / r2)
print("LEO->GEO: dv1, dv2, total (km/s):", round((vp - v1) / 1e3, 3), round((v2 - va) / 1e3, 3), round((vp - v1 + v2 - va) / 1e3, 3), " time (h):", round(np.pi * np.sqrt(at ** 3 / GM) / 3600, 2))
r1, r2 = 1.0, 1.524; at = (r1 + r2) / 2; tt = .5 * at ** 1.5
print("Earth->Mars: transfer time (yr):", round(tt, 4), "(days:", round(tt * 365.25), ") lead angle:", round(180 - 360 * tt / 1.524 ** 1.5, 1), "deg")

print("--- Module 8")
R_ = 1.0; print("div theorem F=r: flux =", 4 * np.pi * R_ ** 3, " volume integral 3V =", 3 * 4 / 3 * np.pi * R_ ** 3)
print("Stokes F=(-y,x,0): circulation 2 pi R^2 =", round(2 * np.pi, 4), "  curl flux = 2 * pi R^2 =", round(2 * np.pi, 4))
print("Torricelli h=1.25: v =", round(np.sqrt(2 * g * 1.25), 3), " venturi: v2 = 5, dp =", .5 * 1000 * (25 - 4), "Pa")

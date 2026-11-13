"""Recomputes every worked number quoted in the Fluid Mechanics concept notes added alongside fm_concepts_viz.py.
Run `python fm_concepts_check.py`; each line is `label  value  (note)`.  Nothing here is imported elsewhere."""
from math import pi, sqrt, log10, log, exp, atan, degrees, cos, radians

g = 9.81
rho_w = 998.0
out = []


def show(label, value, note=""):
    out.append((label, value, note))
    print(f"{label:<58s} {value:>14.5g}  {note}")


# ---- density, compressibility -------------------------------------------------------------------------------------
show("air rho (20C, 101325 Pa)", 101325 / (287 * 293.15), "kg/m3  Density")
show("speed of sound air 20C", sqrt(1.4 * 287 * 293.15), "m/s")
show("water dV/V at 100 atm", 10.13e6 / 2.2e9 * 100, "%  K=2.2 GPa")
show("gamma water", rho_w * g, "N/m3")
show("stagnation rho rise at Ma 0.3 (Ma^2/2)", 0.3 ** 2 / 2 * 100, "%")

# ---- surface tension ----------------------------------------------------------------------------------------------
show("droplet R=0.5mm dp=2s/R", 2 * 0.0728 / 0.0005, "Pa")
show("soap bubble R=25mm dp=4s/R", 4 * 0.025 / 0.025, "Pa")
show("capillary length water", sqrt(0.0728 / (rho_w * g)) * 1e3, "mm")
show("water-glass rise d=1mm", 4 * 0.0728 / (rho_w * g * 0.001) * 1e3, "mm")
show("water-glass rise d=3mm", 4 * 0.0728 / (rho_w * g * 0.003) * 1e3, "mm")
show("mercury depression d=2mm (th=140, rho=13550, s=.48)", 4 * 0.48 * cos(radians(140)) / (13550 * g * 0.002) * 1e3, "mm")

# ---- cavitation ---------------------------------------------------------------------------------------------------
show("siphon/suction head limit water 20C", (101325 - 2339) / (rho_w * g), "m")
show("venturi onset V1 (A1/A2=1/0.3,p1=150kPa)", sqrt(2 * (150e3 - 2339) / (rho_w * ((1 / 0.3) ** 2 - 1))), "m/s")
show("NPSHa: tank 2 m above, p=101.3kPa, pv=2.339, loss 0.8", (101325 - 2339) / (rho_w * g) + 2 - 0.8, "m")

# ---- angular momentum: sprinkler ----------------------------------------------------------------------------------
Q = 3e-4
A = pi * 0.005 ** 2 / 4
Vrel = (Q / 2) / A
R = 0.15
mdot = rho_w * Q
show("sprinkler Vrel", Vrel, "m/s")
show("sprinkler standstill torque", mdot * R * Vrel, "N.m")
show("sprinkler free-spin omega", Vrel / R, "rad/s")
show("sprinkler free-spin rpm", Vrel / R * 60 / (2 * pi), "rpm")
om_f = (Vrel - 0.05 / (mdot * R)) / R
show("sprinkler omega with 0.05 N.m friction", om_f, "rad/s")
show("sprinkler rpm with friction", om_f * 60 / (2 * pi), "rpm")

# ---- moving control volume ----------------------------------------------------------------------------------------
show("rocket initial acceleration", 10 * 2000 / 500 - g, "m/s2")
show("jet on fixed plate rho A V^2", rho_w * 1e-3 * 20 ** 2, "N")
show("jet on plate moving at 8 m/s rho A (V-U)^2", rho_w * 1e-3 * (20 - 8) ** 2, "N")
show("jet on series of plates rho A V (V-U)", rho_w * 1e-3 * 20 * (20 - 8), "N")

# ---- dimensionless groups -----------------------------------------------------------------------------------------
show("Re water 25mm pipe 2 m/s", 2 * 0.025 / 1.0e-6, "")
show("Re air 30 m/s 1 m", 30 * 1 / 1.5e-5, "")
show("Fr ship L=100 U=10", 10 / sqrt(g * 100), "")
show("We 1 mm drop 5 m/s", rho_w * 25 * 0.001 / 0.0728, "")

# ---- similarity ---------------------------------------------------------------------------------------------------
show("ship model 1:25 speed", 10 * sqrt(1 / 25), "m/s")
show("ship model force ratio 1/25^3", 1 / 25 ** 3, "")
Vm = 30 * 4 * (1.0e-6 / 1.5e-5)
show("1:4 car in water Vm", Vm, "m/s")
show("force ratio rho nu^2", (998 * (1e-6) ** 2) / (1.2 * (1.5e-5) ** 2), "")
show("force ratio by CD route", (998 / 1.2) * (Vm / 30) ** 2 / 16, "")

# ---- continuity / kinematics --------------------------------------------------------------------------------------
show("accel tank tan(theta)=a/g, a=3", 3 / g, "")
show("accel tank theta", degrees(atan(3 / g)), "deg")
show("rotating tank rise Omega=10, r=0.1", 10 ** 2 * 0.1 ** 2 / (2 * g), "m")
# element V=(3y,2x)
show("element: omega_z (u=3y, v=2x)", .5 * (2 - 3), "1/s")
show("element: shear-rate gamma_dot", 3 + 2, "1/s")
# Rankine
Om, Rc = 10.0, 0.5
Gam = 2 * pi * Om * Rc ** 2
show("Rankine Gamma", Gam, "m2/s")
show("Rankine vmax", Om * Rc, "m/s")
show("Rankine v at r=2", Gam / (2 * pi * 2), "m/s")

# ---- Bernoulli ----------------------------------------------------------------------------------------------------
show("Torricelli h=2", sqrt(2 * g * 2), "m/s")
A1 = pi * 0.1 ** 2 / 4
A2 = pi * 0.05 ** 2 / 4
V1 = 2.0
dp = 0.5 * rho_w * ((V1 * A1 / A2) ** 2 - V1 ** 2)
show("venturi dp for V1=2, area ratio 4", dp, "Pa")
show("venturi Q", A1 * V1 * 1e3, "L/s")
show("stagnation: q at 60 m/s sea-level air", 0.5 * 1.225 * 60 ** 2, "Pa")
show("Ma at 60 m/s (a=340.3)", 60 / 340.3, "")
show("compressibility correction Ma^2/4", (60 / 340.3) ** 2 / 4 * 100, "%")
show("Pitot air 550 Pa", sqrt(2 * 550 / 1.225), "m/s")
show("Pitot water, Hg manometer h=50 mm", sqrt(2 * g * 0.05 * (13.6 - 1)), "m/s")

# ---- stress / viscous ---------------------------------------------------------------------------------------------
show("Couette wall shear mu=.1,U=2,h=2mm", 0.1 * 2 / 0.002, "Pa")
mu_i = 0.01 / (0.1 + 0.01)
show("two-fluid Couette interface velocity", mu_i, "m/s")
show("two-fluid Couette shear", 0.1 * mu_i / 0.001, "Pa")
U = 3000 * 2 * pi / 60 * 0.025
tau = 0.05 * U / 1e-4
F = tau * pi * 0.05 * 0.04
show("journal bearing U", U, "m/s")
show("journal bearing tau", tau, "Pa")
show("journal bearing F", F, "N")
show("journal bearing torque", F * 0.025, "N.m")
show("journal bearing power", F * 0.025 * (3000 * 2 * pi / 60), "W")
# plane Poiseuille
h = 1e-3
mu = 1e-3
G = 100.0
show("plane Poiseuille umax", G * h ** 2 / (8 * mu), "m/s")
show("plane Poiseuille mean", G * h ** 2 / (12 * mu), "m/s")
show("plane Poiseuille q", G * h ** 3 / (12 * mu), "m2/s")
show("plane Poiseuille Re", rho_w * (G * h ** 2 / (12 * mu)) * h / mu, "")
show("plane Poiseuille tau_w", G * h / 2, "Pa")
# Hagen-Poiseuille
d = 0.002
L = 1.0
Qh = 1e-6
dpH = 128 * mu * L * Qh / (pi * d ** 4)
Vh = Qh / (pi * d ** 2 / 4)
show("HP dp", dpH, "Pa")
show("HP V", Vh, "m/s")
show("HP Re", rho_w * Vh * d / mu, "")
show("HP tau_w 8 mu V/d", 8 * mu * Vh / d, "Pa")
show("HP entry length 0.06 Re d", 0.06 * rho_w * Vh * d / mu * d * 1e3, "mm")
show("HP umax", 2 * Vh, "m/s")

# ---- pipe flow ----------------------------------------------------------------------------------------------------
show("V crit water 25 mm Re 2300", 2300 * 1.0e-6 / 0.025, "m/s")
show("turbulent entry 4.4 Re^(1/6)", 4.4 * 50000 ** (1 / 6), "diameters")


def colebrook(Re, rel):
    f = 0.02
    for _ in range(60):
        f = (-2 * log10(rel / 3.7 + 2.51 / (Re * sqrt(f)))) ** -2
    return f


def haaland(Re, rel):
    return (-1.8 * log10((rel / 3.7) ** 1.11 + 6.9 / Re)) ** -2


D = 0.10
e = 0.046e-3
Qp = 0.01
nu = 1.01e-6
Vp = Qp / (pi * D ** 2 / 4)
Re = Vp * D / nu
rel = e / D
fc = colebrook(Re, rel)
fh = haaland(Re, rel)
show("pipe V", Vp, "m/s")
show("pipe Re", Re, "")
show("pipe e/D", rel, "")
show("pipe f Colebrook", fc, "")
show("pipe f Haaland", fh, "")
hl = fc * (100 / D) * Vp ** 2 / 2
show("pipe h_l (J/kg) L=100", hl, "")
show("pipe head (m)", hl / g, "")
show("pipe dp (kPa)", rho_w * hl / 1e3, "")
show("fully rough f", (-2 * log10(rel / 3.7)) ** -2, "")
show("f at Re=2.5e5", colebrook(2.5e5, rel), "")
show("f at Re=1e6", colebrook(1e6, rel), "")
show("f smooth Re=1.26e5 (e/D=0)", colebrook(Re, 1e-12), "")
show("viscous sublayer 5 nu/u_tau", 5 * nu / (Vp * sqrt(fc / 8)) * 1e3, "mm  vs e=0.046mm")
show("tau_w = f rho V^2/8", fc * rho_w * Vp ** 2 / 8, "Pa")
show("friction velocity", Vp * sqrt(fc / 8), "m/s")

# ---- energy equation / pump ---------------------------------------------------------------------------------------
V = sqrt(2 * g * 1.0)
Dm = 0.5
Qm = V * pi * Dm ** 2 / 4
Hp = 8 + 0.5 + 0.04 * 85 + 1.0
show("main V (V^2/2g=1m)", V, "m/s")
show("main Q", Qm, "m3/s")
show("Hp", Hp, "m")
show("water power", rho_w * g * Qm * Hp / 1e3, "kW")
show("shaft power eta=0.8", rho_w * g * Qm * Hp / 0.8 / 1e3, "kW")

# ---- minor losses -------------------------------------------------------------------------------------------------
fL = 0.025 * 20 / 0.05
SK = 0.5 + 2 * 0.025 * 30 + 0.025 * 8 + 1.0
show("system: f L/D", fL, "")
show("system: sum K", SK, "")
show("system: total head J/kg at V=2", (fL + SK) * 2, "")
show("system: head m", (fL + SK) * 2 / g, "")
show("system: dp kPa", rho_w * (fL + SK) * 2 / 1e3, "")
show("system: minor share", SK / (fL + SK) * 100, "%")
show("expansion A1/A2=0.25 K", (1 - 0.25) ** 2, "")
show("expansion V1=3, A1/A2=.25: loss J/kg", (1 - .25) ** 2 * 9 / 2, "")

# ---- pipe systems -------------------------------------------------------------------------------------------------
show("parallel Q ratio D 100 vs 50 mm", 2 ** 2.5, "")
show("parallel share large pipe", 2 ** 2.5 / (1 + 2 ** 2.5) * 100, "%")
Qop = sqrt(20 / 7000)
show("pump-system Q", Qop, "m3/s")
show("pump-system H", 10 + 2000 * Qop ** 2, "m")

# find Q: tank H=10 m, L=50 m, D=0.05, e=0.046 mm, Kent=0.5, free jet exit
D = 0.05
L = 50
H = 10
f = 0.02
for _ in range(30):
    Vq = sqrt(2 * g * H / (1 + 0.5 + f * L / D))
    Re = Vq * D / nu
    f = colebrook(Re, e / D)
show("find-Q: V", Vq, "m/s")
show("find-Q: Re", Re, "")
show("find-Q: f", f, "")
show("find-Q: Q L/s", Vq * pi * D ** 2 / 4 * 1e3, "")
f0 = (-2 * log10(e / D / 3.7)) ** -2
V0 = sqrt(2 * g * H / (1 + 0.5 + f0 * L / D))
show("find-Q: first guess fully-rough f", f0, "")
show("find-Q: first-guess V", V0, "")

"""Applied Mechanics Lab mock papers: every number in the answer keys is computed here.
Run: python aml_mock_core.py   (prints all results).  Units: N, mm, MPa unless a name says otherwise."""
import numpy as np
from math import pi, sqrt, atan, tan, degrees, radians, log

g = 9.81


# ------------------------------------------------------------------ the 2023 paper (model answers)
def real_paper():
    out = {}
    # Q2 hollow shaft di/do = 0.6, same torsional strength as a solid shaft
    k = 0.6
    out["q2_do_over_d"] = (1 - k**4) ** (-1 / 3)
    out["q2_mass_ratio"] = (1 - k**2) / (1 - k**4) ** (2 / 3)
    # Q3 mirror and scale: 5 mm at 50 mm
    phi = 0.5 * atan(5 / 50)
    out["q3_phi_rad"] = phi
    out["q3_phi_deg"] = degrees(phi)
    out["q3_small_angle"] = 5 / (2 * 50)
    # Q10 photoelastic beam, N=2, t=5 mm, f=8
    out["q10_sigma"] = 2 * 8 / 5
    # Q11 two beams: steel width b, brass width b/2 and rotated 90 deg; E_s = 2 E_b
    out["q11_ratio_h_over_b"] = {r: 16 * r**2 for r in (1.0, 1.5, 2.0)}   # delta_brass/delta_steel = 16 (h/b)^2
    # Q7c equal perimeter: circle vs square (and a 2:1 rectangle)
    P = 1.0
    I_circle = P**4 / (64 * pi**3)
    I_sq = (P / 4) ** 4 / 12
    b, h = P / 6, P / 3     # 2:1 rectangle with perimeter P: 2(b+h)=P -> b=P/6, h=P/3
    I_rect = h * b**3 / 12
    out["q7c"] = dict(I_circle=I_circle, I_square=I_sq, I_rect=I_rect, circle_over_square=I_circle / I_sq, circle_over_rect=I_circle / I_rect)
    # Q8 disk: N ~ 1/f
    out["q8_ratio"] = 8 / 0.2
    return out


# ------------------------------------------------------------------ Mock paper 1
def m1():
    o = {}
    # Q1 strain gauge on a cantilever: R=120, GF=2.1, steel E=200 GPa, 25 x 6 mm, P=20 N at 300 mm
    b, t, L, P, E, R, GF, Vex = 25.0, 6.0, 300.0, 20.0, 200e3, 120.0, 2.1, 5.0
    sigma = 6 * P * L / (b * t**2)
    eps = sigma / E
    o["q1"] = dict(sigma=sigma, eps_micro=eps * 1e6, dR=GF * R * eps, quarter_mV=Vex * GF * eps / 4 * 1e3, half_mV=Vex * GF * eps / 2 * 1e3,
                   full_mV=Vex * GF * eps * 1e3)
    # Q2 hollow (k=0.5) vs solid, same material, length and mass
    k = 0.5
    # same area: d^2 = do^2 (1-k^2)
    d_over_do = sqrt(1 - k**2)
    o["q2"] = dict(torque_ratio=(1 - k**4) / d_over_do**3, stiffness_ratio=(1 - k**4) / d_over_do**4, d_over_do=d_over_do)
    # Q3 mirror and scale, D = 1000 mm, s = 30 mm; d = 8 mm, L = 500 mm, T = 1.0 N m
    D, s = 1000.0, 30.0
    phi = 0.5 * atan(s / D)
    d, Ls, T = 8.0, 500.0, 1000.0
    J = pi * d**4 / 32
    o["q3"] = dict(phi_rad=phi, phi_deg=degrees(phi), small=s / (2 * D), J=J, G_GPa=T * Ls / (J * phi) / 1e3)
    # Q7 strut, 20 x 3 mm, L=600, E=210 GPa
    E, b, t, L = 210e3, 20.0, 3.0, 600.0
    I = b * t**3 / 12
    A = b * t
    r = sqrt(I / A)
    Pcr = lambda K: pi**2 * E * I / (K * L)**2
    o["q7"] = dict(I=I, r=r, lam_pinned=L / r, P_pp=Pcr(1.0), P_fp=Pcr(0.7), P_ff=Pcr(0.5), P_fixfree=Pcr(2.0), sigma_pp=Pcr(1.0) / A)
    # square vs circle equal area
    o["q7c"] = dict(sq_over_circ_area=(1 / 12) / (1 / (4 * pi)))
    # Q10 photoelastic beam: N=6 at extreme fibre, t=6 mm, f=10.5, depth 20 mm
    N, t, f, h = 6, 6.0, 10.5, 20.0
    sig = N * f / t
    o["q10"] = dict(sigma=sig, M=sig * t * h**2 / 6, N_at_quarter_depth=N / 2)
    # Q11 steel flat vs aluminium on edge, same 20 x 10 section
    Es, Ea = 200e3, 70e3
    I_flat = 20 * 10**3 / 12
    I_edge = 10 * 20**3 / 12
    o["q11"] = dict(I_flat=I_flat, I_edge=I_edge, steel_flat_vs_edge=I_edge / I_flat, al_edge_over_steel_flat=(Es * I_flat) / (Ea * I_edge),
                    al_flat_over_steel_flat=(Es * I_flat) / (Ea * I_flat))
    # Q12 clamp ends: 48 -> 192 ; deeper section
    o["q12"] = dict(clamp=48 / 192, double_depth=1 / 8, edge_vs_flat=(10 / 20) ** 2)
    # Q13 four-point-like: supports L=600 mm apart, overhangs a=200, P=50 N at both tips; Al 25 x 6 (EI)
    P, L, a = 50.0, 600.0, 200.0
    EI = 70e3 * 25 * 6**3 / 12
    d_mid = P * a * L**2 / (8 * EI)
    th = P * a * L / (2 * EI)
    tip = th * a + P * a**3 / (3 * EI)
    o["q13"] = dict(EI=EI, uplift_mid=d_mid, theta=th, tip_down=tip, M=P * a)
    return o


# ------------------------------------------------------------------ Mock paper 2
def m2():
    o = {}
    # Q1 DIC strain from displacement
    o["q1"] = dict(eps=0.060 / 20.0, eps_micro=0.060 / 20.0 * 1e6)
    # Q2 shaft diameter halved
    o["q2"] = dict(tau=8, phi=16)
    # Q3 ES6: nut 3.20 mm, dial 2.90 mm, A0 = 9 mm2, L0 = 31 mm
    nut, dial, A0, L0 = 3.20, 2.90, 9.0, 31.0
    F = dial * 100
    ext = nut - dial
    o["q3"] = dict(F=F, ext=ext, sigma=F / A0, eps=ext / L0, spring_share=dial / nut)
    # Q4 true stress and strain: S=400, e=0.18, A0=78.5
    S, e, A0 = 400.0, 0.18, 78.54
    o["q4"] = dict(sigma_t=S * (1 + e), eps_t=log(1 + e), A=A0 / (1 + e), diff_pct=(S * (1 + e) - S) / S * 100)
    # Q7 strut 25 x 3 steel, 400 mm, E 210
    E, b, t, L = 210e3, 25.0, 3.0, 400.0
    I = b * t**3 / 12
    o["q7"] = dict(I=I, P_pp=pi**2 * E * I / L**2, P_fp=pi**2 * E * I / (0.7 * L)**2, P_ff=pi**2 * E * I / (0.5 * L)**2,
                   P_fp_shorter=pi**2 * E * I / (0.7 * (L - 20))**2, r=sqrt(I / (b * t)), lam=L / sqrt(I / (b * t)), sigma_cr=pi**2 * E * I / L**2 / (b * t))
    # Q10 tensile test, d=10, L0=50, Py=19.6 kN, Pmax=31.4 kN, Lf=63, df=6
    d, L0, Py, Pm, Lf, df = 10.0, 50.0, 19.6e3, 31.4e3, 63.0, 6.0
    A0 = pi * d**2 / 4
    o["q10"] = dict(A0=A0, sy=Py / A0, su=Pm / A0, EL=(Lf - L0) / L0 * 100, RA=(d**2 - df**2) / d**2 * 100)
    # Q11 load at L/4: ratios with centre load
    a_, b_ = 0.25, 0.75
    y_load = a_**2 * b_**2 / 3                          # P L^3 / EI
    y_max = a_ * (1 - a_**2) ** 1.5 / (9 * sqrt(3))        # a_ is the SHORTER distance
    xm = sqrt((1 - a_**2) / 3)                              # from the far support; 1 - xm from the near one
    y_c = 1 / 48
    o["q11"] = dict(y_load=y_load, y_max=y_max, x_max=xm, y_c=y_c, load_over_c=y_load / y_c, max_over_c=y_max / y_c,
                    steel_over_al=1 / 3, depth_ratio=3 ** (1 / 3))
    # Q12 cantilever 4 mm: 20 % shorter, 20 % deeper, both
    o["q12"] = dict(shorter=4 * 0.8**3, deeper=4 / 1.2**3, both=4 * 0.8**3 / 1.2**3)
    # Q13 self weight of overhang, Al 25 x 6, L=400, l=60, W=24.5 N
    E, b, t, L, l, W = 70e3, 25.0, 6.0, 400.0, 60.0, 24.5
    I = b * t**3 / 12
    EI = E * I
    w = 2700 * (b * t * 1e-6) * g / 1000                 # N/mm
    d1 = W * L**3 / (48 * EI)
    d2 = 5 * w * L**4 / (384 * EI)
    M0 = w * l**2 / 2
    d3 = M0 * L**2 / (8 * EI)
    o["q13"] = dict(EI=EI, w=w, d_load=d1, d_selfweight=d2, d_overhang_relief=d3, total=d1 + d2 - d3, tip_up=(W * L**2 / (16 * EI)) * l, M0=M0)
    return o


# ------------------------------------------------------------------ Mock paper 3
def m3():
    o = {}
    # Q1 three-point bending: Al 25 x 6, L=400, P=2.5 kg
    b, t, L, E, P = 25.0, 6.0, 400.0, 70e3, 2.5 * g
    I = b * t**3 / 12
    o["q1"] = dict(P=P, I=I, delta=P * L**3 / (48 * E * I), k=48 * E * I / L**3, sigma=3 * P * L / (2 * b * t**2))
    # Q2 shaft 5 kW at 1500 rpm, tau 40 MPa
    T = 5e3 * 60 / (2 * pi * 1500) * 1e3
    o["q2"] = dict(T_Nm=T / 1e3, d=(16 * T / (pi * 40)) ** (1 / 3))
    # Q3 torsion: steel 0.86 deg -> brass, Al
    G = dict(steel=79.6, brass=38.0, Al=25.5)
    o["q3"] = {k: 0.86 * G["steel"] / v for k, v in G.items()}
    # Q4 two gauges on a tension bar: axial 500, transverse -150 micro; E=210
    ea, et = 500e-6, -150e-6
    o["q4"] = dict(nu=-et / ea, sigma=210e3 * ea, gain=(1 + (-et / ea)))
    # Q5 ES6 resolution: 0.01 mm over 31 mm for steel
    o["q5"] = dict(eps=0.01 / 31, sigma_steel=200e3 * 0.01 / 31, sigma_al=70e3 * 0.01 / 31, frac_of_yield=200e3 * 0.01 / 31 / 250)
    # Q6 strut transition length: 25 x 3, sigma_p=200, E=210
    E, sp = 210e3, 200.0
    lam_p = pi * sqrt(E / sp)
    r = 3 / sqrt(12)
    o["q6"] = dict(lam_p=lam_p, r=r, L_crit=lam_p * r)
    # Q7 photoelastic disk D=40, t=6, f=8, P=600 N
    P, D, f = 600.0, 40.0, 8.0
    N = 8 * P / (pi * D * f)
    o["q7"] = dict(N=N, N_double=2 * N, N_f02=8 * P / (pi * D * 0.2), sigma_diff=8 * P / (pi * D * 6))
    # Q10 load at L/4
    o["q10"] = dict(under_load=9 / 16 * 1.0, max=(0.25 * (1 - 0.0625) ** 1.5 / (9 * sqrt(3))) / (1 / 48), xmax_from_far=sqrt((1 - 0.0625) / 3), xmax_from_near=1 - sqrt((1 - 0.0625) / 3))
    # Q11 b x h vs 2b x h/2
    o["q11"] = dict(defl=4.0, stress=2.0)
    # Q12 ruler 25 x 3 flat vs edge
    o["q12"] = dict(ratio=(25 / 3) ** 2)
    # Q13 overhang with two loads: L=0.8 m span, a=0.2 m overhang, P at mid and at tip (unit loads)
    L, a, P = 0.8, 0.2, 1.0
    RA = P * L / 2 / L - P * a / L        # moments about B (B at x=L)
    x_contra = (P * L / 2) / (P - RA * 0) if False else None
    # M(x) = RA x - P<x-L/2>  -> zero for x > L/2 when RA x = P (x - L/2)  ->  x = (P L/2)/(P-RA)
    xc = (P * L / 2) / (P - RA)
    o["q13"] = dict(RA=RA, RB=2 * P - RA, M_mid=RA * L / 2, M_B=-P * a, x_contra=xc, x_contra_over_L=xc / L)
    return o


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for name in ("real_paper", "m1", "m2", "m3"):
        print("==", name)
        for k, v in globals()[name]().items():
            if isinstance(v, dict):
                print("  ", k, {kk: (round(float(vv), 5) if not isinstance(vv, dict) else vv) for kk, vv in v.items()})
            else:
                print("  ", k, round(float(v), 5))

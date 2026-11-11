"""Strength of Materials question bank: every number in the four question-bank notes is computed here.
Units: N, mm, MPa unless a variable name says otherwise.   Run: python sm_bank_core.py   (prints all results)
Each problem is an independent function returning a dict; where possible the answer is checked a second way
(numerical integration, brute-force search or a closed-form identity)."""
import numpy as np
from math import pi, sqrt, sin, cos, tan, atan, atan2, radians, degrees, exp, log
from scipy.optimize import brentq

g = 9.81


# =========================================================================== PART 1: axial, thermal, torsion
def p1_n1():
    """stepped bar, steel AB + aluminium BC, 100 kN pull at B, 60 kN push at C (towards the wall)."""
    Es, Ea = 200e3, 70e3
    dAB, LAB, dBC, LBC = 40, 800, 25, 600
    AAB, ABC = pi * dAB**2 / 4, pi * dBC**2 / 4
    P_BC, P_AB = -60e3, 100e3 - 60e3
    dAB_ = P_AB * LAB / (AAB * Es)
    dBC_ = P_BC * LBC / (ABC * Ea)
    return dict(AAB=AAB, ABC=ABC, P_AB=P_AB, P_BC=P_BC, sAB=P_AB / AAB, sBC=P_BC / ABC, dAB=dAB_, dBC=dBC_, dC=dAB_ + dBC_)


def p1_n2():
    """rigid bar pinned at A; steel wire at x=1 m, aluminium wire at x=2 m; load P at x=3 m."""
    Es, Ea = 200e3, 70e3
    d1, L1, d2, L2 = 6, 2000, 8, 1500
    A1, A2 = pi * d1**2 / 4, pi * d2**2 / 4
    P = 8e3
    k1, k2 = A1 * Es / L1, A2 * Ea / L2            # wire stiffnesses N/mm
    # rotation theta at A:  stretch1 = 1000 th, stretch2 = 2000 th ; moments about A: F1*1000+F2*2000 = P*3000
    th = P * 3000 / (k1 * 1000**2 + k2 * 2000**2)
    F1, F2 = k1 * 1000 * th, k2 * 2000 * th
    return dict(A1=A1, A2=A2, k1=k1, k2=k2, F1=F1, F2=F2, s1=F1 / A1, s2=F2 / A2, d1=1000 * th, d2=2000 * th, dP=3000 * th)


def p1_n3():
    """steel rod in copper tube between rigid plates: 80 kN compression and dT=+40 C."""
    Es, Ec, as_, ac = 200e3, 110e3, 12e-6, 17e-6
    As, Ac = pi * 20**2 / 4, 600.0
    P, dT = 80e3, 40.0
    # F_s + F_c = -P (compression negative);  F_s/(As Es) + as dT = F_c/(Ac Ec) + ac dT
    # solve linear system
    M = np.array([[1, 1], [1 / (As * Es), -1 / (Ac * Ec)]])
    rhs = np.array([-P, (ac - as_) * dT])
    Fs, Fc = np.linalg.solve(M, rhs)
    L = 400.0
    dL = (Fs / (As * Es) + as_ * dT) * L
    return dict(As=As, Ac=Ac, Fs=Fs, Fc=Fc, ss=Fs / As, sc=Fc / Ac, dL=dL,
                Fs_thermal_only=np.linalg.solve(M, np.array([0, (ac - as_) * dT]))[0])


def p1_n4():
    """steel bar between rigid walls, 1.0 mm gap, heated 80 C."""
    E, a, L, A, gap, dT = 200e3, 12e-6, 2000.0, 500.0, 1.0, 80.0
    free = a * dT * L
    comp = max(free - gap, 0)
    s = E * comp / L
    return dict(free=free, comp=comp, sigma=s, F=s * A, dT_contact=gap / (a * L), eps=comp / L)


def p1_n5():
    """vertical rod, L=15 m, d=12 mm, 8 kN at the bottom, own weight."""
    E, rho, L, d, P = 200e3, 7850.0, 15.0, 12.0, 8e3
    A = pi * d**2 / 4
    W = rho * g * (A * 1e-6) * L
    s_top = (P + W) / A
    dl = P * L * 1e3 / (A * E) + rho * g * (L**2) / (2 * E * 1e6) * 1e3   # mm
    return dict(A=A, W=W, s_top=s_top, s_load=P / A, dl=dl, dl_P=P * L * 1e3 / (A * E), dl_w=W * L * 1e3 / (2 * A * E))


def p1_n6():
    """steel plate generalized Hooke: sx=120, sy=-40, sz=0 (and plane strain version)."""
    E, nu = 200e3, 0.3
    sx, sy = 120.0, -40.0
    ex = (sx - nu * sy) / E
    ey = (sy - nu * sx) / E
    ez = -nu * (sx + sy) / E
    dV = ex + ey + ez
    t, b, h = 10, 100, 50
    dt = ez * t
    V = b * h * t
    # plane strain (ez=0): sz = nu (sx+sy)
    sz = nu * (sx + sy)
    K = E / (3 * (1 - 2 * nu))
    return dict(ex=ex, ey=ey, ez=ez, dV=dV, dt=dt, V=V, dVol=dV * V, sz_pe=sz, K=K, G=E / (2 * (1 + nu)))


def p1_n7():
    """hollow shaft, 60 kW at 300 rpm, di/do=0.6, tau_allow 60 MPa, twist <=1 deg/m, G=80 GPa."""
    P, N, k, tau, G = 60e3, 300.0, 0.6, 60.0, 80e3
    T = P * 60 / (2 * pi * N) * 1e3                                    # N mm
    do_s = (16 * T / (pi * tau * (1 - k**4))) ** (1 / 3)
    th = radians(1) / 1000                                              # rad per mm
    do_t = (32 * T / (pi * G * th * (1 - k**4))) ** 0.25
    do = max(do_s, do_t)
    J = pi * do**4 * (1 - k**4) / 32
    # solid shaft for same strength
    d_solid_s = (16 * T / (pi * tau)) ** (1 / 3)
    d_solid_t = (32 * T / (pi * G * th)) ** 0.25
    d_solid = max(d_solid_s, d_solid_t)
    A_h = pi / 4 * do**2 * (1 - k**2)
    A_s = pi / 4 * d_solid**2
    return dict(T_Nm=T / 1e3, do_s=do_s, do_t=do_t, do=do, di=k * do, J=J, tau_actual=T * do / 2 / J, theta_deg_per_m=degrees(T / (G * J)) * 1000,
                d_solid_s=d_solid_s, d_solid_t=d_solid_t, d_solid=d_solid, mass_ratio=A_h / A_s)


def p1_n8():
    """solid shaft d=40, L=1.5 m, fixed both ends, 800 N m at 0.6 m from A."""
    d, L, a, T, G = 40.0, 1500.0, 600.0, 800e3, 80e3
    b = L - a
    J = pi * d**4 / 32
    TA, TB = T * b / L, T * a / L
    tauA, tauB = 16 * TA / (pi * d**3), 16 * TB / (pi * d**3)
    phiC = TA * a / (G * J)
    return dict(J=J, TA=TA / 1e3, TB=TB / 1e3, tauA=tauA, tauB=tauB, phiC=phiC, phiC_deg=degrees(phiC), phi_check=TB * b / (G * J))


def p1_n9():
    """steel tube (50/40) bonded over brass core (d=40), T=1.5 kN m."""
    Gs, Gb, T = 80e3, 38e3, 1.5e6
    Js = pi * (50**4 - 40**4) / 32
    Jb = pi * 40**4 / 32
    Ts = T * Gs * Js / (Gs * Js + Gb * Jb)
    Tb = T - Ts
    tau_s = Ts * 25 / Js
    tau_b = Tb * 20 / Jb
    # shear stress in steel at the interface (r=20) vs brass at the interface (r=20): jump G ratio
    tau_s_int = Ts * 20 / Js
    phi_per_L = Ts / (Gs * Js)
    return dict(Js=Js, Jb=Jb, Ts=Ts / 1e3, Tb=Tb / 1e3, tau_s=tau_s, tau_b=tau_b, tau_s_int=tau_s_int, twist_deg_per_m=degrees(phi_per_L) * 1000)


# =========================================================================== PART 2: beams
def beam_ss(L, loads, n=2001):
    """simply supported beam: loads list of ('P', x, P_down) and ('w', x1, x2, w_down). returns x, V, M, RA, RB"""
    x = np.linspace(0, L, n)
    RA = RB = 0.0
    mom_A = 0.0
    tot = 0.0
    for ld in loads:
        if ld[0] == 'P':
            _, a, P = ld; tot += P; mom_A += P * a
        else:
            _, a, b, w = ld; F = w * (b - a); tot += F; mom_A += F * (a + b) / 2
    RB = mom_A / L; RA = tot - RB
    V = np.full_like(x, RA); M = RA * x
    for ld in loads:
        if ld[0] == 'P':
            _, a, P = ld
            V = V - P * (x > a); M = M - P * np.clip(x - a, 0, None)
        else:
            _, a, b, w = ld
            V = V - w * np.clip(np.minimum(x, b) - a, 0, None)
            xm = np.clip(x - a, 0, b - a)
            M = M - w * xm * (np.clip(x, a, b) - a) / 2 - np.where(x > b, w * (b - a) * (x - b), 0) * 1
            # careful: partial UDL moment = integral; recompute below for exactness
    # exact recompute of M by integrating V
    M = np.concatenate([[0], np.cumsum((V[1:] + V[:-1]) / 2 * np.diff(x))])
    return x, V, M, RA, RB


def p2_n1():
    """SS beam L=8 m: UDL 10 kN/m full span + 20 kN at 3 m."""
    L = 8.0
    x, V, M, RA, RB = beam_ss(L, [('w', 0, 8, 10.0), ('P', 3.0, 20.0)], 8001)
    i = np.argmax(M)
    # analytic: V=0 in segment x>3: RA - 20 - 10 x = 0
    xm = (RA - 20) / 10
    Mm = RA * xm - 20 * (xm - 3) - 5 * xm**2
    return dict(RA=RA, RB=RB, x_zero=xm, Mmax=Mm, Mmax_num=M[i], x_num=x[i], M_at_load=RA * 3 - 5 * 9, V_left=RA - 30, V_right=RA - 50)


def p2_n2():
    """overhanging beam: supports A (x=0), C (x=6), overhang to D (x=8). UDL 12 kN/m on AC, 18 kN down at D."""
    w, P, L, ov = 12.0, 18.0, 6.0, 2.0
    # moments about A: RC*6 = 12*6*3 + 18*8
    RC = (w * L * L / 2 + P * (L + ov)) / L
    RA = w * L + P - RC
    x = np.linspace(0, L + ov, 8001)
    V = np.where(x <= L, RA - w * x, RA + RC - w * L - P + P)   # placeholder, rebuild properly below
    V = RA - w * np.clip(x, 0, L) + RC * (x > L) - P * (x > L + ov - 1e-9) * 0
    M = np.zeros_like(x)
    # M(x) from the right end: overhang part
    for i, xx in enumerate(x):
        if xx <= L:
            M[i] = RA * xx - w * xx**2 / 2
        else:
            M[i] = -P * (L + ov - xx)
    Mc = -P * ov
    # contraflexion in AC: RA x - w x^2/2 = 0 -> x = 2 RA / w
    xc = 2 * RA / w
    xm = RA / w
    Mmax = RA * xm - w * xm**2 / 2
    return dict(RA=RA, RC=RC, Mc=Mc, x_contra=xc, x_Vzero=xm, Mmax=Mmax, V_Cleft=RA - w * L, V_Cright=RA - w * L + RC)


def p2_n3():
    """T-section: flange 120 x 20 on top, web 20 x 100 below (total 120). M=8 kN m sagging."""
    bf, tf, bw, hw = 120.0, 20.0, 20.0, 100.0
    A1, A2 = bf * tf, bw * hw
    y1, y2 = hw + tf / 2, hw / 2              # from the bottom
    ybar = (A1 * y1 + A2 * y2) / (A1 + A2)
    I = bf * tf**3 / 12 + A1 * (y1 - ybar)**2 + bw * hw**3 / 12 + A2 * (y2 - ybar)**2
    M = 8e6
    c_top, c_bot = (hw + tf) - ybar, ybar
    s_top, s_bot = -M * c_top / I, M * c_bot / I     # top compression (sagging), bottom tension
    # section moduli
    # cast iron: sigma_allow 30 (T), 90 (C).  Upright T: tension on the web side (c_bot).  Inverted T: tension on the flange side (c_top).
    up = min(30 * I / c_bot, 90 * I / c_top) / 1e6
    inv = min(30 * I / c_top, 90 * I / c_bot) / 1e6
    return dict(A=A1 + A2, ybar=ybar, I=I, c_top=c_top, c_bot=c_bot, s_top=s_top, s_bot=s_bot, Z_top=I / c_top, Z_bot=I / c_bot,
                M_allow_upright=up, M_allow_inverted=inv, gain=inv / up)


def p2_n4():
    """built-up I: flanges 100 x 12 top and bottom, web 10 x 150; V=60 kN."""
    bf, tf, tw, hw = 100.0, 12.0, 10.0, 150.0
    H = hw + 2 * tf
    I = tw * hw**3 / 12 + 2 * (bf * tf**3 / 12 + bf * tf * (hw / 2 + tf / 2)**2)
    V = 60e3
    Qflange = bf * tf * (hw / 2 + tf / 2)
    Q_na = Qflange + tw * (hw / 2) * (hw / 4)
    tau_na = V * Q_na / (I * tw)
    tau_j_web = V * Qflange / (I * tw)
    tau_j_fl = V * Qflange / (I * bf)
    # fraction of V carried by web: integrate tau over web
    y = np.linspace(-hw / 2, hw / 2, 4001)
    Qy = Qflange + tw * ((hw / 2)**2 - y**2) / 2
    tau = V * Qy / (I * tw)
    Vweb = np.trapezoid(tau * tw, y)
    return dict(H=H, I=I, Qflange=Qflange, Q_na=Q_na, tau_na=tau_na, tau_j_web=tau_j_web, tau_j_fl=tau_j_fl, Vweb=Vweb / 1e3, frac=Vweb / V,
                tau_avg_web=V / (tw * hw))


def p2_n5():
    """wood 100 wide x 200 deep, steel plate 100 x 10 attached at the bottom; M=12 kN m. Es/Ew=20."""
    n = 20.0
    bw, hw, bs, ts = 100.0, 200.0, 100.0, 10.0
    # transform steel to wood: width n*bs
    Aw, As = bw * hw, n * bs * ts
    yw, ys = ts + hw / 2, ts / 2                # from the bottom of steel
    yb = (Aw * yw + As * ys) / (Aw + As)
    I = bw * hw**3 / 12 + Aw * (yw - yb)**2 + n * bs * ts**3 / 12 + As * (ys - yb)**2
    M = 12e6
    top = hw + ts - yb
    s_wood_top = -M * top / I
    s_wood_bot = M * (yb - ts) / I                         # wood at its bottom face (tension)
    s_steel_bot = n * M * yb / I
    s_steel_top = n * M * (yb - ts) / I
    Iw_only = bw * hw**3 / 12
    return dict(yb=yb, I_tr=I, top=top, s_wood_top=s_wood_top, s_wood_bot=s_wood_bot, s_steel_bot=s_steel_bot, s_steel_top=s_steel_top,
                Iw_only=Iw_only, s_wood_alone=M * 100 / Iw_only)


def p2_n6():
    """two planks 150 x 25 form a T: flange on top, web 25 x 150 below, nailed; V = 3 kN, nail shear capacity 700 N."""
    bf, tf, bw, hw = 150.0, 25.0, 25.0, 150.0
    A1, A2 = bf * tf, bw * hw
    y1, y2 = hw + tf / 2, hw / 2
    yb = (A1 * y1 + A2 * y2) / (A1 + A2)
    I = bf * tf**3 / 12 + A1 * (y1 - yb)**2 + bw * hw**3 / 12 + A2 * (y2 - yb)**2
    Q = A1 * (y1 - yb)
    V, Fn = 3e3, 700.0
    q = V * Q / I
    s = Fn / q
    # two nails per cross-section
    s2 = 2 * Fn / q
    return dict(ybar=yb, I=I, Q=Q, q=q, s1=s, s2=s2)


def p2_n7():
    """cantilever 60 wide (z) x 120 deep (y), L=1.2 m, tip load 2 kN at 20 deg to the vertical."""
    b, h, L, P, th = 60.0, 120.0, 1200.0, 2e3, radians(20)
    Iz, Iy = b * h**3 / 12, h * b**3 / 12
    Mz, My = P * cos(th) * L, P * sin(th) * L
    # stress at corners (y=+-h/2, z=+-b/2): s = Mz y / Iz + My z / Iy  (magnitudes add at one pair of corners)
    s_max = Mz * (h / 2) / Iz + My * (b / 2) / Iy
    s_vert_only = P * L * (h / 2) / Iz
    alpha = atan((Iz / Iy) * (My / Mz))            # NA angle from z axis
    alpha_deg = degrees(atan((Iz / Iy) * tan(th)))
    return dict(Iz=Iz, Iy=Iy, Mz=Mz / 1e6, My=My / 1e6, s_max=s_max, s_vert_only=s_vert_only, na_deg=alpha_deg, ratio=s_max / s_vert_only)


def p2_n8():
    """short column 150 x 200, P=240 kN at e=40 mm along the 200 side."""
    b, h, P, e = 150.0, 200.0, 240e3, 40.0
    A = b * h
    I = b * h**3 / 12
    s0 = P / A
    sb = P * e * (h / 2) / I
    s_max, s_min = -(s0 + sb), -(s0 - sb)      # compression negative
    kern = h / 6
    # neutral axis: s=0 at y_na from centre where P/A = P e y / I  -> y = I/(A e) = h^2/(12 e)
    y_na = I / (A * e)
    tension_depth = h / 2 - y_na
    return dict(A=A, I=I, s0=s0, sb=sb, s_comp=s_max, s_other=s_min, kern=kern, y_na=y_na, tension_depth=tension_depth)


def p2_n9():
    """SS beam L=6 m, 24 kN centre, sigma_allow 120 MPa: circular vs 1:2 rectangle."""
    L, P, sa = 6.0, 24e3, 120.0
    M = P * L / 4 * 1e3                               # N mm
    S = M / sa
    d = (32 * S / pi) ** (1 / 3)
    h = (12 * S) ** (1 / 3)                            # b = h/2: S = b h^2/6 = h^3/12
    b = h / 2
    Ac, Ar = pi * d**2 / 4, b * h
    Vmax = P / 2
    tau_c = 4 * Vmax / (3 * Ac)
    tau_r = 1.5 * Vmax / Ar
    return dict(M=M / 1e6, S=S, d=d, h=h, b=b, Ac=Ac, Ar=Ar, ratio=Ac / Ar, tau_c=tau_c, tau_r=tau_r)


# =========================================================================== PART 3: transformation and vessels
def principal(sx, sy, txy):
    c = (sx + sy) / 2
    R = sqrt(((sx - sy) / 2)**2 + txy**2)
    th = 0.5 * atan2(2 * txy, sx - sy)
    return c, R, c + R, c - R, degrees(th)


def transform(sx, sy, txy, th_deg):
    t = radians(th_deg)
    c2, s2 = cos(2 * t), sin(2 * t)
    sn = (sx + sy) / 2 + (sx - sy) / 2 * c2 + txy * s2
    sn90 = (sx + sy) / 2 - (sx - sy) / 2 * c2 - txy * s2
    tn = -(sx - sy) / 2 * s2 + txy * c2
    return sn, sn90, tn


def p3_n1():
    sx, sy, txy = 80.0, -40.0, 30.0
    c, R, s1, s2, thp = principal(sx, sy, txy)
    sn, sn90, tn = transform(sx, sy, txy, 30)
    th_s = thp + 45
    return dict(c=c, R=R, s1=s1, s2=s2, thp=thp, tmax=R, th_s=th_s, s30=sn, s120=sn90, t30=tn,
                check_sum=sn + sn90, check_inv=sx + sy)


def p3_n2():
    """shaft d=50: T=1.2 kN m, P=60 kN, sY=280"""
    d, T, P, sY = 50.0, 1.2e6, 60e3, 280.0
    A = pi * d**2 / 4
    sx = P / A
    tau = 16 * T / (pi * d**3)
    c, R, s1, s2, thp = principal(sx, 0.0, tau)
    s_vm = sqrt(s1**2 - s1 * s2 + s2**2)
    s_tr = s1 - s2
    return dict(sx=sx, tau=tau, c=c, R=R, s1=s1, s2=s2, thp=thp, s_vm=s_vm, s_tresca=s_tr, FS_vm=sY / s_vm, FS_tr=sY / s_tr)


def p3_n3():
    """rosette 0/45/90: ea=620, eb=280, ec=-150 (micro); E=200 GPa, nu=0.3"""
    ea, eb, ec = 620e-6, 280e-6, -150e-6
    E, nu = 200e3, 0.3
    ex, ey = ea, ec
    gxy = 2 * eb - ea - ec
    c = (ex + ey) / 2
    R = sqrt(((ex - ey) / 2)**2 + (gxy / 2)**2)
    e1, e2 = c + R, c - R
    thp = 0.5 * degrees(atan2(gxy, ex - ey))
    s1 = E / (1 - nu**2) * (e1 + nu * e2)
    s2 = E / (1 - nu**2) * (e2 + nu * e1)
    sx = E / (1 - nu**2) * (ex + nu * ey)
    sy = E / (1 - nu**2) * (ey + nu * ex)
    txy = E / (2 * (1 + nu)) * gxy
    ez = -nu / (1 - nu) * (e1 + e2)
    return dict(ex=ex, ey=ey, gxy=gxy, c=c, R=R, e1=e1, e2=e2, thp=thp, s1=s1, s2=s2, sx=sx, sy=sy, txy=txy, gmax=2 * R, ez=ez)


def p3_n4():
    """thin cylinder r=250, t=5, steel E=200 nu=0.3: gauge at 30 deg to the axis reads 300 microstrain."""
    r, t, E, nu, th = 250.0, 5.0, 200e3, 0.3, radians(30)
    # per MPa of pressure
    sh, sl = r / t, r / (2 * t)
    eh, el = (sh - nu * sl) / E, (sl - nu * sh) / E
    e_th = el * cos(th)**2 + eh * sin(th)**2
    p = 300e-6 / e_th
    return dict(sh_per_p=sh, sl_per_p=sl, eh_per_p=eh, el_per_p=el, e_th_per_p=e_th, p=p, sh=sh * p, sl=sl * p, eh=eh * p, el=el * p)


def p3_n5():
    """cylinder d_i=1.2 m, p=2.5 MPa, sigma_allow=110, eta_long=0.7 (hoop), eta_circ=0.5 (longitudinal); sphere same."""
    d, p, sa, el_, ec_ = 1200.0, 2.5, 110.0, 0.7, 0.5
    t_hoop = p * d / (2 * sa * el_)
    t_long = p * d / (4 * sa * ec_)
    t_hoop_seamless = p * d / (2 * sa)
    t_sph = p * d / (4 * sa)
    t_sph_j = p * d / (4 * sa * 0.5)
    return dict(t_hoop=t_hoop, t_long=t_long, t=max(t_hoop, t_long), t_cyl_seamless=t_hoop_seamless, t_sphere=t_sph, ratio=t_sph / t_hoop_seamless, t_sph_j=t_sph_j)


def p3_n6():
    """thin cylinder d=800, t=8, L=2000, p=1.6, E=200, nu=0.28"""
    d, t, L, p, E, nu = 800.0, 8.0, 2000.0, 1.6, 200e3, 0.28
    sh, sl = p * d / (2 * t), p * d / (4 * t)
    eh, el = (sh - nu * sl) / E, (sl - nu * sh) / E
    dd, dL = eh * d, el * L
    dV = 2 * eh + el
    V = pi / 4 * d**2 * L
    # in-plane and absolute max shear (surface, sigma_3 = 0)
    return dict(sh=sh, sl=sl, eh=eh, el=el, dd=dd, dL=dL, dVV=dV, V_litres=V / 1e6, dV_litres=dV * V / 1e6, t_inplane=(sh - sl) / 2, t_abs=sh / 2,
                dd_formula=p * d**2 * (2 - nu) / (4 * t * E))


def p3_n7():
    """sx=-60, sy=-20, txy=-25: principal, in-plane and absolute max shear."""
    sx, sy, txy = -60.0, -20.0, -25.0
    c, R, s1, s2, thp = principal(sx, sy, txy)
    s3 = 0.0
    sset = sorted([s1, s2, s3], reverse=True)
    tabs = (sset[0] - sset[2]) / 2
    return dict(c=c, R=R, s1=s1, s2=s2, thp=thp, tinplane=R, tabs=tabs, sorted=sset)


def p3_n8():
    """strain Mohr: ex=400, ey=-200, gxy=300 (micro): principal strains, gmax, strain at 30 deg"""
    ex, ey, gxy = 400e-6, -200e-6, 300e-6
    c = (ex + ey) / 2
    R = sqrt(((ex - ey) / 2)**2 + (gxy / 2)**2)
    thp = 0.5 * degrees(atan2(gxy, ex - ey))
    t = radians(30)
    e30 = (ex + ey) / 2 + (ex - ey) / 2 * cos(2 * t) + gxy / 2 * sin(2 * t)
    return dict(c=c, R=R, e1=c + R, e2=c - R, thp=thp, gmax=2 * R, e30=e30)


# =========================================================================== PART 4: deflection, energy, columns
def p4_n1():
    """SS, w=12 kN/m, L=5 m, E=200 GPa, I=80e6 mm4"""
    w, L, E, I = 12.0, 5.0, 200e3, 80e6          # kN/m, m, MPa, mm4
    wN = w                                          # N/mm = kN/m
    Lmm = L * 1e3
    dmax = 5 * wN * Lmm**4 / (384 * E * I)
    th = wN * Lmm**3 / (24 * E * I)
    return dict(EI_kNm2=E * I * 1e-9, dmax=dmax, theta=th, theta_deg=degrees(th), span_over=Lmm / dmax)


def p4_n2():
    """cantilever L=3 m, P=10 kN at mid-span; tip deflection and slope. EI = 12000 kN m^2"""
    P, L, EI = 10.0, 3.0, 12000.0
    a = L / 2
    theta_a = P * a**2 / (2 * EI)
    dtip = P * a**3 / (3 * EI) + theta_a * (L - a)
    return dict(theta=theta_a, dtip=dtip * 1e3, closed=5 * P * L**3 / (48 * EI) * 1e3)


def p4_n3():
    """SS span L=4 m, overhang a=1.5 m with P=20 kN at the tip, EI=12000"""
    P, L, a, EI = 20.0, 4.0, 1.5, 12000.0
    M0 = P * a
    thC = M0 * L / (3 * EI)              # rotation at the support under the overhang from the span moment
    dtip = thC * a + P * a**3 / (3 * EI)
    dmid = M0 * L**2 / (16 * EI)         # uplift at mid-span
    # numerical check by direct integration
    xs = np.linspace(0, L + a, 4001)
    M = np.where(xs <= L, -M0 * xs / L, -P * (L + a - xs))
    # integrate EI v'' = M
    th = np.concatenate([[0], np.cumsum((M[1:] + M[:-1]) / 2 * np.diff(xs))]) / EI
    v = np.concatenate([[0], np.cumsum((th[1:] + th[:-1]) / 2 * np.diff(xs))])
    iL = np.argmin(abs(xs - L))
    c1 = -v[iL] / L                       # v(0)=0, v(L)=0 -> v += c1 x
    v = v + c1 * xs
    return dict(thC=thC, dtip=dtip * 1e3, dmid_up=dmid * 1e3, dtip_num=-v[-1] * 1e3, dmid_num=-v[np.argmin(abs(xs - L / 2))] * 1e3)


def p4_n4():
    """propped cantilever, UDL w=15 kN/m, L=6, prop at free end."""
    w, L = 15.0, 6.0
    RB = 3 * w * L / 8
    RA = w * L - RB
    MA = w * L**2 / 8
    xs = np.linspace(0, L, 6001)                 # from the wall
    M = -MA + RA * xs - w * xs**2 / 2
    imax = np.argmax(M)
    xc = brentq(lambda x: -MA + RA * x - w * x**2 / 2, 0.1, L - 1e-6)
    # deflection (EI=1): v'' = M
    th = np.concatenate([[0], np.cumsum((M[1:] + M[:-1]) / 2 * np.diff(xs))])
    v = np.concatenate([[0], np.cumsum((th[1:] + th[:-1]) / 2 * np.diff(xs))])
    xdm = xs[np.argmin(v)]
    return dict(RB=RB, RA=RA, MA=MA, Mpos=M[imax], x_Mpos=xs[imax], x_contra=xc, x_dmax=xdm, x_dmax_closed=L * 0.5785, v_end_check=v[-1])


def p4_n5():
    """SS L=8 m, 30 kN at 3 m, UDL 10 kN/m from 5 to 8 m, EI=40000 kN m^2 -> deflection at 4 m, location of max."""
    L, EI = 8.0, 40000.0
    # reactions
    F_udl, xbar = 30.0, 6.5
    RB = (30 * 3 + F_udl * xbar) / L
    RA = 30 + F_udl - RB

    def Mx(x):
        return RA * x - 30 * max(x - 3, 0) - 10 * max(x - 5, 0)**2 / 2

    xs = np.linspace(0, L, 16001)
    M = np.array([Mx(x) for x in xs])
    th = np.concatenate([[0], np.cumsum((M[1:] + M[:-1]) / 2 * np.diff(xs))]) / EI
    v = np.concatenate([[0], np.cumsum((th[1:] + th[:-1]) / 2 * np.diff(xs))])
    v = v - v[-1] * xs / L
    i4 = np.argmin(abs(xs - 4))
    imax = np.argmax(-v)
    # Macaulay constants
    # EI v = RA x^3/6 - 30<x-3>^3/6 - 10<x-5>^4/24 + C1 x  (C2=0)
    C1 = -(RA * L**3 / 6 - 30 * (L - 3)**3 / 6 - 10 * (L - 5)**4 / 24) / L
    def vm(x):
        return (RA * x**3 / 6 - 30 * max(x - 3, 0)**3 / 6 - 10 * max(x - 5, 0)**4 / 24 + C1 * x) / EI
    return dict(RA=RA, RB=RB, C1=C1, v4=vm(4) * 1e3, v4_num=v[i4] * 1e3, xmax=xs[imax], vmax=vm(xs[imax]) * 1e3, vmax_num=v[imax] * 1e3,
                v_mid=vm(4.0) * 1e3, th_A=C1 / EI)


def p4_n6():
    """L-frame: column h=2 m, horizontal arm a=1.5 m, P=5 kN down at free end; EI=8000 kN m^2"""
    P, a, h, EI = 5.0, 1.5, 2.0, 8000.0
    d_arm = P * a**3 / (3 * EI)
    d_col = P * a**2 * h / EI
    return dict(d_arm=d_arm * 1e3, d_col=d_col * 1e3, d_tot=(d_arm + d_col) * 1e3, M_wall=P * a)


def p4_n7():
    """impact: m=20 kg falls h=100 mm onto centre of a SS steel beam 40x40, L=1 m, E=200 GPa"""
    m, h, L, E, b = 20.0, 100.0, 1000.0, 200e3, 40.0
    I = b**4 / 12
    S = b**3 / 6
    W = m * g
    k = 48 * E * I / L**3
    dst = W / k
    dmax = dst * (1 + sqrt(1 + 2 * h / dst))
    n = dmax / dst
    F = k * dmax
    M = F * L / 4
    sig = M / S
    dmax_exact = None
    # with h measured to the contact point, energy balance: W (h + d) = 0.5 k d^2
    d2 = brentq(lambda d: 0.5 * k * d**2 - W * (h + d), 0, 100)
    sig_static = W * L / 4 / S
    return dict(I=I, S=S, k=k, dst=dst, dmax=dmax, d_energy=d2, n=n, F=F, M=M / 1e6, sigma=sig, sigma_static=sig_static, approx=sqrt(2 * h / dst) * dst)


def p4_n8():
    """Euler: steel tube 60 OD x 4 wall, L=3 m, E=200 GPa, sigma_Y=250, FS=2.5; pinned-pinned, pinned-fixed, fixed-fixed, fixed-free"""
    do, t, L, E, sY, FS = 60.0, 4.0, 3000.0, 200e3, 250.0, 2.5
    di = do - 2 * t
    A = pi / 4 * (do**2 - di**2)
    I = pi / 64 * (do**4 - di**4)
    r = sqrt(I / A)
    out = dict(A=A, I=I, r=r)
    for name, K in [("pinned-pinned", 1.0), ("fixed-pinned", 0.699), ("fixed-fixed", 0.5), ("fixed-free", 2.0)]:
        Pcr = pi**2 * E * I / (K * L)**2
        lam = K * L / r
        lam_c = pi * sqrt(2 * E / sY)
        sig_j = sY * (1 - sY * lam**2 / (4 * pi**2 * E))
        use = 'Euler' if lam >= lam_c else 'Johnson'
        P_use = Pcr if lam >= lam_c else sig_j * A
        out[name] = dict(K=K, lam=lam, Pcr_euler=Pcr / 1e3, sig_euler=Pcr / A, sig_johnson=sig_j, use=use, P=P_use / 1e3, allow=P_use / FS / 1e3)
    out["lam_transition"] = pi * sqrt(2 * E / sY)
    out["P_yield"] = sY * A / 1e3
    return out


def p4_n9():
    """intermediate column: steel, sY=250, E=200 GPa; A=1000 mm2? use r=20 mm, L_e=1.6 m -> lam=80; Johnson vs Euler vs Rankine."""
    E, sY = 200e3, 250.0
    r = 20.0
    res = {}
    for Le in (1200.0, 1600.0, 2400.0, 4000.0):
        lam = Le / r
        euler = pi**2 * E / lam**2
        johnson = sY * (1 - sY * lam**2 / (4 * pi**2 * E))
        rankine = 330.0 / (1 + lam**2 / 7500.0)          # textbook constants for mild steel, pinned ends
        use = 'Euler' if lam >= pi * sqrt(2 * E / sY) else 'Johnson'
        res[Le] = dict(lam=lam, euler=euler, johnson=johnson, rankine=rankine, use=use)
    res["lam_c"] = pi * sqrt(2 * E / sY)
    return res


def p4_n10():
    """secant formula: pinned steel column L=2.4 m, 100 x 60 section, load eccentric by e=6 mm in the 60 mm direction
    (bending about the weak axis, which is also the buckling axis); E=200 GPa, sY=250 MPa"""
    E, sY = 200e3, 250.0
    b, h, L, e = 100.0, 60.0, 2400.0, 6.0
    A = b * h
    I = b * h**3 / 12
    r2 = I / A
    c = h / 2

    def smax(P):
        return P / A * (1 + e * c / r2 / np.cos(L / (2 * sqrt(r2)) * sqrt(P / (E * A))))

    Pe = pi**2 * E * I / L**2
    P_allow = brentq(lambda P: smax(P) - sY, 1e3, 0.999 * Pe)
    P_lin = sY * A / (1 + e * c / r2)          # linearized (no deflection amplification)
    return dict(A=A, I=I, r2=r2, Pe=Pe / 1e3, P_secant=P_allow / 1e3, P_linear=P_lin / 1e3, P_yield=sY * A / 1e3, lam=L / sqrt(r2),
                s_at_half=smax(P_allow / 2))


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    np.set_printoptions(precision=5)
    for name in sorted(k for k in dict(globals()) if k.startswith("p") and k[1].isdigit() and "_n" in k):
        res = globals()[name]()
        print("==", name)
        for k, v in res.items():
            if isinstance(v, dict):
                print("   ", k, {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()})
            elif isinstance(v, float) or isinstance(v, np.floating):
                print("   ", k, round(float(v), 5))
            else:
                print("   ", k, v)

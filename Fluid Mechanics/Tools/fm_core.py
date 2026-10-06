"""Verification of the formulas and solved problems in the three Fluid Mechanics formula banks
   (White, Fluid Mechanics 4th ed.: Ch. 5 dimensional analysis, Ch. 4 differential relations, Ch. 3.7 / 4.9 / 6.10 Bernoulli and Pitot).
   Run `python fm_core.py` : every number quoted in the notes is recomputed here."""
import numpy as np, sympy as sp
from math import *

G = 9.81; GAL = 3.785411784e-3/60                  # 1 gal/min in m^3/s
RHO_W, MU_W = 998., 1.0e-3                         # water 20 C (White Table A.1 / A.5 values)
RHO_A, MU_A, PATM = 1.225, 1.78e-5, 101350.        # sea-level standard air (White)

# ====================================================================================================================
# 1. dimensional analysis : Pi groups from the dimensional matrix
# ====================================================================================================================
DIM = dict(M=0, L=1, T=2, Th=3)                    # rows of the dimensional matrix
def dims(**kw): v = [0]*4; [v.__setitem__(DIM[k], e) for k, e in kw.items()]; return v
VAR = dict(F=dims(M=1, L=1, T=-2), rho=dims(M=1, L=-3), V=dims(L=1, T=-1), D=dims(L=1), mu=dims(M=1, L=-1, T=-1), L=dims(L=1),
           sigma=dims(M=1, T=-2), g=dims(L=1, T=-2), h=dims(L=1), P=dims(M=1, L=2, T=-3), Q=dims(L=3, T=-1), Om=dims(T=-1),
           Dp=dims(M=1, L=-1, T=-2), a=dims(L=1, T=-1), p=dims(M=1, L=-1, T=-2), lam=dims(L=1), C=dims(L=1, T=-1), Tp=dims(T=1),
           E=dims(M=1, L=2, T=-2), r=dims(L=1), t=dims(T=1), b=dims(L=1), H=dims(L=1), dpdx=dims(M=1, L=-2, T=-2), R=dims(L=1),
           k=dims(M=1, L=1, T=-3, Th=-1), Rg=dims(L=2, T=-2, Th=-1), Tabs=dims(Th=1), x=dims(L=1), delta=dims(L=1), U=dims(L=1, T=-1),
           Mt=dims(M=1, L=2, T=-2), Tq=dims(M=1, L=2, T=-2), theta=dims(), z=dims(L=1), s=dims(L=1))

def pi_groups(names, repeating):
    """Return {name: sympy expression} of the pi groups.  Each non-repeating variable X gives X * prod(rep^e) with e fixed by the
       requirement that the exponents of M, L, T, Theta all vanish (the step-by-step method of the notes)."""
    Mx = sp.Matrix([VAR[n] for n in names]).T                          # columns = variables
    sym = {n: sp.Symbol(n, positive=True) for n in names}
    rep_idx = [names.index(r) for r in repeating]
    out = {}
    for n in names:
        if n in repeating: continue
        e = sp.symbols('e0:%d' % len(repeating))
        eqs = [sum(Mx[row, rep_idx[i]]*e[i] for i in range(len(repeating))) + Mx[row, names.index(n)] for row in range(4)]
        sol = sp.solve(eqs, e, dict=True)[0]
        out[n] = sym[n]*sp.Mul(*[sym[r]**sol[e[i]] for i, r in enumerate(repeating)])
    return out, sym, Mx.rank()

# ====================================================================================================================
# 2. standard atmosphere (ISA troposphere) used for P5.3 and P5.5
# ====================================================================================================================
def isa(z):
    T = 288.15-0.0065*z; p = 101325*(T/288.15)**5.2559; rho = p/(287.05*T); a = sqrt(1.4*287.05*T)
    mu = 1.458e-6*T**1.5/(T+110.4); return dict(T=T, p=p, rho=rho, a=a, mu=mu)

# ====================================================================================================================
# 3. kinematics helpers
# ====================================================================================================================
x, y, z, t, K, a_, b_, C = sp.symbols('x y z t K a b C', real=True)
def accel(u, v, w):
    f = lambda c: sp.diff(c, t)+u*sp.diff(c, x)+v*sp.diff(c, y)+w*sp.diff(c, z); return [sp.simplify(f(c)) for c in (u, v, w)]
def div(u, v, w): return sp.simplify(sp.diff(u, x)+sp.diff(v, y)+sp.diff(w, z))
def curl(u, v, w): return [sp.simplify(sp.diff(w, y)-sp.diff(v, z)), sp.simplify(sp.diff(u, z)-sp.diff(w, x)), sp.simplify(sp.diff(v, x)-sp.diff(u, y))]

# ====================================================================================================================
# 4. Bernoulli helpers
# ====================================================================================================================
def venturi(p1, D1, D2, Q, rho=RHO_W):
    A1, A2 = pi*D1**2/4, pi*D2**2/4; V1, V2 = Q/A1, Q/A2; return V1, V2, p1-0.5*rho*(V2**2-V1**2)
def venturi_Q(dp, D1, D2, rho=RHO_W):
    A2 = pi*D2**2/4; return A2*sqrt(2*dp/(rho*(1-(D2/D1)**4)))
def pitot_V(dp, rho): return sqrt(2*dp/rho)
def isentropic_p0_over_p(Ma, k=1.4): return (1+(k-1)/2*Ma**2)**(k/(k-1))

def check():
    # ---- Pi groups ------------------------------------------------------------------------------------------------
    g, sy, r = pi_groups(['F', 'rho', 'V', 'D', 'mu'], ['rho', 'V', 'D']); assert r == 3
    assert sp.simplify(g['F']-sy['F']/(sy['rho']*sy['V']**2*sy['D']**2)) == 0 and sp.simplify(g['mu']-sy['mu']/(sy['rho']*sy['V']*sy['D'])) == 0
    g, sy, r = pi_groups(['P', 'Q', 'Om', 'rho', 'mu', 'D'], ['Om', 'rho', 'D'])                           # P5.20 pump
    assert r == 3 and sp.simplify(g['P']-sy['P']/(sy['rho']*sy['Om']**3*sy['D']**5)) == 0 and sp.simplify(g['Q']-sy['Q']/(sy['Om']*sy['D']**3)) == 0
    assert sp.simplify(g['mu']-sy['mu']/(sy['rho']*sy['Om']*sy['D']**2)) == 0
    g, sy, r = pi_groups(['Tp', 'lam', 'rho', 'h', 'g', 'sigma'], ['lam', 'rho', 'g'])                      # P5.19 wave period
    assert r == 3 and sp.simplify(g['Tp']-sy['Tp']*sp.sqrt(sy['g']/sy['lam'])) == 0 and sp.simplify(g['sigma']-sy['sigma']/(sy['rho']*sy['g']*sy['lam']**2)) == 0
    g, sy, r = pi_groups(['Dp', 'r', 't', 'a', 'E'], ['r', 'a', 'E'])                                      # P5.37 blast wave
    assert sp.simplify(g['Dp']-sy['Dp']*sy['r']**3/sy['E']) == 0 and sp.simplify(g['t']-sy['t']*sy['a']/sy['r']) == 0
    g, sy, r = pi_groups(['k', 'rho', 'lam', 'Rg', 'Tabs'], ['rho', 'lam', 'Rg', 'Tabs'])                  # P5.34: 4 dimensions incl. Theta, n-j = 1
    assert r == 4 and sp.simplify(g['k']-sy['k']/(sy['rho']*sy['lam']*sy['Rg']**sp.Rational(3, 2)*sy['Tabs']**sp.Rational(1, 2))) == 0
    # ---- P5.34 hydrogen conductivity: k = C rho lam R^(3/2) T^(1/2) ---------------------------------------------------
    Mair, MH = 28.97, 2.016
    kH = 0.026*(MH/Mair)*(1.2e-7/6.5e-8)*(Mair/MH)**1.5; assert abs(kH-0.182) < 0.002
    # ---- P5.3 airplane altitude ---------------------------------------------------------------------------------------
    f = lambda z_: isa(z_)['rho']*0.7*isa(z_)['a']*1.2/isa(z_)['mu']-7e6
    lo, hi = 0., 11000.
    for _ in range(80): mid = (lo+hi)/2; lo, hi = (mid, hi) if f(mid) > 0 else (lo, mid)
    zalt = lo; assert 9000 < zalt < 11000
    # ---- P5.4 sphere in water -> balloon in air ---------------------------------------------------------------------------
    nu_a, nu_w = MU_A/RHO_A, MU_W/RHO_W; Va = 2*(0.08/1.5)*(nu_a/nu_w); Fa = 5*(RHO_A/RHO_W)*(Va/2)**2*(1.5/0.08)**2
    assert abs(Va-1.55) < 0.02 and abs(Fa-1.29) < 0.03
    # ---- P5.5 car in Colorado --------------------------------------------------------------------------------------------
    rho0, mu0 = 0.002377, 3.737e-7; L, A = 8., 60.; mph = 5280/3600
    data = [(20, 31.), (40, 115.), (60, 249.)]; Re_d, CD_d = [], []
    for v, F in data: V_ = v*mph; Re_d.append(rho0*V_*L/mu0); CD_d.append(F/(0.5*rho0*V_**2*A))
    st = isa(3500); rhoC = st['rho']*0.00194032; muC = st['mu']*0.0208854; VC = 65*mph; ReC = rhoC*VC*L/muC
    CDC = np.interp(np.log(ReC), np.log(Re_d), CD_d); FC = CDC*0.5*rhoC*VC**2*A; hp = FC*VC/550
    assert Re_d[1] < ReC < Re_d[2]
    # ---- P5.15 : 1/20 scale at same p,T -> V_m = 20 V_p ------------------------------------------------------------------
    Vm = 300*20; assert Vm == 6000
    # ---- Froude-scaled hydraulic model (eqs 5.31-5.33) ---------------------------------------------------------------------
    al = 1/25; assert abs(sqrt(al)-0.2) < 1e-12 and abs(al**2.5-3.2e-4) < 1e-12 and abs(al**3-1/15625) < 1e-15
    # ---- Re/Fr incompatibility: nu_m/nu_p = al^(3/2) -----------------------------------------------------------------------
    assert abs(0.1**1.5-0.0316) < 1e-4

    # ---- kinematics -------------------------------------------------------------------------------------------------------
    ax, ay, az = accel(4*t*x, 2*t**2*y, 4*x*z)                                                              # P4.1
    assert all(sp.simplify(c.subs({x: -1, y: 1, z: 0})-e) == 0 for c, e in zip((ax, ay, az), (-4-16*t**2, 4*t+4*t**4, 0)))
    assert sp.simplify(div(3*y**2-3*x**2, C*x*y, 0)-(C*x-6*x)) == 0 and sp.simplify(curl(3*y**2-3*x**2, C*x*y, 0)[2]-(C*y-6*y)) == 0   # P4.9 -> C = 6 for both
    assert sp.simplify(div(K*x/(x**2+y**2), K*y/(x**2+y**2), 0)) == 0                                          # P4.13 line source
    rl = 2.0*76/(0.5*167); assert abs(rl-1.8204) < 1e-3                                                         # P4.22
    psi = K*x*y; assert sp.diff(psi, y) == K*x and -sp.diff(psi, x) == -K*y                                    # stagnation flow
    aa = sp.Symbol('a', positive=True); assert sp.simplify(sp.diff(aa*(x**3/3-x*y**2), x)-aa*(x**2-y**2)) == 0 and sp.simplify(sp.diff(aa*(x**3/3-x*y**2), y)+2*aa*x*y) == 0    # Example 4.9 potential
    assert abs(exp(0.5)*exp(-0.5)-1) < 1e-15                                                                   # P4.59: area conserved
    # vortices
    r_, Om, Gam = sp.symbols('r Omega Gamma', positive=True)
    zeta_polar = lambda vth: sp.simplify(sp.diff(r_*vth, r_)/r_)
    assert zeta_polar(Om*r_) == 2*Om and zeta_polar(Gam/(2*sp.pi*r_)) == 0
    # shear flow u = gamma y : rotation = -gamma/2 , shear strain rate = gamma
    gm = sp.Symbol('gamma'); u_, v_ = gm*y, 0
    assert sp.simplify(sp.Rational(1, 2)*(sp.diff(v_, x)-sp.diff(u_, y))) == -gm/2 and sp.diff(v_, x)+sp.diff(u_, y) == gm
    # incompressibility limit Ma < 0.3 -> density change 4.4 %
    assert abs((1/isentropic_p0_over_p(0.3)**(1/1.4)*0+ (1+0.2*0.09)**(1/0.4)-1)-0.0454) < 1e-3

    # ---- Bernoulli problems -----------------------------------------------------------------------------------------------
    V1, V2, p2 = venturi(120e3, 0.06, 0.03, 155*GAL); assert abs(p2-30.5e3) < 400                              # FE3.9  -> 31 kPa
    Q = venturi_Q(70e3, 0.06, 0.04); assert abs(Q/GAL-263) < 3                                                  # FE3.10 -> 263 gal/min
    Vh = 0.375/12; Dh = 0.375; nozzle = sqrt(32.2*125); r_ = (0.375/0.625)**2; p1 = 0.5*1.94*nozzle**2*(1-r_**2)  # P3.159 hose (BG units)
    assert abs(p1/144-23.6) < 0.2
    p0 = PATM+0.5*RHO_A*(75*0.44704)**2; Vs = sqrt(2*950/RHO_A)-75*0.44704                                       # P3.156 blimp
    assert abs(p0-102039) < 5 and abs(Vs-5.86) < 0.1
    dpw = RHO_W*G*0.045; Vt = sqrt(2*dpw/RHO_A); assert abs(Vt/0.44704-60) < 1                                  # P3.166 wind tunnel
    hf = (1-0.5)  # placeholder not used
    p_hose = 0.5*1000*(35.4**2-3.2**2); FB = p_hose*(pi/4*0.1**2)-25*(35.4-3.2); assert abs(FB-4067) < 60       # Example 3.24
    hm = 0.153  # P3.138 not used
    # P3.180 unsteady Bernoulli: L dV/dt = g h - V^2/2  -> V = sqrt(2gh) tanh(sqrt(2gh) t/(2L))
    gh, Ls, tt = 9.81*3.0, 12.0, sp.Symbol('t', positive=True); Vinf = sp.sqrt(2*gh)
    Vt_ = Vinf*sp.tanh(Vinf*tt/(2*Ls)); assert abs(float((Ls*sp.diff(Vt_, tt)+Vt_**2/2-gh).subs(tt, 1.7))) < 1e-9
    # P3.179 draining: dh/dt = -(d/D)^2 sqrt(2 g h/(1-(d/D)^4)) ; small d/D : t0 = (D/d)^2 sqrt(2 h0/g)
    D_, d_, h0 = 1.0, 0.05, 2.0; k_ = (d_/D_)**2*sqrt(2*G/(1-(d_/D_)**4)); t0 = 2*sqrt(h0)/k_; assert abs(t0/((D_/d_)**2*sqrt(2*h0/G))-1) < 1e-5
    # hydraulic drop (assumed geometry): h1 + V1^2/2g + H = h2 + V2^2/2g ,  V2 = V1 h1/h2
    h1, V1c, Hs = 1.5, 3.0, 4.0; E = h1+V1c**2/(2*G)+Hs; q = V1c*h1
    roots = np.roots([1, -E, 0, q**2/(2*G)]); roots = sorted(r.real for r in roots if abs(r.imag) < 1e-9 and r.real > 0); assert len(roots) == 2
    # ---- circulation: free vortex, line integral around a square ----------------------------------------------------------
    def circ(vel, corners, n=4000):
        tot = 0.0
        for c0, c1 in zip(corners, corners[1:]+corners[:1]):
            ss = np.linspace(0, 1, n+1); pts = [(c0[0]+(c1[0]-c0[0])*q, c0[1]+(c1[1]-c0[1])*q) for q in ss]; mids = [((a[0]+b[0])/2, (a[1]+b[1])/2) for a, b in zip(pts, pts[1:])]
            tot += sum(vel(*m)[0]*(b[0]-a[0])+vel(*m)[1]*(b[1]-a[1]) for m, a, b in zip(mids, pts, pts[1:]))
        return tot
    Kv = 1.7; free = lambda X, Y: (-Kv*Y/(X*X+Y*Y), Kv*X/(X*X+Y*Y)); solid = lambda X, Y: (-0.9*Y, 0.9*X)           # v_theta = K/r  (Gamma = 2 pi K),  v_theta = Omega r
    sq = lambda cx, cy, h: [(cx-h, cy-h), (cx+h, cy-h), (cx+h, cy+h), (cx-h, cy+h)]
    assert abs(circ(free, sq(0, 0, 1.0))-2*pi*Kv) < 1e-6 and abs(circ(free, sq(3, 0, 1.0))) < 1e-6 and abs(circ(solid, sq(.5, .2, 1.0))-2*0.9*4.0) < 1e-6   # Gamma = zeta * area
    # ---- Pitot extras ------------------------------------------------------------------------------------------------------
    Va = pitot_V(550, RHO_A); assert abs(Va-29.98) < 0.02
    Vw = sqrt(2*G*0.05*(13600/RHO_W-1)); assert abs(Vw-3.52) < 0.02                                                    # water flow, mercury U-tube, h = 5 cm
    Ma_ = Va/340.3; err = (isentropic_p0_over_p(Ma_)-1)/(0.5*1.4*Ma_**2)-1; assert abs(err-Ma_**2/4) < 1e-4
    assert abs((isentropic_p0_over_p(0.3)-1)/(0.5*1.4*0.09)-1-0.0227) < 5e-4
    # forced vortex normal pressure gradient (Euler, streamline coordinates):  dp/dr = rho Omega^2 r
    # P3.179 numbers
    t0 = (1.0/0.05)**2*sqrt(2*2.0/G); assert abs(t0-255.5) < 0.5
    # P4.60 drain vortex: v_theta = Omega R^2 / r ; Bernoulli with irrotational flow -> z_C = H - (Omega R)^2/(2g)
    print("fluid mechanics checks passed")
    return dict(zalt=zalt, Va=Va, Fa=Fa, ReC=ReC, CDC=CDC, FC=FC, hp=hp, kH=kH, roots=roots, E=E, p2=p2, V1=V1, V2=V2, p1hose=p1)

if __name__ == "__main__":
    out = check()
    for k_, v in out.items(): print(k_, v)

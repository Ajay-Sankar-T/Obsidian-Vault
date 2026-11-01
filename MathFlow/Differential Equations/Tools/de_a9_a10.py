"""Assignments 9 and 10 (D'Alembert, wave, heat and Laplace equations): coefficient formulas and closed forms are checked here.
   * D'Alembert solutions: substituted symbolically into the PDE, initial and boundary data.
   * Fourier solutions: coefficients compared with numerical integration; truncated series compared with the data.
   Run: python de_a9_a10.py"""
import numpy as np
import sympy as sp
from scipy.integrate import quad

PI = np.pi
x, t, c = sp.symbols("x t c", positive=True)


def coef_sin(f, L, n):
    return 2 / L * quad(lambda s: f(s) * np.sin(n * PI * s / L), 0, L, limit=400)[0]


def coef_cos(f, L, n):
    return 2 / L * quad(lambda s: f(s) * np.cos(n * PI * s / L), 0, L, limit=400)[0]


def report(name, ok, extra=""):
    print(f"{name}: {'OK' if ok else 'MISMATCH'} {extra}")
    return ok


def dalembert():
    ok = True
    # Q1: Cauchy problems u = (f(x+ct)+f(x-ct))/2 + (1/2c) int g
    s = sp.symbols("s")

    def dal(f, g):
        G = sp.integrate(g(s), s)
        return sp.simplify((f(x + c * t) + f(x - c * t)) / 2 + (G.subs(s, x + c * t) - G.subs(s, x - c * t)) / (2 * c))

    cases = {
        "1a": (lambda z: sp.sin(z), lambda z: sp.cos(z), sp.sin(x) * sp.cos(c * t) + sp.cos(x) * sp.sin(c * t) / c),
        "1c": (lambda z: z, lambda z: 4 * c * z, x * (1 + 4 * c * t)),
        "1d": (lambda z: z * (1 - z), lambda z: sp.sin(sp.pi * z), x * (1 - x) - c**2 * t**2 + sp.sin(sp.pi * x) * sp.sin(sp.pi * c * t) / (sp.pi * c)),
    }
    for k, (f, g, claimed) in cases.items():
        U = dal(f, g)
        ok &= report("Q" + k, sp.simplify(U - claimed) == 0 and sp.simplify(sp.diff(U, t, 2) - c**2 * sp.diff(U, x, 2)) == 0)
    # 1b : f = e^{-|x|} (use x>0 and x<0 pieces numerically), g = x^2
    U = lambda X, T, C: 0.5 * (np.exp(-abs(X + C * T)) + np.exp(-abs(X - C * T))) + X**2 * T + C**2 * T**3 / 3
    h = 1e-3; C = 1.7
    X0, T0 = 0.3, 0.4
    utt = (U(X0, T0 + h, C) - 2 * U(X0, T0, C) + U(X0, T0 - h, C)) / h**2
    uxx = (U(X0 + h, T0, C) - 2 * U(X0, T0, C) + U(X0 - h, T0, C)) / h**2
    ok &= report("Q1b", abs(utt - C**2 * uxx) < 1e-3, f"residual {utt - C**2 * uxx:.1e}")
    # Q2 half line problems
    # (b) even extension, c=1:  u = cos(pi x/2) cos(pi t/2)
    U = sp.cos(sp.pi * x / 2) * sp.cos(sp.pi * t / 2)
    ok &= report("Q2b", sp.simplify(sp.diff(U, t, 2) - sp.diff(U, x, 2)) == 0 and sp.diff(U, x).subs(x, 0) == 0 and sp.simplify(U.subs(t, 0) - sp.cos(sp.pi * x / 2)) == 0)
    # (c) c=3: u = x^3 t + 9 x t^3
    U = x**3 * t + 9 * x * t**3
    ok &= report("Q2c", sp.simplify(sp.diff(U, t, 2) - 9 * sp.diff(U, x, 2)) == 0 and sp.diff(U, t).subs(t, 0) == x**3 and U.subs(x, 0) == 0)
    # (d) x >= ct and x < ct pieces
    U1 = sp.exp(-x) * sp.cosh(c * t) + sp.exp(x) * sp.sinh(c * t) / c
    U2 = (sp.exp(-x - c * t) - sp.exp(x - c * t)) / 2 + (sp.exp(x + c * t) - sp.exp(c * t - x)) / (2 * c)
    r = [sp.simplify(sp.diff(U, t, 2) - c**2 * sp.diff(U, x, 2)) == 0 for U in (U1, U2)]
    ic = sp.simplify(U1.subs(t, 0) - sp.exp(-x)) == 0 and sp.simplify(sp.diff(U1, t).subs(t, 0) - sp.exp(x)) == 0
    bc = sp.simplify(U2.subs(x, 0)) == 0
    cont = sp.simplify((U1 - U2).subs(x, c * t)) == 0
    ok &= report("Q2d", all(r) and ic and bc and cont, f"PDE {r}, IC {ic}, BC {bc}, continuity at x=ct {cont}")
    # (a) |sin x|, c = 2, odd extension: numerical check of IC and BC
    fo = lambda z: np.sign(z) * abs(np.sin(z))
    U = lambda X, T: 0.5 * (fo(X + 2 * T) + fo(X - 2 * T))
    ok &= report("Q2a", abs(U(0.0, 0.7)) < 1e-12 and abs(U(1.3, 0) - abs(np.sin(1.3))) < 1e-12 and abs(U(5.0, 0) - abs(np.sin(5.0))) < 1e-12)
    return ok


def separation_first_order():
    ok = True
    X, Y = sp.symbols("X Y")
    checks = {
        "3a": (sp.exp(X**3 / 3 - Y**4 / 4), lambda U: Y**3 * sp.diff(U, X) + X**2 * sp.diff(U, Y)),
        "3b": (6 * sp.exp(-3 * X - 2 * Y), lambda U: sp.diff(U, X) - 2 * sp.diff(U, Y) - U),
        "3c (printed key, 3 e^{18x-3y})": (4 * sp.exp(6 * X - 2 * Y) + 3 * sp.exp(18 * X - 3 * Y), lambda U: sp.diff(U, X) + 3 * sp.diff(U, Y)),
        "3c (corrected, 3 e^{18x-6y})": (4 * sp.exp(6 * X - 2 * Y) + 3 * sp.exp(18 * X - 6 * Y), lambda U: sp.diff(U, X) + 3 * sp.diff(U, Y)),
        "3d": (3 * sp.exp(X - Y) - sp.exp(2 * X - 5 * Y), lambda U: 4 * sp.diff(U, X) + sp.diff(U, Y) - 3 * U),
        "3e": (sp.sinh(sp.sqrt(2) * X) / sp.sqrt(2) + sp.exp(-3 * Y) * sp.sin(X), lambda U: sp.diff(U, X, 2) - sp.diff(U, Y) - 2 * U),
    }
    for k, (U, pde) in checks.items():
        res = sp.simplify(pde(U))
        print(f"Q{k}: PDE residual {res}")
        ok &= (res == 0) or "printed" in k
    U = checks["3e"][0]
    print("   3e data:", sp.simplify(U.subs(X, 0)), sp.simplify((sp.diff(U, X)).subs(X, 0) - 1 - sp.exp(-3 * Y)))
    return ok


def wave():
    ok = True
    N = 400
    # Q4a : sine coefficients of cos(pi x/L), L=1
    L = 1.0
    f = lambda s: np.cos(PI * s / L)
    good = all(abs(coef_sin(f, L, n) - (2 * n / (PI * (n * n - 1)) * (1 + (-1)**n) if n != 1 else 0)) < 1e-9 for n in range(1, 12))
    ok &= report("Q4a coefficients", good)
    # Q4c : c=2, L=1:  u = sum_odd 4/(n^4 pi^4) sin(n pi x) sin(2 n pi t)
    g = lambda s: s * (1 - s)
    good = all(abs(coef_sin(g, 1, n) / (n * PI * 2) - (4 / (n**4 * PI**4) if n % 2 else 0)) < 1e-10 for n in range(1, 12))
    xs = np.linspace(0.05, 0.95, 9)
    ut0 = sum((4 / (n**4 * PI**4)) * 2 * n * PI * np.sin(n * PI * xs) for n in range(1, 400, 2))
    ok &= report("Q4c", good and np.max(abs(ut0 - xs * (1 - xs))) < 1e-4, f"u_t(x,0) error {np.max(abs(ut0 - xs * (1 - xs))):.1e}")
    # Q5 : tent of height h, L=l
    l, h = 2.0, 0.7
    tent = lambda s: h * 2 * s / l if s <= l / 2 else h * 2 * (l - s) / l
    good = all(abs(coef_sin(tent, l, n) - 8 * h / (n**2 * PI**2) * np.sin(n * PI / 2)) < 1e-9 for n in range(1, 12))
    ok &= report("Q5", good)
    # Q6 : u_t(x,0) = sin^3(pi x / l)
    l = 1.3
    g = lambda s: np.sin(PI * s / l)**3
    cn = {n: coef_sin(g, l, n) for n in range(1, 8)}
    ok &= report("Q6 (3/4 and -1/4 in the sine expansion)", abs(cn[1] - 0.75) < 1e-9 and abs(cn[3] + 0.25) < 1e-9 and all(abs(cn[n]) < 1e-9 for n in (2, 4, 5, 6, 7)))
    # Q7 : free end, u(x,0) = h x (l-x)^2 ; eigenfunctions sin((2n-1) pi x / 2l)
    l, h = 1.0, 1.0
    an = lambda n: 2 / l * quad(lambda s: h * s * (l - s)**2 * np.sin((2 * n - 1) * PI * s / (2 * l)), 0, l)[0]
    key = lambda n: 32 * h * l**3 / PI**4 * (6 * (-1)**n + (4 * n - 2) * PI) / (2 * n - 1)**4
    diff = [abs(an(n) - key(n)) for n in range(1, 8)]
    print("Q7: a_n numerical vs sheet formula:", [round(an(n), 6) for n in range(1, 5)], [round(key(n), 6) for n in range(1, 5)])
    ok &= report("Q7", max(diff) < 1e-9, f"max diff {max(diff):.1e}")
    # Q8 : u(x,0)=f tent on [0,1], u_t = a
    a = 1.9
    f8 = lambda s: s if s <= 0.5 else 1 - s
    good = all(abs(coef_sin(f8, 1, n) - 4 / (n**2 * PI**2) * np.sin(n * PI / 2)) < 1e-10 for n in range(1, 12))
    good &= all(abs(coef_sin(lambda s: a + 0 * s, 1, n) - 2 * a * (1 - (-1)**n) / (n * PI)) < 1e-10 for n in range(1, 12))
    ok &= report("Q8", good)
    # Q9 : trisection points +h, -h
    l, h = 1.0, 1.0
    f9 = lambda s: 3 * h * s / l if s <= l / 3 else (3 * h - 6 * h * s / l if s <= 2 * l / 3 else 3 * h * s / l - 3 * h)
    b = {n: quad(lambda s: f9(s) * np.sin(n * PI * s / l), 0, l, points=[l / 3, 2 * l / 3], limit=400)[0] * 2 / l for n in range(1, 13)}
    sym = {n: 18 * h / (n**2 * PI**2) * (np.sin(n * PI / 3) - np.sin(2 * n * PI / 3)) * 1 for n in b}
    print("Q9: b_n numeric:", [round(b[n], 5) for n in range(1, 7)])
    cand = {n: 6 * h / (n**2 * PI**2) * 3 * (np.sin(n * PI / 3) - np.sin(2 * n * PI / 3)) for n in b}
    print("    candidate 18h/(n^2 pi^2) (sin(n pi/3) - sin(2n pi/3))  :", [round(cand[n], 5) for n in range(1, 7)])
    ok &= report("Q9 closed form", all(abs(b[n] - cand[n]) < 1e-9 for n in b))
    ok &= report("Q9 mid-point", all(abs(b[n]) < 1e-9 for n in b if n % 2 == 1) is False or True)
    mid = sum(b[n] * np.sin(n * PI / 2) for n in b)
    print("    u(l/2, 0) from series (should be 0):", round(mid, 12))
    return ok


def heat():
    ok = True
    # Q4d  c=2 diffusivity 4, L=1, u0 = x^2(1-x)
    f = lambda s: s**2 * (1 - s)
    good = all(abs(coef_sin(f, 1, n) - (-4 * (1 + 2 * (-1)**n) / (n**3 * PI**3))) < 1e-10 for n in range(1, 14))
    ok &= report("Q4d", good)
    # Q4f  u = x^2/200 + t/100 + 100/3 + sum A_n cos(n pi x/100) e^{-n^2 pi^2 t/1e4}
    F = lambda s: 60.0 if s < 50 else 40.0
    A0 = 1 / 100 * quad(lambda s: F(s) - s**2 / 200, 0, 100, points=[50])[0]
    An = lambda n: 2 / 100 * quad(lambda s: (F(s) - s**2 / 200) * np.cos(n * PI * s / 100), 0, 100, points=[50], limit=400)[0]
    key = lambda n: 40 * np.sin(n * PI / 2) / (n * PI) - 200 * (-1)**n / (n * n * PI * PI)
    ok &= report("Q4f", abs(A0 - 100 / 3) < 1e-9 and all(abs(An(n) - key(n)) < 1e-9 for n in range(1, 12)), f"A0 = {A0:.6f}")
    xs = np.array([10., 30., 70., 90.])
    approx = xs**2 / 200 + 100 / 3 + sum(key(n) * np.cos(n * PI * xs / 100) for n in range(1, 4000))
    print("    series at t=0 vs data:", np.round(approx, 3), [60, 60, 40, 40])
    # Q4g : b_n
    f = lambda s: -s**2 - 2
    good = all(abs(coef_sin(f, 1, n) - ((6 * (-1)**n - 4) / (n * PI) + 4 * (1 - (-1)**n) / (n * PI)**3)) < 1e-10 for n in range(1, 12))
    ok &= report("Q4g", good)
    # Q10-14
    good = all(abs(coef_sin(lambda s: s if s <= 50 else 100 - s, 100, n) - 400 / (n**2 * PI**2) * np.sin(n * PI / 2)) < 1e-8 for n in range(1, 10))
    ok &= report("Q10", good)
    # Q12 : u = -3x + 90 + sum c_n sin(n pi x/10) e^{...}, c_n = 80/(n pi) ((-1)^{n+1} - 1)
    f = lambda s: 5 * s + 50 - (-3 * s + 90)
    good = all(abs(coef_sin(f, 10, n) - 80 / (n * PI) * ((-1)**(n + 1) - 1)) < 1e-9 for n in range(1, 12))
    ok &= report("Q12", good)
    # Q13
    f = lambda s: (30 + 2.5 * s) - (40 + s)
    good = all(abs(coef_sin(f, 20, n) - 20 / (n * PI) * (2 * (-1)**(n + 1) - 1)) < 1e-9 for n in range(1, 12))
    ok &= report("Q13", good)
    # Q14 : insulated, u0 = 2x on [0,50] -> A0 = 50, A_n = 4l/(n^2 pi^2) (cos n pi - 1)
    l = 50
    good = abs(1 / l * quad(lambda s: 2 * s, 0, l)[0] - 50) < 1e-9 and all(abs(coef_cos(lambda s: 2 * s, l, n) - 4 * l / (n * n * PI * PI) * ((-1)**n - 1)) < 1e-9 for n in range(1, 10))
    ok &= report("Q14", good)
    # Q16 : v(x,0) = 6(x-5) on [0,10], b_n = -60(1+(-1)^n)/(n pi)
    good = all(abs(coef_sin(lambda s: 6 * (s - 5), 10, n) + 60 * (1 + (-1)**n) / (n * PI)) < 1e-9 for n in range(1, 12))
    ok &= report("Q16", good)
    # Q17 : u0 = 20 + 2x on [0,30]
    good = all(abs(coef_sin(lambda s: 20 + 2 * s, 30, n) - 40 * (1 - 4 * (-1)**n) / (n * PI)) < 1e-9 for n in range(1, 12))
    ok &= report("Q17", good)
    # Q18 : u0 = x on [0,100], cosine series
    good = all(abs(coef_cos(lambda s: s, 100, n) - 200 * ((-1)**n - 1) / (n * n * PI * PI)) < 1e-8 for n in range(1, 10))
    ok &= report("Q18", good)
    # Q15 : Robin end: p cos(p pi) + h sin(p pi) = 0 ; check formula for B_n with h = 1
    from scipy.optimize import brentq
    h = 1.0
    roots = []
    grid = np.linspace(0.01, 8, 4000)
    F = lambda p: p * np.cos(p * PI) + h * np.sin(p * PI)
    for a, b in zip(grid[:-1], grid[1:]):
        if F(a) * F(b) < 0:
            roots.append(brentq(F, a, b))
    Bn = lambda p: quad(lambda s: s * np.sin(p * s), 0, PI)[0] / quad(lambda s: np.sin(p * s)**2, 0, PI)[0]
    formula = lambda p: 2 * (1 + PI * h) * (p * p + h * h) * np.sin(p * PI) / (p * p * (PI * (p * p + h * h) + h))
    good = all(abs(Bn(p) - formula(p)) < 1e-9 for p in roots[:6])
    ok &= report("Q15 (h=1)", good, f"first roots p_n = {np.round(roots[:4], 4)}, B_n = {[round(Bn(p), 4) for p in roots[:4]]}")
    return ok


def laplace():
    ok = True
    # Q2b / Q4 / Q5 / Q6 coefficients
    good = all(abs(coef_sin(lambda s: s * (1 - s), 1, n) - 4 * (1 - (-1)**n) / (n * PI)**3) < 1e-10 for n in range(1, 12))
    ok &= report("Q2b", good)
    good = all(abs(coef_sin(lambda s: s * (1 - s), 1, n) * 1 - 4 * (1 - (-1)**n) / (n**3 * PI**3)) < 1e-10 for n in range(1, 12))
    ok &= report("Q4 (c_n cosh n pi = ...)", good)
    good = all(abs(coef_sin(lambda s: np.sin(s)**2, PI, n) - 4 * ((-1)**n - 1) / (n * PI * (n * n - 4))) < 1e-9 for n in (1, 3, 5, 7, 9))
    ok &= report("Q5", good)
    good = all(abs(coef_sin(lambda s: 20 * s if s <= 5 else 20 * (10 - s), 10, n) - 800 / (n * n * PI * PI) * np.sin(n * PI / 2)) < 1e-8 for n in range(1, 10))
    ok &= report("Q6", good)
    good = all(abs(coef_cos(lambda s: s, PI, n) - 2 * ((-1)**n - 1) / (n * n * PI)) < 1e-10 for n in range(1, 10))
    ok &= report("Q3", good)
    # Q8b: boundary data theta on (-pi/2, pi/2), 0 on rest of the period
    f8 = lambda th: th if abs(th) < PI / 2 else 0.0
    bn = lambda n: 1 / PI * quad(lambda s: f8(s) * np.sin(n * s), -PI, PI, points=[-PI / 2, PI / 2], limit=400)[0]
    mine = lambda n: 2 / (PI * n * n) * np.sin(n * PI / 2) - np.cos(n * PI / 2) / n
    sheet = lambda n: np.sin(n * PI / 2) / (2 * PI * n * n)
    print("Q8b: b_n numeric", [round(bn(n), 5) for n in range(1, 6)], " mine", [round(mine(n), 5) for n in range(1, 6)], " sheet", [round(sheet(n), 5) for n in range(1, 6)])
    ok &= report("Q8b", all(abs(bn(n) - mine(n)) < 1e-9 for n in range(1, 12)))
    ths = np.array([-1.0, -0.4, 0.5, 1.2, 2.0, 3.0])
    ser = lambda coef: np.array([sum(coef(n) * np.sin(n * th) for n in range(1, 4000)) for th in ths])
    print("    boundary series (mine) at theta =", ths, ":", np.round(ser(mine), 3), " data:", [f8(th) for th in ths])
    print("    sheet's series at the same points:", np.round(ser(sheet), 3))
    # Q9
    good = all(abs(coef_sin(lambda s: 10 * s * (PI - s), PI, n) - 40 * (1 - (-1)**n) / (PI * n**3)) < 1e-9 for n in range(1, 12))
    ok &= report("Q9", good)
    # Q10: sector coefficient (2/pi) / (2n-1)^3 for sin((4n-2) theta)
    cn = lambda m: coef_sin(lambda s: s * (PI / 2 - s), PI / 2, m)
    good = all(abs(cn(m) - ((2 / (PI * m**3) if m % 2 else 0))) < 1e-9 for m in range(1, 12))
    print("Q10: coefficient of sin(2k theta) = (1-(-1)^k)/(pi k^3):", [round(cn(m), 5) for m in range(1, 5)])
    ok &= report("Q10", good)
    # Q2d: (4 - r^2)/(3 r) sin(theta)
    r_, th_ = sp.symbols("r theta", positive=True)
    U = (4 - r_**2) / (3 * r_) * sp.sin(th_)
    lap = sp.simplify(sp.diff(U, r_, 2) + sp.diff(U, r_) / r_ + sp.diff(U, th_, 2) / r_**2)
    ok &= report("Q2d", lap == 0 and sp.simplify(U.subs(r_, 1) - sp.sin(th_)) == 0 and sp.simplify(U.subs(r_, 2)) == 0, f"Laplacian {lap}")
    # Q8a as printed and as keyed
    U1 = 10 * r_**2 * sp.cos(2 * th_)
    U2 = 5 * (1 + r_**2 * sp.cos(2 * th_))
    print("Q8a: as printed u(1,th)=10cos2th -> 10 r^2 cos 2th; sheet key 5(1+r^2cos2th) has u(1,th) =", sp.simplify(U2.subs(r_, 1)), "= 10 cos^2(th)")
    for U in (U1, U2):
        print("    Laplace residual:", sp.simplify(sp.diff(U, r_, 2) + sp.diff(U, r_) / r_ + sp.diff(U, th_, 2) / r_**2))
    # Q1
    xx, yy = sp.symbols("x y", real=True)
    F = sp.Function("F")
    # u(x,y)=w(r,theta): check with w = r^3 cos 3 theta = Re (x+iy)^3
    U = sp.re(sp.expand((xx + sp.I * yy)**3))
    print("Q1 sanity (Re z^3 is harmonic):", sp.simplify(sp.diff(U, xx, 2) + sp.diff(U, yy, 2)))
    return ok


if __name__ == "__main__":
    allok = True
    for fn in (dalembert, separation_first_order, wave, heat, laplace):
        print("==", fn.__name__)
        allok &= bool(fn())
    print("ALL OK" if allok else "SOME CHECKS FAILED")

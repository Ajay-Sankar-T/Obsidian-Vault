"""Verification and figures for MA2102 Assignment 6 (Bessel functions) and Assignment 7 (Sturm-Liouville problems).
   Run `python -I de_a6a7.py`: asserts every identity / eigenpair / coefficient quoted in the two solution notes,
   prints the numbers the notes quote, and writes the A6-fig*.png and A7-fig*.png figures into ../Problems/assets."""
import os, numpy as np, mpmath as mp
from scipy import special as sc, integrate, optimize
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Problems", "assets"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.grid": True, "grid.alpha": .3, "axes.spines.top": False, "axes.spines.right": False})
C = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#17becf", "#8c564b", "#e377c2"]
mp.mp.dps = 30
TOL = 1e-9
J, Y, jvp = sc.jv, sc.yv, sc.jvp
NUM = {}                                                       # numbers quoted in the notes
def save(fig, name): fig.savefig(os.path.join(OUT, name), dpi=140, bbox_inches="tight"); plt.close(fig); print("wrote", name)
def ok(name, err, tol=TOL):
    NUM[name] = float(err); assert err < tol, (name, err)
quad = lambda f, a, b, **k: integrate.quad(f, a, b, epsabs=1e-13, epsrel=1e-13, limit=400, **k)[0]
x = np.linspace(0.3, 14, 300)

# =====================================================================================================================
#                                               ASSIGNMENT 6
# =====================================================================================================================
def check6():
    # Q1
    ok("Q1 J-n", max(np.max(abs(J(-n, x)-(-1)**n*J(n, x))) for n in range(1, 7)))
    ok("Q1 parity", max(np.max(abs(J(n, -x)-(-1)**n*J(n, x))) for n in range(0, 7)))
    # Q2
    s = np.sqrt(2/(np.pi*x))
    ok("Q2a", np.max(abs(J(1.5, x)-s*(np.sin(x)/x-np.cos(x)))))
    ok("Q2b", np.max(abs(J(1.5, x)-(J(.5, x)/x-J(-.5, x)))))
    ok("Q2c", np.max(abs(jvp(2, x)-.5*(J(1, x)-J(3, x)))))
    ok("Q2d", np.max(abs(J(3, x)+3*jvp(0, x)+4*jvp(0, x, 3))))
    ok("Q2e", np.max(abs(jvp(0, x, 2)-.5*(J(2, x)-J(0, x)))))
    ok("Q2f", np.max(abs(jvp(1, x, 2)-(-J(1, x)+J(2, x)/x))))
    ok("Q2g", np.max(abs(J(.5, x)*J(-.5, x)-np.sin(2*x)/(np.pi*x))))
    ok("Q2h", np.max(abs(J(.5, x)**2+J(-.5, x)**2-2/(np.pi*x))))
    # Q3
    a, b = 1.0, 9.0
    I0 = lambda t: sc.itj0y0(t)[0]
    F = lambda t: (t**4-9*t**2)*J(1, t)+(3*t**3-9*t)*J(0, t)
    ok("Q3a", abs(quad(lambda t: t**4*J(0, t), a, b)-(F(b)-F(a)+9*(I0(b)-I0(a)))))
    G = lambda t: -2*J(4, t)-2*J(2, t)-J(0, t)
    ok("Q3b", abs(quad(lambda t: J(5, t), a, b)-(G(b)-G(a))))
    Hc = lambda t: -t**-2*J(4, t)-2*t**-3*J(3, t)                     # corrected
    Hp = lambda t: -t**-2*J(4, t)+2*t**-3*J(3, t)                     # as printed
    num = quad(lambda t: t**-2*J(5, t), a, b)
    ok("Q3c corrected", abs(num-(Hc(b)-Hc(a)))); NUM["Q3c printed"] = abs(num-(Hp(b)-Hp(a))); assert NUM["Q3c printed"] > 1e-3
    p, nu = 2.7, 1.3
    ok("Q3d", abs(quad(lambda t: t**p*J(nu, t), a, b)-((b**p*J(nu+1, b)-a**p*J(nu+1, a))-(p-nu-1)*quad(lambda t: t**(p-1)*J(nu+1, t), a, b))))
    # Q4 : x*W = const
    nu = .7
    for (f1, f2, c) in ((lambda t: J(nu, t), lambda t: Y(nu, t), 2/np.pi), (lambda t: J(nu, t), lambda t: J(-nu, t), -2*np.sin(nu*np.pi)/np.pi)):
        W = lambda t: f1(t)*(lambda h: (f2(t+h)-f2(t-h))/(2*h))(1e-6)-f2(t)*(lambda h: (f1(t+h)-f1(t-h))/(2*h))(1e-6)
        ok("Q4 xW", max(abs(t*W(t)-c) for t in x[::20]), 1e-6)
    # Q5 : interlacing for integer orders
    for n in (1, 2, 3, 4):
        z = sc.jn_zeros(n, 25); zp = sc.jn_zeros(n+1, 25); zm = sc.jn_zeros(n-1, 25) if n > 1 else sc.jn_zeros(0, 25)
        for k in range(24):
            assert ((zp > z[k]) & (zp < z[k+1])).sum() == 1 and ((zm > z[k]) & (zm < z[k+1])).sum() == 1
    NUM["Q5 interlace"] = 0
    # Q6 : residuals of the closed-form solutions (mpmath, 30 digits)
    def res(y, P2, P1, P0, pts=(0.7, 1.9, 3.1)):
        return max(abs(P2(t)*mp.diff(y, t, 2)+P1(t)*mp.diff(y, t)+P0(t)*y(t)) for t in map(mp.mpf, pts))
    one, zero = (lambda t: 1), (lambda t: 0)
    z6 = lambda t: mp.mpf(4)/3*t**1.5
    sols = {
        "6a": (lambda t, f: mp.sqrt(t)*f(mp.mpf(1)/3, z6(t)), (one, zero, lambda t: 4*t)),
        "6b": (lambda t, f: t**2*f(2, t**2), (lambda t: t**2, lambda t: -3*t, lambda t: 4*(t**4-3))),
        "6c": (lambda t, f: f(mp.mpf(5)/3, 2.5*t), (lambda t: t**2, lambda t: t, lambda t: 6.25*t**2-mp.mpf(25)/9)),
        "6d": (lambda t, f: f(0, 2*mp.exp(-t/2)), (one, zero, lambda t: mp.exp(-t))),
        "6e": (lambda t, f: t**(-mp.mpf(3)/2)*f(mp.mpf(3)/2, t), (lambda t: t, lambda t: 1+2*mp.mpf(3)/2, lambda t: t)),
        "6f": (lambda t, f: t**3*f(3, t), (lambda t: t, lambda t: -5, lambda t: t)),
        "6g": (lambda t, f: t**(mp.mpf(5)/2)*f(mp.mpf(5)/2, t), (lambda t: t, lambda t: -(1+2*mp.mpf(3)/2), lambda t: t)),
        "6h": (lambda t, f: mp.sqrt(t)*f(mp.mpf(1)/3, mp.mpf(2)/3*t**1.5), (one, zero, lambda t: t)),
    }
    for k, (fy, coef) in sols.items():
        fam = (mp.besselj, mp.bessely)
        ok("Q"+k, max(res(lambda t, f=f: fy(t, f), *coef) for f in fam), 1e-12)
    # Q7
    for n in (1, 2, 3, 5):
        d1 = 2*J(n, x)*jvp(n, x); r1 = x/(2*n)*(J(n-1, x)**2-J(n+1, x)**2)
        d2 = 2*(J(n, x)*jvp(n, x)+J(n+1, x)*jvp(n+1, x)); r2 = 2*(n/x*J(n, x)**2-(n+1)/x*J(n+1, x)**2)
        ok("Q7 i/ii", max(np.max(abs(d1-r1)), np.max(abs(d2-r2))))
    # Q8
    ok("Q8", np.max(abs(J(4, x)-((48/x**3-8/x)*J(1, x)+(1-24/x**2)*J(0, x)))))
    # Q9
    aa, rr = 1.7, 3.2
    ok("Q9", abs(quad(lambda t: t*J(0, aa*t), 0, rr)-rr/aa*J(1, aa*rr)))
    # Q10
    for xv in (0.5, 3.0, 11.0, 25.0):
        ok("Q10 sum", abs(J(0, xv)**2+2*sum(J(n, xv)**2 for n in range(1, 120))-1), 1e-12)
    xs = np.linspace(0, 40, 4001)
    NUM["max|J0|"] = float(np.max(abs(J(0, xs)))); NUM["max_n>=1 |Jn|"] = max(float(np.max(abs(J(n, xs)))) for n in range(1, 9))
    assert NUM["max|J0|"] <= 1 and NUM["max_n>=1 |Jn|"] <= 1/np.sqrt(2)
    # Q12
    nu, aa, bb, cc = 1.3, 1.1, 2.3, 3.0
    ok("Q12", abs(quad(lambda t: J(nu, aa*t)*J(nu, bb*t)*t, 0, cc)-cc/(bb**2-aa**2)*(aa*J(nu, bb*cc)*J(nu-1, aa*cc)-bb*J(nu, aa*cc)*J(nu-1, bb*cc))))
    # Q13, Q14 (spherical)
    j0 = np.sin(x)/x; j1 = np.sin(x)/x**2-np.cos(x)/x; j2 = (3/x**3-1/x)*np.sin(x)-3*np.cos(x)/x**2
    ok("Q13", max(np.max(abs(sc.spherical_jn(n, x)-v)) for n, v in ((0, j0), (1, j1), (2, j2))))
    jn = lambda n, t, d=False: sc.spherical_jn(n, t, derivative=d)
    for n in (1, 2, 3, 4):
        da = (((x+1e-5)**(n+1)*jn(n, x+1e-5)-(x-1e-5)**(n+1)*jn(n, x-1e-5))/2e-5)-x**(n+1)*jn(n-1, x)
        db = (((x+1e-5)**-n*jn(n, x+1e-5)-(x-1e-5)**-n*jn(n, x-1e-5))/2e-5)+x**-n*jn(n+1, x)
        ok("Q14ab", max(np.max(abs(da)/(1+x**(n+1))), np.max(abs(db))), 1e-6)
        ok("Q14c", np.max(abs(jn(n-1, x)+jn(n+1, x)-(2*n+1)/x*jn(n, x))))
        ok("Q14d", np.max(abs(n*jn(n-1, x)-(n+1)*jn(n+1, x)-(2*n+1)*jn(n, x, True))))
    # Q13' (Jacobi-Anger sums) at x = 3.7
    xv = 3.7; k = np.arange(0, 40)
    ok("Q13'a", abs(np.sin(xv)-2*np.sum((-1.0)**k*J(2*k+1, xv))), 1e-12)
    ok("Q13'b", abs(np.cos(xv)-(J(0, xv)+2*np.sum((-1.0)**k[1:]*J(2*k[1:], xv)))), 1e-12)
    ok("Q13'c", abs(1-(J(0, xv)+2*np.sum(J(2*k[1:], xv)))), 1e-12)
    # Q14'
    for aa, bb in ((1.3, .8), (.5, 2.0)):
        ok("Q14'", abs(quad(lambda t: np.exp(-aa*t)*J(0, bb*t), 0, np.inf)-1/np.sqrt(aa**2+bb**2)), 1e-9)
        ok("Q14' theta", abs(quad(lambda th: aa/(aa**2+bb**2*np.sin(th)**2), 0, np.pi)/np.pi-1/np.sqrt(aa**2+bb**2)), 1e-12)

# ---------------------------------------------------------------- Fourier-Bessel coefficients (Q11)
def fb_coeffs(nu, L, f, N):
    """a_n = 2/(L^2 J_{nu+1}(alpha)^2) * int_0^L x f(x) J_nu(alpha x / L) dx, J_nu(alpha)=0"""
    al = sc.jn_zeros(int(nu), N)
    return al, np.array([2/(L**2*J(nu+1, a)**2)*quad(lambda t: t*f(t)*J(nu, a*t/L), 0, L) for a in al])
def fb_sum(nu, L, al, c, xx, N): return sum(c[i]*J(nu, al[i]*xx/L) for i in range(N))

def check11(N=30):
    out = {}
    al, c = fb_coeffs(2, 1, lambda t: t, N)
    I0 = lambda t: sc.itj0y0(t)[0]
    cf = 2*(3*I0(al)-(al**2+6)*J(1, al))/(al**3*J(1, al)**2); ok("11a closed form", np.max(abs(c-cf)), 1e-10); out["a"] = (al, c)
    al, c = fb_coeffs(0, 3, lambda t: 1+0*t, N); ok("11b closed form", np.max(abs(c-2/(al*J(1, al)))), 1e-10); out["b"] = (al, c)
    al, c = fb_coeffs(1, 3, lambda t: t**3, N); ok("11c closed form", np.max(abs(c-54*(al**2-8)/(al**3*J(2, al)))), 1e-10); out["c"] = (al, c)
    al, c = fb_coeffs(2, 2, lambda t: t**2, N); ok("11d closed form", np.max(abs(c-8/(al*J(3, al)))), 1e-10); out["d"] = (al, c)
    # (e) nu = 1/2 : alpha = k pi, a_k = (-1)^(k+1) sqrt(2/k)
    kk = np.arange(1, N+1); alh = kk*np.pi
    ce = np.array([2/J(1.5, a)**2*quad(lambda t: t*np.sqrt(t)*J(.5, a*t), 0, 1) for a in alh])
    ok("11e closed form", np.max(abs(ce-(-1.0)**(kk+1)*np.sqrt(2/kk))), 1e-10); out["e"] = (alh, ce)
    kc = 0.4
    al = sc.jn_zeros(0, N); cfq = np.array([2/J(1, a)**2*quad(lambda t: t*J(0, a*t), 0, kc) for a in al])
    ok("11f closed form", np.max(abs(cfq-2*kc*J(1, al*kc)/(al*J(1, al)**2))), 1e-10); out["f"] = (al, cfq)
    # orthogonality / norm used in the derivation
    al0 = sc.jn_zeros(1, 4); G = np.array([[quad(lambda t: t*J(1, a*t)*J(1, b*t), 0, 1) for b in al0] for a in al0])
    ok("FB gram", np.max(abs(G-np.diag(.5*J(2, al0)**2))), 1e-12)
    return out

# ---------------------------------------------------------------- figures A6
def fig6_basics():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2)); t = np.linspace(-12, 12, 800)
    a = ax[0]
    for n in range(0, 5): a.plot(t, J(n, t), color=C[n], label=f"$J_{n}$")
    a.set_ylim(-1, 1.05); a.legend(ncol=5, fontsize=8); a.set_title(r"Q1: $J_n(-x)=(-1)^nJ_n(x)$ — even $n$ even, odd $n$ odd"); a.set_xlabel("x")
    a = ax[1]; tt = np.linspace(0.05, 14, 400)
    for n, c in ((1, C[0]), (2, C[1]), (3, C[2])):
        a.plot(tt, J(-n, tt), color=c, lw=3, alpha=.35); a.plot(tt, (-1)**n*J(n, tt), "--", color=c, lw=1.2, label=f"$J_{{-{n}}}$ (solid) vs $(-1)^{n}J_{n}$ (dashed)")
    a.legend(fontsize=7.5); a.set_title("Q1: the series for $J_{-n}$ coincides with $(-1)^nJ_n$"); a.set_xlabel("x")
    a = ax[2]; a.semilogy(tt, abs(J(4, tt)-((48/tt**3-8/tt)*J(1, tt)+(1-24/tt**2)*J(0, tt)))+1e-17, color=C[3], label=r"$|J_4-[(48/x^3-8/x)J_1+(1-24/x^2)J_0]|$")
    a.set_ylim(1e-18, 1e-6); a.legend(fontsize=8); a.set_title("Q8: $J_4$ from $J_0,J_1$ (rounding level)"); a.set_xlabel("x")
    fig.tight_layout(); save(fig, "A6-fig1-basics.png")

def fig6_identities():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2)); t = np.linspace(0.3, 14, 500); s = np.sqrt(2/(np.pi*t))
    a = ax[0]; a.plot(t, J(.5, t), color=C[0], label=r"$J_{1/2}=\sqrt{2/\pi x}\,\sin x$"); a.plot(t, J(-.5, t), color=C[1], label=r"$J_{-1/2}=\sqrt{2/\pi x}\,\cos x$")
    a.plot(t, J(1.5, t), color=C[2], label=r"$J_{3/2}=\sqrt{2/\pi x}\,(\sin x/x-\cos x)$"); a.plot(t, s, "k:", lw=1); a.plot(t, -s, "k:", lw=1)
    a.set_ylim(-1, 1); a.legend(fontsize=7.5); a.set_title("Q2(a),(b): half-integer orders are elementary"); a.set_xlabel("x")
    a = ax[1]; a.plot(t, J(.5, t)**2+J(-.5, t)**2, color=C[3], label=r"$J_{1/2}^2+J_{-1/2}^2$"); a.plot(t, 2/(np.pi*t), "k--", label=r"$2/(\pi x)$")
    a.plot(t, J(.5, t)*J(-.5, t), color=C[4], label=r"$J_{1/2}J_{-1/2}$"); a.plot(t, np.sin(2*t)/(np.pi*t), "k:", label=r"$\sin2x/(\pi x)$")
    a.set_ylim(-.2, .7); a.legend(fontsize=8); a.set_title("Q2(g),(h)"); a.set_xlabel("x")
    a = ax[2]
    names = ["a", "b", "c", "d", "e", "f", "g", "h", "7i/ii", "8"]; keys = ["Q2a", "Q2b", "Q2c", "Q2d", "Q2e", "Q2f", "Q2g", "Q2h", "Q7 i/ii", "Q8"]
    a.bar(range(len(keys)), [max(NUM[k], 1e-17) for k in keys], color=C[0]); a.set_yscale("log"); a.set_xticks(range(len(keys))); a.set_xticklabels(["2"+n if len(n) == 1 else "Q"+n for n in names], fontsize=8)
    a.set_ylim(1e-17, 1e-8); a.set_title("max residual of each identity\n(300 points, orders up to 5): all at rounding level"); a.set_ylabel("residual")
    fig.tight_layout(); save(fig, "A6-fig2-identities.png")

def fig6_integrals():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2)); t = np.linspace(0, 14, 600)
    a = ax[0]; a.plot(t, [quad(lambda u: u**4*J(0, u), 0, v) for v in t], color=C[0], lw=3, alpha=.4, label=r"$\int_0^x u^4J_0\,du$ (quadrature)")
    I0 = lambda v: sc.itj0y0(v)[0]; a.plot(t, (t**4-9*t**2)*J(1, t)+(3*t**3-9*t)*J(0, t)+9*I0(t), "k--", lw=1.1, label="Q3(a) closed form"); a.legend(fontsize=8); a.set_xlabel("x"); a.set_title(r"Q3(a): needs the non-elementary $\int J_0$")
    a = ax[1]; a.plot(t, [quad(lambda u: J(5, u), 0, v) for v in t], color=C[1], lw=3, alpha=.4, label=r"$\int_0^xJ_5$"); a.plot(t, -2*J(4, t)-2*J(2, t)-J(0, t)+1, "k--", lw=1.1, label=r"$-2J_4-2J_2-J_0+1$ ($C=1$)")
    a.legend(fontsize=8); a.set_xlabel("x"); a.set_title("Q3(b): telescoping $J_{n+1}=J_{n-1}-2J_n'$")
    a = ax[2]; tt = np.linspace(1, 12, 300)
    num = np.array([quad(lambda u: u**-2*J(5, u), 1, v) for v in tt]); Hc = lambda v: -v**-2*J(4, v)-2*v**-3*J(3, v); Hp = lambda v: -v**-2*J(4, v)+2*v**-3*J(3, v)
    a.plot(tt, num, color=C[2], lw=3, alpha=.4, label=r"$\int_1^xu^{-2}J_5$"); a.plot(tt, Hc(tt)-Hc(1), "k--", lw=1.1, label=r"$-x^{-2}J_4-2x^{-3}J_3$ (corrected)")
    a.plot(tt, Hp(tt)-Hp(1), color=C[1], lw=1.4, label=r"as printed: $+2x^{-3}J_3$ (wrong)"); a.legend(fontsize=8); a.set_xlabel("x"); a.set_title("Q3(c): the printed sign is wrong")
    fig.tight_layout(); save(fig, "A6-fig3-integrals.png")

def fig6_wronskian_zeros():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2)); t = np.linspace(0.3, 16, 500)
    a = ax[0]
    for nu, c in ((0, C[0]), (1, C[1]), (2.5, C[2])):
        W = J(nu, t)*Y(nu+0, t); h = 1e-6
        Wr = J(nu, t)*(Y(nu, t+h)-Y(nu, t-h))/(2*h)-Y(nu, t)*(J(nu, t+h)-J(nu, t-h))/(2*h); a.plot(t, t*Wr, color=c, label=rf"$\nu={nu}$")
    a.axhline(2/np.pi, color="k", ls="--", lw=1); a.set_ylim(.4, .9); a.legend(fontsize=8); a.set_title(r"Q4: $x\,W(J_\nu,Y_\nu)=2/\pi$ (constant)"); a.set_xlabel("x")
    a = ax[1]; t = np.linspace(0, 20, 800)
    for n, c in ((2, C[0]), (3, C[1]), (1, C[2])): a.plot(t, J(n, t), color=c, label=f"$J_{n}$")
    z = sc.jn_zeros(2, 5); a.plot(z, 0*z, "o", color=C[0]);
    for n, c in ((3, C[1]), (1, C[2])): zz = sc.jn_zeros(n, 5); a.plot(zz, 0*zz, "s", color=c, ms=5)
    a.set_xlim(0, 20); a.legend(fontsize=8); a.set_title("Q5: between consecutive zeros of $J_2$ exactly one zero\nof $J_3$ (squares, red) and one of $J_1$ (squares, green)")
    a = ax[2]; N = 15; zs = {n: sc.jn_zeros(n, N) for n in (0, 1, 2)}
    for i, (n, c) in enumerate(((0, C[0]), (1, C[1]), (2, C[2]))): a.plot(zs[n], np.full(N, i), "o", color=c, label=f"zeros of $J_{n}$")
    a.set_yticks([0, 1, 2]); a.set_yticklabels(["$J_0$", "$J_1$", "$J_2$"]); a.set_title("zeros of $J_0,J_1,J_2$ interlace (shifted by $\\approx\\pi/2$ each)"); a.set_xlabel("x"); a.grid(axis="y", alpha=0)
    fig.tight_layout(); save(fig, "A6-fig4-wronskian-zeros.png")

def fig6_transformations():
    fig, ax = plt.subplots(2, 3, figsize=(15, 8)); ax = ax.ravel()
    def nsolve(P, y0, dy0, t0, t1):                              # reference numerical solution y'' = P(t,y,y')
        s = integrate.solve_ivp(lambda t, u: [u[1], P(t, u[0], u[1])], (t0, t1), [y0, dy0], rtol=1e-12, atol=1e-13, dense_output=True); return s.sol
    cases = [("(a) $y''+4xy=0$", lambda t, y, dy: -4*t*y, lambda t: np.sqrt(t)*J(1/3, 4/3*t**1.5), lambda t: np.sqrt(t)*J(-1/3, 4/3*t**1.5), (0.5, 4)),
             ("(b) $x^2y''-3xy'+4(x^4-3)y=0$", lambda t, y, dy: (3*t*dy-4*(t**4-3)*y)/t**2, lambda t: t**2*J(2, t**2), lambda t: t**2*Y(2, t**2), (0.6, 3.2)),
             ("(d) $y''+e^{-x}y=0$", lambda t, y, dy: -np.exp(-t)*y, lambda t: J(0, 2*np.exp(-t/2)), lambda t: Y(0, 2*np.exp(-t/2)), (0, 8)),
             ("(f) $xy''-5y'+xy=0$", lambda t, y, dy: (5*dy-t*y)/t, lambda t: t**3*J(3, t), lambda t: t**3*Y(3, t), (0.5, 12)),
             ("(g) $xy''-(1+2p)y'+xy=0$, $p=1.5$", lambda t, y, dy: (4*dy-t*y)/t, lambda t: t**2.5*J(2.5, t), lambda t: t**2.5*J(-2.5, t), (0.5, 12)),
             ("(h) $y''+xy=0$", lambda t, y, dy: -t*y, lambda t: np.sqrt(t)*J(1/3, 2/3*t**1.5), lambda t: np.sqrt(t)*J(-1/3, 2/3*t**1.5), (0.3, 12))]
    for a, (ttl, P, y1, y2, (t0, t1)) in zip(ax, cases):
        tt = np.linspace(t0+1e-3, t1, 600)
        for yy, c, lab in ((y1, C[0], "$y_1$"), (y2, C[1], "$y_2$")):
            h = 1e-6; y0 = yy(t0+.05); d0 = (yy(t0+.05+h)-yy(t0+.05-h))/(2*h); sol = nsolve(P, y0, d0, t0+.05, t1)
            tr = tt[tt > t0+.05]; a.plot(tr, yy(tr), color=c, lw=3, alpha=.4); a.plot(tr, sol.sol(tr)[0] if hasattr(sol, "sol") else sol(tr)[0], "--", color=c, lw=1.1, label=lab+" (formula, solid; ODE solver, dashed)" if c == C[0] else lab)
        m = np.max(np.abs(y1(tt)))*1.3 if "(b)" not in ttl else 6; a.set_ylim(-min(m, 12), min(m, 12)); a.set_title(ttl, fontsize=9.5); a.set_xlabel("x"); a.legend(fontsize=7)
    fig.suptitle("Q6: the Bessel-form solutions (thick) coincide with direct numerical integration of the original ODE (dashed)", y=1.0); fig.tight_layout(); save(fig, "A6-fig5-transformations.png")

def fig6_sums():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2))
    a = ax[0]; N = 14; n = np.arange(1, N+1)
    for xv, c in ((0.5, C[0]), (3, C[1]), (10, C[2])):
        ps = [J(0, xv)**2+2*sum(J(k, xv)**2 for k in range(1, m+1)) for m in range(0, 25)]; a.plot(range(0, 25), ps, "o-", color=c, ms=3, label=f"$x={xv}$")
    a.axhline(1, color="k", ls="--"); a.set_xlabel("number of terms $m$"); a.legend(fontsize=8); a.set_title(r"Q10: $J_0^2+2\sum_{n\leq m}J_n^2\uparrow1$"); a.set_ylim(0, 1.1)
    a = ax[1]; xs = np.linspace(0, 30, 1500)
    for n_, c in ((0, C[0]), (1, C[1]), (2, C[2]), (5, C[3])): a.plot(xs, J(n_, xs), color=c, lw=1, label=f"$J_{n_}$")
    a.axhline(1/np.sqrt(2), color="k", ls="--", lw=1); a.axhline(-1/np.sqrt(2), color="k", ls="--", lw=1); a.axhline(1, color="grey", ls=":"); a.legend(fontsize=8, ncol=4); a.set_xlabel("x")
    a.set_title(r"$|J_0|\leq1$ and $|J_n|\leq1/\sqrt{2}$ ($n\geq1$): bounds hold");
    a = ax[2]; nu, aa, bb, cc = 1.3, 1.1, 2.3, 3.0; cs = np.linspace(.2, 6, 60)
    lhs = [quad(lambda t: J(nu, aa*t)*J(nu, bb*t)*t, 0, c_) for c_ in cs]; rhs = cs/(bb**2-aa**2)*(aa*J(nu, bb*cs)*J(nu-1, aa*cs)-bb*J(nu, aa*cs)*J(nu-1, bb*cs))
    a.plot(cs, lhs, color=C[4], lw=4, alpha=.4, label="quadrature"); a.plot(cs, rhs, "k--", lw=1.1, label="Q12 closed form"); a.legend(fontsize=8); a.set_xlabel("c"); a.set_title(r"Q12: $\int_0^cJ_\nu(ax)J_\nu(bx)x\,dx$ ($\nu=1.3,a=1.1,b=2.3$)")
    fig.tight_layout(); save(fig, "A6-fig6-sums.png")

def fig6_fourier_bessel(co):
    fig, ax = plt.subplots(2, 3, figsize=(15, 8)); ax = ax.ravel()
    spec = [("a", 2, 1, lambda t: t, r"(a) $f=x$ on $[0,1]$, $\nu=2$"), ("b", 0, 3, lambda t: 1+0*t, r"(b) $f=1$ on $[0,3]$, $\nu=0$"), ("c", 1, 3, lambda t: t**3, r"(c) $f=x^3$ on $[0,3]$, $\nu=1$"),
            ("d", 2, 2, lambda t: t**2, r"(d) $f=x^2$ on $[0,2]$, $\nu=2$")]
    for a, (k, nu, L, f, ttl) in zip(ax, spec):
        al, c = co[k]; xx = np.linspace(0, L, 500); a.plot(xx, f(xx), "k", lw=3, alpha=.35, label="$f$")
        for N, col in ((3, C[1]), (8, C[2]), (25, C[0])): a.plot(xx, fb_sum(nu, L, al, c, xx, N), color=col, lw=1.1, label=f"{N} terms")
        a.set_title(ttl, fontsize=10); a.legend(fontsize=8); a.set_xlabel("x")
    a = ax[4]; al, c = co["e"]; xx = np.linspace(.001, 1, 800); a.plot(xx, np.sqrt(xx), "k", lw=3, alpha=.35, label=r"$\sqrt{x}$")
    for N, col in ((3, C[1]), (8, C[2]), (30, C[0])): a.plot(xx, sum(c[i]*J(.5, al[i]*xx) for i in range(N)), color=col, lw=1.1, label=f"{N} terms")
    a.set_title(r"(e) $f=\sqrt{x}$, $\nu=\frac{1}{2}$: $\alpha_k=k\pi$, $a_k=(-1)^{k+1}\sqrt{2/k}$", fontsize=10); a.legend(fontsize=8); a.set_xlabel("x")
    a = ax[5]; al, c = co["f"]; kc = .4; xx = np.linspace(0, 1, 800); a.plot(xx, (xx < kc)*1.0, "k", lw=3, alpha=.35, label=f"$f$ ($\kappa={kc}$)")
    for N, col in ((5, C[1]), (15, C[2]), (30, C[0])): a.plot(xx, fb_sum(0, 1, al, c, xx, N), color=col, lw=1.1, label=f"{N} terms")
    a.plot([kc], [.5], "o", color=C[4], label="limit at the jump = 1/2"); a.set_title("(f) step function, $\\nu=0$: Gibbs overshoot, value $\\frac{1}{2}$ at $x=k$", fontsize=10); a.legend(fontsize=8); a.set_xlabel("x")
    fig.tight_layout(); save(fig, "A6-fig7-fourier-bessel.png")

def fig6_spherical():
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.2)); t = np.linspace(0.01, 20, 800)
    a = ax[0]
    for n in range(0, 4): a.plot(t, sc.spherical_jn(n, t), color=C[n], label=f"$j_{n}$")
    a.plot(t, np.sin(t)/t, "k:", lw=1); a.set_ylim(-.4, 1.05); a.legend(fontsize=8, ncol=4); a.set_title(r"Q13,14: $j_n(x)=\sqrt{\pi/2x}\,J_{n+1/2}(x)$"); a.set_xlabel("x")
    a = ax[1]; xv = 3.7; K = np.arange(0, 12)
    sin_p = np.cumsum(2*(-1.0)**K*J(2*K+1, xv)); cos_p = J(0, xv)+np.concatenate([[0], np.cumsum(2*(-1.0)**K[1:]*J(2*K[1:], xv))]); one_p = J(0, xv)+np.concatenate([[0], np.cumsum(2*J(2*K[1:], xv))])
    a.plot(range(1, 13), sin_p, "o-", color=C[0], ms=4, label=r"$2J_1-2J_3+\dots\to\sin x$"); a.plot(range(0, 12), cos_p, "s-", color=C[1], ms=4, label=r"$J_0-2J_2+2J_4-\dots\to\cos x$"); a.plot(range(0, 12), one_p, "^-", color=C[2], ms=4, label=r"$J_0+2J_2+2J_4+\dots\to1$")
    for v, c in ((np.sin(xv), C[0]), (np.cos(xv), C[1]), (1, C[2])): a.axhline(v, color=c, ls="--", lw=.9)
    a.set_xlabel("number of terms"); a.legend(fontsize=8); a.set_title("Q13 (Jacobi–Anger series) at $x=3.7$: converge super-geometrically")
    a = ax[2]; bb = 0.8; aa = np.linspace(.2, 4, 60); a.plot(aa, [quad(lambda s: np.exp(-q*s)*J(0, bb*s), 0, np.inf) for q in aa], color=C[3], lw=4, alpha=.4, label="quadrature"); a.plot(aa, 1/np.sqrt(aa**2+bb**2), "k--", lw=1.1, label=r"$1/\sqrt{a^2+b^2}$ ($b=0.8$)")
    a.legend(fontsize=8); a.set_xlabel("a"); a.set_title(r"Q14: $\int_0^\infty e^{-ax}J_0(bx)\,dx$")
    fig.tight_layout(); save(fig, "A6-fig8-spherical-jacobi-laplace.png")

# =====================================================================================================================
#                                               ASSIGNMENT 7
# =====================================================================================================================
mpf = mp.mpf
def residual(res_fn, y_fn, pts):
    """res_fn(y, t) : mp expression of the operator applied to y at t (uses mp.diff)"""
    return max(abs(res_fn(y_fn, mpf(t))) for t in pts)
d1 = lambda y, t: mp.diff(y, t); d2 = lambda y, t: mp.diff(y, t, 2)

def eig_problems():
    """each entry: (label, operator residual, y_n, lambda_n, boundary functionals, weight r, interval)"""
    P = {}
    P["a"] = dict(res=lambda y, t, lam: d2(y, t)+lam*y(t), y=lambda n: (lambda t: mp.sin((n-mpf(1)/2)*t)), lam=lambda n: (n-mpf(1)/2)**2, bc=lambda y: (y(0), d1(y, mpf(mp.pi))), w=lambda t: 1, I=(0, np.pi), ns=range(1, 5))
    P["b"] = dict(res=lambda y, t, lam: d2(y, t)+4*d1(y, t)-lam*y(t), y=lambda n: (lambda t: mp.exp(-2*t)*((n*mp.pi/2)*mp.cos(n*mp.pi*t/2)+2*mp.sin(n*mp.pi*t/2))) if n else (lambda t: mpf(1)),
                  lam=lambda n: -(4+(n*mp.pi/2)**2) if n else mpf(0), bc=lambda y: (d1(y, mpf(0)), d1(y, mpf(2))), w=lambda t: np.exp(4*t), I=(0, 2), ns=range(0, 4))
    P["c"] = dict(res=lambda y, t, lam: d2(y, t)+lam*y(t), y=lambda n: (lambda t: mp.cos(n*t)), lam=lambda n: mpf(n)**2, bc=lambda y: (y(0)-y(2*mp.pi), d1(y, mpf(0))-d1(y, 2*mp.pi)), w=lambda t: 1, I=(0, 2*np.pi), ns=range(0, 4))
    P["d"] = dict(res=lambda y, t, lam: d2(y, t)+2*d1(y, t)+(lam+1)*y(t), y=lambda n: (lambda t: mp.exp(-t)*mp.sin(n*t)), lam=lambda n: mpf(n)**2, bc=lambda y: (y(0), y(mp.pi)), w=lambda t: np.exp(2*t), I=(0, np.pi), ns=range(1, 5))
    L = mpf(2.7)
    P["e"] = dict(res=lambda y, t, lam: d2(y, t)-d1(y, t)+lam*y(t), y=lambda n: (lambda t: mp.exp(t/2)*mp.sin(n*mp.pi*t/L)), lam=lambda n: mpf(1)/4+(n*mp.pi/L)**2, bc=lambda y: (y(0), y(L)), w=lambda t: np.exp(-t), I=(0, float(L)), ns=range(1, 5))
    P["f"] = dict(res=lambda y, t, lam: d1(lambda s: s*d1(y, s), t)+lam/t*y(t), y=lambda n: (lambda t: mp.sin((n-mpf(1)/2)*mp.pi*mp.log(t))), lam=lambda n: ((n-mpf(1)/2)*mp.pi)**2, bc=lambda y: (y(1), d1(y, mp.e)), w=lambda t: 1/t, I=(1, np.e), ns=range(1, 5))
    kg = lambda n: n*mp.pi/(1-mp.exp(-2*mp.pi))
    P["g"] = dict(res=lambda y, t, lam: d1(lambda s: mp.exp(2*s)*d1(y, s), t)+mp.exp(-2*t)*(lam+1)*y(t), y=lambda n: (lambda t: mp.sin(kg(n)*(mp.exp(-2*t)-mp.exp(-2*mp.pi)))), lam=lambda n: 4*kg(n)**2-1, bc=lambda y: (y(0), y(mp.pi)), w=lambda t: np.exp(-2*t), I=(0, np.pi), ns=range(1, 5))
    kh = lambda n: n*mp.pi/(mp.e-1)
    P["h"] = dict(res=lambda y, t, lam: 4*d1(lambda s: mp.exp(-s)*d1(y, s), t)+(1+lam)*mp.exp(t)*y(t), y=lambda n: (lambda t: mp.sin(kh(n)*(mp.exp(t)-1))), lam=lambda n: 4*kh(n)**2-1, bc=lambda y: (y(0), y(1)), w=lambda t: np.exp(t), I=(0, 1), ns=range(1, 5))
    P["i"] = dict(res=lambda y, t, lam: d1(lambda s: (s**2+1)*d1(y, s), t)+lam/(t**2+1)*y(t), y=lambda n: (lambda t: mp.cos(4*n*mp.atan(t))), lam=lambda n: mpf(16)*n**2, bc=lambda y: (d1(y, mpf(0)), d1(y, mpf(1))), w=lambda t: 1/(1+t**2), I=(0, 1), ns=range(0, 4))
    P["l"] = dict(res=lambda y, t, lam: t**2*d2(y, t)+t*d1(y, t)+lam*y(t), y=lambda n: (lambda t: mp.sin(n*mp.pi*mp.log(t))), lam=lambda n: (n*mp.pi)**2, bc=lambda y: (y(1), y(mp.e)), w=lambda t: 1/t, I=(1, np.e), ns=range(1, 5))
    P["m"] = dict(res=lambda y, t, lam: t**2*d2(y, t)-t*d1(y, t)+(lam+1)*y(t), y=lambda n: (lambda t: t*mp.sin(n*mp.pi*mp.log(t))), lam=lambda n: (n*mp.pi)**2, bc=lambda y: (y(1), y(mp.e)), w=lambda t: t**-3, I=(1, np.e), ns=range(1, 5))
    return P

def check_eig(P):
    for k, p in P.items():
        lo, hi = p["I"]; pts = [lo+(hi-lo)*u for u in (.13, .41, .77)]
        r = 0
        for n in p["ns"]:
            y = p["y"](n); lam = p["lam"](n)
            r = max(r, residual(lambda yy, t: p["res"](yy, t, lam), y, pts), *[abs(v) for v in p["bc"](y)])
        ok("Q3"+k, r, 1e-15)
        # orthogonality with the S-L weight
        ns = list(p["ns"]); fl = [(lambda t, y=p["y"](n): float(y(mpf(t)))) for n in ns]
        G = np.array([[quad(lambda t: p["w"](t)*fl[i](t)*fl[j](t), *p["I"]) for j in range(len(ns))] for i in range(len(ns))])
        off = np.max(abs(G-np.diag(np.diag(G)))); ok("Q3"+k+" orth", off/np.max(abs(np.diag(G))), 1e-9)
        p["G"] = G

def check_Q4_5_6():
    mus = np.array([optimize.brentq(lambda m: np.cos(m)-m*np.sin(m), n*np.pi+1e-9, n*np.pi+np.pi/2-1e-9) for n in range(0, 40)])
    NUM["mu"] = mus[:4]
    N_b = lambda m: .5*(1+np.sin(m)**2)
    ok("Q4b norm", max(abs(quad(lambda t: np.cos(m*t)**2, 0, 1)-N_b(m)) for m in mus[:5]), 1e-12)
    G = np.array([[quad(lambda t: np.cos(a*t)*np.cos(b*t), 0, 1) for b in mus[:5]] for a in mus[:5]]); ok("Q4b orth", np.max(abs(G-np.diag(np.diag(G)))), 1e-12)
    ok("Q4a norm", max(abs(quad(lambda t: np.sin((n-.5)*np.pi*t)**2, 0, 1)-.5) for n in range(1, 6)), 1e-12)
    # Q4(d): J_m(alpha_k x / a)
    m, a_ = 2, 1.7; al = sc.jn_zeros(m, 4); Gd = np.array([[quad(lambda t: t*J(m, p*t/a_)*J(m, q*t/a_), 0, a_) for q in al] for p in al])
    ok("Q4d", np.max(abs(Gd-np.diag(.5*a_**2*J(m+1, al)**2))), 1e-12)
    # Q5: expansions in sin((n-1/2) pi x)
    n = np.arange(1, 4001); mu = (n-.5)*np.pi
    cos_h = lambda s: np.cos(s*mu/2); sin_h = lambda s: np.sin(mu/2)
    A5 = {"a": 2/mu, "b": 2*(-1.0)**(n+1)/mu**2, "c": 2/mu-2*(-1.0)**(n+1)/mu**2, "step": 2*(1-np.cos(mu/2))/mu, "tent": 4*np.sin(mu/2)/mu**2}
    fs = {"a": lambda t: 1+0*t, "b": lambda t: t, "c": lambda t: 1-t, "step": lambda t: (t < .5)*1.0, "tent": lambda t: np.where(t < .5, 2*t, 1.0)}
    for k in A5:
        for i in range(5):
            ref = 2*quad(lambda t: fs[k](t)*np.sin(mu[i]*t), 0, 1, points=[.5]); assert abs(ref-A5[k][i]) < 1e-11, (k, i, ref, A5[k][i])
    NUM["A5"] = A5
    # Q6: orthonormal expansions in cos(mu_n x)/sqrt(N_n)
    c6 = {"a": lambda m: np.sin(m)/m, "b": lambda m: np.sin(m)/m+(np.cos(m)-1)/m**2, "c": lambda m: (1-np.cos(m))/m**2, "step": lambda m: np.sin(m/2)/m,
          "tent": lambda m: np.sin(m)/m+2*(np.cos(m/2)-1)/m**2}
    for k in c6:
        for i in range(5):
            ref = quad(lambda t: fs[k](t)*np.cos(mus[i]*t), 0, 1, points=[.5]); assert abs(ref-c6[k](mus[i])) < 1e-11, (k, i)
    NUM["A6"] = {k: c6[k](mus) for k in c6}; NUM["mus"] = mus
    NUM["A5ok"] = True
    return mus, A5, c6, fs

# ---------------------------------------------------------------- figures A7
def fig7_eigenfunctions(P):
    fig, ax = plt.subplots(3, 4, figsize=(19, 10.5)); ax = ax.ravel()
    ttl = {"a": r"(a) $y''+\lambda y=0$, $y(0)=y'(\pi)=0$", "b": r"(b) $y''+4y'-\lambda y=0$, $y'(0)=y'(2)=0$", "c": r"(c) periodic: $\cos nx$ ($\sin nx$ too)", "d": r"(d) $y''+2y'+(\lambda+1)y=0$",
           "e": r"(e) $y''-y'+\lambda y=0$, $L=2.7$", "f": r"(f) $(xy')'+\frac{\lambda}{x}y=0$", "g": r"(g) $(e^{2x}y')'+e^{-2x}(\lambda+1)y=0$", "h": r"(h) $4(e^{-x}y')'+(1+\lambda)e^xy=0$",
           "i": r"(i) $((x^2+1)y')'+\frac{\lambda}{x^2+1}y=0$", "l": r"(l) $x^2y''+xy'+\lambda y=0$", "m": r"(m) $x^2y''-xy'+(\lambda+1)y=0$"}
    for a, (k, p) in zip(ax, [(k, p) for k, p in P.items()]):
        lo, hi = p["I"]; tt = np.linspace(lo+1e-9, hi, 500)
        for j, n in enumerate(list(p["ns"])[:3]):
            y = p["y"](n); v = np.array([float(y(mpf(t))) for t in tt]); a.plot(tt, v/np.max(abs(v)), color=C[j], label=rf"$n={n}$, $\lambda={float(p['lam'](n)):.2f}$")
        a.axhline(0, color="k", lw=.6); a.set_title(ttl[k], fontsize=8); a.legend(fontsize=7, loc="lower left")
    a = ax[11]; a.set_title(r"(j) as printed: $x^2y''-3xy'+\lambda y=0$, $y'(0)=y'(\pi)=0$", fontsize=8)
    a.set_xlim(-.5, 8); a.set_ylim(-1, 1); a.set_yticks([]); a.axvspan(3, 8, color=C[1], alpha=.3); a.plot([0], [0], "o", color=C[0], ms=8)
    a.annotate(r"$\lambda=0$, $y=1$", (0, 0), (.3, .5), arrowprops=dict(arrowstyle="->"), fontsize=8); a.text(3.2, -.2, r"every $\lambda>3$ passes:" + chr(10) + r"a continuum (singular end $x=0$," + chr(10) + "not a discrete SLP)", fontsize=8, color=C[1]); a.set_xlabel(r"$\lambda$ admitted by the printed conditions")
    fig.tight_layout(); save(fig, "A7-fig1-eigenfunctions.png")

def fig7_orthogonality(P, mus):
    fig, ax = plt.subplots(1, 4, figsize=(16, 3.9))
    ims = []
    def gram(a, G, ttl):
        d = np.sqrt(np.diag(G)); Gn = G/np.outer(d, d); im = a.imshow(abs(Gn), cmap="Blues", vmin=0, vmax=1); a.set_title(ttl, fontsize=9)
        for i in range(len(G)):
            for j in range(len(G)): a.text(j, i, f"{Gn[i, j]:.0e}" if i != j else "1", ha="center", va="center", fontsize=7)
        a.set_xticks(range(len(G))); a.set_yticks(range(len(G))); a.grid(False)
    gram(ax[0], P["a"]["G"], "4(a) $\\sin((n-\\frac{1}{2})\\pi x)$, weight 1")
    Gb = np.array([[quad(lambda t: np.cos(p*t)*np.cos(q*t), 0, 1) for q in mus[:4]] for p in mus[:4]]); gram(ax[1], Gb, r"4(b) $\cos\mu_nx$, $\mu\tan\mu=1$")
    gram(ax[2], np.array([[quad(lambda t: np.sin(i*np.pi*t/2.5)*np.sin(j*np.pi*t/2.5), 0, 2.5) for j in range(1, 5)] for i in range(1, 5)]), "4(c) $\\sin(n\\pi x/L)$, weight 1")
    al = sc.jn_zeros(2, 4); gram(ax[3], np.array([[quad(lambda t: t*J(2, p*t)*J(2, q*t), 0, 1) for q in al] for p in al]), "4(d) $J_2(\\alpha_nx/a)$, weight $x$")
    fig.suptitle("Q4: normalised Gram matrices $\\langle y_m,y_n\\rangle_r/\\sqrt{\\langle y_m,y_m\\rangle\\langle y_n,y_n\\rangle}$ — off-diagonal entries are rounding errors", y=1.03)
    fig.tight_layout(); save(fig, "A7-fig2-orthogonality.png")

def fig7_expansions(mus, A5, c6, fs):
    lab = {"a": "$f=1$", "b": "$f=x$", "c": "$f=1-x$", "step": r"$f=1$ on $[0,\frac{1}{2})$, 0 after", "tent": r"$f=2x$ on $[0,\frac{1}{2})$, 1 after"}
    xx = np.linspace(0, 1, 700); n = np.arange(1, len(A5["a"])+1)
    for tag, fname in (("5", "A7-fig3-expansions-4a.png"), ("6", "A7-fig4-expansions-4b.png")):
        fig, ax = plt.subplots(1, 5, figsize=(20, 3.8))
        for a, k in zip(ax, ("a", "b", "c", "step", "tent")):
            a.plot(xx, fs[k](xx), "k", lw=3, alpha=.3, label="$f$")
            for N, col in ((2, C[1]), (6, C[2]), (30, C[0])):
                if tag == "5": s = sum(A5[k][i]*np.sin((i+.5)*np.pi*xx) for i in range(N))
                else: s = sum(c6[k](mus[i])/(.5*(1+np.sin(mus[i])**2))*np.cos(mus[i]*xx) for i in range(N))
                a.plot(xx, s, color=col, lw=1.1, label=f"{N} terms")
            a.set_title(lab[k], fontsize=9); a.legend(fontsize=7)
        fig.suptitle("Q5: eigenfunction expansions in the eigenfunctions of 4(a)" if tag == "5" else "Q6: orthonormal expansions in the eigenfunctions of 4(b)", y=1.04); fig.tight_layout(); save(fig, fname)
    # coefficient / error decay
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.2)); Ns = np.arange(1, 60)
    nn = np.arange(1, 3000)
    a = ax[0]
    for k, col in zip(("a", "b", "c", "step", "tent"), C):
        a.loglog(nn[:200], abs(A5[k][:200])+1e-18, color=col, label=lab[k])
    a.set_xlabel("n"); a.set_ylabel("$|a_n|$"); a.set_title("Q5: $|a_n|\\sim1/n$ if $f(0)\\neq0$ or $f$ jumps; $\\sim1/n^2$ if $f$ is continuous with $f(0)=0$"); a.legend(fontsize=7.5)
    a = ax[1]
    for k, col in zip(("a", "b", "c", "step", "tent"), C):
        tot = quad(lambda t: fs[k](t)**2, 0, 1, points=[.5]); parts = np.cumsum(A5[k]**2/2); a.semilogy(Ns, np.maximum(tot-parts[Ns-1], 1e-17), color=col, label=lab[k])
    a.set_xlabel("N"); a.set_ylabel(r"$\|f-S_N\|^2$ (Parseval)"); a.set_title("Q5: $L^2$ error via Parseval $\\|f\\|^2=\\frac{1}{2}\\sum a_n^2$"); a.legend(fontsize=7.5)
    fig.tight_layout(); save(fig, "A7-fig5-decay.png")

# =====================================================================================================================
if __name__ == "__main__":
    check6(); co = check11(); print("A6 checks passed")
    P = eig_problems(); check_eig(P); mus, A5, c6, fs = check_Q4_5_6(); print("A7 checks passed")
    for k in ("Q3c printed", "max|J0|", "max_n>=1 |Jn|"): print(k, NUM[k])
    print("mu_n", NUM["mu"])
    for k in ("a", "b", "c", "step", "tent"): print("Q5", k, np.round(A5[k][:4], 6), "| Q6 c_n", np.round(c6[k](mus[:4]), 6))
    for k in ("a", "b", "c", "d", "e", "f"): print("Q11", k, np.round(co[k][1][:4], 6), "alpha", np.round(co[k][0][:3], 5))
    fig6_basics(); fig6_identities(); fig6_integrals(); fig6_wronskian_zeros(); fig6_transformations(); fig6_sums(); fig6_fourier_bessel(co); fig6_spherical()
    fig7_eigenfunctions(P); fig7_orthogonality(P, mus); fig7_expansions(mus, A5, c6, fs)
    print("all checks passed")

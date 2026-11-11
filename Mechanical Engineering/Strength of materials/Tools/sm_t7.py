"""AM2200 Tutorial 7 (Bending and Shear Stresses): verification numbers and figures.
Run:  python -I sm_t7.py        (figures -> ../assets/SM-T7-*.png)
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Wedge, Circle

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')
os.makedirs(ASSETS, exist_ok=True)
def save(fig, name): fig.savefig(os.path.join(ASSETS, name), dpi=130, bbox_inches='tight'); plt.close(fig)

TEN, COM = '#d62728', '#1f77b4'          # tension red, compression blue

def rect_section(parts):
    """parts = [(z_bot, z_top, width, weight)]  (z up). Returns centroid, EI-like I (weight-scaled), A_w."""
    Aw = sum(w*(t-b)*k for b, t, w, k in parts)
    zc = sum(k*w*(t-b)*(t+b)/2 for b, t, w, k in parts)/Aw
    I = sum(k*(w*(t-b)**3/12 + w*(t-b)*((t+b)/2-zc)**2) for b, t, w, k in parts)
    return zc, I, Aw

# ================================================================ Q1 simply supported rod, self weight
gam = 490.0                                  # lb/ft^3
L = 10.0                                     # ft
sig_allow = 4000*144.0                       # lb/ft^2
# sigma = 32 M/(pi d^3), M = w L^2/8, w = gam pi d^2/4  ->  sigma = gam L^2/d  (d^2 cancels)
d1 = gam*L**2/sig_allow
print('Q1 d = %.5f ft = %.4f in   (w = %.3f lb/ft, M = %.1f lb-ft)' % (d1, d1*12, gam*np.pi/4*d1**2, gam*np.pi/4*d1**2*L**2/8))
# brute-force check: stress at d = d1
w = gam*np.pi/4*d1**2; M = w*L**2/8; I = np.pi*d1**4/64
print('Q1 check sigma = %.1f psi' % (M*(d1/2)/I/144))
ds = np.linspace(0.5, 2.0, 200)/12
sig_d = gam*L**2/ds/144/1000                                       # ksi
fig, axs = plt.subplots(1, 3, figsize=(16, 3.8))
ax = axs[0]
ax.plot([0, L], [0, 0], 'k', lw=6, solid_capstyle='round'); ax.plot([0], [-.12], '^', ms=14, c='gray'); ax.plot([L], [-.12], 'o', ms=12, c='gray')
for xx in np.linspace(.4, L-.4, 12): ax.annotate('', xy=(xx, .08), xytext=(xx, .55), arrowprops=dict(arrowstyle='->', color='crimson'))
ax.text(L/2, .65, 'w = γπd²/4  (self-weight)', ha='center', color='crimson'); ax.annotate('', xy=(0, -.5), xytext=(L, -.5), arrowprops=dict(arrowstyle='<->')); ax.text(L/2, -.8, 'L = 10 ft', ha='center')
ax.set_xlim(-1, L+1); ax.set_ylim(-1, 1); ax.axis('off'); ax.set_title('Simply supported rod, uniform self-weight')
ax = axs[1]; x = np.linspace(0, L, 200); ax.plot(x, w*x*(L-x)/2, c='navy', lw=2); ax.fill_between(x, w*x*(L-x)/2, alpha=.2); ax.set_title('M(x) = w x (L−x)/2,  M_max = wL²/8 at midspan'); ax.set_xlabel('x (ft)'); ax.set_ylabel('lb·ft'); ax.grid(alpha=.3)
ax = axs[2]; ax.plot(ds*12, sig_d, c='crimson', lw=2); ax.axhline(4, c='k', ls=':'); ax.axvline(d1*12, c='k', ls=':'); ax.plot(d1*12, 4, 'ko'); ax.text(d1*12+.05, 4.4, f'd = {d1*12:.3f} in', fontsize=10)
ax.set_xlabel('d (in)'); ax.set_ylabel('σ_max (ksi)'); ax.set_title('σ_max = γL²/d  (weight ∝ d², S ∝ d³)'); ax.grid(alpha=.3); ax.set_ylim(0, 12)
save(fig, 'SM-T7-Q1-rod.png')

# ================================================================ Q2 bimodular beam
def bimodular(Et, Ec, b=1.0, h=1.0, M=1.0):
    c = h*np.sqrt(Et)/(np.sqrt(Et)+np.sqrt(Ec))           # compression-side depth
    t = h-c
    k = 3*M*(np.sqrt(Et)+np.sqrt(Ec))**2/(b*h**3*Et*Ec)  # curvature
    return c, t, k, Ec*k*c, Et*k*t
Et, Ec = 1.0, 2.0
c, t, k, sc, st = bimodular(Et, Ec)
# brute-force: find NA from force balance and M by numerical integration
y = np.linspace(-1, 1, 400001); dy = y[1]-y[0]
def forces(na):
    # y measured from bottom; y>na is tension. strain = k (y - na)
    yy = np.linspace(0, 1, 200001); e = (yy-na)
    s = np.where(e > 0, Et*e, Ec*e)
    return np.trapezoid(s, yy), np.trapezoid(s*(yy-na), yy)
from scipy.optimize import brentq
na = brentq(lambda a: forces(a)[0], 0.01, 0.99)
print('Q2 (Et=1, Ec=2): c_formula = %.5f, c_numeric(NA from bottom) = %.5f' % (c, na))
Mnum = abs(forces(na)[1]); print('Q2 M for unit curvature = %.5f, formula k=1 -> M = %.5f' % (Mnum, 1.0/(3*(np.sqrt(Et)+np.sqrt(Ec))**2/(Et*Ec))))
ratios = np.logspace(-1.5, 1.5, 200)
fig, axs = plt.subplots(1, 3, figsize=(16, 4))
ax = axs[0]; ax.plot([0, 0], [-1.05, 1.05], 'k', lw=.5); ax.plot([-1.2, 1.2], [0, 0], 'k', lw=.5)
e = np.linspace(-1, 1, 3); ax.plot(e, np.where(e > 0, Et*e, Ec*e), c='navy', lw=3); ax.text(.45, .5, 'slope $E_t$', color=TEN); ax.text(-.9, -1.35, 'slope $E_c$', color=COM); ax.set_title('Bimodular σ–ε law (Fig. 2)'); ax.set_xlabel('ε'); ax.set_ylabel('σ'); ax.grid(alpha=.3)
ax = axs[1]
ax.add_patch(Rectangle((0, 0), .4, 1, fc='#eeeeee', ec='k')); ax.plot([-.1, .5], [c, c], 'k--'); ax.text(.52, c, 'neutral axis', va='center')
ax.annotate('', xy=(-.08, 0), xytext=(-.08, c), arrowprops=dict(arrowstyle='<->')); ax.text(-.12, c/2, 'c', fontsize=12, ha='right', va='center')
ax.annotate('', xy=(-.08, c), xytext=(-.08, 1), arrowprops=dict(arrowstyle='<->')); ax.text(-.12, (1+c)/2, 'h − c', fontsize=10, ha='right', va='center')
ax.text(.2, c/2, 'compression', ha='center', color=COM); ax.text(.2, (1+c)/2, 'tension', ha='center', color=TEN)
ax.set_title('Neutral axis for $E_t=1$, $E_c=2$:  c = %.3f h' % c); ax.set_xlim(-.4, 1.0); ax.set_ylim(-.05, 1.05); ax.axis('off')
ax = axs[2]; yy = np.linspace(0, 1, 300); sg = np.where(yy > c, Et*k*(yy-c), Ec*k*(yy-c))
ax.fill_betweenx(yy, 0, sg, where=sg > 0, color=TEN, alpha=.4); ax.fill_betweenx(yy, 0, sg, where=sg < 0, color=COM, alpha=.4); ax.plot(sg, yy, 'k', lw=1.5); ax.axvline(0, c='k', lw=.5); ax.axhline(c, c='k', ls='--', lw=.7)
ax.text(sg[0]*1.0, 0.03, f'σ_c,max = {sc:.2f} (M/bh²)', ha='left', fontsize=8); ax.text(sg[-1]*.98, .96, f'σ_t,max = {st:.2f}', ha='right', fontsize=8)
ax.set_title('Stress profile: kink at the NA'); ax.set_xlabel('σ  (units of M/(b h²))'); ax.set_ylabel('y/h from bottom')
save(fig, 'SM-T7-Q2-bimodular.png')
fig, ax = plt.subplots(figsize=(6.2, 3.8)); ax.semilogx(ratios, np.sqrt(ratios)/(1+np.sqrt(ratios)), c='navy', lw=2)       # c/h vs Et/Ec
ax.axhline(.5, c='gray', ls=':'); ax.axvline(1, c='gray', ls=':'); ax.plot(1, .5, 'ko'); ax.text(1.15, .46, 'E_t = E_c: NA at mid-depth')
ax.set_xlabel('E_t / E_c'); ax.set_ylabel('c / h  (compression depth)'); ax.set_title('Neutral-axis position vs modulus ratio'); ax.grid(alpha=.3)
save(fig, 'SM-T7-Q2-na-shift.png')

# ================================================================ Q3 diving board (mm, N)
m, g = 78.0, 9.81; W = m*g
RA = -W*2.5/1.5                               # downward on board at A (negative = down)
RB = W - RA                                    # upward at B
MB = W*2.5*1e3                                 # N mm, hogging at B
# section (z up from bottom of legs): legs 3 x (10 wide, 30 tall) at 0-30, plate 350 x 20 at 30-50
sec = [(0, 30, 30, 1.0), (30, 50, 350, 1.0)]          # legs: total width 3*10 = 30
zc, I, A = rect_section(sec)
ctop, cbot = 50-zc, zc
E = 125e3                                       # MPa
sig_max = MB*max(ctop, cbot)/I
print('Q3 R_A = %.1f N (down), R_B = %.1f N (up), M_B = %.1f N m (hogging)' % (-RA, RB, MB/1e3))
print('Q3 zbar = %.3f mm above bottom, I = %.1f mm^4 (%.4e), c_top = %.3f, c_bot = %.3f' % (zc, I, I, ctop, cbot))
print('Q3 sigma_max = %.3f MPa (bottom, compression), eps_max = %.6e' % (sig_max, sig_max/E))
# grid cross-check of centroid and I
zg = np.linspace(0, 50, 500001); wg = np.where(zg < 30, 30, 350.0); Ag = np.trapezoid(wg, zg); zcg = np.trapezoid(wg*zg, zg)/Ag; Ig = np.trapezoid(wg*(zg-zcg)**2, zg)
print('Q3 grid check: zc = %.3f, I = %.1f' % (zcg, Ig))
fig, axs = plt.subplots(1, 4, figsize=(20, 4.4), gridspec_kw={'width_ratios': [1.2, 1, 1.1, 1]})
ax = axs[0]; ax.plot([0, 4], [0, 0], 'k', lw=5); ax.plot([0], [-.1], 'o', ms=10, c='gray'); ax.plot([1.5], [-.14], '^', ms=12, c='gray')
ax.annotate('', xy=(4, .05), xytext=(4, 1.0), arrowprops=dict(arrowstyle='->', color='crimson', lw=2)); ax.text(3.9, 1.08, 'W = 765.2 N', color='crimson', ha='center')
ax.annotate('', xy=(0, .05), xytext=(0, .9), arrowprops=dict(arrowstyle='->', color='green', lw=1.5)); ax.text(0, 1.0, 'R_A = 1275 N (down)', color='green', fontsize=8, ha='left')
ax.annotate('', xy=(1.5, .95), xytext=(1.5, .05), arrowprops=dict(arrowstyle='->', color='green', lw=1.5)); ax.text(1.5, -.55, 'R_B = 2040 N (up)', color='green', fontsize=8, ha='center')
ax.text(.75, -.35, '1.5 m', ha='center'); ax.text(2.75, -.35, '2.5 m', ha='center'); ax.set_xlim(-.5, 4.8); ax.set_ylim(-.8, 1.4); ax.axis('off'); ax.set_title('Free-body diagram')
ax = axs[1]; x = np.linspace(0, 4, 400); Mx = np.where(x < 1.5, -(W*2.5/1.5)*x, -W*(4-x))
ax.plot(x, Mx, c='navy', lw=2); ax.fill_between(x, Mx, alpha=.2); ax.axhline(0, c='k', lw=.5); ax.text(1.6, Mx.min()*.93, f'M_B = −{MB/1e3:.0f} N·m\n(hogging)', fontsize=9); ax.set_xlabel('x from A (m)'); ax.set_ylabel('N·m'); ax.set_title('Bending moment diagram'); ax.grid(alpha=.3)
ax = axs[2]
ax.add_patch(Rectangle((-175, 30), 350, 20, fc='#cfd8dc', ec='k'))
for x0 in (-175, -5, 165): ax.add_patch(Rectangle((x0, 0), 10, 30, fc='#cfd8dc', ec='k'))
ax.plot([-190, 190], [zc, zc], 'k--', lw=.8); ax.text(85, zc-9, f'NA, z̄ = {zc:.2f} mm from bottom', ha='center', fontsize=8, color='r')
ax.annotate('', xy=(-200, 50), xytext=(-200, 30), arrowprops=dict(arrowstyle='<->')); ax.text(-205, 40, '20', ha='right', va='center'); ax.annotate('', xy=(-200, 30), xytext=(-200, 0), arrowprops=dict(arrowstyle='<->')); ax.text(-205, 15, '30', ha='right', va='center')
ax.text(0, -10, '3 legs, 10 mm wide each', ha='center', fontsize=8); ax.text(0, 56, 'plate 350 mm wide', ha='center', fontsize=8)
ax.set_xlim(-230, 200); ax.set_ylim(-14, 62); ax.set_aspect('equal'); ax.axis('off'); ax.set_title('Cross-section (mm)')
ax = axs[3]; zz = np.linspace(0, 50, 100); sg = MB*(zz-zc)/I
ax.fill_betweenx(zz, 0, sg, where=sg > 0, color=TEN, alpha=.4); ax.fill_betweenx(zz, 0, sg, where=sg < 0, color=COM, alpha=.4); ax.plot(sg, zz, 'k'); ax.axvline(0, c='k', lw=.5)
ax.text(sg[0]+2, 1.5, f'{sg[0]:.1f} MPa', ha='left', fontsize=9); ax.text(sg[-1]-2, 48, f'+{sg[-1]:.1f} MPa', ha='right', fontsize=9, va='top')
ax.set_xlabel('σ at section B (MPa)'); ax.set_ylabel('z from bottom (mm)'); ax.set_title(f'Stress at B:  ε_max = σ/E = {sig_max/E:.2e}'); ax.grid(alpha=.3)
save(fig, 'SM-T7-Q3-diving-board.png')

# ================================================================ Q4 box beam (mm, N)
Ibox = (200*200**3-150*150**3)/12
sigD = 30.0
M4 = sigD*Ibox/75; smax = M4*100/Ibox
print('Q4 I = %.4e mm^4, M = %.4f kN m, sigma_max = %.3f MPa' % (Ibox, M4/1e6, smax))
zg = np.linspace(-100, 100, 400001); wg = np.where(np.abs(zg) <= 75, 50.0, 200.0); Ig4 = np.trapezoid(wg*zg**2, zg); print('Q4 grid check I = %.4e' % Ig4)
fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axs[0]
ax.add_patch(Rectangle((-100, -100), 200, 200, fc='#d7c4a3', ec='k')); ax.add_patch(Rectangle((-75, -75), 150, 150, fc='white', ec='k'))
ax.plot(-75, 75, 'ko'); ax.text(-82, 80, 'D', ha='right', fontsize=12); ax.axhline(0, c='k', ls='--', lw=.7); ax.text(104, 0, 'NA', va='center')
ax.annotate('', xy=(-120, 100), xytext=(-120, 75), arrowprops=dict(arrowstyle='<->')); ax.text(-125, 88, '25', ha='right', fontsize=8)
ax.annotate('', xy=(-110, 75), xytext=(-110, -75), arrowprops=dict(arrowstyle='<->')); ax.text(-114, -40, '150', ha='right', fontsize=8)
ax.set_xlim(-140, 135); ax.set_ylim(-115, 115); ax.set_aspect('equal'); ax.axis('off'); ax.set_title('Box section (mm): D at y = +75 mm')
ax = axs[1]; zz = np.linspace(-100, 100, 200); sg = -smax*zz/100        # top compression (negative)
ax.fill_betweenx(zz, 0, sg, where=sg < 0, color=COM, alpha=.4); ax.fill_betweenx(zz, 0, sg, where=sg > 0, color=TEN, alpha=.4); ax.plot(sg, zz, 'k'); ax.axvline(0, c='k', lw=.5)
ax.plot(-30, 75, 'ko'); ax.annotate('σ_D = −30 MPa', (-30, 75), xytext=(-25, 55), arrowprops=dict(arrowstyle='->')); ax.text(-smax, 102, f'−{smax:.0f} MPa (top fibre)', ha='left', fontsize=9); ax.text(smax, -108, f'+{smax:.0f} MPa (bottom)', ha='right', fontsize=9)
ax.set_xlabel('σ (MPa)'); ax.set_ylabel('y (mm)'); ax.set_title(f'Stress distribution for M = {M4/1e6:.2f} kN·m'); ax.grid(alpha=.3); ax.set_xlim(-55, 55)
save(fig, 'SM-T7-Q4-box-beam.png')

# ================================================================ Q5 plywood / pine box beam (in, psi)
Ep, Ew = 1.4e6, 1.8e6                          # pine, plywood (plywood = webs)
parts = [(-6, 6, 1.0, Ew), (-6, 6, 1.0, Ew)]     # two plywood webs each 1 in wide, 12 tall
EIw = 2*Ew*(1*12**3/12)
EIp = 2*Ep*(3.5*1.5**3/12 + 3.5*1.5*(6-0.75)**2)
EIt = EIw + EIp
Mply = 2000*EIt/(Ew*6); Mpine = 1750*EIt/(Ep*6)
print('Q5 EI_w = %.4e, EI_p = %.4e, EI = %.4e lb in^2' % (EIw, EIp, EIt))
print('Q5 M_ply = %.1f lb in, M_pine = %.1f lb in -> M_max = %.1f lb in = %.3f kip ft' % (Mply, Mpine, min(Mply, Mpine), min(Mply, Mpine)/12000))
# numerical integration check
zz = np.linspace(-6, 6, 120001)
Ewz = np.where(True, Ew, Ew)
Ig_w = 2*np.trapezoid(np.full_like(zz, 1.0)*Ew*zz**2, zz)
fl = np.abs(zz) >= 4.5
Ig_p = np.trapezoid(np.where(fl, 3.5*Ep, 0.0)*zz**2, zz)
print('Q5 grid EI = %.4e (analytic %.4e)' % (Ig_w+Ig_p, EIt))
Mm = min(Mply, Mpine); curv = Mm/EIt
fig, axs = plt.subplots(1, 3, figsize=(16, 4.6))
ax = axs[0]
ax.add_patch(Rectangle((-3.5/2-1, -6), 1, 12, fc='#e8d9b5', ec='k')); ax.add_patch(Rectangle((3.5/2, -6), 1, 12, fc='#e8d9b5', ec='k'))
ax.add_patch(Rectangle((-1.75, 4.5), 3.5, 1.5, fc='#a9835a', ec='k')); ax.add_patch(Rectangle((-1.75, -6), 3.5, 1.5, fc='#a9835a', ec='k'))
ax.axhline(0, c='k', ls='--', lw=.7); ax.text(3.1, .3, 'z (NA)', fontsize=9); ax.text(0, 5.2, 'pine', ha='center', fontsize=8, va='center'); ax.text(-2.25, 0, 'plywood', rotation=90, va='center', ha='center', fontsize=8)
ax.set_xlim(-4.5, 4.5); ax.set_ylim(-7, 7); ax.set_aspect('equal'); ax.axis('off'); ax.set_title('Box beam (in): 12 in. deep, 5.5 in. wide')
ax = axs[1]; y = np.linspace(-6, 6, 200); ax.plot(y*curv*1e3, y, 'k', lw=1.5); ax.axvline(0, c='k', lw=.5); ax.fill_betweenx(y, 0, y*curv*1e3, alpha=.25, color='gray'); ax.set_title('Strain ε = yM/ΣEI (×10⁻³), M = %.1f k·in' % (Mm/1e3), fontsize=10); ax.set_xlabel('ε (×10⁻³)'); ax.set_ylabel('y (in)'); ax.grid(alpha=.3)
ax = axs[2]
for yy0, yy1, E_, col, lab in [(-6, 6, Ew, '#c9a66b', 'plywood'), (4.5, 6, Ep, '#8d6e63', 'pine'), (-6, -4.5, Ep, '#8d6e63', None)]:
    ys = np.linspace(yy0, yy1, 50); ax.plot(E_*ys*curv, ys, c=col, lw=3, label=lab)
ax.axvline(2000, c='#c9a66b', ls=':'); ax.axvline(-2000, c='#c9a66b', ls=':'); ax.axvline(1750, c='#8d6e63', ls=':'); ax.axvline(-1750, c='#8d6e63', ls=':')
ax.set_xlabel('σ (psi)'); ax.set_ylabel('y (in)'); ax.set_title('Stress: plywood hits 2000 psi first', fontsize=10); ax.legend(); ax.grid(alpha=.3)
save(fig, 'SM-T7-Q5-box-beam.png')

# ================================================================ Q6 glued cantilever
a = 1.0
def shear_profile(rects):
    """rects: list of (z_bot, z_top, width) z downward irrelevant; returns zc, I, function tau(z)/ (F/a^2)."""
    A = sum(w*(t-b) for b, t, w in rects); zc = sum(w*(t-b)*(t+b)/2 for b, t, w in rects)/A
    I = sum(w*(t-b)**3/12 + w*(t-b)*((t+b)/2-zc)**2 for b, t, w in rects)
    def Q(z):               # first moment above height z
        q = 0
        for b, t, w in rects:
            lo = max(b, z)
            if t > lo: q += w*(t-lo)*((t+lo)/2-zc)
        return q
    def width(z):
        # width at height z (just above)
        return sum(w for b, t, w in rects if b <= z+1e-12 < t)
    return zc, I, Q, width
v1 = [(-2, -1, 2), (-1, 1, 1), (1, 2, 2)]      # flange 2a x a, web a x 2a, flange   (centre at 0)
v2 = [(-1.5, -.5, 2), (-.5, .5, 2), (.5, 1.5, 2)]
res = {}
for name, rs, zi in (('1', v1, 1.0), ('2', v2, .5)):
    zc, I, Q, width = shear_profile(rs)
    q_int = Q(zi); t_int = min(w for b, t, w in rs if (abs(t-zi) < 1e-9 or abs(b-zi) < 1e-9))
    tau_int = q_int/(I*t_int)          # per unit F / a^2
    res[name] = (I, q_int, t_int, tau_int)
    print('Q6 variant %s: I = %.4f a^4, Q = %.4f a^3, t = %.4f a, tau_int = %.5f F/a^2  -> F_max = %.4f tau a^2' % (name, I, q_int, t_int, tau_int, 1/tau_int))
print('Q6 ratio F2/F1 = %.4f' % (res['1'][3]/res['2'][3]))
fig, axs = plt.subplots(1, 4, figsize=(18, 4.6), gridspec_kw={'width_ratios': [1, 1.2, 1, 1.2]})
def draw_sec(ax, rs, title):
    for b, t, w in rs: ax.add_patch(Rectangle((-w/2, b), w, t-b, fc='#e0cfa8', ec='k'))
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-2.4, 2.4); ax.set_aspect('equal'); ax.axis('off'); ax.set_title(title); ax.axhline(0, c='b', ls='--', lw=.7)
draw_sec(axs[0], v1, 'Variant 1: I-shape'); draw_sec(axs[2], v2, 'Variant 2: stacked')
for ax, rs, name, zi in ((axs[1], v1, '1', 1.0), (axs[3], v2, '2', .5)):
    zc, I, Q, width = shear_profile(rs)
    top = max(t for b, t, w in rs); zs = np.linspace(-top+1e-4, top-1e-4, 800)
    tau = np.array([Q(z)/(I*max(width(z), 1e-9)) for z in zs]); ax.plot(tau, zs, c='navy', lw=2)
    ax.axhline(zi, c='crimson', ls='--'); ax.axhline(-zi, c='crimson', ls='--', lw=.5)
    ax.text(res[name][3]*.5, zi+.07, f'glue line: τ = {res[name][3]:.4f} F/a²', color='crimson', fontsize=9)
    ax.set_xlabel('τ (units of F/a²)'); ax.set_ylabel('z (units of a)'); ax.set_title(f'Variant {name}: τ(z) (shear stress, jumps with width)'); ax.grid(alpha=.3)
save(fig, 'SM-T7-Q6-glued-cantilever.png')

# ================================================================ Q7 steel I beam + concrete slab (N, mm)
Ec_, Es_ = 3.5e4, 2.1e5; n = Es_/Ec_; h = 400.0; M7 = 1000e6
b7 = n*0 + (Es_/Ec_)*h/3                     # E_s h /(3 E_c)
print('Q7 n = %.2f, b = %.1f mm (= %.3f h)' % (n, b7, b7/h))
# NA at interface; check zero net force
Fc = Ec_*b7*h*(h/2); Fs = Es_*(h**2/6)*h         # first moment (E-weighted): concrete above NA, steel below -> must match
print('Q7 force balance (E*Q): %.4e vs %.4e' % (Fc, Fs))
EI = Ec_*(b7*h**3/12 + b7*h*(h/2)**2) + Es_*(h**4/18 + (h**2/6)*h**2)
kap = M7/EI
sc_top = -Ec_*kap*h; ss_bot = Es_*kap*2*h
print('Q7 EI = %.4e N mm^2, kappa = %.4e 1/mm' % (EI, kap)); print('Q7 sigma_c,top = %.4f MPa, sigma_s,bottom = %.4f MPa' % (sc_top, ss_bot))
print('Q7 strains: eps_c,top = %.3e, eps_s,bot = %.3e' % (-kap*h, kap*2*h))
fig, axs = plt.subplots(1, 3, figsize=(17, 5))
ax = axs[0]; ax.add_patch(Rectangle((-b7/2, 0), b7, h, fc='#cfcfcf', ec='k'))
ax.add_patch(Rectangle((-h/4, 0), h/2, 12, fc='steelblue', ec='k')); ax.add_patch(Rectangle((-h/4, -2*h), h/2, 12, fc='steelblue', ec='k')); ax.add_patch(Rectangle((-6, -2*h), 12, 2*h, fc='steelblue', ec='k'))
ax.plot([-b7/2-20, b7/2+20], [0, 0], 'r--'); ax.text(0, -60, 'NA = slab/steel interface', color='r', ha='center', fontsize=9)
ax.annotate('', xy=(-b7/2, h+30), xytext=(b7/2, h+30), arrowprops=dict(arrowstyle='<->')); ax.text(0, h+45, f'b = {b7:.0f} mm = 2h', ha='center')
ax.text(b7/2+15, h/2, 'concrete\nE_c', fontsize=9); ax.text(h/4+20, -h, 'steel I-beam\nE_s = 6 E_c', fontsize=9)
ax.set_xlim(-b7/2-40, b7/2+200); ax.set_ylim(-2*h-40, h+110); ax.set_aspect('equal'); ax.axis('off'); ax.set_title('Composite section (h = 400 mm)')
ax = axs[1]; zz = np.linspace(-2*h, h, 300); ax.plot(-kap*zz*1e3, zz, 'k', lw=2); ax.fill_betweenx(zz, 0, -kap*zz*1e3, where=zz > 0, color=COM, alpha=.3); ax.fill_betweenx(zz, 0, -kap*zz*1e3, where=zz < 0, color=TEN, alpha=.3); ax.axvline(0, c='k', lw=.5); ax.axhline(0, c='r', ls='--', lw=.7)
ax.set_xlabel('ε (×10⁻³)'); ax.set_ylabel('z from NA (mm, up)'); ax.set_title('Strain: one straight line'); ax.grid(alpha=.3)
ax = axs[2]
zc_ = np.linspace(0, h, 80); ax.plot(-Ec_*kap*zc_, zc_, c='gray', lw=3, label='concrete'); zs_ = np.linspace(-2*h, 0, 80); ax.plot(-Es_*kap*zs_, zs_, c='steelblue', lw=3, label='steel')
ax.axvline(0, c='k', lw=.5); ax.legend(loc='center right'); ax.text(sc_top+2, h-20, f'{sc_top:.2f} MPa', ha='left', va='top'); ax.text(ss_bot-3, -2*h+25, f'+{ss_bot:.2f} MPa', ha='right')
ax.set_xlabel('σ (MPa)'); ax.set_ylabel('z from NA (mm)'); ax.set_title('Stress: kink at the interface (E jumps)'); ax.grid(alpha=.3)
save(fig, 'SM-T7-Q7-composite-beam.png')

# ================================================================ Q8 section with semicircular notch (in, ksi)
Arect = 1.6*0.8; Asemi = np.pi*0.5**2/2
yb = (Arect*0.4 - Asemi*4*0.5/(3*np.pi))/(Arect-Asemi)
Ib = 1.6*0.8**3/3 - np.pi*0.5**4/8
Ic = Ib - (Arect-Asemi)*yb**2
ctop8, cbot8 = 0.8-yb, yb
print('Q8 A = %.4f, ybar = %.4f in (from bottom), I = %.5f in^4, c_top = %.4f, c_bot = %.4f' % (Arect-Asemi, yb, Ic, ctop8, cbot8))
# grid check
yy = np.linspace(0, 0.8, 800001)
wy = np.where(yy < 0.5, 1.6-2*np.sqrt(np.maximum(0.25-yy**2, 0)), 1.6)
Ag = np.trapezoid(wy, yy); ybg = np.trapezoid(wy*yy, yy)/Ag; Ig8 = np.trapezoid(wy*(yy-ybg)**2, yy)
print('Q8 grid check: A = %.4f, ybar = %.4f, I = %.5f' % (Ag, ybg, Ig8))
# case A: tension at top (read from figure), compression at bottom
MA = min(12*Ic/ctop8, 16*Ic/cbot8); MA_t = 12*Ic/ctop8; MA_c = 16*Ic/cbot8
MB_ = min(12*Ic/cbot8, 16*Ic/ctop8); MB_t = 12*Ic/cbot8; MB_c = 16*Ic/ctop8
print('Q8 case A (top tension): M_t = %.4f, M_c = %.4f -> M = %.4f k-in' % (MA_t, MA_c, MA))
print('Q8 case B (bottom tension): M_t = %.4f, M_c = %.4f -> M = %.4f k-in' % (MB_t, MB_c, MB_))
fig, axs = plt.subplots(1, 3, figsize=(17, 4.4))
ax = axs[0]; ax.add_patch(Rectangle((-.8, 0), 1.6, .8, fc='#d9d9d9', ec='k')); ax.add_patch(Wedge((0, 0), .5, 0, 180, fc='white', ec='k')); ax.plot(0, 0, 'k.')
ax.axhline(yb, c='r', ls='--'); ax.text(0, yb+.03, f'NA: ȳ = {yb:.4f} in from bottom', ha='center', color='r', fontsize=8)
ax.annotate('', xy=(-.95, 0), xytext=(-.95, .8), arrowprops=dict(arrowstyle='<->')); ax.text(-1.0, .4, '0.8', ha='right'); ax.set_xlim(-1.2, 1.0); ax.set_ylim(-.15, .95); ax.set_aspect('equal'); ax.axis('off'); ax.set_title('Section: 1.6 × 0.8 in with R = 0.5 in notch')
def stress_plot(ax, M, top_is_tension, title):
    y = np.linspace(0, .8, 100); s = M*(y-yb)/Ic*(1 if top_is_tension else -1)
    ax.fill_betweenx(y, 0, s, where=s > 0, color=TEN, alpha=.4); ax.fill_betweenx(y, 0, s, where=s < 0, color=COM, alpha=.4); ax.plot(s, y, 'k'); ax.axvline(0, c='k', lw=.5)
    for lim in (12, -16): ax.axvline(lim, c='gray', ls=':')
    ax.text(s[0], .01, f'{s[0]:+.1f}', ha='left' if s[0] < 0 else 'right', fontsize=9); ax.text(s[-1], .79, f'{s[-1]:+.1f}', ha='right' if s[-1] > 0 else 'left', va='top', fontsize=9)
    ax.set_xlim(-22, 22); ax.set_xlabel('σ (ksi)'); ax.set_ylabel('y (in)'); ax.set_title(title); ax.grid(alpha=.3)
stress_plot(axs[1], MA, True, f'Fig. 8 as drawn (tension on top): M = {MA:.3f} k·in\ncompression at the notch side governs')
stress_plot(axs[2], MB_, False, f'If M were reversed (tension at notch): M = {MB_:.3f} k·in\ntension at notch governs')
save(fig, 'SM-T7-Q8-notched-section.png')
print('done')

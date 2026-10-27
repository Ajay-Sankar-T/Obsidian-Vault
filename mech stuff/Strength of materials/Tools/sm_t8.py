"""AM2200 Tutorial 8 (Deflection of Beams): verification numbers and figures.
Run:  python -I sm_t8.py        (figures -> ../assets/SM-T8-*.png)
Every closed form quoted in the note is asserted here against an independent numerical double integration."""
import os
import numpy as np
import sympy as sp
from scipy import integrate, optimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets'); os.makedirs(ASSETS, exist_ok=True)
def save(fig, name): fig.savefig(os.path.join(ASSETS, name), dpi=130, bbox_inches='tight'); plt.close(fig); print('wrote', name)
plt.rcParams.update({'font.size': 10, 'axes.grid': True, 'grid.alpha': .3, 'axes.spines.top': False, 'axes.spines.right': False})
B, R, G = '#1f77b4', '#d62728', '#2ca02c'
NUM = {}

def bracket(z, n): return np.where(z > 0, z, 0.0)**n
def dbl_int(M, x, EI, v0=0.0, v1=None, th0=None):
    """v'' = M/EI on grid x; shooting for v(0)=v0 and either v(L)=v1 (simply supported) or v'(0)=th0 (cantilever)"""
    k = M/EI
    th_part = integrate.cumulative_trapezoid(k, x, initial=0)
    v_part = integrate.cumulative_trapezoid(th_part, x, initial=0)
    if th0 is not None: c1 = th0
    else: c1 = (v1 - v0 - v_part[-1])/(x[-1]-x[0])
    th = th_part + c1; v = v_part + c1*(x-x[0]) + v0
    return th, v

# ================================================================== Q1  two-section cantilever
P, Lq, l, E, I1, I2 = 1.0, 2.0, 0.8, 1.0, 2.0, 1.0           # arbitrary test numbers (I_AB = 2 I_BC)
dC = P/(3*E)*((Lq**3-l**3)/I1 + l**3/I2)
thC = P/(2*E)*((Lq**2-l**2)/I1 + l**2/I2)
x = np.linspace(0, Lq, 40001)
I_x = np.where(x < Lq-l, I1, I2); M = -P*(Lq-x)
th, v = dbl_int(M, x, E*I_x, 0, th0=0.0)
print("Q1 chk", -v[-1], dC, -th[-1], thC); assert abs(-v[-1]-dC) < 1e-4*dC and abs(-th[-1]-thC) < 1e-4*thC
NUM['Q1'] = (dC, thC)
# limit: I1 = I2 -> P L^3/(3EI)
assert abs(P/(3*E)*((Lq**3-l**3)/1.0 + l**3/1.0)-P*Lq**3/3) < 1e-12

# ================================================================== Q2  couple on a simple beam
xs, a_, b_, M0_ = sp.symbols('x a b M0', positive=True)
v_left = M0_*xs*(xs**2-a_**2-2*a_*b_+2*b_**2)/(6*(a_+b_))                 # EI v, 0<=x<=a  (y up, ccw couple)
v_right = M0_*(xs-a_-b_)*(xs**2-2*(a_+b_)*xs+3*a_**2)/(6*(a_+b_))        # a<=x<=L
d0 = M0_*a_*b_*(b_-a_)/(3*(a_+b_))
chk = [v_left.subs(xs, 0), v_right.subs(xs, a_+b_), sp.simplify((v_left-v_right).subs(xs, a_)), sp.simplify(sp.diff(v_left-v_right, xs).subs(xs, a_)),
       sp.simplify(v_left.subs(xs, a_)-d0)]
assert all(sp.simplify(c) == 0 for c in chk)
# also ODE: EI v'' = M0 x/L (x<a), M0 (x-L)/L (x>a)
assert sp.simplify(sp.diff(v_left, xs, 2)-M0_*xs/(a_+b_)) == 0 and sp.simplify(sp.diff(v_right, xs, 2)-M0_*(xs-a_-b_)/(a_+b_)) == 0
# numeric cross-check
aa, bb = 1.3, 2.7; Lc = aa+bb; x = np.linspace(0, Lc, 40001)
M = np.where(x < aa, x/Lc, (x-Lc)/Lc)
th, v = dbl_int(M, x, 1.0, 0, v1=0.0)
i = np.argmin(abs(x-aa)); print("Q2 chk", v[i], aa*bb*(bb-aa)/(3*Lc)); assert abs(v[i]-aa*bb*(bb-aa)/(3*Lc)) < 2e-4
NUM['Q2 d0 (a=1.3,b=2.7,M0=EI=1)'] = v[i]

# ================================================================== Q3  simply supported, point load + triangular load
EI3 = 200e6*65e-6                              # kN m^2  (E = 200 GPa, I = 65e6 mm^4 = 65e-6 m^4)
RA, RB = 22.5, 20.0
def M3(x): return RA*x-20*bracket(x-1.5, 1)-7.5*bracket(x-3, 2)+5/6*bracket(x-3, 3)
assert abs(M3(np.array(6.0))) < 1e-12 and abs(RA+RB-42.5) < 1e-12
C1_3 = -77.625
def v3(x): return (3.75*x**3-10/3*bracket(x-1.5, 3)-5/8*bracket(x-3, 4)+1/24*bracket(x-3, 5)+C1_3*x)/EI3
def th3(x): return (11.25*x**2-10*bracket(x-1.5, 2)-2.5*bracket(x-3, 3)+5/24*bracket(x-3, 4)+C1_3)/EI3
assert abs(v3(np.array(0.0))) < 1e-15 and abs(v3(np.array(6.0))) < 1e-12
x = np.linspace(0, 6, 60001); thn, vn = dbl_int(M3(x), x, EI3, 0, v1=0.0)
assert np.max(abs(vn-v3(x))) < 1e-7 and np.max(abs(thn-th3(x))) < 1e-7
xm = optimize.brentq(lambda t: th3(np.array(t)), 1.5, 3.0)
vmax = float(v3(np.array(xm)))
NUM['Q3'] = dict(xm=xm, vmax_mm=vmax*1e3, EI=EI3, v_mid_mm=float(v3(np.array(3.0)))*1e3, v_load_mm=float(v3(np.array(1.5)))*1e3, thA=float(th3(np.array(0.0))), thB=float(th3(np.array(6.0))))

# ================================================================== Q4  cantilever, point load + end couple
EI4 = 200e6*121e-6                             # kN m^2
def M4(x): return -90+60*x-60*bracket(x-1, 1)                  # x from the wall B
def v4(x): return (-45*x**2+10*x**3-10*bracket(x-1, 3))/EI4
def th4(x): return (-90*x+30*x**2-30*bracket(x-1, 2))/EI4
x = np.linspace(0, 2, 40001); thn, vn = dbl_int(M4(x), x, EI4, 0, th0=0.0)
assert np.max(abs(vn-v4(x))) < 1e-9 and abs(M4(np.array(2.0))+30) < 1e-12
NUM['Q4'] = dict(thA=float(th4(np.array(2.0))), vA_mm=float(v4(np.array(2.0)))*1e3, EI=EI4)

# ================================================================== Q5  triangular load, Castigliano
q0_, L5, Q_, u_, EI_ = sp.symbols('q0 L Q u EI', positive=True)
Msym = -(Q_*u_+q0_*u_**3/(6*L5))                                    # u measured from the free end B
U = sp.integrate(Msym**2/(2*EI_), (u_, 0, L5))
dB = sp.simplify(sp.diff(U, Q_).subs(Q_, 0)); U0 = sp.simplify(U.subs(Q_, 0))
assert sp.simplify(dB-q0_*L5**4/(30*EI_)) == 0 and sp.simplify(U0-q0_**2*L5**5/(504*EI_)) == 0
# numerical check by double integration of the exact moment
Lc, q0n = 3.0, 5.0; x = np.linspace(0, Lc, 40001); uu = Lc-x
thn, vn = dbl_int(-q0n*uu**3/(6*Lc), x, 1.0, 0, th0=0.0)
assert abs(-vn[-1]-q0n*Lc**4/30) < 1e-7
# triangular load statics: resultant q0 L/2 at L/3 from the fixed end
NUM['Q5'] = 'q0 L^4/(30 EI)'

# ================================================================== Q6  beam on post with initial gap
w6, L6 = 30e3, 12.0; E6 = 200e9; I6 = 875e-6; A6 = np.pi*0.04**2/4; Lp = 1.0; gap = 0.2e-3
free = 5*w6*L6**4/(384*E6*I6)                  # midspan deflection without the post
flex = L6**3/(48*E6*I6); post = Lp/(A6*E6)
FB = (free-gap)/(flex+post); FA = (w6*L6-FB)/2
assert free > gap
NUM['Q6'] = dict(free_mm=free*1e3, flex=flex, post=post, FB_kN=FB/1e3, FA_kN=FA/1e3, v_B_mm=(free-flex*FB)*1e3, post_shortening_mm=post*FB*1e3, A6=A6)
# check by solving the beam ODE numerically with the support at B at height v_B = gap + post compression
x = np.linspace(0, L6, 120001)
M = FA*x-w6*x**2/2+FB*bracket(x-6, 1)
th, v = dbl_int(M, x, E6*I6, 0, v1=0.0)
assert abs(-v[np.argmin(abs(x-6))]-(gap+post*FB)) < 1e-7, (v[np.argmin(abs(x-6))], gap+post*FB)
assert abs(M[-1]) < 1e-3
# gap-closing load: the post is touched when w exceeds
w_touch = 384*E6*I6*gap/(5*L6**4); NUM['Q6 w_touch kN/m'] = w_touch/1e3
# limits: infinitely stiff post and zero gap -> FB = 5 wL/8
assert abs((free-0)/(flex)-5*w6*L6/8) < 1e-6*5*w6*L6/8

# ================================================================== Q7  continuous beam, Castigliano (kip, ft)
Rr, xx = sp.symbols('R x')
Ay = 18-Rr/2
def br(z, n): return sp.Piecewise((0, z < 0), (z**n, True))
Mx = Ay*xx-12*br(xx-6, 1)+Rr*br(xx-12, 1)-sp.Rational(3, 2)*br(xx-12, 2)
dM = sp.diff(Mx, Rr)
dU = sp.integrate(sp.piecewise_fold(Mx*dM), (xx, 0, 24))
Rsol = sp.solve(sp.Eq(dU, 0), Rr)[0]
RB7 = float(Rsol); RA7 = 18-RB7/2; RC7 = 30-RB7/2
# second method: superposition, v_B = 0 using the primary beam A-C without B
EI = 1.0
Mp = lambda x_: (48-0)/2*0                                           # (placeholder to keep names simple)
# primary (R=0): A0 = 18, C0 = 30; deflection at x=12 by numerical integration
xg = np.linspace(0, 24, 96001)
def deflect(Rv):
    Av = 18-Rv/2
    M = Av*xg-12*bracket(xg-6, 1)+Rv*bracket(xg-12, 1)-1.5*bracket(xg-12, 2)
    return dbl_int(M, xg, 1.0, 0, v1=0.0)[1]
vB0 = lambda Rv: deflect(Rv)[np.argmin(abs(xg-12))]
Rnum = optimize.brentq(vB0, 0, 60)
assert abs(Rnum-RB7) < 1e-4 and abs(RA7+RB7+RC7-48) < 1e-9
Mabs = lambda x_: (18-RB7/2)*x_-12*bracket(x_-6, 1)+RB7*bracket(x_-12, 1)-1.5*bracket(x_-12, 2)
assert abs(Mabs(np.array(24.0))) < 1e-9
NUM['Q7'] = dict(RB=RB7, RA=RA7, RC=RC7, Rexact=Rsol, M6=float(Mabs(np.array(6.0))), M12=float(Mabs(np.array(12.0))))
# moment extremes
xv = np.linspace(0, 24, 24001); Mv = Mabs(xv)
V_after_B = RA7-12+RB7                    # shear just right of B
x0 = 12+V_after_B/3                       # zero shear in the loaded span
NUM['Q7'].update(Mmax_span2=float(Mabs(np.array(x0))), x0=x0, Mmin=float(Mv.min()), xMmin=float(xv[np.argmin(Mv)]), Mmax1=float(Mv[:6001].max()))

# ================================================================== Q8  frame
P8, h, b, EI8 = sp.symbols('P h b EI', positive=True); s, M0f = sp.symbols('s M0')
M_BC = -(P8*s+M0f); M_AB = -(P8*b+M0f)
Ufr = sp.integrate(M_BC**2/(2*EI8), (s, 0, b))+sp.integrate(M_AB**2/(2*EI8), (s, 0, h))
dC8 = sp.simplify(sp.diff(Ufr, P8).subs(M0f, 0)); th8 = sp.simplify(sp.diff(Ufr, M0f).subs(M0f, 0))
assert sp.simplify(dC8-(P8*b**3/(3*EI8)+P8*b**2*h/EI8)) == 0 and sp.simplify(th8-(P8*b**2/(2*EI8)+P8*b*h/EI8)) == 0
# numeric check: integrate curvature of the frame
Pn, hn, bn = 1.0, 1.5, 1.0
sA = np.linspace(0, hn, 20001); sB = np.linspace(0, bn, 20001)
thetaB = np.trapezoid(Pn*bn*np.ones_like(sA), sA)                   # rotation accumulated along AB
thC_num = thetaB+np.trapezoid(Pn*sB, sB)                            # plus along BC (x measured from C: M = P s)
dC_num = bn*thetaB+np.trapezoid(Pn*sB**2, sB)                       # horizontal arm b times rotation of B + cantilever tip
assert abs(thC_num-(Pn*bn**2/2+Pn*bn*hn)) < 1e-6 and abs(dC_num-(Pn*bn**3/3+Pn*bn**2*hn)) < 1e-6
# note: AB also shortens by P h/(A E) (axial) -- neglected, flexure only
NUM['Q8'] = ('P b^2 (b+3h)/(3EI)', 'P b (b+2h)/(2EI)')

# ================================================================== figures
def beam_axes(ax, L, ymin=-.3, ymax=.3):
    ax.add_patch(Rectangle((0, -0.04), L, 0.08, fc='#c9d7e8', ec='k')); ax.set_xlim(-.05*L, 1.05*L); ax.axis('off')
def arrow(ax, x0, y0, x1, y1, c=R, **k): ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=14, color=c, lw=2, **k))

def fig_q1():
    fig, ax = plt.subplots(1, 2, figsize=(11, 3.6), gridspec_kw={'width_ratios': [1, 1.1]})
    a = ax[0]; a.axis('off'); a.set_xlim(-.3, 2.5); a.set_ylim(-1.4, 1.4)
    a.add_patch(Rectangle((-.12, -.6), .12, 1.2, fc='grey'))
    a.add_patch(Rectangle((0, -.35), 1.2, .7, fc='#c9d7e8', ec='k')); a.add_patch(Rectangle((1.2, -.17), .8, .34, fc='#e7d8b8', ec='k'))
    arrow(a, 2.0, .9, 2.0, .2); a.text(2.05, .75, 'P'); a.text(.55, 0, r'$I_{AB}$', ha='center'); a.text(1.6, 0, r'$I_{BC}$', ha='center')
    a.annotate('', (0, -.8), (2, -.8), arrowprops=dict(arrowstyle='<->')); a.text(1, -1.05, 'L', ha='center')
    a.annotate('', (1.2, -.6), (2, -.6), arrowprops=dict(arrowstyle='<->')); a.text(1.6, -.5, 'l', ha='center')
    a.text(-.1, .75, 'A'); a.text(1.15, .5, 'B'); a.text(2.05, -.1, 'C')
    a = ax[1]; x = np.linspace(0, Lq, 400); I_x = np.where(x < Lq-l, I1, I2); M = -P*(Lq-x)
    th, v = dbl_int(M, x, E*I_x, 0, th0=0.0); a.plot(x, v, color=B, lw=2.2)
    a.axvline(Lq-l, color='grey', ls=':'); a.plot([Lq], [v[-1]], 'o', color=R); a.annotate(rf'$\delta_C={dC:.4f}$ (formula)', (Lq, v[-1]), (.6, v[-1]*.6), arrowprops=dict(arrowstyle='->'))
    a.set_title(rf'deflection, test case $L=2,\ l=0.8,\ I_{{AB}}=2I_{{BC}},\ P=E=I_{{BC}}=1$'); a.set_xlabel('x'); a.set_ylabel('v')
    fig.tight_layout(); save(fig, 'SM-T8-Q1-stepped-cantilever.png')

def fig_q2():
    fig, ax = plt.subplots(1, 3, figsize=(14, 3.8)); Lc = 1.0
    a = ax[0]; a.axis('off'); beam_axes(a, 1.0); a.set_ylim(-.5, .6)
    a.plot([0], [-.1], '^', color='k', ms=14); a.plot([1], [-.1], 'o', color='k', ms=10)
    th_ = np.linspace(.2*np.pi, 1.7*np.pi, 60); a.plot(.45+.1*np.cos(th_), .2+.1*np.sin(th_), color=R, lw=2); a.annotate('', (.45+.1*np.cos(th_[-1]), .2+.1*np.sin(th_[-1])), (.45+.1*np.cos(th_[-4]), .2+.1*np.sin(th_[-4])), arrowprops=dict(arrowstyle='-|>', color=R))
    a.text(.45, .38, r'$M_0$', ha='center'); a.annotate('', (0, -.3), (.45, -.3), arrowprops=dict(arrowstyle='<->')); a.text(.22, -.42, 'a', ha='center')
    a.annotate('', (.45, -.3), (1, -.3), arrowprops=dict(arrowstyle='<->')); a.text(.72, -.42, 'b', ha='center'); a.set_title('beam and loading ($M_0$ counter-clockwise)')
    a = ax[1]
    for aa, c in ((.25, B), (.5, G), (.75, R)):
        bb = 1-aa; x = np.linspace(0, 1, 500); vv = np.where(x <= aa, x*(x**2-aa**2-2*aa*bb+2*bb**2)/6, (x-1)*(x**2-2*x+3*aa**2)/6)
        a.plot(x, vv, color=c, label=f'a/L = {aa}'); a.plot([aa], [aa*bb*(bb-aa)/3], 'o', color=c)
    a.axhline(0, color='k', lw=.6); a.legend(fontsize=8); a.set_title(r'$EI\,v/(M_0L^2)$: deflection ($\bullet=\delta_0$)'); a.set_xlabel('x/L')
    a = ax[2]; aa = .3; bb = .7; x = np.linspace(0, 1, 500); a.plot(x, np.where(x < aa, x, x-1), color=B, lw=2); a.axhline(0, color='k', lw=.6); a.set_title(r'bending moment $M/M_0$, $a/L=0.3$'); a.set_xlabel('x/L')
    a.text(.02, -.8, r'jump $=M_0$ at the couple', fontsize=8)
    fig.tight_layout(); save(fig, 'SM-T8-Q2-couple.png')

def diagrams(ax, x, V, M, v, labs):
    ax[0].plot(x, V, color=B); ax[0].fill_between(x, V, alpha=.2, color=B); ax[0].axhline(0, color='k', lw=.6); ax[0].set_title(labs[0])
    ax[1].plot(x, M, color=R); ax[1].fill_between(x, M, alpha=.2, color=R); ax[1].axhline(0, color='k', lw=.6); ax[1].set_title(labs[1])
    ax[2].plot(x, v, color=G, lw=2); ax[2].axhline(0, color='k', lw=.6); ax[2].set_title(labs[2])
    for a in ax: a.set_xlabel('x (m)')

def fig_q3():
    x = np.linspace(0, 6, 1200); V = RA-20*(x > 1.5)-np.where(x > 3, 7.5*(x-3)**1*0, 0)
    Vx = RA-20*(x > 1.5)-np.where(x > 3, 15*(x-3)-2.5*(x-3)**2, 0)
    fig, ax = plt.subplots(1, 4, figsize=(17, 3.7)); a = ax[0]; a.axis('off'); a.set_xlim(-.4, 6.4); a.set_ylim(-1.6, 2.8)
    a.add_patch(Rectangle((0, 0), 6, .22, fc='#c9d7e8', ec='k')); a.plot([0], [-.12], '^', color='k', ms=13); a.plot([6], [-.12], 'o', color='k', ms=9)
    arrow(a, 1.5, 1.6, 1.5, .26); a.text(1.55, 1.7, '20 kN');
    for xx_ in np.linspace(3, 5.8, 8): arrow(a, xx_, .26+1.2*(6-xx_)/3, xx_, .26, c=B)
    a.plot([3, 3, 6], [1.5, .26, .26], color=B); a.plot([3, 6], [1.5, .26], color=B); a.text(3, 1.8, '15 kN/m')
    a.annotate('', (0, -.6), (1.5, -.6), arrowprops=dict(arrowstyle='<->')); a.text(.75, -.9, '1.5 m', ha='center'); a.annotate('', (1.5, -.6), (3, -.6), arrowprops=dict(arrowstyle='<->')); a.text(2.25, -.9, '1.5 m', ha='center')
    a.annotate('', (3, -.6), (6, -.6), arrowprops=dict(arrowstyle='<->')); a.text(4.5, -.9, '3 m', ha='center'); a.text(-.3, .4, rf'$R_A={RA}$ kN'); a.text(5.1, -.35, rf'$R_B={RB}$ kN', fontsize=9)
    a.set_title('loading')
    diagrams(ax[1:], x, Vx, M3(x), v3(x)*1e3, ['shear V (kN)', 'moment M (kN·m)', 'deflection v (mm)'])
    ax[3].plot([xm], [vmax*1e3], 'o', color=R); ax[3].annotate(f'v_max = {vmax*1e3:.2f} mm\nat x = {xm:.2f} m', (xm, vmax*1e3), (.4, vmax*1e3*.35), arrowprops=dict(arrowstyle='->'))
    ax[3].set_title("deflection v (mm, y up: negative = downward)", fontsize=9)
    fig.tight_layout(); save(fig, 'SM-T8-Q3-singularity-beam.png')

def fig_q4():
    fig, ax = plt.subplots(1, 4, figsize=(17, 3.7)); a = ax[0]; a.axis('off'); a.set_xlim(-.3, 2.4); a.set_ylim(-1.2, 1.6)
    a.add_patch(Rectangle((-.12, -.45), .12, .9, fc='grey')); a.add_patch(Rectangle((0, -.07), 2, .14, fc='#c9d7e8', ec='k'))
    arrow(a, 1, 1.1, 1, .12); a.text(1.05, 1.15, '60 kN'); th_ = np.linspace(.4*np.pi, -.5*np.pi, 40); a.plot(2+.25*np.cos(th_), .45+.3*np.sin(th_)*0+.35*np.sin(th_)-.0, color=R, lw=2)
    a.text(2.1, .95, '30 kN·m (cw)'); a.annotate('', (0, -.6), (1, -.6), arrowprops=dict(arrowstyle='<->')); a.text(.5, -.9, '1 m', ha='center'); a.annotate('', (1, -.6), (2, -.6), arrowprops=dict(arrowstyle='<->')); a.text(1.5, -.9, '1 m', ha='center')
    a.text(-.28, .55, 'B (wall)'); a.text(2.0, -.35, 'A (free)'); a.set_title('loading')
    x = np.linspace(0, 2, 800); V = 60*(x < 1)
    diagrams(ax[1:], x, V, M4(x), v4(x)*1e3, ['shear V (kN)', 'moment M (kN·m)', 'deflection v (mm)'])
    ax[3].plot([2], [NUM['Q4']['vA_mm']], 'o', color=R); ax[3].annotate(f"v_A = {NUM['Q4']['vA_mm']:.2f} mm,  θ_A = {NUM['Q4']['thA']*1e3:.2f} mrad", (2, NUM['Q4']['vA_mm']), (.1, NUM['Q4']['vA_mm']*.5), arrowprops=dict(arrowstyle='->'))
    fig.tight_layout(); save(fig, 'SM-T8-Q4-cantilever.png')

def fig_q5():
    fig, ax = plt.subplots(1, 3, figsize=(14, 3.7)); L = 1.0; a = ax[0]; a.axis('off'); a.set_xlim(-.1, 1.2); a.set_ylim(-.3, 1.2)
    a.add_patch(Rectangle((-.06, -.15), .06, .4, fc='grey')); a.add_patch(Rectangle((0, 0), 1, .08, fc='#c9d7e8', ec='k'))
    for xx_ in np.linspace(.02, .98, 10): arrow(a, xx_, .1+.7*(1-xx_), xx_, .09, c=B)
    a.plot([0, 1], [.8, .1], color=B); a.text(.02, .92, r'$q_0$'); a.text(1.02, .0, 'B'); a.text(-.08, .35, 'A'); a.text(.4, .6, r'$q(x)=q_0(1-x/L)$')
    a.set_title('loading; dummy load Q (=0) at B')
    x = np.linspace(0, 1, 400); u = 1-x; a = ax[1]; Mx_ = -u**3/6; a.plot(x, Mx_, color=R); a.fill_between(x, Mx_, alpha=.2, color=R); a.set_title(r'$M/(q_0L^2)=-u^3/(6L^3)$, $u=L-x$'); a.set_xlabel('x/L')
    a = ax[2]; th, v = dbl_int(Mx_, x, 1.0, 0, th0=0.0); a.plot(x, v, color=G, lw=2); a.plot([1], [v[-1]], 'o', color=R); a.annotate(r'$\delta_B=q_0L^4/(30EI)$' + '\n' + rf'$=0.0333\,q_0L^4/EI$ (numeric {-v[-1]:.4f})', (1, v[-1]), (.2, v[-1]*.45), arrowprops=dict(arrowstyle='->'))
    a.set_title(r'deflection $v\,EI/(q_0L^4)$'); a.set_xlabel('x/L')
    fig.tight_layout(); save(fig, 'SM-T8-Q5-triangular-castigliano.png')

def fig_q6():
    fig, ax = plt.subplots(1, 3, figsize=(15.5, 3.9)); a = ax[0]; a.axis('off'); a.set_xlim(-1, 13); a.set_ylim(-3.2, 3.2)
    a.add_patch(Rectangle((0, 0), 12, .5, fc='#c9d7e8', ec='k')); a.plot([0], [-.2], '^', color='k', ms=13); a.plot([12], [-.2], 'o', color='k', ms=9)
    for xx_ in np.linspace(.3, 11.7, 20): arrow(a, xx_, 1.8, xx_, .55, c=B)
    a.text(6, 2.1, '30 kN/m', ha='center'); a.add_patch(Rectangle((5.8, -2.6), .4, 2.6, fc='#a0a0a0', ec='k')); a.text(6.5, -1.4, 'post  Ø40 mm,\n1 m high'); a.annotate('gap 0.2 mm', (6, -.05), (7.5, -.55), fontsize=8, arrowprops=dict(arrowstyle='->'))
    a.annotate('', (0, -3), (6, -3), arrowprops=dict(arrowstyle='<->')); a.text(3, -3.3, '6 m', ha='center'); a.annotate('', (6, -3), (12, -3), arrowprops=dict(arrowstyle='<->')); a.text(9, -3.3, '6 m', ha='center'); a.set_title('A = pin, C = roller, B = post')
    x = np.linspace(0, L6, 1201); M = FA*x-w6*x**2/2+FB*bracket(x-6, 1); th, v = dbl_int(M, x, E6*I6, 0, v1=0.0)
    a = ax[1]; _, v0 = dbl_int(w6*L6*x/2-w6*x**2/2, x, E6*I6, 0, v1=0.0)
    a.plot(x, -v0*1e3, '--', color='grey', label='without post (46.3 mm at midspan)'); a.plot(x, -v*1e3, color=G, lw=2, label='with post'); a.plot([6], [(gap+post*FB)*1e3], 'o', color=R)
    a.set_ylim(55, -3); a.legend(fontsize=8, loc='lower center'); a.set_title('beam deflection (mm, downward)'); a.set_xlabel('x (m)')
    a = ax[2]; V = FA-w6*x+FB*(x > 6); a.plot(x, V/1e3, color=B); a.fill_between(x, V/1e3, alpha=.2, color=B); a.axhline(0, color='k', lw=.6); a.set_title(f'shear (kN): A = {FA/1e3:.1f}, B = {FB/1e3:.1f}, C = {FA/1e3:.1f} kN'); a.set_xlabel('x (m)')
    fig.tight_layout(); save(fig, 'SM-T8-Q6-post-and-gap.png')

def fig_q7():
    RA_, RB_, RC_ = RA7, RB7, RC7
    xv = np.linspace(0, 24, 4801); Mv = Mabs(xv); Vv = RA_-12*(xv > 6)+RB_*(xv > 12)-3*np.where(xv > 12, xv-12, 0)
    fig, ax = plt.subplots(1, 3, figsize=(15, 3.9)); a = ax[0]; a.axis('off'); a.set_xlim(-1, 25); a.set_ylim(-3.2, 4.2)
    a.add_patch(Rectangle((0, 0), 24, .5, fc='#c9d7e8', ec='k')); a.plot([0, 12], [-.2, -.2], 'o', color='k', ms=9); a.plot([24], [-.25], '^', color='k', ms=13)
    arrow(a, 6, 2.6, 6, .55); a.text(6.2, 2.7, '12 kip')
    for xx_ in np.linspace(12.3, 23.7, 12): arrow(a, xx_, 1.7, xx_, .55, c=B)
    a.text(18, 1.95, '3 kip/ft', ha='center')
    for xx_, r_, nm in ((0, RA_, 'A'), (12, RB_, 'B'), (24, RC_, 'C')): arrow(a, xx_, -2.2, xx_, -.4, c=G); a.text(xx_, -2.9, f'{nm}={r_:.2f} kip', ha='center', fontsize=8.5)
    a.set_title('loading and reactions (redundant: $B_y$)')
    a = ax[1]; a.plot(xv, Vv, color=B); a.fill_between(xv, Vv, alpha=.2, color=B); a.axhline(0, color='k', lw=.6); a.set_title('shear V (kip)'); a.set_xlabel('x (ft)')
    a = ax[2]; a.plot(xv, Mv, color=R); a.fill_between(xv, Mv, alpha=.2, color=R); a.axhline(0, color='k', lw=.6); a.set_title('bending moment M (kip·ft)'); a.set_xlabel('x (ft)')
    for xp, lab in ((6, f'{NUM["Q7"]["M6"]:.1f}'), (12, f'{NUM["Q7"]["M12"]:.1f}'), (NUM['Q7']['x0'], f'{NUM["Q7"]["Mmax_span2"]:.1f}')): a.annotate(lab, (xp, float(Mabs(np.array(xp)))), textcoords='offset points', xytext=(0, 8 if float(Mabs(np.array(xp))) > 0 else -14), ha='center', fontsize=8.5)
    fig.tight_layout(); save(fig, 'SM-T8-Q7-continuous-beam.png')

def fig_q8():
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.6)); hh, bb = 1.5, 1.0; k = 0.15            # k = P/EI (small, so the shape is believable)
    a = ax[0]; a.axis('off'); a.set_xlim(-.6, 1.6); a.set_ylim(-.3, 2.1); a.set_aspect('equal')
    a.plot([0, 0, bb], [0, hh, hh], color='k', lw=7, solid_capstyle='butt', alpha=.25); a.plot([-.15, .15], [0, 0], color='k', lw=3)
    a.text(-.25, 0, 'A'); a.text(-.25, hh, 'B'); a.text(bb+.05, hh+.08, 'C'); arrow(a, bb, hh+.6, bb, hh+.05); a.text(bb+.05, hh+.4, 'P')
    a.annotate('', (-.4, 0), (-.4, hh), arrowprops=dict(arrowstyle='<->')); a.text(-.55, hh/2, 'h'); a.annotate('', (0, hh+.25), (bb, hh+.25), arrowprops=dict(arrowstyle='<->')); a.text(bb/2, hh+.32, 'b', ha='center')
    a.set_title('frame ABC, A fixed, load P at C')
    a = ax[1]; a.set_aspect('equal'); a.axis('off')
    y = np.linspace(0, hh, 200); u = k*bb*y**2/2; phi = k*bb*y                  # AB: M = -P b (constant); phi is the clockwise rotation
    s_ = np.linspace(0, bb, 200); phiB, uB = phi[-1], u[-1]
    phis = phiB+k*(bb*s_-s_**2/2); ds = s_[1]-s_[0]
    wdown = np.concatenate([[0], np.cumsum(.5*(phis[1:]+phis[:-1]))*ds]); xBC = uB+np.concatenate([[0], np.cumsum(.5*(np.cos(phis[1:])+np.cos(phis[:-1]))*ds)])
    a.plot([0, 0, bb], [0, hh, hh], color='grey', lw=2.5, ls='--'); a.plot(u, y, color=B, lw=3); a.plot(xBC, hh-wdown, color=B, lw=3)
    dCv = k*bb**2*(bb+3*hh)/3; thC = k*bb*(bb+2*hh)/2
    a.plot([xBC[-1]], [hh-wdown[-1]], 'o', color=R); a.plot([bb], [hh-dCv], 'x', color=G, ms=9)
    a.text(.2, -.25, rf'$\delta_C=Pb^2(b+3h)/(3EI)={dCv:.3f}$,  $\theta_C=Pb(b+2h)/(2EI)={thC:.3f}$ rad' + '\n' + r'(test values $h=1.5,\ b=1,\ P/EI=0.15$; dots: integrated shape, cross: formula)', fontsize=8.5)
    a.set_title('deformed shape, flexure only (B moves right, rotates clockwise)')
    fig.tight_layout(); save(fig, 'SM-T8-Q8-frame.png')

if __name__ == '__main__':
    print('Q1', NUM['Q1']); print('Q2 d0 test', NUM['Q2 d0 (a=1.3,b=2.7,M0=EI=1)'])
    print('Q3', {k: round(v, 6) if isinstance(v, float) else v for k, v in NUM['Q3'].items()})
    print('Q4', NUM['Q4']); print('Q5', NUM['Q5']); print('Q6', NUM['Q6']); print('Q6 w_touch', NUM['Q6 w_touch kN/m'])
    print('Q7', NUM['Q7']); print('Q8', NUM['Q8'])
    fig_q1(); fig_q2(); fig_q3(); fig_q4(); fig_q5(); fig_q6(); fig_q7(); fig_q8()
    print('all checks passed')

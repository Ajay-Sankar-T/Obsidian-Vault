"""AM2200 Tutorial 6 (Torsional Members): verification numbers and figures.
Run:  python sm_t6.py        (figures -> ../assets/SM-T6-*.png)
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')
os.makedirs(ASSETS, exist_ok=True)
def save(fig, name): fig.savefig(os.path.join(ASSETS, name), dpi=130, bbox_inches='tight'); plt.close(fig)

# ======================================================== Q1 stepped shaft (kip, in, ksi)
G = 11.6e3; L = 25.0
d = {'AB': 3.5, 'BC': 2.75, 'CD': 2.5}
T = {'AB': 12.5+9.8+9.2, 'BC': 9.8+9.2, 'CD': 9.2}                 # internal torques, same sense
J = {k: np.pi*v**4/32 for k, v in d.items()}
tau = {k: 16*T[k]/(np.pi*d[k]**3) for k in d}
dphi = {k: T[k]*L/(G*J[k]) for k in d}
phiB = dphi['AB']; phiC = phiB+dphi['BC']; phiD = phiC+dphi['CD']
U = sum(T[k]**2*L/(2*G*J[k]) for k in d)
W = 0.5*(12.5*phiB+9.8*phiC+9.2*phiD)
print('Q1 J', {k: round(v, 4) for k, v in J.items()}, 'tau', {k: round(v, 3) for k, v in tau.items()})
print('Q1 phiB,phiC,phiD (rad)', phiB, phiC, phiD, ' deg', np.degrees(phiD), ' U', U, ' W', W)
# Castigliano: phi_D = dU/dT_D with T_CD = TD, T_BC = TD+9.8, T_AB = TD+9.8+12.5
def U_of(TD):
    Ts = {'CD': TD, 'BC': TD+9.8, 'AB': TD+9.8+12.5}
    return sum(Ts[k]**2*L/(2*G*J[k]) for k in d)
h = 1e-6; print('Q1 Castigliano dU/dTD =', (U_of(9.2+h)-U_of(9.2-h))/(2*h))
# figure
x = np.array([0, 25, 50, 75]); Tp = [T['AB'], T['BC'], T['CD']]
fig, axs = plt.subplots(1, 4, figsize=(18, 4))
ax = axs[0]
for i, (k, c) in enumerate(zip(['AB', 'BC', 'CD'], ['#1f77b4', '#ff7f0e', '#2ca02c'])):
    r = d[k]/2; ax.add_patch(plt.Rectangle((25*i, -r), 25, 2*r, fc=c, alpha=.35, ec='k'))
    ax.text(25*i+12.5, 0, f'{k}\nd={d[k]} in', ha='center', va='center', fontsize=8)
for xx, lab in [(25, '12.5'), (50, '9.8'), (75, '9.2')]: ax.annotate(f'{lab} k-in', (xx, 1.8), ha='center', fontsize=8, color='crimson')
ax.set_xlim(-3, 80); ax.set_ylim(-3, 3); ax.set_aspect('equal'); ax.set_title('Geometry (A fixed on the left)'); ax.axis('off')
ax = axs[1]; ax.step([0, 25, 50, 75], Tp+[Tp[-1]], where='post', c='navy', lw=2); ax.fill_between([0, 25, 50, 75], Tp+[Tp[-1]], step='post', alpha=.2); ax.set_title('Internal torque T(x) (k-in)'); ax.set_xlabel('x from A (in)'); ax.grid(alpha=.3)
ax = axs[2]; ax.step([0, 25, 50, 75], [tau['AB'], tau['BC'], tau['CD']]+[tau['CD']], where='post', c='crimson', lw=2); ax.axhline(tau['BC'], c='k', ls=':'); ax.text(2, tau['BC']+.08, f"τ_max = {tau['BC']:.3f} ksi (segment BC)", fontsize=9); ax.set_title('Surface shear stress τ = 16T/(πd³) (ksi)'); ax.set_xlabel('x from A (in)'); ax.grid(alpha=.3); ax.set_ylim(0, 5.3)
ax = axs[3]; xs = [0, 25, 50, 75]; ph = [0, phiB, phiC, phiD]; ax.plot(xs, np.degrees(ph), 'o-', c='green', lw=2); ax.set_title(f'Cumulative twist φ(x) (deg): φ_D = {np.degrees(phiD):.3f}°'); ax.set_xlabel('x from A (in)'); ax.grid(alpha=.3)
save(fig, 'SM-T6-Q1-stepped-shaft.png')

# ======================================================== Q2 tapered bar
f = lambda x: 3*x**3-2*x**2-2*x-2                         # phi_t/phi_p = 1/2  <=>  (1+x+x^2)/(3x^3) = 1/2
xr = brentq(f, 1.0, 2.0); print('Q2 dB/dA =', xr)
# numerical check of the taper integral (dA = 1, L = 1, T = 1, G = 1, pi/32 absorbed)
dA = 1.0; dB = xr
phi_t = quad(lambda s: 32/(np.pi*(dA+(dB-dA)*s)**4), 0, 1)[0]; phi_p = 32/(np.pi*dA**4)
print('Q2 phi_t/phi_p =', phi_t/phi_p)
xs = np.linspace(0.6, 3, 300); ratio = (1+xs+xs**2)/(3*xs**3)
fig, axs = plt.subplots(1, 2, figsize=(12, 4.2)); ax = axs[0]
ax.plot(xs, ratio, c='navy', lw=2); ax.axhline(.5, c='gray', ls=':'); ax.axvline(xr, c='gray', ls=':'); ax.plot(xr, .5, 'ro'); ax.annotate(f'd_B/d_A = {xr:.4f}', (xr, .5), xytext=(xr+.2, .75), arrowprops=dict(arrowstyle='->'))
ax.plot(1, 1, 'ks'); ax.text(1.03, 1.02, 'prismatic (x = 1)'); ax.set_xlabel('x = d_B/d_A'); ax.set_ylabel('φ_taper / φ_prismatic'); ax.set_title('Twist ratio  (1 + x + x²)/(3x³)'); ax.grid(alpha=.3)
ax = axs[1]; s = np.linspace(0, 1, 100); ax.fill_between(s, -(1+(xr-1)*s)/2, (1+(xr-1)*s)/2, alpha=.3, color='orange', ec='k'); ax.plot(s, np.full_like(s, .5), 'k--', lw=1); ax.plot(s, -np.full_like(s, .5), 'k--', lw=1)
ax.text(0, .62, 'd_A'); ax.text(1, (1+(xr-1))/2+.1, f'd_B = {xr:.3f} d_A'); ax.set_aspect('equal'); ax.axis('off'); ax.set_title('Tapered bar giving half the twist of the d_A prismatic bar (dashed)')
save(fig, 'SM-T6-Q2-taper.png')

# ======================================================== Q3 mismatched shafts (illustrative numbers, SI)
Gs = 80e9; a_, b_ = 0.5, 0.4
Do, Di, ds = 0.040, 0.034, 0.030
J1 = np.pi*(Do**4-Di**4)/32; J2 = np.pi*ds**4/32; alpha = np.radians(2.0)
MT = alpha/(a_/(Gs*J1)+b_/(Gs*J2)); beta = MT*a_/(Gs*J1); phi2 = MT*b_/(Gs*J2)
print('Q3 MT (N m)', MT, 'beta (deg)', np.degrees(beta), 'phi2 (deg)', np.degrees(phi2), 'sum', np.degrees(beta+phi2), ' tau1', 16*MT*Do/(np.pi*(Do**4-Di**4))/1e6, ' tau2', 16*MT/(np.pi*ds**3)/1e6, 'MPa')
print('Q3 beta formula alpha*a/(a + b J1/J2) =', np.degrees(alpha*a_/(a_+b_*J1/J2)))
fig, ax = plt.subplots(figsize=(8.5, 4.2))
xs1 = np.array([0, a_]); xs2 = np.array([a_, a_+b_])
ax.plot(xs1, np.degrees([0, beta]), 'b-', lw=3, label='shaft ① (wall at x = 0): rises to β'); ax.plot(xs2, np.degrees([beta, alpha]), 'r-', lw=3, label='shaft ② measured from the bolt side: reaches α at its wall')
ax.plot([a_, a_], [np.degrees(beta), np.degrees(beta)], 'ko'); ax.annotate('', xy=(a_+b_+.03, np.degrees(alpha)), xytext=(a_+b_+.03, 0), arrowprops=dict(arrowstyle='<->')); ax.text(a_+b_+.04, np.degrees(alpha)/2, 'α (mismatch)')
ax.annotate('', xy=(a_-.03, np.degrees(beta)), xytext=(a_-.03, 0), arrowprops=dict(arrowstyle='<->', color='b')); ax.text(a_-.04, np.degrees(beta)/2, 'β = φ₁', ha='right', color='b')
ax.set_xlabel('x (m)'); ax.set_ylabel('angle (deg)'); ax.set_title('Compatibility: φ₁ + φ₂ = α  (example: α = 2°)'); ax.legend(fontsize=8, loc='lower right'); ax.grid(alpha=.3)
save(fig, 'SM-T6-Q3-mismatch.png')

# ======================================================== Q4 distributed torque
tA, Lb, db, Gb = 500.0, 1.2, 0.040, 80e9; Jb = np.pi*db**4/32
Tx = lambda x: tA*(Lb-x)**2/(2*Lb)                          # internal torque at x (A fixed at x = 0)
tmax = 16*Tx(0)/(np.pi*db**3); ph = quad(lambda x: Tx(x)/(Gb*Jb), 0, Lb)[0]
print('Q4 T(0)=tA L/2 =', Tx(0), ' tau_max =', tmax/1e6, 'MPa (formula', 8*tA*Lb/(np.pi*db**3)/1e6, ')  phi =', ph, 'rad =', np.degrees(ph), 'deg (formula', tA*Lb**2/(6*Gb*Jb), ')')
xs = np.linspace(0, Lb, 200); phx = np.array([quad(lambda s: Tx(s)/(Gb*Jb), 0, xx)[0] for xx in xs])
fig, axs = plt.subplots(1, 3, figsize=(15, 3.8)); axs[0].plot(xs, tA*(1-xs/Lb), c='crimson', lw=2); axs[0].fill_between(xs, tA*(1-xs/Lb), alpha=.2, color='crimson'); axs[0].set_title('t(x) = t_A(1 − x/L)  (N·m/m)')
axs[1].plot(xs, Tx(xs), c='navy', lw=2); axs[1].fill_between(xs, Tx(xs), alpha=.2); axs[1].set_title('Internal torque T(x) = t_A (L−x)²/(2L): max t_A L/2 at the wall'); axs[1].set_ylabel('N·m')
axs[2].plot(xs, np.degrees(phx), c='green', lw=2); axs[2].set_title('Twist φ(x): cubic, ends at t_A L²/(6GJ)'); axs[2].set_ylabel('deg')
for a_ in axs: a_.set_xlabel('x from fixed end A (m)'); a_.grid(alpha=.3)
save(fig, 'SM-T6-Q4-distributed-torque.png')

# ======================================================== Q5 shrink-fit composite
R1, R2, G1, G2, l, MT5 = 0.020, 0.030, 80e9, 27e9, 1.0, 2000.0
J1 = np.pi*R1**4/2; J2 = np.pi*(R2**4-R1**4)/2
phi5 = MT5*l/(G1*J1+G2*J2); T1 = G1*J1*phi5/l; T2 = G2*J2*phi5/l
tau1 = G1*R1*phi5/l; tau2 = G2*R2*phi5/l
print('Q5 phi', phi5, 'rad', np.degrees(phi5), 'deg; T1', T1, 'T2', T2, 'sum', T1+T2, '; tau1max', tau1/1e6, 'tau2max', tau2/1e6, 'MPa; tau2 at R1', G2*R1*phi5/l/1e6)
r = np.linspace(0, R2, 400); g = np.where(r <= R1, G1, G2); tauR = g*r*phi5/l/1e6
fig, ax = plt.subplots(figsize=(8, 4.2)); ax.plot(r*1e3, tauR, c='crimson', lw=2); ax.axvline(R1*1e3, c='gray', ls=':'); ax.text(R1*1e3+.3, 5, 'interface R₁ (strain continuous, stress jumps)', rotation=90, fontsize=8)
ax.annotate(f'τ₁,max = {tau1/1e6:.1f} MPa', (R1*1e3, tau1/1e6), xytext=(3, tau1/1e6+4), arrowprops=dict(arrowstyle='->')); ax.annotate(f'τ₂,max = {tau2/1e6:.1f} MPa', (R2*1e3, tau2/1e6), xytext=(18, tau2/1e6+10), arrowprops=dict(arrowstyle='->'))
ax.set_xlabel('radius r (mm)'); ax.set_ylabel('τ(r) = G(r) r φ/l (MPa)'); ax.set_title('Shrink-fit shaft (steel core R₁ = 20 mm, aluminium tube R₂ = 30 mm, M_T = 2 kN·m)'); ax.grid(alpha=.3)
save(fig, 'SM-T6-Q5-composite-shaft.png')

# ======================================================== Q6 gear train
R1g, R2g, M1, l1, l2, tadm, Gg = 0.100, 0.050, 500.0, 0.60, 0.40, 60e6, 80e9
M2 = M1*R2g/R1g; d1 = (16*M1/(np.pi*tadm))**(1/3); d2 = (16*M2/(np.pi*tadm))**(1/3)
J1g = np.pi*d1**4/32; J2g = np.pi*d2**4/32
phiB = M2*l2/(Gg*J2g); phiC = (R2g/R1g)*phiB+M1*l1/(Gg*J1g)
phiC_formula = 32*M1/(Gg*np.pi)*(l1/d1**4+l2/d2**4*(R2g/R1g)**2)
print('Q6 M2', M2, 'd1,d2 (mm)', d1*1e3, d2*1e3, ' phiB deg', np.degrees(phiB), ' phiC deg', np.degrees(phiC), 'formula', np.degrees(phiC_formula))
fig, axs = plt.subplots(1, 2, figsize=(13, 4.6)); ax = axs[0]
ax.set_xlim(-1, 9); ax.set_ylim(-3.2, 4); ax.set_aspect('equal'); ax.axis('off')
ax.add_patch(plt.Circle((3, 2), 1.6, fc='#cfe3ff', ec='k')); ax.add_patch(plt.Circle((3, -0.6), 0.8, fc='#ffd9b3', ec='k'))
ax.text(3, 2, 'gear\nR₁', ha='center', va='center'); ax.text(3, -.6, 'gear R₂', ha='center', va='center', fontsize=8)
ax.plot([3, 8], [2, 2], c='navy', lw=8, alpha=.5); ax.text(5.5, 2.35, 'shaft ①  (l₁, d₁)', ha='center'); ax.text(8.1, 2, 'C', va='center')
ax.plot([-.3, 3], [-.6, -.6], c='darkorange', lw=8, alpha=.5); ax.text(1.2, -1.1, 'shaft ②  (l₂, d₂)', ha='center'); ax.text(-.5, -.6, 'A', ha='right', va='center')
ax.annotate('M₁', (8.6, 2.0), xytext=(7.6, 3.1), color='crimson', fontsize=11, arrowprops=dict(arrowstyle='->', color='crimson')); ax.annotate('M₂', (-1.3, -.6), xytext=(-.3, -2), color='crimson', fontsize=11, arrowprops=dict(arrowstyle='->', color='crimson'))
ax.annotate('', xy=(3, 0.2), xytext=(3, 0.4), arrowprops=dict(arrowstyle='<->')); ax.text(3.2, .35, 'mesh point:\nF = M₁/R₁', fontsize=8, color='green')
ax.set_title('Gear train (Fig. 6): same tooth force F, opposite rotation')
ax = axs[1]; xa = [0, l2, l2+0.0, l2+l1]; ang = [0, np.degrees(phiB), np.degrees((R2g/R1g)*phiB), np.degrees(phiC)]
ax.plot([0, l2], [0, np.degrees(phiB)], 'o-', c='darkorange', lw=3, label='shaft ②: twist φ₂ = M₂l₂/(GJ₂)'); ax.plot([l2, l2], [np.degrees(phiB), np.degrees((R2g/R1g)*phiB)], ':k'); ax.plot([l2, l2+l1], [np.degrees((R2g/R1g)*phiB), np.degrees(phiC)], 'o-', c='navy', lw=3, label='shaft ①: (R₂/R₁)φ_B + M₁l₁/(GJ₁)')
ax.text(l2+.01, np.degrees(phiB)*.75, 'gear ratio\nφ₁ = (R₂/R₁) φ_B', fontsize=8); ax.set_xlabel('distance along the path A → B → C (m)'); ax.set_ylabel('angle (deg, magnitude)'); ax.set_title(f'Angle of twist along the path: φ_C = {np.degrees(phiC):.3f}° (example)'); ax.legend(fontsize=8); ax.grid(alpha=.3)
save(fig, 'SM-T6-Q6-gear-train.png')
print('done')

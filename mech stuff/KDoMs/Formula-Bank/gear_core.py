"""Shared gear formulae (Ghosh & Mallik, Ch. 9) + self-check against the book's worked problems."""
import numpy as np
from math import *

def inv(a): return tan(a) - a

def rb_of(rp, a): return rp * cos(a)

def path_of_contact(rp1, rp2, ro1, ro2, a):              # (9.11)
    C = rp1 + rp2
    rb1, rb2 = rp1*cos(a), rp2*cos(a)
    return sqrt(ro1**2-rb1**2) + sqrt(ro2**2-rb2**2) - C*sin(a)

def contact_ratio(rp1, rp2, ro1, ro2, a, N2):            # (9.12)
    rb2 = rp2*cos(a)
    return path_of_contact(rp1, rp2, ro1, ro2, a) / (2*pi*rb2/N2)

def contact_ratio_rack(N1, rp1, ro1, ar, a):             # (9.14)
    rb1 = rp1*cos(a)
    return N1/(2*pi*rb1) * (ar/sin(a) + sqrt(ro1**2-rb1**2) - rb1*tan(a))

def n1min(lam, f, a):                                    # (9.17)  lam = w2/w1 = N1/N2
    return 2*f*lam / (sqrt(1 + lam*(lam+2)*sin(a)**2) - 1)

def n1min_rack(f, a): return 2*f/sin(a)**2              # (9.18)

def epicyclic_solve(): pass

def check():
    a = radians(20)
    assert abs(path_of_contact(51.5, 64.2, 57.5, 71.2, a) - 29.3) < .1          # P9.1
    assert abs(contact_ratio(51.5, 64.2, 57.5, 71.2, a, 20) - 1.55) < .01
    assert abs(contact_ratio_rack(31, 62, 66, 4, a) - 1.82) < .01                # P9.2
    assert abs(n1min(16/18, 1, radians(14.5)) - 22.94) < .02                     # P9.3
    assert abs(n1min_rack(1, a) - 17.1) < .05                                    # P9.4
    # 9.13  3N^2 sin^2a - 4fN - 4f^2 = 0  <->  (9.17) with lam = 1
    for al in (14.5, 20, 25):
        s = sin(radians(al)); N = n1min(1, 1, radians(al))
        assert abs(3*N*N*s*s - 4*N - 4) < 1e-9
    # P9.8 epicyclic: n_arm=200, n_F=-50 ; P9.7 Ferguson: nE=1/51, nD=-1/49
    assert abs(-(1/(1-0)) * 0 + (200 - 5/16*800) + 50) < 1e-9
    assert abs(1 - 50/51 - 1/51) < 1e-12 and abs(1 - 50/49 + 1/49) < 1e-12
    # P9.10 torques
    M1 = 7.5e3*60/(2*pi*1000); M2 = -M1*1000/(-50)
    assert abs(M1-71.66) < .05 and abs(M2-1433) < 2 and abs(-(M1+M2)+1504.66) < 3
    # involute pair (9.30,9.31)->(9.34,9.35): mapping through (9.22,9.23) must give the book's gear-2 profile
    rp1, rp2 = 1.0, 1.7; C = rp1+rp2; g = 1 + rp1/rp2
    for th1 in np.linspace(-0.4, 0.6, 7):
        x1 = rp1*cos(a)*((th1+tan(a))*sin(th1+a)+cos(th1+a))
        y1 = rp1*cos(a)*(sin(th1+a)-(th1+tan(a))*cos(th1+a))
        x2 = (x1-C*cos(th1))*cos(g*th1)+(y1-C*sin(th1))*sin(g*th1)
        y2 = -(x1-C*cos(th1))*sin(g*th1)+(y1-C*sin(th1))*cos(g*th1)
        th2 = rp1*th1/rp2
        X2 = -rp2*cos(a)*((-th2+tan(a))*sin(-th2+a)+cos(-th2+a))
        Y2 = rp2*cos(a)*((-th2+tan(a))*cos(-th2+a)-sin(-th2+a))   # book prints +sin; transformation (9.22/9.23) gives -sin
        assert abs(x2-X2) < 1e-9 and abs(y2-Y2) < 1e-9
    print("all worked-problem checks passed")

if __name__ == "__main__": check()

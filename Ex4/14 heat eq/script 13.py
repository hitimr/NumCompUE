import numpy as np
from scipy.fft import fft, ifft
from cmath import pi, exp
import matplotlib.pyplot as plt


n = 100


def Chi(a,b,x):
    if (a <= x) and (x < b): return 1.0
    else: return 0.0

a, b = 0, 1
n = 1000
dx = (a+b)/n
x_vals = np.linspace(a, b, n)


#The returned float array f contains the frequency bin centers in cycles per
#unit of the sample spacing (with zero at the start). For instance, if the
#sample spacing is in seconds, then the frequency unit is cycles/second.
kappa = 2*pi*np.fft.fftfreq(n, d=dx)



u0 = [Chi(0.3,0.7,x) for x in x_vals]
u0_hat = fft(u0)


def u_hat_t(kappa, t): return u0_hat*exp(-kappa**2*t)

t = 0.001
sol = [u_hat_t(kappa[i], t) for i in range(n)]
plt.plot(x_vals, u0)
plt.plot(x_vals, ifft(sol))
plt.show()
import numpy as np
from math import sin, cos, pi, exp
from scipy.fftpack import fft
import time
import matplotlib.pyplot as plt


def f1(x): return sin(40*pi*x)
def f2(x,a=0.25, b=0.75): 
    if (a <= x) and (x < b): return 1.0
    else: return 0.0
def f3(x): return min([x, 1 - x])
def f4(x): return exp(-100.0*(x-0.5)**2)
def f5(x): return exp(-4.0*(x-0.5)**2)
def f6(x): return exp(-100.0*(x-0.5)**2) * sin(40*pi*x)



times = []
p_max = 22 # evaluated b trial and error
for p in range(2, p_max+1):
    n = 2**p
    x = [j/n for j in range(n)]
    f1_vals = np.array([f1(x_i) for x_i in x])

    start_time = time.time()
    a_k = fft(f1_vals)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(times)
#plt.yscale("log")
plt.show()

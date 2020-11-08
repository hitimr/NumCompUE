import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi

# Functrions from Exercise shit
def f_x(t): return (t+1)*cos(4*pi*t)    
def f_y(t): return (t+1)*sin(4*pi*t)


# C-Coefficients accordinbg to (Dahmen+Reusken Alg 9.12)
def C(j, p, k, x_vals, c_vals, t):   
    if p == 0:
        return c_vals[j]
    else:
        return (x_vals - t[j]) / (t[j+k-p] - t[j]) * C(j, p-1, k, x_vals, c_vals, t) + \
           (t[j+k-p] - x_vals) / (t[j+k-p] - t[j]) * C(j-1, p-1, k, x_vals, c_vals, t)

def Chi(a,b,x):
    if (a <= x) and (x < b): return 1.0
    else: return 0.0

def N(j, k, x, t):
    if k == 1:
        return Chi(t[j], t[j+1], x)
    else:
        if (t[j+k-1] - t[j]) == 0: 
            c1 = 0
        else: 
            c1 = (x - t[j]) / (t[j+k-1] - t[j])

        if (t[j+k] - t[j+1]) == 0: 
            c2 = 0
        else: 
            c2 = (t[j+k] - x) / (t[j+k] - t[j+1])

        return  c1 * N(j, k-1, x, t) +  c2 * N(j+1, k-1, x, t)

def Q(x, m, k, c, t):
    return [k * (c[j+m-k+1] - c[j+m-k]) / (t[j+m+1] - t[j+m-k+1]) for j in range(0, k)]
     



# Find m ∈[t_m, t_m+1] while excluding k-multiple points at the ends
# Would work much faster with divide-and-conquer algorithm but this one does the job as well
def find_m(x, t, k):
    for m in range(len(t)-1):
        if t[m] <= x < t[m+1]: 
            return m
    return len(t)-k-2

def BSpline(f):
    end = pi
    k = 6
    n = 1000
    knots = [0 for i in range(k)] + np.linspace(0, end, n).tolist() + [end for i in range(k)]   # Knots with k-multiple at the ends
    control_points = [f(j) for j in np.linspace(0, end,n+2*k)]
    return [C(find_m(t, knots, k), k-1, k, t, control_points, knots) for t in np.linspace(0, end, n)]

def BSpline_deriv(f):
    x = 1
    n = 100
    k = 6
    t = 0.5
    end = pi
    knots = [0 for i in range(k)] + np.linspace(0, end, n).tolist() + [end for i in range(k)]
    control_points = [f(j) for j in np.linspace(0, end,n+2*k)]

    for j in range(n):
        N(j, k-1, t, knots)*Q(t, find_m(t, knots, k), k, control_points, knots)


S_x = BSpline_deriv(f_x)
S_y = BSpline_deriv(f_y)
plt.plot(S_x, S_y)
plt.show()
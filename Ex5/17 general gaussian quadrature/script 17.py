import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigh, det
from math import sqrt, pow


def gamma(j):
    return 1.0 / sqrt(4 - (j+1)**-2.0)

def A_n(n):
    A = np.zeros((n,n), dtype=np.float64)

    # fill secondary diagonal;
    for i in range(n-1):
        g = gamma(i)
        A[i][i+1] = g
        A[i+1][i] = g
    return A

def L_n(x, n):
    A = A_n(n)
    I = np.identity(n)
    return det(x*I-A)


point_cnt = 1000
x_vals = np.linspace(-1,1, point_cnt)

# Todo Plots
for n in range(0,5):
    y_vals = [L_n(x,n) / L_n(1,n) for x in x_vals]
    plt.plot(x_vals, y_vals)
plt.grid()
#plot.show()



# Find roots of L_n by computing the eigenvalues of A_n
#roots = eigh(A_n) 

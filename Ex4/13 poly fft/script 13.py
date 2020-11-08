from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
from cmath import exp, pi, rect


def polynom(coeffs, x): 
    """calculate a polynom of type c_0 + c_1 * x^1 + c_2 * x^3 + ...c_n * x^n

    Args:
        coeffs (array-like): list or array of coefficients c0 ... cn
        x (array-like): list of x values to compute

    Returns:
        (array): result of the polynom
    """    
    if hasattr(x, "__len__"):
        return np.array([polynom(coeffs, x_i) for x_i in x])
    return sum([coeffs[i]*x**i for i in range(len(coeffs))])

def complex_unitCircle_points(n):
    return [rect(1, phi) for phi in np.linspace(0, 2*pi, n)]


resolution = 1000
n = 100 # order of the polynom - 1
x_vals = np.linspace(-1, 1, resolution)
a_coeffs = [1 for i in range(n)] #a(x) = sum(x^i)
b_coeffs = [i for i in range(n)] #b(x) = sum(i*x^i)

# The procuct of two polynoms of degree n is 2n. Therefore we need to append some zeroes make the algorithm work
a_coeffs += [0 for i in range(n)]
b_coeffs += [0 for i in range(n)]

x_j = complex_unitCircle_points(2*n)
A_vals = polynom(a_coeffs, x_j)
B_vals = polynom(b_coeffs, x_j)
C_vals = A_vals*B_vals

c_coeffs = ifft(C_vals)

print(polynom([0,0,0], 0))
plt.plot(x_vals, polynom(c_coeffs, x_vals))
plt.show()


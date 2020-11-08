import numpy as np
import matplotlib.pyplot as plt

def T_n(x, n):
    if n == 0: return 1
    if n == 1: return x
    return 2*x*T_n(x,n-1) - T_n(x, n-2) 

def lc(n):
    if n == 0: return 0
    else: return 2**(n-1)


x_min = -1.0
x_max = 1.0
point_count = 500
polynomial_count = 6

x_vals = np.linspace(x_min, x_max, point_count)

Chebyshev_polynomials = []
for n in range(polynomial_count):
    Chebyshev_polynomials.append([T_n(x,n) for x in x_vals])

# Plot the first few polynomials
i = 0
for polynomial in Chebyshev_polynomials:
    i += 1
    label = "n=" + str(i)
    plt.plot(x_vals, polynomial, label=label)

plt.title("The first 6 Chebyshec Polynomials")
plt.legend()
plt.savefig("Lagrange_Poltnomials")

# Determine the leading coefficient
# 2*x*T_n -> previous LC will always get doubled. By definition LC_0 = 0, LC_1 = 1, => LC_2 = 2, LC_3 = 4
# => LC_n = 2^(n-1)


    
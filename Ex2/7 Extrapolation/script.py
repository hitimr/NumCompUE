from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
from math import pi
import numpy as np

def g(x):
    if hasattr(x, "__len__"): return [g(x) for x in x]
    else: return sum([6.0 / (j*j) for j in range(1, 1+int(round(1/x, 0)))])

def generate_knots(count):
     return [2**(-i) for i in range(count)]

knots = generate_knots(10)
poly = lagrange(knots, g(knots))
p0 = poly(0)


x_vals = np.linspace(0,1,100)
y = [poly(x) for x in x_vals]
plt.plot(x_vals, y)
plt.title("Interpolated Polynom p of the transofmed sum")
plt.plot(knots, g(knots), "x")
#plt.show()

print("p(0) = " + str(p0))
print("π² = " + str(pi*pi))
print("Error = " + str(abs(p0 - pi*pi)))

import numpy as np


x = np.loadtxt("in/x.txt")
y = np.loadtxt("in/y.txt")
n = len(x)
z = np.zeros(n)

for i in range(n):
    z[i] = x[i] + y[i]
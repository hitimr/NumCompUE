import numpy as np


x = np.loadtxt("in/x.txt")
A = np.loadtxt("in/A.txt")
n = len(x)
z = np.zeros(n)

for i in range(n):
    for j in range(n):
        z[i] += x[j]*A[i][j]
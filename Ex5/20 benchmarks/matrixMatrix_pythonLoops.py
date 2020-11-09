import numpy as np


A = np.loadtxt("in/A.txt")
B = np.loadtxt("in/B.txt")
n = len(A)
C = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][j] + B[j][k]
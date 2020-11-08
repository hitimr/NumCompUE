import numpy as np


x = np.loadtxt("in/x.txt")
A = np.loadtxt("in/A.txt")
z = np.matmul(A,x)

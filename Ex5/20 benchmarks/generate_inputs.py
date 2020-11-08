import numpy as np
import sys

try:
    n = int(sys.argv[1])
except:
    n = 2

x = np.random.rand(n)
y = np.random.rand(n)
A = np.random.rand(n, n)
B = np.random.rand(n, n)
C = np.random.rand(n, n)

np.savetxt("in/x.txt", x)
np.savetxt("in/y.txt", y)
np.savetxt("in/A.txt", A)
np.savetxt("in/B.txt", B)
np.savetxt("in/C.txt", C)
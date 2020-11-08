import numpy as np
from scipy import linalg


A = np.array([
    [10**-6, 1],
    [1,0]
    ])


L = np.array([
    [1, 0], 
    [10**6, 1]
    ])

U = np.array([
    [10**-6, 1], 
    [0, -1.0*10**6]
    ])


print(L*U)


import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin

def Chi(a,b,x):
    if (a <= x) and (x < b): return 1.0
    else: return 0.0

def N(j, k, x, t):
    if k == 1:
        return Chi(t[j], t[j+1], x)
    else:
        if (t[j+k-1] - t[j]) == 0: 
            c1 = 0
        else: 
            c1 = (x - t[j]) / (t[j+k-1] - t[j])

        if (t[j+k] - t[j+1]) == 0: 
            c2 = 0
        else: 
            c2 = (t[j+k] - x) / (t[j+k] - t[j+1])

        return  c1 * N(j, k-1, x, t) +  c2 * N(j+1, k-1, x, t)



plt.figure(figsize=(7,7))
k = 4
n = 8
x_vals = np.linspace(0,n, 1000)
t = [0 for i in range(k-1)] + [j for j in range(n-1)] + [n-1 for i in range(k)]
print(t)

for j in range(n+k-2):
    y_vals = [N(j, k, x, t) for x in x_vals]
    plt.plot(x_vals, y_vals, label="j="+str(j))
plt.legend()
plt.title("B for fixed k = 3")
plt.show()
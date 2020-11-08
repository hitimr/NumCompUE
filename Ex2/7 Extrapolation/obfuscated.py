from scipy.interpolate import lagrange as l
def g(x): 
    if hasattr(x, "__len__"): return [g(x) for x in x]
    else: return sum([6.0 / (j*j) for j in range(1, int(round(1/x, 0)))])

k = [2**(-i) for i in range(10)]
p = l(k, g(k))
print(p(0))

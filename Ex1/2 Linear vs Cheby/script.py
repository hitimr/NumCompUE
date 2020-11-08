import numpy as np
import scipy
import matplotlib.pyplot as plt

def func(x_vals):
    #if type(x_vals) == np.float64: return (1.0 / (x**2 + 1))
    #return [1.0 / (x**2 + 1) for x in x_vals]
    return 1.0 / (1 + x*x)
     
    #return x*x*x


def Lagrange (pts, i, x):
    prod = 1
    for j in range(len(pts)):
        if j != i:
            prod = prod * (x-pts[j])/(pts[i]-pts[j])
    return prod

def InterpolationPolynomial (fun, pts, x):
    return sum( [fun(p) * Lagrange(pts, i, x) for i,p in enumerate(pts)] )


if __name__ == "__main__":
    x_min = -5.0
    x_max = 5.0
    n = 20

    x = np.linspace(x_min, x_max, 1000)
    pts = np.linspace(x_min, x_max, n)
    #plt.plot (x, func(x), x, InterpolationPolynomial(func, pts, x), pts, func(pts), "x")
    plt.plot(x, InterpolationPolynomial(func, pts, x))
    plt.ylim(-2,2)
    plt.show()

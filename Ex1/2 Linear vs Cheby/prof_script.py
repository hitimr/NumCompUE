from math import pi
import math
from numpy import sin, linspace
import numpy as np
import matplotlib.pyplot as plt

# l_i
def Lagrange (pts, i, x):
    prod = 1
    for j in range(len(pts)):
        if j != i:
            prod = prod * (x-pts[j])/(pts[i]-pts[j])
    return prod

# p(x)
def InterpolationPolynomial (fun, pts, x):
    sum = 0
    for i in range(len(pts)):
        sum = sum + fun(pts[i]) * Lagrange(pts, i, x)
    return sum



def chebyshev_points(start, end, count):
    return [5*math.cos( (i+0.5)*pi / (count + 1)) for i in range(count)]

# f(x) = 1 / (x² + 1)
# returns a number if x is a number or a list if x is list-like object
def func(x):
    if (type(x) == np.float64) or (type(x) == float): return 1.0/(1 + x*x)
    return [1.0/(1 + x_i*x_i) for x_i in x]

def chebyshev_points(start, end, count):
    return [5*math.cos( (i+0.5)*pi / (count + 1)) for i in range(count)]

def createInterpolationPlot(pts, title, filename):
    y_min, y_max = -10,10
    x = linspace(a,b,1000)
    plt.plot(x, func(x), label="analytical function")
    plt.plot(x, InterpolationPolynomial(func, pts, x), label="lagrange interpolation")
    plt.plot(pts, func(pts), "x")
    plt.legend()
    plt.ylim(y_min, y_max)
    plt.title(title)
    plt.savefig(filename)
    plt.cla()

def createLagrangePlot(pts, title, filename):

    for i in range(8):
        plt.plot(Lagrange(pts, i, x))

    plt.ylim(-10,10)
    #plt.xlim(-5,5)
    plt.title(title)
    plt.savefig(filename)
    plt.cla()

def createPlots():
    a,b = -5.0, 5.0
    x = linspace(a,b,1000)
    pts = linspace(a,b, 10)

    pts = linspace(a,b, 10)
    createInterpolationPlot(pts, "uniformly distributed points, n=10", "linear_10")
    createLagrangePlot(pts, "Lagrange Polynomials, linear, n=10", "lagrange_linear_10")

    pts = linspace(a,b, 20)
    createInterpolationPlot(pts, "uniformly distributed points, n=20", "linear_20")
    createLagrangePlot(pts, "Lagrange Polynomials, linear, n=20", "lagrange_linear_20")

    pts = linspace(a,b, 40)
    createInterpolationPlot(pts, "uniformly distributed points, n=40", "linear_40")
    createLagrangePlot(pts, "Lagrange Polynomials, linear, n=40", "lagrange_linear_40")

    pts = chebyshev_points(a,b, 10)
    createInterpolationPlot(pts, "chebyshev points, n=10", "chebyshev_10")
    createLagrangePlot(pts, "Lagrange Polynomials, chebyshev, n=10", "lagrange_chebyshev_10")

    pts = chebyshev_points(a,b, 20)
    createInterpolationPlot(pts, "chebyshev points, n=20", "chebyshev_20")
    createLagrangePlot(pts, "Lagrange Polynomials, chebyshev, n=10", "lagrange_chebyshev_20")

    pts = chebyshev_points(a,b, 40)
    createInterpolationPlot(pts, "chebyshev points, n=40", "chebyshev_40")
    createLagrangePlot(pts, "Lagrange Polynomials, chebyshev, n=40", "lagrange_chebyshev_40")


def calculate_max_vals(pts):

    n_max = 10
    x_vals = linspace(a,b,1000)

    # max ( max ( |l_i(x)| ))
    max_vals1 = [max([max(abs(Lagrange(pts, i, x))) for i in range(n)]) for n in range(1,n_max)]

    max_vals2 = []
    for n in range(n_max):
        sum = np.zeros(len(x), dtype=float)
        for i in range(n):
            sum += abs(Lagrange(pts, i, x))
        max_vals2.append(max(sum))

    return max_vals1, max_vals2


a,b = -5.0, 5.0
x = linspace(a,b,100)
pts = linspace(a,b, 20)



#createPlots()
pts = linspace(a,b, 20)
max1_lin, max2_lin = calculate_max_vals(pts)

pts = chebyshev_points(a,b, 20)
max1_cheb, max2_cheb = calculate_max_vals(pts)

plt.cla()
plt.plot(max1_lin, label="linear")
plt.plot(max1_cheb, label="chebychev")
plt.title("max(max(|li|))")
plt.legend()
plt.xlabel("n")
plt.savefig("max1")

plt.cla()
plt.plot(max2_lin, label="linear")
plt.plot(max2_cheb, label="chebychev")
plt.title("max(sum(|li|))")
plt.legend()
plt.xlabel("n")
plt.savefig("max2")







#plt.cla()


#.plot(max_vals2)
#lt.title("max(sum(|l_i_x|)) depending on n")
#plt.xlabel("n")
#plt.savefig("max2")
#plt.cla()




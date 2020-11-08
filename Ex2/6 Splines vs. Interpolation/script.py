import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from math import sqrt, atan, cos, pi


F1_XMIN, F1_XMAX = 0.0, 1.0
F2_XMIN, F2_XMAX = -1.0, 1.0
PLOT_POINT_CNT = 1000



def f1(x):
    if hasattr(x, "__len__"):
        return [f1(x) for x in x]
    else:
        return sqrt(x)

def f2(x):
    if hasattr(x, "__len__"):
        return [f2(x) for x in x]
    else:
        return atan(10.0*x)

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

# Function for generating Chebyshev Points
def chebyshev_points(count):
    return np.array([cos((2*i-1)*pi / (2*n)) for i in range(count)])



def compareFunctions(f, f_knots, xMin, xMax, plotPoint_count):
    xVals = np.linspace(xMin, xMax, plotPoint_count)

    f_analyticVals = f(xVals)

    # Cubic Spline Interpolation
    cubicInterpolation = interpolate.CubicSpline(f_knots, [f(x) for x in f_knots])
    cubic_vals = cubicInterpolation(xVals)

    # Polynomial Interpolation
    poly_interpolation = InterpolationPolynomial(f, f_knots, xVals)


    # Plot functions
    plt.cla()
    plt.plot(xVals, f_analyticVals, label="analytic")
    plt.plot(xVals, cubic_vals, label="cubic")
    plt.plot(xVals, poly_interpolation, label="polynomial")
    plt.plot(f_knots, f(f_knots), "x", label="interpolated points")
    plt.legend()
    #plt.show()

    # Plot convergence
    plt.cla()
    error = abs(f_analyticVals - poly_interpolation)
    max_error = max(error)
    print(max_error)


    plt.plot(xVals, abs(f_analyticVals - cubic_vals), label="cubic")
    plt.plot(xVals, abs(f_analyticVals - poly_interpolation), label="polynomial")

    plt.show()


if __name__ == "__main__":
    f1_knots = chebyshev_points(20)
    f2_knots = np.linspace(F1_XMIN, F1_XMAX, 20)
    compareFunctions(f1, f1_knots, F1_XMIN, F1_XMAX, PLOT_POINT_CNT)
    compareFunctions(f2, f2_knots, F2_XMIN, F2_XMAX, PLOT_POINT_CNT)


import numpy as np
import matplotlib.pyplot as plt

# Analytical function for f1
def f1(x):
    return 1.0 / (x - 1.0)

# Tatylor series for f1
# -1 - x - x^2 - x^3 - ...
def f1_taylor(x, n):
    ret_val = 0
    for i in range(n):
        ret_val = ret_val + -1.0*x**i
    return ret_val

# Analytical function for f2
def f2(x):
    return 1.0 / (x**2 + 1)

# Tatylor series for f2
# 1 - x^2 + x^4 - x^6 + x^8 ...
def f2_taylor(x, n):
    ret_val = 0
    for i in range(n):
        if not (i % 2): # if even
            # alternating signs
            if i % 4: 
                ret_val -= x**i                   
            else: 
                ret_val += x**i
    return ret_val

def createPlot(x, analytic, taylor10, taylor20, taylor40, title, fileName):
    y_min, y_max = -10, 10
    plt.plot(x, analytic, label="exact")
    plt.plot(x, taylor10, label="taylor n=10")
    plt.plot(x, taylor20, label="taylor n=20")
    plt.plot(x, taylor40, label="taylor n=40")

    plt.legend(loc="upper right")
    plt.title(title)
    plt.ylim(y_min, y_max)
    plt.savefig(fileName)
    plt.cla()

if __name__ == "__main__":
    x_min = -2
    x_max = 2

    point_count = 1000

    x_vals = np.linspace(x_min, x_max, point_count)

    f1_analytic = [ f1(x) for x in x_vals ]
    f2_analytic = [ f2(x) for x in x_vals ]

    f1_taylor_vals10 = [ f1_taylor(x, 10) for x in x_vals ]
    f1_taylor_vals20 = [ f1_taylor(x, 20) for x in x_vals ]
    f1_taylor_vals40 = [ f1_taylor(x, 40) for x in x_vals ]

    f2_taylor_vals10 = [ f2_taylor(x, 10) for x in x_vals ]
    f2_taylor_vals20 = [ f2_taylor(x, 20) for x in x_vals ]
    f2_taylor_vals40 = [ f2_taylor(x, 40) for x in x_vals ]

    # f1
    createPlot(x_vals, f1_analytic, f1_taylor_vals10, f1_taylor_vals20, f1_taylor_vals40, "f1(x) := 1 / (x - 1)", "f1")
    createPlot(x_vals, f2_analytic, f2_taylor_vals10, f2_taylor_vals20, f2_taylor_vals40, "f2(x) := 1 / (x² - 1)", "f2")

    # f2
    #createPlot(x_vals, f2_analytic, f2_taylor_vals10, "1 / (x² + 1); n=10", "f2_10")
    #createPlot(x_vals, f2_analytic, f2_taylor_vals20, "1 / (x² + 1); n=20", "f2_20")
    #createPlot(x_vals, f2_analytic, f2_taylor_vals40, "1 / (x² + 1); n=40", "f2_40")





import numpy as np
from math import exp, sqrt

def f1(x): return exp(x)
def f2(x): return sqrt(x)

def I_f1_analytic(a, b): return exp(b) - exp(a)
def I_f2_analytic(a, b): return 2.0 / 3.0 * x**(3/2)


# rules are transposed in respect to the exercise sheet
# [[c0, ... cn], [w0, ..., wn]]
trapezoidal =   [[0, 1], [0.5, 0.5]]
simpson =       [[0, 0.5, 1], [1.0/6.0, 2.0/3.0, 1.0/6.0]]
mid_point =     [[0.5], [1]]
double_gauss =  [[0.5 - 0.5/sqrt(3.0), 0.5 + 0.5/sqrt(3.0)], [0.5, 0.5]]


def integrate(f, a, b, m, rule):
    """ Integrate by summing up sub-intervals 
    sub-intervals are calculated using newton-cotes

    Args:
        f (fucntion): function to integrate
        a (float): lower bound
        b (float): upper bound
        m (int): number of subintervals used for integration
        rule ([[], []]): rules as defined above

    Returns:
        float: Numerical value of the integration
    """    
    x = np.linspace(a,b,m+1) # create m subintervals
    return sum( [integrate_subinterval(f, x[i], x[i+1], rule[0], rule[1]) for i in range(len(x)-1)] )


# Algorithm for integrating 1 sub-interval accoring to Dahmen 10.13
def integrate_subinterval(f, a, b, c, w):
    h = b - a
    return h*sum([w[j] * f(a + c[j]*h) for j in range(len(w))])



print(integrate(f1, 0, 1, 10, double_gauss))
print(I_f1_analytic(0,1))
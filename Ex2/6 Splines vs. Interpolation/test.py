from math import cos, pi
import numpy as np

# Function for generating Chebyshev Points
def chebyshev_points(start, end, count):
    # generate points in [0,1]
    pts = np.array([cos( (i+0.5)*pi / (2*count + 1)) for i in range(2*count)]) 
    pts = pts[0: int(count)]

    # map them from start to end
    k = float(end) - float(start)
    mapped_pts = [k*x for x in pts]

    return mapped_pts[::-1]



chebyshev_points(0,2, 10)


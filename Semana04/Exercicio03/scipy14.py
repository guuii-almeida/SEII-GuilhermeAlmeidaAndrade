import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import dblquad

integrand = lambda y, x: np.sin(x+y**2)
lwr_y = lambda x: -x
upr_y = lambda x: x**2
integral, integral_error = dblquad(integrand, 0, 1, lwr_y, upr_y)
print(integral)
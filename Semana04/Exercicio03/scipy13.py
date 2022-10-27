import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import quad

integrand = lambda x: x**2 * np.sin(2*x) * np.exp(-x)
integral, integral_error = quad(integrand, 0, 1)
print(integral)
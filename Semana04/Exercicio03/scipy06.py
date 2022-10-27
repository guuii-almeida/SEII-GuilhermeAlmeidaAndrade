import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import curve_fit

x_data = np.linspace(0, 10, 10)
y_data = 3*x_data**2 + 2
def func(x, a, b):
    return a*x**2 + b
popt, pcov = curve_fit(func, x_data, y_data, p0=(1,1))
print(popt)
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import minimize

x = np.linspace(0, 10, 10)
y = x**2 * np.sin(x)
plt.scatter(x,y)
plt.show()
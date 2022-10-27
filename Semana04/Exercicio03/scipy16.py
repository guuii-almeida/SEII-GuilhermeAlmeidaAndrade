import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint

def dSdx(S, x):
    y1, y2 = S
    return [y1 + y2**2  + 3*x,
           3*y1 + y2**3 - np.cos(x)]
y1_0 = 0
y2_0 = 0
S_0 = (y1_0, y2_0)
x = np.linspace(0, 1, 100)
sol = odeint(dSdx, S_0, x)
y1_sol = sol.T[0]
y2_sol = sol.T[1]
plt.plot(x, y1_sol)
plt.plot(x, y2_sol)
plt.show()
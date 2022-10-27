import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint

def dvdt(v, t):
    return 3*v**2 - 5
v0 = 0
t = np.linspace(0, 1, 100)
sol = odeint(dvdt, v0, t)
v_sol = sol.T[0]
plt.plot(t, v_sol)
plt.show()
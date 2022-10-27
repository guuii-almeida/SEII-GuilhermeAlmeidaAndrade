import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint

def dSdt(S, t):
    theta, omega = S
    return [omega,
           np.sin(theta)]
theta0 = np.pi/4
omega0 = 0
S0 = (theta0, omega0)
t = np.linspace(0, 20, 100)
sol = odeint(dSdt, S0, t)
theta, omega = sol.T
plt.plot(t, theta)
plt.show()
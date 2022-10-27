import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x = np.linspace(0, 10*np.pi, 100)
y = np.sin(2*np.pi*x) + np.sin(4*np.pi*x) + 0.1*np.random.randn(len(x))
plt.plot(x, y)
plt.show()
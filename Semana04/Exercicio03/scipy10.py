import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.special import legendre

x = np.linspace(0, 1, 100)
plt.plot(x, legendre(6)(x))
plt.show()
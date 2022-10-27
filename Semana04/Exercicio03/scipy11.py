import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.special import jv

x = np.linspace(0, 10, 100)
plt.plot(x, jv(3,x))
plt.show()
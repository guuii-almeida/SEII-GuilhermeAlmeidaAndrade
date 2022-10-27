import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import beta

a, b = 2.5, 3.1
mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
x = np.linspace(beta.ppf(0, a, b), beta.ppf(1, a, b), 100)
plt.plot(x, beta.pdf(x, a, b))
plt.show()
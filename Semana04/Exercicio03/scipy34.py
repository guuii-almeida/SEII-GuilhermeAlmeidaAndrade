import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import norm

mu = 1
sigma = 2
mean, var = norm.stats(loc=mu, scale=sigma, moments='mv')
x = np.linspace(norm.ppf(0.01, mu, sigma), norm.ppf(0.99, mu, sigma), 100)
plt.plot(x, norm.pdf(x, mu, sigma))
plt.show()
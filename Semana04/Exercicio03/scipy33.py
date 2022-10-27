import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import beta

a, b = 2.5, 3.1
mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
r = beta.rvs(a, b, size=10)
print(r)
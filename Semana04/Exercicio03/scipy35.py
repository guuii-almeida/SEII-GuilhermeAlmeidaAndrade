import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.stats import multinomial

p = np.ones(6)/6
print(multinomial.pmf([6,0,0,0,0,0], n=6, p=p))
print(multinomial.rvs(n=100, p=p, size=5))
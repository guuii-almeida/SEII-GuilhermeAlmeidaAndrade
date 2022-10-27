import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.linalg import lu

A = np.array([[2, 5, 8, 7], [5, 2, 2, 8], [7, 5, 6, 6], [5, 4, 4, 8]])
p, l, u = lu(A)
print(p,l,u)
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.linalg import solve_triangular

a = np.array([[3, 0, 0, 0],
              [2, 1, 0, 0],
              [1, 0, 1, 0],
              [1, 1, 1, 1]])
b = np.array([4, 2, 4, 2])
x = solve_triangular(a, b, lower=True)
print(x)
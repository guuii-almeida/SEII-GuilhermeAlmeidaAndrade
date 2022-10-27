import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.linalg import cholesky

A = np.array([[1,0.2],[0.2,1]])
C = cholesky(A, lower=True)
print(C)
print(C@C.T)
print(A)
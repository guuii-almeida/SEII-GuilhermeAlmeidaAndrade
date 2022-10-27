import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.linalg import eigh_tridiagonal

d = 3*np.ones(4)
e = -1*np.ones(3)
w, v = eigh_tridiagonal(d, e)
A = np.diag(d) + np.diag(e, k=1) + np.diag(e, k=-1)
print(A,'\n', A@v.T[0], '\n',w[0] * v.T[0])
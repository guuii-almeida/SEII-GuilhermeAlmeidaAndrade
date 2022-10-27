import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.linalg import kron # kronecker product, NOT sum

N= 5
d = -2*np.ones(N)
e = np.ones(N-1)
D = np.diag(d) + np.diag(e, k=1) + np.diag(e, k=-1)
D_kronsum = kron(D, np.identity(N)) + kron(np.identity(N),D)
print(D_kronsum)
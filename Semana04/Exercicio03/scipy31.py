import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import sparse

N=100
diag = np.ones([N])
diags = np.array([diag, -2*diag, diag])
D = sparse.spdiags(diags, np.array([-1,0,1]), N, N)
T = -1/2 * sparse.kronsum(D,D)
print(T)
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.fft import fft, fftfreq

x = np.linspace(0, 10*np.pi, 100)
y = np.sin(2*np.pi*x) + np.sin(4*np.pi*x) + 0.1*np.random.randn(len(x))
N = len(y)
yf = fft(y)[:N//2]
xf = fftfreq(N, np.diff(x)[0])[:N//2]
plt.plot(xf, np.abs(yf))
plt.show()
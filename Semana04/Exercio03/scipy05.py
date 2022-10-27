import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

x_data = np.linspace(0, 10, 10)
y_data = 3*x_data**2 + 2
plt.scatter(x_data, y_data)
plt.show()
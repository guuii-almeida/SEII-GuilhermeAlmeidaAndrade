import numpy as np

print(np.__version__)

a = np.array(array[1,2,3,4])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)

print(a[0])
a[0]=10
print(a)

b = a + np.array([2,0,2])
print(b)

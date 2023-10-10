import numpy as np

a = np.array([[1, 2],[4, -1]])
b = np.array([[2, -3],[-4, 1]])
c = a.dot(b) - b.dot(a)
print (c)
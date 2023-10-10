import numpy as np

a = np.array([[1, 2, 3, 4], [-2, 1, -4, 3], [3, -4, -1, 2], [4, 3, -2, -1]])
deter = np.linalg.det(a)
print(round(deter, 5))
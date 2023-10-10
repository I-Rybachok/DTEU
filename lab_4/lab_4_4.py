import numpy as np

a = np.array([[2, 3, 4], [1, 0, 6], [7, 8, 9]])
deter = np.linalg.det(a)
print(round(deter, 5))
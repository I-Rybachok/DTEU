import numpy as np

a = np.array([[2, 1, 0, 0], [3, 2, 0, 0], [1, 1, 3, 4], [2, -1, 2, 3]])
invers = np.linalg.inv(a)
print(invers)
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
import math

def func(x):
  return (math.e**(-x))+2*x
x = np.array([i * 0.1 for i in range(1, 11)])
y = np.array([func(xi) for xi in x])
print('x =', x)
print('y =', y)

#Наближення параболою
def fun(a, x, y):
  return a[0] + a[1] * x + a[2] * x**2 - y
a0 = np.array([1, 1, 1])
res_lsq = least_squares(fun, x0 = a0, args = (x, y))
print("a0 = %.2f, a1 = %.2f, a2 = %.2f" % tuple(res_lsq.x))
f = lambda x: sum([u * v for u, v in zip(res_lsq.x, [1, x, x**2])])
x_p = np.linspace(min(x), max(x), 20)
y_p = f(x_p)
plt.plot(x, y, 'o')
plt.plot(x_p, y_p, 'b')
plt.title("МНК (наближення параболою)")
plt.grid(True)
plt.show()
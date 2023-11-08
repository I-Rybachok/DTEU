import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import approximate_taylor_polynomial

# Задаємо функцію
def f(x):
    return 2 * np.sin(x)

#Будуємо багаточлен Тейлора за допомогою approximate_taylor_polynomial
x = np.linspace(-2.0, 2.0, num=400)

plt.figure(figsize=(10, 6))
plt.plot(x, f(x), label="f(x) curve", color='blue')
degree = 3

taylor = approximate_taylor_polynomial(f, 0, degree, 1)
print('taylor=', taylor)

plt.plot(x, taylor(x), label=f"degree={degree}", color='red', linestyle='--' )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left',borderaxespad=0.0, shadow=True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Графік функції та наближення ,багаточленами Тейлора")
plt.tight_layout()
plt.grid()
plt.show()
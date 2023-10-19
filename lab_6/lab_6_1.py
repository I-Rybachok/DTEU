import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# Функція для обчислення інтерполяційної функції Лагранжа
def lagrange_interpolation(x, y, x_test):
    n = len(x)
    p = np.zeros(n)
    for i in range(n):
        p_i = 1
        for j in range(n):
            if i != j:
                p_i *= (x_test - x[j]) / (x[i] - x[j])
        p[i] = p_i
    return np.dot(y, p)

# Задана функція
x = np.array([-2.,0.,2.,4.], dtype=float)
y = np.array([-5.,1.,-9.,13.], dtype=float)

f_interp_1 = lagrange_interpolation(x, y, -1.5)
f_interp_2 = lagrange_interpolation(x, y, -1)
f_interp_3 = lagrange_interpolation(x, y, 3)
f_interp_4 = lagrange_interpolation(x, y, 3.5)

print("Значення функції у заданій точці x =", f_interp_1)
print("Значення функції у заданій точці x =", f_interp_2)
print("Значення функції у заданій точці x =", f_interp_3)
print("Значення функції у заданій точці x =", f_interp_4)

#Точки, за якими будуємо графік
x_new = np.linspace(np.min(x),np.max(x),100)
y_new = [lagrange_interpolation(x, y, i) for i in x_new]

#Графік інтерполяційної функції Лагранжа
plt.plot(x, y, 'mo', x_new, y_new, 'g-')
plt.title('Інтерполяційний багаточлен Лагранжа')
plt.grid(True)
plt.show()

#Перевірка
f = lagrange(x, y)
fig = plt.figure(figsize = (7, 5))
plt.plot(x, y, 'bo', x_new, f(x_new), 'y-')
plt.title('Інтерполяційний багаточлен Лагранжа (перевірка)')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
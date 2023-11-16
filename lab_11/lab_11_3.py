#Обчислення інтегралу методом трапецій
from scipy import integrate 
import math

# Задаємо функцію, яку необхідно інтегрувати
def f(x):
    return 1 / math.sqrt(0.5 + x**2)

# Задаємо межі інтегрування та початкову кількість розбиттів
a = 1.2
b = 2.4
n = 20

# Обчислюємо значення інтегралу методом трапецій
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = a
    sum = 0
    for i in range(1, n):
        x += h
        sum += 2 * f(x)
    sum += f(b)
    integral = h / 2 * sum

    return integral

# Обчислюємо значення інтегралу методом трапецій з точністю 0.001
# Перевірка точності за правилом Рунге
integral1 = trapezoidal_rule(f, a, b, n)
integral2 = trapezoidal_rule(f, a, b, n * 2)
while abs(integral2 - integral1) / 3 > 0.001:
    integral1 = integral2
    integral2 = trapezoidal_rule(f, a, b, n * 2)

# Виводимо результат
print("Метод трапецій:", round(integral2, 7))

#Перевірка
v,err = integrate.quad(f, a, b)
print("Перевірка для методу трапецій =",round(v, 7))
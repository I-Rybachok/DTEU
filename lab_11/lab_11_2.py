#Обчислення інтеграла методом Симпсона
from scipy import integrate 
import math

# Задаємо функцію, яку необхідно інтегрувати
def f(x):
    return (math.sin(x**2 - 0.4)) / (x + 2)

# Задаємо межі інтегрування та початкову кількість розбиттів
a = 0.8
b = 1.2
n = 8

# Обчислюємо значення інтегралу методом Симпсона
def simpson_rule(f, a, b, n):
    h = (b - a) / n 
    integr = f(a) + f(b) 
    for i in range(1, n): 
        k = a + i * h 
        if i % 2 == 0: 
            integr += 2 * f(k) 
        else: 
            integr += 4 * f(k) 
    integr *= h / 3 
    return integr 

# Обчислюємо значення інтегралу методом Сімпсона з точністю 0.001
integral1 = simpson_rule(f, a, b, n)
integral2 = simpson_rule(f, a, b, n * 2)
while abs(integral2 - integral1) / 15 > 0.001:
    integral1 = integral2
    n *= 2
    integral2 = simpson_rule(f, a, b, n)

# Виводимо результат
print("Метод Сімпсона:", round(integral2, 7))

#Перевірка
v, err = integrate.quad(f, a, b)
print("Перевірка для методу Сімпсона =", round(v, 7))

from scipy import optimize
import math

# Задання початкових значень
x0 = 0.1
y0 = 0.7
delta = 0.001

# Задання функцій
def f1(x):
    return 0.8 - (1/2) * math.sin(x)
def f2 (y):
    return 1 - math.cos(y - 1)


# Метод ітерацій
def iter (x, y, delta):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1 - xn) >= delta) & (abs(yn1 - yn) >= delta)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print ('Метод ітерацій:')
    print ('x =', xn, '; y =', yn, '; кількість ітерацій =', n)
iter(x0, y0, delta)

#Перевірка розв'язку
def f3(x):
    return math.sin(x[0]) + 2 * x[1] - 1.6, math.cos(x[1] - 1) + x[0] - 1
s = optimize.root(f3, [0.,0.], method = 'hybr')
print ('Перевірка:', s.x)

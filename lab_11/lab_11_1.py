#Обчислення інтеграла методом прямокутників
from scipy import integrate 
import math
eps = 0.001
a = 1.4
b = 2.6
n = 10

def f(x): 
  return 1 / math.sqrt(1.5 * x + 0.2)
  
def left_rec(f, a, b, n):
  h = (b - a) / n
  sum = 0
  for i in range(0, n):
      sum += f(a + i * h)
  return sum * h

#Перевірка точності за правилом Рунге:
integral1 = left_rec(f, a, b, n)
integral2 = left_rec(f, a, b, n * 2)
if (integral2 - integral1) / 3 <= eps:
    print("Лівий прямокутник:",round (left_rec(f, a, b, n), 7)) 
    

def right_rec(f, a, b, n): 
    h = (b - a) / n 
    sum=0
    for i in range(1, n+1): 
        sum += f(a + i * h) 
    return sum * h 
print("Правий прямокутник:", round(right_rec(f, a, b, n), 7))

def aver_rec(f, a, b, n):
    h = (b - a) / n
    sum = 0 
    for i in range(0, n): 
        sum += f(a + i * h) 
    return sum * h 
print("Середній прямокутник:", round(aver_rec(f, a, b, n), 7))

#Перевірка
v, err = integrate.quad(f, a, b)
print("Перевірка для прямокутного методу =", round (v, 7))
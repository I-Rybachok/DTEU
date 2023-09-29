import numpy as np
import numdifftools as nd

eps=0.0001
def f(x):
  return 2 * pow(x, 4) + 4 * pow(x, 3) + pow(x, 2) + 3 * x - 6

#Відокремлення коренів (знаходимо відрізки)
def find_segments(): 
  search_range = np.arange(-10, 10, 1)
  
  previous_x = None
  current_x  = None
  segments = []

  for x in search_range:
    x = round(x, 4)
    current_x = f(x)
    if previous_x != None and (previous_x * current_x) < 0:
      segments.append((n, x))
    n = x
    previous_x = current_x
  return segments
segments = find_segments()
print('Отримані відрізки: ', segments)
    
# Метод Ньютона (метод дотичних)
def nuton(a, b, eps):
  df2 = nd.Derivative(f, n = 2)
  if (f(b) * df2(b) > 0):
    xi = b
  else:
    xi = a
  df1 = nd.Derivative(f)
  xi_1 = xi - f(xi) / df1(xi)
  while (abs(xi_1 - xi) > eps):
    xi = xi_1
    xi_1 = xi - f(xi) / df1(xi)
  return print ('x = ', xi_1, ' - Метод Ньютона (метод дотичних)')
  
# Комбінований метод
def comb(a, b, eps):
  df1 = nd.Derivative(f)
  df2 = nd.Derivative(f, n = 2)
  if (df1(a) * df2(a) > 0):
    a0 = a
    b0 = b
  else:
    a0 = b
    b0 = a
  ai = a0
  bi = b0
  while abs(ai - bi) > eps:
    ai_1 = ai - f(ai) * (bi - ai) / (f(bi) - f(ai))
    bi_1 = bi - f(bi) / df1(bi) 
    ai = ai_1
    bi = bi_1
  x = (ai_1 + bi_1) / 2
  return print('x = ', x, ' - Комбінований метод')

#Виведення результатів
a = -3
b = -2
a1 = 0
b1 = 1

print (f'Рішення нелінійного рівняння на відрізку [{a}, {b}]')
nuton (a,b,eps)
comb(a,b,eps) 

print (f'Рішення нелінійного рівняння на відрізку [{a1}, {b1}]')
nuton (a1,b1,eps)
comb(a1,b1,eps)
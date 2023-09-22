import numpy as np

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

#Метод половинного ділення

def half_division(a, b, eps): 
    while (abs(a - b) >= eps):
        if f(a) * f((a + b) / 2) < 0: 
            b = (a + b) / 2 
        else: 
            a = (a + b) / 2
        x = (a + b) / 2
    
    print ('x = ', round(x, 5), ' - Метод половинного ділення')

 #Метод хорд

def сhord(a,b,eps):
    
    x0 = a
    x = a - f(a) * (b - a) / (f(b) - f(a))
    
    if (f(a) * f(x) > 0):
        a = x
    else:
        b = x
        
    while (abs(x0 - x) > eps):
        x0 = x
        x = a - f(a) * (b - a) / (f(b) - f(a))
        if (f(a) * f(x) > 0):
          a = x
        else:
          b = x
          
    print('x = ', round (x, 5) , ' - Метод хорд')
    
#Виведення результатів

a = -3
b = -2
a1 = 0
b1 = 1

print (f'Рішення нелінійного рівняння на відрізку [{a}, {b}]')
half_division(a,b,eps) 
сhord(a,b,eps) 

print (f'Рішення нелінійного рівняння на відрізку [{a1}, {b1}]')
half_division(a1,b1,eps)
сhord(a1,b1,eps)
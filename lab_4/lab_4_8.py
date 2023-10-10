import numpy as np

a = np.array([[3, 2, 1], [2, -1, 1], [1, 5, 0]])
b = np.array([[5], [6], [-3]])

# Матричний метод 
def matr (a, b):
  a_invers = np.linalg.inv(a)
  result = a_invers.dot(b)
  print("Матричний метод: ")
  print(result)
  return result
  
matr(a, b)
# Метод Крамера
def kram(a,b):
    det_a = np.linalg.det(a)
    if det_a != 0:
       a1 = np.matrix(a)
       a2 = np.matrix(a)
       a3 = np.matrix(a)
       a1[:, 0] = b
       a2[:, 1] = b
       a3[:, 2] = b
       x = np.linalg.det(a1) / det_a
       y =np.linalg.det(a2) / det_a
       z= np.linalg.det(a3) / det_a
       print("Метод Крамера: ")
       print('x =', x.round(3), '; y =', y.round(3), '; z =', z.round(3))
    else:
      print('Визначник дорівнює нулю, система не має рішень')
    return x,y,z
kram(a,b)

# Перевірка за допомогою методу solve() пакету linalg
check = np.linalg.solve(a,b).round(3)
print ("Перевірка за допомогою методу solve() пакету linalg: ")
print(check)
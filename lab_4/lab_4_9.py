import numpy as np

# Користувач задає кількість рядків(n) та стовпчиків(m) і задається матриця m*n з випадковими числами від 1 до 99
n = int (input("Введіть кількість рядків(n): "))
m = int (input("Введіть кількість стовпчиків(m): "))
arr = np.random.randint(1, 100, (n, m))
print("Початкова матриця: ")
print(arr)

# Знаходимо середні значення у кожного рядка
arr_mean = np.mean(arr, axis = 1)
print("Середні значення всіх рядків: ")
print(arr_mean)

# Знаходимо мінімальне значення з усіх середніх значень рядків
min = arr_mean[0]

for i in range(len(arr_mean)):
  if arr_mean[i] < min:
    min = arr_mean[i]
  else:
    continue
print("Мінімальне значення з усіх середніх значень рядків: ")
print(min)
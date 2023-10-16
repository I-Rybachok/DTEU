import numpy as np
import matplotlib.pyplot as plt

# Область значень для x та y
x_min, x_max = -3, 3
y_min, y_max = -3, 3
step = 0.001

# Масиви значень x та y
x, y = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))

# Рівняння системи
eq1 = np.sin(x) + 2 * y - 1.6
eq2 = np.cos(y - 1) + x - 1

# Створення графіка
fig, ax = plt.subplots(figsize=(10, 10))

# Графік першого рівняння
ax.contour(x, y, eq1, levels=[0], colors='purple')

# Графік другого рівняння
ax.contour(x, y, eq2, levels=[0], colors='green')

# Налаштування графіка і його показ
ax.set_xlim([x_min, x_max])
ax.set_ylim([y_min, y_max])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Графік системи рівнянь')
plt.grid(True)
plt.show()

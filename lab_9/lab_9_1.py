import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Задаємо символьну змінну x та функцію f(x)
x = sp.symbols('x')
f = 2 * sp.sin(x)

# Знаходимо перші три похідні
f1 = sp.diff(f, x)
f2 = sp.diff(f1, x)
f3 = sp.diff(f2, x)

# Виводимо похідні
print("f'(x) =", f1)
print("f''(x) =", f2)
print("f'''(x) =", f3)

# Знаходимо значення функції та її похідних в точці x = 0
x0 = 0
f_x0 = f.subs(x, x0).evalf()
f1_x0 = f1.subs(x, x0).evalf()
f2_x0 = f2.subs(x, x0).evalf()
f3_x0 = f3.subs(x, x0).evalf()

# Обчислюємо значення многочлена Тейлора в точці x = 0
T = f_x0 + f1_x0*(x - x0) + (f2_x0 / 2) * (x - x0)**2 + (f3_x0 / 6) * (x - x0)**3

# Виводимо значення функції та її наближення за багаточленом Тейлора в точці x=0
print("f(0) =", f_x0)
print("f'(0) =", f1_x0)
print("f''(0) =", f2_x0)
print("f'''(0) =", f3_x0)
print("T(x) =", T.evalf())

# Будуємо графіки
x_vals = np.linspace(-2, 2, 1000)
f_vals = np.array([f.subs(x, xi).evalf() for xi in x_vals])
T_vals = np.array([T.subs(x, xi).evalf() for xi in x_vals])

fig, ax = plt.subplots()
ax.plot(x_vals, f_vals, label="f(x)")
ax.plot(x_vals, T_vals, label="T(x)")
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Графік функції та наближення многочленом Тейлора")
plt.grid(True)
plt.show()
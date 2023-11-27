#Розв’язок диф. Рівняння за допомогою scipy.integrate import odeint

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dx
def model(y,x):
    return x + np.cos(y/np.sqrt(0.7))

h = 0.1
# initial condition
y0 = 1.7
a = 0.8 # ліва межа відрізку, менша на 0.1
b = 1.9 # права межа відрізку

# x points
x = np.array ([i*h + a for i in range(1, 12)])

# solve ODE
y = odeint(model, y0, x)
print('x=', x)
print('y=',y)

# plot results
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Розв’язання диф. рівняння')
plt.grid() 
plt.show()

#Розв’язок диф. Рівняння за допомогою scipy.integrate import odeint

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dx
def model(y,x):
    return x + np.sin(y/np.sqrt(1.3))

h = 0.1
# initial condition
y0 = 0.8

# x points
x = np.array ([i*h for i in range(1, 12)])

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

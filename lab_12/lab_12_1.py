#Метод Ейлера для розв'язання диф. рівнянь
import numpy as np
import matplotlib.pyplot as plt 

def f(x, y):
    return x + np.sin(y/np.sqrt(1.3))

a = 0.1 # ліва межа відрізку
b = 1.1 # права межа відрізку
h = 0.1 # крок
y0 = 0.8 # початкова умова

n = int((b - a) / h) # кількість кроків

x = np.array ([i*h for i in range(1, 12)]) # задаємо x генератором списків

y=np.empty(n+1) 
y[0] = y0

for i in range (n):
    y[i+1]=y[i]+f(x[i],y[i])*h

y_rounded=np.round_(y,4) 
print("x=",x, "\ny=",y_rounded) 

plt.plot(x,y, "o",x,y, "red") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Метод Ейлера") 
plt.legend(["точки", "x + sin(y/sqrt(1.3)"]) 
plt.grid() 
plt.show()

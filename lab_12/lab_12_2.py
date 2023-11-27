#Метод Ейлера-Коші
import numpy as np
import matplotlib.pyplot as plt 

def f(x, y):
    return x + np.cos(y/np.sqrt(0.7))

a = 0.8 # ліва межа відрізку, менша на 0.1
b = 1.9 # права межа відрізку
h = 0.1 # крок
y0 = 1.7 # початкова умова
n = int((b - a) / h) # кількість кроків
x = np.array ([i*h + a for i in range(1, 12)]) # задаємо x генератором списків

y=np.empty(n+1) 
y[0] = y0
for i in range(n): 

     y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],y[i])+h*f(x[i],y[i]))*h/2 

y_rounded=np.round_(y,4)

print("x=",x, "\ny=",y_rounded) 
plt.plot(x,y, "o",x,y, "red")
plt.xlabel("x") 
plt.ylabel("y") 
plt.title("Метод Ейлера-Коші") 
plt.legend(["точки", "x + cos(y/sqrt(0.7))"]) 
plt.grid() 
plt.show()
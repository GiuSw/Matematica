import numpy as np 
import matplotlib.pyplot as plt

def f(t): 
    return np.sin(t)

x = np.linspace(-np.pi, np.pi, 1000)
a = 2

div_x = np.split(x, a)
x_max = np.array([])
y_max = np.array([])


x_min = np.array([])
y_min = np.array([])

# linee tratteggiate che separano gli intervalli 

for array in div_x[:-1]: 
    plt.axvline(np.max(array), color = "gray", linestyle = "--")


#calcolo dei minimi e dei massimi
for array in div_x: 
    y_max = np.append(y_max, np.max(f(array)))
    indice = np.argmax(f(array))
    x_max = np.append(x_max, array[indice])


for array in div_x: 
    y_min = np.append(y_min, np.min(f(array)))
    indice = np.argmin(f(array))
    x_min = np.append(x_min, array[indice])

#calcolo delle aree
aree_max = np.array([])
base = div_x[0][-1] - div_x[0][0]
for i in x_max:
    aree_max = np.append(aree_max, base * f(i))

# print(aree_max)
area = aree_max.sum()
print(area)
plt.plot(x, f(x), color = "red", label = "sin(x)")
plt.axhline(0)
plt.scatter(x_max, y_max, color = "green")
# plt.scatter(x_min, y_max, color = "blue")
plt.grid()
plt.legend()
plt.show()

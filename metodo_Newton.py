import numpy as np
import matplotlib.pyplot as plt 
from random import randint

def f(t): 
    return - t + np.sin(t) + 6

def dydx(t, h = 1e-7): 
    return (f(t + h) - f(t)) / h

estremo = 100
punti = 1000
x = np.linspace(-estremo, estremo, punti)

x0 = x[randint(0, punti-1)]
m0 = dydx(x0)
q0 = - dydx(x0)*x0 + f(x0)

tentativi = 100
eps = 1e-8
n_tentativi = []
sol = []


for i in range(1, tentativi +1 ): 
    x_new  = - q0 / dydx(x0)

    if abs (x_new - x0) < eps: 
        break 

    x0 = x_new
    q0 = - dydx(x0)*x0 + f(x0)
    m0 = dydx(x0)
    sol.append(x0)
    n_tentativi.append(i)

print(sol[-1])
sol = np.array(sol)
n_tentativi = np.array(n_tentativi)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(x, f(x), label = "f(x)", color = "navy")
ax1.scatter(sol, np.zeros_like(sol), color = "crimson")
ax1.axvline(color = "gray", linestyle = "--")
ax1.axhline(color = "gray", linestyle = "--")
ax1.set_xlim(-estremo, estremo)
ax1.grid()
ax1.legend()

ax2.plot(n_tentativi, sol, color = "green", marker = "x", label = "Convergenza soluzioni")
ax2.set_xticks(n_tentativi)
ax2.legend()
plt.show()
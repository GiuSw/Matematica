import matplotlib.pyplot as plt 
import numpy as np 
from scipy.optimize import curve_fit


f = open("dati.txt", "r")

t = []
v = []

for riga in f: 
    riga = riga.strip()
    riga = riga.split(";")
    t.append(float(riga[0]))
    v.append(float(riga[1]))

f.close()

t = np.array(t)
v = np.array(v)

v_inf = 5

def model_f(t, a, b):
    return v_inf + (a - v_inf) * np.exp(b * t)

popt, pcov = curve_fit(model_f, t, v, p0=[0.2, -1/1000])
a, b = popt

t_fit = np.linspace(min(t), max(t), 5000)


plt.plot(t_fit, 
        model_f(t_fit, a, b), 
        color = "crimson", 
        linewidth = 2, 
        zorder = 1, 
        label = r"Modello di fitting $a \cdot e^{-b \cdot t}$"
        )

plt.scatter(
    t, 
    v, 
    marker = "*", 
    s = 10,
    color = "royalblue", 
    zorder = 2, 
    label = "Dati campionati"
)

plt.grid(True, linestyle = ":")
plt.title("Retta di fitting calcolata con scipy.optimize", fontweight = "bold")
plt.xlabel("Tempo [ms]")
plt.ylabel("Tensione [V]")
plt.legend(loc = "lower right")
plt.tight_layout()

plt.show()
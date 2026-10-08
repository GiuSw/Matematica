import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.widgets import Cursor


x = np.linspace(1e-14, 1, 10000)
x_deg = x * 180 / np.pi
y1 = np.sin(x)
y2 = x

rap = y1/y2
limite = 1

fig1, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(x_deg, y1, color = "red", label = r"$y = sin(x)$")
ax1.plot(x_deg, y2, color = "blue", label = r"$y = x$") 
ax1.set_xlabel("Gradi = (0, 57.29°]")

ax1.legend()


ax2.plot(x_deg, rap, color = "orange", label = r"$f(x) = \frac{sin(x)}{x}$")
ax2.grid()
ax2.set_xlabel("Gradi = (0, 57.29°]")
plt.tight_layout()


fig2, ax3 = plt.subplots(1, 1)

errAss = np.abs(limite - rap)
errRel = (errAss / limite) * 100

erroreMininimo = 1
idxMin = np.argmin(np.abs(errRel - erroreMininimo))

ax3.semilogy(x_deg, errRel, label = "Errore relativo percentuale al variare di x")
ax3.scatter(x_deg[idxMin], errRel[idxMin], color = "crimson", label = f"Errore relativo del {erroreMininimo}%, deg = {x_deg[idxMin]:.2f}°", zorder = 2)

ax3.legend()
ax3.set_ylabel("%")
ax3.set_xlabel("Gradi = (0, 57.29°]")
ax3.grid()
plt.tight_layout()

ax2.scatter(x_deg[idxMin], rap[idxMin], color = "crimson", label = f"f({x_deg[idxMin]:.2f}°) = {rap[idxMin]:.8f}", zorder = 2)
ax2.legend(fontsize = 10)



cursor1 = Cursor(ax3, useblit=True, color='red', linewidth=1)
cursor2 = Cursor(ax2, useblit=True, color='red', linewidth=1)

# facendo i conti con lo sviluppo di taylor del seno, apporssimeto fino o(x3), calcolando l'errore relativo con il seno approssimato all'ordine 3
# (massimo impostato a 0,01)
# possiamo porre x = sqrt(6 * err) e trovare la x massima per raggiungere quell'errore che è circa 14

# ANALITCAMENTE CORRETTO QUELLOS CRITTO SOPRA ORA FAI I CALCOLI CON PYTHON SOTTRAENDO DAL VETTORE L'ERRRORE E TROVANDO LA POSIZIONE DI ZERO 
plt.show()
import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import quad

# definizione di estremi di integrazione e funzione integranda 
a = 0
b = np.pi
punti = 1000

x = np.linspace(a, b, punti)

def f(t): 
    return np.sin(t)


# calcolo del numero di rettangoli 
divisori = []
for i in range(1, punti+1): 
    if punti %  i == 0: 
        divisori.append(i)

aree_massimi_tot = np.array([])
aree_minimi_tot = np.array([])


# SOSTITUISCI CON L'INTEGRAZIONE DI SCIPY 
area_esatta, errore = quad(f, a, b)


# calcolo delle aree con iterazioni
for div in divisori: 

    div_x = np.split(x, div)
    
    x_max = np.array([])
    y_max = np.array([])

    x_min = np.array([])
    y_min = np.array([])


    #calcolo dei minimi e dei massimi
    for array in div_x: 
        y_max = np.append(y_max, np.max(f(array)))
        indice = np.argmax(f(array))
        x_max = np.append(x_max, array[indice])

    for array in div_x: 
        y_min = np.append(y_min, np.min(f(array)))
        indice = np.argmin(f(array))
        x_min = np.append(x_min, array[indice])

    # calcolo delle aree dei rettangoli con altezza pari ai minimi e massimi
    area_rett_max = np.array([])
    area_rett_min = np.array([])

    base = (b-a)/div

    for i in x_max:
        area_rett_max = np.append(area_rett_max, base * f(i))

    for i in x_min: 
        area_rett_min = np.append(area_rett_min, base * f(i))

    somme_superiori = area_rett_max.sum()
    somme_inferiori = area_rett_min.sum()

    aree_massimi_tot = np.append(aree_massimi_tot, somme_superiori)
    aree_minimi_tot = np.append(aree_minimi_tot, somme_inferiori)



#calcolo degli errori e delle iterazioni 
err_massimo = (np.abs(aree_massimi_tot - area_esatta) / area_esatta)*100
err_minimo = (np.abs(aree_minimi_tot - area_esatta) / area_esatta)*100

n_iterazioni = np.arange(1, len(err_massimo)+1)


# subplot della funzione integranda e dell'errore relativo in funzione dei tentativi
fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(x, f(x), label = "sin(x)")
ax1.set_title("Funzione Integranda")
ax1.grid()
ax1.legend()

ax2.plot(n_iterazioni, err_massimo, color = "red", linestyle = "--", label = "Err. massimo")
ax2.plot(n_iterazioni, err_minimo, color = "orange", linestyle = "--", label = "Err. minimo")
ax2.set_title("Errore relativo percentuale delle somme superiori e inferiori")
ax2.legend()
ax2.set_xticks(n_iterazioni)
ax2.yaxis.set_major_formatter("{x:.0f}%")
ax2.set_xlabel("n. iterazioni")
plt.tight_layout()
plt.show()

print(aree_massimi_tot)
print(aree_minimi_tot)
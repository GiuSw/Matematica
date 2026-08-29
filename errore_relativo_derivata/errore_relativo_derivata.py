import numpy as np 
import matplotlib.pyplot as plt

# QUESTO CODICE HA LO SCOPO DI DIMOSTRARE QUAL E' IL VALORE DI 
# H MIGLIORE PER CALCOLARE LA DERIVATA  

def f(t): 
    return np.sin(t)

def dfdx(t): 
    return np.cos(t)


array_err = []

x = np.linspace(-np.pi, np.pi, 1000)
derivata_esatta = dfdx(x)
norma_derivata_esatta = np.linalg.norm(derivata_esatta, ord=2)

n_iterazioni = 20 

for i in range(n_iterazioni): 
    h = 10.0 ** (-i)
    derivata_numerica = (f(x+h) - f(x)) / h
    err = np.abs(np.linalg.norm(derivata_esatta - derivata_numerica, ord=2))/norma_derivata_esatta
    err = err * 100
    array_err.append(err)
    print(err)

array_err = np.array(array_err)
idx_min = array_err.argmin()

x_min = idx_min
y_min = array_err[idx_min]


plt.semilogy(np.arange(0, len(array_err)), array_err, color = "crimson", marker = "o", label = "Errore relativo percentuale")
plt.title("Errore relativo della derivata in norma 2 al variare di h \n funzione di riferimento: sin(x)")
plt.grid()
plt.legend()
plt.xticks(np.arange(0, n_iterazioni))
plt.xlabel("h^-i")
plt.ylabel("%")

plt.annotate(
    f'Err = {y_min:.2e}%',
    xy=(x_min, y_min),                       # Punto esatto a cui punta la freccia (x, y)
    xytext=(x_min + 3, y_min * 50),       # Posizione del testo (in scala logaritmica su Y)
    arrowprops=dict(
        facecolor='black', 
        shrink=0.08, 
        width=1, 
        headwidth=6
    ),
    fontsize=9,
    fontweight='bold'
)
plt.tight_layout()



plt.show()


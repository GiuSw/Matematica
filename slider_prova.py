import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Dati noti
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 2, 5, 4])

# Creazione dell'interpolatore
cs = CubicSpline(x, y)

# Valutazione su nuovi punti più densi
x_new = np.linspace(0, 4, 50)
y_new = cs(x_new)

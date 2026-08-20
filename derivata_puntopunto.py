import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider 
import numpy as np


x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)
dydx = np.gradient(y, x)
x0 = np.pi/4
idx = np.argmin(np.abs(x - x0))

def ytan(indice, array, punto): 
    return dydx[indice] * (array - punto) + y[indice]



fig, ax = plt.subplots()

l1, = ax.plot(x, y, label = "f(x)") 
l2, = ax.plot(x, ytan(idx, x, x0), linestyle = "--", label = "y - y0 = f'(x) * (x - x0)")
l3, = ax.plot(x0, np.sin(x0), "o", label = "Punto di tangenza")
plt.legend()
plt.grid()
plt.subplots_adjust(bottom=0.25)
axslider = plt.axes([0.25, 0.1, 0.65, 0.03])


slider = Slider(
    ax=axslider ,
    label = "ascissa", 
    valmin=-0,
    valmax=2*np.pi, 
    valinit=x0,
)

def upgrade(val): 
    x0 = slider.val
    idx = np.argmin(np.abs(x - x0))
    l2.set_ydata(ytan(idx, x, x0))
    l3.set_data(x0, np.sin(x0))
    fig.canvas.draw_idle()


slider.on_changed(upgrade)
plt.show()
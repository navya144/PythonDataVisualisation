import matplotlib.pyplot as plt  #to import matplotibs plotting function
import numpy as np  #to import numpy for its utility function

plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "black",
    "axes.facecolor": "white",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black"})

x = np.linspace(0, 20)              # max value of the axis
y1 = np.sin(x)
y2 = np.sin(x - np.pi)
 
plt.figure()
 
plt.plot(x, y1)
plt.plot(x, y2)

plt.savefig('show.png', dpi=150)

plt.show()
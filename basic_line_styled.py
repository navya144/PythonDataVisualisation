import matplotlib.pyplot as plt  #to import matplotibs plotting function
import numpy as np  #to import numpy for its utility function

x = np.linspace(0, 20)              # max value of the axis
y1 = np.sin(x)
y2 = np.sin(x - np.pi)
 
plt.figure()

plt.plot(x,
        y1,
        color='black',
        linestyle='-',
        linewidth=2,
        marker='s',
        markersize=6,
        label='y1')
 
plt.plot(x,
        y2,
        color='gray',
        linestyle='--',
        linewidth=2,
        marker='^',
        markersize=6,
        label='y2')
 
plt.legend()

plt.savefig('show.png', dpi=150)

plt.show()
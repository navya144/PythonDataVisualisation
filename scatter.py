import matplotlib.pyplot as plt  #to import matplotibs plotting function
import numpy as np  #to import numpy for its utility function

x = range(20)
y = np.arange(50, 70) + (np.random.random(20) * 10.)            # generate some random numbers to plot

plt.figure()
plt.scatter(x, y)                                   # x and y are the two variables - axes

plt.savefig('show.png', dpi=150)

plt.show()          
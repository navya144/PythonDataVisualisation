import matplotlib.pyplot as plt
import numpy as np

#Optional:
#Setting the state of the pseudo-random number generator
#to a fixed value for reproducibility - will give random, different results each time if disabled
np.random.seed(13)

column_data = np.random.normal(42, 3, 1000)             # generate some random x values to plot on the histogram
plt.figure()
plt.hist(column_data)

plt.savefig('show.png', dpi=150)
plt.show()   
import matplotlib.pyplot as plt
import numpy as np

#Optional:
#Setting the state of the pseudo-random number generator
#to a fixed value for reproducibility - will give random, different results each time if disabled
np.random.seed(13)

two_columns_data = [np.random.normal(57, 3, 1000),              # random x values to plot in 3 box plots
np.random.normal(42, 7, 1000), np.random.normal(50, 6, 1000)]
plt.boxplot(two_columns_data)

plt.savefig('show.png', dpi=150)
plt.show()   
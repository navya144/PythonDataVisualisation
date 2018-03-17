import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2016)
 
plt.figure()
 
for category_num in range(1, 17):
    y_vals = np.arange(10, 16) + (np.random.random(6) * category_num / 4.)
    plt.plot(years, y_vals)
    plt.ylim(10, 18)
    plt.xticks(years, [str(year) for year in years])

plt.show()
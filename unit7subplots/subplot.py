import matplotlib.pyplot as plt
import numpy as np

# Allows you to place multiple charts in a figure
# matplotlib function: subplot(nrows, ncols, plot_number)

plt.figure()
 
for i in range(1, 7):
    plt.subplot(3, 2, i)
    plt.title(i)
    plt.xticks([])
    plt.yticks([])
 
plt.tight_layout()

plt.show();
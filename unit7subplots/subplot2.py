import matplotlib.pyplot as plt
import numpy as np

dist1 = np.random.normal(42, 7, 1000)
dist2 = np.random.normal(59, 3, 1000)
 
plt.figure(figsize=(10, 4))
 
plt.subplot(1, 2, 1)
plt.hist(dist1)
plt.title('dist1')
 
plt.subplot(1, 2, 2)
plt.scatter(dist2, dist1)
plt.xlabel('dist2')
plt.ylabel('dist1')

plt.show() 
plt.tight_layout()
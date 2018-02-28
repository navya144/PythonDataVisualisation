import matplotlib.pyplot as plt  #to import matplotibs plotting function
import numpy as np  #to import numpy for its utility function

categories = ['A', 'B', 'C', 'D', 'E']          # name categories - bars
values = [7, 12, 4, 2, 9]                       # the value of each bar
 
plt.figure()
 
plt.barh(np.arange(len(categories)), values)        # plotting the chart
 
plt.yticks(np.arange(len(categories)),                              # label the bars  - yticks sets location of labels
         ['Category {}'.format(x) for x in categories])

plt.savefig('show.png', dpi=150)

plt.show()
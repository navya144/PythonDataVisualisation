import matplotlib.pyplot as plt  #to import matplotibs plotting function
import numpy as np  #to import numpy for its utility function

years = np.arange(2012, 2015)   # years from 2012 to 2015
values = [2, 5, 9] 

plt.figure() 
plt.bar(years, values) 
plt.savefig('show.png', dpi=150)

plt.show()

# second example
years = np.arange(2012, 2015)
category1_values = [2, 5, 9]
category2_values = [7, 6, 3]
 
plt.figure()
 
plt.bar(years - 0.2,                # 0.2 is distance between the two category bars, if it was 0, the bars would be on top of each other
       category1_values,
       color='purple',
       edgecolor='none',
       width=0.4,
       align='center',
       label='y1')
 
plt.bar(years + 0.2,
       category2_values,
       color='orange',
       edgecolor='none',
       width=0.4,
       align='center',
       label='y2')
 
plt.xticks(years, [str(year) for year in years])
 
plt.legend()

plt.show()
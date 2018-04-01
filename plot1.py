# Just some values that we'll be using in the examples below
x1_values = [2012, 2013, 2014, 2015]
y1_values = [4.3, 2.5, 3.5, 4.5]
 
x2_values = [2012, 2013, 2014, 2015]
y2_values = [2.4, 4.4, 1.8, 2.8]
 
x3_values = [2012, 2013, 2014, 2015]
y3_values = [2, 2, 3, 5]

import matplotlib.pyplot as plt

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
 
# include the values from the above segment here 
plt.figure()
plt.plot(x1_values, y1_values, label='Python')
plt.plot(x2_values, y2_values, label='JavaScript')
plt.plot(x3_values, y3_values, label='R')
 
plt.xlim(2012, 2015)
plt.ylim(1, 5)
plt.xticks([2012, 2013, 2014, 2015], ['2012', '2013', '2014', '2015'])
plt.yticks([1, 2, 3, 4, 5])
 
plt.xlabel('')
plt.ylabel('Web Searches')
 
plt.legend(loc='upper center', ncol=3)
plt.grid()

plt.savefig('web-searches.png', dpi=150)
 
plt.show()
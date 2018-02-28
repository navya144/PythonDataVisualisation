import matplotlib.pyplot as plt  #to import matplotibs plotting function
import numpy as np  #to import numpy for its utility function

#first example
counts = [17, 14, 23]           # the numbers of the different sections e.g. 14 units and 17 units, if 14 and 14, would be equal halves in pie
plt.figure()
plt.pie(counts)

plt.savefig('show.png', dpi=150)

plt.show()                              # if more than 2 figures in one file, plt.show() must be done once for each figure

#second example
counts = [17, 14]
plt.figure(figsize=(4, 4))              # figsize = 4 and 4 - equal numbers will ensure perfect circle pie chart
plt.pie(counts)

plt.savefig('show.png', dpi=150)

plt.show()

#third example - with numbers
counts = [17, 14]
plt.figure(figsize=(4, 4))
plt.pie(counts,
colors=['blue', 'orange'],
labels=['Category A', 'Other categories'],
startangle=90,
autopct='%1.1f%%')
plt.savefig('show.png', dpi=150)
plt.show()
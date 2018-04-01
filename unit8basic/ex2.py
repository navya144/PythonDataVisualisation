#Practice 2: Write a Python program to draw line charts of the financial data of
#Alphabet Inc. between October 3, 2016 to October 7, 2016.
import matplotlib.pyplot as plt
import csv 

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

with open('fdata.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

dates = []
o = []
h = []
l = []
c = []

for i in range(1, len(your_list)):
    dates.append(your_list[i][0])
    o.append(your_list[i][1])
    h.append(your_list[i][2])
    l.append(your_list[i][3])
    c.append(your_list[i][4])

plt.plot(dates, o)
plt.plot(dates, h)
plt.plot(dates, l)
plt.plot(dates, c)

plt.legend()

plt.show()
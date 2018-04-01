#Practice 1: Write a Python program to draw a line with suitable label in the x axis, y axis and a title. 
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

plt.figure()

y_values = [0, 30, 60, 90, 120, 150]
x_values = [0, 10, 20, 30, 40, 50]
plt.xlim(0, 50)
plt.ylim(0, 160)

plt.plot(x_values, y_values)

plt.xticks([0, 10, 20, 30, 40, 50])

plt.xlabel('x - axis')
plt.ylabel('y - axis2')

plt.title('Draw a line.')

#plt.show()

# more efficient solution:

plt.figure()

x = range(1, 50)
y = [value * 3 for value in x]

plt.plot(x, y)

plt.xlabel('x - axis')
plt.ylabel('y - axis2')

plt.title('Draw a line.')

plt.show()




from matplotlib import pyplot as plt
from matplotlib import style
 
style.use('ggplot')
 
x = [5,8,10]                        # location of bar on x-axis
y = [12,16,6]                       # height of bar
 
x2 = [6,9,11]
y2 = [6,15,7]
 
plt.bar(x, y, align='center')                       # bar instead of plot
 
plt.bar(x2, y2, color='g', align='center')
 
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
 
plt.show()
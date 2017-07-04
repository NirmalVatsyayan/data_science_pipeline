'''
A simple scatter plot, where we give x and y axis points
x and y axis list should be same length.

A data point is created on combination of point, the name of
all data points could be given by variable label

mutiple scatter plots could also be plotted in same graph

'''

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='data points', color='k', s=25, marker="o")

plt.scatter([3,5,6,7,8,9,6], [4,5,6,2,2,3,4], label='new data', color='b', s=23, marker='o')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
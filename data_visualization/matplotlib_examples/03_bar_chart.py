'''
A simple bar chart
both x and y axis are data input from user

If you dont select a color then default color will
be used with both bar which will e confusing
'''

import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')

plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.title('Epic Graph\nBar chart comparison! Whoa')

plt.show()
'''
A simple example to load data from file using numpy and plotting it using matplotlib
'''
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('text_example_files/example.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

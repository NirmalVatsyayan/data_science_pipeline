'''
http://matplotlib.org/basemap/users/download.html
http://www.lfd.uci.edu/~gohlke/pythonlibs/ || download wheels
'''

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='mill')
m.drawcoastlines()
plt.show()

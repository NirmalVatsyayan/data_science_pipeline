'''
Pie charts are very much similar to stack plots but only for a certain period of time
Mostly used to show %share of each variable

Slices are the weight of each activities
cols is the color of each slice
Shadow just to make chart beautiful
Start angle is the angle to start for first division

Explode is to make a particular slice a bit exploded. We have normal size
of all slice except eating

we do autopct to optionally overlay the percentages on to the graph itself.
Here in autopct we could give how many numbers after decimal we want etc
'''
import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0),
        autopct='%1.2f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()
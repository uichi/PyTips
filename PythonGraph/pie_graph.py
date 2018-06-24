import numpy as np
import matplotlib.pyplot as plt
 
x = np.array([10, 20, 30, 40, 50])
plt.pie(x)

label = ["Apple", "Banana", "Orange", "Grape", "Strawberry"]
plt.pie(x, labels=label)

plt.pie(x, labels=label, counterclock=False, startangle=90)

plt.pie(x, labels=label, counterclock=False, startangle=90)
plt.axis('equal')

fig = plt.figure()
fig.patch.set_facecolor('white')
plt.pie(x, labels=label, counterclock=False, startangle=90)

plt.pie(x, labels=label, counterclock=False, startangle=90, explode=[0.2, 0, 0, 0, 0])

colors = ["lightpink", "yellow", "gold", "slateblue", "lightcoral"]
plt.pie(x, labels=label, counterclock=False, startangle=90, colors=colors)



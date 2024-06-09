import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
minSalary = 20000
maxSalary = 80000
numberOfEntries = 100
low=21
high=65
# this is so that the "random" numbers are the same each time to make it easier t o debug.
np.random.seed(1) 
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low, high, size = numberOfEntries)
 # I don’t like this, I prefer having absolute values set at the top
plt.scatter(ages, salaries, label="salaries")
#plt.show() 
# if you do this the proram will halt here until the plot is closed 
# add x squared 
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints
# multiply each entry by itself 
plt.plot(xpoints, ypoints, color='r', label = "x squared") 
plt.title("random plot") 
plt.xlabel("Salaries") 
plt.ylabel("age") 
plt.legend()
plt.savefig('prettier-plot.png')
plt.show()
# see how the axis have changed 
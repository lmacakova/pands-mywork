import numpy as np
import matplotlib.pyplot as plt

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1)
# this is so that the "random" numbers are the same each time t o make it easier to debug. 
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
plt.hist(salaries)
plt.show()
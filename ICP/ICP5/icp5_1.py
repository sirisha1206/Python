import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])



#mean value of x and y
meanOfX = sum(x)/len(x)
meanOfy = sum(y)/len(y)

#calculating slope
slope = np.sum((x - meanOfX)*(y - meanOfy))/np.sum(np.square(x-meanOfX))
#calculating intercept
intercept = meanOfy - (slope * meanOfX)
#y output
yOutput = (slope * x) + intercept
plt.plot(x,y)  # plotting the line made by linear regression
plt.plot(x, yOutput)
plt.show()
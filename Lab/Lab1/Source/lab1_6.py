import numpy as np #importing numpy module
ranVector = np.random.random_integers(20,size=15)#generate random vector between 0-20 of size 15
print('Vector with random numbers :',ranVector)
print('Most frequent item in the list :',np.bincount(ranVector).argmax())#get the frequent number using bincount().argmax()
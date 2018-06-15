import numpy as np
N=10  #dimensions of the array
arr = np.random.random((N,N)) #generating the random 10 X 10 array
print(arr)
print(np.min(arr,axis=1)) #finding minimum of each row
print(np.max(arr,axis=1)) #finding maximum of each row
#print(np.min(arr,axis=0))
#print(np.max(arr,axis=0))
import numpy as np
#implementing binary operators in numpy
a=np.array([[1,2], 
            [3,4]])
b=np.array([[4,3], 
            [2,1]])
#add arrays
print("Array sum: \n", a+b)
print("Array Multiplication:\n", a*b)
print("Array Matrix:\n", a.dot(b))
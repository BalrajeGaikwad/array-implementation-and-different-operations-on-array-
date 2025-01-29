#Program: Remove duplicates from a 2D array

import numpy as np

array=np.array([[1,2,3],
                [4,3,5],
                [6,2,7]])

flattened=array.flatten()

unique_elements=np.unique(flattened)

print(array)
print(flattened)
print(unique_elements)
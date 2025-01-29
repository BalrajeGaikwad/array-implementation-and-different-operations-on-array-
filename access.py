#Accessing element of 2D array

import numpy as np

array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
element=array[1,2]

print("Element at row 1, column 2 :", element)

element1=array[1,1]
print("Element at row 1, column 1 :", element1)


for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        print(f"Element at row {i}, columns {j} : {array[i,j]}")



column=array[:,2]
print("cplumn 2 :",column)
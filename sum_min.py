import numpy as np

array=np.array([[1,2,3],[4,5,6],[7,8,9]])


sum_all=np.sum(array)

mean_all=np.mean(array)


sum_columns=np.sum(array, axis=0)

sum_rows=np.sum(array, axis=1)

print(array)
print("sum of all elements: ",sum_all)
print("mean of all elements: ",mean_all)

print("sum of columns: ",sum_columns)
print("sum of rows :", sum_rows)
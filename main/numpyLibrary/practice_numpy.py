import numpy as np

# -----------------------
print(np.__version__) # check numpy version

# -----------------------
array_1 = np.array([1,2,3,4])
print(array_1, ", array type : " , type(array_1))

# -----------------------
# the length of arrays is equals, otherwise comming a error
arr_1 = np.array([10,20,30])
arr_2 = np.array([20,10,40])

# addition
print(arr_1+arr_2)

# substraction
print(arr_1-arr_2)

# multiplication
print(arr_1*arr_2)

# division
print(arr_1/arr_2)



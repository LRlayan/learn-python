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

# square root
print(np.sqrt(arr_1))

# summation
print(np.sum(arr_1))

# mean (Average)
print(np.mean(arr_1))

# min
print(np.min(arr_1))

# max
print(np.max(arr_1))

# -----------------------
# 2D arrays
arr_3 = np.array([[10,20,30],[5,8,6]])
print(arr_3)
print(arr_3.size)
print(arr_3.shape) # (2, 3) 2-> the 2D array has two 1D arrys / 3-> one 1D array has 3 elements

# -----------------------
# 3D array
arr_4 = np.array([[[10,20,30],[20,10,30]],[[100,50,150],[50,100,50]]])
print(arr_4)
print(arr_4.size)
print(arr_4.shape) # (2, 2, 3)
# (2, 2, 3)
# 2 -> the 3D array has two 2D arrays
# 2 -> the 2D array has two 1D arrays
# 3 -> the 1D array has 3 elements

# -----------------------

# shape attribute
#   > This property returns the dimension as a tuple in an array.

# -----------------------
# dtype
array = np.array([10,20,30])
print(array.dtype) #int64
# the result varies depending on the bit of computer

# -----------------------
# ndim
array = np.array([10,20,30])
print(array.ndim) # 1-> 1D array

array_2 = np.array([[1,2,3],[10,20,30]])
print(array_2.ndim) # 2-> 2D array

# -----------------------
# index
array_3 = np.array([[[4,3,6],[7,8,9]],[[1,2,3],[4,5,6]]])
print(array_3[0]) # [4,3,6],[7,8,9]
print(array_3[0,1]) # [7,8,9]
print(array_3[1,0]) # [1 2 3]

# -----------------------




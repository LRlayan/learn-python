# 1. creat a 1D numpy array with value 1 to 20
# use boolean index into extract all even numbers
# 2. create a 1D numpy array with elements 10,20,30,40,50 use boolean index into extract all element greater than mean(madyanya) of the array

import numpy as np

# answer 1
array = np.array([range(1,21)])

# answer 2
extract_even_numbers = array[array%2==0]
print(extract_even_numbers) # [ 2  4  6  8 10 12 14 16 18 20]

# answer 3
array_1 = np.array([10,20,30,40,50,60])
filtered_element = array_1[np.mean(array_1) < array_1]
print(filtered_element) # [40 50 60]
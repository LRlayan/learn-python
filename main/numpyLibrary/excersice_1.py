# 1.create a 2d numpy array which has dimensions 4 ^ 5 which contains the numbers 1 to 20
# 1.2 . perform the following on this array 
    # 1.add 10 to every element
    # 2.mulitiply every element by 2
    # 3.calulate square of each element
    
import numpy as np
import math as m

array = np.array(
    [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20]
    ]
)

# answer 1
print(array+10)
# answer 2
print(array*2)
# answer 3
print(array**2)
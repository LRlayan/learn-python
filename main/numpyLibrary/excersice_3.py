import numpy as np

def filter_temperature():
    array = np.array(
        [
            [12,15,85,45,32,16,95,48,25,74,36,12,95,44,11,22,33,66,32,21],
            [10,8,3,23,52,30,15,74,12,9,7,26,32,84,45,47,44,19,91,20],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            [15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],
            [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
            [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70],
            [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],
        ]
    )
    
    filter_below_15C = array[array < 15]
    print("Filter temperature 15C below : ",filter_below_15C)
    
    higher_temperature = array[array >= 15]
    return higher_temperature
    

result = filter_temperature()
print("Filter temperature 15C or Higher 15C : " ,result)
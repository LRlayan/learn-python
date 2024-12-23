# write a python program with the following requirement
# 1. create a decorator check positive
    # i. check if the input must be a positive number
    # ii. if the input is a not positive print a message line input must be a positive number
# 2. use this decrator one function calculate square_root that 
    # i. case one number input
    # ii. return the square_root of the input number

import math as m    

def check_positive(function):
    def inner(number):
        if number > 0:
            return function(number)
        else:
            print("input must be a positive number!")
            return None
    return inner

@check_positive
def calculate_the_squareRoot(number):
    return m.sqrt(number)

print(calculate_the_squareRoot(10))
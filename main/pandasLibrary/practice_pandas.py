import pandas as pd

# how to create Dataframe using python dictionary
data = {
    'name':['Alice','John'],
    'age':[23,28]
}

data = pd.DataFrame(data)
print(data)
    # name  age
# 0  Alice   23
# 1   John   28
# 0,1 is the normal default index for identifying rows, you can change this index if you want. 


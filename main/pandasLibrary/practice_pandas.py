import pandas as pd

# how to create Dataframe using python dictionary
data = {
    'Name':['Alice','John'],
    'Age':[23,28]
}

data_frame = pd.DataFrame(data)
print(data_frame)
    # name  age
# 0  Alice   23
# 1   John   28
# 0,1 is the normal default index for identifying rows, you can change this index if you want. 

# ---------------------------
# how to get data in rows
# You can get the value in relevent to the row index of header
print(data_frame.loc[1,'Name']) # John

# You can get the value in relevent to the row and colomn index
print(data_frame.iloc[1,0]) # John
print(data_frame.iloc[1,1]) # 28

# you can get the value in relevent to the row index
print(data_frame.loc[1]) 
# name    John
# age       28
# Name: 1, dtype: object

print(data_frame.loc[0].Name) # Alice
print(data_frame.loc[0].Age) # 23

# multiple rows can returns
print(data_frame.loc[[0,1]])
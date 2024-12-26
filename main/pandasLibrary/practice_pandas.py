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

# ----------------------------
# how to refactor row index

data = {
    'calories':[420,253,562],
    'duration':[50,10,30]
}

data_frame_2 = pd.DataFrame(data,index=["day1","day2","day3"])
print(data_frame_2)
#       calories  duration
# day1       420        50
# day2       253        10
# day3       562        30

# ----------------------------
# how to get data in columns
# it is possible get all the data in the column
print(data_frame_2['calories'])
# day1    420
# day2    253
# day3    562
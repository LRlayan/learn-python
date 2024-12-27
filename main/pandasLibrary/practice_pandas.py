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

# ---------------------------
# shape - returns dimension like a tuple in the dataframe
print(data_frame_2.shape) # (3, 2)
# 3 -> rows
# 2 -> columns

# ---------------------------
# how to get column names
print(data_frame_2.columns) # Index(['calories', 'duration'], dtype='object')
print(list(data_frame_2.columns)) # ['calories', 'duration']

# ---------------------------
# how to get size in dataframe
# This is comming the multiplication in rows and columns
print(data_frame_2.size) # 6

# ---------------------------
# values - values purpose is convert dataframe to the numpy array
data_3 = pd.DataFrame({'A':[1,2],'B':[3,4]})
print(data_3)
print(data_3.values) # [[1 3] [2 4]]
print(type(data_3.values)) # <class 'numpy.ndarray'>

# ---------------------------
# len
# This len is the number of rows in a data frame.
print(len(data_3)) # 2

# ---------------------------

data = {
    'age':[10,20,30],
    'salary':[2500,36000,58000]
}

# ---------------------------
# mean (Average)
print(pd.DataFrame(data).mean()) 
# sum
print(pd.DataFrame(data).sum())
# describe - we are given statistical parameters about the relevent data set
print(pd.DataFrame(data).describe())
#         age        salary
# count   3.0      3.000000
# mean   20.0  32166.666667
# std    10.0  27947.868136
# min    10.0   2500.000000
# 25%    15.0  19250.000000
# 50%    20.0  36000.000000
# 75%    25.0  47000.000000
# max    30.0  58000.000000

# ---------------------------
data = {
    'Name':["Alice","Bob","charlie","David"],
    'Age':[24,27,22,32],
    'score':[85,70,90,88]
}

data_frame_3 = pd.DataFrame(data)

# filter data
filtered_age = data_frame_3[data_frame_3['Age'] > 25]
print(filtered_age)

# ----------------------------
# how to add new row in data frame
data_frame_3.loc[len(data_frame_3)] = ['ramesh',23,85]
print(data_frame_3)

# ----------------------------
#  how to drop column and row
# drop()
# remove column in data frame
new_data_frame_1 = data_frame_3.drop('Age',axis=1,inplace=False)
print(new_data_frame_1)

# remove row in data frame
new_data_frame_2 = data_frame_3.drop(4,axis=0,inplace=False)
print(new_data_frame_2)

# ---------------------------
# read csv file
customer_csv_file = pd.read_csv("main\pandasLibrary\customers-100.csv")
print(customer_csv_file)

# ---------------------------
# read json file
read_json_file = pd.read_json("main\pandasLibrary\example_1.json")
print(read_json_file)
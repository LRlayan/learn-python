# You are given a dataset containing employee records in a CSV file named "employee_data.csv". The dataset 
# includes the following columns:

# • EmployeeID (integer)
# • Age (integer)
# • Salary (float)
# • Department (string)
# • ExperienceYears (integer)

# Write a Python program using NumPy, Pandas, and file handling to analyze and modify the dataset as specified
#below:

# (a) Load the dataset using Pandas and display the first five rows.
# (b) Compute the mean, median, and standard deviation of the Salary column using NumPy.
# (c) Find the total number of employees who have ExperienceYears greater than 10.
# (d) Identify and display the five highest-paid employees, sorted in descending order of Salary.
# (e) Determine the percentage of employees aged above 50.
# (f) Add a new column to the existing dataframe as "ExperienceLevel", where:
# • If ExperienceYears ≥ 15, classify as "Senior"
# • If ExperienceYears between 5 and 14, classify as "Mid-Level"
# • Otherwise, classify as "Junior"

# (g) Sort the dataset by ExperienceLevel (Senior first) and then by Salary in descending order.
# Your solution should demonstrate proper use of NumPy, Pandas, and file handling in Python while ensuring 
# efficient and optimized code.

# answer (a)
import pandas as pd

file_path = "main\csv-pandas-numpy-excersice\employee_data.csv"

def read_five_row():
    with open(file_path, "r", newline='') as file:
        reader = pd.read_csv(file)
        read_first_five_data = reader.head()
        print("Read five employee data : ",read_first_five_data)
        
read_five_row()
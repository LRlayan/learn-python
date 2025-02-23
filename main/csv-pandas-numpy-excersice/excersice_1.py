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
import numpy as np

file_path = "main\csv-pandas-numpy-excersice\employee_data.csv"

def read_employee_date():
    with open(file_path, "r", newline='') as file:
        reader = pd.read_csv(file)
        return reader
        
employe_data = read_employee_date()
get_five_first_employee = employe_data.head()
print(get_five_first_employee) # answer (a)

# answer (b)
def salary():
    reader = read_employee_date()
    salaries = reader['Salary']
    print("\nMean of salary : " ,np.mean(salaries))
    print("Median of salary" ,np.median(salaries))
    print("Deviation of salary" ,np.std(salaries, ddof=1))

    
salary()

# answer (c)
number_of_years_employee_experiance = employe_data[employe_data["ExperienceYears"] > 10]
print("\nNumber_Of_Years Employee Experiance\n",number_of_years_employee_experiance)

# answer (d)
df = pd.DataFrame(employe_data)
data = df.sort_values(by="Salary", ascending=False)
heighest_five_salary = data.head()
print("\nHeighest Five Salary\n",heighest_five_salary)

# answer (e)
df = pd.DataFrame(employe_data)
above_50_age = df[df['Age'] > 50]
precentage = len(above_50_age)/len(employe_data)*100
print("\nPrecentage of employe above 50 age : ", precentage)


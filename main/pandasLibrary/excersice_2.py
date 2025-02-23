import pandas as pd

file_path = "main\pandasLibrary\student.csv"

def employee_manage():
    
    read_student = pd.read_csv(file_path)
    print(read_student)
    
    
employee_manage()
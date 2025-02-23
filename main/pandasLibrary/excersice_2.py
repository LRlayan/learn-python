import pandas as pd

file_path = "main\pandasLibrary\student.csv"

def employee_manage():
    
    # 1
    df = pd.read_csv(file_path)
    print(df)
    
    # 2
    average = df.groupby(["StudentID","Name"])["Score"].mean().reset_index()
    average.rename(columns={"Score":"AverageScore"}, inplace=True)
    print(average)
    
    # 3
    filter_student_higher_average = average[average["AverageScore"] >= 90]
    print(filter_student_higher_average)
    
employee_manage()
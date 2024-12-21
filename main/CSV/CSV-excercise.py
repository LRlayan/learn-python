# you are task with ceating a python program to manage a compnay is employe records stored in csv file
# the program should read the employe details from a csv file , filter the record base on a condition an write the filters record 
# contains the following field 
    # emp_ID,name,department,salary <- csv file headrs
    # output file
        # high salary employe.csv
    # it should contain record for employe who's salaries are above 57000 
    
    # task
    # 1.read the input file <- use csv.reader to read emloyes.csv and display all the record on the console
    # 2.filter the record identify employe with the saraly > 57000
    # 3. write the filter records you csv.Dicwriter to write the filter record to a new file name high-salary-employee.csv

import csv

file_path ="main\CSV\employe.csv"

all_employees = []
filtered_employee = []
field_names = []

def dashboard():
    with open(file_path,"r",newline='') as read_file:
        employe_read = csv.reader(read_file)
        for employe in employe_read:
            print(employe)
            all_employees.append(
                {
                    "employeID":employe[0],
                    "name":employe[1],
                    "department":employe[2],
                    "salary":employe[3]
                }
            )
        field_names = all_employees.pop(0)

dashboard()   
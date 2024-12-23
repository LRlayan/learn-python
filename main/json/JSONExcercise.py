# you are given a json file name student of json which containes information above student and their grades you are task
# 1.read the json file
# 2.display the name of all students who scored above 75
# 3.add the new students record to the file
# 4.save to the update data to the json file

import json

def view_student():
    try:
        with open("student.json","r") as read_student:
            students = json.load(read_student)
            print(students)
            for student in range(len(students)):
                if students[student]["grade"] > 75:
                    print("this is student more than grade 75 : " + students[student]["name"])
    except FileNotFoundError:
        print("File not found!!!")

def add_new_student():
    name = input("Enter the name : ")
    grade = int(input("Enter the grade : "))
    
    try:
        with open("student.json","r") as students:
            student = json.load(students)
    except FileNotFoundError:
        student = []
        print("File not found")
    except json.JSONDecodeError:
        student = []
        print("File is empty or currupted")
        
    student_dict = {
        "name":name,
        "grade":grade
    }
    
    student.append(student_dict)
    
    with open("student.json","w") as save_student:
        json.dump(student , save_student , indent=4)
        print("Saved studeent successfully!")
        
def main():
    while True:
        input_option = int(input("Enter the option 1(view) or 2(save) or 3(exit) : "))
        if input_option == 1:
            view_student()
        elif input_option == 2:
            add_new_student()
        elif input_option == 3:
            break
        else:
            print("Please enter a valid option!!!")

main()
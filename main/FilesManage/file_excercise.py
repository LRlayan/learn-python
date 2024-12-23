# implement the simple contact management system
# 1.create the program that stores an manage contacts in a file name contacts.txt
# each contact entry should include name , number and email
# 2. features is implement
#  add a new contact (append the new contact the file)
#  view all conatct(read and display all contact your file)
# 3. exist the program

def save_contact():
    name = input("Enter the name : ")
    mobile = input("Enter the mobile : ")
    email = input("Enter the email : ")
    contact_details = ["\n"+" Name : " + name + " " + " Mobile : " + mobile + " Email : " + " " + email]
    with open("contact.txt" , "a") as save_contact:
        save_contact.writelines(contact_details)
              
def view_contact():
    try:
        with open("contact.txt","r") as view_contact:
            print(view_contact.read())
    except FileNotFoundError:
        print("File Not Found!")
        
def dashboard():
    while True:
        input_option = int(input("Enter the option - #1-save  ,  #2-view  ,  #3-exit :"))
        if input_option == 1:
            save_contact()
        elif input_option == 2:
            view_contact()
        elif input_option == 3:
            break
        else:
            print("Wrong Input!")

dashboard()

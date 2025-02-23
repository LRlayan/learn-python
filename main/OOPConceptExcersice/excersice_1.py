# You are developing a Library Management System using Object-Oriented Programming concepts in Python. 
# You have to implement the following classes:
# 
# Classes and Attributes:
# 
# 1. Person (Base Class)
# • Attributes: name (string), age (integer)
# • Method: display_infoO - Prints the name and age
# 
# 2. Librarian (Derived Class from Person)
# • Additional Attribute: employee_id (string)
# • Override display info to include the employee_id
# 
# 3. Member (Derived Class from Person)
# • Additional Attribute: membership_id (string)
# • Override display _info to include the membership_id
# 
# 4. Library (Encapsulated Class)
# • Private Attribute: _books (dictionary storing book titles as keys and available copies as values)
# • Private Attribute: _members (list to store Member objects)
# • Methods:
# • add_book(title: str, copies: int) - Adds a book and its available copies
# • register_member(member: Member) - Adds a member to the_members list
# • lend_book(title: str, member: Member) - Allows a member to borrow a book if available
# • show_all_books - Displays all books with available copies
# • show_all_members - Displays information about all registered members

# (a). Implement the above classes with appropriate constructors, inheritance, and method overriding. Use 
# encapsulation to prevent direct modification of _books and _members lists from outside the Library class.
# 
# (b). Write a Python script to:
# • Add at least three books to the library
# • Register at least two members
# • Lend a book to a member and display the updated book list
# 
# (c). Demonstrate polymorphism by calling the display_info method on Librarian and Member objects. Ensure
# that the correct overridden method is executed for each object.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        

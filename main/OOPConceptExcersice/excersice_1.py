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
# • Private Attribute: __books (dictionary storing book titles as keys and available copies as values)
# • Private Attribute: __members (list to store Member objects)
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
        
class Librarian(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name,age)
        self.employee_id = employee_id
        
    def display_info(self):
        super().display_info()
        print(f"Employee ID : {self.employee_id}")
        
class Member(Person):
    def __init__(self,name,age,membership_id):
        super().__init__(name,age)
        self.membership_id = membership_id
        
    def display_info(self):
        super().display_info()
        print(f"Membership Id : {self.membership_id}")
        
class Library:
    def __init__(self):
        self.__books = {}
        self.__members = []
        
    def add_book(self,title,copies):
        if title in self.__books:
            self.__books[title] += copies
        else:
            self.__books[title] = copies
        print(f"Added {title} Book with {copies} Copies.")
        
    def register(self,member):
        self.__members.append(member)
        print(f"{member.name} Member is Registered")
        
    def lend_book(self,title,member):
        if title in self.__books and self.__books[title] > 0:
            self.__books[title] -= 1
            print(f"{title} book lead to {member.name}.")
        else:
            print(f"Sorry, not available {title} book")        
        
    

librarian = Librarian("Ramesh",24,"E001")
librarian.display_info()

member_1 = Member("Layan",25,"M001")
member_1.display_info()

library = Library()

library.add_book("Python",5)
library.add_book("Java",10)
 
member_2 = Member("Raj",60,"M002")
library.register(member_1)
library.register(member_2)

library.lend_book("Java",member_1)
class Person: # Base Class
    __count = 0 #usage of private variable
    def __init__(self, name, email): # default constructor __init__
        self.name = name
        self.email = email # usage of self
        Person.__count +=1
    def dispDetails(self):
        print("Name: ", self.name,"Email: ", self.email)
    def displayCount(self):
        print("Total Count:", Person.__count)

class Student(Person): #usage of inheritance
    def __init__(self, name, email, student_id):# default constructor __init__
        Person.__init__(self, name, email)
        self.student_id = student_id
    def dispDetails(self):
        Person.dispDetails(self)
        print("Student Id: ",self.student_id)

class Librarian(Person):
    def __init__(self, name, email, emp_id):# default constructor __init__
        super().__init__(name, email) # use of super call
        self.emp_id = emp_id
    def dispDetails(self):
        Person.dispDetails(self)
        print("Employee ID: ",self.emp_id)
class Book():
    def __init__(self, name, author, isbn):# default constructor __init__
        self.book_name = name
        self.author = author
        self.isbn = isbn
    def dispDetails(self):
        print("Book_Name: ", self.book_name,"Author: ", self.author,"Book_ID: ", self.isbn)

class BookBorrow(Student, Book):#multiple inheritance
    def __init__(self, name, email, student_id, bookname, author, isbn):# default constructor __init__
        Student.__init__(self, name, email, student_id)
        Book.__init__(self, bookname, author, isbn)
    def dispDetails(self):
        Student.dispDetails(self)
        Book.dispDetails(self)

#creation of instances for all the classes
student1 = Student('Sirisha', 'sirisha1206@gmail.com', 16265791)
student2 = Student('Vinay', 'viany1301@yahoo.com', 16264245)
librarian1 = Librarian('Micheal', 'micheal@gmail.com', 9834)
librarian2 = Librarian('John', 'john@yahoo.com', 4371)
book1 = Book('Learning Python', 'Mark Lutz', 1837)
book2 = Book('Fundamentals of Deep Learning', 'Nikhil Buduma', 4738)

print('##### Person Count ######')
Person.displayCount(Person)

borrow_book1 = BookBorrow('Sirisha', 'sirisha1206@gmail.com', 16265791, 'Learning Python','Mark Lutz', 1837)

print('####### Student Details ######')
student1.dispDetails();
student2.dispDetails();

print('###### Librarian Details #####')
librarian1.dispDetails();

print('##### Book Details #####')
book1.dispDetails();
book2.dispDetails();

print('##### Borrowing book details ######')
borrow_book1.dispDetails();

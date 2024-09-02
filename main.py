from Library import *
from Book import *

books = []
lib = Library(books)
while True:
    print ("1. Add new book\n2. Borrow a book\n3. Return a book\n4. Display all books\n5. Display borrowed books\n6. Exit")
    not_number = True
    
    while not_number:
        choice = (input("Enter choice: "))
        if (not choice.isnumeric()):
                print("Please enter an integer")
        else:
            choice = int(choice)
            not_number = False
        
    if (choice == 1):   #add new book
        id = input("Enter book ID: ")
        if (not id.isnumeric()):
            print("Please enter an integer")
        else:
            id = int(id)
            title = input ("Enter book title: ")
            author = input("Enter author:")
            lib.add_book(id, title, author)
        
    
    elif (choice == 2): #borrow a bookc
        id = input("Enter book ID: ")
        if (not id.isnumeric()):
            print("Please enter an integer")
        else:
            id = int(id)
            borrower = input ("Enter borrower name: ")
            due_date = input("Enter due date:")
            lib.borrow_book(id, borrower, due_date)
        
    elif (choice == 3): #return a book
        id = input("Enter book ID: ")
        if (not id.isnumeric()):
            print("Please enter an integer")
        else:
            id = int(id)
            lib.return_book(id)
        
    elif (choice == 4):
        lib.display_books()
        
    elif (choice == 5): #display borrower books
        lib.display_borrowed_books()
        
    elif (choice == 6): #exit
        print ("Goodbye!")
        break
    else:
        print ("Invalid Input, please enter numbers between 1 through 6")
        
        
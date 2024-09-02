from Book import *
class Library:
    def __init__(self, books_list):
        #attributes
        self.books_list = books_list
        
    def add_book (self,book_id, title, author):
        if self.find_book(book_id) != -1:   
            print ("Book ID already in the library")
        else:
            new_book = Book(book_id, title, author)
            self.books_list.append(new_book)
            print (f"Book {title} added")
    
    def find_book(self, book_ID):
        #Finds and returns the book object for the given book ID.
        for i in self.books_list:
            if i.id == book_ID:
                return i
        print ("Book not found")
        return -1   #Meaning the book isnt found
    
    def borrow_book(self, book_ID, borrower, due_date):                
        target = self.find_book(book_ID)
        if target != -1:
            if not target.is_available():
                print ("Book is being borrowed")
            else:
                target.borrow_book(borrower, due_date)
        
        
    def return_book (self, book_ID):
        target = self.find_book(book_ID)
        if target != -1:    #meaning that the book is found
            if target.is_available():
                print("The book is already available")
            else:
                target.return_book()
        else:
            print ("The book is not in the library")
    
    def display_books (self):
        if len(self.books_list) == 0:
            return print ("The libary is empty!")
        else:
            for i in self.books_list:
              print(f"Book ID: {i.id} | Ttitle:  {i.title} | Author: {i.author} | Borrower: {i.borrower} | Due Date: {i.due_date} ")
       
    def display_borrowed_books(self):
        if len(self.books_list) == 0:
            return print ("The libary is empty!")
        else:
            for i in self.books_list:
                if not i.is_available():
                    print(f"Book ID: {i.id} | Ttitle:  {i.title} | Author: {i.author} | Borrower: {i.borrower} | Due Date: {i.due_date} ")
        

        
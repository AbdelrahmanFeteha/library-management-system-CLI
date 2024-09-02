from Book import *
from Library import *

def borrow(lib):
    id = int(input("Enter book ID: "))
    borrower = input ("Enter borrower name: ")
    due_date = input("Enter due date:")
    lib.borrow_book(id, borrower, due_date)
    
    






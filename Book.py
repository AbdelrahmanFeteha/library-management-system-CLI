class Book:
    def __init__(self,id,title,author,borrower=None,due_date=None):
        self.id=id
        self.title=title
        self.author=author
        self.borrower=borrower
        self.due_date=due_date
    def borrow_book(self,borrower,due_date):
        self.borrower=borrower
        self.due_date=due_date
    def return_book(self):
        self.borrower=None
        self.due_date=None
    def is_available(self):
        if self.due_date == None:
            return True
        return False
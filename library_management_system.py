class Book:
    def __init__(self, title, author, isbn, available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f'title: {self.title}, author: {self.author}, isbn: {self.isbn}, avalable: {self.available}'

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True
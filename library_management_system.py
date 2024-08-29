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

    def return_b(self):
        self.available = True


class Member:
    def __init__(self, name, member_id, borrowed_books = []):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def __str__(self):
        return f'name: {self.name}, member id: {self.member_id}, borrowed books: {self.borrowed_books}'

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        book.borrow()

    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.return_b()
class Book:
    def __init__(self, title, author, isbn, available = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f'title: {self.title}, author: {self.author}, isbn: {self.isbn}, available: {self.available}'

    def borrow(self):
        self.available = False

    def return_book(self):
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
        book.return_book()


class Library:
    def __init__(self, books = [], members = []):
        self.books = books
        self.members = members

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def issue_book(self, member_id, isbn):
        for book in self.books:
            if book.isbn == isbn:
                inp_book = book
                break
        for member in self.members:
            if member.member_id == member_id:
                inp_member = member
                break
        inp_member.borrow_book(inp_book)
    
    def return_book(self, member_id, isbn):
        for book in self.books:
            if book.isbn == isbn:
                inp_book = book
                break
        for member in self.members:
            if member.member_id == member_id:
                inp_member = member
                break
        inp_member.return_book(inp_book)
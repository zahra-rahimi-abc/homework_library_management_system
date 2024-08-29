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

    def list_books(self):
        return [str(book) for book in self.books]

    def list_members(self):
        return [str(member) for member in self.members]


# ایجاد کتاب‌ها
book1 = Book("1984", "جورج اورول", "1234567890")
book2 = Book("کشتن مرغ مقلد", "هارپر لی", "0987654321")
print(book1)
print(book2)

# ایجاد کتابخانه و اضافه کردن کتاب‌ها
library = Library()
library.add_book(book1)
library.add_book(book2)
print(library.list_books())

# ثبت یک عضو
member = Member("آلیس", "M001")
library.register_member(member)
print(member)
print(library.list_members())

# امانت دادن کتاب به عضو
library.issue_book("M001", "1234567890")
print(library.list_books())

# بازگرداندن کتاب
library.return_book("M001", "1234567890")
print(library.list_books())
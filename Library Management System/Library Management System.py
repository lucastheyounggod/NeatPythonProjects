class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not borrowed")

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")



class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"{member.name} has registered as a library member.")

    def display_books(self):
        print(f"\nBooks in the Library:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"- {book.title} by {book.author} ({status})")


book1 = Book("1984", "George Orwell")
book2 = Book("To Kill A Mockingbird", "Harper Lee")

library = Library()
library.add_book(book1)
library.add_book(book2)

member1 = Member("Alice")
member2 = Member("Tony")
library.register_member(member1)
library.register_member(member2)

library.display_books()

member1.borrow_book(book1)
member2.borrow_book(book2)
library.display_books()

member1.return_book(book1)

library.display_books()
# Design a Library Management System: 
# Design a basic library system where a Book class stores a title and an author and a Library class can add books and display all available books.

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
    

class Library(Book):
    def __init__(self):
        self.all_books = [] # DON'T FORGET SELF.

    def add_books(self, book):
        self.all_books.append(book)

    def remove_books(self, book):
        if book in self.all_books:
            self.all_books.remove(book)

    def display_library_content(self):
        if len(self.all_books) == 0:
            print("The library is empty.")
        for book in self.all_books:
            print(f"{book.title} by {book.author}")
            

book1 = Book("Harry Potter", "JK Rowling")
book2 = Book("The Kite Runner", "Khaled Hosseini")
book3 = Book("The Fault in our Stars", "John Green")

# Can't directly call Library.
library = Library()
library.display_library_content()
library.add_books(book1)
library.add_books(book3)
library.display_library_content()
library.add_books(book2)
library.remove_books(book1)
library.display_library_content()
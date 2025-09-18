## Aggregation = Represents a relationship where one object contains refereneces to one or more 
##               independent objects


class Library:
    def __init__(self, name):
        self.name =name
        self.books = []

    def add_book(self, book):
        self.books.append(book) 

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]   

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("City Library")


book1 = Book("BOOK1", "AUTHOR1")
book2 = Book("BOOK2", "AUTHOR2")
book3 = Book("BOOK3", "AUTHOR3")
book4 = Book("BOOK4", "AUTHOR4")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

print(f"Library: {library.name}")

print("List of books:", library.list_books())

for book in library.books:
    print(f"Book: {book.title}, Author: {book.author}")

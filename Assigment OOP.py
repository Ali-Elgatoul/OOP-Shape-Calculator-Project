#question 1
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero."
        return a / b

calc = Calculator()

print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 2))
print(calc.divide(10, 0))

#question 2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        return f"Title: {self.title}, Author: {self.author}"


class Library:
    def __init__(self):
        self.books = []
        print("Library initialized with an empty collection.")

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.display()}")

    def list_books(self):
        print("Library books:")
        for book in self.books:
            print(book.display())

lib = Library()

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

lib.add_book(book1)
lib.add_book(book2)

lib.list_books()

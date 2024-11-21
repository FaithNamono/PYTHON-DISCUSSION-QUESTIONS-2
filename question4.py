# Object Oriented Programming(OOP)
#BASIC
#Create a Car class and print attributes
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

myCar= Car("Toyota", "Red")
print(myCar.brand, myCar.color)

#Intermediate
#Add a start_engine method to car
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.brand} car has started.")

car = Car("Toyota", "Red")
car.start_engine()

#Advanced
#Implement BamkAccount class with deposit,withdraw and balance methods
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def print_balance(self):
        print("Balance:", self.balance)

account = BankAccount("12345", 100)
account.deposit(50)
account.withdraw(30)
account.print_balance()

#Challenge
#Implement a library class to manage the book collection.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def is_available(self, title):
        for book in self.books:
            if book.title == title:
                return book.available
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True

library = Library()
library.add_book("Python Programming", "John Doe")
print(library.is_available("Python Programming"))
library.borrow_book("Python Programming")
print(library.is_available("Python Programming"))
library.return_book("Python Programming")
print(library.is_available("Python Programming"))

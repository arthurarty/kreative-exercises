"""
Create a dataclass named Address with attributes 
street (str), city (str), and zip_code (str). 
Then, create another dataclass named PersonInfo with attributes 
name (str), age (int), and address (an instance of Address). 
Create instances of PersonInfo with appropriate data 
and access nested attributes.


Create a dataclass named Book with attributes 
title (str), author (str), and year (int). 
Compare two Book instances based on their attributes. > < ==
"""


from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    zip_code: str


@dataclass
class PersonInfo:
    name: str
    age: int
    address: Address

address = Address('13 Valley Curve', 'Durban', '34A')
person_john = PersonInfo('John Doe', 38, address)
print(person_john)


@dataclass
class Book:
    title: str
    author: str
    year: int


first_book = Book('Little Red', 'Charles Perraault', 1700)
second_book = Book('A Song of ice and fire', 'George R R Martin', 1991)
print(first_book == second_book)
print(first_book.title > second_book.title)
print(first_book.author > second_book.author)
print(first_book.year> second_book.year)

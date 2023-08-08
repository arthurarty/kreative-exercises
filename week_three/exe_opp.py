"""
Create a class Author with attributes name and birth_year,
and a class Book with attributes title, publication_year,
and an instance of Author.
In the end associate an author with a book.
"""


class Author:
    """
    Representation of a person who writes a book
    """
    def __init__(self, name: str, birth_year: int) -> None:
        self.name = name
        self.birth_year = birth_year

    def __str__(self) -> str:
        return f"Author: {self.name} born {self.birth_year}"


class Book:
    """
    A book written by an author.
    """
    def __init__(self, title: str, publication_year: int, author: Author) -> None:
        self.title = title
        self.publication_year = publication_year
        self.author = author

    def __str__(self) -> str:
        return f"{self.title} published: {self.publication_year} author: {self.author.name}"


jk_rowling = Author('JK Rowling', 1982)
book = Book('Harry Potter', 2001, jk_rowling)
print(book)

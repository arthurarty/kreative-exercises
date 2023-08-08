class Person:
    """
    Representation of a person
    """
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def __str__(self) -> str:
        return f'My name is {self.fname} {self.lname}'


class Student(Person):
    def __init__(self, fname: str, lname: str, graduation_year: int) -> None:
        super().__init__(fname, lname)
        self.graduation_year = graduation_year

    def welcome(self):
        print("Welcome", self.lname, "to the class of", self.graduation_year)


arthur = Student('Arthur', 'Nangai', 2025)
arthur.welcome()

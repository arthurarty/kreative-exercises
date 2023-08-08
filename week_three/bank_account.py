"""
Create a BankAccount class with attributes account_number
and balance. Implement methods to deposit and withdraw 
funds, and another method to display the account details.
"""


class BankAccount:
    def __init__(self, account_number: int, balance: int) -> None:
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount
        print(f"New balance is {self.balance}")

    def withdraw(self, amount: int):
        if amount < self.balance:
            self.balance -= amount
            print(f"New balance is {self.balance}")
            return
        print("Withdraw amount is more than balance")

    def display_account_details(self):
        print("Account Number", self.account_number, "Balance", self.balance)


ac1 = BankAccount(23, 4000)
ac1.display_account_details()
ac1.deposit(5200)
ac1.withdraw(10500)
ac1.display_account_details()
ac1.withdraw(6200)
ac1.display_account_details()

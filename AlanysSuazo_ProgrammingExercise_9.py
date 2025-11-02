# Alanys Suazo
# Assignment: Programming Exercise 9

# The purpose of this assignment is to practice using and creating classes. The purpose of this program is to
#    create a class for a bank account that contains information like the name, account number, amount,
#    and interest rate. This class should also be able to adjust interest rate, withdraw and deposit,
#    show the current balance, as well as calulate interest based on number of days entered.
#    This program should aslso be able to test all the diferent functions and methods.


class BankAcct:


    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name.strip()
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate


    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("We don't deal deal in alphabetic currency...")
        if amount <= 0:
            raise ValueError("You can't deposit negative cash")
        self.amount += amount
        return self.amount


    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("We don't deal deal in alphabetic currency...")
        if amount <= 0:
            raise ValueError("You can't withdraw negative cash!")
        if amount > self.amount:
            raise ValueError(f"You don't have enough money to withdraw {amount:.2f}.")
        self.amount -= amount
        return self.amount


    def set_interest_rate(self, new_rate):
        if not isinstance(new_rate, (float, int)) or new_rate < 0:
            raise ValueError("Interest Rate must be a non-negative number.")
        self.interest_rate = float(new_rate)


    def show_balance(self):
        return self.amount


    def calc_interest(self, days):
        if not isinstance(days, (int)) or days < 0:
            raise ValueError("Days must be positive.")
        interest = self.amount * (self.interest_rate * (days / 365))
        return interest

    def __str__(self):
        account_info = (
            f"Account Summary for {self.name}\n"
            f"  Account Number: {self.account_number}\n"
            f"  Current Balance: ${self.ammount:,.2f}\n"
            f"  Interest Rate: {self.interest_rate:.2%}\n"
        )
        one_yr_interest = self.calc_interest(365)
        account_info += f"  Interest (1 year): ${one_yr_interest:,.2f}\n"
        return account_info
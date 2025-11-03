# Alanys Suazo
# Assignment: Programming Exercise 9

# The purpose of this assignment is to practice using and creating classes. The purpose of this program is to
#    create a class for a bank account that contains information like the name, account number, amount,
#    and interest rate. This class should also be able to adjust interest rate, withdraw and deposit,
#    show the current balance, as well as calulate interest based on number of days entered.
#    This program should aslso be able to test all the diferent functions and methods.


class BankAcct:


    def __init__(self, name, account_number, amount, interest_rate,):
        if not isinstance(name,str) or not name.strip:
            raise ValueError('Name canno be empty.')
        if not isinstance(amount, (float, int)) or amount < 0:
            raise ValueError("Initail amount in the account cannot be below 0.")
        if not isinstance(interest_rate, (float, int)) or interest_rate < 0:
            raise ValueError("Interest Rate cannot be negative.")
        self.name = name.strip()
        self.account_number = str(account_number)
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)


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
        return amount, self.amount


    def set_interest_rate(self, new_rate):
        if not isinstance(new_rate, (float, int)) or 0 > new_rate :
            raise ValueError("Interest Rate must be a non-negative number.")
        self.interest_rate = float(new_rate)


    def show_balance(self):
        return self.amount


    def calc_interest(self, days):
        if not isinstance(days, (float, int)) or days < 0:
            raise ValueError("Days must be positive.")
        interest = self.amount * (self.interest_rate * (days / 365))
        return interest

    def __str__(self):
        account_info = (
            f"Account Summary for {self.name}\n"
            f"  Account Number: {self.account_number}\n"
            f"  Current Balance: ${self.amount:,.2f}\n"
            f"  Interest Rate: {self.interest_rate:.2%}\n"
            f"  Interest (365 days): ${self.calc_interest(365):,.2f}\n"
        )
        return account_info

def test_bank_acct():
    print('Testing class functionality')
    acct = BankAcct("Test User", 8790, 500.00, 0.03)
    print(acct)

    acct.deposit(1500)
    assert acct.show_balance() == 2000.0

    acct.withdraw(100.50)
    assert acct.show_balance() == 1899.50

    try:
        acct.withdraw(99999)
    except ValueError:
        print("withdraw method handled overdraft attempt.")

    try:
        acct.withdraw(-1)
    except ValueError:
        print("withdraw method hendled negative intput.")

    try:
        acct.deposit(-1)
    except ValueError:
        print("deposit method hendled negative intput.")

    acct.set_interest_rate(0.04)
    assert acct.interest_rate == 0.04

    try:
        acct.set_interest_rate(-0.01)
    except ValueError:
        print("set_interest_rate handled negative input.")

    interest = acct.calc_interest(670)
    print(f"Interest for 670 days: ${interest:,.2f}")
    assert round(interest, 2) == round(1899.50*(0.04*(670/365)),2)
    print("all tests passed")

if __name__ == "__main__":
    test_bank_acct()
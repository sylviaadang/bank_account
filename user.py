from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            "savings": BankAccount(int_rate = 0.02, balance=0),
            "checking": BankAccount(int_rate = 0.05, balance=0)
        }

    def make_deposit(self, amount, target):
        self.accounts[target].deposit(amount)
        return self

    def make_withdrawal(self, amount, target):
        self.accounts[target].withdraw(amount)
        return self

    def display_user_balance(self, target):
        self.accounts[target].display_account_info()
        return self

user1 = User('Kyle', 'kyle@gmail.com')

user1.make_deposit(10, 'savings')

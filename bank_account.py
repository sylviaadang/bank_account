class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited to your account.")
        return self


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return self
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
            return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print(f"Your account balance has increased by ${self.balance}")
        return self


bank1 = BankAccount(.3)
bank2 = BankAccount(.1)

bank1.deposit(10).deposit(5).deposit(15).withdraw(2).yield_interest().display_account_info()

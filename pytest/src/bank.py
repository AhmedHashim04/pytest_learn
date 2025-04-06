class BankAccount:
    def __init__(self, balance=0):

        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive and less than or equal to the balance")

    def get_balance(self):
        return self.balance
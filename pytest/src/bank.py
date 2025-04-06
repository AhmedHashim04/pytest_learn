class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount

            if amount > 0:
                self.transactions.append(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            if amount > 0:
                self.transactions.append(f"Withdrew: {amount}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance")

    def get_balance(self):
        return self.balance
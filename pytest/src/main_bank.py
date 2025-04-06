from bank import BankAccount

balance = 1000
account = BankAccount(balance)

print(f"Initial balance: {account.get_balance()}")
account.deposit(500)
print(f"Balance after deposit: {account.get_balance()}")
account.withdraw(200)
print(f"Balance after withdrawal: {account.get_balance()}")
account.withdraw(2000)  # This should raise an error

from bank import BankAccount
import pytest
# Test cases for the BankAccount class


def test_initial_balance():
    account = BankAccount(1000)
    assert account.get_balance() == 1000, f' balance{account.get_balance()}'
    account = BankAccount()
    assert account.get_balance() == 0 , f' balance{account.get_balance()}'
    account = BankAccount(-500)
    assert account.get_balance() == -500 , f' balance{account.get_balance()}'
    account = BankAccount(0)
    assert account.get_balance() == 0 , f' balance{account.get_balance()}'

def test_deposit():
    account = BankAccount(1000)
    account.deposit(500)
    assert account.get_balance() == 1500, f' balance{account.get_balance()}'
    account.deposit(0)
    assert account.get_balance() == 1500, f' balance{account.get_balance()}'
    account.deposit(-500)
    assert account.get_balance() == 1500, f' balance{account.get_balance()}'

def test_withdraw():
    account = BankAccount(1000)
    account.withdraw(200)
    assert account.get_balance() == 800, f' balance{account.get_balance()}'
    account.withdraw(0)
    assert account.get_balance() == 800, f' balance{account.get_balance()}'
    account.withdraw(-200)
    assert account.get_balance() == 800, f' balance{account.get_balance()}'
    account.withdraw(1000)
    assert account.get_balance() == 800, f' balance{account.get_balance()}'
    account.withdraw(2000)
    assert account.get_balance() == 800, f' balance{account.get_balance()}'

def test_transactions():
    account = BankAccount(1000)
    account.deposit(500)
    assert account.transactions == ["Deposited: 500"], f' transactions{account.transactions}'
    account.withdraw(200)
    assert account.transactions == ["Deposited: 500", "Withdrew: 200"], f' transactions{account.transactions}'
    account.withdraw(2000)
    assert account.transactions == ["Deposited: 500", "Withdrew: 200"], f' transactions{account.transactions}'
    account.deposit(-500)
    assert account.transactions == ["Deposited: 500", "Withdrew: 200"], f' transactions{account.transactions}'
    account.withdraw(0)
    assert account.transactions == ["Deposited: 500", "Withdrew: 200"], f' transactions{account.transactions}'
    account.deposit(0)
    assert account.transactions == ["Deposited: 500", "Withdrew: 200"], f' transactions{account.transactions}'
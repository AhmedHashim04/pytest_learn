from bank import BankAccount
import pytest

def test_initial_balance():
    account = BankAccount(1000)
    assert account.get_balance() == 1000, f' balance{account.get_balance()}'
    account = BankAccount()
    assert account.get_balance() == 0 , f' balance{account.get_balance()}'
    account = BankAccount(-500)
    assert account.get_balance() == -500 , f' balance{account.get_balance()}'
    account = BankAccount(0)
    assert account.get_balance() == 0 , f' balance{account.get_balance()}'

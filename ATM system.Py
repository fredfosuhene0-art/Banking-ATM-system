
"""Banking ATM System - Case Study Implementation

Implements a BankAccount class with deposit, withdraw, and check_balance
methods, along with custom exception handling for invalid operations.
"""


class InsufficientFundsError(Exception):
    """Custom exception raised when a withdrawal exceeds the available balance."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = (
            f"Insufficient funds: attempted to withdraw {amount}, "
            f"but available balance is {balance}."
        )
        super().__init__(message)


class BankAccount:
    """Represents a simple bank account with deposit, withdraw, and balance checks."""

    def __init__(self, account_holder, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account. Raises ValueError for negative deposits."""
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        if amount == 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        """Withdraw money from the account.

        Raises:
            ValueError: if the withdrawal amount is invalid (negative or zero).
            InsufficientFundsError: if the amount exceeds the current balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount == 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def check_balance(self):
        """Return and display the current account balance."""
        print(f"Current balance for {self.account_holder}: {self.balance}")
        return self.balance


def main():
    """Demonstrates the BankAccount class and its exception handling."""
    account = BankAccount("Jane Doe", 100)

    # Normal operations
    account.check_balance()
    account.deposit(50)
    account.withdraw(30)
    account.check_balance()

    # Negative deposit
    try:
        account.deposit(-20)
    except ValueError as e:
        print(f"Error: {e}")

    # Invalid withdrawal amount (zero/negative)
    try:
        account.withdraw(-10)
    except ValueError as e:
        print(f"Error: {e}")

    # Insufficient funds
    try:
        account.withdraw(10000)
    except InsufficientFundsError as e:
        print(f"Error: {e}")

    account.check_balance()


if __name__ == "__main__":
    main()

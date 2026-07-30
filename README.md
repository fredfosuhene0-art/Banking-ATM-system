# Banking-ATM-system
# Banking ATM System - Case Study

A simple Python implementation of an ATM banking system, built around a
`BankAccount` class with deposit, withdrawal, and balance-check operations,
plus custom exception handling.

## Files

- `bank_account.py` — main implementation and demo

## Class: `BankAccount`

### Constructor
```python
BankAccount(account_holder, initial_balance=0)
```
Creates a new account. Raises `ValueError` if `initial_balance` is negative.

### Methods

| Method | Description |
|---|---|
| `deposit(amount)` | Adds `amount` to the balance. Raises `ValueError` if the amount is negative or zero. |
| `withdraw(amount)` | Subtracts `amount` from the balance. Raises `ValueError` for an invalid amount, or `InsufficientFundsError` if `amount` exceeds the balance. |
| `check_balance()` | Prints and returns the current balance. |

## Custom Exception: `InsufficientFundsError`

Raised when a withdrawal is attempted for more than the available balance.
Stores the current `balance` and the requested `amount` for reference.

## Exceptions Handled

- **Negative deposit** — `ValueError` raised in `deposit()`
- **Invalid withdrawal amount** (negative or zero) — `ValueError` raised in `withdraw()`
- **Insufficient funds** — `InsufficientFundsError` raised in `withdraw()`

## Usage

```python
from bank_account import BankAccount, InsufficientFundsError

account = BankAccount("Jane Doe", 100)
account.deposit(50)
account.withdraw(30)
account.check_balance()

try:
    account.withdraw(10000)
except InsufficientFundsError as e:
    print(e)
```

## Running the Demo

```bash
python bank_account.py
```

This runs `main()`, which demonstrates normal operations plus each of the
three error cases (negative deposit, invalid withdrawal amount, and
insufficient funds).

# from .exceptions.minbal_error import MinBalError
from lib.bank.exceptions.minbal_error import MinBalError

class Account:
  min_balance: float = 1000

  def __init__(self, acc_no: int, acc_type: str, balance: float):
    self.acc_no = acc_no
    self.acc_type = acc_type
    self.balance = balance

  def deposit(self, amount: float) -> float:
    self.balance += amount
    return self.balance
  
  def withdraw(self, amount: float) -> float:
    print('Hello, Transaction starts...')

    try:
      if amount <= 0:
        raise ValueError('Amount must be greater than zero')
      
      if self.balance - amount < Account.min_balance:
        raise MinBalError(message='Insufficient balance')

      self.balance -= amount
      return self.balance
    finally:
      # finally block is executed irrespective of whether an exception occurs or not
      print('Good bye, Transaction ends...')
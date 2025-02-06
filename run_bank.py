from lib.bank.account import Account
from lib.bank.exceptions.minbal_error import MinBalError
from traceback import print_exc

acc: Account = Account(acc_no=123, acc_type='Savings', balance=10000)

try:
  ub: float = acc.withdraw(900000)
except ValueError:
  # print('Amount must be greater than zero')
  print_exc()
except MinBalError as err:
  print_exc()
else:
  print('Updates bal is {0}'.format(ub))
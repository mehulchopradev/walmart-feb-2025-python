''' print('Program starts')

n = int(input('Enter a number: '))
print('Even' if n % 2 == 0 else 'Odd')

print('Program ends') '''

# Proper input
# python interpreter -> play_input.py -> Program starts -> '5' -> int('5') -> 5 -> Odd -> Program ends

# Improper input
# python interpreter -> play_input.py -> Program starts -> 'five' -> int('five') -> ValueError -> play_input.py -> ValueError -> python interpreter

# Improper input with handling of the exception
# python interpreter -> play_input.py -> Program starts -> 'five' -> int('five') -> ValueError -> play_input.py -> handle ValueError -> Program ends

# handling errors
# try-except block
# try-except-else block
# try-except-except block
# try-finally block

print('Program starts')

try:
  n = int(input('Enter a number: '))
except ValueError: # ValueError is a built in exception class
  print('Please enter proper integer input')
else:
  # if no exception occurs
  print('Even' if n % 2 == 0 else 'Odd')

print('Program ends')

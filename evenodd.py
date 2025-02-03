# python unlike Java does not have block level scope for variables


def even_or_odd(n):
  # scope of n is only within this function
  if n % 2:
    # scope of ans variable in python is the enclosing function block (even_or_odd)
    ans = 'odd'
  else:
    # scope of ans variable in python is the enclosing function block (even_or_odd)
    ans = 'even'
  return ans

n = int(input('Enter a number: ')) # scope of n is only within this file
print(even_or_odd(n=n))
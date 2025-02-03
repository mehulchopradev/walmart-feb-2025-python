def greet(username):
  # if-else comprehensions - one statement per branch in order to use it in one line
  '''
  multiline comments
  on one
  per line
  '''
  return 'Welcome ' + username if username else 'Welcome guest'


print(greet(username='John'))
print(greet(username=None)) # None is a special value in Python indicates the absence of a value
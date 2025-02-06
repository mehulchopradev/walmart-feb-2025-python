from typing import Dict, Tuple

books: Dict[str, Tuple[str, int, int]] = {'B001': ('Book 1', 900, 1000), 'B002': ('Book 2', 800, 2000)}
print(books)
print(type(books))

ed = {} # empty dictionary
print(type(ed))

# indexing
print(books['B002'])
books['B001'] = ('Book 1', 450, 900) # update
print(books)

# looping
for bookId in books:
  # bookId is the key
  print(bookId)
  print(books[bookId])

# add a new book
books['B003'] = ('Book 3', 700, 1500)
print(books)

# remove a book
del books['B002']
print(books)

# books.pop('B002') # error

# membership
print('B003' in books)
print('B002' in books)

items = books.items()
print(items)
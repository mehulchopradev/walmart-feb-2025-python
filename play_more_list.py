marks = [4, 5, 6, 4, 3, 2, 10, 9, 3]

# create a new list consisting of even marks more than 2 from the marks list (filtering)
''' nl = []
for mark in marks:
  if mark % 2 == 0 and mark > 2:
    nl.append(mark) '''

# for comprehensions (pre requisite is that we should be needing a new list from an existing list)
nl = [mark for mark in marks if mark % 2 == 0 and mark > 2]
print(nl)

# create a new list consisting of marks from the marks list but where every mark is deducted by 1 (mapping)
nl_2 = [mark - 1 for mark in marks]
print(nl_2)

# create a new list consisting of odd marks from the marks list squared up in the new list (filtering and mapping)
nl_3 = [mark ** 2 for mark in marks if mark % 2]
print(nl_3)
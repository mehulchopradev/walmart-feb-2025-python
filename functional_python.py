marks = [4, 5, 6, 4, 3, 2, 10, 9, 3]
# Functional programming

# create a new list consisting of even marks more than 2 from the marks list (filtering)
def even_more_than_2(mark):
  return mark % 2 == 0 and mark > 2
l1 = list(filter(even_more_than_2, marks))
print(l1)

# create a new list consisting of marks from the marks list but where every mark is deducted by 1 (mapping)
def deduct_by_1(mark):
  return mark - 1
l2 = list(map(deduct_by_1, marks))
print(l2)

# create a new list consisting of odd marks from the marks list squared up in the new list (filtering and mapping)
def odd_marks(mark):
  return mark % 2 != 0
def square(mark):
  return mark ** 2

l3 = filter(odd_marks, marks)
l4 = map(square, l3)
print(list(l4))

# lambda functions
# Pre requisite: the function should have only one expression that is returned
l5 = list(filter(lambda mark: mark % 2 == 0 and mark > 2, marks))
print(l5)

print(list(map(lambda mark: mark - 1, marks)))

l6 = list(map(lambda mark: mark ** 2, filter(lambda mark: mark % 2 != 0, marks)))
print(l6)
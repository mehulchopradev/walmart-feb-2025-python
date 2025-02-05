fruits = {'apple', 'banana', 'cherry', 'apple'}
print(fruits)
print(type(fruits))

# es = {} # wont create a set
es = set()
print(type(es))

# looping
for fruit in fruits:
  print(fruit.capitalize())

# print(fruits[0]) # error. No indexing in a set as there is no order

fruits.add('orange')
fruits.add('orange') # no error but the set will not have a duplicate
print(fruits)

fruits.remove('banana')
print(fruits)

# membership
print('cherry' in fruits)

print(len(fruits))

marks = [4, 5, 6, 4, 3, 2, 10, 9, 3]
# unique set of marks that were scored in the class
print(list(set(marks)))

ma1 = [1, 3, 5, 7]
ma2 = [3, 5, 9, 10]

# common set of marks that were scored across both the classes (intersection)
ma1_set = set(ma1)
ma2_set = set(ma2)
print(ma1_set & ma2_set)

# all unique marks that were scored in both the classes (union)
print(ma1_set | ma2_set)

# marks that were scored in ma1 but not in ma2 (difference)
print(ma1_set - ma2_set)

# marks that were scored in ma2 but not in ma1 (difference)
print(ma2_set - ma1_set)
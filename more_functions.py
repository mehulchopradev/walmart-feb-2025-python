# variable number of arguments / parameters
def next_gen_add(*elements):
  # print(elements) # elements is a tuple
  sum = 0
  for element in elements:
    sum += element
  return sum


# packing the arguments into a tuple
print(next_gen_add(5, 4, 3))
print(next_gen_add(5, 4, 3, 2, 6, 7))
print(next_gen_add(5, 4, 3, 2, 6, 7, 8, 9, 10))
print(next_gen_add())

def perimeter(length, breadth):
  return 2 * (length + breadth)

stats = (7, 3)
# print(perimeter(length=stats[0], breadth=stats[1]))
print(perimeter(*stats)) # unpacking the tuple


def area(**stats):
  return stats['length'] * stats['breadth']


# print(area(8, 4)) # should give an error
# packing of named arguments into a dictionary
print(area(length=8, breadth=4))
print(area(breadth=4, length=8))



rect_stats = {'length': 9, 'breadth': 3}
# print(perimeter(length=rect_stats['length'], breadth=rect_stats['breadth']))

# unpacking the dictionary into the function arguments
print(perimeter(**rect_stats))
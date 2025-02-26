from typing import Tuple

def perimeter(length:int=3, breadth:int=2) -> int:
  return 2 * (length + breadth)

def area(length:int, breadth:int) -> int:
  return length * breadth

def stats(length:int, breadth:int) -> Tuple[int, int]:
  p = perimeter(length=length, breadth=breadth)
  a = area(length=length, breadth=breadth)
  return (p, a)


print(perimeter(10, 5))


''' l = int(input('Enter length: ')) # str -> int
b = int(input('Enter breadth: ')) '''

# positional parameters
# p = perimeter(l, b)

# named parameters
# p = perimeter(length=l, breadth=b)
# p = perimeter(breadth=b, length=l)

# a = area(l, b)

# 28 -> '28'

''' print('Perimeter is ' + str(p))
print('Area is ' + str(a))

print(perimeter(10)) # default value of 2 for the breadth
print(perimeter(5))
print(perimeter(3))

print(perimeter()) # default values of 3 for the length and 2 for the breadth

# perimeter with default length value and breadth passed by the user
print(perimeter(breadth=1))

t = stats(length=6, breadth=3)
print(t[0])
print(t[1]) '''
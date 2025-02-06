from typing import List

el = []
print(el)
print(type(el))

cars:List[str] = ['bmw', 'audi', 'toyota'] # homogenous data
s1 = ['mehul', 10, 'm', 90] # type: ignore # hetrogenous data -- list is not ideal data structure for this

# looping
for car in cars:
  print(car.capitalize())

# indexing
print(cars[0])
print(cars[-1])
# update an element in the list
cars[-1] = 'kia'
print(cars)

fullname: str = 'mehul chopra'
age:int = 10
pi:float = 3.14
is_lights_on:bool = True

marks:List[int] = [4, 5, 6, 4, 3, 2, 10, 9, 3]
# slicing
l1 = marks[0:4] # marks[:4]
print(l1)
l2 = marks[-3:]
print(l2)

# bifs
print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks) / len(marks))

# oop
# ['bmw', 'audi', 'kia']
cars.append('hyundai i10')
# ['bmw', 'audi', 'kia', 'hyundai i10']
cars.extend(['mercedes', 'jaguar'])
# ['bmw', 'audi', 'kia', 'hyundai i10', 'mercedes', 'jaguar']
cars.insert(1, 'jeep')
# ['bmw', 'jeep', 'audi', 'kia', 'hyundai i10', 'mercedes', 'jaguar']
print(cars)

# ['bmw', 'jeep', 'audi', 'kia', 'hyundai i10', 'mercedes', 'jaguar']
print(cars.pop())
# ['bmw', 'jeep', 'audi', 'kia', 'hyundai i10', 'mercedes']
print(cars.pop(2))
# ['bmw', 'jeep', 'kia', 'hyundai i10', 'mercedes']
cars.remove('jeep')
# ['bmw', 'kia', 'hyundai i10', 'mercedes']
print(cars)

copy_marks = marks.copy() # marks[:]
copy_marks.reverse()
print(copy_marks)
print(marks)

# membership
print('audi' in cars) # False
print('kia' in cars) # True

# other oop
print(marks.count(4))
print(marks.count(0))

# sorting
copy_marks = marks.copy()
copy_marks.sort()
print(copy_marks) # ascending sort

another_copy = marks.copy()
another_copy.sort(reverse=True) # using named argument
print(another_copy) # descending sort

cars.sort()
print(cars)


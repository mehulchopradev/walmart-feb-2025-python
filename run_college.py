from lib.college.student import Student

# 0
print(Student.count)

# s1 = Student("John", 'm', 10, 90)
s1 = Student(name='John', marks=90, gender='m', roll=10)
# Internally
# 1. Memory is allocated for the object -- 4003
# 2. Student | __init__(4003, "John", 'm', 10, 90)

# attributes to the objects
''' s1.name = "John"
s1.gender = 'm'
s1.roll = 10
s1.marks = 90 '''

# s2 = Student("Jane", 'f', 12, 45)
# Internally
# 1. Memory is allocated for the object -- 4006
# 2. Student | __init__(4006, "Jane", 'f', 12, 45)

s2 = Student.new_instance(name='Jane', gender='f', roll=12, marks=45)
# Internally
# Student | new_instance("Jane", 'f', 12, 45)

# 2
print(Student.count)

''' s2.name = "Jane"
s2.gen = 'f'
s2.r = 12
s2.mar = 45 '''

s3 = Student()

print(s1.get_details())
# Internally
# Student | get_details(s1)


print(s2.get_details())
# Internally
# Student | get_details(s2)

''' print(s1)
print(s2)
print(s3)

print(s1.name)
print(s1.gender)

print(s2.name)
print(s2.gender)

print(s3.name)
print(s3.gender) '''

# 3
print(Student.count)
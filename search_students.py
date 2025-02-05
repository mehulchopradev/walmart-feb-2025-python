from lib.college.student import Student

students = [
  Student(name='Alice', gender='F', roll=10, marks=90),
  Student(name='Jane', gender='F', roll=5, marks=70),
  Student(name='Mehul', gender='M', roll=13, marks=95),
  Student(name='Jill', gender='F', roll=3, marks=89),
]

roll_no = int(input('Enter roll to search: '))

''' found = False
for student in students:
  if student.roll == roll_no:
    print(student.get_details())
    found = True
    break

if not found:
  print('Student not found') '''

# for-else construct
for student in students:
  if student.roll == roll_no:
    print(student.get_details())
    break
else:
  # else block will execute if the loop completes without a `break`
  print('Student not found')
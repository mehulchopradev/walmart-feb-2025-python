from lib.college.student import Student

students = {
  10: Student(name='Alice', gender='F', roll=10, marks=90),
  5: Student(name='Jane', gender='F', roll=5, marks=70),
  13: Student(name='Mehul', gender='M', roll=13, marks=95),
  3: Student(name='Jill', gender='F', roll=3, marks=89),
}

roll_no = int(input('Enter roll to search: '))

if roll_no in students:
  print(students[roll_no].get_details())
else:
  print('Student not found')

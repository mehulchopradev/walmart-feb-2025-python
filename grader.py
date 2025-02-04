# grader
'''
>= 70: A
>= 60: B
>= 40: C
< 40: F
> 100 or < 0: I
'''
# if - elif - elif - elif - else

def calculate_grade(marks):
  if marks > 100 or marks < 0:
    grade = 'I'
  elif marks >= 70:
    grade = 'A'
  elif marks >= 60:
    grade = 'B'
  elif marks >= 40:
    grade = 'C'
  else:
    grade = 'F'
  return grade

marks = int(input('Enter marks: '))
print('Grade is :' + calculate_grade(marks=marks))
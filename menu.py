# menu
'''
1. Even series
2. Odd series
3. Calculating grade
4. Exit
Please enter ur option: 1
Enter n: 5
0 2 4
1. Even series
2. Odd series
3. Calculating grade
4. Exit
Please enter ur option: 2
Enter n: 5
1 3 5
1. Even series
2. Odd series
3. Calculating grade
4. Exit
Please enter ur option: 3
Enter ur marks: 90
Grade: A
1. Even series
2. Odd series
3. Calculating grade
4. Exit
Please enter ur option: 4
'''

# import the module
import lib.series as ser

# import directly the functions from the module
from lib.student_ops import calculate_grade as calc

from math import factorial # built in module


while True:
  print("1. Even series", "2. Odd series", "3. Calculating grade", "4. Factorial", "5. Exit", sep="\n")
  option = int(input("Please enter ur option: "))

  if option == 1:
    n = int(input("Enter n: "))
    print(ser.even_series(n))
  elif option == 2:
    n = int(input("Enter n: "))
    print(ser.odd_series(n))
  elif option == 3:
    marks = int(input("Enter ur marks: "))
    print(calc(marks))
  elif option == 4:
    n = int(input("Enter n: "))
    print(factorial(n))
  else:
    break # exit()
# module --> lib.college.student
# every class in python is represented by a class object in memory
# 1 class object per class
class Student:
  # class attribute
  count = 0

  # default __init__

  # constructor
  def __init__(self, name=None, gender=None, roll=None, marks=None):
    # self --> reference to the current object
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks

    # access class attributes using the class name
    Student.count += 1
    

  # instance (object) methods
  def get_details(self):
    # self -> s1, s2
    return 'Name: ' + self.name + '\nGender: ' + self.gender \
      + '\nRoll: ' + str(self.roll) + '\nMarks: ' + str(self.marks)
  
  # calculate grade

  # class methods
  def new_instance(name=None, gender=None, roll=None, marks=None):
    return Student(name=name, gender=gender, roll=roll, marks=marks)
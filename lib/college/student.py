from typing import Optional
from .college_user import CollegeUser

# module --> lib.college.student
# every class in python is represented by a class object in memory
# 1 class object per class
class Student(CollegeUser):
  # class attribute
  count:int = 0

  # default __init__

  # constructor

  def __init__(self, name:Optional[str] = None, gender: Optional[str] = None, \
               roll: Optional[int] = None, marks: Optional[int] = None):
    # self --> reference to the current object
    super().__init__(name=name, gender=gender)
    self.roll = roll
    self.marks = marks

    # access class attributes using the class name
    Student.count += 1
    

  # instance (object) methods
  # method overriding
  def get_details(self) -> str:
    # self -> s1, s2
    ''' return 'Name: ' + self.name + '\nGender: ' + self.gender \
      + '\nRoll: ' + str(self.roll) + '\nMarks: ' + str(self.marks)'''
    # return 'Name: {0}\nGender: {1}\nRoll: {2}\nMarks: {3}'.format(self.name, self.gender, self.roll, self.marks)
    return 'Name: {name}\nGender: {gender}\nRoll: {roll}\nMarks: {marks}'\
      .format(name=self.name, roll=self.roll, gender=self.gender, marks=self.marks)
  
  # calculate grade

  # class methods
  @classmethod
  def new_instance(cls, name:Optional[str] = None, gender: Optional[str] = None, \
               roll: Optional[int] = None, marks: Optional[int] = None) -> 'Student':
    # cls --> class object
    return Student(name=name, gender=gender, roll=roll, marks=marks)
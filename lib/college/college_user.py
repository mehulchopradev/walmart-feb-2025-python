# generalized / super class
from typing import Optional
class CollegeUser:

  def __init__(self, name:Optional[str]=None,\
                gender:Optional[str]=None) -> None:
    self.name = name
    self.gender = gender

  def get_details(self) -> str:
    return 'Name:{0}\nGender:{1}'\
    .format(self.name, self.gender)
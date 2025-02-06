from typing import List, Optional
from .college_user import CollegeUser

class Professor(CollegeUser):

  def __init__(self, name:Optional[str]=None, gender:Optional[str]=None,\
                subjects:List[str]=[]):
    super().__init__(name=name, gender=gender)
    self.subjects = subjects
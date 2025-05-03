from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str = "Sagar"
    age: Optional[int] = None 

new_student = {"age":18}
student = Student(**new_student)
print(student)

# output:
# name='Sagar' age=18
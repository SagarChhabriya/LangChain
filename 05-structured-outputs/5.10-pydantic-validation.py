from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = "Sagar"
    age: Optional[int] = None 
    email: EmailStr

new_student = {"age":18, "email":"xyz"}
student = Student(**new_student)
print(student)

# output:
# email
#   value is not a valid email
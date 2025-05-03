from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Sagar"
    age: Optional[int] = None 
    email: EmailStr
    cgpa: int = Field(gt=0, lt=10, default=5, description="Student CGPA in decimal form")

new_student = {"age":18, "email":"xyz", "cgpa":12}
student = Student(**new_student)
print(student)
print(dict(student)) # convert pydantic object to dict
print(student.model_dump_json()) # convert pydantic object to JSON

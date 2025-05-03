from pydantic import BaseModel

class Student(BaseModel):
    name: str = "Sagar"

student = Student()
print(student)

# output:
# name='Sagar'
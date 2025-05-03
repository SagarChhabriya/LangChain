from pydantic import BaseModel

class Student(BaseModel):
    name: str 

new_student = {"name":18} # pass the input of str then it will work well.

student = Student(**new_student)

print(type(student))

# pydantic_core._pydantic_core.ValidationError: 1 validation error for Student
# name
#   Input should be a valid string [type=string_type, input_value=18, input_type=int]




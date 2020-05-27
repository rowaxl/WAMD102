student = {
  "__age__": 10,
  "name": "John"
}

# print(student)

class Student:
  def __init__(self, name, age):
    self.__age__ = age
    self.name = name
  


stu = Student("DOE", 20)
print(stu["name"])
print(stu["__age__"])
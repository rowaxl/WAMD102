class Person:
  def __init__(self, name):
    self.name = name

  def greeting(self):
    print(f"Hi, good morning. I'm {self.name}")


steveJobs = Person("Steve Jobs")
steveJobs.greeting()
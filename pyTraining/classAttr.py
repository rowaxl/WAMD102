class Car:
  def __init__(self, model, color):
    self.model = model
    self.color = color

  def drive(self, speed: int):
    return f"{self.color} {self.model} driving {speed}km/h now"

class Koenigsegg(Car):
  def __init__(self, year, *args, **kwargs):
    self.__year = year
    super(Koenigsegg, self).__init__(*args, **kwargs)
  
  def drive(self, speed: int):
    return f"{self.color} {self.model}({self._year}) driving {speed}km/h now"

koen1 = Koenigsegg(2010, model="CCR", color="White")

koen1.__pub = "its pub"
# print(koen1.__year) # __year is private attribute and cannot be accessed
print(koen1.__pub)
print(koen1.drive(200))
class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 def information(self):
  print(f"Имя: {self.name}, Возраст: {self.age}")
person = Person("Яна", 22)
person.information()
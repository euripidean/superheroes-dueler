# dog.py
class Dog:
  # Required properties are defined inside the __init__ constructor method
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print("Woof!")

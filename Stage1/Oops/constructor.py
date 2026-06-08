#Constructor Defenition
# A Constructor is a Special method that is automatically called when an object is created . In Python cunstructor are defined using __init__.

#Example Program

class Laptop:

  def __init__(self, brand, ram):
    self.brand = brand
    self.ram = ram

  def display(self):
    print(f"Brand : {self.brand} RAM : {self.ram}")

l1 = Laptop("Asus",16)
l2 = Laptop("Dell",8)

l1.display()
l2.display()

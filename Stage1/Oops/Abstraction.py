# Abstraction Definition 
# Abstaction is a process of hiding implementaion and exposing only essential functionallities to the user 

#Example Program
from abc import ABC,abstractmethod

class Shape(ABC):
  
  @abstractmethod
  def area(self):
    pass

class Rectangle(Shape):

  def area(self):
    print("Rectangle area calculating......")

class Square(Shape):

  def area(self):
    print("Square Area calculating......")

r1 = Rectangle()

s1 = Square()

r1.area()
s1.area()


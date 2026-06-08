#Object Defenition 
# An Object is a instance of a class
# If the class is a blueprint, Then the Object is the actual thing created from the blueprint.

#Example Program 
class Car:

  def start(self):
    print("Car started.")

car1 = Car()
car2 = Car()

car1.start()
car2.start()
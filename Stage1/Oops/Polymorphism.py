#Polymorphism Defenition 
# Polymorphism is an OOP concepts where same method or interface have different behaviours based on the object that invokes it .
# Method Overiding is a form of Polymorphism . Method Overiding occurs when a child class provides its own implementaion of a method that is already exiting in the parent class

#Example Program
class Vehicle:

  def start(self):
    print("Vehicle started.")

class Car(Vehicle):

  def start(self):
    print("Car started")

class Bike(Vehicle):
  
  def start(self):
    print("Bike started")

c1 = Car()
b1 = Bike()

c1.start()
b1.start()


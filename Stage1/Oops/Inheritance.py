#Inheritance Defenition 
#Inheritance is a oop feature it allow one class to aquire the properties and method of another class, Promoting Code reuseablitiy

#Example Program 

class Person :
  
  def introduce(self):
    print("Iam a Person ")

class Student(Person):

  def study(self):
    print("Iam Studing")

s1 = Student()
s1.introduce()
s1.study()
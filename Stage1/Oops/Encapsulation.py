# Encapsulation defenition 
# Encapsulation is the process of combaining data and method into a single class . while restricting access to sensitive data 

#Example Program 
class Emp:

  def __init__(self,name,sal):
    
    self.name = name
    self.__salary=sal

  def addIncrement(self,amount):
    self.__salary += amount

  def showDetails(self):
    print(f"Name : {self.name}\nSalary : {self.__salary}")

emp1 = Emp("Shree",30000)
emp1.addIncrement(5000)
emp1.showDetails()

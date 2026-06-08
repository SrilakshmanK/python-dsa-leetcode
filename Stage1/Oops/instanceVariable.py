#Instance Variable Defenition
# Instance Variable is a Variable that belongs to a particular Object . It declare using self and each object a its own copy of variable .
#Example Program 

class Emp:

  def __init__(self,name,dept,sal):
    self.name = name 
    self.dept = dept
    self.sal = sal

  def show_details(self):
    print(f"Name : {self.name}\nSalary : {self.sal}\nDepartment : {self.dept}\n")

e1 = Emp("Shree","IT",40000)
e2 = Emp("Gojo","Sales",50000)

e1.show_details()
e2.show_details()
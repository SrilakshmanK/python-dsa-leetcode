#Instance Method Defenition
# Instance method is a method that belongs to an object . Operates on the instance variable of that object. it takes slef as a first parameter

# Example Program 

class BankAccount:

  def __init__(self,name,bal):
    
    self.name = name
    self.bal = bal

  def deposit(self,amount):

    self.bal += amount

  def withdraw(self,amount):

    self.bal -= amount

  def show_balance(self):

    print(f"Name : {self.name}\nBalance : {self.bal}")

Acc1 = BankAccount("Shree",10000)

Acc1.deposit(5000)
Acc1.withdraw(3000)

Acc1.show_balance()

  
      
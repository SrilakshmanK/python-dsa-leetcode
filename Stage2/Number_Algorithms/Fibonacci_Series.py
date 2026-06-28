n=int(input("Enter the value :"))

first = 0 
second = 1

if(n == 0): 
  print(first) 
  exit()

if(n ==1 ): 
  print(first)
  exit()
  
print(first)
print(second)

for i in range(n-2):
  next = first + second 
  print(next)  
  first = second 
  second = next 
  


n=int(input("Enter the value:"))

original=n
num=n
digit=0
total=0
count=0

while num!=0:
  count+=1
  num //= 10
  

while n!=0 :
  digit = n % 10 
  total = total + digit ** count
  n //= 10 
  
if total == original :
  print("It is an Armstrong Number.")
else:
  print("It is not an Armstrong Number.")


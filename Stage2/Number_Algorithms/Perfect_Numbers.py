n=int(input("Enter the value to check : "))

perfect_sum=0 

for i in range (1, n):
  if n % i == 0:
    perfect_sum += i
    
if n == perfect_sum : 
  print("Its a Perfect Number.")
else: 
  print("Its not a Perfect Number.")
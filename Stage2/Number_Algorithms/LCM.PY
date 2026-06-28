a = int(input("Enter the first number : "))
b = int(input("Enter the second  number : "))

if a < b:
  lar=b 
else: lar=a

lcm=lar

while True :
  if lcm % a == 0 and lcm % b == 0 :
   print(lcm)
   break
  lcm = lcm + lar 


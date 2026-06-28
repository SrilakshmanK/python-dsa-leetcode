a = int(input("Enter the first number : "))
b = int(input("Enter the second  number : "))

if a > b:
  limit=b 
else: limit=a

for i in range (1,limit+1):
  if a % i == 0 and b % i == 0 :
    hcf=i

print(hcf)

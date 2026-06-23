n= int(input("Enter the N value: "))

count = 0; 

if n == 0 : 
  print(1)
  exit() 
else:
  while n != 0 :
    count += 1
    n //= 10

print(count)


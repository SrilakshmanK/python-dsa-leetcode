n=int(input("Enter the value to check:"))

factor_count = 0 

for i in range( 1, n+1 ):
  if n % i == 0:
    factor_count += 1

print(factor_count)

if factor_count == 2 :
  print("Its a Prime Number.")
else:
  print("Its not a Prime Number.")
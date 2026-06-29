n=int(input("Enter the value : "))

result = 1 
original = n
strong_num=0


while n != 0:
  digit = n % 10

  for i in range( 1 , digit + 1):
    result = result * i
  
  strong_num += result
  result=1
  n //= 10
    
if original == strong_num :
  print("Its a Strong Number")
else:
  print("Its not a Strong Number")

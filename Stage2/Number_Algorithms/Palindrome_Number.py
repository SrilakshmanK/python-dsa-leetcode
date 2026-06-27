n = int(input("Enter a number to check whether it is a palindrome: "))

original = n 
digit = 0
reverse =0

while n !=0 :
  digit = n % 10
  reverse = reverse * 10 + digit
  n //= 10
  
if reverse == original :
 print("It is a palindrome.")
else:
  print("not a palindrome !!")
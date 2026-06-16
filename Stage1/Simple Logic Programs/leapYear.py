year = int(input("Enter the year : "))

if year <= 0:
  print("Invalid Input !!!")
elif year % 400 == 0 :
  print("Leap Year")
elif year % 4 == 0 and year % 100 != 0 :
  print("Leap Year")
else:
  print("Not a Leap year.")
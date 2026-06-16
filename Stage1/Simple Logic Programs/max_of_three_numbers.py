A = int(input("Enter the first num:"))
B = int(input("Enter the second num:"))
C = int(input("Enter the third num: "))

if A == B and B == C :
  print("All are equal. ")
elif A > B and A > C :
  print(f"{A} is the largest .")
elif B > C:
  print(f"{B} is the largest .")
else :
  print(f"{C} is the largest .")
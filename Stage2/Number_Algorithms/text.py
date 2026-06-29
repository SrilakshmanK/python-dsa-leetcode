n = int(input("Enter the Number : "))


for i in range (1, n+1):
  count_factor=0
  for j in range (1, n+1):
    
    if i % j == 0 :
      count_factor += 1
  if count_factor == 2:
    print(i)
    

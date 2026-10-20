n = int(input("Enter the number : "))

for row in range ( 1 , n + 1):
    for i in range (n - row):
        print(" ",end=" ")
    for j in range (1 , row + 1):
        print(f"{j}",end=" ")
    for k in range (row - 1 , 0 , -1):
        print(f"{k}",end=" ")
    print()
    

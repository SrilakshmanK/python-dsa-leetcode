n = int(input("Enter the number : "))

for row in range (1 , n + 1):
    for i in range(row - 1):
        print(" ",end="")
    for j in range(2 * (n - row) + 1):
        print("*",end="")
    print()



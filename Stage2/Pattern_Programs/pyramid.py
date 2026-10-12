n = int(input("Enter the number : "))

for row in range (1, n + 1):
    for i in range ( n - row):
        print(" ", end="")
    for j in range (2 * row -1):
        print("*",end="")
    print()
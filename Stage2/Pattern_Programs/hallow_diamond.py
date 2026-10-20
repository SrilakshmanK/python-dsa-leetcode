n = int(input("Enter the number : "))

for upper in range ( 1 , n + 1):
    for i in range (n - upper):
        print(" ",end="")

    print("*",end="")

    if  upper  > 1 :
        for j in range ( 2 * upper - 3):
            print(" ",end="")
        print("*",end="")

    print()


for lower in range (n - 1 , 0 , -1):
    for i in range ( n - lower):
        print(" ",end="")

    print("*",end="")

    if lower > 1 : 
        for j in range ( 2 * lower - 3):
            print(" ", end="")
        print("*",end="")

    print()
    
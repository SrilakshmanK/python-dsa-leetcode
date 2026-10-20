n = int(input("Enter the number : "))

for row in range (1 , n + 1):
    if row == 1 or row == n :
        for i in range (n):
            print("*",end="")
    else : 

        print("*",end="")

        if row > 1 :
            for j in range (n - 2):
                print(" ",end="")
            print("*",end="")
    print()
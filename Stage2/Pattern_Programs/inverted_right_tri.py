n = int(input("Enter the number : "))

for row in range (n , 0 , -1):
    for i in range(row):
        print("*", end=" ")
    print()

    
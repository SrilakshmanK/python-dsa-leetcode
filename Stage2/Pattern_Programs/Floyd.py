n = int(input("Enter the number : "))

num = 1

for row in range (1 , n + 1):
    for i in range (row):
        print(f"{num} ",end="")
        num += 1
    print()


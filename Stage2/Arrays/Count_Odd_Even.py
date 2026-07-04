arr = [ 3 , 2 , 4 , 1 , 5]


if len(arr) == 0:
    print("Empty array")
    exit()

odd_count=0
even_count=0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even Count : {even_count}")
print(f"Odd Count :  {odd_count}")
arr = [ 3 , 2 , 4 , 1 , 5]

if arr[0] < arr[1]:
    smallest=arr[0]
    second_smallest=arr[1]
else:
    smallest=arr[1]
    second_smallest=arr[0]

for i in range(2, len(arr)):
    if arr[i] < smallest:
        second_smallest=smallest
        smallest=arr[i]
    elif arr[i] < second_smallest:
        second_smallest=arr[i]

print(second_smallest)
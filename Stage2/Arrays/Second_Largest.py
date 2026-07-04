arr = [20, 10, 15]


if arr[0] > arr[1]:
    largest=arr[0]
    second_largest=arr[1]
else:
    largest = arr[1]
    second_largest = arr[0]


for i in range (2, len(arr)):
    if  arr[i] > largest :
        second_largest=largest
        largest  = arr[i]
    elif arr[i] > second_largest:
        second_largest = arr[i]
        

print(second_largest )
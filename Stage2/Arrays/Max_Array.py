arr = [-8, -5, -10, -3 , 1]

max_value = arr[0]

for i in range (1, len(arr)):
    if  arr[i] > max_value :
        max_value = arr[i]

print(max_value)
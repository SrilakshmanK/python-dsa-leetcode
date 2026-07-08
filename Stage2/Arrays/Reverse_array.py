arr = [1 , 3 , 4 , 9 , 7]

reverse_arr = []

if len(arr) == 0:
    print("Empty array")
    exit()

for i in range (len(arr)-1,-1,-1):
    reverse_arr.append(arr[i])

print(reverse_arr)
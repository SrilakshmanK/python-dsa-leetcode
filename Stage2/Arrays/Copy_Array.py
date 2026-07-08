arr = [1 , 3 , 4 , 9 , 7]

copy_arr = []

if len(arr) == 0:
    print("Empty array")
    exit()
    
for i in range (len(arr)):
    copy_arr.append(arr[i])


print("Original Array : ", arr)
print("Copy Array : ",copy_arr)